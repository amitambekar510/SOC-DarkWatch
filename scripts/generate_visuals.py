#!/usr/bin/env python3
"""Generate a readable, synthetic six-step SOC-DarkWatch 2.0 README GIF."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets" / "darkwatch-workflow.gif"
OUT.parent.mkdir(parents=True, exist_ok=True)
W, H = 1200, 500
STAGES = [
    ("01", "MONITOR", "Authorized exposure intelligence",
     "Review approved public sources for organizational domains and brands.",
     "Input: example.invalid (fictional domain)"),
    ("02", "VALIDATE", "Analyst verification",
     "Check provenance, confidence, duplicates and false-positive risk.",
     "Output: unconfirmed finding, analyst review required"),
    ("03", "ENRICH", "Threat intelligence context",
     "Add relevant metadata and approved MISP indicators when available.",
     "Output: indicator context and source reference"),
    ("04", "CORRELATE", "Existing security stack",
     "Compare validated indicators with existing SIEM and firewall telemetry.",
     "Output: correlation note; no automatic incident claim"),
    ("05", "ESCALATE", "SOC case management",
     "Create a tracked case, assign an owner and document next steps.",
     "Output: DEMO-CASE-001 (synthetic)"),
    ("06", "DOCUMENT", "Audit evidence review",
     "Record investigation, approvals, remediation and review timestamps.",
     "Output: redacted evidence checklist"),
]
def font(size, bold=False):
    stem = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    p = Path("/usr/share/fonts/truetype/dejavu") / stem
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

frames = []
for i, (number, name, headline, detail, output) in enumerate(STAGES):
    im = Image.new("RGB", (W, H), "#081725")
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((22, 20, W-22, H-20), radius=24, fill="#102b3d", outline="#37bea9", width=3)
    d.text((58, 52), "SOC-DarkWatch 2.0", font=font(30, True), fill="#66e8cf")
    d.text((58, 100), "DEFENSIVE MONITORING  /  AUDIT-READY WORKFLOW", font=font(18), fill="#b8d4df")
    d.rounded_rectangle((58, 158, 150, 236), radius=16, fill="#1bc5ac")
    d.text((80, 175), number, font=font(37, True), fill="#09202b")
    d.text((174, 154), name, font=font(37, True), fill="#ffffff")
    d.text((175, 207), headline, font=font(24), fill="#9fe7dd")
    d.text((59, 268), detail, font=font(20), fill="#e1edf3")
    d.text((59, 312), output, font=font(18), fill="#bbd4df")
    for j, label in enumerate(("MONITOR", "VALIDATE", "ENRICH", "SIEM", "CASE", "AUDIT")):
        x = 58 + j*186
        d.rounded_rectangle((x, 365, x+169, 415), radius=10, fill="#20c5a9" if j <= i else "#34566a")
        bbox = d.textbbox((0,0), label, font=font(15, True))
        d.text((x+(169-(bbox[2]-bbox[0]))//2, 380), label, font=font(15, True), fill="#06232c" if j <= i else "#e4f0f4")
    d.text((59, 448), "ILLUSTRATIVE DATA ONLY  |  NOT A LIVE DARK-WEB FEED  |  NO COMPLIANCE CERTIFICATION", font=font(15), fill="#a8c1cf")
    frames.append(im)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=1200, loop=0, optimize=True)
check = Image.open(OUT)
assert check.n_frames == len(STAGES) and check.size == (W,H)
print(f"Validated {check.n_frames} frames: {OUT}")
