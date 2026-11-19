#!/usr/bin/env python3
"""Display source lines for semantic review; performs no classification or verdicts."""
from pathlib import Path
import argparse, hashlib, datetime
p=argparse.ArgumentParser()
p.add_argument('path');p.add_argument('start',type=int);p.add_argument('end',type=int);p.add_argument('--output',required=True)
a=p.parse_args();path=Path(a.path);lines=path.read_text().splitlines()
s=f'SOURCE {path.name}; SHA256 {hashlib.sha256(path.read_bytes()).hexdigest()}; 1-based lines {a.start}–{min(a.end,len(lines))}\n'
s+='\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,min(a.end,len(lines))+1))+'\n'
Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(s);print(s)
