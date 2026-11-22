"""Stage the exact review16 comparison after all post23 promotions."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
manifests = sorted(root.glob('parts/*/post23_research/integration_manifest*.json'))
assert len(manifests) == 10, [str(x) for x in manifests]
verified = []
all_labels = []
for path in manifests:
    m = json.loads(path.read_text())
    audits = m['audit_scope'] if isinstance(m['audit_scope'], dict) else m['audits']
    assert set(audits) == {'root', 'B', 'C', 'D'}
    assert hashlib.sha256((root / m['path']).read_bytes()).hexdigest() == m['sha256']
    assert '[Candidate:' not in (root / m['path']).read_text()
    assert '\\input{' + m['path'] + '}' in (root / 'parts/D/paper_D.tex').read_text()
    verified.append(dict(path=m['path'], sha256=m['sha256'], audit_manifest=str(path.relative_to(root))))
    all_labels.extend(m['labels'])
assert len(all_labels) == len(set(all_labels)) == 20

path = root / 'parts/D/unresolved_D.tex'
source = path.read_text()
start = source.index('\\paragraph{Current scope after the global finite-puncture synthesis.}')
end = source.index('\\subsection{D.1 and D.2(ii):', start)
current = r'''\paragraph{Current scope after the original-boundary projective synthesis.}
Only general D.1, general D.2(ii), and their dependent residual L8
remain requested open rows. The checked local projective theorem
\ref{D:SNC-general-projective-quadratic-count} covers arbitrary SNC
exceptional graphs, including secondary residues, and
\ref{D:complete-local-projective-growth-all-dimensions} gives the
stated complete local dimensional and finite-normalization closure.
Theorem~\ref{D:local-divisorial-tame-projective-growth} also treats
every fixed complete normal local surface with an original reduced
divisorial tame boundary. Its constant is independent of rank,
coefficient field and horizontal root order; exceptional wild images
are retained.

Theorems~\ref{D:global-finite-puncture-projective-growth} and
\ref{D:global-original-boundary-projective-growth} prove the
unrestricted-period quadratic projective count for every fixed
normal proper surface with its original boundary convention.
The stated dimensional, controlled-centre and finite-normalization
closures are given by
\ref{D:global-projective-finite-puncture-closure} and
\ref{D:global-tame-projective-controlled-closure}.
Every defining-characteristic Lie simple-product quotient is
finitely generated in these scopes. Hereditary constants linear
in the degree of arbitrary finite covers remain unproved.

The restricted alternating factorial count in
\ref{D:finite-puncture-local-orbit-factorial-count},
\ref{D:fixed-local-quotient-alternating-count}, and
\ref{D:alternating-dimensional-normalization-closure} uses the
whole fixed detecting-surface local groups. It requires the
square-sum of uncontrolled orbit sizes to be $O(n\log(n+1))$.
Orbits factoring through any chosen fixed finitely generated
local quotients may be omitted; in particular, nilpotent-image
and prime-to-$p$-image orbits may have arbitrary size.
Disconnected covers and the stated dimensional and nonnormal
closures are included. Unrestricted alternating multiplicities
remain open.

In the one-curve radially tame scope,
\ref{D:tame-projective-automorphism-crowns} and
\ref{D:normal-subgroup-projective-crowns} permit unbounded field
image; the classical and exceptional recognition results include
all defining-characteristic Lie families in that same scope.
Wild outer covers, other crown geometries, uncovered
cross-characteristic families, and higher-dimensional boundaries
outside the proved reductions remain unresolved. The following
record retains successive approaches and their later closures;
a historical intermediate gate is not a new open item.

'''
path.write_text(source[:start] + current + source[end:])

path = root / 'code/assemble.py'
source = path.read_text()
lines = source.splitlines(keepends=True)
global_scope = '; unrestricted-period projective representations satisfy q^(C r²) for every fixed normal proper surface with its original divisorial tame boundary, and every fixed complete normal local surface pair; the stated finite-puncture, controlled-centre and finite-normalization closures apply; every defining-characteristic Lie simple-product quotient is finitely generated in these scopes'
alternating_scope = '; selected alternating multiplicities have polynomial simple-order bounds when the square-sum of uncontrolled whole detecting-surface local orbit sizes is O(n log(n+1)); arbitrary nilpotent-image and prime-to-p-image orbit blocks may be omitted, with the stated disconnected-cover, dimensional and normalization closures; unrestricted alternating factors and general crowns remain open'
global_paragraph = 'After checkpoint23, one global projective reduction is proved for every fixed normal proper surface with the original boundary convention. A fixed geometric-generic curve detects original covers and obtains its full local types from fixed original complete local punctures, original divisorial tame pairs, and tame cyclic groups. The local-pair proof controls the actual coefficient gerbe while allowing unbounded horizontal root orders; normalized marked sources and invariant Hom intervals remove those orders from the coordinate bound. The fixed-local-type curve theorem gives q^(C r²) globally without bounding geometric Brauer period or exceptional wild images. The stated dimensional, controlled-centre and finite-normalization closures and all defining-characteristic Lie simple-product conclusions belong to this same reduction. All twenty new supporting and consequence units have four actual proof/source audits; their exact hashes and reading scopes are recorded. Arbitrary-cover hereditary constants and full finite generation remain separate gates.'
alternating_paragraph = 'The restricted alternating reduction counts actual finite local sets, paying the ambiguity of their modular permutation bases. The fixed-formal curve fibre bound gives n^(A n) covers when the square-sum of uncontrolled whole completed-local orbit sizes is O(n log(n+1)). Orbits factoring through fixed finitely generated local quotients may be omitted. In particular arbitrary nilpotent-image and prime-to-p-image orbit blocks are controlled by the known Suzuki Theorem1.2 and Grothendieck--Murre Theorem9.2 inputs, with exact opened-source scopes. Disconnected covers, fixed detecting-surface dimensional transfer and finite normalization preserve the bound. This remains one restricted alternating reduction; it does not prove unrestricted alternating multiplicities.'
for i,line in enumerate(lines):
    if line.startswith('post23_global_scope='):
        lines[i] = 'post23_global_scope=' + repr(global_scope) + '\n'
    elif line.startswith('post23_global_labels='):
        labels = [x for x in all_labels if 'alternating' not in x and x not in ['D:local-permutation-orbit-energy']]
        lines[i] = 'post23_global_labels=' + repr('; '.join(labels)) + '\n'
    elif line.startswith('post23_alternating_scope='):
        lines[i] = 'post23_alternating_scope=' + repr(alternating_scope) + '\n'
    elif line.startswith('post23_alternating_labels='):
        labels = ['D:local-permutation-orbit-energy', 'D:finite-puncture-local-orbit-factorial-count', 'D:fixed-local-quotient-alternating-count', 'D:alternating-dimensional-normalization-closure']
        lines[i] = 'post23_alternating_labels=' + repr('; '.join(labels)) + '\n'
    elif line.startswith("'After checkpoint23, one complete global projective reduction is proved."):
        lines[i] = repr(global_paragraph) + ',\n'
    elif line.startswith("'The restricted alternating reduction uses actual finite sets,"):
        lines[i] = repr(alternating_paragraph) + ',\n'
source = ''.join(lines).replace('original divisorial-boundary projective representations at unbounded geometric period,', 'hereditary projective constants for arbitrary finite covers,')
assert 'All ten supporting and consequence units' not in source
assert 'The original divisorial-boundary and arbitrary-cover hereditary gates remain open.' not in source
path.write_text(source)

assessment = dict(
    assessment_actor='root', assessment_staged_utc=now, formal_review_completed=False,
    movement=True, requested_status_changes=[], requested_open=['general D.1', 'general D.2(ii)', 'residual dependent L8'],
    strict_main_gate_reductions=[
        'One strict global projective reduction after review15: unrestricted-period q^(C r²) projective counts now hold for every fixed normal proper surface with the original divisorial tame boundary, retaining all exceptional wild images. Fixed complete local divisor-pair counts and a single detecting curve with fixed full local sources supply the transfer. The stated dimensional, controlled-centre and finite-normalization closures and every defining-characteristic Lie simple-product quotient belong to this same reduction.',
        'One strict restricted-alternating reduction after review15: factorial cover counts and polynomial alternating-kernel multiplicities now hold when the square-sum of uncontrolled whole fixed detecting-surface local orbit sizes is O(n log(n+1)). Orbits factoring through fixed finitely generated local quotients may be omitted, including arbitrary nilpotent-image and prime-to-p-image orbits. Disconnected-cover, dimensional and finite-normalization extensions are consequences of this same reduction.'
    ],
    verified_files=verified, all_required_proof_audits_completed=True,
    remaining_strongest_gates=[
        'Unrestricted alternating simple-quotient multiplicities outside the proved whole-local-group orbit-energy criterion; the remaining orbit images need be neither nilpotent nor prime-to-p, and need not factor through any fixed finitely generated local quotient.',
        'Hereditary projective constants linear in the degree of arbitrary finite covers, beyond the proved geometric cover classes. Fixed-pair unrestricted projective counts on complete local punctures, local original-divisor tame pairs and global original-boundary proper surfaces are now proved; no degree-linear constant follows automatically.',
        'Uncovered cross-characteristic Lie families with order divisible by the ground characteristic and outside the proved linear/order and projective/order criteria.',
        'General monolithic nonabelian crowns outside the proved radially tame one-smooth-exceptional-curve faithful-linear and faithful-projective families. Unbounded tame field-image actions and all defining-characteristic Lie families are covered in that same restricted crown scope. Wild radial permutation quotients, arbitrary outer covers, other realizations and other geometries remain unresolved.',
        'Full finite generation for the residual nonprojective normal proper surface punctures and original-boundary tame quotients. Simple-product counts alone do not settle all crowns.',
        'Higher-dimensional boundary reductions outside finite omitted loci, controlled exceptional centres and the proved projective-model full-generation criteria; nonnormal D.2 scope retained.',
        'Dependent residual L8.'
    ],
    auxiliary_not_movement=[
        'The different/Frobenius lattice, fixed detecting-curve construction, fixed-full-local-type curve atlas, local-pair H2 and horizontal residue lemmas, coefficient-gerbe comparison, marked-root atlas, and all global/dimensional/simple-family consequences are prerequisites or consequences of the same global projective reduction, not additional movements.',
        'The alternating energy inequality, fixed finitely generated local quotients, nilpotent and prime-to-p recognition, disconnected-cover count and normalization/descent closure belong to the same restricted alternating reduction, not additional movements.',
        'All complete-local arbitrary-SNC and one-curve unbounded-field crown results already counted at review15 remain historical inputs and are not counted again.',
        'Searches, citation precision, audit refreshes, compilation, actual image inspection and lossless historical image re-encoding are not research movement.'
    ],
    report_summary='Two strongest main gates are strictly smaller after review15: unrestricted-period projective growth now covers the original-boundary global proper-surface groups, and a factorial bound controls alternating quotients under the precise whole-local-group orbit criterion. All supporting and closure results are counted with those two reductions. General D.1, D.2(ii) and residual L8 remain open.')
out = root / 'code/output/review16_main_assessment.json'
assert not out.exists()
out.write_text(json.dumps(assessment, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Review16 assessment staged before the scheduled review\n\nINCOMPLETE. ' + now + '. Twenty post23 units are fully promoted, audited and integrated. Two strict reductions are grouped in the staged comparison: original-boundary global projective growth and the restricted alternating factorial criterion. No requested row changes. This staging is not the formal review and creates no archive; review16 remains due18:10UTC before checkpoint24.\n')
print(json.dumps(dict(utc=now, verified_files=len(verified), new_units=len(all_labels), requested_status_changes=[], formal_review_performed=False, archive_created=False), indent=2))
