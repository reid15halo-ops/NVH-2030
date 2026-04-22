"""
Generate:
1. PET Foam Deep-Dive (03_Analysen/)
2. Dual-Pillar Investment Proposal (04_Praesentationen/)
3. PET Foam Factsheet (06_Technologie_Factsheets/)
"""
import os

BASE = r"c:\Users\122798\OneDrive - Autoneum\Organized_Workspace\05_Projects\Factory_Layouts\NVH 2030"

# ══════════════════════════════════════════════════════════════
# Shared CSS (identical to MJF deep-dive for consistency)
# ══════════════════════════════════════════════════════════════
CSS = open(os.path.join(BASE, "03_Analysen", "HP_MJF_3D_Printing_DeepDive.html"), "r", encoding="utf-8").read()
# Extract just the <style> block
css_start = CSS.index("<style>")
css_end = CSS.index("</style>") + len("</style>")
STYLE_BLOCK = CSS[css_start:css_end]

print("CSS extracted:", len(STYLE_BLOCK), "chars")

# ══════════════════════════════════════════════════════════════
# 1. PET FOAM DEEP-DIVE
# ══════════════════════════════════════════════════════════════
pet_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EV Acoustic + PET Foam Sandwich – Deep-Dive Analysis</title>
    {STYLE_BLOCK}
</head>
<body>

<!-- HERO -->
<div class="hero">
    <div class="hero-top">
        <div>
            <div class="hero-tag">Technology Deep-Dive &bull; Highest-Scoring Investment Option</div>
            <h1>EV Acoustic Components + <span>PET Foam Sandwich</span> <span class="vbadge">SCORE: 92/100</span></h1>
        </div>
        <div style="text-align:right;">
            <div style="font-size:20px; font-weight:700; color:var(--atn-green); letter-spacing:1px;">AUTONEUM</div>
            <div class="classification">- CONFIDENTIAL -</div>
        </div>
    </div>
    <p class="hero-sub"><strong style="color:var(--atn-green);">The #1 strategic investment</strong> for Gundernhausen. 40% of EV noise comes from tire/road interaction &mdash; exactly where Autoneum&rsquo;s core competency lies. No Chinese competitor can match the PET foam + nonwoven combination independently. $17.6B addressable market by 2030. This annex provides a comprehensive analysis of technology, products, supply chain, BYD opportunity, and implementation roadmap.</p>
    <div style="margin-bottom:14px; padding:12px 16px; background:rgba(184,196,0,.08); border:1px solid rgba(184,196,0,.25); border-radius:6px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
            <div>
                <div style="font-size:9px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--atn-green); opacity:.8;">Researched, Evaluated &amp; Compiled by</div>
                <div style="font-size:16px; font-weight:700; color:var(--atn-white);">Jonas Roland Erwin Glawion</div>
                <div style="font-size:11px; color:rgba(255,255,255,.7);">Process Engineer &mdash; Autoneum Germany GmbH &ndash; Gundernhausen</div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:9px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--atn-green); opacity:.8;">Reference Documents</div>
                <div style="font-size:11px; color:rgba(255,255,255,.7);"><a href="Gundernhausen Innovation Strategies 2026.html" style="color:var(--atn-light-blue); text-decoration:none;">&larr; CEO Paper V3</a> &nbsp;|&nbsp; <a href="HP_MJF_3D_Printing_DeepDive.html" style="color:var(--atn-light-blue); text-decoration:none;">MJF Deep-Dive</a></div>
            </div>
        </div>
    </div>
    <div class="hero-meta">
        <span>Autoneum Germany GmbH &ndash; Gundernhausen</span><span>|</span><span>March 2026</span><span>|</span><span>Confidential</span><span>|</span><span>Author: J.R.E. Glawion</span>
    </div>
</div>

<!-- KEY NUMBERS -->
<div class="key-numbers">
    <div class="kn"><div class="v">$17.6<span>B</span></div><div class="l">Market by 2030</div></div>
    <div class="kn"><div class="v">25&ndash;35<span>%</span></div><div class="l">Projected IRR</div></div>
    <div class="kn"><div class="v">18&ndash;24<span>Mo</span></div><div class="l">Payback Period</div></div>
    <div class="kn"><div class="v">92<span>/100</span></div><div class="l">Investment Score</div></div>
    <div class="kn"><div class="v">88<span>%</span></div><div class="l">Revenue Certainty</div></div>
    <div class="kn"><div class="v">&euro;2&ndash;4<span>M</span></div><div class="l">Investment Range</div></div>
</div>

<div class="container">

<!-- ============ WHY PET FOAM ============ -->
<div class="sh"><div class="tag">01 &bull; Strategic Context</div><h2>Why PET Foam Is the Future of Automotive NVH</h2><p>EVs are quiet powertrains but LOUD on road noise &mdash; creating massive demand for acoustic solutions</p></div>

<div style="background:linear-gradient(135deg,#4A0E00,#7A1800); border:2px solid var(--atn-orange); border-radius:8px; padding:22px 26px; margin-bottom:22px; color:var(--atn-white);">
    <div style="display:flex; align-items:flex-start; gap:16px;">
        <div style="font-size:36px; line-height:1;">&#9888;</div>
        <div>
            <div style="font-size:16px; font-weight:700; color:var(--atn-orange); margin-bottom:8px;">THE EV ACOUSTIC PROBLEM</div>
            <div style="font-size:11px; line-height:1.7;">
                <strong style="color:var(--atn-orange);">40% of perceived EV cabin noise</strong> comes from tire/road interaction. Without engine noise to mask it, road noise, wind noise, and drivetrain whine become 40% more noticeable to occupants.<br><br>
                <strong>Chinese EVs designed for China market</strong> tolerate higher cabin noise than European consumers expect. Every BYD, Geely, and NIO entering Europe needs acoustic upgrades: wheelhouse liners, underbody shields, door insulation, frunk absorbers, e-motor capsules.<br><br>
                <strong style="color:var(--atn-green);">PET foam + nonwoven sandwich</strong> is Autoneum&rsquo;s proprietary combination that no single Chinese supplier replicates. This is a defensible competitive moat.
            </div>
        </div>
    </div>
