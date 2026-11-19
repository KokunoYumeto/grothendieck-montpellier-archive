"""Record actual checks, separating source fidelity, proof and finite computation."""
from pathlib import Path
import json,csv
B=Path('/workspace/scratch/7feb9690b71f/SA08_work');P=B/'work/late'
DATE='2026-11-19';WHO='GPT-6 Astra Pro; effort not exposed by runtime; SA08/late'
items=json.loads((P/'items.json').read_text());claims=json.loads((P/'claims.json').read_text());refs=json.loads((P/'reference_verification.json').read_text())
C={int(c['id'].split('C')[-1]):c for c in claims};events=[]
def E(s,t,o,refined='',evidence='',who=WHO):
 events.append(dict(statement_id=s,date=DATE,who=who,type=t,outcome=o,refined_statement_id=refined,evidence=evidence))
for i in items:
 scope='Source-fidelity check, not a mathematical proof. '
 if not i['scans']:scope='Provenance/inventory check, not a mathematical proof or a check of unavailable external project files. '
 E(i['id'],'used and rechecked in this run',scope+i['check']+': '+i['check_reason'],evidence=i['lines']+'; source entries '+','.join(i['sources']))
for c in claims:
 E(c['id'],'used and rechecked in this run','The actual transcription passage, page status and exact claim-specific literature envelope were compared. '+c['fate']+' Reading the theorem is not recorded as an independent proof.',evidence=c['lines']+'; search families '+','.join(c['searches'])+'; refs '+','.join(c['refs']))

