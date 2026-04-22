"""
Generate Technology Factsheet HTML pages for all recommended technologies.
Each page: ~200 lines, Autoneum CI, same template structure.
Output: 06_Technologie_Factsheets/
"""
import os

BASE = r"c:\Users\122798\OneDrive - Autoneum\Organized_Workspace\05_Projects\Factory_Layouts\NVH 2030"
OUT  = os.path.join(BASE, "06_Technologie_Factsheets")

CSS = """<style>
:root{--g:#B8C400;--dg:#99CC00;--o:#E86A10;--b:#69BBFF;--dk:#2d2d2d;--gy:#666;--lg:#DCDCDC;--vlg:#F4F4F4;--wh:#FFF;--pg:#EDF0BF}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial,Calibri,sans-serif;background:var(--wh);color:#000;line-height:1.6;font-size:12px}
@media print{body{font-size:9.5px}.hero{padding:20px 25px!important}.container{padding:10px 20px!important}}
.hero{background:linear-gradient(135deg,#1a1a1a 0%,#2d2d2d 60%,#3a3a3a 100%);color:var(--wh);padding:35px 50px;position:relative}
.hero::before{content:'';position:absolute;top:-40%;right:-15%;width:400px;height:400px;background:radial-gradient(circle,rgba(184,196,0,.12) 0%,transparent 70%);border-radius:50%}
.hero-tag{font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--g);margin-bottom:6px}
.hero h1{font-size:24px;font-weight:700;line-height:1.2;margin-bottom:8px}
.hero h1 span{color:var(--g)}
.hero-sub{font-size:12px;opacity:.85;max-width:650px;margin-bottom:10px}
.hero-meta{display:flex;gap:12px;font-size:9px;opacity:.5;flex-wrap:wrap}
.badge{display:inline-block;padding:2px 8px;border-radius:3px;font-size:9px;font-weight:700;margin-left:6px}
.b-phase{background:var(--g);color:#000}
.b-cost{background:var(--o);color:var(--wh)}
.kn-bar{display:grid;grid-template-columns:repeat(4,1fr);background:var(--wh);border-radius:8px;box-shadow:0 3px 12px rgba(0,0,0,.07);margin:-20px 30px 18px;position:relative;z-index:10;border:1px solid var(--lg)}
.kn{padding:14px 10px;text-align:center;border-right:1px solid var(--lg)}
.kn:last-child{border-right:none}
.kn .v{font-size:18px;font-weight:700;color:#000;line-height:1;margin-bottom:2px}
.kn .v span{color:var(--g)}
.kn .l{font-size:8px;color:var(--gy);text-transform:uppercase;letter-spacing:.5px}
.container{max-width:960px;margin:0 auto;padding:18px 40px}
.sh{margin-bottom:14px}
.sh .tag{font-size:8px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g);margin-bottom:3px}
.sh h2{font-size:18px;font-weight:700;color:var(--g)}
.sh p{color:var(--gy);margin-top:2px;font-size:11px}
.box{border-radius:6px;padding:16px 20px;margin-bottom:18px}
.box h3{font-size:12px;font-weight:700;margin-bottom:6px}
.box ul{list-style:none;padding:0}
.box li{padding:2px 0 2px 16px;position:relative;font-size:10.5px}
.box li::before{content:'';position:absolute;left:0;top:6px;width:7px;height:7px;border-radius:2px}
.box-green{background:#F7F9E6;border-left:4px solid var(--g)}
.box-green h3{color:var(--dg)}
.box-green li::before{background:var(--g)}
.box-dark{background:#1a1a1a;border-left:4px solid var(--g);color:#ddd}
.box-dark h3{color:var(--g)}
.box-dark li::before{background:var(--g)}
.box-warn{background:#FFF5EB;border-left:4px solid var(--o)}
.box-warn h3{color:var(--o)}
.box-warn li::before{background:var(--o)}
.box-blue{background:#EBF5FF;border-left:4px solid var(--b)}
.box-blue h3{color:#2E75B6}
.box-blue li::before{background:var(--b)}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:10px}
th{background:var(--g);color:var(--wh);padding:6px 8px;text-align:left;font-weight:700;font-size:8.5px;text-transform:uppercase;letter-spacing:.4px}
th:first-child{border-radius:4px 0 0 0}th:last-child{border-radius:0 4px 0 0}
td{padding:6px 8px;border-bottom:1px solid var(--lg)}
tr:nth-child(even){background:var(--vlg)}
tr:hover{background:var(--pg)}
.footer{text-align:center;padding:14px;border-top:1px solid var(--lg);margin-top:10px}
.footer p{font-size:8px;color:var(--gy);font-style:italic}
</style>"""

def page(title, tag, subtitle, phase, cost_label, kn, overview, how_it_works, auxiliaries, hardware, software, gundernhausen, sources):
    kn_html = ""
    for v, l in kn:
        kn_html += f'<div class="kn"><div class="v">{v}</div><div class="l">{l}</div></div>\n'

    def li_list(items):
        return "\n".join(f"        <li>{i}</li>" for i in items)

    def table_rows(rows):
        return "\n".join(f'            <tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in rows)

    src_rows = "\n".join(f'            <tr><td><a href="{u}" style="color:var(--b);">{n}</a></td><td>{d}</td></tr>' for n, u, d in sources)

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} – Technology Factsheet</title>
    {CSS}
</head>
<body>
<div class="hero">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
        <div>
            <div class="hero-tag">{tag}</div>
            <h1>{title} <span class="badge b-phase">{phase}</span> <span class="badge b-cost">{cost_label}</span></h1>
        </div>
        <div style="text-align:right;">
            <div style="font-size:18px;font-weight:700;color:var(--g);letter-spacing:1px;">AUTONEUM</div>
            <div style="font-size:9px;font-style:italic;color:var(--o);">- CONFIDENTIAL -</div>
        </div>
    </div>
    <p class="hero-sub">{subtitle}</p>
    <div class="hero-meta">
        <span>Autoneum Germany GmbH – Gundernhausen</span><span>|</span><span>March 2026</span><span>|</span><span>Annex to MJF Deep-Dive</span>
    </div>
</div>

<div class="kn-bar">
{kn_html}</div>

<div class="container">

<div class="sh"><div class="tag">Overview</div><h2>What It Does</h2></div>
<div class="box box-dark">
    <h3>{overview[0]}</h3>
    <ul>
{li_list(overview[1])}
    </ul>
</div>

