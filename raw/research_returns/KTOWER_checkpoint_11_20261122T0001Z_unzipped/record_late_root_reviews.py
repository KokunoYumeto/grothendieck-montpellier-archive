"""Freeze root's completed whole-proof readings and one fresh small replay."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, shutil, subprocess, sys

B = Path(__file__).resolve().parent
D = B / 'evidence/root_late_arithmetic_review'
D.mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
proofs = {
    'evidence/lean_chain/quadratic_evaluation_limits.tex':
        '8703fc171d24eb2104993897089224d3d77fa1c45461add6b467d8671e2bc491',
    'evidence/lean_chain/cohen_heat_cycle_limit.tex':
        'fc225f00d48f647a95c396e3c658401e699954675ac77f60103f5efd33beb432',
    'evidence/unitary_audit/reducible_comparison/actual_source_pairing_audit.tex':
        '6b724b90e260f0a6b45a6e2e91435bf874f25ace9f9e1a7f5fb208e237b3168c',
}
for name, expected in proofs.items():
    source = B / name
    assert sha(source) == expected, name
    target = D / source.name
    if target.exists():
        assert target.read_bytes() == source.read_bytes()
    else:
        shutil.copyfile(source, target)
script = B / 'evidence/lean_chain/quadratic_evaluation_control.py'
assert sha(script) == 'f22b51b5e31993e210d18c3852e792db032145fa0c5a5651611b0d9f31147a28'
shutil.copyfile(script, D / script.name)
subprocess.run([sys.executable, str(D / script.name)], check=True)
fresh = D / 'quadratic_evaluation_control.json'
assert fresh.read_bytes() == (B / 'evidence/lean_chain/quadratic_evaluation_control.json').read_bytes()
sources = {
 'evidence/main_gate/literature/character_unit_followup/Choi_Choie_Richter_2011.pdf':
 'Section2 complete definitions and Propositions1-2 printed1457, full Theorem2 statement1458; underlying foundational proofs imported.',
 'evidence/unitary_audit/reducible_comparison/primary/milne_ADT_2006.pdf':
 'II.3.1(b), II.3.3 complete statements177 and full short Corollary3.3 proof178; global duality theorem imported.',
 'evidence/unitary_audit/reducible_comparison/primary/mccallum_sharifi_pairing.pdf':
 'Section4 assumptions10, full Proposition4.2 proof11 and following lambda/cyclicity scope12; no whole-paper proof claim.',
 'evidence/unitary_audit/reducible_comparison/primary/sharifi_paireis.pdf':
 'Hypothesis1 and immediate Gorenstein scope6, Hypothesis2 at11, full Theorem5.6 statement/proof25-26, Theorem5.7 sketch and Corollaries5.8-5.9 at27; source computations imported, not rerun.',
}
now = datetime.now(timezone.utc).isoformat()
report = {
 'date_utc': now, 'reviewer': '/root; run KTOWER',
 'model': 'GPT-6 Astra Pro', 'effort': 'not exposed',
 'verdict': 'PASS', 'whole_written_proofs_read': True,
 'whole_control_script_read': True, 'proofs': proofs,
 'fresh_frozen_copy_replay': {'script_sha256': sha(D/script.name),
     'report_sha256': sha(fresh), 'byte_equal_author': True,
     'scope': '48 finite orthogonality checks, exact Euler factors, 12 beta3 controls; same-character sum28 at p31,q311,m105. Not a uniform computation.'},
 'primary_source_scope': {name: {'sha256': sha(B/name), 'read': scope}
                          for name, scope in sources.items()},
 'additional_primary_web': {
   'source': 'William Stein, Modular Forms: A Computational Approach',
   'url': 'https://wstein.org/books/modform/stein-modform.pdf',
   'read': 'Complete definitions printed92, Proposition6.1 printed93 and Theorem8.23 with parity definitions printed141.',
   'refs': ['turn685050086view0', 'turn364595489view0', 'turn364595489view1'],
   'scope': 'Published dimension and period-pairing inputs imported; no local PDF or independent foundational proof claimed.'},
 'checks': [
   'Full cuspidal parity dimension strictly exceeds number of small quadratic rows; no implication for detection of the particular Eisenstein class.',
   'Hecke closure on an eigenvector preserves the exact evaluation ideal.',
   'Full finite quadratic convolution, imprimitive Euler factors, and separate-support limitation.',
   'All beta3 integrality cases, including d divisible by3; positive Fourier bound and d^5<=1600p^2 sufficient unit condition.',
   'Heat filtration induction, first exceptional indexp-2, Fermat recurrence and lower bound for last iterate.',
   'Local even-exponent parity excludes Tate-valued contractions, with correct Cartier dual.',
   'Kummer exact sequence for compact-support dual, unit line plus original class-group component.',
   'Exact normalized matrix product TP.4 and each TP.5 cross term; irreducibility does not remove higher off-diagonal compensation.'
 ],
 'limits': ['No field existence in the short window', 'No simultaneous two-twisted-unit theorem',
     'No nonzero higher arithmetic obstruction', 'No source-to-jet comparison',
     'No additional degree or rational component vanishing', 'No Lean build'],
 'movement': False,
}
rp = D / 'review.json'
rp.write_text(json.dumps(report, indent=2)+'\n')
ids = ['KT-SMALL-QUADRATIC-SPAN-LIMIT', 'KT-EISENSTEIN-HECKE-EVALUATION-IDEAL',
       'KT-BETA3-SHORT-WINDOW', 'KT-COHEN-SPECIAL-HEAT-FILTRATION',
       'KT-SOURCE-TATE-PAIRING-SCOPE']
with (B/'ROOT_CHECK_EVENTS.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid in ids:
        writer.writerow([sid, now, '/root; run KTOWER', 'GPT-6 Astra Pro', 'not exposed',
            'targeted proof check', 'PASS whole exact written proof; stated scope and imported inputs retained; no main arithmetic movement.', str(rp.relative_to(B))])
    writer.writerow(['KT-QUADRATIC-EVALUATION-CONTROL', now, '/root; run KTOWER',
       'GPT-6 Astra Pro', 'not exposed', 'computation or formal certificate',
       'PASS fresh frozen-copy complete small control, byte-identical report; no uniform nonvanishing.', str(fresh.relative_to(B))])
    for sid in ['STEIN-PROP6.1-THM8.23','CCR2011-PROP1-2','MILNE-ADT-II3.1-II3.3',
                'MCCALLUM-SHARIFI-PROP4.2','SHARIFI-PAIREIS-THM5.6']:
        writer.writerow([sid, now, '/root; run KTOWER', 'GPT-6 Astra Pro', 'not exposed',
           'used and rechecked in this run', 'PASS exact source scope specified in review; no broader foundational proof or computational replay claimed.', str(rp.relative_to(B))])
print(json.dumps({'verdict':'PASS', 'report_sha256':sha(rp), 'proofs':len(proofs)}))
