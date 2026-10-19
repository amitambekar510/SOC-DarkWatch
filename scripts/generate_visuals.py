#!/usr/bin/env python3
"""Generate a synthetic conceptual six-stage GIF for the SOC-DarkWatch README."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
OUT=Path(__file__).resolve().parents[1]/"assets"/"darkwatch-workflow.gif"
OUT.parent.mkdir(parents=True,exist_ok=True)
def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if Path(p).exists() else ImageFont.load_default()
stages=[
    ("01 / MONITOR","Authorized public exposure sources","Fictional example.invalid indicator"),
    ("02 / VALIDATE","Review confidence and provenance","Analyst confirms source and scope"),
    ("03 / ENRICH","Normalize indicator in TI repository","MISP tags, owner and case reference"),
    ("04 / CORRELATE","Check existing SIEM and controls","ELK alert + FortiGate context"),
    ("05 / ESCALATE","Create tracked SOC investigation","Severity, timestamps, assigned owner"),
    ("06 / EVIDENCE","Retain redacted audit artifacts","Review, remediation and closure"),
]
frames=[]
for idx,(title,subtitle,detail) in enumerate(stages):
    im=Image.new("RGB",(1100,440),"#081827")
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((22,20,1078,420),radius=20,fill="#123047",outline="#3aaf9e",width=3)
    d.text((55,53),"SOC-DARKWATCH   /   AUDIT-READY WORKFLOW",font=font(25),fill="#55e3cb")
    d.text((55,119),title,font=font(36),fill="#ffffff")
    d.text((55,176),subtitle,font=font(22),fill="#c8e0eb")
    d.text((55,215),detail,font=font(18),fill="#a3c0d0")
    for i in range(6):
        x=57+i*173
        d.rounded_rectangle((x,295,x+151,342),radius=11,fill="#27c5ac" if i<=idx else "#34546a")
        d.text((x+17,309),["MONITOR","VALIDATE","ENRICH","SIEM","ESCALATE","EVIDENCE"][i],font=font(15),fill="#061c27" if i<=idx else "#dceaf2")
    d.text((55,380),"SYNTHETIC DEMO • NOT LIVE DARK-WEB INTELLIGENCE • NO COMPLIANCE CERTIFICATION",font=font(14),fill="#91b1c2")
    frames.append(im)
frames[0].save(OUT,save_all=True,append_images=frames[1:],duration=1100,loop=0,optimize=True)
assert Image.open(OUT).n_frames==6
print(OUT,OUT.stat().st_size)