<div class="sh"><div class="tag">How It Works</div><h2>Process &amp; Principle</h2></div>
<div class="box box-green">
    <h3>{how_it_works[0]}</h3>
    <ul>
{li_list(how_it_works[1])}
    </ul>
</div>

<div class="sh"><div class="tag">Requirements</div><h2>Auxiliaries &amp; Infrastructure</h2></div>
<div style="background:var(--wh);border-radius:8px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.05);margin-bottom:18px;border:1px solid var(--lg);">
    <table>
        <thead><tr><th>Auxiliary</th><th>Specification</th><th>Status at Gundernhausen</th></tr></thead>
        <tbody>
{table_rows(auxiliaries)}
        </tbody>
    </table>
</div>

<div class="sh"><div class="tag">Hardware</div><h2>Required Hardware</h2></div>
<div style="background:var(--wh);border-radius:8px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.05);margin-bottom:18px;border:1px solid var(--lg);">
    <table>
        <thead><tr><th>Component</th><th>Model / Specification</th><th>Est. Cost</th></tr></thead>
        <tbody>
{table_rows(hardware)}
        </tbody>
    </table>
</div>

<div class="sh"><div class="tag">Software</div><h2>Required Software</h2></div>
<div style="background:var(--wh);border-radius:8px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.05);margin-bottom:18px;border:1px solid var(--lg);">
    <table>
        <thead><tr><th>Software</th><th>Function</th><th>Est. Cost</th></tr></thead>
        <tbody>
{table_rows(software)}
        </tbody>
    </table>
</div>

<div class="sh"><div class="tag">Gundernhausen Fit</div><h2>Relevance &amp; Recommendation</h2></div>
<div class="box box-blue">
    <h3>{gundernhausen[0]}</h3>
    <ul>
{li_list(gundernhausen[1])}
    </ul>
</div>

<div class="sh"><div class="tag">Sources</div><h2>Key References</h2></div>
<div style="background:var(--wh);border-radius:8px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.05);margin-bottom:18px;border:1px solid var(--lg);">
    <table>
        <thead><tr><th>Source</th><th>Topic</th></tr></thead>
        <tbody>
{src_rows}
        </tbody>
    </table>
</div>

</div>
<div class="footer">
    <p>&copy; 2026 Autoneum Germany GmbH – Gundernhausen | - CONFIDENTIAL - | Technology Factsheet | Author: J.R.E. Glawion</p>
