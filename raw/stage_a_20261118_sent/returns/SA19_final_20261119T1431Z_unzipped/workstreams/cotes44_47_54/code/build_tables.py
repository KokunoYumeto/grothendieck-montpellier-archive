"""Serialize hand-authored reading alarms, checked links and actual coverage."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
def tsv(name,header,rows):
    with (ROOT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
read=[]
def alarm(c,s,l,r,a,e,w='major',confidence='high mathematical alarm; ink undecided'):
    read.append([str(c),str(s),l,r,a,e,w,confidence])
alarm(47,3,'2087–2096','D_parf|prof','D_parf (perfect complexes)','The named functor and perfect-pushforward proof use perfect complexes; the transcription itself leaves the subscript uncertain.')
alarm(47,3,'2100–2108','ordinary product in the input or unclear star','Pontryagin product on A, tensor product on the target','The proof on scan4 and Poincaré multiplicativity distinguish the two operations.')
alarm(47,4,'2184','second pr_13','pr_23','The two input sheaves live on distinct A factors; the displayed tensor calculation otherwise repeats the first factor.')
alarm(47,4,'2217–2224','K-theory square=(-1)^g inversion without τ','multiply by [π_A^*τ_A] over a general base','The corrected derived square on scan5 includes τ_A[-g]; taking K_0 retains its line-bundle class.')
alarm(47,5,'2258–2260','proof target remains identity','inversion pullback with determinant twist/shift','The anti-diagonal kernel later computed acts by inversion; cancellation or carryover from the earlier statement must be read on the image.')
alarm(47,5,'2264','kernel in D_parf(A)','kernel in D_parf(A×_S A)','A kernel for an endofunctor on A must live on the product.')
alarm(47,5,'2266','L pr_13*|R pr_13*','R pr_13*','This is the derived pushforward in kernel composition; L belongs to pullback.')
alarm(47,5,'2273–2276','φ:A→B while ψ targets B∨','φ:A→B∨ if the following ψ is the classifying homomorphism','Source and target typing in the next diagram; a different definition of φ would need explicit evidence.')
alarm(47,6,'2280–2294','projection labels pr1/pr2 inconsistent','projection to B∨ and projection to B must be distinguished','The base-change square and the Poincaré pushforward use different factors.')
alarm(47,6,'2312–2324','Lψ*(τ[-g])','Lψ*(e_*τ[-g])','τ lives on the base, while the object pulled back is supported at the zero section of B∨. Without e_* the kernel and its higher Tor disappear.')
alarm(47,6,'2326–2330','φ:A≃C∨','φ:A≃B∨ in this specialization','The preceding argument specializes C=A×A and uses dual abelian varieties A,B; C∨ gives the wrong dimension.')
alarm(47,7,'2334–2353','H^i(X,L)=0','H^i(B,L)=0','The admitted lemma is stated for L on B; X has not been introduced for this cohomology group.','minor')
alarm(47,8,'2399–2403','last convolution factor δ_t','δ_-t under T_t(x)=x+t','Convolution by δ_u is T_-u^*; Φ(P_t)=τδ_-t[-g]. A hidden translation convention remains an alternative.')
alarm(47,9,'2449–2458','expanded c2,c3/general denominator has one fewer χ','coefficient of (1-D′/χ)^χ with denominator k!χ^(k-1) after canceling the leading χ','Exact symbolic expansion and degree(1,2) elliptic-product counterexample; generating series itself is correct.')
alarm(47,9,'2461–2468','mod torsion attached to unspecified Gr','identify the filtration/coefficient ring before evaluating the question','K_0 filtration, Chow modulo torsion and cohomological integrality are different assertions; source does not fix the intended target.')
alarm(47,10,'2486','D in Gr1(A×A)','D in Gr1(A×B)','D is the first Chern class of the Poincaré bundle on A×B.','minor')
alarm(47,10,'2505','ch(a|x)','ch(x)','The input of φ is x; the extra a is not typed by the surrounding formula.','minor')
alarm(47,11,'2535;2539','juxtaposition of the two output transforms','Pontryagin star between the output transforms','The reverse product theorem changes tensor product to convolution; a juxtaposition is a different operation.')
alarm(47,11,'2535–2542','single Todd factor T_A chω_A','T_A T_B chω_A','GRR for source projection and target convolution each contributes a Todd factor; product equals Td(H1_dR).')
alarm(47,11,'2553–2557','check F undefined','(−1_A)^*F∨ for the same-kernel formula, or use P∨','Ordinary duality changes P to P∨. It is not permissible to add inversion to the notation silently.')
alarm(47,11,'2553','shift [+n|-n]','[+g] for the relative dualizing complex','Smooth proper duality has f!O=ω[g], while inversion has[-g]; these are separate uses of the shift.')
alarm(47,11,'2563–2570','u.F and transpose action unspecified','state whether the action is pullback or pushforward','Poincaré functoriality interchanges the two; no unique formula is selected by the shorthand alone.')
alarm(54,3,'2628–2645','t_E=H1(B) could look reversed','retain B if E is the universal extension of A','The tangent of E(A) is H1_dR(A∨); invariant differentials give H1_dR(A). Mathematical check supports the supplied variance.','major','high variance check; no proposed ink change')
alarm(54,4,'2664–2666','nilpotent deleted, conclusion changed to every I-adic quotient','restore nilpotence or identify an additional topological hypothesis','A=k[t],I=(t),A1=k[t,t^-1],M=k satisfies all remaining tests but fails flatness over k[t]/t². EGA IV₃11.4.7 adds topology control.')
alarm(54,4,'2677','M_0 free in an iff criterion for M flat','possibly flat, or an additional freeness assumption retained','Flat M need not have a free reduction over arbitrary A/I; source is uncertain and preceding cancellation obscures the intended hypotheses.')
alarm(54,4,'2670–2677','noetherian plus ideally separated appears sufficient','inspect omitted hypotheses and definition of ideal separation','The same finite separated counterexample defeats the literal broad criterion; EGA11.4.7 requires equivalent topologies.')
alarm(54,5,'2687','H^q(B,Ω_A^p)','H^q(B,Ω_B^p)','The sheaf on B must be Ω_B; exterior duality gives precisely that expression.')
alarm(54,5,'2696','p^A|_p A','finite group scheme A[p], rather than geometric p-torsion points','Cartier duality and rank p^(2g) identify the group scheme object.')
alarm(54,7,'2716–2725','terminal arrow labelled V|A and absent twists','V with Frobenius-twisted source/target as required','Cartier dual of Frobenius is Verschiebung; Oda’s σ-semilinear formulas rule out an unqualified ordinary transpose.')
alarm(54,7,'2727–2730','restricted p-operation on the additive kernel','zero on the additive vector subgroup, with the operation on the middle extension specified','The universal vector extension is an algebraic group; its restricted Lie operation is more than an arbitrary extension of vector spaces.')
alarm(54,6,'2707','Y≠∅ in place of the published irreducible Y','check whether irreducible was implicit or omitted','EGA IV₃11.4.5 assumes irreducibility. The broader nonempty version is reconstructible by noetherian approximation and a component open, but that reduction is not explicit in the line.')
alarm(54,6,'2710','for every i, Mi⊗A′ free iff J vanishes','all chart modules simultaneously free iff J=ΣJi vanishes','Vanishing of one Ji does not imply vanishing of their sum; quantifier scope must remain simultaneous.')
alarm(54,8,'2748–2750','H_o|H_0 and C_o|C_0','consistent zero subscript','This labels a distinguished wall and the chamber after removing it; the distinction is typographic, not a new theorem.','minor')
alarm(44,2,'2799–2800','complementary index n−i|n+1−i','n+1−i for codimension-indexed incidence duality','The separate dated letter on scan8 writes n+1−i; incidence degree counting agrees. It cannot settle the programme ink.')
alarm(44,2,'2802–2803','Connu telquel near the positivity theorem','determine its exact scope and insertion order','The same letter explicitly marks positivity unproved; the marginal phrase cannot certify the whole statement without its attachment.')
alarm(44,3,'2809–2840','TF undefined, completion proof canceled, final faithfulness insertion','identify graded TF category and cancellation sequence','Graded finite-module faithfulness is valid; ungraded faithful flatness needs extra hypotheses. Neither reading is imposed from modern theory.')
alarm(44,4,'2850–2864','(-1)^m with m undefined for general i+j=n','m=i=j=n/2 only in the balanced case, or another stated convention','The middle fibre dimension is2m−1 only when n=2m; unbalanced cases do not determine m.')
alarm(44,4,'2866–2871','both sides vanish by Lefschetz','intersection side follows directly; height side needs realization/fixed-part input','Weak Lefschetz alone proves a cohomological intersection calculation, not the full height statement.')
alarm(44,4,'2880–2885','middle finite-kernel clause crossed out','do not retain finite kernel in the theorem','The diplomatic deletion must survive in the claims map even if a later model has an isogeny statement.')
alarm(44,5,'2910–2915','γ_α∈P′; roots primitive deduced from earlier axioms','inspect a missing crystallographic or primitive-root assumption','The eight-root rescaled B2 example satisfies every displayed input but has coroot(1/2,1/2). The whole fragment is canceled.')
alarm(44,5,'2918–2920','en dualité deleted; accouplés à Z inserted; rationalizations dual','retain integral pairing with only rational perfection','The usual root datum’s perfect integral dual lattices are a stronger condition than the actual text.')
alarm(44,6,'2942–2944','τ-equivalence undefined; Matsusaka margin','identify τ and whether divisors were intended','The usual algebraic-modulo-torsion interpretation is true for divisors and false for arbitrary cycles by Clemens; neither the symbol nor a missing qualifier is decided.')
alarm(44,7,'2956–2962','copoids radiciels need not be copoids','retrieve the definitions in the reused Bourbaki draft','The local terminology is proposed and mutable; standard modern root/coroot names cannot identify the claimed failed inclusion.','major','low semantic identification; ink undecided')
alarm(44,8,'2974','i=0|1,…,n','i=1,…,n if indexed by codimension','The endpoints are J1=Pic0 and Jn=Alb; index0 would need a separately defined object.')
alarm(44,8,'2976–2978','tangent sign ∈|⊂|subquotient unclear','inclusion or subquotient, not equality with all H^iΩ^(i−1)','The algebraic Abel–Jacobi tangent is level1, while the full intermediate torus tangent may have other Hodge components.')
alarm(44,8,'2979','symmetric versus antisymmetric wording with deletions','distinguish symmetric homomorphism from alternating Tate pairing','A polarization is symmetric as A→A∨ and induces a skew/alternating pairing after the relevant duality convention.')
alarm(44,8,'2979','modulo factor2','retain the factor2 qualification','Graph pullback of Poincaré gives λ_L=f+f∨=2f. This does not prove ampleness.')
alarm(44,9,'2993–2995','N=noyau of A→A∨; quotient J=A/N; descent asserted','full scheme-theoretic kernel versus reduced neutral abelian radical; integral versus rational correspondences','For z=2P on an elliptic curve, λ_D=−4, q=[4], and integral descent would need μ=−1/4. This exposes a mathematical ambiguity but does not authorize an emendation.')
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],read)

coverage=[
 (47,1,'2051–2075','Cover, catalogue/folio matter','No mathematical claim'),
 (47,2,'2076–2085','Fourier title leaf','No mathematical claim'),
 (47,3,'2086–2156','Opening transform, binary margin, classifying reduction','401,402'),
 (47,4,'2157–2226','Product proof and first inversion/K0 statement','401,403,405'),
 (47,5,'2227–2278','Corrected twist/shift, bounded-qcoh margin, composition kernel','403,404,405,421,425'),
 (47,6,'2279–2332','Base-change kernel, zero-section lemma, flat specialization','403,406,409'),
 (47,7,'2333–2379','Admitted vanishing, comparison map, determinant line','404,406,407,408'),
 (47,8,'2380–2419','Unfinished fibre compatibility; sections, translation, invariants','408,410,411,412,413'),
 (47,9,'2420–2471','Adjugate, exponential heuristic, Chern arithmetic, integral question','413,414,415,416,417'),
 (47,10,'2472–2527','Relative GRR; retained T² cancellation and canceled attempt','418,419,420'),
 (47,11,'2528–2572','Reverse product, Todd/parity, Kleiman criticism, duality, equivariance','421,422,423,424'),
 (54,1,'2574–2600','Cover and label','No mathematical claim'),
 (54,2,'2601–2608','Duality title','No mathematical claim'),
 (54,3,'2609–2655','Hodge/Lie identifications, universal extension, de Rham pairing','426,427,428'),
 (54,4,'2656–2681','Reused canceled generic-freeness and amended flatness typescript','432,433,458'),
 (54,5,'2682–2704','Exterior Hodge duality and finite Frobenius kernels','426,428,429'),
 (54,6,'2705–2713','Retained reused Proposition A and universal ideal proof','434,458'),
 (54,7,'2714–2733','F/V diagram, restricted Lie extension, A[p] question','429,430,431'),
 (54,8,'2734–2751','Reused printed hyperplane-arrangement fragment, page13 no391','435'),
 (44,1,'2753–2779','Cover and catalogue matter','No mathematical claim'),
 (44,2,'2780–2806','Programme Theorems1–4 and marginal annotations','440,441,442,443,448'),
 (44,3,'2807–2843','Reused canceled graded-completion argument and marginal faithfulness','455'),
 (44,4,'2844–2888','Theorems5–6: heights, vanishing and Lefschetz restriction','451,452,453'),
 (44,5,'2889–2938','Reused canceled root-system and paired-lattice axioms','456,457,464,465'),
 (44,6,'2939–2947','Theorem7, numerical=τ, Matsusaka annotation','454,460'),
 (44,7,'2948–2965','Reused LaTribu57 comments; graph and mutable root terminology','466'),
 (44,8,'2966–2984','Bures12August1964 letter: cycle targets, realizations, positivity','440–448,461,462'),
 (44,9,'2985–3001','Letter: incidence divisor, kernel quotient, positivity, Pic0(Y) test','449,450,459,461,463')]
tsv('reading_coverage.tsv',['cote','scan','original_tex_lines','material_read','claims_checked','coverage'],[list(r)+['entire page read; supplied transcription only; no scan available'] for r in coverage])

links=[]
def link(kind,fr,to,what,evidence,ids=''):
    links.append([kind,fr,to,what,evidence,ids])
link('folder','cote47 scans5,7,11;tex2228–2235,2358–2376,2535–2542','cote54 scan3;tex2611–2652',
 'The Fourier determinant/Todd factors meet the Hodge exact sequence and dual determinant lines.',
 'Both endpoints read. This is a mathematical connection reconstructed in this run, not an explicit authorial cross-reference. CL404,421 versus426–428.','MPL_16+47+54+44#47;#60;#65;#66')
link('folder','cote44 scans2,8–9;tex2799–2803,2974–2995','cote54 scans3,5;tex2628–2652,2685–2701',
 'Proposed cycle-variety duality uses the Picard/Albanese and abelian duality formalism studied separately in cote54.',
 'Both endpoints read. No claim that de Rham duality proves the unknown cycle quotient’s integral self-duality or positivity.','MPL_16+47+54+44#65;#66;#72;#77')
link('folder','cote54 scan4;tex2658–2660','cote54 scan6;tex2707–2710',
 'The canceled generic-freeness corollary explicitly invokes Proposition A.',
 'Direct authorial internal reference: Prop.A inserted in the corollary proof. Both pages read; EGA11.4.5→11.4.6 confirms the logical order.','MPL_16+47+54+44#70')
link('folder','cote44 scan2;tex2799–2803','cote44 scans8–9;tex2974–2995',
 'Programme complementary index and middle positivity are elaborated in the dated Serre letter.',
 'Both endpoints read; n+1−i explicit only in the letter. It suggests but does not decide the ambiguous programme index.','MPL_16+47+54+44#72;#77')
link('published work','cote54 scan4;tex2658–2660','EGAIV3 Cor11.4.6,p147',
 'Exact nonreduced irreducible-base generic-freeness corollary.',
 'Both source and primary published statement/proof read; all finite-presentation hypotheses match. Receipt15Nov1964/publication1966, source sheet undated.','MPL_16+47+54+44#70')
link('published work','cote54 scan6;tex2707–2710','EGAIV3 Prop11.4.5,pp146–147',
 'Universal generic closed flattening stratum, including simultaneous freeness on a chosen finite affine cover.',
 'Both endpoints read. Published Y irreducible; source Y merely nonempty. The additional reduction is proved separately and labelled reconstruction.','MPL_16+47+54+44#70')
link('published work','cote54 scans4,6;tex2664–2666,2710','EGAIV3 Th11.4.1,pp143–145;Cor11.4.4,pp145–146',
 'Original nilpotent flatness descent and the universal ideal referred to as4.1bis.',
 'Exact primary theorem and proof read. They validate the nilpotent mechanism, not the canceled nonnilpotent amendment.','MPL_16+47+54+44#70')
link('published work','cote54 scan4;tex2664–2677','EGAIV3 Prop11.4.7,p147',
 'Published nonnilpotent flatness criterion adds explicit equivalence of adic topologies.',
 'Both endpoints read; the missing hypothesis is mathematically material, as the independent k[t] counterexample shows.','MPL_16+47+54+44#70')
link('published work','cote44 scan5;tex2893–2935','SGA3XXI Def1.1.1,Lem1.1.9,Cor1.1.11,§1.2',
 'Root data, invariant form and contragredient paired reflections.',
 'Both endpoints read. The source’s rational-perfect pairing is weaker than a full integral dual lattice pair; its earlier integral-coroot inference is refuted. No authorship of the reused draft is assigned.','')
link('published work','cote44 scan6;tex2942–2944','Grothendieck1962Picard FGA VI§4,p242',
 'Matsusaka’s numerical-versus-torsion algebraic equivalence theorem for divisors.',
 'Both endpoints read; source does not explicitly restrict Th7 to divisors and does not defineτ.','MPL_16+47+54+44#78')
link('published work','cote54 scans5,7;tex2696–2701,2727–2730','Gabriel1970 SGA3VIIB Cor4.4.1',
 'Height-one group schemes and restricted Lie algebras.',
 'Both endpoints read. The categorical equivalence concerns height≤1, not arbitrary finite p-torsion from ordinary Lie algebra alone.','MPL_16+47+54+44#68;#69')
link('published work','cote44 scans2,8;tex2793–2800,2974–2979','Kleiman1971ICM pp446–447',
 'Published account attributes the bounded Picard-family mechanism to an unrecorded1964 observation of Grothendieck.',
 'Both endpoints read. Supports the incidence model historically, while the local Albanese-equivalence definition remains unknown. This is publication by Kleiman reporting Grothendieck, not a newly identified own paper.','MPL_16+47+54+44#72;#73')
link('published work','cote44 scan8;tex2968–2981','Grothendieck1964Letter,CSG transcriptionL23d,April2024',
 'Parallel public transcription of the dated Serre letter.',
 'Both transcriptions read; neither is the absent image for the separate programme leaf. Public transcription is not a1964 publication.','MPL_16+47+54+44#72;#74;#77')
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
tsv('our_project_leads.tsv',['kind','from','to','what','evidence','note_ids'],[])
(ROOT/'our_project_leads.md').write_text('# Other-project leads\n\nNo assigned entry (#44–79 and #85) makes a substantive link to La Longue Marche, Les Dérivateurs or a named external research run. The heading S6 elsewhere in the mixed notes is an entry label, not evidence of the user’s S6 project. Consequently this worker adds no invented other-project link. Cross-cote43 comparisons are handled at the two read endpoints by the Pro43 worker and root integration.\n')
print('Reading alarms:',len(read))
print('Entire source pages covered:',len(coverage))
print('Checked links:',len(links))
print('Other-project leads:',0)