</div>

<div class="box box-dark">
    <h3>PET Foam vs PUR Foam &mdash; Why the Transition</h3>
    <div class="stats stats-4">
        <div class="stat"><div class="sv">100%</div><div class="sl">PET = fully recyclable (rPET closed-loop)</div></div>
        <div class="stat"><div class="sv">15%</div><div class="sl">EU ELV mandate: recycled plastic in vehicles</div></div>
        <div class="stat"><div class="sv">30&ndash;40%</div><div class="sl">Lighter than equivalent PUR parts</div></div>
        <div class="stat"><div class="sv">0</div><div class="sl">Isocyanate / TDI / MDI required (safer)</div></div>
    </div>
    <p style="font-size:10px; margin-top:8px; color:#aaa;"><strong>Gundernhausen today:</strong> PUR foam (polyurethane) production. <strong>Gundernhausen tomorrow:</strong> PET foam sandwich technology &mdash; lighter, recyclable, EU ELV compliant, no hazardous isocyanates. The MJF Print Hub (Phase 1) produces jigs/fixtures/tooling <strong>for</strong> the PET foam production lines.</p>
</div>

<!-- ============ PRODUCT PORTFOLIO ============ -->
<div class="page-break"></div>
<div class="sh"><div class="tag">02 &bull; Product Portfolio</div><h2>Target Products for Chinese OEM European Plants</h2><p>12+ product types addressing BYD, Geely/Volvo, Leapmotor, Chery, NIO acoustic needs</p></div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <table>
        <thead><tr><th>Product</th><th>Technology</th><th>Application</th><th>Autoneum Brand</th><th>EV Relevance</th></tr></thead>
        <tbody>
            <tr style="background:var(--atn-lightest-green);"><td><strong>Wheelhouse liners</strong></td><td>PET foam sandwich + nonwoven</td><td>Tire/road noise barrier &mdash; #1 EV noise source</td><td>Ultra-Silent</td><td class="sc-h">Critical</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>Acoustic underbody panels</strong></td><td>PET foam + needlepunch</td><td>Road noise shield, aerodynamic, stone impact protection</td><td>Ultra-Silent</td><td class="sc-h">Critical</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>PET foam door insulation</strong></td><td>PET foam core sandwich</td><td>Wind noise barrier, thermal insulation, weight savings</td><td>Hybrid-Acoustics PET</td><td class="sc-h">Critical</td></tr>
            <tr><td><strong>Frunk liners</strong></td><td>PET foam + nonwoven finish</td><td>EV-specific: front trunk acoustic + aesthetic treatment</td><td>Ultra-Silent Frunk</td><td class="sc-h">EV-only</td></tr>
            <tr><td><strong>E-motor capsules</strong></td><td>PET foam encapsulation</td><td>Electric motor noise containment (whine, PWM)</td><td>Hybrid-Acoustics</td><td class="sc-h">EV-only</td></tr>
            <tr><td><strong>Gigacasting acoustic inlays</strong></td><td>PET foam insert</td><td>Damping inserts for megacast body structures</td><td>New development</td><td class="sc-h">EV-only</td></tr>
            <tr><td><strong>Needlepunch carpets</strong></td><td>100% PET, rPET fibers</td><td>Floor covering with integrated acoustic decoupler</td><td>Di-Light / Relive-1</td><td class="sc-m">All vehicles</td></tr>
            <tr><td><strong>Flexi-Light carpets</strong></td><td>Lightweight needlepunch</td><td>20% lighter than conventional &mdash; range optimization</td><td>Autoneum Pure.</td><td class="sc-m">All vehicles</td></tr>
            <tr><td><strong>Inner dash insulation</strong></td><td>Hybrid-Acoustics PET</td><td>Firewall / bulkhead insulator + absorber combination</td><td>IFP-R2</td><td class="sc-m">All vehicles</td></tr>
            <tr><td><strong>Headliners</strong></td><td>PET foam core + fabric</td><td>Roof NVH + aesthetic + thermal management</td><td>Standard</td><td class="sc-m">All vehicles</td></tr>
            <tr><td><strong>Battery enclosure insulation</strong></td><td>PET FR foam</td><td>Thermal + acoustic barrier around battery pack</td><td>New development</td><td class="sc-h">EV-only</td></tr>
            <tr><td><strong>Trunk trim / load floor</strong></td><td>PET foam sandwich</td><td>Structural + acoustic + aesthetic</td><td>Standard</td><td class="sc-l">All vehicles</td></tr>
        </tbody>
    </table>
</div>

<!-- ============ PET FOAM TECHNOLOGY ============ -->
<div class="sh"><div class="tag">03 &bull; Technology</div><h2>ArmaFORM PET Foam Core &mdash; Material Properties</h2><p>100% recycled PET (rPET from bottles), thermoformable at 185&ndash;210&deg;C, zero spring-back</p></div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <h3 style="font-size:12px; font-weight:700; color:var(--atn-green); margin-bottom:10px;">ArmaFORM PET Grades for Automotive</h3>
    <table>
        <thead><tr><th>Grade</th><th>Density (kg/m&sup3;)</th><th>Compressive Str. (MPa)</th><th>Shear Str. (MPa)</th><th>Key Feature</th><th>Application</th></tr></thead>
        <tbody>
            <tr style="background:var(--atn-lightest-green);"><td><strong>GR60</strong></td><td>60</td><td>0.45</td><td>0.35</td><td>Lightweight, eco (100% rPET)</td><td>Wheelhouse, underbody, doors</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>FR60</strong></td><td>60</td><td>0.45</td><td>0.35</td><td>Flame retardant (halogen-free)</td><td>Battery enclosure, e-motor</td></tr>
            <tr><td><strong>GR80</strong></td><td>80</td><td>0.80</td><td>0.55</td><td>Higher structural load</td><td>Load floors, structural panels</td></tr>
            <tr><td><strong>GR115</strong></td><td>115</td><td>1.45</td><td>0.80</td><td>High stiffness</td><td>Headliners, roof structures</td></tr>
            <tr><td><strong>GR250</strong></td><td>250</td><td>5.00</td><td>2.80</td><td>Structural core</td><td>Gigacasting inlays, brackets</td></tr>
        </tbody>
    </table>
    <p style="font-size:8.5px; color:var(--atn-dark-grey); margin-top:6px; font-style:italic;">Thermoforming window: 185&ndash;210&deg;C. Close to zero spring-back after cooling. No ozone-depleting HFC/CFC blowing agents. Halogen-free flame retardant additives only. Supplier: Armacell (global).</p>
