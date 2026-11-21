"""Merge actual check records and update the live question table."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
header=['statement_id','date_utc','who_model_effort_run','type','outcome']
old=list(csv.reader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
rows=[r for r in old[1:] if r and r[0].startswith('SRC-')]
for p in sorted((ROOT/'research').glob('CHECK_EVENTS_*.tsv'))+[ROOT/'checks/ROOT_CHECK_EVENTS.tsv']:
    for r in list(csv.reader(p.open(),delimiter='\t'))[1:]:
        if not r: continue
        if p.name=='CHECK_EVENTS_local_newvectors.tsv' and len(r)==8:
            event,actor,effort,date,statement,scope,result,notes=r
            typ='targeted proof check' if statement=='LN1-LN7' else 'used and rechecked in this run'
            r=[statement,date,f'{actor}; effort {effort}; DEG_L_20261121/lvalue_bounds/local_newvectors',typ,f'{event}: {scope}; {result}; {notes}']
        if len(r)!=5: raise ValueError((p,len(r),r))
        rows.append(r)
seen=set(); unique=[]
for r in rows:
    key=tuple(r)
    if key not in seen: unique.append(r);seen.add(key)
with (ROOT/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(header);w.writerows(unique)
qh=['id','source_locator','question','state','finding_ids','current_gate_or_scope']
qrows=list(csv.DictReader((ROOT/'QUESTIONS.tsv').open(),delimiter='\t'))
q={r['id']:r for r in qrows}
def put(id,loc,question,state,findings,gate):
    q[id]=dict(zip(qh,[id,loc,question,state,findings,gate]))
put('Q-T6','Prompt task1; sketch T6','Can source level alone determine the raw degree as a single character L-value?','REFUTED','T6.3; refined T6.10–T6.14','At fixed level multiplication of denominator-clearing maps changes raw degree by M^4; exact refined finite spectral formula retains all actual input data')
put('Q-T6-EXACT','Prompt task1; 032 Prop3.1 and §7','Exact Rallis expression for the degree of the specified polarized pushforward surface','PROVED','T6.1; T6.9–T6.14','Finite rank-two standard-L(1) norm sum with explicit Haar factor; finite Hecke-L(3/2) energy identity gives upper bound; reduced image divides by generic degree')
put('Q-T6-CHARONLY','Prompt degree premise; DEG_L T6.12–T6.15','Must all actual rank-two wedge source parameters factor through Hecke characters?','REFUTED','T6.15','A balanced holomorphic theta wedge and actual CM-Albanese surface degree have a contributing cuspidal GL2 source with nonzero Steinberg monodromy; no claim about isolated numerical values or a prescribed indecomposable switch relation')
put('Q-BOUNDS','Prompt task2; sketch Route2','Bound degrees uniformly along target Hecke movement','OPEN','B1–B20; T6.7–T6.15','B17 removes radial input ambiguity for an existing split theta vector; B19 gives exact integral CM Hom covolume and O(J) complexity in a fixed simple CM isogeny class; B20 shows reduced images of a fixed finite witness menu still have degree of order sqrt(J); target-dependent bounded witnesses remain')
put('Q-DIV','Prompt task4; sketch2.1,2.4','Obtain bounded division in open Weil families','OPEN','B6–B8; B19–B20; DIV1–DIV5; S-14; DER4; DER7','Bounded nonzero effective Weil witnesses on a dense set, or one weakly target-equivariant gluable semiregular object with full B-normalized character P(theta)+lambda t; DER4 gives fixed cycles in all ranks and DER7 gives a gerbe-order-independent multiplier in nonzero rank')
for id in ['Q-T6.12','Q-T6.13']:
    q[id]['state']='PROVED';q[id]['current_gate_or_scope']='Whole-proof checked; actual multiplicity copies and intertwiners retained; no automatic character factorization asserted'
new=[
('S-21','semireg_t7_proofs.tex','Can an arbitrary effective finite translation/tensor action make an equivariantly simple ample imaginary-quadratic secant seed fully semiregular?','REFUTED','All nonidentity Hochschild coefficient sectors vanish; induction-forgetting and categorical RR give Euler scaling; semiregularity requires ext0_G>=2+chi/(2|G|)>2; arbitrary algebraic B-field allowed'),
('B21','bounded_source_transport.md','Can target-dependent selection among bounded-degree source witnesses avoid Hecke index growth?','REFUTED','Entire bounded Hilbert family has uniformly finite stabilizers; every reduced transported witness has degree at least c(D0)sqrt J, matching the upper order; no intrinsic target-cycle lower bound'),
('S-19','semireg_t7_proofs.tex','The isolated-point genus-four secant seed for every parameter','REFUTED','Quantitative invariant ext2 at least24d+6>28; all linearizations for its translation action excluded; qualitative secant failure already known'),
('S-20','semireg_t7_proofs.tex','The cyclic partial-normalization genus-four seed for every parameter','REFUTED','Quantitative full-kernel dimension at least4d−3; known CY4 adjunction criterion and rank12 applied to the actual gluable simple complex'),
('LN7','local_fourier_period.md','Does a unit-bounded integral local test vector force a model Fourier period bounded below?','REFUTED','Primitive finite-ring Gauss sum gives magnitude q^(-m/2) with bounded Rallis norm; explicitly not the geometric Weil period'),
('B17','lvalue_bounds.md','Can split theta radial support be replaced without changing an existing global theta vector?','PROVED','Canonical one-shell section preserves the actual global vector by the Rallis norm identity; arithmetic integral-output size is retained'),
('B18','lvalue_bounds.md','Can the normalized generic Weil period of an integral witness tend to zero?','REFUTED','Period at least 1/R because the positive integral middle square on a torus is even; does not control a full-CM embedding coefficient before realization'),
('B19','lvalue_bounds.md','Compute the actual CM Hom covolume and a conductor-dependent witness bound','PROVED','Fixed primitive CM type and maximal-order reference; exact covolume proportional to core index J, witness degree O(sqrt J), signed complexity O(J); no uniform intrinsic bound asserted'),
('B20','fixed_witness_transport.md','Does passing to the reduced image remove index growth for a fixed simple-CM witness?','REFUTED','Generic degree equals the kernel intersection with its finite stabilizer; reduced image degree at least a fixed positive multiple of sqrt J for every integral isogeny'),
('S-17','semireg_t7.md','Tensor–determinant untwisting after a successful nonzero-rank deformation','PROVED','Exact inertia cancellation; effective Chern cycle and fixed-multiplier Hilbert locus produce common signed degree bound'),
('S-18','semireg_t7.md','Can canonical categorical induction remove a full semiregularity kernel?','REFUTED','Identity direct summand makes induction faithful on every morphism; natural trace map retains the original kernel'),
('DER5','derived_functors.md','Can arbitrary evaluation cones or nonzero-Euler convolution remove an existing full kernel?','REFUTED','Nonzero-rank tensor is faithful by graded trace; Mukai convolution identity makes ideal-diagonal transform faithful for every perfect input in positive dimension'),
('DER6','derived_functors.md','Can polarization-polynomial tensor corrections retain the Weil component and repair a full kernel?','REFUTED','Nonzero rank preserves the kernel; zero rank annihilates the primitive Weil component'),
('DER7','derived_functors.md','Remove gerbe-order dependence from the cycle multiplier in nonzero virtual rank','PROVED','Adams degree |r| and determinant sign cancel inertia exactly; N*=v|b beta0||r|^n, with a gcd refinement; the degree bound still depends on bundle generation'),
('T6.15','rallis_t6.md','Can a non-character rank-two parameter occur in an actual theta wedge and CM surface degree?','PROVED','Global compact U2 construction with split Steinberg monodromy, fixed holomorphic cocycle and toric extraction; balanced decomposable relation and CM-Albanese degree scope'),
('T6.14','rallis_t6.md','Exact dependence on finite adelic level','PROVED','Fixed adelic data on the full Shimura cover; all geometric integrals scale with actual covering degree'),
('B1a','lvalue_bounds.md','The actual archimedean factor and critical normalization','PROVED','Source infinity character trivial in compatible splitting; all-place gamma ratio (2pi)^(-[F:Q])'),
('B14a','lvalue_bounds.md','Exact split local estimate for arbitrary angular Schwartz inputs','PROVED','Character projector and weighted shell seminorm; ramified source characters and convergent tails included'),
('B16','lvalue_bounds.md','Upgrade the Weil projector to an exact rational Chow idempotent','PROVED','Uses canonical degree projector and Moonen multiplicative polynomial law; relative base smooth connected quasi-projective'),
('B15','lvalue_bounds.md','Quantitative upper bound along a polarized Weil Hecke orbit','PROVED','Explicit linear bound in isogeny degree without scalar transport; square-root bound in aligned flat-class case'),
('B13','lvalue_bounds.md','Bound generic degree for a fixed surface mapping to a simple target','PROVED','General-type image and canonical-volume bound; simplicity retained'),
('B14','lvalue_bounds.md','Bound local Rallis factors from their actual Schwartz data','PROVED','Fixed-level unit-norm family has Z=M; shell-count and weighted-seminorm bounds and compact-torus bound proved'),
('S-13','semireg_t7.md','Can a single exponential repair the coherent pure-Weil semiregularity obstruction?','REFUTED','In the precise Q(i) fourfold setting, a line-bundle twist reduces to S-12'),
('S-14','semireg_t7.md','Does weak target-equivariant semiregularity with compatible full character imply bounded division?','PROVED','Conditional implication via Perry Th1.2 and DIV1; does not construct the required object'),
('S-15','semireg_t7.md','Do the canonical source-cover equivariant lifts remove a full object trace kernel?','REFUTED','Canonical deck and target-isogeny lifts preserve a kernel; arbitrary relinearizations are not excluded'),
('S-16','semireg_t7.md','Realize any integral K-class by a bundle after adding a polarization exponential','PROVED','Finite bundle resolution and globally generated kernel construction; no semiregularity conclusion'),
('DER1','derived_candidates.md','Necessary polarization-discriminant condition for a Hermite–Einstein replacement','PROVED','Strict p1^2−2rp2>0; positive sums of exponentials excluded only for the Hermite–Einstein route'),
('DER2','derived_candidates.md','Does the globally generated evaluation syzygy remove a full trace kernel?','REFUTED','Ideal-diagonal Fourier–Mukai functor injects degree-two self-Ext and preserves its semiregularity kernel'),
('DER3','derived_candidates.md','Does the canonical opposite-exponential syzygy repair semiregularity?','REFUTED','It passes the strict numerical test while retaining the established kernel by DER2'),
('DER4','derived_candidates.md','Construct a fixed signed-cycle bound after weak equivariant deformation, including virtual rank zero','PROVED','Homogeneous Adams operation on the explicit finite gerbe descends; bundle realization and c_n degeneracy loci give fixed multiplier and degree'),
]
for fid,fn,question,state,scope in new:
    put('Q-'+fid,'DEG_L_20261121 / '+fn+' / '+fid,question,state,fid,scope)
with (ROOT/'QUESTIONS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=qh,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(q.values())
print(f'{len(unique)} check events; {len(q)} question rows')
