"""Editorial promotion of the independently audited checkpoint-11 results."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, shutil, time

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
draft = root / 'notes/C_finish_global_function_WG_draft.tex'
source = draft.read_text()
before = hashlib.sha256(draft.read_bytes()).hexdigest()
assert before == '6d885f2a9bd0d0470dcf85206802fc31f45fb0359c83b1e8f4c479c9b6e01b16'
for label in ['C:global-function-finite-algebra-algorithms', 'C:global-function-central-simple-algorithms']:
    source = source.replace('Lemma~\\ref{' + label + '}', 'Theorem~\\ref{' + label + '}')
target = root / 'sections/C_finish_global_function_WG.tex'
target.write_text(source)
after = hashlib.sha256(target.read_bytes()).hexdigest()
shutil.copyfile(root/'notes/C_global_function_WG_flat_union_audit.tsv', root/'checks_C_global_function_WG_peer_audit.tsv')
fields = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
data = [
 ['C:global-function-coefficient-WG', 'Complete ordinary canonical indecomposable form and split WG coordinates with tensor and exterior algorithms over all explicit global function field finite coefficient algebras and the stated effective henselizations', 'Proved', str(target.relative_to(root)), 'C:global-function-finite-algebra-algorithms; C:global-function-hermitian-isometry; C:nonnoetherian-henselian-lifting; C:effective-coherent-henselization-WG', '', 'Actual division factors and all hermitian isometry decisions are computed, including the quaternion skew-hermitian global obstruction. Least Gram-pair coordinates are a decidable literal set. Actual Hom residue images and lifted forms are used. No infinite input or efficiency claim.'],
 ['C:global-function-henselization-WG', 'All affine local henselizations at explicitly supplied closed points over explicit global function fields and all stated effective valuation henselizations have the full ordinary WG answer', 'Proved', str(target.relative_to(root)), 'C:global-function-coefficient-WG; C:C1-henselization-access; C:lexicographic-valuation-henselization-WG', '', 'Includes singular nonreduced affine bases and arbitrary finite rank lexicographic valuation domains with supplied global function field residue. The exact-access proofs use field arithmetic and finite kernels, not the C1 property.']
]
with (root/'results_C_global_function_WG.csv').open('w', newline='') as f:
    w=csv.writer(f);w.writerow(fields);w.writerows(data)
with (root/'checks_C_global_function_WG_own_proof.tsv').open('w', newline='') as f:
    w=csv.writer(f, delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
    for row in data:
        w.writerow([row[0],now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); inherited effort; RESEARCH_SA17_FINISH/root','targeted proof check','OWN written-proof verification, not an independent audit. Checked the full finite algebra and henselian access arguments, actual radical quotients and lifts, canonical least codes and cancellative Gram pairs, projective R-duals, reference-adjoint signs, balanced tensor products and exterior quotients without factorials. Independent full audit is in checks_C_global_function_WG_peer_audit.tsv. The only post-audit changes replace two incorrect environment names Lemma by Theorem.'])
cpath=root/'sections/C.tex'; c=cpath.read_text()
c=c.replace('\\input{sections/C_finish_global_function_hermitian}\n', '\\input{sections/C_finish_global_function_hermitian}\n\\input{sections/C_finish_global_function_WG}\n')
needle='criterion and the further explicit families below.\n'
assert needle in c
c=c.replace(needle, needle+'''Proposition~\\ref{C:noncoherent-positive-boundary} gives a normal local,
noncoherent, nonvaluation positive example. Thus regular coherence is
not necessary in the full arbitrary-ring problem; this example is
already obtained by the filtered-colimit theorem.
Theorem~\\ref{C:shallow-full-support-three-torsion} bounds the remaining
mixed shallow classes by three, but does not prove their vanishing
or the existence of a nonzero class.
''')
cpath.write_text(c)
upath=root/'sections/unresolved.tex'; u=upath.read_text()
needle='Thus the remaining task concerns coefficient bases outside the completed\n'
assert needle in u
u=u.replace(needle, '''Theorems~\\ref{C:C1-henselization-WG} and
\\ref{C:function-field-henselization-WG} extend the ordinary answer to
the stated effective, possibly imperfect, $C_1$ residue fields and
all explicitly supplied finite towers over $\\overline{\\mathbf F}_p(t)$.
Theorem~\\ref{C:effective-coherent-henselization-WG} uses finite matrix
kernels instead of Noetherianity. Its lexicographic valuation examples
have nonzero infinitely divisible elements and cannot be flat local
unions of Noetherian local stages, so they remove a further family.
Theorem~\\ref{C:C1-coherent-products-WG} gives exact bounded product
coordinates with the full square-class coordinate at symmetric factors.

Theorems~\\ref{C:global-function-field-arithmetic}--
\\ref{C:global-function-hermitian-isometry} now compute factorization,
all places, actual division algebras, reduced norms, and every hermitian
isometry problem over explicit global function fields of odd
characteristic, including inseparable towers and wild division degree.
The quaternion skew-hermitian argument retains the rank-one norm
obstruction, rather than invoking false local-global isometry.
Theorems~\\ref{C:global-function-coefficient-WG} and
\\ref{C:global-function-henselization-WG} consequently give complete
ordinary canonical representation and form coordinates, equality,
tensor products and exterior operations over every finite-dimensional
coefficient algebra over those fields, all stated effective local
henselizations, and effective valuation henselizations. No division-index
or hermitian-isometry oracle remains in this family.

'''+needle)
u=u.replace('reduced singular bases remain unclassified.','''reduced singular bases remain unclassified.
The mixed shallow classes are now proved to be killed by three in
Theorem~\\ref{C:shallow-full-support-three-torsion}; this is not a
vanishing theorem. Proposition~\\ref{C:noncoherent-positive-boundary}
shows that regular coherence is not necessary among arbitrary rings,
but its positive example was already covered by filtered colimits.''')
upath.write_text(u)

rpath=root/'code/finish_report.py'; r=rpath.read_text()
lines=r.splitlines()
updates={
'C.1': ('Open all-ring classification; exact regular-coherent and valuation criterion and coherent modular-locus sufficiency', 'C:regular-coherent-criterion; C:valuation-domain-criterion; C:coherent-regular-modular-locus; C:allrings_obstructions; C:allprime_squarezero_criterion; C:ramified_squarezero_criterion; C:cyclotomic_flat_criterion; C:dyadic_normal_node_criterion; C:ramified_exponent_two_node; C:shallow-full-support-three-torsion; C:noncoherent-positive-boundary', 'For every regular coherent ring, polynomiality is equivalent to characteristic zero and the unit isomorphism Z to K0; all valuation domains of arbitrary rank are included. For coherent rings, regular coherence is needed only at positive-characteristic points. The previous exact square-zero and node criteria remain. A normal local noncoherent nonvaluation positive example shows that this sufficient regularity is not necessary in the unrestricted problem; it is already covered by filtered colimits. Mixed shallow cubic classes are killed by three, but neither their vanishing nor a nonzero class is proved. The smallest ramified node and mixed shallow directions remain open. Failed detector searches and nonperfect underived Schur lifts do not count as main-gate movement.'),
'C.3': ('Lambda criterion settled; full global function field arithmetic and WG algorithms added; arbitrary coefficient bases open', 'C:BO_affine_lambda; C:Om-canonical-WG; C:Om-finite-base-algorithm; C:all_algebraic_fields_WG; C:function-field-WG; C:profinite-WG; C:complete_algclosed_WG; C:arithmetic-henselization-WG; C:arithmetic-strict-henselization-WG; C:C1-henselization-WG; C:effective-coherent-henselization-WG; C:C1-coherent-products-WG; C:global-function-central-simple-algorithms; C:global-function-hermitian-isometry; C:global-function-coefficient-WG; C:global-function-henselization-WG', 'Special iff m<=2 or the base with2 invertible is a Q-algebra. Existing finite, algebraically closed, algebraic finite-field, effective C1, Artinian, complete, profinite and henselian answers remain. Ordinary algorithms now cover the specified C1-residue henselizations and local rings with finite matrix-kernel algorithms without Noetherianity; explicit higher-rank valuation examples lie outside flat unions of Noetherian local stages. Full square-class coordinates and explicit rank/degree bounds determine arbitrary products of the stated factors. Over every supplied finite global function field tower, including inseparable towers, we compute all places, CSA splitting/index/actual division factors, reduced norms, radicals and every hermitian isometry problem. The quaternion skew-hermitian rank-one norm obstruction is retained. These give decidable literal indecomposable and Gram-pair coordinates, equality, actual representatives, tensor and exterior algorithms for every finite-dimensional coefficient algebra and the stated effective affine and valuation henselizations. No division-index or isometry oracle remains there. Arbitrary-field access and coefficient bases outside the completed families remain open.')}
for i,line in enumerate(lines):
    for key,value in updates.items():
        if line.startswith(repr(key)+':'):
            lines[i]=repr(key)+':'+repr(value)+','
r='\n'.join(lines)+'\n'
marker='| `C_finish_ramified_higherpage_failure`'
at=r.index(marker)
r=r[:at]+'''| `C_finish_shallow_mixed_three_torsion` | 96 character-rotation/gauge identities and3,600 actual first-order extension/shear identities across multiplicities(1,0),(0,1),(1,1),(2,1),(1,2) | All pass;0.323237 s. The unrestricted three-torsion bound has a separate full proof and is not a mixed-class vanishing theorem. |
| `C_probe_shallow_pi3_bockstein` | Four rank-six signed L012/Q baselines at pi cubed:6,561+6,561+729+729=14,580 fixed-transposition tangent parameters; exact residual Bockstein image curvatures and primary multiplicities | No candidate detections;3.791522 s. A bounded exploratory search only; no additive detector or class-vanishing theorem is inferred. |
| `C_finish_schur_nonperfect_boundary` | Two exact matrix-factorization identities and two syzygy identities; degree-two Schur rank10, symmetric-group corner rank2 and Schur column rank4; explicit triangular extension and regular-orbit quotient | All pass;0.112447 s. A separately written infinite periodic resolution proves that a polynomial representation class can have a nonperfect underived Schur lift. This rejects necessity of that proposed method, not the main C.1 criterion. |
| `C_finish_ramified_firstpi_curvature_zero` | All rank-one and rank-two involutions over the eight-element pi-cubed quotient:2 and112; all530 saved exact extensions and37,552 residual cycle vectors | Both first Bocksteins and both parity curvatures coincide;0.807807 s. The all-rank equality is separately proved. It rejects the proposed primary image-length detector, without deciding the ramified node. |
'''+r[at:]
rpath.write_text(r)

record={'timestamp':now,'scope':'editorial promotion and report update, not a new mathematical test','WG_audited_draft_sha256':before,'WG_compiled_source_sha256':after,'post_audit_changes':'Lemma to Theorem in two prerequisite references only','statements':[row[0] for row in data],'seconds':time.perf_counter()-started}
(root/'logs/C_checkpoint11_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
