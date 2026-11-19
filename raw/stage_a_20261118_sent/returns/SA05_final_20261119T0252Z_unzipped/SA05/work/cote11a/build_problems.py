"""Manually consolidated source problems; every formulation is bounded by a read passage."""
import json,pathlib
R=pathlib.Path('SA05/work/cote11a'); P='sources/texts/pro/MPL_11_002-042_transcription.tex'; B='sources/texts/codex/B12-01_transcription.tex'
out=[]
def p(n,title,loc,as_he,plausible,state,worth,refs,claims,why='The supplied pages give no historical explanation for leaving this step unfinished; a mathematical obstruction is not evidence of the author’s reason.',author='Grothendieck manuscript'):
 out.append(dict(id=f'MP-SA05-{n}',title=title,occurrences=loc,as_he_states=as_he,plausible_today=plausible,state_of_art='As of2026-11-19: '+state,why_open=why,worth=worth,refs=refs,claim_ids=[f'SA05-C{i}' for i in claims],attribution=author))
p(1001,'Coherent graded signs for kernel composition',[f'{P}; cote11 scans5,7; lines88-139,176-229'],
'The associativity/unit calculations flag signs and use projection and exchange formulas.',
'Give one symmetric monoidal convention for graded pullbacks, homogeneous pushforwards, traces and symmetry; prove convolution, graph actions and tensor compatibility in that convention.',
'Stacks0FFZ proves the even Chow formalism; Kock2003 §3.3.9 gives Koszul symmetry. Neither certifies the unread ink or all formulas of this draft. The64-case parity check is convention-specific.',
'Yes: a focused sign audit would settle a small, central obstruction to a dependable edition.',['Stacks0FFZ','Kock2003'],[1001,1005,1022])
p(1002,'Which squares satisfy exchange?',[f'{P}; cote11 scans3,9,31; lines4-11,261-278,1053'],
'Which exchange squares suffice for the kernel calculus, and does cartesianness plus the dimension relation suffice inPoincaré algebras?',
'Assume exchange for the exact product and diagonal/graph squares used; for abstract gauged objects characterize additional trace compatibility rather than deducing it from cartesianness.',
'The currentQ_2/Q_1 isomorphism square is Cartesian with all dimensions0 but exchange1≠2. Hua2026 Cor1.3 proves the restricted commutative tensor-square adjoint identity.',
'Yes: the counterexample makes an axiom-minimization task concrete and prevents a false general theorem.',['Hua2026','Stacks0FGS'],[1001,1002,1023,1024],why='The source asks the general question explicitly. The counterexample identifies an obstruction today; it is not a documented historical reason for abandonment.')
p(1003,'Transpose as an anti-functor',[f'{P}; cote11 scan15; lines529-542'],
'Verify that factor transposition is multiplicative in the reversed order.',
'Prove(v∘u)^t=u^t∘v^t in the even convention and record the graded correction under the chosen symmetry.',
'Stacks0FFZ Remark45.3.5 and the current named-projection proof settle the even case. The local variance discrepancy remains a scan alarm.',
'Yes as an editorial verification; the even theorem is already established.',['Stacks0FFZ'],[1006])
p(1004,'Compatibility of graph, transpose and realization functors',[f'{P}; cote11 scan17; lines570-581'],
'The displayed comparison diagram is marked for verification.',
'Substitute the established graph action and transpose into each route, first in the even case; compare all-degree symmetry conventions separately.',
'The even diagram follows from Stacks0FFZ graph identities and proof_checks.md §1; a broad motives citation alone does not verify the original diagram.',
'Yes: a short diagram audit will remove a concrete self-flagged step.',['Stacks0FFZ'],[1007])
p(1005,'Centrality in trace adjointness',[f'{P}; cote11 scan17; lines595-625','sources/texts/codex/K11-02_transcription.tex; cote11 scan17; lines51-58'],
'Pro reads an assertion thatu is central, while Codex reads a question about the central case.',
'State adjointness for central/even kernels, then calculate the explicit homogeneous sign whenu is not central.',
'The trace calculation is checked. Stacks0FGS Lemma45.7.1 covers geometric even shifts. The punctuation/wording conflict is unresolved without scans.',
'Yes: deciding the ink changes the exact hypothesis, not merely style.',['Stacks0FGS','Stacks0FFZ'],[1009])
p(1006,'Gauged monoids without addition',[f'{P}; cote11 scan19; lines656-660'],
'Formulate the correspondence theory using bivariant monoids, then use graded bijectionsσ^i to handle signs.',
'Start with ungraded monoids and explicit projection/exchange/unit axioms; separately formulate coherent degreewise sign actions compatible with products and pushforwards.',
'The recorded exact-phrase searches and Frobenius/categorical literature did not locate a complete match. Kock treats additive vector-space models, and Hua2026 excludes this programme.',
'Moderately: one run could produce a precise axiom inventory, but a full new theory is beyond this consolidation.',['Kock2003','Hua2026'],[1010,1011],why='The manuscript itself says the viewpoint is not convenient when the two projection formulas cannot both hold without signs.')
p(1007,'Pushforwards for a chosen class of maps',[f'{P}; cote11 scan21; lines690-693'],
'A selected-map variant is announced with conditions left blank.',
'Specify closure under composition, products and the needed base changes; require allowed graphs/diagonals exactly where used.',
'The exact intended class is not identifiable. Chow correspondences are a proper-map model; no generality is supplied from that example.',
'Yes after scan/context recovery, because the finite list of used squares is already available.',['Stacks0FFZ'],[1012])
p(1008,'Repairing the rejected tensor-pushforward formula',[f'{P}; cote11 scans29,31; lines919-956,992-1001'],
'The naive all-degree tensor formula is rejected with “Mais c’est faux”; subsequent sign manipulations remain uncertain.',
'Retain the even-shift theorem, and express any odd-degree theorem with a completely specified tensor-duality convention.',
'Hua2026 Cor1.3 proves only the commutative ungraded tensor-adjoint formula. The current64-case parity certificate is valid for its stated convention, not as a reading of the page.',
'Yes: a compact algebraic audit can determine which manuscript expressions could be correct.',['Hua2026','Kock2003'],[1022,1023],why='The author explicitly discovers failure and later restricts to even degree shifts; this is a documented local correction.')
p(1009,'Choosing left or right projection formula',[f'{P}; cote11 scan34; lines1081-1091'],
'The margin says one must choose between the two formulas and suggests(−1)^(δj).',
'Use one signed module convention consistently; the other formula then has sign(−1)^(δj), so both unsigned forms agree whenδ is even.',
'All8 parity cases and the symbolic identity are checked; Stacks0FGS gives the standard geometric even-degree form.',
'Yes as a resolved editorial step; the remaining decision is the edition’s convention.',['Stacks0FGS','Kock2003'],[1020,1025],why='The source itself identifies the parity incompatibility and inserts the even-degree restriction.')
p(1010,'Unspecified universal constructions beyond Poincaré algebras',[f'{P}; cote11 scan36; line1163'],
'The text says universal constructions require leaving thePoincaré category, without naming a diagram.',
'Recover the intended construction before asking for an existence theorem; keep separate the tensor product, which is a product forPoincaré targets in the commutative gauged category.',
'No exact theorem is identifiable. The tensor universal property is checked in proof_checks.md §2, but it does not identify the unnamed construction.',
'Low until additional context is supplied: first locate the missing diagram or following development.',['Kock2003','Hua2026'],[1029,1030])
p(1011,'Evaluation of a special finite-set system',[f'{P}; cote11 scans38,42; lines1188-1198,1294-1301'],
'An equivalence withPoincaré algebras is asserted after introducing specialness, and later full faithfulness is flagged.',
'For commutative ungraded systems, impose special Künneth isomorphisms, aPoincaré singleton and multiplicative gauges; then singleton evaluation is an equivalence.',
'Hua2026 Theorem1.2 pp18–20 gives exactly this restricted theorem and prose proof; its Lean compilation is not checked here. The unrestricted reading is refuted by the verified partition system.',
'Yes: compare the precise restrictions and variance with the source, rather than re-proving the unrestricted false version.',['Hua2026','Kock2003'],[1031,1032,1035])
p(1012,'Equivalent closure conditions on cohomology of powers',[f'{P}; cote11 scan40; lines1242-1258'],
'The proposition claims equivalence of closure by actions/graphs and by simplicial push/pull maps; two displayed targets only say ambientH*.',
'Replace those targets by the appropriateA_m/A_(n+m) only as a proposed scan reading, then prove the equivalence from the kernel axioms and specified elementary maps.',
'The formal even implications follow the graph-action calculation; Hua2026 explicitly excludes a proof of this proposition. The literal transcription is too weak and its zero-power convention is unfinished.',
'Yes: the task is finite once the two targets and empty-power convention are decided on scans.',['Hua2026','Stacks0FFZ'],[1033])
p(1013,'Axiom system for the diagonal class',[f'{P}; cote11 scan42; lines1298-1301'],
'Specify the axioms onΔ; verify that knowingδ_*1 suffices to recoverδ_* and the system.',
'In the finite projective commutativeFrobenius case, impose the trace-dual diagonal, or equivalently the compatible counital cocommutativeFrobenius comultiplication. The larger degenerate graded case needs its own axiom list.',
'Kock2003 Proposition2.4.10 settles theFrobenius comultiplication; Hua2026 settles special commutative power systems. The arbitrary gauged/graded claim remains a precise residual.',
'High: one run can separate the establishedFrobenius theorem from the genuinely wider requested structure.',['Kock2003','Hua2026'],[1034,1035])
p(1014,'Empty finite set and the gauge',[f'{P}; cote11 scans38,40,42; lines1188,1258,1298'],
'The indexing category starts with nonempty finite sets, later usesn,m≥0 and an uncertain∅/ω glyph for the gauge.',
'Choose explicitly whether to adjoin the empty set withA(∅)=k and its unit/trace operations; do not interpret the unresolved glyph as ink evidence.',
'Kock2003 §3.3 finite-set constructions include the empty set and tensor unit. The source convention is not settled by that modern example.',
'Yes: a scan check plus a short convention note resolves a recurring boundary issue.',['Kock2003'],[1031,1033,1035])
p(1015,'Rational ray attaining the numerical infimum',[f'{P}; cote11 scans16,14,12; lines560-566,476-501,391-394'],
'The proof leaves as elementary calculus the attainment of the finite rational-weight maximum on a rational ray.',
'Assume nonemptyS and nonempty direction space and a rational positive-definite norm; reduce to finitely many rational polyhedral faces and prove attainment on a rational ray.',
'GIT1982 Proposition2.17 preserves the exercise; Kempf1978 proves stronger optimality in its unstable-vector setup. The emptyS formulation is false, and finite tests do not prove rational attainment.',
'Yes: a few-hour proof/edition task can fill the exercise with exact hypotheses.',['GIT1982','Kempf1978'],[1043],author='Mumford reused GIT typescript')
p(1016,'A center or optimal parabolic for instability',[f'{P}; cote11 scan16; lines553-558'],
'A Tits conjecture is invoked to select the parabolic most responsible for instability via a center ofC.',
'For an unstable vector and a fixed invariant norm, use the optimal cocharacter class and its unique parabolic; for an arbitrary convex building subset specify the exact finite-type/polyhedral or subcomplex hypotheses and the stabilizer whose fixed point is required.',
'Kempf1978 Theorems6–7 give optimal parabolic and rational descent. Ramos-Cuevas2009/2013 concerns convex subcomplexes. Bate–Martin–Röhrle2010 Theorem4.5 characterizesG-centres of convex polyhedral finite-type subsets via bounded integral quasi-states;Remark5.10 explicitly says GIT sets need not be subcomplexes. These scopes do not justify an undefined universal center statement.',
'Yes as a historical comparison with exact quantifiers; developing a new general center theorem is not indicated.',['GIT1982','Kempf1978','RamosCuevas2013','BateMartinRoehrle2010'],[1042],why='The reused page names a conjecture but gives no later history; the literature supplies several distinct precise successors.',author='Mumford reused GIT typescript, invoking Tits')
p(1017,'Missing character value and negative parallel rays',[f'{P}; cote11 scan26; lines803-810'],
'The character-extension/separation argument has a blank value and a reference mismatch.',
'Distinguish nonparallel directions from negative parallel rays; fill a proposed character value only after checking the ink or the exact published proof.',
'GIT1982 Corollary2.11 supplies the final isogeny statement. The elementary observationχ(−λ)=−χ(λ) exposes the omitted case in the local separating-character argument.',
'Yes: a tightly bounded collation can repair a proof gap without changing the final theorem.',['GIT1982'],[1049,1050],author='Mumford reused GIT typescript')
p(1018,'The missing last criterion in the determinant-cone proof',[f'{P}; cote11 scan41; lines1265-1279','sources/texts/pro/MPL_11_043-058+56_transcription.tex; cote11 scans58,56; lines650-689,514-550'],
'The proposition announces determinant monomials; the continuation reduces to a final equivalent condition whose typed page3.16 is absent.',
'Write the cone-interior statement with a nonzero separating functional and complete the greedy-flag reduction, or compare the published independent-set proof.',
'GIT1982 Appendix toChapter3 proves the criterion using Edmonds partitions; main-textOCR is incomplete. Both attached continuation endpoints were read, so only the final missing criterion—not the whole proof—is a gap.',
'Yes: a source collation and convex-combinatorial proof check are feasible within one run.',['GIT1982'],[1058,1059],author='Mumford reused GIT typescript')
p(1019,'Generic freeness in the separating-family lemma',[f'{B}; cote12 scans22,66; lines6-17','sources/texts/pro/MPL_12_051-098_transcription.tex; cote12 scan72; lines444-449','sources/texts/codex/K12-05_transcription.tex; cote12 scan72; lines143-164'],
'Replace projectivity ofA′ by generic freeness on every integral quotient; prove the resulting separating-family statement.',
'First recover the missing proposition hypotheses and correct the candidate module toB′_h overB_h as an ink question; then compare EGAIV3 11.9.7–10 and the support-induction proof.',
'Published EGA supplies exact finite-family, finite-presentation and projective variants. Its11.9.8 itself records a separate locally-projective localization question, so “all solved by generic freeness” is too strong.',
'Yes: collation can distinguish the proved final theorem from the cancelled stronger draft.',['EGAIV3'],[1060,1061],why='The entire draft is cancelled; no reason is supplied. The text itself proposes support induction to avoid the associated-point equality.',author='Cancelled EGA reused draft')
p(1020,'Integrality of the total local ring',[f'{B}; cote12 scan68; lines26-30'],
'Flat localA→B, geometrically integral closed fiber, excellent geometrically unibranchA: isB integral? The draft reports characteristic0 and essentially finite-type cases, but ignorance even for completeA,B with trivial residue extension.',
'Use at least a reduced/integral base, or the proposed normal-base reduction, and distinguish total-domainhood from geometric punctual integrality of all fibers.',
'The literal unreduced wording hasA=B=Q[ε]/ε² as counterexample under Stacks0BPZ. Murayama2022 Cor4.1 solves the fiberwise punctual-integrality statement for quasi-excellentA;Remark4.2 warns domainhood does not satisfy general ascent. The exact intended total-domain implication was not identified as settled by the opened references.',
'High for source/literature clarification: a run can locate the exact final EGA7.9 variant and test whether a published total-space theorem supplies the missing bridge.',['Murayama2022','EGAIV2','Stacks0BPZ'],[1062,1063,1064,1067,1090],why='The source explicitly cites resolution in characteristic0 and says the general case was unknown; it provides no reason for the later cancellation.',author='Cancelled EGA reused draft')
p(1021,'The correct general localization-property theorem',[f'{B}; cote12 scans70,83; lines59-78,107-123'],
'Reformulate7.5.1 so the theorem states everything the proof proves, including codepth andintegrality examples.',
'Write a theorem with explicit permanence conditions onR, formal-fiber/quasi-excellence assumptions and pointwise interpretation; keepR/Q consistent and separate total-space ascent.',
'Murayama2022 Theorem3.4/Cor3.6 andTables1–2 provide a modern exact framework. Final EGA7.5 text access was partial, so draft-specific weaker hypotheses are not all certified.',
'Yes as an editorial-historical project; the central modern theorem is established.',['Murayama2022','EGAIV2'],[1065,1066,1067],why='The draft says the preceding version was too restrictive for its proof; this is an explicit reason for rewriting, not an unresolved theorem by itself.',author='Cancelled EGA reused draft')
p(1022,'Schematic dominance under arbitrary base change over a field',[f'{B}; cote12 scan85; lines130-134'],
'Does a schematically dominant family overk remain so after everyk-base change, even withoutNoetherianX?',
'The affirmative statement holds for arbitrary schemes over a field and arbitrary base change.',
'EGAIV3 Proposition11.10.6 and module counterpart11.9.13 answer exactly this question; both were opened. Definition11.10.8 fixes the later universal-relative terminology.',
'No new theorem needed: record the exact published answer and its hypotheses in the edition.',['EGAIV3'],[1074,1075,1076],why='The draft says “nous ignorons”; the final published result answers it. The source does not date the resolution of the question.',author='Cancelled EGA reused draft')
p(1023,'Nilpotent lifting of schematic density',[f'{B}; cote12 scan85; lines136-138'],
'FlatX,Z_i overS and schematic dominance after a nilpotent closed-base reduction should imply dominance before reduction.',
'Retain the published sufficient condition that everyJ^n/J^(n+1) is locally free onS_0, or formulate a distinct universality condition strong enough to justify tensoring the jointly injective family.',
'The ordinary draft assertion is false for S=Spec Q[x,ε]/(ε²,xε), X=S, Z=D(x). SGA3II ExposéIX Lemma4.2 and EGAIV3 11.9.15 include local freeness explicitly; their induction uses it. The relative-universal version is a different, stronger premise and is not refuted by this example.',
'Yes as a source correction: check whether the omitted hypothesis was on the preceding page and separate the ordinary from the universal assertion.',['SGA3II','EGAIV3'],[1077,1089],why='The draft delegates the proof toSGADIX4.2; the opened target has a hypothesis absent from the draft.',author='Cancelled EGA reused draft')
p(1024,'Cycle-class construction versus its compatibility assertions',[f'{B}; cote12 scan100; lines160-180'],
'Define classes by trace duality, then assert invariance under rational equivalence and products.',
'Use the twistedℓ-adic class for smooth properX, define singular-cycle classes via purity/fundamental classes, and prove the ring-map properties separately.',
'Milne2013 §23 gives the direct construction and Theorem23.4 states compatibility with the Chern-class map; the long proof is not included there. The English sheet’s author and missing preceding hypotheses remain unidentified.',
'Yes for attribution and precise hypotheses; the underlying cycle-class theorem is established.',['Milne2013','Stacks0FHA','Kleiman1968'],[1078,1079,1080],why='The page assumes preceding cohomological formalism and gives no historical explanation for deferred proofs.',author='Unidentified reused English typescript')
(R/'problems.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Authored problems={len(out)}')
