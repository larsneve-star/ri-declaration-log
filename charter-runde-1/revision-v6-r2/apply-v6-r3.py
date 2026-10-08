#!/usr/bin/env python3
"""Rebuild editorial V6-R3 from pinned R2 and Annex D. Python 3 stdlib only."""
import argparse
import hashlib
import re
from pathlib import Path

def sha256(data): return hashlib.sha256(data).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--r2",required=True,type=Path)
    ap.add_argument("--annex",required=True,type=Path)
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--expected-sha256",default="")
    args=ap.parse_args()
    data=args.r2.read_bytes()
    annex=args.annex.read_text(encoding="utf-8")
    if b"\r" in data: raise SystemExit("Unexpected CR byte in R2")
    text=data.decode("utf-8")
    parts=re.split(r"^## (R3-[^\n]+)$",annex,flags=re.MULTILINE)
    count=0
    for i in range(1,len(parts),2):
        blocks=re.findall(r"```text\n([\s\S]*?)\n```",parts[i+1])
        if len(blocks)!=2: raise SystemExit("Bad OLD/NEW blocks for "+parts[i])
        old,new=blocks
        if text.count(old)!=1: raise SystemExit("Non-unique OLD for "+parts[i]+": "+str(text.count(old)))
        text=text.replace(old,new,1)
        count+=1
    if count!=17: raise SystemExit("Expected 17 explicit operations, got "+str(count))
    extras=[
      ("Status: V6-R2 PROPOSED TARGETED REVISION - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE.",
       "Status: V6-R3 EDITORIAL BUILT CANDIDATE - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE. V6-R2 remains the immutable reviewed input."),
      ("V6-R2 changes and translations are recorded in ANNEX-D-V6-R2.md and executable instructions.",
       "V6-R2 changes and translations are recorded in ANNEX-D-V6-R2.md and its instructions. V6-R3 proposed changes are recorded in ANNEX-D-V6-R3-BUILD.md; this is an editorial build, not an appointed compiler's formally admitted result.")
    ]
    for old,new in extras:
        if text.count(old)!=1: raise SystemExit("Non-unique metadata OLD: "+old)
        text=text.replace(old,new,1)
    output=text.encode("utf-8")
    digest=sha256(output)
    if args.expected_sha256 and digest.lower()!=args.expected_sha256.lower():
        raise SystemExit("FAIL: expected "+args.expected_sha256+" got "+digest)
    args.output.write_bytes(output)
    print("OK: operations=17 metadata=2 bytes="+str(len(output))+" sha256="+digest)
if __name__=="__main__": main()