</div>

<div class="box box-green">
    <h3>PET Foam Sandwich Construction</h3>
    <ul>
        <li><strong>Core:</strong> ArmaFORM PET foam (GR60/FR60) &mdash; acoustic absorption + structural stiffness + thermal insulation</li>
        <li><strong>Face skins:</strong> Needlepunch nonwoven (100% PET, up to 70% recycled fibers) &mdash; surface finish + additional absorption</li>
        <li><strong>Bonding:</strong> Thermoplastic adhesive (no latex, no water) via Autoneum ABC process &mdash; monomaterial, fully recyclable</li>
        <li><strong>Result:</strong> 100% PET monomaterial sandwich &mdash; closed-loop recyclable, EU ELV compliant from day one</li>
        <li><strong>Weight saving:</strong> 30&ndash;40% lighter than equivalent PUR-based parts</li>
        <li><strong>Acoustic performance:</strong> Dual function &mdash; insulator (blocks sound) + absorber (dissipates sound energy) in one part</li>
    </ul>
</div>

<!-- ============ EU REGULATION ============ -->
<div class="page-break"></div>
<div class="sh"><div class="tag">04 &bull; Regulatory Driver</div><h2>EU ELV Regulation &mdash; Recycled Content Mandate</h2><p>December 2025: EU Council + Parliament agreed on mandatory recycled plastic targets for vehicles</p></div>

<div class="stats stats-4" style="margin-bottom:18px;">
    <div class="stat"><div class="sv">15%</div><div class="sl">Recycled plastic (6 yrs after entry)</div></div>
    <div class="stat"><div class="sv">25%</div><div class="sl">Recycled plastic (10 yrs after entry)</div></div>
    <div class="stat"><div class="sv">20%</div><div class="sl">Of recycled content from closed-loop ELV</div></div>
    <div class="stat"><div class="sv">Dec 2025</div><div class="sl">Provisional agreement reached</div></div>
</div>

<div class="box box-warn">
    <h3>Why This Is a Game-Changer for Autoneum</h3>
    <ul>
        <li><strong>PET foam products use 100% rPET</strong> (recycled PET from post-consumer bottles) &mdash; built-in ELV compliance</li>
        <li>OEMs will <strong>actively seek suppliers</strong> who can certify recycled content from day one &mdash; first-mover advantage</li>
        <li>PUR foam has <strong>no established recycled-content pathway</strong> &mdash; PUR recycling is TRL 3-4, expensive, and not closed-loop</li>
        <li>Autoneum&rsquo;s Relive-1 and Di-Light carpets already use up to <strong>70% recycled PET fibers</strong></li>
        <li>20% of recycled content must come from <strong>closed-loop ELV recycling</strong> &mdash; favors monomaterial PET (easily sortable) over mixed PUR</li>
        <li>Chinese OEMs entering Europe have <strong>zero recycled-content supply chain</strong> &mdash; they need European Tier-1s like Autoneum</li>
    </ul>
</div>

<!-- ============ BYD OPPORTUNITY ============ -->
<div class="sh"><div class="tag">05 &bull; Target Customer</div><h2>BYD Hungary (Szeged) &mdash; The Immediate Opportunity</h2><p>300,000 vehicles/year starting Q2 2026. Supplier nominations happening NOW.</p></div>

<div class="stats stats-5" style="margin-bottom:18px;">
    <div class="stat"><div class="sv">Q2 2026</div><div class="sl">Series production start</div></div>
    <div class="stat"><div class="sv">300k</div><div class="sl">Max. vehicles/year</div></div>
    <div class="stat"><div class="sv">&euro;4B</div><div class="sl">BYD Szeged investment</div></div>
    <div class="stat"><div class="sv">Dolphin</div><div class="sl">First model (+ Atto 2)</div></div>
    <div class="stat"><div class="sv">~700 km</div><div class="sl">Gundernhausen &rarr; Szeged</div></div>
</div>

<div class="box box-dark">
    <h3>What BYD Szeged Needs from Autoneum</h3>
    <ul>
        <li><strong>Wheelhouse liners:</strong> 4 per vehicle &times; 300k vehicles = 1.2M parts/year &mdash; PET foam + nonwoven, thermoformed</li>
        <li><strong>Underbody panels:</strong> 2&ndash;3 per vehicle &mdash; aerodynamic + acoustic + stone impact protection</li>
        <li><strong>Carpet systems:</strong> Full floor + trunk &mdash; 100% PET monomaterial, EU ELV compliant</li>
        <li><strong>Frunk liner:</strong> EV-specific &mdash; acoustic treatment for front trunk (no engine bay)</li>
        <li><strong>Door insulation:</strong> Wind noise barrier &mdash; critical for European NVH expectations</li>
        <li><strong>E-motor capsule:</strong> Electric motor noise containment &mdash; BYD e-Platform 3.0 whine reduction</li>
        <li>Additional Chinese OEMs building EU plants: Geely/Volvo, Leapmotor/Stellantis, Chery, NIO &mdash; same acoustic needs</li>
    </ul>
</div>

<!-- ============ PRODUCTION TECHNOLOGY ============ -->
<div class="page-break"></div>
<div class="sh"><div class="tag">06 &bull; Production</div><h2>Production Technology &amp; Equipment</h2><p>Thermoforming + needlepunch + ABC bonding &mdash; three process steps for complete sandwich parts</p></div>

