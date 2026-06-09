"""
Rebuilds the Autoneum "Target-Erreichung pro Stunde" report for work center
C04-011 (DE01) from the three source exports, reusing the original report's
exact layout and calculation basis (pausenbereinigt).

Sources:
  data_5.xlsx -> hourly target/produced per shift  -> Auslastung / Target-Erreichung
  data_6.xlsx -> production transactions (timestamps, PPH) -> Zykluszeit + Timelines
  data_7.xlsx -> downtime events                   -> Stillstandsanalyse

The original report (report.html) is fully driven by a single `const DATA = {...}`
constant. We recompute that constant for C04-011 and splice it back into the
untouched original HTML so layout, CSS and chart code are byte-for-byte identical.

Run: python3 generate_report5.py
"""
import json
import re
import statistics
from collections import defaultdict, Counter
from datetime import datetime

UP = '/root/.claude/uploads/d6ee9e7a-401b-540f-bd3b-e5e383e7ada3'
DATA5 = f'{UP}/6c8db3b1-data_5.xlsx'
DATA6 = f'{UP}/e8faf3d9-data_6.xlsx'
DATA7 = f'{UP}/6692e9e3-data_7.xlsx'
TEMPLATE = f'{UP}/7b438eb8-report.html'
OUT = '/home/user/NVH-2030/report_data5.html'

WC = 'C04-011'
EOL = 'C04-011_EOL - Vollautomat Nr. 187'
DATE_FROM = '20.05.2026'
DATE_TO = '09.06.2026'

import openpyxl

# ── break schedule (identical to original) ───────────────────────────────────
BREAKS = {
    0:('Verteilzeit',12,48), 4:('Verteilzeit',12,48), 8:('Verteilzeit',12,48),
    12:('Verteilzeit',12,48),16:('Verteilzeit',12,48),20:('Verteilzeit',12,48),
    2:('Pause',30,30), 10:('Pause',30,30), 18:('Pause',30,30),
    6:('Schichtwechsel',10,50), 14:('Schichtwechsel',10,50), 21:('Schichtwechsel',10,50),
}
def avail_min(h): return BREAKS[h][2] if h in BREAKS else 60
def target_factor(h): return avail_min(h) / 60.0

WD = ['Mo','Di','Mi','Do','Fr','Sa','So']               # Python weekday() order
def shift_of(hour): return 'S1' if 6 <= hour <= 13 else 'S2' if 14 <= hour <= 21 else 'S3'

def med(xs, d=1):
    return round(statistics.median(xs), d) if xs else 0

# ─────────────────────────────────────────────────────────────────────────────
# data_5 : capacity / Auslastung
# columns: 0 shift, 1 hour-label, 2 TARGET(pph), 3 PRODUCED, 4 REPORTED,
#          5 GOOD, 6 GOOD_FIRST, 7 GPF_RATIO, 8 NCR, ...
# ─────────────────────────────────────────────────────────────────────────────
rows5 = list(openpyxl.load_workbook(DATA5)['Sheet1'].iter_rows(values_only=True))[3:]

shift_dates = {}   # shift label -> datetime (for weekday / month)
def parse_shift_date(label):
    p = label.split(' ')
    mm = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    return datetime(2000 + int(p[3]), mm[p[2]], int(p[1].rstrip('.')))

records = []   # one per valid (shift,hour) row
for r in rows5:
    if not r[1]:
        continue
    target, produced = r[2], r[3]
    if target is None or target <= 0 or produced is None:
        continue
    hour = int(str(r[1]).split(' ')[0])
    shift_label = str(r[0])
    f = target_factor(hour)
    raw = produced / target * 100.0
    ber = raw / f
    eff = min(produced / target * 60.0, 60.0)
    if shift_label not in shift_dates:
        shift_dates[shift_label] = parse_shift_date(shift_label)
    records.append(dict(shift=shift_label, hour=hour, target=target, produced=produced,
                        raw=raw, ber=ber, eff=eff, reached=ber >= 100.0,
                        date=shift_dates[shift_label]))

# headline KPIs
all_ber  = [x['ber'] for x in records]
all_raw  = [x['raw'] for x in records]
all_eff  = [x['eff'] for x in records]
total_hours = len(records)
reached_pct = round(sum(x['reached'] for x in records) / total_hours * 100, 1)

shift_labels = set(x['shift'] for x in records)
shifts_s1 = len([s for s in shift_labels if s.startswith('S1')])
shifts_s2 = len([s for s in shift_labels if s.startswith('S2')])
shifts_s3 = len([s for s in shift_labels if s.startswith('S3')])

