#!/usr/bin/env python3
"""Run the parent's exact verifier after full code audit, preserving its outputs."""
from pathlib import Path
import sys
base=Path(__file__).resolve().parents[1]
root=base.parents[1]
source=root/'outputs/ss_contact_witness_03.json'
sys.path.insert(0,str(root/'code'))
for name in ('verify_ss_contact_geometry.py','verify_ss_contact_collisions.py'):
 original=root/'code'/name
 sys.argv=[str(original),str(source)]
 namespace={'__file__':str(base/'code'/name),'__name__':'__independent_audit__'}
 exec(compile(original.read_text(),str(original),'exec'),namespace)