<div class="flow">
    <div class="flow-box dark">rPET Fiber<br>Input</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-box">ANDRITZ<br>Needlepunch</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-box">PET Foam<br>Lamination</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-box dark">Thermoform<br>Press</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-box">Trim &amp;<br>Finish</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-box dark">QC &amp;<br>Ship</div>
</div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <h3 style="font-size:12px; font-weight:700; color:var(--atn-green); margin-bottom:10px;">Required Equipment &amp; Investment</h3>
    <table>
        <thead><tr><th>Equipment</th><th>Function</th><th>Supplier</th><th>Est. Investment</th></tr></thead>
        <tbody>
            <tr style="background:var(--atn-lightest-green);"><td><strong>ANDRITZ Needlepunch Line</strong></td><td>Produce nonwoven face skins from rPET fibers (30&ndash;4,200 gsm)</td><td>ANDRITZ Nonwoven</td><td>&euro;800k &ndash; 1.5M</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>Thermoforming Press</strong></td><td>Form PET foam sandwich at 185&ndash;210&deg;C into 3D shape</td><td>Existing or Dieffenbacher</td><td>&euro;300k &ndash; 600k (if new)</td></tr>
            <tr><td><strong>PET Foam Cutting / Lamination</strong></td><td>Cut ArmaFORM sheets + laminate with nonwoven skins</td><td>Various</td><td>&euro;150k &ndash; 300k</td></tr>
            <tr><td><strong>Trimming / Water Jet / CNC</strong></td><td>Trim thermoformed parts to final contour</td><td>Existing or new CNC router</td><td>&euro;100k &ndash; 200k</td></tr>
            <tr><td><strong>QC / Measurement</strong></td><td>Dimensional inspection, weight check, acoustic testing</td><td>Various</td><td>&euro;50k &ndash; 100k</td></tr>
            <tr><td><strong>Tooling (molds per part)</strong></td><td>Thermoform tools per product variant</td><td>Toolmaker</td><td>&euro;30k &ndash; 80k per tool</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td colspan="3"><strong>TOTAL INVESTMENT (excl. tooling)</strong></td><td><strong>&euro;1.4M &ndash; 2.7M</strong></td></tr>
        </tbody>
    </table>
    <p style="font-size:8.5px; color:var(--atn-dark-grey); margin-top:6px; font-style:italic;">Gundernhausen advantage: existing thermoforming presses may be reusable for PET foam (ArmaFORM compatible with standard automotive presses). Reduces investment by &euro;300&ndash;600k. ANDRITZ already supplies Autoneum Mexico &mdash; existing vendor relationship.</p>
</div>

<div class="box box-green">
    <h3>Autoneum Competitive Advantage</h3>
    <ul>
        <li><strong>Hybrid-Acoustics technology:</strong> Proprietary combination of insulator + absorber in one part &mdash; no competitor replicates this</li>
        <li><strong>ABC process (Alternative Backcoating):</strong> Thermoplastic adhesive instead of latex &mdash; monomaterial, no water, recyclable</li>
        <li><strong>100% PET monomaterial:</strong> Easy to sort, shred, and re-extrude at end of life &mdash; true closed-loop</li>
        <li><strong>Autoneum Pure. label:</strong> Certified sustainability brand recognized by OEMs &mdash; marketing advantage</li>
        <li><strong>280 skilled employees at Gundernhausen:</strong> Decades of NVH + foam + textile experience, transferable to PET</li>
        <li><strong>MJF Print Hub synergy:</strong> 3D-printed jigs, fixtures, and tooling for PET production lines &mdash; faster line setup, lower tooling cost</li>
    </ul>
</div>

<!-- ============ MJF SYNERGY ============ -->
<div class="sh"><div class="tag">07 &bull; Synergy</div><h2>MJF + PET Foam &mdash; The Dual-Pillar Synergy</h2><p>Phase 1 (MJF) directly enables Phase 2 (PET Foam) &mdash; complementary, not competing investments</p></div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <table>
        <thead><tr><th>MJF Print Hub Produces</th><th>For PET Foam Production</th><th>Benefit</th></tr></thead>
        <tbody>
            <tr><td><strong>Thermoform tool inserts</strong></td><td>Prototype/small-series mold inserts for PET foam parts</td><td>2 days vs 4&ndash;6 weeks from toolmaker</td></tr>
            <tr><td><strong>Trim fixtures &amp; holding jigs</strong></td><td>Locating fixtures for CNC/waterjet trimming</td><td>Custom per part, iterate overnight</td></tr>
            <tr><td><strong>Assembly aids</strong></td><td>Positioning jigs for sandwich lamination</td><td>Exact contour, lightweight, no metal</td></tr>
            <tr><td><strong>Quality gauges</strong></td><td>Go/no-go gauges for thermoformed parts</td><td>Print on demand, no stock needed</td></tr>
            <tr><td><strong>Packaging inserts</strong></td><td>Custom-contour KLT inserts for shipping to BYD</td><td>Exact part protection, reusable</td></tr>
            <tr><td><strong>Spare parts</strong></td><td>Machine components, guides, adapters for needlepunch/press</td><td>No lead time, no MOQ, overnight</td></tr>
        </tbody>
    </table>
</div>