</div>
</body>
</html>"""

# ══════════════════════════════════════════════════════════════
# TECHNOLOGY DEFINITIONS
# ══════════════════════════════════════════════════════════════

techs = []

# 1 — HP MJF 5200
techs.append(("01_HP_MJF_5200", page(
    title="HP Jet Fusion <span>5200</span> — Multi Jet Fusion",
    tag="Technology Factsheet 01 • Core 3D Printer",
    subtitle="Industrial powder-bed fusion 3D printer. Voxel-level control via fusing and detailing agents at 1200 dpi. Proven in automotive serial production (GM, BMW, VW). Lights-out capable.",
    phase="PHASE 1", cost_label="€370–420k",
    kn=[("380<span>³mm</span>","Build Volume"),("1200<span>dpi</span>","XY Resolution"),("550<span>+/wk</span>","Parts Throughput"),("80<span>%</span>","Powder Reuse")],
    overview=("HP Multi Jet Fusion 5200 — Industrial 3D Printer",[
        "Powder-bed fusion process: 80µm PA12 layers fused by IR energy via chemical agents at 1200 dpi",
        "Build volume: 380 × 284 × 380 mm (41 liters) — hundreds of parts per build via 3D nesting",
        "Build speed: ~2,800 cm³/hr — full build in 12–14 hours, continuous with 3 rotating build units",
        "No support structures needed — parts float in powder bed, enabling complex geometries for free",
        "Materials: PA12, PA11, PP, TPU, PA12-GB, PA12-FR — all HP-certified (closed RFID ecosystem)",
        "170+ million parts produced on MJF globally as of 2025 — automotive is #1 segment (23%)",
    ]),
    how_it_works=("4-Step Layer Process",[
        "<strong>Step 1 — Recoat:</strong> Powder spreader deposits 80µm PA12 layer across build area",
        "<strong>Step 2 — Agent Jetting:</strong> Thermal inkjet heads deposit fusing agent (where part is) + detailing agent (at boundaries)",
        "<strong>Step 3 — IR Fusing:</strong> Infrared lamps pass over the full layer — fusing agent absorbs energy, melting powder into solid part",
        "<strong>Step 4 — Repeat:</strong> Platform lowers 80µm, process repeats. ~4,750 layers for a full-height build",
        "After build: build unit moves to Processing Station for controlled cooling (4–12h) + depowdering (10–30 min)",
    ]),
    auxiliaries=[
        ("Electrical","3-phase 400V, 32A — ~10 kW average draw","Available"),
        ("Compressed Air","6–8 bar, clean dry air (ISO 8573-1 Class 1.4.1)","Available"),
        ("HVAC / Ventilation","6–10 air changes/hr, local exhaust at powder handling, HEPA H13/H14","Needs installation"),
        ("Floor Space","75–85 m² complete cell (printer + processing + post-proc + QC)","Halle 3 available"),
        ("ATEX Zone 22","Combustible dust area — ESD flooring, grounding, ATEX Cat 3D equipment","Assessment needed"),
        ("Powder Storage","Climate-controlled silo (18–25°C, <60% RH) with anti-bridging agitator","Needs designation"),
        ("Network","Gigabit Ethernet for HP 3D Center cloud monitoring","Available"),
        ("Ceiling Height","Minimum 3.0 m clear","Available"),
    ],
    hardware=[
        ("HP Jet Fusion 5200 Printer","Incl. 1 build unit, print carriage, IR lamps, agent delivery","€370–420k"),
        ("HP Processing Station","Cooling + depowdering + powder sieving/recycling (typically bundled)","Incl. in system"),
        ("Additional Build Units (×2)","Enable 24/7 rotation: one prints, one cools, one unpacks","€90–110k"),
        ("Natural Cooling Unit","Optional accelerated cooling for build units","€18–22k"),
        ("Bead Blast Cabinet","Post-processing: surface finish, residual powder removal","€10–20k"),
        ("ATEX Vacuum Cleaner","Ruwac/Nilfisk ATEX-rated for powder cleanup","€3–5k"),
        ("HEPA Dust Extraction","Local exhaust at depowdering station — Keller/Nederman","€8–15k"),
    ],
    software=[
        ("HP SmartStream 3D Build Manager","Job preparation, nesting, build queue, cost estimation","Included"),
        ("HP 3D Process Control","Real-time thermal mapping, build-to-build consistency, SPC","Included"),
        ("HP 3D Center","Cloud fleet management, remote monitoring, analytics","Included"),
        ("Materialise Magics (optional)","Advanced nesting, STL repair, orientation optimization","€10–20k/yr"),
        ("Apriso MES Integration","Connect print queue to Kanban triggers via REST API","Internal dev"),
    ],
    gundernhausen=("Why MJF 5200 for Gundernhausen",[
        "<strong>Phase 1 (Month 1–3):</strong> Order 1× HP 5200 system + 2 extra build units = €480–550k total",
        "<strong>Evonik proximity:</strong> 17 km to Hanau R&D, 300 km to Marl powder plant — unique supply chain advantage",
        "<strong>Halle 3:</strong> Cleared by NVH 2030 Phase A — dedicated innovation space, no interference with foam production",
        "<strong>Print Hub:</strong> Serve 10+ European Autoneum locations with next-day delivery from central Germany",
        "<strong>Payback:</strong> 12–24 months at moderate utilization — fastest ROI of all 11 evaluated investment options",
        "<strong>Alternative:</strong> Evaluate Farsoon SLS alongside for open-material powder supply from Evonik INFINAM direct",
    ]),
    sources=[
        ("HP Official — Jet Fusion 5200","https://www.hp.com/us-en/printers/3d-printers/products/multi-jet-fusion-5200.html","Specifications"),
        ("HP Automotive Gallery","https://www.hp.com/us-en/printers/3d-printers/industries/transportation.html","Case Studies"),
        ("3DPrint.com — GM Case Study","https://3dprint.com/291335/gm-turns-to-hps-mjf-3d-printing-for-fast-part-production/","60k parts"),
    ],
)))

# 2 — Zoo Design Studio + Zookeeper
techs.append(("02_Zoo_Design_Studio", page(
    title="Zoo Design Studio + <span>Zookeeper</span>",
    tag="Technology Factsheet 02 • AI-Powered CAD",
    subtitle="AI-native CAD platform with conversational Zookeeper agent. Generates manufacturing-ready B-Rep geometry (STEP files) from natural language descriptions. Built on KCL parametric language.",
    phase="PHASE 2", cost_label="€0–2.8k/yr",
    kn=[("B-Rep","Output Format (STEP)"),("KCL","Parametric Language"),("v1.1","GA Jan 2026"),("Free","20 min/mo included")],
    overview=("Zoo Design Studio — AI-Native CAD Platform",[
        "Desktop CAD application built on Zoo's high-performance geometry engine (Rust-based, GPU-accelerated)",
        "Zookeeper: conversational AI agent that writes KCL code (Zoo's parametric design language) from natural language",
        "Generates B-Rep surfaces (not meshes) — output is editable STEP files importable into any CAD program",
        "Agent loop: Plan → Act (write KCL) → Observe (render, check geometry) → Update → Repeat until correct",
        "Engineering tools: center of mass, volume, surface area, multi-view snapshots for design review",
        "Roadmap: multimodal (image input), reverse engineering (STEP→KCL), fleet management (multi-agent)",
    ]),
    how_it_works=("Conversational Design Workflow",[
        "<strong>Step 1:</strong> Operator describes part in natural language: 'Create a bracket with 4 M6 mounting holes, 80mm wide, 3mm wall thickness'",
        "<strong>Step 2:</strong> Zookeeper generates KCL parametric code — dimensions as variables, fully editable",
        "<strong>Step 3:</strong> Agent renders geometry, inspects from multiple angles, checks for errors",
        "<strong>Step 4:</strong> If issues detected: agent debugs and regenerates. If OK: exports STEP file",
        "<strong>Step 5:</strong> STEP file imported into HP SmartStream for nesting and printing on MJF",
        "Parametric: changing one dimension (e.g., width=100mm) regenerates entire model automatically",
    ]),
    auxiliaries=[
        ("Internet Connection","Required for Zookeeper AI reasoning (cloud-based)","Available"),
        ("Modern PC/Laptop","GPU-accelerated rendering — any modern workstation","Existing operator PCs"),
        ("File Storage","STEP/KCL files stored in digital catalog (Würth DIS or local)","Available"),
    ],
    hardware=[
        ("Workstation PC","Any modern PC with GPU (existing operator stations)","€0 (existing)"),
        ("Display","Standard monitor — no special requirements","€0 (existing)"),
    ],
    software=[
        ("Zoo Design Studio","Desktop CAD application — free download","Free"),
        ("Zookeeper AI Agent","Conversational design assistant — 20 min/mo free tier","Free / €1k/yr per seat"),
        ("Zoo ML API (optional)","Text-to-CAD API for automated pipelines","$0.0083/sec usage"),
    ],
    gundernhausen=("Recommendation for Gundernhausen (3 Workcells)",[
        "<strong>Start free:</strong> 20 min/mo × 3 seats = 60 min Zookeeper reasoning per month — sufficient for initial evaluation",
        "<strong>Use case:</strong> Operators describe needed jigs/brackets → Zookeeper generates parametric STEP → validate → print on MJF",
        "<strong>Annual cost:</strong> Free tier or ~€2.8k/yr for 3 Annual seats — negligible vs €400k printer",
        "<strong>Combine with Claude + CadQuery</strong> for parts requiring Python scripting flexibility",
        "<strong>Phase 3:</strong> Integrate with nTopology for lattice-optimized NVH parts",
    ]),
    sources=[
        ("Zoo.dev — Zookeeper Research","https://zoo.dev/research/zookeeper","Agent architecture"),
        ("Zoo.dev — Pricing","https://zoo.dev/design-studio-pricing","License costs"),
        ("Zoo.dev — Text-to-CAD","https://zoo.dev/text-to-cad","ML API"),
    ],
)))

# 3 — Claude + CadQuery
techs.append(("03_Claude_CadQuery", page(
    title="Claude Opus + <span>CadQuery</span>",
    tag="Technology Factsheet 03 • LLM Parametric CAD",
    subtitle="Use Anthropic's Claude Opus 4 LLM to generate Python CadQuery scripts that produce manufacturing-ready STEP/STL files. ~85% executable rate on first attempt. Real CAD kernel (OpenCASCADE).",
    phase="PHASE 1–2", cost_label="~€200/mo API",
    kn=[("85<span>%</span>","First-Attempt Success"),("STEP","Output (OpenCASCADE)"),("Python","CadQuery API"),("0","License Cost (OSS)")],
    overview=("Claude + CadQuery — LLM-Generated Parametric CAD",[
        "Claude Opus generates Python CadQuery scripts from natural language part descriptions",
        "CadQuery is open-source, Python-based, runs on OpenCASCADE kernel — fillets, chamfers, booleans work correctly",
        "Output: STEP files (industry standard), also STL for direct 3D printing",
        "Dimensions as Python variables → parametric: change one value, regenerate entire model",
        "Academic research (Text-to-CadQuery, 2025): best models achieve 69% exact match, 85%+ executable with feedback loops",
        "No license cost for CadQuery (MIT license) — only Claude API usage cost",
    ]),
    how_it_works=("Text → Python → STEP Pipeline",[
        "<strong>Step 1:</strong> Operator describes part: 'Spray nozzle adapter, 25mm OD, 12mm ID, 3 mounting tabs at 120°'",
        "<strong>Step 2:</strong> Claude generates Python CadQuery script with parametric variables",
        "<strong>Step 3:</strong> Script executes locally — CadQuery builds geometry on OpenCASCADE kernel",
        "<strong>Step 4:</strong> If error: Claude reviews traceback, fixes code, re-executes (feedback loop)",
        "<strong>Step 5:</strong> Export STEP → import to HP SmartStream → nest → print",
        "FDM/MJF best practices encodable: min wall 2mm, 0.3mm hole clearance, chamfers on bottom edges",
    ]),
    auxiliaries=[
        ("Python 3.10+","CadQuery runtime environment","Install via pip"),
        ("Internet Connection","Required for Claude API calls","Available"),
        ("Claude API Key","Anthropic API access for code generation","Sign up at anthropic.com"),
    ],
    hardware=[
        ("Any PC/Laptop","Python + CadQuery runs on any modern system","€0 (existing)"),
        ("No GPU required","CadQuery is CPU-based (OpenCASCADE)","€0"),
    ],
    software=[
        ("CadQuery","Open-source parametric CAD library (pip install cadquery)","Free (MIT)"),
        ("Claude API (Opus 4)","LLM for code generation — ~$15/M input, $75/M output tokens","~€150–250/mo"),
        ("Claude Code CLI (optional)","Interactive coding assistant with CadQuery skill","Included with API"),
        ("CQ-Editor (optional)","Visual CadQuery IDE for preview/debug","Free (OSS)"),
        ("FreeCAD (optional)","STEP file viewer and manual editing","Free (OSS)"),
    ],
    gundernhausen=("Recommendation for Gundernhausen",[
        "<strong>Immediate start:</strong> Install CadQuery on operator PCs today — zero cost, zero approval needed",
        "<strong>Simple workflow:</strong> Operator opens Claude → describes part → gets Python script → runs → exports STEP",
        "<strong>Best for:</strong> Simple-to-medium jigs, brackets, clips, cable management, sensor mounts",
        "<strong>Limitation:</strong> Threads, snap fits, complex assemblies need human validation — always check critical dims",
        "<strong>Combine with Zoo Zookeeper</strong> for complex parametric parts needing engineering review",
        "<strong>Cost:</strong> ~€200/mo API — generates 100+ part designs per month at that budget",
    ]),
    sources=[
        ("Towards AI — Claude + CadQuery","https://medium.com/@nchourrout/i-taught-claude-to-design-3d-printable-parts-heres-how-675f644af78a","Tutorial"),
        ("arXiv — Text-to-CadQuery","https://arxiv.org/html/2505.06507v1","Academic benchmark"),
        ("CadQuery GitHub","https://github.com/CadQuery/cadquery","Open-source library"),
    ],
)))

# 4 — DyeMansion Post-Processing
techs.append(("04_DyeMansion_PostProcessing", page(
    title="DyeMansion <span>Post-Processing</span>",
    tag="Technology Factsheet 04 • Automated Finishing",
    subtitle="Automated depowdering, dyeing, and vapor smoothing for MJF parts. Industry standard 'Print-to-Product' workflow endorsed by HP. Fully automated batch processing — no operator needed during cycle.",
    phase="PHASE 2–3", cost_label="€50–120k",
    kn=[("10<span>min</span>","Depowder Cycle"),("ISO","Certified Colors"),("Auto","Unattended Cycles"),("HP","Endorsed Partner")],
    overview=("DyeMansion — Print-to-Product Finishing",[
        "Complete automated post-processing ecosystem for powder-bed 3D printed parts (MJF, SLS, HSS)",
        "Three core processes: <strong>Clean</strong> (depowdering) → <strong>Smooth</strong> (surface finish) → <strong>Color</strong> (dyeing)",
        "All systems are fully enclosed, batch-automated — load parts, close door, press start, walk away",
        "ISO-certified colors for end-use applications — automotive, medical, consumer products",
        "Formally endorsed by HP as the recommended post-processing partner for MJF",
        "Used by BMW, GM, Jabil, and all major MJF service bureaus globally",
    ]),
    how_it_works=("Three-Stage Finishing",[
        "<strong>Powershot C (Clean):</strong> Automated PolyShot Cleaning — proprietary media removes residual powder from part surfaces. 10 min per build-load. Replaces manual bead blasting.",
        "<strong>Powershot S (Smooth):</strong> Automated shot peening / blasting for uniform surface texture. Consistent Ra across all parts in batch.",
        "<strong>DM60 (Color):</strong> Automated dyeing — parts immersed in heated dye bath. ISO-certified black + custom colors. 2–4 hr cycle.",
        "<strong>VaporFuse Surfacing:</strong> Chemical vapor smoothing — sealed, water-repellent surfaces without dimensional change. 2–6 hr automated cycle.",
        "All processes work on MJF PA12, PA11, PP parts. TPU requires specific settings.",
    ]),
    auxiliaries=[
        ("Compressed Air","6 bar for Powershot C/S blast systems","Available"),
        ("Water Supply","Required for DM60 dyeing process","Available"),
        ("Ventilation","Local exhaust for dye fumes and VaporFuse chemical vapors","Needs extension"),
        ("Floor Space","~15–20 m² for 2–3 DyeMansion units","Within allocated cell"),
        ("Electrical","230V single-phase for each unit","Available"),
        ("Waste Disposal","Dye waste water, blast media, chemical waste per local regs","Process needed"),
    ],
    hardware=[
        ("DyeMansion Powershot C","Automated depowdering / PolyShot Cleaning","€50–70k"),
        ("DyeMansion DM60","Automated dyeing — ISO colors, heated bath","€40–55k"),
        ("DyeMansion VaporFuse (optional)","Chemical vapor smoothing for sealed surfaces","€80–110k"),
        ("Alternative: AMT PostPro","Chemical vapor smoothing (competing product)","€60–90k"),
        ("Alternative: Rösler AM Solutions","Automated tumbling / mass finishing","€30–50k"),
    ],
    software=[
        ("DyeMansion Software Suite","Recipe management, process control, batch tracking","Included"),
        ("HP 3D Center Integration","Build report → post-processing recipe matching","API available"),
    ],
    gundernhausen=("Recommendation for Gundernhausen",[
        "<strong>Phase 1:</strong> HP Processing Station (included) + €15k bead blaster is sufficient for functional parts (jigs, fixtures)",
        "<strong>Phase 2 (Month 7–12):</strong> Add Powershot C (€50–70k) when volume exceeds manual blasting capacity",
        "<strong>Phase 3:</strong> Add DM60 dyeing + VaporFuse only if customer-facing or inter-plant parts require premium finish",
        "<strong>For our portfolio (tooling, fixtures):</strong> Chemical smoothing is NOT needed — Ra ~6–10 µm as-printed is acceptable",
        "<strong>When to invest:</strong> If Print Hub scales to consumer-visible parts for other plants, DyeMansion becomes essential",
    ]),
    sources=[
        ("DyeMansion Products","https://dyemansion.com/products/","Full portfolio"),
        ("DyeMansion + HP Partnership","https://dyemansion.com/post-processing-3d-printing/","Technology"),
    ],
)))

# 5 — Farsoon SLS (Open Platform)
techs.append(("05_Farsoon_SLS_Open_Platform", page(
    title="Farsoon SLS — <span>Open Material</span> Platform",
    tag="Technology Factsheet 05 • Strategic Alternative",
    subtitle="Chinese-manufactured SLS 3D printer with fully open material platform. Enables direct Evonik INFINAM PA12 powder supply without HP's RFID markup. 30–50% lower powder cost. Procurement leverage.",
    phase="EVALUATE", cost_label="€150–300k",
    kn=[("Open","Material Platform"),("30–50<span>%</span>","Powder Cost Savings"),("€15–35<span>/kg</span>","Direct PA12 Price"),("300<span>km</span>","Evonik Marl Distance")],
    overview=("Farsoon SLS — Open-Material Alternative to HP MJF",[
        "Selective Laser Sintering (SLS) using CO₂ laser to sinter polymer powder layer-by-layer",
        "<strong>Key differentiator:</strong> Fully open material platform — use any qualified PA12/PA11/PP/TPU powder",
        "Enables direct supply from Evonik (INFINAM), BASF, Arkema, or third-party powder manufacturers",
        "PA12 powder direct from Evonik: estimated €15–35/kg vs HP's RFID-locked €50–70/kg",
        "Farsoon HT1001P: 400×400×540 mm build volume (larger than HP's 380³), industrial-grade",
        "Trade-off: SLS is ~8–10× slower than MJF (laser point scanning vs full-layer fusing)",
    ]),
    how_it_works=("SLS vs MJF — Key Differences",[
        "<strong>SLS:</strong> CO₂ laser traces each cross-section point-by-point → slow but precise, proven for 30+ years",
        "<strong>MJF:</strong> Chemical agents + IR lamps fuse entire layer simultaneously → fast but locked ecosystem",
        "<strong>Speed:</strong> SLS ~400 cm³/hr vs MJF ~2,800 cm³/hr — MJF is 7× faster for full builds",
        "<strong>Materials:</strong> SLS has 50+ qualified powders from 10+ vendors. MJF has 6 HP-only materials.",
        "<strong>Economics:</strong> For <100 parts/week, open SLS + cheap powder can be 30–50% cheaper per part",
        "<strong>Strategy:</strong> Use SLS for large/slow parts where powder cost dominates; MJF for high-volume/speed",
    ]),
    auxiliaries=[
        ("Nitrogen Supply","SLS requires inert N₂ atmosphere during printing","Needs installation"),
        ("Electrical","3-phase 400V, ~15 kW average","Available"),
        ("HVAC / Ventilation","Same ATEX Zone 22 as MJF — powder handling","Same as MJF cell"),
        ("Compressed Air","6–8 bar for depowdering","Available"),
        ("Powder Sieve","External sieve for open powders (not integrated like HP)","€5–10k"),
        ("Floor Space","~30–40 m² for SLS cell","Halle 3 available"),
    ],
    hardware=[
        ("Farsoon HT252P","252×252×350 mm build, CO₂ laser, mid-range","€150–200k"),
        ("Farsoon HT1001P","400×400×540 mm build, dual-laser, industrial","€250–350k"),
        ("Alternative: EOS P396","Open-ish platform, German-made, proven","€300–400k"),
        ("Alternative: Formlabs Fuse 1+","Entry-level SLS, benchtop, open powder","€20–30k"),
        ("Powder sieving station","Russell Finex or equivalent vibratory sieve","€5–10k"),
    ],
    software=[
        ("Farsoon Make Software","Native build preparation, nesting, slicing","Included"),
        ("Materialise Magics (optional)","Advanced nesting, Farsoon build processor available","€10–20k/yr"),
    ],
    gundernhausen=("Strategic Assessment for Gundernhausen",[
        "<strong>Not a replacement for MJF</strong> — SLS is too slow for the Print Hub's high-volume ambition",
        "<strong>Complementary:</strong> Add one Farsoon SLS for large parts, prototypes, or when powder cost dominates",
        "<strong>Evonik leverage:</strong> Buying a Farsoon gives you direct access to €15–35/kg INFINAM PA12 from 300 km away (Marl)",
        "<strong>Procurement leverage:</strong> Telling HP 'we're also evaluating Farsoon with direct Evonik supply' pressures HP on powder pricing",
        "<strong>Phase 2 evaluation:</strong> Request Farsoon demo prints with Evonik INFINAM PA12 to validate quality vs HP MJF",
        "<strong>Formlabs Fuse 1+ (€25k):</strong> Could serve as a low-cost open-platform pilot before committing to Farsoon",
    ]),
    sources=[
        ("Farsoon Technologies","https://www.farsoon.com","Product portfolio"),
        ("Evonik INFINAM PA12","https://www.infinam.com/en/3d-printing-materials/polymer-powders/polyamide-12-nylon","Direct powder supply"),
        ("Evonik Marl Expansion","https://corporate.evonik.com/en/new-polyamide-12-powder-plant-25589.html","€400M PA12 plant"),
    ],
)))

# 6 — nTopology
techs.append(("06_nTopology_Generative_Design", page(
    title="nTopology — <span>Implicit Modeling</span> for AM",
    tag="Technology Factsheet 06 • Advanced Generative Design",
    subtitle="Computational design platform for lattice optimization, topology optimization, and functional grading — specifically designed for additive manufacturing. Rated 5/5 AM suitability. Highly relevant for NVH acoustic structures.",
    phase="PHASE 3", cost_label="€15–30k/yr",
    kn=[("5/5","AM Suitability"),("Lattice","Structure Optimization"),("NVH","Acoustic Relevance"),("STEP","Production Output")],
    overview=("nTopology — Engineering Design for Additive Manufacturing",[
        "Implicit modeling platform: geometry defined by mathematical fields, not boundary meshes",
        "Enables lattice structures, topology optimization, and functionally graded materials in a single workflow",
        "Specifically designed for AM constraints: overhang angles, min feature sizes, build orientation",
        "<strong>NVH relevance:</strong> Lattice-optimized acoustic structures can tune sound absorption properties when printed on MJF",
        "Used by aerospace (Lockheed Martin), automotive (Scuderia AlphaTauri), and medical industries",
        "Output: STEP, STL, 3MF — directly to HP SmartStream for MJF printing",
    ]),
    how_it_works=("Field-Driven Design",[
        "<strong>Step 1:</strong> Import design space (CAD model) + define load cases and constraints",
        "<strong>Step 2:</strong> nTopology generates optimal topology/lattice within the design space",
        "<strong>Step 3:</strong> Apply AM-specific constraints (MJF: min wall 0.5mm, min hole 0.5mm, no support needed)",
        "<strong>Step 4:</strong> Functionally grade lattice density: dense where loads are high, open where sound absorption is needed",
        "<strong>Step 5:</strong> Export production-ready geometry → nest in HP SmartStream → print",
        "Parametric: change load case → entire lattice regenerates automatically",
    ]),
    auxiliaries=[
        ("Workstation PC","GPU recommended for real-time lattice preview (NVIDIA RTX series)","May need upgrade"),
        ("FEA Validation","Ansys/Abaqus for structural validation of optimized geometry","Existing or new"),
        ("CAD Environment","Input models from SolidWorks, Fusion 360, CATIA, or CadQuery","Existing"),
    ],
    hardware=[
        ("Engineering Workstation","i7/Ryzen 9 + RTX 3060+ GPU + 32GB RAM","€2–4k (if new)"),
    ],
    software=[
        ("nTopology Platform","Implicit modeling, lattice, topology optimization, AM design","€15–30k/yr"),
        ("Autodesk Fusion 360 (alternative)","Generative Design module — simpler, cheaper, less AM-specific","€2–5k/yr"),
        ("Siemens NX + Topology (alternative)","Enterprise topology optimization — if already in Siemens ecosystem","€10–20k/yr"),
    ],
    gundernhausen=("Recommendation for Gundernhausen",[
        "<strong>Phase 3 (Month 12+):</strong> Evaluate for lattice-optimized acoustic parts — high strategic value for Autoneum's NVH expertise",
        "<strong>Key use case:</strong> Lightweight, sound-absorbing lattice inserts printed on MJF — could become a differentiating product offering",
        "<strong>Alternative start:</strong> Fusion 360 Generative Design (€2–5k/yr) covers 80% of topology optimization at 1/5th the cost",
        "<strong>When nTopology justifies its cost:</strong> When designing parts where lattice grading directly improves NVH performance metrics",
        "<strong>Combine with:</strong> Claude + CadQuery for simple parts, nTopology for complex optimized parts",
    ]),
    sources=[
        ("nTopology Platform","https://ntopology.com","Product overview"),
        ("nTopology for AM","https://ntopology.com/additive-manufacturing/","AM-specific features"),
    ],
)))

# 7 — Würth Digital Inventory
techs.append(("07_Wuerth_Digital_Inventory", page(
    title="Würth DIS + <span>3MF Secure</span>",
    tag="Technology Factsheet 07 • Digital Warehouse",
    subtitle="Würth Additive Group's Digital Inventory Services (DIS) integrated with HP MJF via 3MF Secure Content extension. Shift from physical stock to on-demand spare parts management across all Autoneum plants.",
    phase="PHASE 2", cost_label="Service model",
    kn=[("Digital","Inventory (zero stock)"),("3MF","Secure File Transfer"),("Global","Logistics Network"),("On-Demand","Print &amp; Ship")],
    overview=("Würth DIS — Digital Warehouse for 3D Printed Parts",[
        "HP + Würth partnership (Formnext 2025): integrate scalable MJF manufacturing with Würth's logistics network",
        "First official implementation of 3MF Secure Content extension — encrypted print files direct to MJF printers",
        "Replace physical spare parts warehouse with digital catalog of certified 3D designs",
        "Any Autoneum plant submits order → Gundernhausen prints → Würth handles packaging and logistics",
        "Reduces inventory holding costs, eliminates obsolescence, enables true just-in-time supply",
        "Würth's global logistics network provides last-mile delivery to any location",
    ]),
    how_it_works=("Digital Inventory Workflow",[
        "<strong>Step 1:</strong> Engineer designs part → validates → certifies for MJF production → uploads to digital catalog",
        "<strong>Step 2:</strong> Other Autoneum plant needs the part → orders via web portal / Apriso integration",
        "<strong>Step 3:</strong> 3MF Secure Content sends encrypted file to Gundernhausen MJF printer",
        "<strong>Step 4:</strong> Part printed overnight → QC inspection → VDA 4902 label → packed in KLT",
        "<strong>Step 5:</strong> Würth logistics picks up → delivers next-day to requesting plant",
        "IP protection: 3MF Secure Content prevents unauthorized copying or modification of part designs",
    ]),
    auxiliaries=[
        ("Internet Connection","Cloud-based catalog and order management","Available"),
        ("ERP Integration","SAP/Apriso connection for order processing and billing","Internal dev"),
        ("Digital Catalog","Web portal for part browsing, ordering, status tracking","Würth provides"),
    ],
    hardware=[
        ("No additional hardware","Uses existing MJF printer and packing station","€0"),
        ("Label Printer","VDA 4902 label printing for outgoing shipments","€2–5k (if not already present)"),
    ],
    software=[
        ("Würth DIS Platform","Digital inventory management, order processing, logistics","Service subscription"),
        ("3MF Secure Content","Encrypted file transfer to MJF printer — IP protection","Included with HP/Würth"),
        ("Autoneum Web Portal","Internal ordering interface for other plants","Internal dev"),
    ],
    gundernhausen=("Recommendation for Gundernhausen Print Hub",[
        "<strong>Phase 2 (Month 4–6):</strong> Engage Würth Additive Group for partnership discussion",
        "<strong>Start small:</strong> Digitize 50 most-ordered spare parts across Autoneum plants → upload to catalog",
        "<strong>Value prop:</strong> Eliminate physical spare parts warehouse at Gundernhausen + reduce inventory at other plants",
        "<strong>Revenue model:</strong> Charge internal cost price + markup to other plants — Print Hub becomes a profit center",
        "<strong>Scale:</strong> Target 1,000+ digitized parts within 18 months — critical mass for digital warehouse ROI",
    ]),
    sources=[
        ("HP + Würth Partnership","https://www.hp.com/us-en/newsroom/press-releases/2025/hp-drives-additive-manufacturing.html","Formnext 2025"),
        ("HP Digital Manufacturing Network","https://www.hp.com/us-en/printers/3d-printers/services/digital-manufacturing-network.html","DMN partners"),
    ],
)))

# 8 — Print & Apply VDA Labeling
techs.append(("08_Print_Apply_VDA_Labeling", page(
    title="Automated <span>Print &amp; Apply</span> VDA Labeling",
    tag="Technology Factsheet 08 • Kanban Label Automation",
    subtitle="Automated label printing and application system for VDA 4902 goods tags. Triggered by Apriso MES when handling unit (HU) is full. Zero manual input, zero labeling errors. PackML-compliant.",
    phase="PHASE 2", cost_label="€5–15k",
    kn=[("VDA 4902","Label Standard"),("Auto","Zero Manual Input"),("Apriso","MES Triggered"),("PackML","PLC Compatible")],
    overview=("Print & Apply — Automated VDA Label System",[
        "Print-and-apply (P&A) system prints VDA 4902 label with DataMatrix code and applies it to HU automatically",
        "Triggered by Apriso MES: when Kanban loop closes (HU full) → system fires without operator intervention",
        "VDA 4902 label (74×210 mm): supplier code, part number, batch ID, quantity, date — machine-readable",
        "Eliminates manual labeling errors — critical for automotive Tier-1 supplier compliance",
        "PackML-compliant controllers available for Allen-Bradley and Siemens PLC integration",
        "Throughput: 10–30 labels/minute — far exceeds MJF cell packing rate",
    ]),
    how_it_works=("Apriso → Print → Apply → Ship",[
        "<strong>Step 1:</strong> Apriso MES detects: HU (KLT bin) is full — parts counted, QC passed",
        "<strong>Step 2:</strong> Apriso sends label data via API to label software (part#, batch, qty, date, destination)",
        "<strong>Step 3:</strong> Label software (BarTender/NiceLabel/TEC-IT) generates VDA 4902 layout with DataMatrix",
        "<strong>Step 4:</strong> P&A head prints label on thermal transfer printer and applies to KLT bin",
        "<strong>Step 5:</strong> Labeled HU moves to shipping area — ready for Würth logistics or internal transport",
        "Full traceability: every label linked to HP build report via batch ID",
    ]),
    auxiliaries=[
        ("Compressed Air","4–6 bar for pneumatic applicator arm","Available"),
        ("Electrical","230V single-phase","Available"),
        ("Network / Ethernet","Apriso MES connection via TCP/IP","Available"),
        ("Label Stock","VDA 4902 thermal transfer labels (74×210 mm roll)","Consumable ~€500/yr"),
        ("Ribbon","Thermal transfer ribbon for label printer","Consumable ~€300/yr"),
    ],
    hardware=[
        ("Print & Apply Unit","Zebra ZE521 / SATO S84-EX / ID Technology — integrated printer + applicator","€5–12k"),
        ("Mounting Bracket","Positioned at packing station — applies label to KLT top or side","€500–1k"),
        ("Barcode Scanner (optional)","Verification scan after application — confirm label readable","€500–1k"),
    ],
    software=[
        ("BarTender (Seagull)","VDA 4902 label design, DataMatrix generation, print automation","€1–3k/yr"),
        ("Alternative: NiceLabel","Cloud-based label management platform","€1–2k/yr"),
        ("Alternative: TEC-IT TBarCode","VDA 4902 specific — free online, professional version available","Free / €500"),
        ("Apriso Integration","REST API trigger from MES to label printer — custom development","Internal dev"),
    ],
    gundernhausen=("Recommendation for Gundernhausen",[
        "<strong>Phase 2 (Month 4–6):</strong> Install P&A unit at MJF cell packing station — €8–15k total",
        "<strong>Integrate with Apriso:</strong> Digital Kanban card status change → automatic label generation → apply to HU",
        "<strong>VDA compliance:</strong> Required for any automotive Tier-1 shipments — install from day one of Print Hub operation",
        "<strong>Existing Siemens PLC:</strong> PackML-compliant controllers available — integrates with existing plant automation",
        "<strong>ROI:</strong> Eliminates 1 manual labeling step per HU × hundreds of HUs/month — pays for itself in error avoidance alone",
    ]),
    sources=[
        ("TEC-IT VDA 4902","https://www.tec-it.com/en/software/label-printing/label-software/vda-4902/Default.aspx","Label software"),
        ("ID Technology P&A","https://www.idtechnology.com/products/print-and-apply/","Hardware"),
    ],
)))

# 9 — MiR AMR
techs.append(("09_MiR_AMR_Transport", page(
    title="MiR <span>AMR</span> — Autonomous Transport",
    tag="Technology Factsheet 09 • Intralogistics",
    subtitle="MiR250 Autonomous Mobile Robot for build unit and parts transport within the MJF workcell and between production zones. AI-navigated, no fixed paths. Evaluate in Phase 3–4.",
    phase="PHASE 3–4", cost_label="€58–83k",
    kn=[("250<span>kg</span>","Payload Capacity"),("AI","Self-Navigating"),("24/7","Autonomous Operation"),("18–30<span>Mo</span>","Payback Period")],
    overview=("MiR250 — Autonomous Mobile Robot",[
        "AMR (Autonomous Mobile Robot): uses LiDAR, 3D cameras, and SLAM to navigate freely — no fixed paths or magnetic tape",
        "Payload: 250 kg — sufficient for MJF build units (~350 kg with top module) or part bins",
        "Self-navigating: dynamically avoids obstacles, adapts to layout changes, integrates with doors/elevators",
        "Fleet management software for multi-robot coordination — can serve multiple workcells",
        "MiR is a Teradyne company — global support, automotive-grade reliability",
        "AMR market growing at 32.7% CAGR — mainstream technology in modern factories by 2026",
    ]),
    how_it_works=("Automated Material Flow",[
        "<strong>Route 1:</strong> Printer → Cooling station (build unit transport after print completes)",
        "<strong>Route 2:</strong> Cooling station → Processing Station (depowdering after cooldown)",
        "<strong>Route 3:</strong> Post-processing → QC/Packing (finished parts to clean zone)",
        "<strong>Route 4:</strong> Packing → Shipping dock (labeled HUs to dispatch)",
        "<strong>Trigger:</strong> Apriso MES sends mission to MiR Fleet when job status changes",
        "<strong>Integration:</strong> REST API connects MiR Fleet to Apriso — fully automated mission dispatch",
    ]),
    auxiliaries=[
        ("WiFi Network","Reliable WiFi coverage across entire workcell / hall","May need extension"),
        ("Charging Station","MiR AutoCharge — robot docks automatically when idle","Included in deployment"),
        ("Floor Condition","Flat, clean floor — no thresholds >20mm, no loose cables","Available (industrial)"),
        ("Safety Certification","CE marked, ISO 3691-4 compliant — safe around people","Built-in"),
    ],
    hardware=[
        ("MiR250 Robot","250 kg payload, LiDAR, 3D cameras, self-navigating","€35–50k"),
        ("MiR250 Top Module","Shelf/cart lifter for build unit or KLT transport","€8–15k"),
        ("MiR AutoCharge Station","Autonomous charging dock","€3–5k"),
        ("MiR Fleet Management","Multi-robot coordination server (if >1 robot)","€5–8k"),
    ],
    software=[
        ("MiR Fleet","Mission management, traffic optimization, reporting","Included with Fleet HW"),
        ("MiR REST API","Integration with Apriso MES for automated mission dispatch","Free (built-in)"),
        ("Apriso Integration","Custom workflow to trigger AMR missions on Kanban events","Internal dev"),
    ],
    gundernhausen=("Recommendation for Gundernhausen",[
        "<strong>Phase 1–2: NOT needed.</strong> With <30 employees and one workcell, manual transport is sufficient",
        "<strong>Phase 3–4 (Month 13+):</strong> Evaluate when 2+ printers running and transport becomes a bottleneck",
        "<strong>Pilot:</strong> Start with 1× MiR250 (€58–83k deployed) for build unit shuttle between zones",
        "<strong>ROI:</strong> Marginal in small operation — primary value is 24/7 autonomous operation for lights-sparse concept",
        "<strong>Alternative:</strong> Simple roller conveyor between printer and processing station (€5–10k) may suffice",
    ]),
    sources=[
        ("MiR Robots","https://mobile-industrial-robots.com","Product portfolio"),
        ("MiR250 Spec Sheet","https://mobile-industrial-robots.com/robots/mir250/","Technical specifications"),
    ],
)))

# ══════════════════════════════════════════════════════════════
# GENERATE ALL FILES + INDEX
# ══════════════════════════════════════════════════════════════

for filename, html in techs:
    path = os.path.join(OUT, f"{filename}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  OK  {filename}.html")

# Generate index page
idx_rows = ""
for i, (filename, _) in enumerate(techs, 1):
    name = filename.split("_", 1)[1].replace("_", " ")
    idx_rows += f'        <tr><td><strong>{i:02d}</strong></td><td><a href="{filename}.html" style="color:var(--b);font-weight:700;text-decoration:none;">{name}</a></td></tr>\n'

index_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technology Factsheets — Index</title>
    {CSS}
</head>
<body>
<div class="hero">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
        <div>
            <div class="hero-tag">NVH 2030 • MJF Deep-Dive Annex</div>
            <h1>Technology <span>Factsheets</span></h1>
        </div>
        <div style="text-align:right;">
            <div style="font-size:18px;font-weight:700;color:var(--g);letter-spacing:1px;">AUTONEUM</div>
            <div style="font-size:9px;font-style:italic;color:var(--o);">- CONFIDENTIAL -</div>
        </div>
    </div>
    <p class="hero-sub">One-page factsheets for each recommended technology in the HP MJF 3D Printing Deep-Dive. Each covers: overview, how it works, auxiliaries, hardware, software, and Gundernhausen-specific recommendation.</p>
    <div class="hero-meta">
        <span>Autoneum Germany GmbH – Gundernhausen</span><span>|</span><span>March 2026</span><span>|</span><span>Author: J.R.E. Glawion</span>
    </div>
</div>

<div class="kn-bar">
    <div class="kn"><div class="v">9</div><div class="l">Technologies Covered</div></div>
    <div class="kn"><div class="v">4</div><div class="l">Implementation Phases</div></div>
    <div class="kn"><div class="v">&euro;520–580k</div><div class="l">Core Investment (2 printers)</div></div>
    <div class="kn"><div class="v">12–24<span>Mo</span></div><div class="l">Payback Period</div></div>
</div>

<div class="container">
    <div class="sh"><div class="tag">Index</div><h2>All Technology Factsheets</h2><p>Click to open each factsheet. Each is a standalone HTML document.</p></div>
    <div style="background:var(--wh);border-radius:8px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.05);margin-bottom:18px;border:1px solid var(--lg);">
        <table>
            <thead><tr><th>#</th><th>Technology Factsheet</th></tr></thead>
            <tbody>
{idx_rows}            </tbody>
        </table>
    </div>
    <p style="font-size:9px;color:var(--gy);font-style:italic;">Reference: <a href="../03_Analysen/HP_MJF_3D_Printing_DeepDive.html" style="color:var(--b);">← Back to MJF Deep-Dive Analysis</a></p>
</div>
<div class="footer">
    <p>&copy; 2026 Autoneum Germany GmbH – Gundernhausen | - CONFIDENTIAL - | Technology Factsheets | Author: J.R.E. Glawion</p>
</div>
</body>
</html>"""

with open(os.path.join(OUT, "00_Index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print(f"  OK  00_Index.html")
print(f"\nDone! {len(techs)} factsheets + 1 index generated in:\n  {OUT}")
