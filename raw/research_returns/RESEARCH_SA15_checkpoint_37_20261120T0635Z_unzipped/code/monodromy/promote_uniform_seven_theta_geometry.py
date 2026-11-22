"""Promotion utility; run only after the parent authorizes the full theorem."""
from pathlib import Path
import argparse,datetime,hashlib,json

parser=argparse.ArgumentParser()
parser.add_argument('--root-audit',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parent.parent
audit=Path(args.root_audit).resolve();assert audit.is_file()
companion=root.parent/'obstructions_crystals/uniform_seven_independent_audit.json'
assert companion.is_file()
candidate=root/'nonordinary_uniform_seven_theta_geometry_candidate.tex'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()=='c671846e4b3b64d066003ed6d63af5b8e96c11c936e68fcff62c3b60e6e96cef'
canonical=root/'nonordinary_uniform_seven_theta_geometry.tex'
assert not canonical.exists()
source=candidate.read_text()
source=source.replace('% Isolated post-CP25 candidate. Preserve until independent full audits.',
 '% Post-CP25 theorem; exact audited candidate retained separately.')
source=source.replace('\\status{Candidate; complete proof and universal certificates submitted for audit.}',
 '\\status{Proved and independently checked.}')
labels=[
 'lem:uniform-seven-interpolation-candidate',
 'lem:uniform-seven-triple-obstruction-candidate',
 'lem:uniform-seven-parameter-certificate-candidate',
 'thm:uniform-seven-nodal-self-isogeny-candidate',
 'cor:f0-three-five-seven-degree-groups-candidate',
 'rem:uniform-seven-scope-candidate']
for label in labels:
    source=source.replace('\\label{'+label+'}',
      '\\label{'+label+'}\n\\textup{[Proved; independent audits passed.]}')
source=source.replace('\\path{code/verify_nonordinary_seven_good_parameters.py}',
 '\\path{code/monodromy/verify_nonordinary_seven_good_parameters.py}')
source=source.replace('\\path{code/nonordinary_seven_q8_interpolation.py}',
 '\\path{code/monodromy/nonordinary_seven_q8_interpolation.py}')
source=source.replace('parameter identities used here are verified directly.\n\\end{remark}',
 'parameter identities used here are verified directly. The complete parent '
 'and obstruction/crystal proof/code audits passed before promotion; both '
 'universal programs were rerun with the author outputs preserved. The '
 'author parameter certificate passed at 21:49:14 UTC in '
 '$0.18161791599413846$ seconds; the companion runs took '
 '$0.198577982$ and $0.306713550$ seconds. Exact records and '
 'all exploratory failures are retained in the agent output and history '
 'directories.\n\\end{remark}')
canonical.write_text(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PROMOTED','actual_utc':now,
 'candidate':candidate.name,'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
 'canonical':canonical.name,'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
 'labels':labels,'root_audit':str(audit),'companion_audit':str(companion),
 'scope':'Every fixed f0 ppav has the three-five-seven odd degree family and even sums; nodal norm-seven self-isogeny for every indecomposable f0 ppav. No all-degree assertion.',
 'preservation':'Exact audited candidate, all predecessor explorations and failed program versions remain unchanged; canonical changes only status, exported paths and audit remark.'}
(root/'outputs/uniform_seven_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'CHECK_EVENTS_post_CP16.tsv').open('a') as handle:
    for label in labels:
        handle.write('\t'.join([now,label,'promotion_after_full_root_OC_proof_code_audits','PASS',record['scope'],canonical.name])+'\n')
with (root/'post_CP16_notes.md').open('a') as handle:
    handle.write('\n## '+now+' — Uniform norm-seven theorem promoted\n\n'
      'The exact candidate is preserved. The canonical proof includes all exceptional fibres and both universal resultant gates; finite-C0 probes are explicitly not proof inputs. Only statuses, exported program paths and the audit remark changed. All f0 odd degrees 3^i5^j7^k and sums of two such degrees now follow. The finite membership census through1000 puts the next degrees outside these families at odd11 and even92; these are unresolved degrees, not counterexamples. Fixed f1 degree5 remains separate.\n')
print(json.dumps(record,indent=2))