# by_hour
by_hour = []
start_minute_by_hour = defaultdict(list)   # filled later from data_6
hour_groups = defaultdict(list)
for x in records:
    hour_groups[x['hour']].append(x)

# by_pph
pph_groups = defaultdict(list)
for x in records:
    pph_groups[x['target']].append(x)

# by_shift (letter)
shift_groups = defaultdict(list)
for x in records:
    shift_groups[shift_of(x['hour'])].append(x)

# by_month
month_groups = defaultdict(list)
for x in records:
    month_groups[x['date'].strftime('%Y-%m')].append(x)

# by_weekday
weekday_groups = defaultdict(list)
for x in records:
    weekday_groups[WD[x['date'].weekday()]].append(x)

# distribution buckets
DIST = [('0-25%',0,25),('25-50%',25,50),('50-65%',50,65),('65-80%',65,80),
        ('80-90%',80,90),('90-100%',90,100),('100-120%',100,120),('>120%',120,1e9)]

# ─────────────────────────────────────────────────────────────────────────────
# data_6 : transactions -> production start minute, timelines, cycle time
# columns: 5 PRODUCED, 14 Sum of PPH, 17 Created On
# ─────────────────────────────────────────────────────────────────────────────
rows6 = list(openpyxl.load_workbook(DATA6)['Sheet1'].iter_rows(values_only=True))[3:]

