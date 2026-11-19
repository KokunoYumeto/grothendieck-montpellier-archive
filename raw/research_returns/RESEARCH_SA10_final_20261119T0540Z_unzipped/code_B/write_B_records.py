"""Generate statement-level metadata for agent B; no mathematical inference is automated."""
from pathlib import Path
import csv, time

t0 = time.perf_counter()
base = Path(__file__).resolve().parents[1]
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); effort not separately exposed; run /root/homotopy_levels'
date = '2026-11-19'
rows = [
('B1.1','Closed-open sheaves are triples (L,E,E to i^-1 j_*L)','Proved','B_levels.tex B1.1','Enough points for sheaves on spaces','151/035-036','No normal triviality required for this exact recollement statement.'),
('B1.2','Tube systems classify constructible sheaves under the explicit nearby-germ comparison; exact Hom criterion','Proved under stated hypotheses','B_levels.tex B1.2','B1.1; adjunction','151/035-036','Criterion holds for the stated compact conical tube bundles; ordinary groupoids also require monodromy hypotheses.'),
('B1.3','An unconditional one-stage pro-tube formula for arbitrary infinite local-system stalks','Refuted','B_levels.tex B1.3','B1.1','151/028;151/035-036','Hawaiian earring, singleton closed stratum, infinite stalk N and two-point open local system. No uniform representative exists.'),
('B1.4','Inertia invariants and long exact sequence; aspherical base and link imply aspherical total tube','Proved','B_levels.tex B1.4','Fibration homotopy exact sequence','151/033-036','Connected fibre for surjectivity; connecting homomorphism must vanish for inertia to equal pi_1 of link.'),
('B1.5','Necessary and sufficient criterion for the actual pro-tube systems','Proved','B_levels.tex B1.5','B1.1; filtered bicategorical colimits of categories','151/035-036','Restriction r on germ local systems must be an equivalence and all explicitly defined mu maps must be bijective.'),
('B2.1','Shape in Pro(Spaces) preserves colimits of infinity-topoi','Known with derivation','B_levels.tex B2.1','Lurie HTT 7.1.6.15; BGH 4.2.1; Hoyois 5.1','151/030;151/043','Apply to the full actual open-cover descent diagrams in A.1, stage by stage; do not commute an arbitrary infinite colimit through a pro-limit.'),
('B2.2','Shape of an arbitrary bicategorical colimit of ordinary topoi is the homotopy colimit of shapes','Refuted','B_levels.tex B2.2','B2.1; finite bar calculation','151/043','Set <- C2-Set -> Set has bicategorical pushout Set, but shape pushout suspension BC2 has H_2=Z/2.'),
('B2.3','Quinn homotopy pushout, normal fibration comparison and exact correction to L2','Known under stated hypotheses; unrestricted L2 refuted','B_levels.tex B2.3','Quinn 2.1;2.4;3.1','151/032;151/043','Metric closed tame pair; source holink fibration is additional. Cylinder topology and ordinary homotopy-pushout comparison are made explicit.'),
('B2.4','Plane and sphere constructible-sheaf topoi are contractible; sphere tube span still reconstructs S2','Proved','B_levels.tex B2.4','B1.2;B1.4; classifying-space calculation','151/036-041','Covariant exit category is opposite to the manuscript presheaf-category convention.'),
('B3.1','Constructible n-truncated sheaves are functors on h_(n+1) Exit; finite-stratum induction','Known with truncation proof and explicit induction','B_levels.tex B3.1','Lurie HA A.9.3;A.9.16;A.9.7;A.7.1;A.8.14','151/035;151/041-043','Paracompact locally singular-shape conical P-space, P ACC. Finite induction uses conical charts and complementary recollements; infinite case is cited rank induction.'),
('B3.2','Constructible groupoid stacks and exit-path 2-functors; exact truncation interpretation of L3','Known with derived restriction','B_levels.tex B3.2','B3.1; Treumann 7.13;7.14','151/041-043','Set level retains pi_0 of exit mapping spaces, stack level pi_1; whole link pi_1 can still enter the set-level boundary action.'),
('B3.3','Gerbe gluing on the sphere yields H2(S2,A)=A for every discrete abelian group A','Proved','B_levels.tex B3.3','B3.2; effective 2-descent; torsor monodromy','151/041-043','Includes the gauge quotient; extension presentation requires choices and the constant abelian band.'),
('B4.1','A full span of groupoids determines a two-stratum homotopy pushout when every component piece is K(pi,1)','Proved; premise of B.4 refuted','B_levels.tex B4.1','B2.3; natural Sing to fundamental-groupoid nerve equivalence','151/033-035;151/041;151/044','No additional invariant is needed for the span itself. The prompt confuses it with the ordinary constructible-sheaf topos.'),
('B4.2','Full spatial flag diagram reconstructs X; all pairwise aspherical incidence links permit coherent groupoid assembly','Proved under stated hypotheses','B_levels.tex B4.2','B3.1; BGH 2.7.3;2.7.4; Lurie HA A.9.4','151/033-035;151/044','Explicit restriction functors, comparison natural isomorphisms and equation B4.8; whole normal links alone do not imply pairwise asphericity (stratified 4-ball).'),
('B4.3','Forgetting gluing coherence changes the assembled space despite identical local groups and homomorphisms','Proved','B_levels.tex B4.3','B4.2; circle-bundle clutching; tetrahedral chain computation','151/044','Hopf bundle S3 versus S2 x S1; full groupoid diagram includes the Cech 2-cocycle.'),
]
with (base/'RESULTS_B.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']); w.writerows(rows)

