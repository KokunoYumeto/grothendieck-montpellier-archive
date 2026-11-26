#!/usr/bin/env python3
"""Rerun the unconditional Target15 certificate on isolated copies.

No discovery bnf/nf object is loaded, and no preserved input is modified.
Requires PARI/GP2.17.4 and python-flint0.9.0 (or compatible exact APIs).
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ap=argparse.ArgumentParser()
ap.add_argument('--gp',default='/tmp/fermat_sections_20261125/external_tools/pari/pari-2.17.4/Olinux-x86_64/gp-dyn')
args=ap.parse_args()
source=Path(__file__).resolve().parent
names=[
    'fresh_checks_target15_field_basis.gp',
    'fresh_checks_target15_generator_embeddings.gp',
    'fresh_checks_target15_principal_witnesses.txt',
    'fresh_checks_target15_prime_counts.tsv',
    'fresh_checks_target15_verify_exact.gp',
    'fresh_checks_target15_analytic_bound.py',
]
digests={n:hashlib.sha256((source/n).read_bytes()).hexdigest() for n in names}
with tempfile.TemporaryDirectory(prefix='fresh_target15_verify_') as tmp:
    work=Path(tmp)
    for name in names:
        shutil.copy2(source/name,work/name)
    verifier=work/'fresh_checks_target15_verify_exact.gp'
    verifier.write_text(verifier.read_text().replace(
        '/tmp/fermat_sections_20261125/research/',str(work)+'/'))
    gp=subprocess.run([args.gp,'-f','-q',str(verifier)],
                      cwd=work,capture_output=True,text=True,timeout=900)
    text=gp.stdout+gp.stderr
    if gp.returncode or 'PASS unconditional exact certificate' not in text:
        raise RuntimeError(text)
    if '***   at' in text:
        raise RuntimeError(text)
    py=subprocess.run([sys.executable,str(work/'fresh_checks_target15_analytic_bound.py')],
                      cwd=work,capture_output=True,text=True,timeout=120)
    if py.returncode:
        raise RuntimeError(py.stdout+py.stderr)
    analytic=json.loads((work/'fresh_checks_target15_analytic_bound.json').read_text())
    assert analytic['all_assertions']=='PASS' and not analytic['GRH_used']
    readrows=lambda p:[tuple(map(int,s.split())) for s in p.read_text().splitlines()]
    expected=[r for r in readrows(work/'fresh_checks_target15_prime_counts.tsv') if r[0]**r[1]<=5000]
    actual=readrows(work/'fresh_checks_target15_verified_counts.tsv')
    assert sorted(expected)==sorted(actual)
    assert sum(c for p,f,c in actual)==592
    assert digests=={n:hashlib.sha256((source/n).read_bytes()).hexdigest() for n in names}
    print(json.dumps({
        'all_assertions':'PASS','preserved_inputs_unchanged':True,
        'exact_verifier_output':gp.stdout,
        'root_discriminant_lower_bound':analytic['extension_root_discriminant_lower_ball'],
        'root_discriminant_M':analytic['M_root_discriminant_ball'],
        'prime_ideals':592,'principal_witnesses':590,
        'input_sha256':digests,
    },indent=2))