<!-- ============ IMPLEMENTATION ============ -->
<div class="page-break"></div>
<div class="sh"><div class="tag">08 &bull; Roadmap</div><h2>Implementation Roadmap</h2><p>Phased rollout: MJF first (quick ROI), PET Foam follows (strategic anchor)</p></div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <table>
        <thead><tr><th>Phase</th><th>Timeline</th><th>Activity</th><th>Investment</th><th>Revenue</th></tr></thead>
        <tbody>
            <tr style="background:var(--atn-lightest-green);"><td><strong>1 &mdash; MJF Print Hub</strong></td><td>Month 1&ndash;6</td><td>HP MJF 5200 installed, Print Hub operational, tooling for PET lines designed</td><td>&euro;520&ndash;580k</td><td>Internal savings + inter-plant supply</td></tr>
            <tr><td><strong>2 &mdash; PET Pilot</strong></td><td>Month 4&ndash;9</td><td>ANDRITZ needlepunch order, ArmaFORM qualification, prototype parts for BYD</td><td>&euro;800k &ndash; 1.5M</td><td>BYD sample contracts</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>3 &mdash; PET Series</strong></td><td>Month 10&ndash;18</td><td>Thermoforming line operational, BYD Szeged series supply begins, carpet production</td><td>&euro;400k &ndash; 800k</td><td><strong>Series revenue from BYD</strong></td></tr>
            <tr><td><strong>4 &mdash; Scale</strong></td><td>Month 18&ndash;24</td><td>Second needlepunch line (if demand), Geely/Leapmotor acquisition, closed-loop rPET</td><td>&euro;500k &ndash; 1M</td><td>Multi-OEM revenue stream</td></tr>
        </tbody>
    </table>
</div>

<!-- CTA -->
<div class="cta">
    <h2>Investment Decision: EV Acoustic + PET Foam Sandwich</h2>
    <p>The highest-scoring investment option (92/100). Addresses a $17.6B market with Autoneum&rsquo;s core NVH competency. PET foam + nonwoven sandwich is a defensible competitive moat. EU ELV regulation creates mandatory demand. BYD Hungary needs suppliers NOW.</p>
    <div class="cta-stats">
        <div class="cs2"><div class="v2">&euro;2&ndash;4M</div><div class="l2">Total Investment</div></div>
        <div class="cs2"><div class="v2">25&ndash;35%</div><div class="l2">Projected IRR</div></div>
        <div class="cs2"><div class="v2">18&ndash;24 Mo</div><div class="l2">Payback Period</div></div>
        <div class="cs2"><div class="v2">92/100</div><div class="l2">Investment Score (Highest)</div></div>
        <div class="cs2"><div class="v2">88%</div><div class="l2">Revenue Certainty</div></div>
    </div>
</div>

<!-- SOURCES -->
<div class="sh"><div class="tag">Sources</div><h2>Source Appendix</h2></div>
<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <table>
        <thead><tr><th>Source</th><th>Topic</th></tr></thead>
        <tbody>
            <tr><td><a href="https://www.armacell.com/en-BH/armapet-technology" style="color:var(--atn-light-blue);">Armacell &mdash; ArmaPET Technology</a></td><td>PET foam core material</td></tr>
            <tr><td><a href="https://www.autoneum.com/pure/" style="color:var(--atn-light-blue);">Autoneum Pure.</a></td><td>Sustainability label, product portfolio</td></tr>
            <tr><td><a href="https://www.autoneum.com/products-technologies/light-vehicles/exterior/" style="color:var(--atn-light-blue);">Autoneum &mdash; Exterior Products</a></td><td>Ultra-Silent, wheelhouse, underbody</td></tr>
            <tr><td><a href="https://www.andritz.com/campaign-nonwoven-en/nonwovens-automotive-technology" style="color:var(--atn-light-blue);">ANDRITZ &mdash; Automotive Nonwoven</a></td><td>Needlepunch technology</td></tr>
            <tr><td><a href="https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/circular-economy-council-and-parliament-strike-deal-on-rules-for-vehicle-circularity-and-management-of-end-of-life-vehicles/" style="color:var(--atn-light-blue);">EU Council &mdash; ELV Regulation Dec 2025</a></td><td>Recycled content mandate</td></tr>
            <tr><td><a href="https://www.maximizemarketresearch.com/market-report/automotive-acoustic-material-market/11403/" style="color:var(--atn-light-blue);">Maximize Market Research &mdash; Acoustic Materials</a></td><td>Market size forecast</td></tr>
            <tr><td><a href="https://www.byd.com/eu/electric-cars/dolphin" style="color:var(--atn-light-blue);">BYD Europe &mdash; Dolphin</a></td><td>Target vehicle platform</td></tr>
        </tbody>
    </table>
</div>

</div><!-- /container -->

<div class="footer">
    <p>&copy; 2026 Autoneum Germany GmbH &ndash; Gundernhausen &nbsp;|&nbsp; - CONFIDENTIAL - &nbsp;|&nbsp; PET Foam Deep-Dive Annex to CEO Paper V3 &nbsp;|&nbsp; Author: J.R.E. Glawion &nbsp;|&nbsp; March 2026</p>
</div>

