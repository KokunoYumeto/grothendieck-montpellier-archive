"""Record completed, independently checked proofs; do not promote open parents."""
from pathlib import Path
import csv, datetime, json

root = Path(__file__).resolve().parents[1]
path = root / 'CHECK_EVENTS.tsv'
rows = list(csv.DictReader(path.open(), delimiter='\t'))
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
checks = [
    ('A1Q-root', 'source and derivation audit',
     'PASS: opened Petrov Cor4.10 p16 and Kawakami-Tanaka I Th6.3 p50 / II Th7.2 p56. Serre-duality and degree-zero specializations give precisely the negative H1/H2 required by A4c. DGJ independent source audit also passed. Target hypotheses retained.'),
    ('A2Z-root', 'independent re-proof',
     'PASS: integral mu-p torsor, normalization conductor from finite duality, ambient ramification determinant, adjunction and positive intersection contradiction. Opened Stacks47.15.8 and48.14.1. This excludes only the stated finite separable degree-p full-inverse-image construction.'),
    ('A2P-independent', 'independent re-proof',
     'PASS by DGJ after root derivation: quotient projective-bundle divisor class and K^p=rho*N give normal Q^p and relative canonical Q^(p-1). The effective normalization conductor of a nontrivial mu-p torsor is incompatible with ample normal bundle. Exact positive-dimensional base and relative-Frobenius section hypotheses retained. work/dgj/A2_p_linear_multisection_audit.md.'),
    ('F13cd-root', 'independent re-proof',
     'PASS: AS divisibility on the proper nodal closed fibre, uniform removal of unramified order, bounded cyclic cover, tame affine cocycles, monomiality and Shapiro. Stacks0A48 reopened. F13.6 geometric generator bound and general derived-length-three case remain unresolved.'),
    ('F13e-root', 'independent re-proof',
     'PASS: saturation degree, residue slope, etale component-degree scaling, projection formula and k+Bt=0 give the exact linear refined-Swan zero bound. No bound on subsequent cleanup complexity is inferred.'),
    ('F13f-root', 'targeted proof check',
     'PASS: under the explicit strict subunit cutoff, integral conductors vanish; tame induction and wild-inertia semisimplicity yield all-prime rank-linear metabelian-coefficient bounds. Existence of such a cutoff is not asserted.'),
    ('F13gh-root', 'independent re-proof',
     'PASS: opened Yatagawa Def2.1 and formula2.5 pp8-9 and Krishna-Majumder Cor9.6-9.7 plus Lemma9.11 pp55-57. Prime-to-p Swan coefficient has nonzero log residue and nonnegative intersection; negative definiteness forces a coefficient at least p. Witt contraction improves the uniform exponent to p^(e+1)>max(t_i), and F13f hypothesis to t_i<p. General cleanup gate remains.'),
    ('I7b-root', 'independent re-proof',
     'PASS: the existing-preimage finite-Ext correction works over arbitrary regular local A, giving an open quotient onto the differential image. Whole-source-column products preserve this topology and dense exactness. Conditional descent still requires the unproved continuous preceding-family map; broad I remains undecided.')
]
seen = {(r['statement_id'], r['outcome']) for r in rows}
added = 0
for ident, kind, outcome in checks:
    outcome += ' Details: work/root/audits_08.md.'
    if (ident, outcome) not in seen:
        rows.append(dict(statement_id=ident, date=now,
            who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited, not exposed',
            type=kind, outcome=outcome))
        added += 1
with path.open('w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=['statement_id','date','who','type','outcome'], delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
result = dict(time_utc=now, checks_considered=len(checks), added=added, events=len(rows))
(root / 'code/record_root_audits_08_output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