events=[]
for row in rows:
    sid=row[0]
    typ='targeted proof check'
    if sid in ('B1.1','B1.3','B1.4','B2.2','B2.4','B3.3','B4.1','B4.3'):
        typ='independent re-proof'
    events.append((sid,date,who,typ,row[2]+': '+row[6]))
events += [
('B2.2',date,who,'computation or formal certificate','check_B_finite.py: C2 group laws, 8 associativity triples; normalized bar differentials d1=0,d2=2,d3=0,d4=2; H1=Z/2.'),
('B4.3',date,who,'computation or formal certificate','check_B_finite.py: tetrahedral sphere 4 vertices,6 edges,4 faces; rank boundary2=3; nonzero pairing -1 proves cocycle not a coboundary.'),
('SA10-C3-04',date,who,'independent re-proof','Confirmed in B1.4. Connecting-map qualification and connected-fibre scope retained.'),
('SA10-C3-05',date,who,'independent re-proof','Confirmed in B2.4; covariant exit category has initial point, whereas presheaf convention uses its opposite.'),
('SA10-C3-06',date,who,'independent re-proof','Confirmed in B2.4; this does not refute reconstruction from the full groupoid span, as shown in B4.1.'),
('SA10-C3-07',date,who,'independent re-proof','Confirmed in B3.3 for discrete abelian constant A; neutralization gauges do not identify distinct classes.'),
('SA10-8',date,who,'used and rechecked in this run','B3.1-B3.2 give exact modern comparison; study line132 must read representations of h1 Exit, not F equals the exit category.'),
('L2',date,who,'refuted, with the refined statement\'s id','B2.1-B2.3. Holink fibration alone omits tameness; ordinary-topos bicategorical colimit principle is false. Infinity-topos shape preserves actual colimits without this geometric hypothesis.'),
('L3',date,who,'used and rechecked in this run','B3.1-B3.3. Correct theorem under stated conical hypotheses; the phrase pi1 of links must distinguish the groupoid boundary-action diagram from pi1 of exit mapping spaces.'),
('PROMPT-B.4-last-sentence',date,who,'refuted, with the refined statement\'s id','B4.1. R5 demonstrates failure of the constructible-sheaf topos, not failure of the aspherical groupoid span; 151/041 explicitly says the fear was unfounded.'),
('B3.1',date,who,'targeted proof check','Replaced an initially overstrong local-link/global-undercategory identification by conical chart descent and the explicit recollement induction of HA A.9.3.'),
('B1.5',date,who,'targeted proof check','Tested necessity with terminal L, giving restriction r; after normalizing via r, identity-base fibres are discrete and force bijectivity of mu.'),
('B2.3',date,who,'targeted proof check','Read Quinn cylinder convention; top-end product collars are cofibrations, so his double cylinder has the ordinary homotopy-pushout weak type.'),
('Woolf2009-Theorem4.3',date,who,'carried as background without fault found','Opened corrected arXiv v3. Constructible-sheaf classification is Theorem4.3 in the body, despite stale introduction reference4.6. Not used as a substitute for infinity-exodromy.'),
]
with (base/'CHECK_EVENTS_B.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['statement_id','date','who','type','outcome']); w.writerows(events)
print('Statement rows:',len(rows))
print('Check event rows:',len(events))
print('elapsed_seconds',round(time.perf_counter()-t0,6))