# Explicitly chosen mathematical proof checks. A nonempty prose field is not
# automatically elevated to proof: every row below names what was verified.
proofs={
205:('independent re-proof','Computed Gamma²(Psi) exactly as k --2→ k in degrees2→1; the ordinary-K interpretation fails overZ and the all-weight nonflasqueness assertion fails overQ in the standard model. The Pi/K ink remains uncertain.','§15'),
206:('independent re-proof','Legendre sum, digit-sum expression and ideal minimum proved over Z_p.','§1'),
207:('independent re-proof','Proved positive filtration at2 is constant, odd-prime cofinality, the finite exact minimization bound and the zero associated-graded piece.','§1'),
209:('targeted proof check','Checked the residual yyprime term in the cancelled odd extension and the factorial/Pascal identities; no unrestricted extension claimed.','§2'),
210:('targeted proof check','Substituted the proposed scalar-change map into sum Xi−pi and sum dXi. Continuity/completed extension is not proved by this algebraic check.','§2 and claim scope'),
211:('targeted proof check','Checked the CP² cup-square contradiction only after adding full positive-even PD descent; coefficient-ideal and weighted versions are excluded from the refutation.','§2'),
212:('independent re-proof','Constructed all four finite adjunction maps and checked inverses and the counit, with grading cutoffs explicit.','§3'),
213:('independent re-proof','Checked tS↪S for S=k[t],cutoff1: q sends it to tS→0, so q is not left exact.','§3'),
214:('targeted proof check','Verified the unit/full-faithfulness criterion componentwise, distinguishing degree-zero full faithfulness from all lower nonnegative components.','§§3–4'),
215:('independent re-proof','Proved weighted binomial rigidity for arbitrary coefficients using prime-local cofinal rows and local-global equality.','§4'),
216:('independent re-proof','Verified bounded Serre closure/non-coproduct closure and the Gamma_Fp extension counterexample for elementwise-tail annihilation.','§7'),
220:('targeted proof check','Derived finite adjunction and injective preservation from exact left inclusion; checked the component Ext formula.','§3'),
221:('independent re-proof','Constructed the triangular category over k[epsilon]/epsilon² and verified exact tau,i,kappa, full faithfulness, underived unit and nonzero higher derived section.','§6'),
222:('independent re-proof','Proved exact coefficient left adjoint L over arbitrary k; i and finite tau preserve injectives, giving the finite derived unit and induced-target Ext vanishing.','§5'),
224:('targeted proof check','The triangular counterexample also has exact kappa; this additional feature does not repair the false abstract inference. Authorial cancellations retained.','§6'),
225:('targeted proof check','Checked the derived-unit criterion for derived full faithfulness; underived full faithfulness alone is insufficient. The localizing replacement is separate.','§§5–7'),
228:('targeted proof check','Checked the standard left exactness of a right adjoint; unresolved grammatical subject prevents attribution of a definite false assertion.','claim-specific scope'),
232:('independent re-proof','Constructed mutually inverse counit/coaction maps for the ordinary cofree cotensor identity without flatness. The NON annotation remains unexplained.','§9'),
233:('independent re-proof','Proved (product Z) tensor Q misses the sequence1/n!, so ordinary base change fails for the completed product.','§9'),
235:('independent re-proof','Checked the flat primitive coalgebra Z⊕Q and P_i=2^iZ counterexample to arbitrary tensor/intersection exchange. The manuscript recursive construction is not globally refuted.','§9'),
237:('independent re-proof','Built additive cotensors and the right Kan-extension end from products and kernels; checked the ordinary adjunction, not a dg enhancement.','§9'),
239:('independent re-proof','Computed the full negative coefficient presentation as Q by prime-local cofinal rows and checked Hom_Z(Q,M), including noninjective evaluation at1.','§8'),
240:('targeted proof check','Checked Yoneda variance and finite-projective duality; no universal bidual conclusion.','§10'),
241:('independent re-proof','Category-of-elements construction and restriction prove the ordinary free-cocompletion universal property.','§10'),
242:('targeted proof check','Checked the normalization projector/surjection decomposition mechanism in an additive idempotent-complete target; full Delta is essential.','§10'),
243:('targeted proof check','Additive functors preserve the finite sums and split-idempotent diagrams used in Dold–Kan. No assertion for nonlinear functors.','§10'),
244:('targeted proof check','Expanded D² and verified the horizontal-degree sign cancels the two commuting cross terms.','§10'),
245:('targeted proof check','Checked the free-additive extension and the normalized chain universal property.','§10'),
246:('targeted proof check','The internal-Hom differential at degree0 gives precisely chain maps; H0 would quotient by homotopy.','§10'),
247:('independent re-proof','Checked the additive representable presentation and extension for Ab-valued presheaves.','§10'),
251:('targeted proof check','Computed the degree-one normalized rank of the levelwise tensor of DK(Z[1]) and compared it with the ordinary tensor.','§10'),
252:('targeted proof check','Evaluated natural transformations at id_A and reconstructed them by naturality; operations are set-valued and need not be additive in f.','§11'),
253:('targeted proof check','Checked positive-index block iteration of the canonical flat divided coproduct after the injective symmetric-tensor comparison; q=0 is separate.','§11'),
254:('targeted proof check','Verified the universal direct-sum inclusions encode addition and the convolution tensor map is lax; rank2 excludes a general isomorphism.','§11'),
255:('independent re-proof','Verified the nonflat counital cocommutative coalgebra, PD ideal and contradiction f²(e)=2u versus2g(e)=0 for every additive g.','§11'),
256:('targeted proof check','Checked canonical flat u_n and its composition identity; all tensor-injection arguments use A or Gamma^qA, not J.','§11'),
257:('targeted proof check','Verified the F2 alternative family only for positive-index composition and binomial products; explicitly checked failure at q=0 and of full additive naturality.','§11'),
260:('targeted proof check','Checked the determinant-sign component distinction and the missing-i rotation formula by an explicit scalar test.','§12'),
262:('targeted proof check','Schwarz-lemma stabilizer is the rotation group; the text itself replaces the full group and changes analytic to topological.','§12'),
263:('targeted proof check','Translations preserve the derivative and refute the unpointed normalization; pointed centered-disc normalization is a different statement.','§12'),
264:('independent re-proof','A holomorphic projective connection induces one on End0; projection onto the nonzero-degree line summand contradicts degree zero for a holomorphic line connection on a compact curve.','§12'),
276:('targeted proof check','Checked that changing valuation normalization by ramification e changes the lattice pairing by the stated1/e denominator.','SGA7IX10.5p445'),
279:('targeted proof check','Compared the inclusion and implication labels to their actual proof endpoints in the original publication. This is a consistency check, not an independent proof of semistable reduction.','SGA7IX3.5,3.8pp350,353'),
281:('independent re-proof','Summation by parts gives the2M tail bound; the explicit short sequence refutes the M bound from initial-sum control alone.','§13'),
282:('independent re-proof','Separated the period mean and bounded zero-mean part, retaining c_n↓0 and divergence for the converse.','§13'),
283:('independent re-proof','Derived the geometric partial-sum identity and uniform bound away from1.','§13'),
284:('targeted proof check','Checked primewise no-carry choices imply the binomial-factor family has gcd1; the result is already explicit in Cartanp271.','§1 and Cartan§7p271'),
285:('independent re-proof','Flat coalgebra divided coproduct, ideal evaluation and addition/scalar/product/iteration identities prove the stated convolution PD structure without assuming J flat.','§11'),
286:('independent re-proof','Completed exact L and negative Q presentations with their different variances. These verify existing manuscript assertions/earlier-run repairs.','§§5,8'),
287:('independent re-proof','For the explicitly changed localizing Serre closure, L kills the class, iI is injective/local, Q(iI) is injective, and the resolution computes derived recovery.','§7'),
289:('independent re-proof','DK(Z[1]) gives representable values0 andZ on point and interval respectively, despite both being contractible.','§14'),
290:('independent re-proof','CP² and S²∨S⁴ have chain-homotopy-equivalent free integral chains and different cup squares; no canonical strict chain-functor isomorphism is claimed.','§14')}
for n,(typ,outcome,where) in proofs.items():E(f'SA08-C{n}',typ,outcome,evidence='work/late/proofs.md '+where)

