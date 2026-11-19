"""Serialize explicit, manually adjudicated close readings of 170 entries.

No heading, keyword, or cue classifier is used.  The groups and decisions below
were made after reading both complete transcriptions and every note entry.
"""
from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
O=R/'work/early'; O.mkdir(parents=True,exist_ok=True)
P={'A':'MPL_136_002-046','B':'MPL_136_047-094'}
items=[]; entries=[]
def add(n,src,kind,loc,words,statement,reconstruction,check,reason,correct=''):
    sources=[P[s[0]]+'#'+s[1:] for s in src.split()]
    lines=[]; scans=[]
    for spec in loc.split(';'):
        pkg,pages,ls=spec.strip().split(':')
        sp=[]
        for a in pages.split(','):
            if '-' in a:
                lo,hi=map(int,a.split('-')); sp+=list(range(lo,hi+1))
            else: sp.append(int(a))
        scans+=sp
        lines.append({'file':P[pkg]+'_transcription.tex','scans':sp,'lines':ls})
    iid='SA08-'+str(n)
    items.append(dict(id=iid,sources=sources,kind=kind,cote='136',scans=sorted(set(scans)),lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    corrections=set(correct.split())
    for j,(s,eid) in enumerate(zip(src.split(),sources)):
        verdict='corrected' if s in corrections else ('kept' if j==0 else 'merged into '+iid)
        entries.append(dict(entry_id=eid,item_id=iid,verdict=verdict,reason=reason))

add(1,'A3 A4 A88 B3 B62 B69','title, date or page count','A:2-4:2-50;B:48,54,78,80,83,89,91,94:2-4,293,1441,1483-1487,1611,1904,2023,2105-2174',
    'Complexe DR à p.d. et ombres des modules; Plan conf. IHES en 1976; 1 Historique',
    'The cover and lecture-plan annotation identify the topic and the written year 1976. The historical list is followed by the PD simplex, shadows, questions, arithmetic, integration and internal topos constructions. This is an editorial reconstruction of bundle order, not proof that every later sheet belonged to the delivered lecture.',
    'No exact lecture day, attendance, or total lecture page count is supplied. B62’s previously missing first leaves are now available; the separate Pursuing Stacks retrospective must be collated externally.',
    'agrees','The titles, date annotation and order are present. The later-package gap concerning the opening plan is closed by scans 2–4, but its Carmona/publication and retrospective questions are independent.','B62')
add(2,'A100 B70','title, date or page count','A:2-18,36,38,40,42,44,46:7-365,1033-1060,1121-1141,1183-1217,1259-1301,1353-1382,1418-1450;B:49,51,53,55,57,59,61,63,71,73,84,86,88,90,92-94:82-109,165-200,253-292,362-394,475-513,536-565,589-614,683-717,1061-1093,1134-1170,1648-1703,1746-1819,1836-1891,1968-2000,2054-2102',
    'mspage{(1)}; mspage{2}; IX; 6; 5; 4',
    'Archive scan identifiers, parenthesized lecture folios, lower-margin foliation, and donor typescript pages are separate numbering systems. Package A contains 44 retained scans (2–46 except 19); B contains 46 (48–78 and 80–94). Scan 93 has only foliation. These are supplied-file counts, not author-written totals.',
    'The person responsible for lower marginal numbering is not identifiable from the transcription.',
    'agrees','The distinct page markers and reversed donor-page sequences are retained. They cannot be used interchangeably as locators or treated as a count on the cover.')
add(3,'A1 A12 A16 B2 B32 B46','unproved claim','A:8-10:165-244;B:80-82,94:1488-1578,2149-2152',
    'acycliques sauf le dernier; tronquée en ... degré n; j≤i',
    'For S=Γ_k(T), the universal simplex algebra is C^{p,q}=Γ_k^p(Φ)⊗Λ_k^q(Ψ), with exterior degree q, total weight w=p+q and d:(p,q)→(p−1,q+1). Under exactness of each augmented weight strand and section-acyclicity of its terms q<w, its sections have H^q≅H^q(X,k)T^[w] for 0≤q≤w, and zero for q>w.',
    'The clean w,q statement is a reconstruction of the intended comparison, not an emendation of p=0/H⁰ readings. Dimension shifting supplies the endpoint; the last term need not be acyclic.',
    'agrees','The notes correctly retain the second grading, exceptional last term and comparison range. The fixed-weight strand, rather than fixed complementary degree, is a complex.')
add(4,'A2 A35 A98','self-flagged step','A:16:325-329;B:80-82,89,91:1488-1606,1891-1964,2021-2048',
    'Faisceautisation; si k est un Anneau comm. d’un topos; définir ... Rf_*',
    'Grothendieck proposes PD differential algebras internal to a ringed topos and structured derived direct images. Later sheets formulate test embeddings k→Φ with flat quotient and tensor-stable acyclicity, not a new site or a separate geometric object identified with the modern crystalline or de Rham topos.',
    'The term “internalization” and the distinction between an algebraic construction and its derived direct image are modern restatements.',
    'agrees','Both the opening program and later concrete embedding data are present. The earlier run’s modern-site analogies have no textual identification behind them.')
add(5,'A5','self-flagged step','A:3:15-35',
    'Notion des formes diff. (Poincaré ?); De Rham (conjecturé par E. Cartan)',
    'The historical plan questions the attribution of differential forms to Poincaré and recalls the de Rham theorem as conjectured by Élie Cartan; it also has a doubtful parenthetical question about the base of the arithmetic theory.',
    'These are historical attributions and one unreadable scope question, not new mathematical conjectures.',
    'agrees','The question mark is explicit. A historical priority claim cannot be settled by normalizing the uncertain words.')
add(6,'A6','self-flagged step','A:3-4:37-50;B:49,51,53:86-107,169-197,257-290',
    'simplement connexe (sauf erreur); une équivalence de cat.',
    'The recalled Sullivan result recovers rational homotopy from a nonnegative commutative differential graded Q-algebra with H⁰=Q and H¹=0. A precise standard equivalence requires the relevant rationalization and finite-type or appropriate duality hypotheses; these are not all written in the opening sentence.',
    'Finite-type restrictions in the modern theorem are supplied explicitly as modern hypotheses, not attributed to this sentence. Reused English minimal-model text is a separate source layer.',
    'agrees','The note correctly identifies “sauf erreur” and does not backfill an editorial finiteness condition into the quote.')
add(7,'A7','unproved claim','A:4-5:56-95',
    'résolution de Q_*; objets acycliques; ce qui se vérifie facilement',
    'Polynomial rational forms on each affine simplex resolve Q by algebraic Poincaré, and their degreewise simplicial coefficient objects are asserted acyclic; both properties underlie comparison with ordinary rational cohomology. Smooth/analytic variants are additional asserted cases.',
    'Acyclicity on each simplex is distinct from the acyclicity required after applying sections on a simplicial slice.',
    'agrees','The two assertions are separately written, but the second is compressed into “easily checked”; the notes do not promote that phrase to a supplied proof.')
add(8,'A8 B54','self-flagged step','A:5:88-95;B:69,75-77,81:974-987,1238-1437,1540-1554',
    'On aimerait avoir une Z-algèbre diff.; il paraît qu’il y a des ths contre !',
    'The hoped-for functorial integral anticommutative cochain algebra must be separated from the weighted PD construction actually made. Later obstruction theorems for natural unital commutative cochain theories have additional model-acyclicity and all-spaces comparison hypotheses; they do not refute the weighted finite-range result.',
    'The identification with a specific later obstruction is a literature comparison, not an attribution in the manuscript.',
    'agrees','The warning and qualified ambition are explicit, and the later text preserves weights and leaves product obligations open.')
add(9,'A9','withdrawn in the same text','A:6-7:106-142',
    'on aurait envie de prendre; mais ce n’est plus; t∈J',
    'The naive PD affine simplex with ΣX_i=1 does not admit the proposed coordinate-elimination map into the standard integral PD polynomial algebra, because 1−Σ_{i<n}X_i is outside its PD ideal. Replacing 1 by a chosen t in a PD ideal J⊂S repairs that coordinate substitution.',
    'The rejected step is the proposed integral elimination argument, not the later parameterized construction.',
    'agrees','The failed proposal and replacement occur consecutively on scan 6.')
add(10,'A10','unproved claim','A:6-7:121-160;B:69:974-986',
    'est une résolution de S; augmentée vers S/J',
    'For a commutative PD ring (S,J,γ) and t∈J, the simplex algebra (S⟨X_0,…,X_n⟩⊗Λ(dX_i))/(ΣX_i−t,ΣdX_i)_PD is isomorphic as a differential S-algebra to S⟨X_0,…,X_{n−1}⟩⊗Λ(dX_0,…,dX_{n−1}), resolving S. Its extra augmentation has target S/J.',
    'The contraction d(X^[m])=X^[m−1]dX provides an independent proof; the augmentation to S/J is not the quasi-isomorphism target.',
    'agrees','The two targets are explicitly different in the manuscript and are correctly separated in the entry.')
add(11,'A11','other','A:7:148-160',
    'Mais on ne peut dire en général quelle est sa cohomologie; elle ne sera pas isom.',
    'For an arbitrary PD triple (S,J,t), objectwise exactness of the simplex complex does not imply that Hom(X_*,C_*) computes H*(X_*,S) uniformly in X. The author explicitly denies this unrestricted conclusion.',
    'No particular counterexample is asserted on this line; modern counterexamples must state the coefficient and simplicial conventions.',
    'agrees','The note preserves an express limitation of the author’s construction.')
add(12,'A13','idea of the earlier run','A:8:195-198;B:74,83,89,94:1190-1195,1613-1619,1914-1919,2110-2132',
    'alternée; pour degré ext',
    'Alternation and the Koszul sign use exterior/cohomological degree, not total weight: over Z, T has weight 1 and exterior degree 0, and T²=2T^[2]≠0. The earlier run correctly diagnoses the incompatible gloss “alternating in total degree.”',
    'The T² diagnostic is the earlier run’s mathematical test; later manuscript lines explicitly name exterior degree.',
    'agrees','The algebra formula and later explicit parity convention support the diagnostic; no ink is changed.')
add(13,'A14','unproved claim','A:9:202-219',
    'homotope à 0 donc ... Γ^p ... si p≠0',
    'An actual simplicial contraction of Φ can be carried through the functor Γ^p and tensor construction, giving contraction of Γ^pΦ⊗Λ^qΨ for p>0. A nonlinear divided-power functor is not thereby proved to preserve arbitrary quasi-isomorphisms.',
    'The claim concerns simplicial homotopies and the particular object; this is the precise modern interpretation of the written implication.',
    'agrees','The note correctly demands contraction rather than substituting acyclicity of an arbitrary chain complex.')
add(14,'A15','reading question','A:9:211-219',
    'si p≠0; si p=0; acycliques sauf le dernier',
    'The consecutive acyclicity sentences conflict: the preceding contraction argument requires positive complementary degree, while the next line literally reads p=0. The endpoint C^{0,w} must remain exceptional in the following weight-strand argument.',
    'Proposed mathematical alternative p≠0 is an alarm only; whether this is ink or transcription is undecided.',
    'agrees','The note reports the literal conflict accurately; a scan check is required.')
add(15,'A17','reading question','A:10:230-244',
    'H^0(X_*,k) ...; H^q(X_*,k) ...',
    'For fixed exterior degree q the first shadow formula uses H⁰ twice, while the reindexed formula on the same page uses H^q. The latter is compatible with the preceding weightwise calculation; the former is false for q>0 in general.',
    'H^q in the first two occurrences is a proposed correction, not a new transcription.',
    'agrees','The note locates the genuine same-page discrepancy.')
add(16,'A18 B33 B66','unproved claim','A:10-11:240-250;B:80-83:1514-1554,1611-1645',
    'compatibles avec les structures multiplicatives; accouplements déduits du cup',
    'If the canonical weighted comparison is multiplicative, classes in weights r and s multiply as binom(r+s,r) times their ordinary cup product, in weight r+s. Equal-weight odd squares can vanish while differently weighted representatives retain a nonzero ordinary square (e.g. weights1,2 over F₂ have coefficient3).',
    'The explicit coefficients and characteristic-two illustration are modern calculations/earlier-run diagnostics. Multiplicativity requires a structured comparison beyond additive dimension shifting.',
    'agrees','The entry’s weighted qualification agrees with k⟨T⟩ multiplication and the author’s explicit claim; it does not impose ordinary PD operations on unweighted cohomology.')
add(17,'A19 A90','other','A:11,23-25:248-250,589-678',
    'la qième ombre de M; Cette théorie des ombres étant ... acquise',
    'The N-th shadow of a k-module M is ω_N(M)=⊕_{i≥N}M T^[i] over Γ_k(T), with the binomial action. The opening asserts recovery of M and pairings; scans20–34 later provide finite-tail proofs. No “tubulure” is defined in this range.',
    'The correction of the tensor base in the displayed definition is separately registered; terminology in other cotes is not identified without its source.',
    'agrees','The definitions and later argument support the note’s chronology; the opening statement is initially conditional.')
add(18,'A20','unproved claim','A:11-12:250-257',
    'en raffinant un peu; RΓ ... plus l’accouplement de cup-produit',
    'Grothendieck claims that the structured weighted complex recovers RΓ(X,k) in D(k), together with RΓ⊗^L_k RΓ→RΓ. This contains both a linear derived reconstruction assertion and a compatible monoidal assertion.',
    'Finite-tail full faithfulness of modules alone proves neither part; any repaired quotient and enhancement must be stated separately.',
    'agrees','The derived cup-product display is explicit. The note correctly distinguishes it from the already proved underived recovery.')
add(19,'A21 B51','unproved claim','A:12:261-268;B:69,80:974-987,1510-1526',
    'quelque soit k; C_DRS(X,k_Q)≃C_DRpd(X,k)/(T−1)',
    'The ordinary coefficient quotient Γ_k(T)/(T−1) is k⊗Z Q: T^n=n!T^[n] makes every factorial invertible, and T^[n]↦1/n! gives the inverse. The manuscript claims the analogous global cochain specialization; this additionally depends on how weights and infinite simplicial limits are assembled.',
    'The coefficient proof does not settle the global formula for arbitrary X. PD specialization to t∈J on scan69 is a different construction.',
    'agrees','The notes correctly distinguish the ordinary ring quotient from a PD ideal quotient and flag the global-limit issue.')
add(20,'A22','idea of the earlier run','A:12:261-268',
    'quelque soit k',
    'For countably many discrete points and direct-sum assembly of weights, specialization gives (Z^N)⊗Q→Q^N, whose image has a common denominator; (1/p_j) for distinct primes is missing. Quotienting the ordinary ungraded product ∏Γ_Z(T) by the common principal relation T−1 instead does commute with that product.',
    'This conditional counterexample is an earlier-run diagnostic, not a manuscript example or a proof against every assembly convention.',
    'agrees','The note’s correction of the overly broad “quotients do not commute with products” warning is mathematically necessary and consistent with the unresolved convention.')
add(21,'A23','self-flagged step','A:12:269-274',
    'Et plus gén. encore; ?',
    'The bracketed claim extends specialization to a PD triple (S,J,t), comparing the quotient by t−1 with Sullivan forms over S_Q/(t−1). A marginal question mark follows it, but its exact attachment is not secured by the transcription.',
    'No precise authorial conjecture is inferred solely from the marginal mark; global totalization remains a separate issue.',
    'agrees','Both the generalized formula and the uncertain nearby question are preserved in the note.')
add(22,'A24','conjecture','A:12-13:276-291',
    'Je suis convaincu que la structure à p.d. ... est importante',
    'The author expects the divided powers on the augmentation ideal to contain information essential to integral homotopy reconstruction, and expressly includes them among all the structures to be retained.',
    'This is a stated conviction rather than a proposition specifying which information is detected.',
    'agrees','The words and their placement before the reconstruction question support exactly this level of assertion.')
add(23,'A25','unpursued implication','A:7-8,13:133-159,195-198,285',
    'd(x^(n))=x^(n−1)dx; compatibles avec la diff',
    'The differential identity makes appropriate divided powers of closed even elements closed. To induce operations on cohomology one must also prove that changing a representative by a boundary leaves the cohomology class unchanged, with the precise PD domain specified.',
    'This extra obligation is an implication identified by earlier notes, not an explicit descent theorem on these pages.',
    'agrees','The notes do not infer a cohomological PD structure from compatibility alone.')
add(24,'A26','self-flagged step','A:13:285-291;B:94:2110-2174',
    'q-ombres?; en inversant les flèches ... qu-isom',
    'The proposed virtual DR category combines nonnegative bigrading, augmented alternating algebra, compatible divided powers and differential, and cohomology shadows, then localizes designated quasi-isomorphisms. The definition of its shadow condition and precise enhanced localization is unfinished at this point.',
    'An ordinary category of fractions is distinguished from a model or infinity category; no such enhancement is silently supplied.',
    'agrees','The note accurately treats this as a proposed framework, not an established equivalence.')
add(25,'A27 B57','conjecture','A:12-13,17-18:280-291,357-363;B:77,94:1410-1437,2160-2174',
    'on peut se demander si ... induit une équivalence',
    'For connected simply connected spaces satisfying the written finite-generation qualifications, ask whether the integral PD complex with all structures determines homotopy type, and whether a suitably restricted derived category of such objects is equivalent to that homotopy category. The margin says homology of finite type; it does not unambiguously say all homotopy groups.',
    'Modern E∞-cochain and cosimplicial-binomial reconstruction theorems concern different targets and cannot identify this category without a comparison functor.',
    'agrees','The question is explicit, with connectivity and finiteness. The later note’s modern-theorem comparison is only a comparison, not a claimed solution.')
add(26,'A28','unproved claim','A:14:297',
    'résultats partiels négatifs; auto multiplicatifs ... rien d’intéressant',
    'Only a restricted method—multiplicative automorphisms of the universal simplicial DRpd object—is reported to yield no interesting Steenrod/Whitney-type operations. This is not a no-go theorem for all higher operations on any enhancement.',
    'The exact automorphism classification is deferred to the later pages; no proof is reconstructed here from this summary.',
    'agrees','The note keeps the quantifier restriction present in the sentence.')
add(27,'A29','self-flagged step','A:14:299',
    'Il faudrait sans doute donner des modèles minimaux ... Je n’ai rien fait',
    'Develop integral analogues of Sullivan minimal models capable of recovering homotopy groups from the structured PD complex, under the stated connectedness and finiteness restrictions.',
    'The author expressly says no work has been done; later comparison zigzags are not minimal models.',
    'agrees','The desideratum and non-construction are explicit.')
add(28,'A30','self-flagged step','A:14:299',
    'Je n’ai = pas développé une formule de Künneth; plats sur k{T}',
    'Find a Künneth/product comparison for DRpd(X×Y) retaining its structures. Potential nonflatness is over Γ_k(T), so underlying k-flatness alone does not justify an ordinary tensor product formula.',
    'A derived tensor comparison is a modern candidate, not a formula supplied in the manuscript.',
    'agrees','The note correctly records both the missing theorem and the base ring relevant to the difficulty.')
add(29,'A31 A32 A33','unproved claim','A:15:305-322',
    'Il est possible ... de définir; compatible avec ... structures; commute aux ... quelconques',
    'A differential bigraded coalgebra with divided copowers is announced that corepresents the cochain construction in every k-algebra k′ via Hom_k(C_chain(X,k),k′), commutes with coefficient extension, and preserves arbitrary colimits of the simplicial input. These are chain-level and ordinary categorical assertions.',
    'Corepresentability is stronger than dualizing one coefficient realization; arbitrary cohomological base change and homotopy-colimit preservation are not asserted by these formulas.',
    'agrees','The three entries concern the same announced corepresenting construction and its explicitly listed functorialities.')
add(30,'A34','idea of the earlier run','A:15:310-322',
    'au lieu de son dual; sans condts de finitude',
    'Audit the no-finiteness strategy by distinguishing direct-sum chains, the product-valued linear dual, restricted duals and completed operations; Hom_k(⊕M_w,k)=∏Hom_k(M_w,k) does not give unrestricted reflexivity.',
    'This is the earlier run’s proposed test of the author’s strategy, not a proved homotopy reconstruction theorem.',
    'agrees','The no-finiteness proposal motivates the diagnostic, while the page does not supply completion data.')
add(31,'A36','self-flagged step','A:16:329',
    'qu. iso. ... composantes ... flasques (mais y en a-t-il tjrs ?)',
    'For a PD differential algebra in a ringed topos, ask for a quasi-isomorphic replacement in the same structured category with sufficient degreewise acyclicity to define structured Rf_*.',
    'The phrase does not quantify a settled notion of universal acyclicity or specify an enhanced derived category.',
    'agrees','The existence question is explicit and not solved merely by the internal algebraic definition.')
add(32,'A37 B43','self-flagged step','A:16:329;B:91:2021-2031',
    'topos des ens. cosimpliciaux; le Pb est ouvert ... posé par Deligne; Non',
    'The opening reports Deligne’s structured derived-image problem for cosimplicial sets. Scan91 answers “No” to the later, specific existence condition for a universal DR test embedding in the cosimplicial topos. The latter negative does not by itself solve every formulation of the former problem.',
    'The scope distinction is editorial; the negative answer’s proof is absent on scan91.',
    'agrees','The note correctly preserves cosimplicial variance and records a locally answered question rather than leaving the narrow question open.')
add(33,'A38','self-flagged step','A:16:329;B:91:2025-2029',
    'sauf erreur (si souvenirs sont exacts); espaces topologiques paracompacts',
    'Grothendieck tentatively recalls a construction for paracompact spaces, later asserting a topological-space example of the DR condition. No source or complete site/acyclicity hypotheses are supplied here.',
    'The later broad example is not a proof that the earlier tentative recollection works for arbitrary topoi.',
    'agrees','The hedged recollection and later assertion have different evidential strength.')
add(34,'A39 B22','unproved claim','A:17:337-354;B:74:1188-1233',
    'résolution de k; Coker ... par dT; Im=Ker',
    'Let D=Γ_k(Φ)⊗Λ_k(Φ) with de Rham differential. Its positive total-weight strands are exact. For a distinguished diagonal vector T, exterior multiplication by dT is square zero and exact, and the quotient by dT identifies with Γ(Φ)⊗Λ(Φ/k); multiplication by dT realizes that quotient as a kernel with exterior-degree shift.',
    'The identification is of complexes with a sign adjustment. It does not make the shifted inclusion an algebra map; termwise simplicial acyclicity is separate from algebraic exactness.',
    'agrees','The later formulas clarify the earlier kernel indices without altering them.')
add(35,'A40 B23 B25','withdrawn in the same text','A:17:345-355;B:74-76:1233-1250,1326-1374',
    'à expliciter; est faux; i(x)i(y)=0',
    'The proposed direct compatibility of the kernel realization with multiplication and divided powers is retracted. In the ambient exterior algebra the kernel image consists locally of multiples of dT and has square-zero product; the nonzero DR product must instead be transported through a quotient or specified separately.',
    'The earlier run’s product diagnostic identifies the precise mismatch. It does not prove that all transported products are impossible.',
    'agrees','The withdrawal spans scans74–75; the following pages rebuild partial operations rather than retracting the whole construction.')
add(36,'A41 A42 A44','conjecture','A:14,17-18:297,335-363',
    'La structure multiplicative à pd cohomologique; en un sens convenable; J’ignore si',
    'A stronger cohomological multiplicative PD invariant is proposed, expected to recover C, D and Sullivan forms. The author does not know whether C or even D already determines it; if not, this stronger structure would be the intended homotopy classifier under connectivity and finiteness.',
    'Higher coherent chain operations are an earlier-run test for what “all structures” might require, not an identified E∞ structure in these pages.',
    'agrees','The conditional alternative and explicit ignorance prevent identifying the program with a completed invariant.')
add(37,'A43','reading question','A:4,7:75-79,148;B:50-52,58:139-156,200-250,515-529',
    '½ simpliciale (et = simpliciale); Δ^op',
    'Here historical “semi-/½-simplicial” usage includes degeneracies: the parenthetical equality with simplicial, all ordinal maps and normalized-cochain degeneracies make this explicit. It cannot automatically be replaced by modern Δ_inj terminology.',
    'The modern indexing-category identification is an interpretation established from the written structure maps.',
    'agrees','The opening and subsequent explicit degeneracies settle the basic convention, while other project uses remain distinct.')
add(38,'A45 B55','idea of the earlier run','A:8-9:165-209;B:80-83:1488-1645',
    'k{T}; d ... degré total',
    'For integer-valued polynomials B=Int(Z), the degree filtration has gr B≅Γ_Z(T), since binom(x,r)binom(x,s) has leading coefficient binom(r+s,r) relative to binom(x,r+s). A comparison with the PD simplex must additionally respect ΣX_i=T, differential, simplicial operators, filtrations and derived realization.',
    'The algebraic associated-graded identity and proposed comparison are earlier-run deductions, not a manuscript theorem identifying the models.',
    'agrees','The manuscript supplies the PD side only; the note correctly labels the bridge as a proposed experiment.')
add(39,'A46','reading question','A:15:305-318',
    'pour k′ ... variable; Hom_Z(C_chain(X,k),k); Hom_k(...,k′)',
    'The ordinary chain/cochain display has unreconciled coefficient symbols after a correction from Z to k, whereas the next PD display explicitly varies k′ and uses Hom_k. These formulas cannot justify identifying Z-linear and k-linear duals without restrictions.',
    'A clean formula over integral chains or Hom_k into k′ is proposed only as an editorial alternative.',
    'agrees','The note reports the actual variable/subscript inconsistency.')
add(40,'A47','reading question','A:8:180-189',
    'Φ_k* → k_*; inclusion diagonale; Ψ=Φ/(k_*)',
    'The arrow labelled diagonal inclusion points from Φ to k although the next formula forms the quotient of Φ by diagonal k. The mathematical construction requires k→Φ; the scan must decide the arrow reading.',
    'Arrow reversal is a suggested alternative, not an authorized emendation.',
    'agrees','The same-page type mismatch is explicit.')
add(41,'A48','unpursued implication','A:20-21:371-498',
    'c_ij≡∏c_uε,vε (p); uε+vε≤p−1',
    'For p prime and nonnegative i,j, c_ij=(i+j)!/(i!j!) is prime to p exactly when their base-p addition has no carry; its residue is the product of digitwise c values. The manuscript writes a low-digit induction and two useful recurrences when p divides N+1.',
    'This is the classical Lucas/Kummer arithmetic, with local transcription anomalies kept separately; no new priority is asserted.',
    'agrees','The proof is written out rather than merely invoked, and its exact arithmetic has been retained for rechecking.')
add(42,'A49','unpursued implication','A:21-23:501-578',
    'mais pas néc. =x_4; Alors ... x_N=x_N+1',
    'For a Z_(p)-module E, N≥0, e≥0 with p^e≥N+1, and I={N}∪{N+p^ε:0≤ε≤e}, the relations binom(j,i)(x_j−x_i)=0 for i=N,N+1 and i<j∈I imply only x_N=x_N+1. For p=2,N=2,e=2, x_4 remains independent of x_2=x_3=x_6 over F₂.',
    'The explicit counterexample confirms the limit of the sparse lemma; the all-pairs infinite theorem is stronger.',
    'agrees','The limitation is the author’s own margin, correctly preserved by the entry.')
add(43,'A50','unpursued implication','A:22-23:513-587',
    'Théorème 1; ... x_i=x_N ∀i≥N; cqfd. Ouf !',
    'For any abelian group E and family (x_i)_{i≥N}, if binom(j,i)(x_j−x_i)=0 for every j>i≥N, then the family is constant. The written proof localizes at every prime and applies the sparse lemma successively; it needs no torsion-free or finite-generation assumption.',
    'The proof’s local-to-global injectivity is standard localization of abelian groups; “Ouf” marks completion, not an open step.',
    'agrees','The note correctly identifies a proved theorem and does not count its concluding exclamation as uncertainty.')
add(44,'A51 A52 A55','unpursued implication','A:24-25:603-674',
    'pleinement fidèle; Bijectivité?; π_N(M)⊂∏M_i',
    'For every commutative k and N≥0, ω_N:k-Mod→gr-Γ_k(T)-Mod is fully faithful. Its right adjoint is the compatible-family equalizer π_N(V)={(x_i)_{i≥N}:T^[j]x_i=binom(i+j,i)x_{i+j}}. The unit M→π_Nω_N(M) is an isomorphism by tail rigidity, also applied to Hom_k(M,M′).',
    'This coefficient-module right adjoint differs from the graded right adjoint to truncation; exactness and derived recovery are separate questions.',
    'agrees','The page immediately answers “Bijectivité?” and supplies the full-faithfulness proof; the three notes concern this single recovery mechanism.')
add(45,'A53','reading question','A:23,25:589-595,676-678',
    'ω_N(M)=M⊗_S S^+(N); ω_0(M)=M⊗_k S',
    'M is declared only a k-module, so the first tensor product over S is not typed as stated. The direct-sum description and later formula indicate M⊗_k S^+(N).',
    'Changing the base from S to k is a mathematical suggestion pending scan review.',
    'agrees','The note identifies a real type discrepancy rather than assuming an unstated S-action.')
add(46,'A54','withdrawn in the same text','A:23:589-591',
    'deleted: engendré par T^(N); défini par Σ_i≥N k.T^(i)',
    'The one-generator PD-ideal description is deleted in favor of the full graded tail. Over Γ_F₂(T), the PD ideal generated by T^[3] does not contain T^[4]: its only degree4 product coefficient is4, and higher PD powers begin in degree6.',
    'The degree4 example is the earlier run’s explanatory test of a deletion, not an example written by Grothendieck.',
    'agrees','The retained definition is the full tail, so the rejected generator statement is not part of the live theorem.')
add(47,'A56','other','A:25-26:676-686',
    'les foncteurs τ_N ne sont pas pl. fidèles bien sûr',
    'The truncation τ_{≥N} on all graded S-modules is not fully faithful: for N≥1 it kills a module supported in degree N−1. Full faithfulness holds only for the coefficient-shadow functor, not for arbitrary virtual shadows.',
    'The one-degree module is a direct modern verification of the author’s explicit distinction.',
    'agrees','The note correctly preserves the distinction.')
add(48,'A57 A61','self-flagged step','A:26-27:685-718',
    '[à degrés ≥0?]; isom en degrés ≥0',
    'The ambient grading of virtual shadows is initially questioned, but the stronger unit theorem explicitly asserts recovery only in nonnegative degrees. It does not assert an isomorphism of all Z-graded components; in characteristic zero a tail admits negative-degree maps related to Laurent shifts.',
    'This identifies the theorem’s written support restriction, without retroactively fixing every earlier ambient category.',
    'agrees','The notes accurately correct a broader context summary while preserving the full manuscript qualification.')
add(49,'A58','reading question','A:26:687-695',
    'τ_N(M)↪M; adjoint à droite; Hom(N,τ_N(M))',
    'The displayed adjunction has wrong variance if read literally. Over S=Q[t], N=1 and both named objects S, Hom_gr(S,tS)=0 whereas Hom_gr(tS,tS)=Q. The inclusion and the right section functor are distinct: inclusion i_N is left adjoint to truncation, which has its own right adjoint.',
    'The proposed correct adjunction chain is mathematical reconstruction; the written arrows/Hom arguments require ink review.',
    'agrees','The earlier run’s counterexample satisfies all named graded hypotheses and exposes the display’s mismatch.')
add(50,'A59','unproved claim','A:26:697',
    '∀x ... S^+(N).x=0; C’est encore une sous-catégorie épaisse',
    'The elementwise tail-annihilated modules are asserted thick. This is false for S=Γ_Fp(T): with I=S_+, both I/I² and S/I are elementwise negligible, but S/I² is not, because the class of1 is hit nontrivially by arbitrarily high p-typical generators. Thus 0→I/I²→S/I²→S/I→0 violates extension closure.',
    'The counterexample was identified in earlier notes and is rechecked here; a Serre/localizing closure is a different category and is not substituted into the transcription.',
    'agrees','The source really makes the false thickness claim, and the entry correctly distinguishes it from fixed-cutoff and uniformly bounded classes.')
add(51,'A60','unproved claim','A:26-27:697-715',
    'et le localisé est; ou encore; Im ess φ_0,∞',
    'The finite essential-image conditions are called equivalent to an infinite-localization condition, but the preceding quotient definition breaks off and its proposed negligible class is not extension closed. Finite-tail arithmetic alone does not define a valid Gabriel quotient or prove the asserted infinite equivalence.',
    'Any repaired quotient from other research runs is external work, not this page’s completed construction.',
    'agrees','The note correctly separates the finite theorem from an unfinished and defective infinite setting.')
add(52,'A62','unproved claim','A:27:729-733',
    'Ext^n(τ_(N−i)(S)[−i],M⊗_k S)=0 si n>0',
    'The displayed higher-Ext vanishing is announced for i≥0 in the nonnegative recovery range. The following argument proves only a Hom-family theorem; an Ext proof needs an appropriate exact adjunction or explicit resolution in the specified graded category.',
    'The precise category and interpretation of τ at nonpositive bounds must be stated before applying the formula.',
    'agrees','The note correctly records the corollary as unproved in this range rather than treating ordinary full faithfulness as a derived theorem.')
add(53,'A63 A64 A68 A70','unpursued implication','A:27-34:737-1002',
    'c_ℓ,k ξ_k=c_ℓ,k−i ξ_k+ℓ; ξ_k=binom(k,i)ξ; Présentation plus simple',
    'For an abelian group M, 0≤i≤N and a family (ξ_k)_{k≥N} satisfying c_{ℓ,k}ξ_k=c_{ℓ,k−i}ξ_{k+ℓ} for ℓ≥0, there is a unique ξ with ξ_k=binom(k,i)ξ. Prime-local no-carry coefficients connect each index to p^r−1; finitely many high binomial coefficients have gcd1, so a Bézout combination reconstructs ξ globally.',
    'The clean coefficients follow the theorem’s main statement, while its conflicting subscript occurrences are separately flagged. The long deleted carry algorithm is replaced locally by the completed-sum proof.',
    'agrees','The notes correctly identify a completed stronger arithmetic theorem, its constructive globalization and a proof simplification, not separate unresolved claims.')
add(54,'A65','reading question','A:20,28-32:379,746-761,918',
    'c_i,k−i; c_k,k−i; c_ab=(a+b)!/(a!b!)',
    'The two subscript patterns are not equal: c_{i,k−i}=binom(k,i), whereas c_{k,k−i}=binom(2k−i,k). At i=1,k=2 they are2 and3. Their alternation in the proof needs a reading check; the prior modernisation’s assertion that both equal binom(k,i) is mathematically false.',
    'Choosing c_{i,k−i} consistently is a reconstructed proof, not a correction of the ink.',
    'agrees','The entry correctly identifies both the manuscript anomaly and the erroneous explanatory gloss.')
add(55,'A66','other','A:21,23,28:502,587,750',
    'Z_p ... le localisé; Z_p:=Z_(pZ)',
    'The notation Z_p in the arithmetic means localization Z_(p), not p-adic completion. The coefficient modules need no completeness or separatedness assumption.',
    'Only notation is modernized; the underlying coefficient hypotheses are unchanged.',
    'agrees','The author explicitly defines the notation, so the note’s clarification is fully supported.')
add(56,'A67','withdrawn in the same text','A:30-31:810-842',
    'deleted: le quotient de (a) et (b); les deux quantités ... égales',
    'A factorial/divisibility calculation is deleted, but the retained proof establishes c_{j′−j,j+i}/c_{j′−j,j}=c_{i,j′}/c_{i,j}. When c_{i,j},c_{i,j′} are p-local units, the two coefficients in the recurrence have the same p-adic valuation; if units, vanishing propagates between ξ_k and ξ_k′.',
    'The rational identity is independently recomputed; deleting one calculation does not withdraw Lemma1.1.',
    'agrees','The entry preserves the local revision and retained argument.')
add(57,'A69','reading question','A:32:909-918',
    'les mêmes conditions ... c_i,k̃−i=0',
    'The comparison of two good indices requires c_{i,k̃−i} to be nonzero modulo p, but the line literally gives equality to zero. The surrounding unit hypothesis makes a sign or transcription error likely.',
    'Replace-by-unit-condition is a mathematical alternative only; the scan must decide.',
    'agrees','The note correctly identifies the internal contradiction and retains the existing index doubt.')
add(58,'A71','idea of the earlier run','A:25-27:658-715',
    'Néanmoins ils sont tous pleinement fidèles',
    'Test the pairing ω_N(M)⊗_Sω_N′(M′)→ω_(N+N′)(M⊗_kM′), and its derived/coherent version in a separately specified repaired quotient. For k=M=M′=Z and N=N′=1, weight2 is multiplication by2, so finite-tail full faithfulness does not make this map degreewise invertible.',
    'The proposed quotient and monoidal comparison belong to the earlier run’s open research program; only the displayed coefficient obstruction is established here.',
    'agrees','The note correctly distinguishes a product-comparison test from a consequence of linear full faithfulness.')

add(59,'A72','reading question','A:20:425-434',
    'Soit unsure{w′|w}=p+w′',
    'The carry case requires w=u+v=p+w′ and w′=u+v−p. The first symbol in the retained line is doubtful; reading w′=p+w′ would be impossible. Other letter variants quoted by a prior modernisation are not confirmed by the supplied transcription.',
    'The consistent formula is a proposed alternative only; manuscript ink decides the initial symbol.',
    'agrees','The note precisely distinguishes its retained reading from variants reported by another interpretation.')
add(60,'A73','unpursued implication','A:35,43:1008-1031,1304-1313',
    'v_p(n!)=(n−chif_p n)/(p−1); =0; T_r^p=pν′_r T_r+1',
    'Legendre’s digit-sum formula gives v_p((p^{r+1})!/((p^r!)^p p!))=0. Thus for T_r=T^[p^r], T_r^p=pν′_rT_{r+1} with ν′_r a p-local unit. The isolated v_p((n+1)!) line is unfinished and is not a completed proof.',
    'Factorial notation is parenthesized to remove ambiguity; the calculations are recomputed independently.',
    'agrees','The entry correctly links the completed valuation to the later p-typical relation, while keeping the abandoned line separate.')
add(61,'A74 A85','unproved claim','A:37,39,45:1063-1087,1144-1175,1413-1417',
    'Hom^d(M*,φ_N N*)≃Hom^d(τ_(N−d)M*,N*); indépendant ... α',
    'The shifted adjunction follows from the truncation/right-adjoint pair with target supported in degrees≥N. Combining it with nonnegative recovery makes Hom^{−d}(τ_α M_S,N_S), d>0, canonically independent of α≥d, by restricting to a common sufficiently high target cutoff.',
    'The unfinished specialization on scan37 is not silently completed as text; the support argument is a modern proof of the stated consequence.',
    'agrees','Both entries concern the same shifted recovery mechanism, and the required nonnegative support is retained.')
add(62,'A75','withdrawn in the same text','A:37:1098-1119',
    'Diagramme de Cayley; Mot ... g_i + origine',
    'The Cayley graph, generators and word fragment are in a deleted block. They are documentary residue, not a surviving step in the homogeneous-Hom proof or a definition of the shadow construction.',
    'No mathematical connection to other projects is inferred from a cancelled graph.',
    'agrees','The note correctly respects cancellation and physical text boundaries.')
add(63,'A76','withdrawn in the same text','A:39:1158-1178',
    'deleted d≥0; d≥β−α; mT^(j)↦c_dj u(m)T^(d+j)',
    'For β≥α≥0 and d≥β−α, degree-d S-linear maps τ_αM_S→τ_βN_S are parametrized by u∈Hom_k(M,N), with coefficient binom(d+j,d) on source degree j. The threshold ensures every output degree is retained.',
    'The correction is a bound on support, not merely a sign; the binomial factor is essential.',
    'agrees','The deleted and retained thresholds are visible on the same page.')
add(64,'A77 A78','reading question','A:39,41:1172-1178,1220-1242',
    'c_d,β−d u=0; α≤j<β−d',
    'For 0≤d<β−α, the same map is allowed precisely when c_{d,j}u=0 for α≤j<β−d. The displayed list incorrectly includes the endpoint β−d if read literally. Over F₂, α=1,β=3,d=1, multiplication by T is nonzero and valid; the extra equation3u=0 would exclude it.',
    'The strict endpoint is a mathematical correction and the F₂ example is an earlier-run test; neither decides the ink.',
    'agrees','The note accurately records the inconsistent endpoint and supplies a counterexample to the stronger reading.')
add(65,'A79','reading question','A:41,43,45:1245-1257,1325-1346,1413-1417',
    'd<0; un hom de degré d<p^r; p^s−d; Hom^(−d)',
    'The negative-degree calculation uses a positive size d for a shift of degree −d, although scan43 calls it a map of degree d. Its images lie in degree p^s−d, and scan45 explicitly states Hom^{−d}, d>0.',
    'A consistent reconstruction renames the positive shift size; no frozen occurrence is overwritten.',
    'agrees','The note identifies the actual sign-convention mismatch.')
add(66,'A80','reading question','A:43:1315-1319',
    'a comme base; Σi_αp^α≥p^r i.e. ∃α≥r ...',
    'The p-typical monomial basis and equivalence require finitely supported exponents 0≤i_α<p. Without digit bounds a lower generator can have weight≥p^r, and unrestricted monomials are not a basis because T_s^p=pν′_sT_{s+1}.',
    'Digit bounds are a necessary mathematical qualification, not words supplied by the transcription.',
    'agrees','The omitted hypothesis matters exactly as the note explains.')
add(67,'A81','idea of the earlier run','A:43:1319-1335',
    'les relations sont; est donné ... avec les relations',
    'The relations T_s^{p−1}t_s=pν′_st_{s+1} are necessary but do not present the tail ideal as an S-module by themselves. Over F₂ the quotient by only T_s e_s=0 still has nonzero T_{r+1}e_r−T_re_{r+1}, which maps to zero in the ideal; cross-generator syzygies are missing.',
    'The earlier run’s explicit syzygy refutes sufficiency of that literal list, while the negative-Hom proof uses only necessity.',
    'agrees','The note is a valid diagnosis of an overstrong interpretation, not a refutation of every subsequent conclusion.')
add(68,'A82 A83 A84 A86','idea of the earlier run','A:43,45:1304-1352,1385-1417',
    'ξ_s=pν′_sξ_s+1; N_0=∩_n nN; plus grand sous-module divisible',
    'The written p-local recurrence supplies coherent p-division after unit rescaling. The intersection N_∞=∩_{n≥1}nN need not be divisible: A=⟨x,y_n | px=0,p^ny_n=x⟩ has A_∞=⟨x⟩≅Z/p. Nevertheless the stated global negative-Hom factorization through N_∞⊗S follows coefficientwise by localizing at every prime and testing N/nN. It gives vanishing for any unital torsion base ring because its modules have bounded integer exponent.',
    'The coherent-root distinction and counterexample are earlier-run corrections. The stronger global factorization through the actual maximal divisible subgroup is not asserted without proof.',
    'agrees','The four entries concern the same proposition’s erroneous description, valid weaker target, and surviving corollary; all hypotheses are preserved.')
add(69,'A87','reading question','A:45:1413-1415',
    'Hom^(−d)(τ_αM_S,N_S) ... Hom^(−d)(τ_αM_S,N_0S)',
    'The supplied transcription distinguishes N_S from N_{0S} on the two sides. An earlier modernisation’s report that they are identical is not confirmed, independently of the genuine infinite-height/divisibility problem.',
    'This is a source-to-source disagreement; no new reading is made.',
    'agrees','The note correctly declines to import a defect that is absent from the frozen transcription.')
add(70,'A89','reading question','A:3,23,26:10,589-595,683-697',
    'ombres des modules; ombres virtuelles; à degrés≥0?',
    'The three named loci provide actual shadow terminology and definitions. The external H05 question’s exact wording is absent, so locating these pages cannot certify that the unspecified question has been answered.',
    'This remains a link lead with the external endpoint unavailable.',
    'agrees','The note observes the correct evidential boundary and supplies the real local anchors.')
add(71,'A91 A99 B60','other','A:36,38,40,42,44,46:1035-1054,1124-1138,1186-1217,1262-1301,1356-1382,1422-1446;B:55,57,59,61,63,71,73,90,92:366-388,480-507,541-559,594-609,688-710,1065-1087,1140-1158,1972-1994,2058-2093',
    'groupe abéloïde; IX; ORDRE DU JOUR',
    'The packet physically contains separate Néron/monodromy/Hodge typescript and administrative donor faces. Their abeloid, Picard and graph vocabulary is not a handwritten application of the new PD cochain construction; the transcription supplies no Fourier/Chern example in these ranges.',
    'Donor mathematical claims are retained in a separately labelled part of the claim map, not omitted or conflated with the new argument.',
    'agrees','The note’s source-layer distinction is confirmed by titles, typography encoding, equation numbers and donor pagination.')
add(72,'A92','unproved claim','A:36:1035-1054;B:90:1988-1994',
    'pour un tore T, on a F(T)=0',
    'In the reused analytic-group source, F(A) is the kernel of the complexification of the exponential lattice into the Lie bundle. For a complex torus (C*)^r this kernel is zero and the corresponding vector objects identify. This T is a torus, not the PD coefficient parameter.',
    'The modern explicit torus description uses the donor definitions; it is not an application of C_DRpd.',
    'agrees','The note correctly treats the assertion as separate donor mathematics requiring its own definitions.')
add(73,'A93','unproved claim','A:38,46:1124-1138,1432-1440;B:90,92:1972-1994,2058-2093',
    'B≃E^ab/(F^ab+R^ab); ... associé à un groupe abéloïde',
    'The donor text characterizes the abeloid quotient by its lattice and Hodge subbundle, assuming the earlier injectivity relation and the appropriate locally constant finite-rank lattice and direct-summand conditions. The quotient expression alone does not imply those hypotheses.',
    'Missing donor assumptions are stated as dependencies, not supplied from the later handwritten construction.',
    'agrees','The note correctly separates the quotient formula from the prerequisites that make it an analytic abeloid group.')
add(74,'A94','other','A:38:1138',
    'a servie de modèle aux conjectures de DELIGNE ... [9,9.8 à9.13]',
    'The donor source itself claims that the analytic mixed-Hodge configuration motivated Deligne’s higher-dimensional Néron conjectures. The cited bibliography and conjectures must be collated in the donor publication; this is not evidence that the handwritten lecture proves them.',
    'The historical motivation is attributed to the source, not independently inferred from a thematic resemblance.',
    'agrees','The note records a real historical assertion while retaining the unresolved bibliography dependency.')
add(75,'A95','reading question','A:38,46:1124,1442-1446',
    'Fil^1E=E, Fil^0E=F, Fil^(−1)E=0; concentrée en degré −1',
    'The retained increasing filtration has nonzero toric jump at +1 when F∩E^t=0, yet the other donor leaf calls it concentrated at −1. This is a cross-page sign/index discrepancy to collate with the donor source and eventually scans.',
    'No contemporary descending convention is imposed as an unmarked correction.',
    'agrees','The note accurately identifies an actual mismatch rather than merely unfamiliar notation.')
add(76,'A96','unproved claim','A:46:1422-1446',
    'la suite exacte (13.4.3) ... commute aux changements de base quelconques',
    'The reused source asserts functoriality and arbitrary analytic base change for the sequence defined by R⊗O_S→Lie′(A). Its non-surjective general form must be separated from the locally free short-exact form under stronger span/local-constancy hypotheses.',
    'Pullback of a kernel requires the donor’s structural argument; it is not a formal consequence of an arbitrary module map.',
    'agrees','The note correctly preserves which sequence is named and the extra hypotheses introduced before (13.4.4).')
add(77,'A97 B61','title, date or page count','A:40,42,44:1199-1207,1272-1301,1356-1376;B:84,86,88:1652-1690,1755-1779,1847-1865',
    '21 Mars1975; 10 juillet1975; 18 au22 novembre1975',
    'Administrative donor leaves bear 1975 dates and the SMF notice has a characteristic-class talk title concerning quadratic modules. They date reused paper and its own meetings/theses, not a precise de Rham lecture day or a Fourier-transform Chern computation.',
    'Only the scan3 annotation directly gives 1976 for the lecture plan.',
    'agrees','The notes correctly decline to convert donor dates and titles into manuscript content.')
add(78,'B1','other','B:48-94:2-2174',
    'Intégration ...; Faisceautisation ...; Condition de De Rham',
    'The planning answers correctly describe representable additive cochains, Stokes comparison, weighted integral PD objects and internal topos constructions. They distinguish multiple universal properties and donor text from the main line. The opening lecture plan, unavailable to that run, is now present in package A.',
    'This is a package-level source summary rather than an additional mathematical theorem.',
    'agrees','Its mathematical distinctions match the passages. Its earlier documentary scope limitation is updated by the present combined corpus.','B1')
add(79,'B4','unproved claim','B:48:6-32',
    'transforme lim→ en lim←; représentables',
    'For the small simplex category Δ and a set/module-valued contravariant functor F on simplicial sets converting all small colimits into limits, density of representables gives F(X)≅Nat(X,[n]↦F(Δ[n])). Module structures on the values make the representing simplicial object a module object. Evaluating a cohomology theory on simplices gives its objectwise resolution condition.',
    'Smallness and chosen universe are explicit modern background; no extra finite-type condition is needed for this presheaf-density argument.',
    'agrees','The note correctly flags precision of representability; the manuscript’s basic claim has a direct presheaf proof.')
add(80,'B5','withdrawn in the same text','B:48:35-79',
    'Mais c’est ... faux déjà pour M=0',
    'A cancelled long-exact-sequence/splitting argument is followed by an explicit rejection at M=0. The numerous illegible words prevent identifying the exact rejected proposition or a fully typed counterexample.',
    'No theorem is invented from a desired conclusion; class F is appropriate for this specific withdrawal target.',
    'agrees','The entry accurately limits the conclusion to visible authorial retraction.')
add(81,'B6','reading question','B:50:130-137;B:52:210-219',
    'M^Hom(Δ_n,Δ_p); Hom_mono(Δ_n,Δ_m)',
    'The right adjoint to degree-p evaluation has value M^{Hom_Δ([p],[n])} in degree n. The doubtful margin on scan50 reverses p,n, while the normalized formula on scan52 uses injections in the expected direction.',
    'Swapping the margin’s indices is a suggested mathematical repair, not a new ink reading.',
    'agrees','The variance complaint is valid, and the independent normalized display supplies internal evidence.')
add(82,'B7','unpursued implication','B:50,52:139-162,200-250',
    'cochaînes non dégénérées; Λ^(n+1)Φ; T∧',
    'Normalized cochains on the standard m-simplex with values M have basis the increasing (n+1)-tuples of vertices and identify with Λ^{n+1}(k^{[m]})⊗M; their differential is wedge with the all-ones vector T. Normalization is defined using degeneracies and commutes with Hom(X,−).',
    'The displayed coefficient-object statement is reconstructed with explicit basis and variance; final faded “sauf erreur” is retained as a qualification.',
    'agrees','The note identifies the actual structural bridge and its reliance on degeneracy maps.')
add(83,'B8 B10 B16','unproved claim','B:54,56,67-68:295-359,396-471,873-923',
    'En fait il suffit; version abstraite; intégrale ... universel',
    'For a simplicial nonnegative cochain object A_n^i=0 for i>n, H^n(A_n)=0 for n≥1 and H^{n−1}(A_n)=0 for n≥2, a Stokes family K_n:A_n^n→M is uniquely determined by K_0. It exists exactly if K_0 annihilates ∂_1ker(d:A_1⁰→A_1¹); hence systems are represented by U=A_0⁰/∂_1ker d. The induction factors through cokernels and extends to an abelian category with the specified commuting differential and boundary.',
    'The clean abelian-category formulation supplies the omitted categorical wording; the core induction is already proved on scans54–56.',
    'agrees','The entries concern the same induction, its minimal hypotheses and its universal target; “proposed abstract version” should not obscure the proof available for groups.')
add(84,'B9','other','B:54,56:336-344,470-471',
    'le système des K_n ne commute pas ... aux op. simpliciales',
    'The degree-specific integration functionals K_n are not a simplicial natural transformation to a constant object. Their Stokes compatibility instead assembles a natural cochain map, and uniqueness makes them compatible with endomorphisms of the entire differential simplicial object.',
    'The two naturality statements have different domains and are not contradictory.',
    'agrees','The entry accurately retains the author’s warning.')
add(85,'B11 B50','reading question','B:58:515-532',
    '(SS)/X≃widehat(Δ/X); Hom(Δ^op,Ens)',
    'A simplicial set X is studied through the slice topos Set^{Δ^op}/X≃Set^{(Δ/X)^op}, whose coefficients are all presheaves on the category of simplices. The final displayed functor category omits /X although the following prose includes it.',
    'The corrected slice identity is a standard categorical reconstruction; the missing symbol is a scan-check entry.',
    'agrees','The note’s substantive coefficient interpretation is supported, and its formula warning is genuine.')
add(86,'B12','reading question','B:60,62:580-585,616-679',
    'cofaisceau; cov.; en remplaçant E par E^op',
    'Contravariant coefficient systems on Δ/X give sums/chain objects by left Kan extension; covariant systems give products/cochains by the dual construction. An arbitrary presheaf has no inverse transport maps, so the initial product formula cannot be used with both conventions without a stated variance conversion.',
    'The cancelled diagrams and question marks document exploration; a coherent modern formulation must choose one convention.',
    'agrees','The note correctly treats variance as mathematically essential rather than a notational preference.')
add(87,'B13 B14 B64','self-flagged step','B:60,64:567-585,719-749',
    'que F soit loc. constant ou non; à vérifier ce point',
    'The claim that Γ(X,C_X^*⊗F) computes RΓ(X,F) for every presheaf F is false in the literal simplicial-slice interpretation. For X=Δ[1]/∂Δ[1], let F=k on vertex-degenerate simplices and0 on edge-degenerate simplices. The tensor complex has no global sections, but an injective copresheaf calculation gives H¹(X,F)=k. For locally constant coefficients the usual comparison survives; coefficient complexes additionally require boundedness/totalization control.',
    'The explicit arbitrary-presheaf counterexample is the earlier run’s construction, rechecked here; it does not refute all restricted coefficient conventions.',
    'agrees','The note accurately records the author’s own warning, the scope increase and a counterexample satisfying the literal arbitrary-presheaf hypotheses.')
add(88,'B15 B17','unpursued implication','B:65-69:759-972',
    'condition de Stokes; u^n(f)=K_n∘f_n; non dégénérées',
    'By the evaluation adjunction, maps A_*^n→C_{*M}^n correspond to K_n:A_n^n→M, and the chain-map equation is K_n∂_{n+1}=K_{n+1}d. Evaluation produces a natural comparison to ordinary cochains, landing in normalized cochains if A_m^n=0 for m<n. It represents a derived comparison, becoming a global quasi-isomorphism only under the requisite section-acyclicity.',
    'This separates construction, normalization and quasi-isomorphism claims.',
    'agrees','The displayed formulas give the asserted additive map; product compatibility is not implied.')
add(89,'B18','self-flagged step','B:69:974-987',
    'dont il faudrait étudier les propriétés ... multiplicatives',
    'For the PD simplex of size t∈J, the Stokes system gives a comparison to normalized S-valued cochains. Its multiplicative and higher-homotopy properties are explicitly left for investigation.',
    'No product-preserving integration theorem is supplied by the preceding additive construction.',
    'agrees','The note correctly records a precise open task.')
add(90,'B19 B20 B21','unproved claim','B:70,72:992-1058,1095-1131',
    'support⊂U; ne servent que pour pouvoir définir; Cartan ... homot fin',
    'For a topological space with a differential-form sheaf resolution Ω of k, a simplex subcomplex S′ locally homology equivalent to singular simplices, compatible pullbacks into an integrable simplicial object define Ω→S′_X. Under local contractibility and appropriate paracompact/fineness hypotheses, the resolution and acyclicity comparisons yield the de Rham isomorphism. A single global homology comparison is insufficient.',
    'The clean sufficient topological hypotheses are modern reconstruction; the faded cube alone does not establish each edge or every topological case.',
    'agrees','The local insertion and final NB separate existence of the map from the hypotheses proving it an isomorphism.')
add(91,'B24 B67 B68','reading question','B:75-76,91:1252-1315,2023-2031',
    'flasque si p≥0; épi si p≠0',
    'The broad p≥0 flasqueness/surjectivity claim conflicts with the complementary-degree-zero exception. DR_*^{0,0}=k_* is not acyclic on every simplicial slice: on S¹ its H¹ is k. Absolute sections on Set^{Δ^op} are evaluation at [0] and exact, so absolute acyclicity cannot justify all slices or arbitrary relative f_*. Tensoring with coefficients from a slice is a further quantifier.',
    'The likely inequality p>0 is a reading alternative; the different meanings of flasque must be fixed before judging the later topos example.',
    'agrees','The notes correctly expose the constant corner and distinguish absolute, slice and relative scopes.')
add(92,'B26','unproved claim','B:77:1377-1406',
    'deleted est stable par; les puiss. div. ... sont nulles',
    'On the kernel image of exterior multiplication by dT inside the larger PD exterior algebra, higher divided powers γ_i(y), i≥2, vanish under the graded PD convention: locally y=(dT)z, and repeated dT factors vanish. This is stronger than stability of the kernel under divided powers.',
    'The precise graded PD convention is necessary, especially for products of odd factors; it is not replaced by ordinary ungraded ring PD axioms.',
    'agrees','The note accurately records the strengthening and the local proof route.')
add(93,'B27','self-flagged step','B:76-77:1337-1437',
    'à la détermination près ... degré complémentaire0; plus les axiomes divers',
    'The data still needed to recover DR from the larger object are products DR^{0,p}×DR^{0,q}→DR^{0,p+q} and divided powers on DR^{0,p}, together with identities ensuring associativity, signs, PD compatibility and differential compatibility. Partial products involving Im(u) are treated first.',
    'A complete axiom system and its existence/naturality are not supplied by these pages.',
    'agrees','The entry’s precise open-task description follows the final display and sentence.')
add(94,'B28 B29','self-flagged step','B:78:1441-1479',
    'Pb trouver des splittings canoniques; projectif; splitting unique',
    'The author asks for canonical splittings of the exterior-kernel sequences for p≥1, asserts projectivity gives some splitting, and singles out p=q=1 where Hom(Φ⊗Ψ,Φ)=0 by evaluation at [0]. The latter proves uniqueness if existence has been established; projectivity must be interpreted in the actual simplicial module category.',
    'The standard affine space/torsor of splittings under Hom explains why existence does not in general select a canonical section. The special Hom calculation does not solve every p,q.',
    'agrees','The note correctly limits the special-case conclusion and preserves the general canonical-splitting problem.')
add(95,'B30','unproved claim','B:80,89:1488-1506,1895-1911',
    'le restent par tensorisation avec tout faisceau; Γ^i(N⊗Φ)⊗M flasque',
    'The test embedding requires flat cokernel and tensor-universal acyclicity of positive divided/exterior powers; a stronger later version quantifies Γ^i(N⊗Φ)⊗M for all modules N,M and i>0. The proposed exterior dévissage then gives acyclicity of Γ^iΦ⊗Λ^jΨ for i>0.',
    '“Flasque” is kept as a hypothesis pending specification of absolute/slice/relative scope; ordinary exactness alone does not prove it.',
    'agrees','The note correctly keeps the tensor quantifiers, which are essential to the argument.')
add(96,'B31 B36 B37','unproved claim','B:80,83,85:1510-1526,1611-1645,1706-1742',
    'résolution de Γ*L; Φ et Ψ ... plats; la donnée ... équivaut',
    'For a flat exact sequence0→L→Φ→Ψ→0 of modules in a ringed topos, the free graded PD/exterior algebra ΓΦ⊗ΛΨ with differential Φ→Ψ resolves ΓL, weightwise. Rank-one/trivialized L is a subsequent specialization yielding k⟨T⟩. Its description by (k,L,Φ,u) and semilinear maps inherits the flatness of Φ and Ψ from the preceding definition.',
    'The omission of repeated flatness in scan85 is interpreted by its explicit backward dependency, not as a theorem for every monomorphism.',
    'agrees','The note correctly preserves the order of hypotheses and separates the algebraic resolution from sheaf acyclicity.')
add(97,'B34','unproved claim','B:81-82:1566-1578',
    'Soit f:X→Y; un certain tronqué du second',
    'The relative comparison f_*K_u→Rf_*(k⟨T⟩) has the same weightwise range q≤w if the pre-endpoint terms are f_*-acyclic. The absolute Γ-acyclicity hypothesis by itself does not supply this for every f.',
    'A precise graded truncation and the required relative acyclicity are modern hypotheses completing the statement; they are not proved by the phrase “corollary.”',
    'agrees','The entry correctly identifies an extra quantifier and missing justification in the passage to direct images.')
add(98,'B35 B38 B40 B41 B42','unproved claim','B:82,87,89,91:1580-1606,1820-1831,1924-1964,2001-2021',
    'Que peut-on dire ... λ,μ?; indépendant du choix; Transitivité évidente',
    'Maps between admissible unit embeddings induce structured maps of the PD algebras and, under the comparison hypotheses, quasi-isomorphisms after sections. Pushouts and further admissible enlargements are proposed to produce choice-independent transitive identifications in a localized category. Equality of parallel maps in that localization and stronger higher coherence must be distinguished from strict chain-level equality.',
    'The common-target argument is a proof sketch with admissibility/equality obligations, not a constructed infinity-functor. The explicit question concerns λ,μ with the same marked section.',
    'agrees','The notes correctly separate the explicit question, the diagrammatic strategy and the strength actually claimed.')
add(99,'B39','unpursued implication','B:89:1895-1911',
    'reste mono par tensorisation; on prend Φ⊗S',
    'If0→k→Φ→Ψ→0 has flat Ψ, then u⊗id_S:S→Φ⊗S remains injective after any further tensoring. If S is flat, its cokernel Ψ⊗S is flat. The strong acyclicity condition is inherited by the stated tensor substitution.',
    'Universal means pure/base-change-stable monomorphism here, not initiality among enlargements.',
    'agrees','The lemma’s proof is precisely this tensor construction, as the note records.')
add(100,'B44','unproved claim','B:91:2033-2050',
    'un quasi-iso universel; En effet',
    'The augmentation k⟨T⟩→K_u is claimed to stay a quasi-isomorphism after ordinary tensor product over k⟨T⟩ with any intended structured A, giving A→K_u⊗_{k⟨T⟩}A. This needs a universal exactness/K-flatness statement at that coefficient algebra, not just k-flat terms.',
    'The sentence beginning “En effet” is unfinished; stronger hypotheses or a derived tensor formulation are possible repairs, not text supplied here.',
    'agrees','The entry correctly identifies the proof obligation named by “universal.”')
add(101,'B45','unproved claim','B:94:2110-2174',
    'spéciale; en rendant inversibles ttes les flèches; ce sont des quasi-isos',
    'A special structure has fixed base k, marked T, cohomology k⟨T⟩ in exterior degree0 and zero in positive exterior degree, and flat terms. Maps preserving these data induce the identity on that cohomology, hence are quasi-isomorphisms; the page then localizes all such arrows.',
    'The missing i>0 in the vanishing is separately flagged. Localization alone proves neither nonemptiness, simple connectedness nor homotopy-type equivalence.',
    'agrees','The notes correctly identify why all structure-preserving maps should be quasi-isomorphisms while limiting the consequences.')
add(102,'B47','reading question','B:94:2139-2147',
    'k{T}≃H^*0; H^*i=0',
    'The vanishing statement must be restricted to i>0 to avoid contradicting the preceding degree-zero cohomology condition. The supplied entry body correctly locates this at scan94; the index’s scan83 is only a contextual comparison.',
    'Adding i>0 is a mathematical reading suggestion, not a transcription change.',
    'agrees','The local conflict is real; the consolidated locator corrects the misleading scan-only index hint.','B47')
add(103,'B48','reading question','B:81,94:1530-1536,2112-2117',
    'unsure{q|0}≤j≤i; degré complémentaire=unsure{j|i}−j',
    'The total/exterior convention requires0≤j≤i and complementary degree i−j. The frozen alternatives in the last definition sheet include incompatible q and j readings; scan81 supplies the internal mathematical comparison.',
    'The alternatives remain undecided pending images.',
    'agrees','The note correctly retains uncertainty and does not substitute expected notation into the source.')
add(104,'B49','reading question','B:89:1913-1919;B:80,83:1510-1526,1621-1627',
    'Γ*(unsure{Ψ|Φ})⊗Λ*Ψ',
    'The first factor is doubtfully read Ψ on scan89, whereas the defining construction uses ΓΦ. The kernel line and differential would be lost by replacing Φ with Ψ without extra data.',
    'Φ is the mathematically suggested alternative, not a decided reading.',
    'agrees','The note identifies a consequential generator ambiguity confirmed by the preceding formulas.')
add(105,'B52','idea of the earlier run','B:81:1530-1554',
    'Algèbre graduée sur ... k{T}',
    'For an abelian group A, the directed system of weight copies with transition multiplication by T has maps a↦(w+1)a, and its colimit is A⊗Q. Thus this proposed stabilization rationalizes and kills torsion; it is not an integral recovery functor.',
    'The transition strategy is the earlier run’s experiment, not a construction prescribed on the page.',
    'agrees','The note’s conditional wording and factorial coefficient calculation are accurate.')
add(106,'B53','idea of the earlier run','B:74,83,94:1193,1613-1619,2110-2132',
    'alterné pour degré ext',
    'An ordinary alternating dg F₂-algebra cannot have cohomology ring H*(BC₂;F₂)=F₂[t], |t|=1, through a product-preserving identification, because every odd cocycle square is already zero. The weighted system is not refuted: its representatives in different weights are different elements.',
    'BC₂ and its normalized bar calculation are earlier-run diagnostic examples, not manuscript examples.',
    'agrees','The hypotheses of the strengthened unweighted interpretation are explicit and the obstruction is valid.')
add(107,'B56','reading question','B:48-52,80-94:6-250,1488-2174',
    'résolution de Z{T}',
    'The later Pursuing Stacks W₂ example concerns a polynomial/binomial discrete-versus-schematic comparison. It does not refute this weighted PD object unless the functors and equivalences are explicitly identified.',
    'The external comparison remains a distinct literature/project link; the note is a warning against conflation.',
    'agrees','No such comparison functor is present in the assigned pages, so the earlier run correctly withholds the transfer.')
add(108,'B58','idea of the earlier run','B:58-64,80-94:515-749,1488-2174',
    'faisceaux ... sur X; condition de De Rham',
    'Constant-coefficient or weighted cohomology comparison does not by itself characterize equivalences detected by finite-dimensional local systems, their monodromy, or a chosen schematization. Any such bridge must specify all three and compare the resulting classes of maps.',
    'This is a logical research constraint in the earlier run, not an authorial theorem or solution of another project’s localizer problem.',
    'agrees','The page’s coefficient language does not contain the missing implication.')
add(109,'B59','other','B:49,51,53:86-107,169-197,257-290',
    'Theorem B; rank of π_i; Whitehead products; Postnikov argument',
    'The reversed English typescript pages4–6 construct a minimal commutative differential algebra by adjoining generators, describe ranks of rational homotopy and Hurewicz, and identify Whitehead products from the quadratic differential. Their source and rational finite-type hypotheses must be collated independently of the handwritten integral proposal.',
    'The donor claims are preserved separately in the map; physical adjacency is not proof that they fill the manuscript’s missing integral minimal-model theorem.',
    'agrees','The note’s attribution/scope caution is supported by the separate language, page numbers and text sequence.')
add(110,'B63','unpursued implication','B:78,80,83,89,94:1453-1475,1494-1526,1630-1645,1895-1911,2142-2152',
    'projectif; plats; universel',
    'Every use of divided powers, tensor product and sections here must keep its actual flatness, projectivity or contraction hypothesis. A later retraction about componentwise divided powers in Pursuing Stacks concerns a different functor and does not automatically prove or refute these concrete complexes.',
    'The audit program is the earlier run’s methodological implication, not a completed comparison.',
    'agrees','The note’s caution matches the distinct hypotheses appearing in the transcription.')
add(111,'B65','idea of the earlier run','B:77,83,94:1377-1437,1613-1645,2125-2132',
    'p.d. ... idéal; d x^(i)=x^(i−1)dx',
    'If an ordinary integral dg algebra with compatible PD operations on every positive-degree cochain computed the ordinary cup ring of CP² multiplicatively, a degree2 cocycle x would give a closed γ₂(x) with [x]²=2[γ₂(x)], contradicting H⁴(CP²;Z)=Z generated by [x]². Weighted copies avoid this imposed unweighted identification.',
    'The CP² obstruction is an earlier-run test, not a manuscript computation or a claim that its actual weighted algebra is impossible.',
    'agrees','The counterexample’s hypotheses are explicitly stronger than the manuscript’s claim and are correctly checked.')

def save():
    (O/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
    with (O/'entries.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
    indexed=[r for r in csv.DictReader((R/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t') if r['package'] in P.values()]
    have=[e['entry_id'] for e in entries]
    missing=[r['entry_id'] for r in indexed if r['entry_id'] not in have]
    dup=sorted({x for x in have if have.count(x)>1})
    report={'items':len(items),'entries':len(entries),'missing':missing,'duplicates':dup}
    (O/'coverage.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
if __name__=='__main__': save()
