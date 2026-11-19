"""Evidence-level event log. A textual attribution audit is not promoted to a proof."""
from pathlib import Path
import csv,json,re
W=Path(__file__).resolve().parents[1]
C=json.loads((W/'claims.json').read_text());I=json.loads((W/'items.json').read_text())
E=[];WHO='GPT-6 Astra Pro; reasoning effort not exposed to worker; SA09/cote137'
def add(s,t,o):
 E.append({'statement id':s,'date':'2026-11-19','who(model,effort,run)':WHO,'type':t,'outcome':o})
 with (W/'CHECK_EVENTS.tsv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=['statement id','date','who(model,effort,run)','type','outcome'],delimiter='\t');w.writeheader();w.writerows(E)
proof='targeted proof check';used='used and rechecked in this run';background='carried as background without fault found';calc='computation or formal certificate';refuted="refuted, with the refined statement's id"
events={
1:(proof,'Checked degree-zero-upwards splitting and projective disk Hom formula for nonnegative complexes; damaged authorial opening remains unresolved.'),
2:(proof,'Checked preservation of the specified simplicial contraction by reduced powers and tensoring, then applied001. No general nonlinear homology-preservation claim.'),
3:(refuted,'Literal projective-only equality case fails for constant Z, q=q′=1. Refined statement in CL-SA09-137-003: strict support inequality or additional vanishing H_q; all hypotheses checked.'),
4:(used,'Checked weight and truncation scope against both occurrences. Full comparison map and coherent PD identification were not proved.'),
5:(proof,'Checked recursive decomposition with projective cycles, boundaries and homology; choices are noncanonical.'),
6:(proof,'Derived rank formula from Dold--Kan, nonnegative-coefficient growth bound and Euler evaluation; finite arithmetic confirms sample values.'),
7:(proof,'Checked tensor closure via integral disk/sphere models, Künneth, rank bound and base change. This also proves strict free closure under the source definition.'),
8:(calc,'Computed normalized Γ²K(Z,1): differential−2 in degrees2→1 and H₁=Z/2. Supports the authorial withdrawal; outputs/recompute.json, proof_audit.md§3.'),
9:(refuted,'Equal ranks do not classify projectives: R=Z[√−5], I=(2,1+√−5), invertible nonprincipal rank1. Refined CL-SA09-137-009 requires coefficient modules or freeness.'),
10:(proof,'Checked Newton-basis uniqueness, nonnegative realizability conditions and evaluation at−1. Integer-valued and integral-coefficient polynomial rings separated.'),
11:(proof,'Checked finite direct-sum/direct-summand transfer through normalization; bounded normalization is essential for the strict perfect version.'),
12:(refuted,'Infinite-rank contractible identity disk is derived-perfect but its terms are not finite. Refined CL-SA09-137-012 uses a chosen replacement/standard derived definition.'),
13:(refuted,'Two directions tested: unbounded contractible finite-free model has rank2^n; disjoint-prime homology has individually polynomial residue fibers but unbounded homology. Refined CL-SA09-137-013 records uniform/model conditions without asserting a new criterion.'),
14:(refuted,'Bounded normalized source cannot surject onto an unbounded normalized contractible target. Refined CL-SA09-137-014 retains a perfect replacement, omitting arbitrary-representative epimorphism.'),
15:(proof,'Checked PID Smith decomposition, invariant factors and degree shifts against sphere/disk maps. General Dedekind extension not proved.'),
16:(refuted,'One identity disk D₁(1) refutes the formula with deleted μ_i. Refined rank formula is in CL-SA09-137-016 and proof_audit.md§3.'),
17:(refuted,'D₁(2) and D₁(3) have identical numerical counts but different torsion homology. Refined CL-SA09-137-017 retains actual elementary divisors.'),
18:(proof,'Solved chain-map equations degree by degree; checked dy=0, dx=ny, qm=np, adjacent-degree maps and componentwise composition. Finite scalar examples saved.'),
19:(used,'Checked extension obstruction and matrix composition in the concrete PID category. Full abstract realization and all exactness axioms remain unproved.'),
20:(refuted,'Scalar-homogeneous nonadditive h:Q²→Q is a natural transformation on {Q}; colimit generation alone is not density. Refined CL-SA09-137-020 requires canonical density or an additive-envelope version.'),
21:(proof,'Checked finite additive-envelope matrix argument and finite-free End-module interpretation; no arbitrary infinite completion.'),
22:(used,'Read Isbell duality and checked Hom variance and finite-weight hypotheses. Broad restriction/essential-image claim not certified from mere presentations.'),
23:(proof,'Checked additive coefficient-functor recovery from finite models/disks where required kernels exist. No space reconstruction or unspecified nonlinear equivalence proved.'),
24:(background,'Read explicit programme and matched hypotheses of rational/E-infinity/binomial/affinization references. Exact strict manuscript reconstruction remains unproved.'),
25:(proof,'Checked universal walking-complex matrix extension and evaluation on generators, extending through finite sums.'),
26:(refuted,'Unconditional Karoubi claim fails over k₁×k₂ via idempotent(1,0). Refined CL-SA09-137-026 preserves the cancelled status and the later projective-freeness assumption.'),
27:(refuted,'Take X=C^{n+1}: same-index pairing has factors k and0. Refined CL-SA09-137-027 uses target C^{n+1}; this is a mathematical candidate, not an ink correction.'),
28:(proof,'Checked cochain-map representing object as kernel of du−ud and finite-free transpose. General tensor existence for nonfree finitely presented weights not assumed.'),
29:(background,'Opened Dold--Kan statement and read source Karoubi hypothesis; did not independently reprove the entire Dold--Puppe theorem.'),
30:(used,'Compared source Sex1--2 and later additions with exact-category axioms; they are not automatically equivalent axiom systems.'),
31:(proof,'Checked two-cone/kernel reconstruction for bounded nonnegative finite-free source, full faithfulness in additive target, equivalence when kernels exist. Hua2026 is a contemporary reported treatment; no Lean build run.'),
32:(proof,'Checked necessity on0→S_{n−1}→D_n→S_n→0 and the abelian-target lifting criterion. Arbitrary relative target formulation deliberately remains outside this check.'),
33:(refuted,'D₁(2) separates original P from the split-homology Q. Refined CL-SA09-137-033 records the incompatible source descriptions rather than inventing a single intrinsic theorem.'),
34:(proof,'Checked2:Z[0]→Z[0] is mono/epi but not invertible in finite-free complex category; kernel existence does not imply abelianity.'),
35:(proof,'Checked projective/injective disk Hom tests and degree-zero sphere exception. Q is not extension-closed in P; no full Ext identification certified.'),
36:(background,'Read the explicit on-doit/sauf-erreur claim. Derived-evaluation hypotheses and ambient exact/functor category remain obligations.'),
37:(proof,'Checked transported degreewise simplicial tensor, unit S₀ and sphere tensor decomposition up to acyclic summands; ordinary total tensor is distinguished.'),
38:(proof,'Checked types and coherence diagrams for lax multiplicative data; unit arrow is not an asserted isomorphism.'),
39:(used,'Checked generator reduction and the explicit lack of a unit in K. General structured-cochain equivalence was not proved.'),
40:(proof,'Checked monicity proves uniqueness only; supplied a conditional kernel-preservation factorization argument. Existence for the manuscript tensor and all coherence were not certified.'),
41:(calc,'Checked the interval Alexander--Whitney example(0 versus1) and read the source homotopy/sign scope. The reference E-infinity action was used as background, not independently reproved.'),
42:(used,'Checked coefficient limitation: characteristic0 does not imply a Q-algebra. No precise integral De Rham--Sullivan theorem extracted from the one-line conclusion.'),
43:(proof,'Checked one-sided distributivity in polynomial laws and type correction for precomposition. Nonlinear composition is not bilinear.'),
44:(calc,'Enumerated scalar equality λ^p=λ over finite fields; checked universal coefficient-algebra variable distinguishes T^p from T. Source retraction preserved.'),
45:(proof,'Checked conditional Yoneda/idempotent and unit arguments. Triadditivity and all-parameter coherence are retained as hypotheses, not inferred from scalar weights.'),
46:(proof,'Checked fold/zero maps give graded commutative multiplication under coherent exponential isomorphisms. Hopf extension is explicitly an earlier-run addition.'),
47:(proof,'Checked homogeneous co-Kleisli substitution via naturality/coassociativity and degree-one units. Contemporary Hua2026 report read; no full mixed-degree equivalence or Lean certificate asserted.'),
48:(proof,'Checked constants require separate degree-zero maps and unit condition; read authorial admission of omission.'),
49:(used,'Audited the source assertion against its actual listed structures and the opened precise partial treatment. Full arbitrary-category equivalence not proved.'),
50:(calc,'Computed PD iteration coefficient(pq)!/[p!(q!)^p], equal3 for p=q=2, and unit-ideal obstruction2γ₂(1)=1 over Z. Abstract PD construction remains a question.'),
51:(used,'Checked concrete module-law enrichment scope in Roby/SGA/Friedlander--Suslin, not a theorem for all abstract tensor-PD categories.'),
52:(used,'Matched printed source pages to Sullivan typescript printed112/105. Provenance check only; no attribution of these printed results to Grothendieck.')}
for n,(typ,out) in events.items():add(f'CL-SA09-137-{n:03}',typ,out+' See proof_audit.md and the claim record for locators.')

# Items all receive a documentary evidence event; mathematical events are separate.
for x in I:add(x['id'],background,'Checked attribution/scope against the original passage '+x['lines']+'. '+x['check_reason']+' This event is a text-evidence check, not a claim that the mathematical theorem was proved.')
for n,claim in [(1,25),(6,31),(7,32),(8,28),(11,33),(12,34),(13,35),(14,35),(17,37),(19,38),(20,38),(24,40),(25,41),(28,4),(31,43),(32,43),(33,44),(36,45),(37,45),(38,45),(40,47),(41,47),(42,48),(43,43)]:
 add(f'SA09-{n}',proof,f'Targeted mathematical component checked as described in CL-SA09-137-{claim:03}; the scope and remaining gaps in that claim are part of this event.')
for n,detail in {
26:'Interval Alexander--Whitney multiplication: f∪e=0,e∪f=1.',
46:'Universal α followed by PD iteration multiplies rank-one γ₄ by3.',
47:'PD on the unit ideal of Z would force2γ₂(1)=1.',
51:'Quadratic splitting equation has solution binom(t,2) in integer-valued polynomials and no integral-coefficient polynomial solution.',
60:'A(C₂)=Z[t]/(t²−2t): binom(t,2)=t/2 is not integral.',
61:'Γ_Z(Zx) lacks integral binom(x,2); Z lacks PD on unit ideal.',
62:'Newton leading coefficients give binomial product constants in gr Int(Z).',
63:'Equal leading symbols b₂ and b₂+t give different constants at1; positive-degree composition coefficient checked.'}.items():
 add(f'SA09-{n}',calc,detail+' Exact arithmetic saved in programs/recompute.py and outputs/recompute.json; general explanation in proof_audit.md.')

bib=(W/'references.bib').read_text()
for key,body in re.findall(r'@\w+\{([^,]+),(.*?)(?=\n@|\Z)',bib,re.S):
 ann=re.search(r'annotation = \{(.*)\},',body)
 add(key,background,'Opened source/metadata and checked the cited statement’s scope; not an independent verification of every proof. '+(ann.group(1) if ann else 'See bibliography entry.'))
assert {x['id'] for x in C+I}<=set(e['statement id'] for e in E)
print(json.dumps({'check_events':len(E),'claim_events':len(events),'item_text_events':len(I),'formal_builds_claimed':0,'computation_events_are_finite_arithmetic':True}))