refutations=[
 (205,205,'The ordinary K(k,p) and unrestricted all-p nonflasqueness readings fail for the standard simplex quotient in weight2; the refined row retains the doubtful name and the derived nonlinear calculation.'),
 (208,206,'The weak-inequality iff fails at p=3,i=2; the exact difference formula supplies the correction.'),
 (213,213,'Unrestricted left exactness of q is false; refined right-exact-only statement and counterexample occur in C213.'),
 (216,287,'The elementwise-tail class is not Serre; C287 uses an explicitly different localizing Serre closure.'),
 (221,222,'The abstract derived inference is false even with exact kappa; C222 proves the special Gamma-tail case by exact L.'),
 (233,234,'Ordinary tensor does not commute with arbitrary completed products; a topology/continuous tensor specification is needed.'),
 (235,235,'Flatness alone does not justify an arbitrary descending-intersection interchange; the refined statement restricts exactly what has been refuted.'),
 (251,251,'The native strict tensor-identification reading is false; transported structure/comparison maps are the refined formulation.'),
 (254,254,'The unrestricted strong-monoidal Hom reading is false even for rank2 finite free coalgebras; lax convolution is correct.'),
 (255,285,'Unrestricted nonflat convolution PD existence is false; C285 gives the proved flat sufficient-hypothesis statement.'),
 (257,257,'Only positive-index, fixed-object uniqueness is refuted. q=0 composition and full additive naturality are explicitly excluded from this counterexample.'),
 (263,263,'Derivative-only unpointed uniqueness is false; pointing and a centered image disc are the refined normalization.'),
 (264,264,'The compact nonzero-degree split holomorphic bundle cannot carry the requested connection; the nonsplit jet comparison is not a textual emendation.'),
 (281,281,'The M remainder bound from initial partial-sum control alone is false;2M is the general corrected bound.')]
for n,r,o in refutations:E(f'SA08-C{n}','refuted, with the refined statement\'s id',o,refined=f'SA08-C{r}',evidence=C[n].get('proof_check','')+'; '+C[n]['computation'])
for c in claims:
 if c['computation'].startswith(('programs/late_computations','late_computations','programs/late_quadratic')):
  certificate=('programs/late_quadratic_normalization.py; logs/late_quadratic_normalization.json'
               if c['computation'].startswith('programs/late_quadratic')
               else 'programs/late_computations.py; logs/late_computations_output.json')
  E(c['id'],'computation or formal certificate','Exact finite computation executed and retained. Its finite range supplements, and does not replace, the general argument. '+c['computation'],evidence=certificate)

for r in refs:
 typ='used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found'
 E(r['key'],typ,r['verification_scope']+(' Access is unverified; no proof or full-text result check is claimed.' if r['note']!='verified' else ' Scope is exactly the inspected passage/metadata, not an independent re-proof of the entire source.'),evidence=r['url'])

for sid in ['SA08-C222','SA08-C286','SA08-430','SA08-431']:
 for run in ['SA08/root','SA08/early']:
  E(sid,'targeted proof check','Peer explicitly reported an independent review of the exact-L prime-local cofinal-row argument and the finite derived-unit consequence over arbitrary k. The review did not certify an unspecified infinite quotient or all multiplicative structure.',evidence='Collaboration messages19Nov2026: parent and early independently verified proofs.md §§5–6; attribution is to their reported review.',who='GPT-6 Astra Pro; effort not exposed by runtime; '+run)

# A later literal-quotation audit is a source-fidelity event, not another proof.
quotation_events=P/'quotation_CHECK_EVENTS.tsv'
if quotation_events.exists():
 with quotation_events.open() as f:
  events.extend(csv.DictReader(f,delimiter='\t'))

with (P/'CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,list(events[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
print(json.dumps({'events':len(events),'items_covered':len(items),'claims_covered':len(claims),'reference_keys_covered':len(refs),'proof_checks':len(proofs)},indent=2))
