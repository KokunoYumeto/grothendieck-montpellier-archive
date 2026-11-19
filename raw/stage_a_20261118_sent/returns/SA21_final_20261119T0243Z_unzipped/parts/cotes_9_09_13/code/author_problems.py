"""Manual consolidation of every explicit open step and work reminder in IX09--13."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
P=[]
def add(n,title,occ,his,today,art,why,worth,refs):
 P.append(dict(id=f'MP-SA21-9-{n:02}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs))
add(9,'Do the strengthened faithful-surjectivity conditions force an isomorphism?',
 ['156-9 scan66 J156-9-09:16–39 (insufficient inclusion)','scan67 same:49–81 (strengthened equality and faithfulness)','scan68 same:88–98 (explicit bijectivity question)','scans81–84 J156-9-10:257–273; J156-9-11:6–94 (later general criterion)'],
 'Under pairwise orthogonality faithfulness of α and the condition cF(ᾱα*(y))=cF{y}, where α*(y)={x:α(x)⊆cF{y}}, must α_*:ΣE→ΣF be bijective? The preceding inclusion-only argument is distinct and is corrected on scan67.',
 'Yes: the closed values cFα(x) preserve and reflect orthogonality and are join-dense in ΣF; Proposition2 then gives a unique ortholattice isomorphism. The inclusion-only version is false (P1).',
 'C-SA21-9-031/032, independent P1/P5. Classical Galois-completion ingredients: Birkhoff1948 IV §§6–7. A modern join-dense subset presentation appears in PasekaVetterlein2025 Proposition2.4, with a unique-zero convention requiring adjustment for the manuscript.',
 'The manuscript says the assumptions may be too strong and later proves the more general representation criterion; no external source was found explaining any historical abandonment.',
 'No new research is needed for the stated implication; it is worth making the internal resolution explicit in the companion commentary.',
 ['Birkhoff1948','PasekaVetterlein2025'])
add(10,'When does a raw correspondence commute with support closure and admit a pretranspose?',
 ['156-9 scans68–70 J156-9-09:98–201','scan72 same:250–265','scan73 same:286–337','scan75 J156-9-10:33–42','scan94 J156-9-12:201–219','scans95–97 same:225–355','crosslink: MP-SA21-9-08 from IX01–08; earlier formula(*) is the same closure issue'],
 'Does cFᾱcE(A)=cFᾱ(A) hold, and does its validity for every A characterize disjunctive correspondences? Can a reverse correspondence β satisfy α(x)⊥y iff x⊥β(y)? The marginal alternatives ask for closed membership fibers and closed γ(y).',
 'Exactly the equivalent conditions of corrected Proposition4: full closure commutation; a pretranspose; closed γ(y); inverse closed-membership fibers; or join preservation of fα together with fασE=cFα. Join preservation alone is insufficient. Every closed-valued compatible assignment comes from a unique join map.',
 'C-SA21-9-033/035/036/038/054, proofsP2–P4. Shmuely1974 gives the complete-lattice Galois background; DomenachLeclerc2001 Theorems4.1/5.1 provide the arbitrary closure-presentation correspondence; PasekaVetterlein2025 Lemmas3.5–3.7 give a modern point-adjoint comparison.',
 'The author initially confuses arbitrary generator assignments with compatible ones, then inserts the missing equality and explicitly acknowledges that addition on scan97. This is a documented internal correction, not a problem left unresolved at the end of these pages.',
 'The corrected theorem is settled; the useful next work is a source-critical exposition that retains the cancelled and corrected formulations.',
 ['Shmuely1974','DomenachLeclerc2001','PasekaVetterlein2025'])
add(11,'Complete the enveloping-support representation and its dense-subspace formulations',
 ['156-9 scan81 J156-9-10:249–273','scan82 J156-9-11:6–17 (formulation b′ and explicit-formula reminders)','scans82–84 same:19–125','scans85–88 same:131–216'],
 'Represent a spatios by a faithful disjoncteur of generators; give the inverse formulas and the alternative injectivity condition b′; identify which subdisjoncteurs are dense enough to give the same spatios.',
 'A faithful orthogonality map with join-dense image yields ΣE≅L. For D⊆E, ambient support join density is equivalent to restriction injectivity and to the closure map ΣD→ΣE being an isomorphism. The point-preorder density phrase requires an explicit convention; its purely intrinsic supremum interpretation is false in the empty-D one-point example.',
 'C-SA21-9-032/045–051; independent P5–P6. Birkhoff1948 IV §7 and PasekaVetterlein2025 Lemma2.3/Proposition2.4 provide checked completion and modern presentation results. The uncertain injection word and missing D quantifiers are in readings.tsv.',
 'The proof reminders are discharged in the next pages. Remaining uncertainty belongs to the transcription/convention of two formulations, not to the precise support-lattice representation theorem.',
 'An exact comparison of redundant-point presentations is a useful bounded exposition task after the scan readings are checked.',
 ['Birkhoff1948','PasekaVetterlein2025'])
add(12,'Discharge Proposition3’s deferred closure identities without circularity',
 ['156-9 scan90 J156-9-12:32–69','scan91 same:89–98','scan92 same:104–137','scan93 same:144–167'],
 'The support-level adjunction is stated with inserted identities b); their proof is deferred, and the first attempted argument is crossed out before a replacement based on the raw pretranspose identity.',
 'A raw point pretranspose gives the subset adjunction; orthogonality is unchanged by source closure, which yields both closure identities. Conversely support adjunction plus those identities recovers raw point adjunction. The support adjunction by itself is insufficient.',
 'C-SA21-9-052 and P4; countermodelP3. CoeckeMoore2000 §3 supplies the support-level orthogonal adjoint; PasekaVetterlein2025 Lemma3.5 checks the closure consequence in its point-map setting.',
 'The cancelled argument attempted to use the support formula before establishing compatibility; the live replacement completes the deferred step on scan93.',
 'The proof is complete; the cancelled circular route should remain documented but is not a research problem.',
 ['CoeckeMoore2000','PasekaVetterlein2025'])
add(13,'Does the generator extension and categorical composition really work?',
 ['156-9 scan71 J156-9-09:227–244','scan89 J156-9-11:249–275 (composition reminder)','scan97 J156-9-12:335–355','scans98–99 J156-9-13:26–88 (remaining verification)','scan100 same:93'],
 'The arbitrary-function lemma and the later corollary require checking that the extension preserves joins and recovers its generator values. The text also leaves a reminder to check composition before announcing the normalized category.',
 'Arbitrary assignments fail; compatible closed-valued assignments are exactly fσE for a join map f. Composition is closure after setwise composition, identity is σE, and the support functor is fully faithful and essentially surjective. The transpose reverses composition.',
 'C-SA21-9-035/054–056, P2/P4/P7. Exact later correspondences: DomenachLeclerc2001 Theorems4.1/5.1; canonical-category conjugation: CoeckeMoore2000 §3[3.4]. The pre-1986 Galois foundation is Shmuely1974.',
 'The author supplies the missing pointwise equality and completes the corollary on scan99. The final categorical assertion is justified by those corrected bijections; it does not validate the earlier unrestricted lemma.',
 'This is settled; checking exact source dependence and map normalization is valuable editorial work rather than a new theorem search.',
 ['DomenachLeclerc2001','CoeckeMoore2000','Shmuely1974'])
add(14,'Does OR-product closure coincide with closed-fiber correspondence closure?',
 ['156-9 scan100 J156-9-13:102 (open-questions heading)','scan101 same:105–112'],
 'Can correspondences be interpreted as supports of E×F with disjunction given by an OR in the two coordinates? Closed supports have closed rows and columns; the converse is doubted except when one factor is trivial.',
 'The converse is false in general and true when one factor is a trivial disjoncteur. Four-point paired-orthogonality factors yield a three-point diagonal with closed fibers and full product closure. The product formula itself needs its cross-factor indices checked on the scan.',
 'C-SA21-9-057/058; proofP8 and exhaustive16-point certificate. Exact tensor comparison: Ischi2010 Theorems3.4 and3.6, primary preprint pp.6–7. Published issue2010, online2011, arXiv2011 as separately recorded.',
 'The supplied pages record doubt but give no reason for subsequent abandonment; the later tensor results are mathematical matches, not evidence of direct historical transmission.',
 'The universal question is answered; identifying restricted geometric factor classes where the two closures agree could be useful, but is a separate research task.',
 ['Ischi2010','Shmuely1974'])
add(15,'Can all correspondences between two spatios form a spatios?',
 ['156-9 scan101 J156-9-13:114','scan102 same:117–137','scan103 same:142–153'],
 'Hom∨(L,M) is complete under pointwise order; does it admit a complement C or disjunction relation making it a spatios? The trivial-source case is a product M^E.',
 'No in general: for the six-element four-atom ortholattice L, Hom∨(L,L) has234 maps,40 atoms and16 coatoms, so it admits no order reversing bijection. The trivial-source product case remains true; complement is pointwise on generator values only.',
 'C-SA21-9-059–062, independent P9/P11 and executed certificate. Ischi2010 Theorems3.6/4.9 give a matching negative result through minimal versus maximal weak tensor products. Shmuely1974 §6 gives completeness of the Galois-map lattice.',
 'The manuscript recognizes that the complement is unclear. The structural obstruction is that complete map lattices need not be self-dual; no source was found documenting the author’s historical reason for leaving this question.',
 'No further work is needed on the universal assertion; a sharply specified restricted correspondence class might support a different positive question.',
 ['Ischi2010','Shmuely1974'])
add(16,'Which point substitutes could support a correspondence geometry?',
 ['156-9 scan103 J156-9-13:153'],
 'The possibility of a complement on correspondences seems tied to identifying minimal nonzero elements or other objects playing the role of points.',
 'The universal hoped-for consequence cannot hold even for finite atomistic ortholattices, by MP-SA21-9-15. A viable statement must first specify the admissible objects, map class and desired point representation; the manuscript does not choose these here.',
 'C-SA21-9-063. Ischi2010 gives a direct obstruction; CoeckeMoore2000 and PasekaVetterlein2025 develop particular adjoint categories, with extra hypotheses in their point-space representations. The bounded search found no exact continuation of this unformulated programme.',
 'No source provides a historical explanation. The text expresses a heuristic link rather than a precise conjecture, so it cannot be declared solved by topical similarity.',
 'Low priority until the intended geometric examples and allowable morphisms are fixed, because atomisticity alone already fails.',
 ['Ischi2010','CoeckeMoore2000','PasekaVetterlein2025'])
add(17,'Can every correspondence factor through a span of morphisms?',
 ['156-9 scan103 J156-9-13:155','scan104 same:160–184','continuation scan105 J156-9-14:6 (these questions are set aside); scan107 same:83 (no general decomposition available)'],
 'The graph of an ordinary relation yields an inverse-image map followed by a direct-image map. Does every general correspondence similarly factor as a comorphism followed by a morphism, where a comorphism commutes with C and a morphism has transpose commuting with C?',
 'No for these definitions: the map f on the six-element four-atom L with f(0)=f(a)=0 and f(b)=f(c)=f(d)=f(1)=a cannot equal h†g for any complete ortholattice K and C-preserving join maps g:L→K,h:L→K. For nontrivial K, h reflects zero and forces f(1)=1; trivial K forces f=0. A factorization under weaker maps is a different question.',
 'C-SA21-9-064–066, P10–P11; executed join-preservation check plus symbolic proof for all intermediateK. The recorded searches found no exact external result for this span. CoeckeMoore2000 §3 verifies the transpose formalism used in the proof, not the factorization.',
 'Scan105 says these questions do not immediately bear on the set formalism of ateliers; scan107 explicitly proceeds without such a decomposition. This explains the local change of focus, not any undocumented later decision.',
 'The literal universal problem is settled negatively; a worthwhile new task would first identify map classes appropriate to the geometric examples rather than ask the same false universal question.',
 ['CoeckeMoore2000','Shmuely1974'])
(ROOT/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
out={'problems':len(P),'ids':[p['id'] for p in P]}
(ROOT/'outputs/author_problems_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
