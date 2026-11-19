#!/usr/bin/env python3
"""Document the exact OCR reading aid used on already rendered SGA5 pages.

This script reproduces the one-off subprocess loop executed on 2026-11-19.
It prints readings to the tool session; it intentionally saves no article text.
Temporary images must be deleted after reading and before a checkpoint.
"""
from pathlib import Path
import subprocess
base=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent46/temporary_public')
for page in [454,455,458,459,460,464,465]:
    p=base/f'page_{page}.png'
    if not p.exists():
        print(f'page{page}: temporary image deleted after completed reading')
        continue
    print(f'PDF zero-based page{page}')
    subprocess.run(['tesseract',str(p),'stdout','-l','eng'],check=True)