# parts per (date, hour, 5-min block) and first-production minute per (date,hour)
blocks = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))  # date->hour->block->parts
pph_for = defaultdict(lambda: defaultdict(list))                     # date->hour->[pph]
first_min = defaultdict(dict)                                        # date->hour->minute
for x in rows6:
    ts, parts, pph = x[17], (x[5] or 0), x[14]
    if not ts:
        continue
    d, h = ts.date(), ts.hour
    blocks[d][h][ts.minute // 5] += parts
    if pph:
        pph_for[d][h].append(pph)
    if parts > 0:
        if h not in first_min[d] or ts.minute < first_min[d][h]:
            first_min[d][h] = ts.minute

# production start minute per hour (median across days)
for d in first_min:
    for h, m in first_min[d].items():
        start_minute_by_hour[h].append(m)

# cycle time: seconds/part on full production blocks (parts >= 60% of block target)
spp_overall = []
spp_by_hour = defaultdict(list)
for d in blocks:
    for h in blocks[d]:
        pph = statistics.median(pph_for[d][h]) if pph_for[d][h] else 189
        block_target = pph / 12.0
        for bi, parts in blocks[d][h].items():
            if parts >= 0.6 * block_target and parts > 0:
                spp = 300.0 / parts
                spp_overall.append(spp)
                spp_by_hour[h].append(spp)
mode_pph = Counter(x[14] for x in rows6 if x[14]).most_common(1)[0][0]
expected_ct = round(3600.0 / mode_pph, 1)
cycle_time = {
    'overall_median': med(spp_overall),
    'expected_ct': expected_ct,
    'by_hour': [{'hour': h, 'median_ct': med(spp_by_hour[h]) if spp_by_hour[h] else expected_ct}
                for h in range(24)],
}

# build by_hour now that start minutes are known
for h in range(24):
    g = hour_groups.get(h, [])
    nm, _, am = (BREAKS[h] if h in BREAKS else (None, 0, 60))
    sm = start_minute_by_hour.get(h, [])
    by_hour.append({
        'hour': h,
        'count': len(g),
        'reached': sum(x['reached'] for x in g),
        'reached_pct': round(sum(x['reached'] for x in g) / len(g) * 100, 1) if g else 0,
        'median_cap': med([x['ber'] for x in g]) if g else 0,
        'median_raw_cap': med([x['raw'] for x in g]) if g else 0,
        'median_eff_min': med([x['eff'] for x in g]) if g else 0,
        'median_start': round(statistics.median(sm), 1) if sm else 0,
        'target_factor': round(target_factor(h), 4),
        'break_name': nm,
        'avail_min': am,
    })

by_shift = [{'shift': s, 'count': len(shift_groups[s]),
             'reached_pct': round(sum(x['reached'] for x in shift_groups[s]) / len(shift_groups[s]) * 100, 1),
             'median_cap': med([x['ber'] for x in shift_groups[s]])}
            for s in ['S1','S2','S3'] if shift_groups[s]]

by_month = [{'month': m,
             'count': len(month_groups[m]),
             'reached_pct': round(sum(x['reached'] for x in month_groups[m]) / len(month_groups[m]) * 100, 1),
             'median_cap': med([x['ber'] for x in month_groups[m]])}
            for m in sorted(month_groups)]

by_weekday = [{'weekday': w, 'median_cap': med([x['ber'] for x in weekday_groups[w]])}
              for w in WD if w in weekday_groups]

by_pph = [{'pph': int(p),
           'count': len(pph_groups[p]),
           'reached_pct': round(sum(x['reached'] for x in pph_groups[p]) / len(pph_groups[p]) * 100, 1),
           'median_cap': med([x['ber'] for x in pph_groups[p]]),
           'avg_produced': round(sum(x['produced'] for x in pph_groups[p]) / len(pph_groups[p]), 1)}
          for p in sorted(pph_groups, key=lambda p: -len(pph_groups[p]))]

distribution = []
for label, lo, hi in DIST:
    distribution.append({'label': label, 'count': sum(1 for x in records if lo <= x['ber'] < hi)})

# timelines: 3 example days with broadest hour coverage
day_cov = sorted(blocks.keys(), key=lambda d: -len(blocks[d]))[:3]
day_cov = sorted(day_cov)
timelines = []
for d in day_cov:
    hrs = []
    for h in range(24):
        if h not in blocks[d]:
            continue
        bl = [blocks[d][h].get(i, 0) for i in range(12)]
        pph = int(statistics.median(pph_for[d][h])) if pph_for[d][h] else mode_pph
        total = sum(bl)
        hrs.append({'hour': h, 'blocks': bl, 'pph': pph,
                    'pct': round(total / pph * 100) if pph else 0})
    timelines.append({'date': d.strftime('%d.%m.%Y'), 'weekday': WD[d.weekday()], 'hours': hrs})

workcenter = {
    'eol': EOL,
    'total_hours': total_hours,
    'reached_pct': reached_pct,
    'total_shifts': len(shift_labels),
    'shifts_s1': shifts_s1, 'shifts_s2': shifts_s2, 'shifts_s3': shifts_s3,
    'median_capacity': med(all_ber),
    'median_raw_capacity': med(all_raw),
    'median_effective_min': int(round(med(all_eff))),
    'by_hour': by_hour, 'by_shift': by_shift, 'by_month': by_month,
    'by_weekday': by_weekday, 'by_pph': by_pph, 'distribution': distribution,
    'timelines': timelines,
}

# ─────────────────────────────────────────────────────────────────────────────
# data_7 : downtime
# columns: 1 REASON TYPE, 2 REASON CLASS, 3 REASON CODE, 5 Created On,
#          6 Start, 7 End, 8 DURATION(min)
# ─────────────────────────────────────────────────────────────────────────────
rows7 = list(openpyxl.load_workbook(DATA7)['Sheet1'].iter_rows(values_only=True))[3:]

events = []
for x in rows7:
    rtype, rclass, rcode, start, end, dur = x[1], x[2], x[3], x[6], x[7], x[8]
    dur = dur or 0
    events.append(dict(rtype=rtype, reason=rcode, start=start, end=end, dur=dur))

durs = [e['dur'] for e in events]
unplanned = [e for e in events if e['rtype'] == 'Unplanned Downtime']
planned   = [e for e in events if e['rtype'] != 'Unplanned Downtime']

# by_reason
reason_g = defaultdict(list)
for e in events:
    reason_g[e['reason']].append(e)
by_reason = sorted(
    [{'reason': r, 'count': len(g), 'total_min': float(sum(e['dur'] for e in g))}
     for r, g in reason_g.items()],
    key=lambda r: -r['total_min'])

# distribution by duration
DDIST = [('0-3 min',0,3),('3-5 min',3,5),('5-10 min',5,10),('10-15 min',10,15),
         ('15-30 min',15,30),('30-60 min',30,60),('60-120 min',60,120),
         ('120-240 min',120,240),('>240 min',240,1e9)]
dt_distribution = []
for label, lo, hi in DDIST:
    g = [e for e in events if lo <= e['dur'] < hi]
    dt_distribution.append({'label': label, 'count': len(g),
                            'total_min': float(sum(e['dur'] for e in g))})

# by_hour / by_shift / by_weekday (keyed on start time)
dh = defaultdict(list); ds = defaultdict(list); dw = defaultdict(list)
for e in events:
    if not e['start']:
        continue
    dh[e['start'].hour].append(e['dur'])
    ds[shift_of(e['start'].hour)].append(e['dur'])
    dw[WD[e['start'].weekday()]].append(e['dur'])

dt_by_hour = [{'hour': h, 'count': len(dh[h]), 'total_min': float(sum(dh[h])),
               'avg_min': round(sum(dh[h]) / len(dh[h]), 1) if dh[h] else 0,
               'median_min': med(dh[h]) if dh[h] else 0} for h in range(24)]
dt_by_shift = [{'shift': s, 'count': len(ds[s]), 'total_min': float(sum(ds[s])),
                'avg_min': round(sum(ds[s]) / len(ds[s]), 1) if ds[s] else 0,
                'median_min': med(ds[s]) if ds[s] else 0}
               for s in ['S1','S2','S3'] if ds[s]]
dt_by_weekday = [{'weekday': w, 'count': len(dw[w]),
                  'avg_min': round(sum(dw[w]) / len(dw[w]), 1) if dw[w] else 0}
                 for w in WD if w in dw]

# top 10 longest
top = sorted([e for e in events if e['start'] and e['end']], key=lambda e: -e['dur'])[:10]
top10 = [{'start': e['start'].strftime('%d.%m.%Y %H:%M'),
          'end': e['end'].strftime('%d.%m.%Y %H:%M'),
          'duration_min': float(e['dur']), 'reason': e['reason'],
          'reason_type': e['rtype'], 'shift': shift_of(e['start'].hour),
          'weekday': WD[e['start'].weekday()]} for e in top]

downtime = {
    'total_events': len(events),
    'total_minutes': float(sum(durs)),
    'total_hours': round(sum(durs) / 60, 1),
    'median_min': med(durs),
    'avg_min': round(sum(durs) / len(durs), 1) if durs else 0,
    'max_min': float(max(durs)) if durs else 0,
    'threshold_sec': 0,
    'unplanned_count': len(unplanned),
    'unplanned_min': float(sum(e['dur'] for e in unplanned)),
    'planned_count': len(planned),
    'planned_min': float(sum(e['dur'] for e in planned)),
    'by_reason': by_reason,
    'distribution': dt_distribution,
    'by_hour': dt_by_hour,
    'by_shift': dt_by_shift,
    'by_weekday': dt_by_weekday,
    'top10': top10,
}

# ─────────────────────────────────────────────────────────────────────────────
# assemble DATA and splice into the original HTML
# ─────────────────────────────────────────────────────────────────────────────
DATA = {
    'workcenter': {WC: workcenter},
    'cycle_time': {WC: cycle_time},
    'downtime':   {WC: downtime},
    'break_schedule': {str(h): {'name': BREAKS[h][0], 'break_min': BREAKS[h][1], 'avail_min': BREAKS[h][2]}
                       for h in BREAKS},
    'date_from': DATE_FROM,
    'date_to': DATE_TO,
}

with open(TEMPLATE, encoding='utf-8') as f:
    html = f.read()

new_data_line = 'const DATA = ' + json.dumps(DATA, ensure_ascii=False) + ';'
html, n = re.subn(r'const DATA = \{.*?\};(?=\s*\n)', lambda m: new_data_line, html, count=1, flags=re.DOTALL)
assert n == 1, f'DATA constant not replaced (n={n})'

# refocus title/header on the single work center + new period
html = html.replace('<title>Target-Erreichung pro Stunde | DE01</title>',
                    '<title>Target-Erreichung pro Stunde | DE01 C04-011</title>')
html = html.replace('Werk DE01 | 8 Work Center | Pausenbereinigt',
                    'Werk DE01 | Work Center C04-011 (Vollautomat Nr. 187) | Pausenbereinigt')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

# verify the embedded JSON parses back
m = re.search(r'const DATA = (\{.*?\});(?=\s*\n)', html, re.DOTALL)
json.loads(m.group(1))

print(f'OK -> {OUT} ({len(html):,} bytes)')
print(f'  shifts={workcenter["total_shifts"]} (S1:{shifts_s1} S2:{shifts_s2} S3:{shifts_s3}) hours={total_hours}')
print(f'  reached={reached_pct}%  bereinigt={workcenter["median_capacity"]}%  roh={workcenter["median_raw_capacity"]}%  eff={workcenter["median_effective_min"]}min')
print(f'  cycle: median={cycle_time["overall_median"]}s expected={expected_ct}s')
print(f'  downtime: {downtime["total_events"]} events, {downtime["total_hours"]}h '
      f'(unplanned {downtime["unplanned_count"]}/{round(downtime["unplanned_min"]/60,1)}h, '
      f'planned {downtime["planned_count"]}/{round(downtime["planned_min"]/60,1)}h)')
print(f'  timelines: {[t["date"] for t in timelines]}')
