"""Human-authored semantic review records; code only serializes and validates them.

No heading, keyword, or cue classifier chooses a verdict. Every entry below was
written after reading the original note and corresponding supplied transcription.
"""
import csv,json
from pathlib import Path
from datetime import datetime,timezone

SHARD=Path(__file__).resolve().parents[1]
ROOT=SHARD.parents[2]
PKG='MPL_36_002-052'
FILE='pro/'+PKG+'_transcription.tex'
items=[]; entries=[]; claims=[]; problems=[]; readings=[]; links=[]; events=[]

def item(n,source,kind,locs,words,statement,reconstruction='',check='agrees',reason='',verdict='kept'):
    ident=f'SA13-{249+n}'
    sources=[f'{PKG}#{x}' for x in source]
    ls=[dict(file=FILE,cote=36,scan=s,start=a,end=b) for s,a,b in locs]
    items.append(dict(id=ident,sources=sources,kind=kind,cote=[36],scans=[f'36:{s:03}' for s,a,b in locs],lines=ls,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,src in enumerate(sources):
        entries.append(dict(entry_id=src,item_id=ident,verdict=verdict if j==0 else 'merged',reason=reason if j==0 else f'Merged with {ident}: '+reason))
    return ident

item(1,[1],'self-flagged step',[(3,10,17)],'Pourquoi $S$ \\unsure{hensélien|Limélien} ?; pourquoi seulement à isogénie près ?',
'The editor asks separately why the base is henselian and why the introductory comparison is only an isogeny for ell different from the residue characteristic. The compared objects are absent from this leaf.',
'No stronger integral theorem is reconstructed; the modern distinction between an integral lattice and its rationalization explains the question only.',reason='The two questions and the explicit ell != p parenthesis are present. The note correctly avoids inferring an integral isomorphism.')
item(2,[2],'self-flagged step',[(3,17,29)],'ni fondé sur des théorèmes',
'An introductory assertion and a remark on higher cohomology are criticized as unsupported; the proposition criticized is not copied.',reason='The editorial judgments are explicit. Neither these remarks nor their punctuation state the omitted cohomological theorem.')
item(3,[3],'self-flagged step',[(3,21,23)],'une référence ou définition pour réduction semi-stable d’une courbe',
'Distinguish a semistable nodal curve from a stable curve with finite automorphism group and identify which reduction theorem or model is intended.',
'The modern distinction is a reconstruction; the leaf asks only for a definition/reference and says reference [3] uses stable terminology.',reason='The note accurately treats this as a reference and definition request, not as a denial of stable reduction.')
item(4,[4],'self-flagged step',[(3,50,56),(4,64,68)],'épimorphisme n’est pas la définition d’isogénie',
'The category of group schemes and the finiteness of an isogeny must be specified; a second editing suggestion replaces separated finite type by quasi-projective in an unseen sentence.',
'For abelian varieties an isogeny is a surjective homomorphism with finite kernel; no blanket implication from epimorphism to isogeny is asserted here.',reason='Both comments occur, but the quasi-projectivity recommendation is local to the criticized draft.')
item(5,[5,89],'self-flagged step',[(4,72,72),(7,260,260),(46,1028,1034)],'As tu vérifié si l’accouplement d’\\unsure{A. M.} coïncide avec le tien ?',
'Compare the actual pairing constructions, including sign and Tate twist, rather than their ranks or perfectness. A later-run proposal tests this first on an elliptic curve.',
'Expanding A. M. as Artin–Mazur remains contextual interpretation. The elliptic-curve normalization experiment belongs to the earlier run, not to the manuscript.',reason='The equality question is explicit and the sign request appears at 36:007. N89 is a proposed way to investigate the same comparison, not a second manuscript result.')
item(6,[6],'self-flagged step',[(4,74,80)],'formellement non ramifié ?; séparablement clos ?',
'Audit the exact infinitesimal and field-closure hypotheses of the missing draft paragraph; no smoothness or étaleness conclusion can be extracted.',reason='The terms are posed as isolated editorial questions. The note correctly refuses to substitute stronger modern assumptions.')
item(7,[7],'unproved claim',[(4,115,115)],'strictement compatible à la filtration par \\unsure{le|les} poids',
'For semiabelian varieties over a field and a homomorphism phi, the torus/abelian filtration is strict up to isogeny; for ell invertible in the field, phi is an isogeny iff its map on rational ell-adic Tate modules is an isomorphism.',
'The field, ell invertibility, geometric Tate modules, and rationalized interpretation of strictness are modern precisions. Integral strictness of all filtered lattices is not automatic.',reason='The page asserts both statements without proof. Its phrase isogeny of Tate modules requires a finite-kernel/finite-cokernel or rational convention.')
item(8,[8],'self-flagged step',[(4,119,120)],'S est-il un trait dans cette remarque ; sait-on assez sur le passage à la limite et Néron ?',
'In draft Remark 2.6(a), audit the reduction to a trait and the compatibility of Néron models with the indicated limit.',reason='Both questions attach to the explicit draft number; the leaf does not supply that remark or establish the limit theorem.')
item(9,[9],'unproved claim',[(5,129,133)],'${}_nK=\\operatorname{Ker}({}_nG\\longrightarrow{}_nH)$',
'If K is the kernel of G -> H in an abelian sheaf category, then K[n] = ker(G[n] -> H[n]). Under finite étale torsion hypotheses the kernel is étale separated; a specialization inclusion and zero-dimensional kernel are proposed but their base/fibre hypotheses are not copied.',
'The kernel identity is formal; the finite étale and specialization conditions must be supplied separately. The eta/s reading remains unresolved.',reason='The identity, proposed subgroup statement, and question on dim ker occur together; the note properly separates their evidentiary strengths.')
item(10,[10],'self-flagged step',[(5,135,139)],'il faudrait au moins choisir un groupe d’inertie',
'To use inertia over a nonhenselian trait one chooses an extension of its valuation/geometric point to a separable closure; the resulting inertia subgroup is determined up to conjugacy.',
'The modern formulation explains the missing choice; the manuscript questions whether draft §§3.5 and 3.7 defined it.',reason='The qualification about choosing inertia is explicit; a canonical subgroup without such a choice is not supported.')
item(11,[11],'unproved claim',[(5,148,152)],'un morphisme de topos $\\operatorname{Spec}(K)_{\\mathrm{et}}\\xrightarrow{\\varphi}\\operatorname{Spec}(k)_{\\mathrm{et}}$',
'A tubular-neighbourhood interpretation of the Néron construction is proposed using a relative scheme on an étale topos with a pulled-back ring object.',
'For a henselian valued field the quotient of absolute Galois groups by inertia yields a morphism of classifying topoi. Which side carries the relative scheme is uncertain in the transcription and is not filled in.',reason='The arrow and ringed-topos proposal are present, but the ambiguous k/K base prevents extraction of a fully specified theorem.')
item(12,[12],'self-flagged step',[(5,154,155)],'l’énoncé primitif était correct',
'An editor contests the contragredient/trace correction; a pencil response is doubtful. The original assertion and final resolution are absent.',reason='The note accurately records a dispute, not a theorem about traces.')
item(13,[13],'self-flagged step',[(5,157,163)],'$\\ell$-groupe signifie-t-il tué par $\\ell$, ou par un $\\ell^{\\unsure{n}}$ ?',
'Specify whether the objects are annihilated by ell or by a power of ell, whether the trait is strictly local, and which cited reference supports the paragraph.',reason='All three requests are present. Neither finite exponent nor strict locality is inferred from the isolated text.')
item(14,[14],'idea of the earlier run',[(6,171,174)],'$f(e)=1$; $f(e)=\\#G$',
'For a finite group of order m, the two functions supported at the identity have normalized counting integrals 1/m and 1, respectively; under ordinary counting measure their integrals are 1 and m.',
'The integrals are the earlier run’s explanatory calculation, not a written computation by Grothendieck.',reason='The two functions occur on the page and exactly explain the normalization ambiguity; the calculation is independently repeated in computations.py.')
item(15,[15],'self-flagged step',[(6,176,176)],'je n’ai pas confiance en dehors du cas strictement local',
'Draft proof 4.7 is challenged for n=2 and outside the strictly local case; the proof itself is absent.',reason='The note keeps the doubt at its actual scope and invents no counterexample.')
item(16,[16],'self-flagged step',[(6,184,189)],'S’agit-il de pro-objets, ou de schémas',
'Specify the category in draft (5.2.3.1); a projective system, its pro-object, and an inverse-limit scheme are different data. The deleted connectedness hypothesis also needs its draft context.',reason='The categorical question and marginal reply je le dis ! are present; the reply is not a resolution visible on this leaf.')
item(17,[17],'withdrawn in the same text',[(6,191,191)],'\\deleted{5.7 est une redite ...} (utilisé en 5.15)',
'A criticism of proposition 5.7 is struck out on the same line, while its use in 5.15 is retained.',reason='The cancelled criticism must not be carried forward as a live claim that 5.7 is false; the theorem itself is not withdrawn.')
item(18,[18],'self-flagged step',[(6,193,199)],'6.6 utilise $\\operatorname{car}(K)=0$, via Tate',
'Differentiate removal of a residue-characteristic restriction in 5.15 from the fraction-field characteristic-zero hypothesis used through Tate in 6.6.',reason='The two characteristics and the marginal answer are explicit. The note correctly refuses to remove both hypotheses together.')
item(19,[19],'self-flagged step',[(6,205,212)],'tu supposes tantôt $A^0$ $\\ell$-divisible ... tantôt non',
'Audit connected/divisible and discrete parts separately in draft pp.57–59; the printed objects and exact maps are not reproduced.',reason='Both inconsistent divisibility and omission of the discrete part are explicitly challenged; these are proof obligations rather than a classification theorem.')
item(20,[20,21],'self-flagged step',[(6,214,216)],'$\\unsure{6.3|63}$ est faux',
'The page denies that a largest ordinary abelian subvariety always lifts through good reduction. It proposes a deformation of an ordinary elliptic curve times a nonordinary elliptic curve to a generically simple abelian surface.',
'A complete counterexample requires an algebraic family with the stated generic simplicity and a precise notion of lift. The earlier run’s contradiction argument is conditional on those existence hypotheses; no p-divisible or formal subgroup is ruled out merely by simplicity.',reason='The proposed counterexample is present but only sketched. N21 formulates missing steps of N20 and is merged without upgrading the sketch to a proved refutation.')
item(22,[22],'conjecture',[(7,227,230)],'Il me semble qu’il doit être possible de définir, à isogénie près',
'Construct finite and toric parts of the expected ranks up to isogeny in the unspecified draft setup.',
'The preceding definitions are absent; this is an expectation with unresolved quantifiers, not a universal splitting theorem for every Néron model.',reason='The tentative wording is explicit. The nearby reply mon argument marche has uncertain attachment and does not furnish the proposed construction.')
item(23,[23],'self-flagged step',[(7,224,227)],'Je n’ai ps confiance en « il est immédiat »; Je n’ai pas lu.',
'Proof 6.4 is disputed; the editor expressly did not read draft pp.61–61bis.',reason='The margin answers that the argument is trivial but supplies no proof. This records the authorial review boundary rather than a missing supplied scan.')
item(24,[24],'reading question',[(7,232,240)],'réf. à Serre pour \\unsure{l’indép.|l’insép.} de $\\ell$',
'Identify the abbreviated Serre result and verify the dependency 6.6 -> 5.13; the uncertain draft page and abbreviation are retained.',
'Independence of ell is a plausible reading and search lead; inseparability is the transcription’s alternative. No unique Serre theorem is identified by the page alone.',reason='The note preserves the primary and alternative reading and correctly does not turn a bibliography request into a theorem.')
item(25,[25],'self-flagged step',[(7,256,262)],'$S$ \\uuline{strictement} hensélien ?; pas d’hyp. d’excellence ?',
'Determine independently whether strict henselianity and excellence are used in draft §9.4 and p.92bis.',reason='The page asks both questions separately; it does not establish necessity of either condition.')
item(26,[26],'self-flagged step',[(7,254,260)],'compatibilité avec $R$ ?; au signe près',
'Check compatibility with the operation R in draft 9.3.3 and the sign in 9.5.8. R and the formulas are absent from this leaf.',reason='Functorial compatibility and sign are distinct obligations. Perfectness cannot resolve an overall sign.')
item(27,[27],'self-flagged step',[(7,267,269)],'Une extension de $K$ (qui ici est infini) est-elle requise ??',
'Audit whether the extension in 10.5.3 can be avoided over the stated infinite field and locate the verifications promised in 10.5.4.',reason='The suggestion is a question about one construction, not an assertion that all extensions of an infinite field are unnecessary.')
item(28,[28],'self-flagged step',[(8,278,278)],'Dire où on trouve que Néron commute à $S\\mapsto\\widehat S$',
'Find a theorem identifying the base change of a Néron model to the completed trait with the Néron model of the completed generic fibre.',
'The familiar theorem is stated for an abelian variety over the fraction field of a DVR, with regularity/separability hypotheses when needed. The leaf itself does not supply these.',reason='The source request is literal and precise enough for a completion/base-change search; no arbitrary smooth model is asserted to commute with completion.')
item(29,[29],'self-flagged step',[(8,280,283)],'prolonger une biextension ... aux ${}_{\\ell^\\infty}A\\times{}_{\\ell^\\infty}A’$',
'Compare the category of extensions of a biextension across a trait with the extension data on ell-primary torsion; specify component and divisibility hypotheses.',
'The line is explicitly a paraphrase of an interlocutor’s claim, introduced by Si j’ai bien compris. It is not itself a proved equivalence.',reason='The note correctly distinguishes torsion-extension data from equality of inverse-limit pairings.')

item(30,[30],'unpursued implication',[(28,289,296),(31,427,432)],'$T=D(M’)$; $T’=D(M)$',
'The diagram arranges a lattice M, a semiabelian-type object G with torus D(M\u2032), and a dual arrangement, later expressed as two-term complexes [M -> G].',
'Calling this a pair of dual 1-motives requires locally free lattices of finite rank, tori, abelian quotients, and compatible biextension data. Headless arrows in scan 28 do not by themselves assert exactness.',reason='The labels and later complexes support the comparison, while the note correctly marks exactness and duality as interpretation.')
item(31,[31],'unproved claim',[(29,314,358)],'$\\underline{\\operatorname{Hom}}(B,G_m)=0$; $\\underline{\\operatorname{Ext}}(M’,G_m)=0$',
'For lattice sheaves M,M\u2032 and a biextension of B,B\u2032 by Gm, the two internal vanishings give the indicated maps into Ext and extensions by the dual tori. Internal Hom vanishing controls uniqueness; internal Ext^1 vanishing controls local lifting.',
'Use the fppf topos, finite locally free constant lattices, and abelian schemes B,B\u2032 for the standard 1-motive case. Global Ext need not vanish when its internal sheaf does.',reason='Both distinct vanishing conditions are written in the margins. The note correctly refuses to replace internal Ext by global Ext.')
item(32,[32],'unproved claim',[(29,360,374)],'les deux splittages ... coïncident',
'A pair of lifts M -> G and M\u2032 -> G\u2032 corresponds to the same rigidification precisely when the induced two trivializations on M x M\u2032 agree.',
'This is the compatibility datum used in a biextension of two-term complexes; the longer cancelled explanation is not reinstated.',reason='The surviving iff criterion is explicit. Its cancelled predecessor is a discarded formulation rather than a denial of the compatibility requirement.')
item(33,[33,34],'self-flagged step',[(31,427,448),(29,370,374),(33,533,541)],'$\\xi\\in\\operatorname{Ext}^1(A\\mathbin{\\overset{L}{\\otimes}}A’,G_m)$',
'A biextension of two complexes [M -> G] and [M\u2032 -> G\u2032] in degrees -1,0 consists of a biextension of G,G\u2032 with compatible trivializations on M x G\u2032 and G x M\u2032. Its isomorphism class corresponds to Ext^1 of their derived tensor by Gm.',
'The precise categorical definition and Ext identification are modern reconstruction checked in Deligne 10.2.1. The manuscript proposes the class, stops its proof, and bears a doubtful pourquoi ?. N34 is the earlier run’s literature comparison to the same construction.',reason='The formula is written but its justification is unfinished. The later published comparison does not retroactively make the manuscript proof complete.')
item(35,[35],'idea of the earlier run',[(31,451,474)],'${}_nA\\overset{\\text{déf}}{=}\\underline{\\operatorname{Ext}}^0(\\mathbb Z/n,A)$',
'For A=[M -> G] in degrees -1,0, M[n]=0, and n:G -> G epimorphic in an abelian sheaf topos, the torsion realization is Vn={(m,g):u(m)=ng}/{(nm\u2032,u(m\u2032))}; it fits 0 -> G[n] -> Vn -> M/nM -> 0.',
'The presentation is the earlier run’s model; a two-term resolution of Z/n identifies it with H^0 RHom(Z/n,A), with the chosen cone sign. The statement is about sheaves and local lifts.',reason='The two written hypotheses are sufficient for the displayed finite exact sequence. The presentation and cone-degree computation are independently checked here.')
item(36,[36],'unproved claim',[(31,476,480)],'passant à la limite sur $n=\\ell^\\nu$',
'The finite torsion sequences give an exact sequence of systems. For geometric realizations of a 1-motive, surjective torsion transitions ensure the exact Tate-module sequence 0 -> T_ell G -> T_ell A -> M tensor Z_ell -> 0.',
'Exactness of inverse limits of arbitrary sheaves or sections needs an additional ML/derived-limit condition; the first term of the second row is uncertain A\u2032|G\u2032.',reason='The passage is asserted without a limit proof. The note correctly separates system exactness from exactness after taking sections and limits.')
item(37,[37],'unproved claim',[(33,529,545)],'\\unsure{qui se recollent}',
'The derived biextension class induces finite torsion pairings and a compatible ell-adic pairing. The local construction must be independent of lifts and compatible on overlaps.',
'Deligne 10.2.5 gives an explicit globally defined formula for 1-motives. The literal diagram Ext^1 -> Hom in this draft lacks a written construction of the boundary map.',reason='Local homomorphisms and gluing are asserted. The note accurately lists the missing independence and descent checks.')
item(38,[38,39,88],'unproved claim',[(33,548,572),(4,115,115)],'Les accouplements induits ... sont ceux qu’on devine.',
'In the torsion realization of dual 1-motives, the torus piece is orthogonal to the opposite semiabelian piece; the matched graded pairings are lattice–Cartier-dual evaluation and the abelian Weil pairing. With finite flat graded pieces and perfect graded dualities, exact Cartier duality yields perfectness of the total pairing.',
'The finite flat setting and exactness of duality are added hypotheses. N39 gives the formal filtered proof; N88 proposes comparison with later arithmetic orthogonality, which requires separate rank/saturation work.',reason='The page asserts orthogonality, expected graded pairings, and the corollary, but does not compute the graded maps. The earlier-run proof organization and bridge are merged as commentary on that exact assertion.')
item(40,[40],'title, date or page count',[(34,578,629),(32,489,521),(30,380,421)],'2. Accouplements définis par une biextension',
'The typed argument reads in the order 36:034 -> 032 -> 030, not archive scan order. Its last visible sentence at 030 is incomplete.',reason='Section and formula continuations verify the reading order. No date or full extent can be inferred from this order.')
item(41,[41,42],'withdrawn in the same text',[(34,603,622),(32,507,521),(30,380,421)],'\\phi^n_\\xi(mx,y)=\\phi^{n’}_\\xi(x,y)',
'For n\u2032=mn and n\u2032P=P, the biextension torsion pairings satisfy phi_n(mx,y)=phi_n\u2032(x,y) for x in P[n\u2032], y in Q[n]; hence phi_n(mx,my)=m phi_n\u2032(x,y). The proof deferral is replaced by a Tor-boundary argument.',
'Membership typos in the literal typed witness must be flagged rather than silently repaired. The displayed symmetric formula needs y in Q[n\u2032], not the printed P. The last proof sentence is incomplete in the retained leaves.',reason='The stronger identity and the replacement of leave to the reader by a proof reference are both explicit. N42 concerns the proof state of the same compatibility, so it is merged.')
item(43,[43],'unpursued implication',[(32,489,503),(50,1142,1144)],'$T_\\ell(M)=({}_{\\ell^\\nu}M)_{\\nu\\geq0}$',
'Here T_ell(M) is expressly a projective system of torsion sheaves. The construction yields a morphism of systems before any inverse-limit group is taken.',reason='The definition and wording système projectif are literal; the note correctly distinguishes this from its inverse limit.')
item(44,[44],'unproved claim',[(36,640,660)],'$H^1(X,\\zeta_\\ell)=P^{(\\ell)}$',
'For a smooth proper geometrically connected curve X over an algebraically closed field and ell invertible, Kummer theory identifies H^1(X,mu_ell) with J[ell](k), H^2(X,mu_ell) with Z/ell, and the principal polarization supplies the Weil pairing on J[ell].',
'Curve, algebraic closure, smoothness, connectedness, topology, and ell invertibility are reconstructed; the word jacobienne suggests this setting but the sheet states none of them.',reason='The note is right that this cannot be a theorem for every proper scheme. The reconstruction matches the coherent curve case only.')
item(45,[45],'reading question',[(36,662,675)],'$\\zeta_p$; $\\mathbb Z/p$; $\\unsure{i_p|\\alpha_p}$',
'In characteristic p, compare separately fppf mu_p cohomology, étale Z/p cohomology, and fppf alpha_p cohomology. For a smooth proper connected curve over an algebraically closed field, Artin–Schreier gives H^1_et(Z/p)=ker(F-1 on H^1(O)) and H^2_et(Z/p)=0; the Frobenius sequence gives H^1(alpha_p)=ker F and H^2(alpha_p)=coker F.',
'Identifying the first and third glyphs with mu_p and alpha_p is a mathematical candidate reading only; the repeated H^2(X,Z/p) and finite-coefficient indices remain frozen.',reason='The note accurately detects that these coefficient objects and topologies cannot be interchanged.')
item(46,[46],'reading question',[(37,690,716)],'$\\operatorname{Ext}_S(B,f_!(G_{mX}))$',
'A local-to-global Ext and Cartier-duality programme is sketched, followed by further themes and an uncertain question about representations. The functor written f_! is not defined.',
'A modern derived-adjunction formulation using Rf_* is a candidate interpretation, not a reading replacement. The final duality question is too uncertain for a precise conjecture.',reason='The exclamation mark is present and distinct from stars elsewhere; the note correctly preserves the undefined operation.')
item(47,[47],'unproved claim',[(39,760,766)],'$H^1(X,A)=\\underset{n}{\\varinjlim}\\ {}_nH^1(X,A)$',
'For a smooth proper scheme X over a field and an abelian variety A, the page uses torsion of H^1_fppf(X,A) before passing from Kummer sequences to a Picard comparison. A regular/smooth-base theorem is intended; normality alone in higher dimension is insufficient.',
'Simple is interpreted as nonsingular in the historical vocabulary; a general base is only suggested in brackets. The precise relative versus absolute version must remain explicit.',reason='The torsion assertion is an input, not a conclusion of the later limit display. The note correctly isolates it for independent checking.')
item(48,[48],'unproved claim',[(39,764,784)],'$\\operatorname{Hom}(\\operatorname{Alb}_X,A)\\simeq\\operatorname{Hom}(A’,\\operatorname{Pic}_X^0)$',
'Over an algebraically closed field, for smooth proper connected pointed X, maps X -> A modulo constant maps are Hom(Alb_X,A), and duality identifies that group with Hom(A^t,Pic^0_X). Kummer gives 0 -> Hom(Alb_X,A)/n -> H^1(X,A[n]) -> H^1(X,A)[n] -> 0.',
'Algebraic closure makes A(k) divisible, so constants disappear after quotient by n; without a point one uses the Albanese torsor. Relative statements require sheafification and universal connectedness.',reason='The substitutions are written but their treatment of constants and base data is omitted. The note correctly identifies those hypotheses rather than simply accepting the displays.')
item(49,[49],'reading question',[(39,786,805)],'$\\operatorname{Hom}(A’,\\underline{\\operatorname{Pic}}_X^0)\\otimes_{\\mathbb Z}\\mathbb Q$',
'The two direct-limit displays contain Q and an undefined lower-dot Tate symbol. Under the standard injective direct system H/nH with transition multiplication by m, the limit is H tensor Q/Z, not H tensor Q.',
'This algebraic diagnosis depends on those transition maps. It does not decide whether the manuscript uses a different convention or whether the quotient /Z was omitted in the ink.',check='understates',reason='The note correctly freezes the symbols, but the explicit finite quotient source strongly motivates Q/Z under usual transitions; the sharper conditional calculation is added to Stage 4.',verdict='corrected')
item(50,[50],'reading question',[(39,775,805),(40,823,830)],'$\\operatorname{Pic}_X^0$; $\\operatorname{Pic}_X^{\\unsure{\\tau|2}}$',
'The argument alternates Pic^0, Pic^tau, and Pic. These differ by component groups; maps from connected abelian schemes land in the identity component, while torsion subgroup maps can detect torsion components.',
'Reduced Pic^0 versus a possibly nonreduced connected Picard scheme also matters in positive characteristic. No uniform replacement of exponents is authorized.',reason='The note identifies a real change of functors and retains the exponent alternatives instead of treating them as typographic variants.')
item(51,[51,52],'self-flagged step',[(40,810,815)],'Cet isomorphisme reste-t-il valable pour $X$ singulier ???',
'The manuscript asks whether its H^1(X,A)–Ext^1(A^t,Pic_X) comparison extends to singular X and speculates about higher Gm vanishing. Smoothness alone does not imply absolute H^2_et(X,Gm)=0: X=Spec R is smooth proper over R and Br(R)=Z/2.',
'The real-field counterexample is the earlier run’s test of the i>=2 absolute reading only; it does not refute a geometrically defined duality over an algebraically closed base, nor the alternative i>2 wording.',reason='The question and uncertain inequality are present. N52 tests one explicitly restricted interpretation of N51 and is merged without claiming to refute the actual unresolved duality.')
item(53,[53,54],'unproved claim',[(40,817,821),(43,888,889)],'$H^1(X,G)\\simeq\\operatorname{Hom}(D(G),\\underline{\\operatorname{Pic}}_X)$',
'A Cartier-duality comparison is asserted for commutative affine G. A verified precise form for finite locally free commutative G, proper flat finitely presented f with f_*O_X=O_S universally, is R^1 f_*f^*G ≅ Hom(G^D,Pic_X/S). Broader affine groups require a specified formal/sheaf dual and possible base terms.',
'For Ga over a characteristic-zero field, field-valued polynomial characters are trivial but the functor of characters on nonreduced algebras is not: exp(epsilon x)=1+epsilon x for epsilon^2=0. Thus the earlier-run test concerns the dual category, not a refutation of sheaf Cartier duality.',reason='The broad affine formula is present but no definition of D or base convention is supplied. N54 is a diagnostic of that same missing definition and is merged.')
item(55,[55],'self-flagged step',[(41,833,839),(41,851,864)],'quand tout est \\uline{affine} sur $S$ (?)',
'The proposed exchange H^1(X/S,Hom(gamma,G)) -> Hom(gamma,H^1(X/S,G)) asks for hypotheses ensuring an edge map is an isomorphism.',
'For a constant finite free gamma=Z^r the comparison follows from finite products; for general gamma, exactness/acyclicity or derived terms must be supplied. Affineness alone is not a general proof.',reason='The isomorphism is explicitly questioned and lower lines retain only a morphism; the note correctly distinguishes them.')
item(56,[56],'self-flagged step',[(41,841,844),(44,945,958)],'Sous quelles conditions ???',
'Determine conditions for H^1 of an internal Ext^1 sheaf to commute with Ext^1 against the relative H^1 functor. General derived-functor spectral sequences carry additional terms and differentials.',
'The manuscript does not specify the site, acyclicity, or convergence assumptions. The most defensible modern formulation is a comparison of total derived functors and its edge maps, not an unconditional isomorphism.',reason='The question and unfinished repetition are literal; the note correctly leaves the required hypotheses open.')
item(57,[57],'withdrawn in the same text',[(42,869,880)],'\\deleted{$f$ morphisme birationnel \\inserted{propre} ...}',
'A cancelled argument attempts to use the locus where a proper birational morphism of integral schemes is invertible and extend a divisor from it. Regularity in codimension one controls that locus; extending Weil divisors as Cartier divisors requires more than integrality.',
'A normal/local-factorial comparison is a modern repair route. The whole local proof, not an independently stated theorem elsewhere, is cancelled.',reason='The note correctly distinguishes a withdrawn proof draft from a live Picard-invariance theorem.')
item(58,[58,59],'self-flagged step',[(43,900,933),(37,690,695),(40,815,815)],'$H^2(X,D(G))\\underset{!}{\\neq}\\operatorname{Ext}^1(G,\\operatorname{Pic}^{(1)})+\\operatorname{Hom}(G,\\operatorname{Pic}^{(2)})$',
'Degree-two cohomology is expressly not asserted to split as the displayed sum. In a precise derived model K=Rf_*Gm, the triangle tau_<=1 K -> K -> tau_>=2 K and the Ext spectral sequence identify possible higher obstructions and extension data.',
'The truncation method is the earlier run’s proposal. Identifying its abutment with H^i(X,D(G)) requires a separate duality theorem and cannot be inferred from formal adjunction alone.',reason='The not-equal sign with exclamation is literal. N59 proposes a framework for this same obstruction and is merged without promoting it to a theorem on the page.')
item(60,[60],'reading question',[(43,900,933)],'$f^!$; $f_!$; $H^{i-1}(X,G’)$',
'The tentative adjunction programme uses shriek and star distinctly and shifts the abelian dual by one degree. All functors and cohomological conventions must be fixed before a derived interpretation is asserted.',reason='The note correctly keeps the shift and distinct operators visible instead of normalizing the draft to current notation.')

item(61,[61],'unproved claim',[(44,940,963)],'Foncteurs adjoints; $\\underline{\\operatorname{Hom}}_S(X,\\gamma)\\unsure{=|-}\\gamma$',
'An unfinished adjunction definition accompanies a possible decomposition of maps X -> gamma into constant maps and maps trivial at a section. If gamma is a commutative group sheaf and a section x exists, evaluation at x splits this decomposition; its pointed factor vanishes only under a separate rigidity hypothesis.',
'The split-map argument is a modern reconstruction. Relative connectedness alone does not force all maps to an arbitrary group sheaf to be constant.',reason='The note correctly marks the definition and formulas as unfinished, and requires a separate rigidity condition.')
item(62,[62],'withdrawn in the same text',[(45,981,1001)],'$H^1(A,\\mathbb W)^{(\\varphi)}$',
'The initial pairing with a stable Witt part is cancelled; the live integral perfect pairing uses Frobenius-fixed classes. A subsequent coefficient-extended formula uses the stable part and W_infinity(k).',
'The standard modern geometric interpretation uses k algebraically closed of characteristic p, continuous Z_p étale H^1 and the slope-zero/Frobenius-fixed Witt realization. The original stable subscript and W_infinity are undefined locally.',reason='The note correctly distinguishes the two coefficient objects and the visible cancellations.')
item(63,[63],'idea of the earlier run',[(45,969,979)],'$H^1(A,\\mathbb Z/p)\\simeq H^1(A,\\underline O_A)^{(\\varphi)}$',
'Artin–Schreier gives 0 -> H^0(A,O)/(F-1) -> H^1_et(A,Z/p) -> ker(F-1 on H^1(A,O)) -> 0. The first term vanishes over an algebraically closed field for a proper geometrically connected A, but survives over F_p and splits off via the origin.',
'This explicit missing-term diagnostic is the earlier run’s calculation, rechecked here; it tests an absolute-cohomology reading without refuting the geometric formulation.',reason='The displayed isomorphism lacks a base hypothesis on the sheet; the counterexample isolates exactly that omission.')
item(64,[64],'unproved claim',[(45,976,1001)],'$\\operatorname{Hom}_{\\mathrm{cont}}(T_p(A),W_\\infty(k))\\simeq H^1(A,\\mathbb W)_s$',
'Artin–Schreier–Witt identifies finite p^n étale classes with Frobenius-fixed Witt cohomology under geometric hypotheses. A limit comparison needs continuous Hom, a specified Witt inverse system, and control of derived limits/invariants.',
'The page supplies none of those transition conventions; modern slope-zero results validate a precise realization, not every possible meaning of the undefined W_infinity and stable subscript.',reason='The note accurately separates finite-level exactness from the further integral limit and freeness assertions.')
item(65,[65],'unproved claim',[(45,993,997),(46,1006,1015)],'un revêtement non ramifié d’une variété abélienne est une variété abélienne',
'Over an algebraically closed field, a connected finite étale cover of an abelian variety, pointed over zero, has a unique abelian-variety structure making the cover an étale isogeny. The geometric pro-ell fundamental group equals the geometric Tate module, including its étale part at p.',
'Finite, connected, étale, geometric, and pointed are reconstruction hypotheses. Arbitrary coverings or arithmetic pi_1 do not satisfy the bare wording.',reason='The note correctly restores the necessary cover and base conventions instead of treating every cover as an abelian variety.')
item(66,[66],'reading question',[(46,1024,1026)],'Si on admet que \\uline{$A$ n’a pas de torsion}',
'The literal torsion-free claim about the abelian variety A conflicts with its nonzero prime-to-p torsion when dim A>0. The preceding Picard discussion suggests that a Néron–Severi quotient may have been intended.',
'The candidate NS(A) has torsion-free group over an algebraically closed field; this is evidence for a scan check only. A is not replaced in the text.',reason='The note correctly leaves the letter frozen and flags the mathematical contradiction of the literal broad reading.')
item(67,[67],'unproved claim',[(46,1017,1034)],'$A^{(\\ell^k)}\\times A^{*(\\ell^k)}\\longrightarrow U^{(\\ell^k)}$',
'For an abelian variety A over an algebraically closed field and ell != char(k), the Poincaré biextension gives a perfect Weil pairing A[ell^r] x A^t[ell^r] -> mu_ell^r, compatible with multiplication, and hence a perfect Tate-module pairing into Z_ell(1).',
'The identification T_ell(A)/ell^r=A[ell^r](k) uses surjective torsion transitions; the claim is not true for arbitrary torsion sheaves without such hypotheses.',reason='The finite and Tate pairings are both written, but their identification and hypotheses are not proved on the leaf.')
item(68,[68,69,70],'unproved claim',[(48,1043,1085)],'Je dis que le foncteur ... est une équiv. de catégories.',
'For an exact sequence 0 -> P\u2032 -> P -> P\u2032\u2032 -> 0 of abelian sheaves, nQ=Q and P[n] -> P\u2032\u2032 epimorphic, the draft classifies biextensions by a restriction to P\u2032 x Q and a compatible pairing P[n] x Q[n] -> G. Its long proposed proof is cancelled.',
'The missing morphism clause is reconstructed as preservation of the pairing. The assumptions imply nP\u2032\u2032=0 and P\u2032\u2032 tensor Q=0; this one vanishing is independently proved, but does not by itself prove essential surjectivity or the entire categorical equivalence.',reason='The live equivalence assertion survives the cancellation. N69 verifies a substep; N70 records the cancelled route. They concern one assertion and are merged with their distinct proof statuses retained.')
item(71,[71],'unproved claim',[(48,1087,1089),(50,1137,1144)],'$\\varinjlim{}_nP\\longrightarrow P’’$ surjectif',
'For Pi-primary torsion surjecting onto P\u2032\u2032 and pQ=Q for each p in Pi, reconstruct a biextension from its restriction and compatible finite-level torsion pairings. The corollary spans scans 048 and 050 across the unrelated typescript 049.',
'The finite-level formulation is retained because the later marginal warning restricts descriptions in projective systems or modules.',reason='The continuation and assumptions are explicit; the note correctly retains compatibility among levels and the interruption by a reused verso.')
item(72,[72],'unproved claim',[(50,1146,1181)],'$pP=P$, $pQ’=Q’$ (ou le symétrique)',
'For two short exact sequences of abelian sheaves, the Pi-primary quotients lift from torsion and the displayed asymmetric divisibilities permit two successive applications of the one-variable reconstruction. The resulting data comprise the restricted biextension and compatible finite-level pairings extending it.',
'A module-level restatement needs the stronger marginal divisibilities; these are not silently folded into the live proof.',reason='The proof visibly applies the first corollary to P,Q\u2032 and then to P,Q. The note accurately tracks the asymmetric rather than universal divisibility assumptions.')
item(73,[73,74],'self-flagged step',[(50,1142,1144),(50,1163,1165)],'Sinon, garder les ${}_nP\\times{}_nQ\\longrightarrow{}_nG$',
'The author requires retention of finite-level pairings when divisibility is insufficient for the module description. For P=Z/ell and Q=G=Q_ell/Z_ell, T_ell(P)=0 but Biext^1(P,Q;G)=Hom(Z/ell,G) is nonzero; compatible finite pairings therefore can disappear in inverse limits.',
'The example is the earlier run’s ordinary-abelian-group model, independently recomputed. It does not identify a strict projective diagram with its pro-category image, nor prove the general reconstruction theorem.',reason='The warning is explicit. N74 supplies an exact model of the lost information and is merged; doubtful marginal equalities still go to Stage 4.')
item(75,[75,76],'unpursued implication',[(52,1232,1243)],'$\\underline{\\operatorname{Hom}}_{gr}(A,G)=0$; $\\underline{\\operatorname{Hom}}_{pt}(A,G)=0$',
'Group-Hom vanishing is weaker than universal vanishing of arbitrary pointed maps. The first condition gives Ext^1(A,G) ≅ H^0(S,Ext^1_sheaf(A,G)) by the low-degree local-to-global Ext sequence; the second is required for forgetting extension laws.',
'The note’s ungraded Ext sheaf is interpreted as degree one. The edge-map proof supplied by N76 is the earlier run’s argument, rechecked with vanishing of both outer cohomology terms.',reason='The manuscript explicitly says maps need not be additive in part b. The two hypotheses must not be identified.')
item(77,[77],'idea of the earlier run',[(52,1241,1248)],'$H^1(A,G_A)\\simeq H^1(S,G)\\times H^0(S,R^1f_*G_A)$',
'If f:A -> S has the zero section e and f_*G_A=G, the Leray five-term sequence has zero transgression because e^*f^*=1 in degree two. Hence H^1(A,G_A) splits into H^1(S,G) and the kernel of e^*, identified with H^0(S,R^1f_*G_A).',
'This is the earlier run’s proof. Identifying rigidifiable torsor classes with uniquely rigidified torsors additionally uses universal pointed-map rigidity.',reason='The product decomposition is written; the added Leray argument proves exactly that statement under the displayed hypotheses and keeps uniqueness separate.')
item(78,[78,79],'unproved claim',[(52,1251,1261)],'pl. fid. (de catégories discrètes)',
'Under universal pointed-map vanishing Hom_pt(A,G)=0, the forgetful functor from commutative extensions of A by G to rigidified G-torsors is fully faithful. Its essential image consists of primitive torsor classes m^*L ≅ pr_1^*L tensor pr_2^*L.',
'The coherence proof is an earlier-run construction: universal rigidity extends to A^r; differences between normalized associativity, unit, commutativity, and inverse diagrams are pointed maps into G and hence vanish. Full faithfulness includes absence of nontrivial automorphisms.',reason='The page asserts the categorical result, not only an injection on isomorphism classes. N79 provides a proof route for the same essential-image claim and is merged.')
item(80,[80],'unpursued implication',[(52,1263,1270)],'$0\\longrightarrow\\underline{\\operatorname{Ext}}^1(A,G)\\longrightarrow R^1f_*G_A$',
'The defect L -> m^*L tensor pr_1^*L^{-1} tensor pr_2^*L^{-1} has primitive extensions as kernel and yields an injection from the quotient called NS(A) into symmetric birigidified torsors.',
'NS is interpreted here as the quotient by primitive classes; identifying it with a classical Néron–Severi sheaf requires the geometric setting and is not automatic.',reason='The exact-sequence shape and quotient diagram are present. The next package supplies the diagonal/doubling continuation but is not silently used to repair this leaf.')
item(81,[81],'reading question',[(52,1268,1270)],'$\\underline{\\operatorname{Tors}}\\ \\underline{\\mathrm{birig}}\\ \\underline{\\mathrm{sym}}(\\unsure{B|A},A;G)$',
'The second argument pair in the quotient diagram is read B|A although the upper row is (A,A), and the vertical mark is wr|i. Type consistency suggests A and an identification, but only a scan review can decide.',reason='The note correctly resists replacing the doubtful primary B merely because the continuation concerns the diagonal.')
item(82,[82],'unproved claim',[(38,732,745)],'$u^p(xy)=\\sum_{r+s=p}\\binom{p}{r}u^r(x)u^s(y)$',
'For an algebra E over a characteristic-zero field and a nilpotent derivation u, the finite exponential exp(u) is an algebra automorphism; multiplicativity follows by the higher Leibniz rule and factorial cancellation, and exp(-u) is its inverse.',
'Characteristic zero (or sufficient factorial invertibility together with a compatible truncation) is essential. The reused printed leaf omits the earlier coefficient assumptions; authorship is not assigned to Grothendieck.',reason='The calculation is actually proved on the page; the earlier note’s kind unproved claim overstates the omission. Corrected to a proved conditional computation with an unprovided ambient hypothesis.',check='overstates',verdict='corrected')
item(83,[83],'unproved claim',[(38,747,755)],'l’image d’une sous-algèbre de Levi ... est une sous-algèbre de Levi',
'For finite-dimensional Lie algebras over a characteristic-zero field, exp(ad x) with x in the nilradical preserves every ideal; under a surjective homomorphism, the image of a Levi subalgebra is a Levi subalgebra of the quotient.',
'Finite dimension and characteristic zero are reconstructed standard hypotheses. This is a claim of the reused Lie-algebra source, whose precise edition is not identified.',reason='Both assertions are present. Ideal preservation follows directly from the exponential; the quotient assertion also uses the radical/semisimple decomposition.')
item(84,[84],'withdrawn in the same text',[(51,1187,1226)],'exact à \\deleted{droite} gauche',
'The Čech H^0 presheaf functor is corrected from right exact to left exact before its right derived functors are introduced. Their value on X is the direct limit over covering sieves of the cohomology over those sieves.',reason='The side of exactness and the evaluation formulas are visibly corrected. The deleted formulation is not retained as a second claim.')
item(85,[85],'unpursued implication',[(49,1102,1132),(51,1187,1200)],'Le foncteur $\\mathcal H^0$ transforme les faisceaux injectifs en préfaisceaux injectifs.',
'On a site, exact sheafification is left adjoint to the inclusion of abelian sheaves into presheaves, so the inclusion preserves injectives; positive-degree cohomology presheaves sheafify to zero. The composite yields the displayed local-to-global spectral sequence on a slice.',
'The statements hold for A-modules with the standard site conventions. The source is a reused SGA-style typescript; edition and author are not inferred from proximity.',reason='The first two claims are proved by adjunction on the page, while the spectral sequence is stated. The note’s direct Stacks comparison is exact.')
item(86,[86],'reading question',[(49,1094,1096)],'[T.F Chap. II, § 5, Th. 10.2]',
'Identify the cited sheaf-theory text and its convention on the empty covering. The leaf says its presheaf Čech notion agrees with the cited one when P(empty)=0 and that constant presheaves show the difference.',
'Godement’s Théorie des faisceaux is a bibliographic candidate; the precise theorem and edition need checking, so the abbreviation is not expanded as fact.',reason='The note properly retains a convention-sensitive bibliographic question rather than declaring all Čech constructions identical.')
item(87,[87],'title, date or page count',[(38,729,730),(49,1093,1093),(51,1185,1185)],'-- 98 --; n° 316; 15; 13',
'The reused printed sources have independent visible page numbers. These establish textual sequences and paper reuse, not authorship, drafting dates, or the date of the surrounding handwritten material.',reason='The numbers are visible and distinct from scan and pencil pagination; the negative provenance conclusion is justified.')
item(90,[90],'title, date or page count',[(3,6,6),(35,633,634),(47,1038,1040),(52,1230,1230)],'Remarques. SGA 7 IX; Picard et dualité; biextensions de faisceaux de groupes',
'The selection contains editorial SGA7 IX remarks, a Picard-duality folder cover, a biextension cover, and a rigidity heading. It has 31 retained scans and no explicit total-page statement on a cover.',reason='The titles and counted scan markers confirm that monodromy alone is an incomplete subject description; scan count is not a manuscript claim about total extent.')
item(91,[91],'other',[(8,273,285),(28,287,298)],'The Pro sequence jumps from scan 008 to 028.',
'The earlier Pro run lacked scans 010–027 and therefore could not check the Hua Griffiths lead. In this consolidation those scans are supplied as A36-01 and A36-02, so that limitation no longer blocks text comparison.',
'This is a change in available evidence, not a correction to what the earlier run saw. The truth or novelty of the old Hua claim is not inherited.',check='understates',reason='The Pro sequence really skips those pages, but the present archive also supplies their Codex transcriptions. Corrected current scope; the omitted-scan lead must now be checked there.',verdict='corrected')
item(92,[92],'other',[(31,441,445),(43,920,933),(52,1263,1270)],'Ext, higher Picard terms, and the rigidity sequence',
'The notes compare these constructions with external project registers, standing inventories, and 34 reported context entries. No supplied manuscript identity gives the arithmetic section-map image or fibres, a class-two residue-complex theorem, or the war-game height/Lefschetz results.',
'The external run names and statuses are earlier-run reports only. They are separated into project leads and do not enter the manuscript claim map as new theorems.',reason='The cited pages really concern biextension/Picard objects. Shared obstruction vocabulary does not establish the cross-project claims; the appended inventories were read as part of this indexed entry.')
item(93,[93],'other',[], 'Earlier run: Limits of the SGA collation.',
'The final indexed entry records the previous run’s bibliography/access limits and transcription integrity audit, not an additional mathematical claim. This run performs its own source searches; earlier verification claims are not inherited.',
'The supplied originals have no second-pass changes for this package. Hash and count assertions about an unavailable earlier 93-image bundle are provenance reports, not independently re-certified facts.',reason='The entry is a methodological and integrity report without a new manuscript passage. It is kept as provenance, with verification restricted to material available in this run.')

def claim(n, item_numbers, statement, status, klass, fate, refs, search,
          computation='No numerical computation is required; see the proof analysis in review.md.',
          confidence='high', words=None, locs=None, authorship='Grothendieck manuscript; attribution not inferred for reused printed leaves'):
    chosen=[next(i for i in items if i['id']==f'SA13-{249+j}') for j in item_numbers]
    places=locs if locs is not None else [p for i in chosen for p in i['lines']]
    # Stable de-duplication, not semantic classification.
    places=list({json.dumps(p,sort_keys=True):p for p in places}.values())
    ident=f'C-SA13-{n}'
    claims.append(dict(id=ident,items=[i['id'] for i in chosen],cote=sorted({p['cote'] for p in places}),
        scans=list(dict.fromkeys(f"{p['cote']}:{p['scan']:03}" for p in places)),lines=places,
        his_statement=words if words is not None else ' / '.join(i['his_words'] for i in chosen),
        statement=statement,status_on_pages=status,computation=computation,**{'class':klass},
        fate=fate,fate_date={'review':'2026-11-19','dating':'Publication and circulation dates are stated in fate and the referenced bibliography; undated manuscripts are not assigned a date.'},
        present_status='As of 2026-11-19: '+fate,refs=refs,confidence=confidence,search_ids=search,authorship=authorship))
    return ident

exec((SHARD/'code/claims_core.py').read_text(),globals())
exec((SHARD/'code/a36_records.py').read_text(),globals())
exec((SHARD/'code/problem_records.py').read_text(),globals())
exec((SHARD/'code/reading_records.py').read_text(),globals())

def save():
    for name,data in [('items',items),('claims',claims),('problems',problems)]:
        (SHARD/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (SHARD/'entries.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
    with (SHARD/'readings.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['cote','scan','line','reading','alternative','evidence','weight','confidence'],delimiter='\t');w.writeheader();w.writerows(readings)
    print(f'{len(entries)} entries; {len(items)} items; {len(claims)} claims; {len(problems)} problems serialized.')

if __name__=='__main__': save()