</body>
</html>"""

with open(os.path.join(BASE, "03_Analysen", "EV_Acoustic_PET_Foam_DeepDive.html"), "w", encoding="utf-8") as f:
    f.write(pet_html)
print("OK  03_Analysen/EV_Acoustic_PET_Foam_DeepDive.html")

# ══════════════════════════════════════════════════════════════
# 2. DUAL-PILLAR INVESTMENT PROPOSAL
# ══════════════════════════════════════════════════════════════
dual_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gundernhausen Dual-Pillar Investment Proposal</title>
    {STYLE_BLOCK}
</head>
<body>

<div class="hero">
    <div class="hero-top">
        <div>
            <div class="hero-tag">Executive Investment Proposal &bull; Two Pillars, One Site</div>
            <h1>Gundernhausen <span>Dual-Pillar</span> Strategy <span class="vbadge">DECISION PAPER</span></h1>
        </div>
        <div style="text-align:right;">
            <div style="font-size:20px; font-weight:700; color:var(--atn-green); letter-spacing:1px;">AUTONEUM</div>
            <div class="classification">- CONFIDENTIAL -</div>
        </div>
    </div>
    <p class="hero-sub"><strong style="color:var(--atn-green);">Two complementary investments that transform Gundernhausen</strong> from a declining PUR foam site into Autoneum&rsquo;s European innovation hub. Pillar 1 (MJF 3D Printing) delivers fast ROI and funds Pillar 2 (EV Acoustic PET Foam) &mdash; the strategic anchor addressing a $17.6B market.</p>
    <div style="margin-bottom:14px; padding:12px 16px; background:rgba(184,196,0,.08); border:1px solid rgba(184,196,0,.25); border-radius:6px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
            <div>
                <div style="font-size:9px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--atn-green); opacity:.8;">Prepared by</div>
                <div style="font-size:16px; font-weight:700; color:var(--atn-white);">Jonas Roland Erwin Glawion</div>
                <div style="font-size:11px; color:rgba(255,255,255,.7);">Process Engineer &mdash; Autoneum Germany GmbH &ndash; Gundernhausen</div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:9px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--atn-green); opacity:.8;">Supporting Documents</div>
                <div style="font-size:10px; color:rgba(255,255,255,.6);">
                    <a href="../03_Analysen/Gundernhausen Innovation Strategies 2026.html" style="color:var(--atn-light-blue); text-decoration:none;">CEO Paper V3</a> &nbsp;|&nbsp;
                    <a href="../03_Analysen/HP_MJF_3D_Printing_DeepDive.html" style="color:var(--atn-light-blue); text-decoration:none;">MJF Deep-Dive</a> &nbsp;|&nbsp;
                    <a href="../03_Analysen/EV_Acoustic_PET_Foam_DeepDive.html" style="color:var(--atn-light-blue); text-decoration:none;">PET Foam Deep-Dive</a>
                </div>
            </div>
        </div>
    </div>
    <div class="hero-meta">
        <span>Autoneum Germany GmbH &ndash; Gundernhausen</span><span>|</span><span>March 2026</span><span>|</span><span>Confidential</span><span>|</span><span>Author: J.R.E. Glawion</span>
    </div>
</div>

<div class="key-numbers">
    <div class="kn"><div class="v">&euro;2.5&ndash;4.6<span>M</span></div><div class="l">Total Investment (Both Pillars)</div></div>
    <div class="kn"><div class="v">30&ndash;40<span>%</span></div><div class="l">Blended IRR</div></div>
    <div class="kn"><div class="v">12&ndash;24<span>Mo</span></div><div class="l">Payback (Pillar 1: 12Mo)</div></div>
    <div class="kn"><div class="v">$17.6<span>B</span></div><div class="l">Addressable Market</div></div>
    <div class="kn"><div class="v">300k</div><div class="l">BYD Vehicles/yr</div></div>
    <div class="kn"><div class="v">5,002<span>m&sup2;</span></div><div class="l">Available Space</div></div>
</div>

<div class="container">

<!-- THE TWO PILLARS -->
<div class="sh"><div class="tag">The Strategy</div><h2>Two Pillars, One Transformation</h2><p>Sequential, complementary investments that de-risk each other</p></div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:22px;">
    <div class="card card-s">
        <div class="ch"><div class="left"><div class="rank" style="background:var(--atn-green);">1</div><div><h3>MJF 3D Print Hub</h3><div class="sub">Quick Win &bull; Fast ROI &bull; Enabler</div></div></div><div class="badges"><span class="badge b-score">82/100</span></div></div>
        <div class="cb" style="grid-template-columns:repeat(3,1fr);">
            <div class="cm"><div class="ml">Invest</div><div class="mv g">&euro;520&ndash;580k</div></div>
            <div class="cm"><div class="ml">IRR</div><div class="mv g">35&ndash;50%</div></div>
            <div class="cm"><div class="ml">Payback</div><div class="mv g">12&ndash;18 Mo</div></div>
        </div>
        <div class="cr">
            <strong>What:</strong> HP MJF 5200 printer + Print Hub serving 10+ European Autoneum plants. 3D-printed jigs, fixtures, spare parts, tooling &mdash; including tooling for PET foam production lines.<br>
            <strong>Why first:</strong> Lowest investment, fastest payback, proves site can innovate. Revenue from Print Hub directly funds Pillar 2.
        </div>
        <div class="cp"><h4>Key Technologies</h4><div class="tags"><span class="tg tg-hot">HP MJF 5200</span><span class="tg">CadQuery + Claude</span><span class="tg">W&uuml;rth DIS</span><span class="tg">Zoo CAD</span></div></div>
    </div>

    <div class="card card-s">
        <div class="ch"><div class="left"><div class="rank" style="background:var(--atn-green);">2</div><div><h3>EV Acoustic + PET Foam</h3><div class="sub">Strategic Anchor &bull; Core Competency</div></div></div><div class="badges"><span class="badge b-score">92/100</span></div></div>
        <div class="cb" style="grid-template-columns:repeat(3,1fr);">
            <div class="cm"><div class="ml">Invest</div><div class="mv g">&euro;2&ndash;4M</div></div>
            <div class="cm"><div class="ml">IRR</div><div class="mv g">25&ndash;35%</div></div>
            <div class="cm"><div class="ml">Payback</div><div class="mv g">18&ndash;24 Mo</div></div>
        </div>
        <div class="cr">
            <strong>What:</strong> ANDRITZ needlepunch + thermoforming line for PET foam sandwich parts. Wheelhouse liners, underbody panels, carpets, frunk liners for BYD, Geely, Leapmotor.<br>
            <strong>Why strategic:</strong> $17.6B market, 92/100 score (highest), proprietary technology no Chinese supplier can match.
        </div>
        <div class="cp"><h4>Key Technologies</h4><div class="tags"><span class="tg tg-hot">ArmaFORM PET</span><span class="tg">ANDRITZ Needlepunch</span><span class="tg">Hybrid-Acoustics</span><span class="tg">ABC Process</span></div></div>
    </div>
</div>

<!-- WHY TOGETHER -->
<div class="qw">
    <h3>WHY BOTH TOGETHER &mdash; THE SYNERGY</h3>
    <div class="qt">MJF enables PET &bull; PET justifies the site &bull; Together they transform Gundernhausen</div>
    <div class="qw-grid">
        <div class="qw-item"><div class="qv">MJF &rarr; PET</div><div class="ql">Print tooling/jigs for PET foam lines</div></div>
        <div class="qw-item"><div class="qv">Fast ROI</div><div class="ql">MJF pays back in 12Mo, funds PET ramp</div></div>
        <div class="qw-item"><div class="qv">Shared Space</div><div class="ql">MJF in Halle 3, PET in Halle 2</div></div>
        <div class="qw-item"><div class="qv">One Team</div><div class="ql">280 employees retrained PUR &rarr; PET + AM</div></div>
    </div>
    <div class="qw-ex">
        <strong>Risk mitigation:</strong> If PET foam ramp is delayed (OEM nomination cycles), MJF Print Hub generates standalone revenue. If MJF demand is lower than expected, PET foam production is the primary revenue driver. Neither investment depends entirely on the other &mdash; but together they are 40% more valuable than apart.
    </div>
</div>

<!-- COMBINED ROADMAP -->
<div class="page-break"></div>
<div class="sh"><div class="tag">Roadmap</div><h2>Combined Implementation Timeline</h2></div>

<div style="background:var(--atn-white); border-radius:8px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,.05); margin-bottom:22px; border:1px solid var(--atn-light-grey);">
    <table>
        <thead><tr><th>Month</th><th>Pillar 1: MJF Print Hub</th><th>Pillar 2: PET Foam</th><th>Cumulative Invest</th></tr></thead>
        <tbody>
            <tr style="background:var(--atn-lightest-green);"><td><strong>1&ndash;3</strong></td><td>HP MJF 5200 ordered + site prep (HVAC, ATEX)</td><td>ArmaFORM material qualification, BYD RFQ prepared</td><td>&euro;520&ndash;580k</td></tr>
            <tr><td><strong>4&ndash;6</strong></td><td>First builds, Print Hub live, 10+ part types in production</td><td>ANDRITZ needlepunch line ordered, prototype tooling (MJF-printed!)</td><td>&euro;1.3&ndash;2.1M</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>7&ndash;12</strong></td><td>2nd printer (if util &gt;70%), W&uuml;rth DIS, inter-plant supply</td><td>Needlepunch installed, thermoforming line, BYD prototype parts</td><td>&euro;2.0&ndash;3.4M</td></tr>
            <tr><td><strong>13&ndash;18</strong></td><td>Generative design, AMR evaluation, full Print Hub</td><td><strong>BYD Szeged series supply begins</strong>, Geely/Leapmotor acquisition</td><td>&euro;2.5&ndash;4.6M</td></tr>
            <tr style="background:var(--atn-lightest-green);"><td><strong>19&ndash;24</strong></td><td>Payback achieved, Print Hub profitable</td><td><strong>PET foam payback achieved</strong>, second NP line evaluation</td><td>Payback zone</td></tr>
        </tbody>
    </table>
</div>

<!-- WHAT IF WE DON'T -->
<div class="box box-warn">
    <h3>What Happens If We Don&rsquo;t Invest?</h3>
    <ul>
        <li>PUR foam volume continues declining as ICE production shrinks &mdash; Gundernhausen becomes a cost center</li>
        <li>BYD, Geely, Leapmotor lock in European Tier-1 supply chains in 2026 &mdash; <strong>locked out for 5&ndash;7 year vehicle lifecycle</strong></li>
        <li>EU ELV recycled content mandate (15% in ~2031) forces OEMs to seek rPET suppliers &mdash; competitors who move first own the certified supply</li>
        <li>5,002 m&sup2; across 3 halls sits underutilized &mdash; 280 skilled employees at risk</li>
        <li>Autoneum loses first-mover advantage in EV acoustic + PET foam to competitors like Adler Pelzer, Grupo Antolin, IAC</li>
    </ul>
</div>

<!-- CTA -->
<div class="cta">
    <h2>Decision Request: Approve Dual-Pillar Investment</h2>
    <p>Pillar 1 (MJF) is a no-regret investment &mdash; fast payback, low risk, serves all plants. Pillar 2 (PET Foam) is the strategic bet that positions Gundernhausen as Autoneum&rsquo;s European EV acoustic hub for the next decade. Together, they transform a declining PUR foam site into a €10M+ revenue innovation center.</p>
    <div class="cta-stats">
        <div class="cs2"><div class="v2">&euro;2.5&ndash;4.6M</div><div class="l2">Total Investment</div></div>
        <div class="cs2"><div class="v2">30&ndash;40%</div><div class="l2">Blended IRR</div></div>
        <div class="cs2"><div class="v2">12 Mo</div><div class="l2">First Payback (MJF)</div></div>
        <div class="cs2"><div class="v2">92 + 82</div><div class="l2">Combined Score</div></div>
        <div class="cs2"><div class="v2">2026</div><div class="l2">Window Closes</div></div>
    </div>
</div>

</div>
<div class="footer">
    <p>&copy; 2026 Autoneum Germany GmbH &ndash; Gundernhausen &nbsp;|&nbsp; - CONFIDENTIAL - &nbsp;|&nbsp; Dual-Pillar Investment Proposal &nbsp;|&nbsp; Author: J.R.E. Glawion &nbsp;|&nbsp; March 2026</p>
</div>
</body>
</html>"""

