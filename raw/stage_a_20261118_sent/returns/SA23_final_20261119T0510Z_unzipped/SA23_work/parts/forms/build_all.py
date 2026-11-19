#!/usr/bin/env python3
"""Recreate registers from manual assessments in the required dependency order.

This does not classify sources, reread manuscripts or change recorded judgments.
The provenance audit follows build_tables and manual_quality; it also accepts
the separated final registers for an idempotent provenance-only rerun.
Narrative prose and physical source read logs are retained as authored files.
"""
from pathlib import Path
import subprocess,sys
P=Path(__file__).parent
for name in ['build_claims.py','build_tables.py','build_refs.py',
             'compute_checks.py','build_directions.py','manual_quality.py',
             'audit_problem_origins.py','build_fate_audit.py',
             'build_concordance.py','finalize_registers.py','validate.py']:
    subprocess.run([sys.executable,str(P/name)],check=True)
