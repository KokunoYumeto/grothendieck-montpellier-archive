#!/usr/bin/env python3
"""Locate requested visible statement headings in the current PDF for visual QA."""
import argparse
import datetime
import json
from pathlib import Path
import time
import fitz

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('label')
parser.add_argument('statements', nargs='+')
args = parser.parse_args()
started = time.perf_counter()
doc = fitz.open(root / 'RESEARCH_SA06_paper.pdf')
texts = [p.get_text() for p in doc]
result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'pdf_pages': len(doc),
          'statement_mentions': {s: [i+1 for i,t in enumerate(texts) if s in t]
                                 for s in args.statements}}
result['runtime_seconds'] = time.perf_counter()-started
(root/'logs'/f'{args.label}_page_locations.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