with open(os.path.join(BASE, "04_Praesentationen", "Gundernhausen_Dual_Pillar_Investment.html"), "w", encoding="utf-8") as f:
    f.write(dual_html)
print("OK  04_Praesentationen/Gundernhausen_Dual_Pillar_Investment.html")

# ══════════════════════════════════════════════════════════════
# 3. PET FOAM FACTSHEET (add to existing factsheets folder)
# ══════════════════════════════════════════════════════════════
# Read existing factsheet CSS from the generator
exec(open(os.path.join(BASE, "_Tools", "generate_tech_factsheets.py"), encoding="utf-8").read().split("techs = []")[0])

# Use the page() function from the factsheet generator
pet_factsheet = page(
    title="EV Acoustic + <span>PET Foam Sandwich</span>",
    tag="Technology Factsheet 10 • Strategic Anchor Investment",
    subtitle="PET foam core + needlepunch nonwoven sandwich for EV acoustic parts. 100% recyclable monomaterial. EU ELV compliant. Autoneum proprietary Hybrid-Acoustics technology. Highest-scoring option (92/100).",
    phase="PHASE 2–3", cost_label="€2–4M",
    kn=[("92<span>/100</span>","Investment Score"),("$17.6B","Market by 2030"),("100%","rPET Recyclable"),("15%","EU ELV Mandate")],
    overview=("EV Acoustic PET Foam Sandwich — Autoneum's Strategic Future",[
        "PET foam core (ArmaFORM GR60/FR60) + needlepunch nonwoven face skins = lightweight acoustic sandwich",
        "Dual function: sound insulator (blocks transmission) + absorber (dissipates energy) in one monomaterial part",
        "100% PET monomaterial → closed-loop recyclable, EU ELV regulation compliant from day one",
        "30–40% lighter than equivalent PUR-based parts — EV range optimization",
        "Products: wheelhouse liners, underbody panels, door insulation, frunk liners, e-motor capsules, carpets",
        "Target customers: BYD Hungary (300k vehicles/yr), Geely/Volvo, Leapmotor/Stellantis, Chery, NIO",
    ]),
    how_it_works=("Production Process",[
        "<strong>Step 1 — Fiber preparation:</strong> rPET fibers (up to 70% recycled PET bottles) fed to carding/cross-lapping",
        "<strong>Step 2 — Needlepunch:</strong> ANDRITZ needlepunch line produces nonwoven face skins (30–4,200 gsm)",
        "<strong>Step 3 — Lamination:</strong> ArmaFORM PET foam core bonded with nonwoven skins via thermoplastic ABC process (no latex, no water)",
        "<strong>Step 4 — Thermoforming:</strong> Sandwich heated to 185–210°C, pressed into 3D shape. Close to zero spring-back after cooling.",
        "<strong>Step 5 — Trimming:</strong> CNC router or waterjet trims to final contour",
        "<strong>Step 6 — QC + Ship:</strong> Dimensional check, weight verification, VDA 4902 labeling, ship to OEM (e.g., BYD Szeged ~700 km)",
    ]),
    auxiliaries=[
        ("Electrical","3-phase 400V for needlepunch + thermoforming press","Available"),
        ("Compressed Air","6–8 bar for pneumatic press, trimming","Available"),
        ("HVAC","Standard ventilation — no ATEX needed (PET is not combustible dust)","Available"),
        ("Floor Space","~500–800 m² for needlepunch + thermoforming + trimming + QC","Halle 2 available"),
        ("Water Supply","Not needed (ABC process is waterless — advantage over latex)","N/A"),
        ("rPET Fiber Supply","Post-consumer PET bottle flakes, recycled fiber suppliers","Procurement needed"),
        ("ArmaFORM PET Supply","Armacell — global supplier, multiple EU production sites","Procurement needed"),
    ],
    hardware=[
        ("ANDRITZ Needlepunch Line","Carding + cross-lapper + needlelooms (30–4,200 gsm)","€800k–1.5M"),
        ("Thermoforming Press","Dieffenbacher or existing press (185–210°C, PET-compatible)","€300k–600k (if new)"),
        ("Lamination Station","PET foam + nonwoven bonding via thermoplastic adhesive","€150k–300k"),
        ("CNC Router / Waterjet","Trimming thermoformed parts to final contour","€100k–200k"),
        ("Thermoform Tooling","Per product variant — steel/aluminum molds","€30–80k per tool"),
        ("QC Equipment","3D scanner, weight scale, acoustic impedance tube","€50k–100k"),
    ],
    software=[
        ("CAD / CAM","Part design + trimming programs (existing SolidWorks/CATIA)","Existing"),
        ("Apriso MES","Production tracking, quality data, Kanban integration","Existing + extension"),
        ("ArmaFORM Thermoform Simulation","Armacell provides forming simulation support","Via supplier"),
        ("ANDRITZ ProWin","Web weight regulation for needlepunch consistency","Included with line"),
    ],
    gundernhausen=("Why Gundernhausen Is the Perfect Site",[
        "<strong>Existing expertise:</strong> 280 employees with decades of NVH + foam + textile experience — transferable to PET",
        "<strong>Existing thermoforming:</strong> Current presses may be reusable for PET foam (ArmaFORM compatible) — saves €300–600k",
        "<strong>MJF synergy:</strong> Print Hub produces jigs, fixtures, tooling inserts for PET production lines — 2-day tooling vs 6 weeks",
        "<strong>5,002 m² available:</strong> Halle 2 for PET foam production, Halle 3 for MJF Print Hub — clean separation",
        "<strong>EU ELV compliance:</strong> 100% rPET monomaterial = built-in recycled content certification from day one",
        "<strong>BYD logistics:</strong> Gundernhausen → BYD Szeged ~700 km — realistic JIT corridor for acoustic parts",
        "<strong>Score: 92/100</strong> — highest of all 11 investment options evaluated in CEO Paper V3",
    ]),
    sources=[
        ("Armacell — ArmaPET Technology","https://www.armacell.com/en-BH/armapet-technology","PET foam core"),
        ("Autoneum Pure.","https://www.autoneum.com/pure/","Product portfolio"),
        ("ANDRITZ Automotive Nonwoven","https://www.andritz.com/campaign-nonwoven-en/nonwovens-automotive-technology","Needlepunch"),
        ("EU ELV Regulation Dec 2025","https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/circular-economy-council-and-parliament-strike-deal-on-rules-for-vehicle-circularity-and-management-of-end-of-life-vehicles/","Regulation"),
    ],
)

with open(os.path.join(BASE, "06_Technologie_Factsheets", "10_EV_Acoustic_PET_Foam.html"), "w", encoding="utf-8") as f:
    f.write(pet_factsheet)
print("OK  06_Technologie_Factsheets/10_EV_Acoustic_PET_Foam.html")

print("\nAll 3 documents generated successfully!")
