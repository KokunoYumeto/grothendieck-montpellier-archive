"""Hand-authored problem, reading, and cross-reference adjudications for Codex leaves.
The claim references below are chosen after reading the entire three files.
"""
import root_build as b
from pathlib import Path
import json
C={int(x['id'].split('C')[1]):x for x in b.claims}
C[953]['fate_date']['Mathew_publication']='2023, Tunisian Journal of Mathematics5,369–403'
C[953]['his_statement']='The corollary at375:825–830 states Ext^i(Ga^perf,Ga^perf)=0 for i>1. Only afterward, line836 explicitly changes the working category to sheaves of Fp-modules.'
C[953]['statement']='The leaf’s perfect-site corollary at375:825–830 states vanishing only for i>1, before the explicit switch to Fp-module sheaves at836. A precise stronger modern Fp-linear statement is: for a perfect Fp-algebra R, on the big perfect étale site, Ext^i_Fp(Ga,Ga)=0 for i>0 and End(Ga)=R[F,F^−1], with Fa=a^pF. The analogous abelian-sheaf formulation has different degree-one behavior; the source’s i>1 must not be silently replaced by i>0 without the category qualification.'
C[953]['status_on_pages']='stated as a corollary for i>1; coefficient category is changed explicitly later at line836'
C[953]['present_status']='As of November2026: the precise perfect-site Fp-linear theorem is established by the cited Breen/Mathew sources. It strengthens the written degree range only after fixing the coefficient category. The manuscript corollary and the subsequent Fp-linear working category are distinguished.'
b.events.append(['SA08-C953',b.DATE,b.WHO,'targeted proof check','Re-read375:823–842 after the literal quotation audit. The corollary says i>1; line836 explicitly switches to Fp-module sheaves. Mathew’s positive-degree Fp-linear theorem is recorded as a precisely qualified modern strengthening, not a verbatim replacement.'])
C[901]['computation']=C[901]['computation'].replace('§3','§16')
C[903]['fate']+=' The flat-coalgebra case is checked independently in work/late/proofs.md §11: SGA4III XVII5.5.2.5 identifies Γ^n(A) with symmetric tensors for flat A; iterated comultiplication and universal PD evaluation give the required operations. This does not remove flatness or settle uniqueness for arbitrary added PD-comultiplications.'
C[903]['refs']+=['SGA4III']
C[903]['present_status']='As of November 2026: the flat cocommutative-coalgebra construction is proved in this run; arbitrary nonflat enrichment and its precise axiom system remain separate.'
# Exact Dold source collated after the first snapshot.
C[926]['statement']='Dold1961 Theorem1.6 concerns natural transformations in an ordered n-tuple of independently varying FD complexes. This natural-Hom complex is acyclic over Z. Sections1.7–1.12 choose a separate positive Z[pi]-free resolution W and construct W→Hom; they do not assert Hom is free. Specializing all inputs afterward gives equivariant operations. If the manuscript instead means all transformations natural only in one diagonal variable X, the claimed H0=Z is false: for n=2 the four natural coordinate maps X²→X² remain linearly independent on a two-point discrete X, where no chain homotopies are possible.'
C[926]['status_on_pages']='corrected by himself from fixed X to X variable, but false as a diagonal-only natural-Hom/free-resolution assertion; further hypotheses are needed'
C[926]['computation']='Direct counterexample and primary proof-scope audit: codex_proof_checks.md §17; root_diagonal_ops.json gives four independent degree-zero outputs on a constant two-point simplicial set. Dold1961 printedpp259–262 Theorem1.6 and construction1.11–1.12 collated. Freeness belongs to the separately chosen W.'
C[926]['fate']='Known before these leaves in the exact multivariable form: Dold1961 Theorem1.6, §§1.7–1.12 and §2. The manuscript’s insertion alone does not establish that precise theorem. Search: root_web_034–035; original PDF downloaded and pp258–263 OCR-read. The original introduction dates the announcement to Lille, June1959, and records receipt1March1960; publicationMarch1961.'
C[926]['fate_date']={'announcement':'June1959, Lille, as stated in the original introduction','received':'1960-03-01','publication':'March1961'}
C[926]['refs']=['DoldSteenrod1961','DoldPuppe1961']
C[926]['present_status']='As of November2026: the precise multivariable theorem is established; the diagonal-only/free-Hom reading is refuted by the explicit discrete-space test.'
C[927]['refs']+=['DoldSteenrod1961']
C[927]['fate']+=' Exact original comparison: Dold1961 §§1.7–1.12 constructs the equivariant map from a separately chosen free resolution, and §2 specializes to equal inputs. No claim of a free natural-Hom module is needed.'
b.events.append(['SA08-C926',b.DATE,b.WHO,'refuted, with refined statement SA08-C926.statement','The variable-X correction is insufficient under diagonal-only naturality; four independent natural maps survive evaluation on a two-point discrete set. Exact multivariable replacement and separate W verified in Dold1961.'])
# Targeted independent peer review by SA08/late, before problem inheritance.
C[908]['statement']='Normalized Lambda^r(Psi) has one rank-one term in degree r for r>=0. For r>=1, normalized Lambda^r(Phi) has rank-one terms in degrees r-1 and r. At r=0 both exterior powers are constant k, normalized only in degree0. Unnormalized Lambda^(m+1)k^(m+2) has rankm+2. The case conditions at341:678 need normalization and consistent indexing.'
C[908]['computation']+=' Independent SA08/late review corrected the r=0 boundary; see codex_proof_checks.md §3 and work/late/root_peer_review.md.'
C[919]['computation']='codex_proof_checks.md §6: for the simplex or a locally split rank-one sequence, use Phi=kT direct sum Psi locally, split each exterior power into two summands, and identify the differential. This direct proof covers the explicitly locally split scope; it does not infer that every flat quotient makes the sequence locally split.'
C[920]['statement']='Assume the two short exact sequences in the scan352 diagram, including tensor exactness. Let e be0→Z^i tensor Z^j→C^i tensor Z^j→Z^(i+1) tensor Z^j→0 and eprime be0→Z^(i+j)→C^(i+j)→Z^(i+j+1)→0. For prescribed cycle and quotient products a,c, a middle lift exists exactly when a_*e−c^*eprime=0 in Ext^1(Z^(i+1) tensor Z^j,Z^(i+j)). If so, the lifts form a torsor under Hom(Z^(i+1) tensor Z^j,Z^(i+j)). Associativity, graded symmetry and naturality remain additional constraints.'
C[920]['computation']='codex_proof_checks.md §6: compare the pushout of the source extension along a and the pullback of the target extension along c. Equality is equivalent to a middle map with the two prescribed endpoints; differences factor through the displayed Hom group. Independent SA08/late review corrected the earlier cycle-valued-lift simplification. No value of this extension difference for the full universal model is invented.'
for sid,outcome in [
 ('SA08-C908','Independent review of the exterior normalization proof corrected the r=0 case; r>=1 statement and distinction from unnormalized rank checked.'),
 ('SA08-C919','Read scan350:402–439 and the direct-sum proof. Verified exactness for the simplex/locally split rank-one sequence with the retained flat quotient; the argument is not claimed to show arbitrary flat extensions locally split.'),
 ('SA08-C920','Read the full scan352 two-extension diagram. Re-derived the obstruction as a_*e−c^*eprime and the Hom torsor of lifts, retaining both endpoint products. This corrects the omitted pullback term.'),
 ('SA08-C926','Read scan360:875–890 and original Dold1961pp259–263. Independently verified four coordinate/AW maps give independent H0 classes under diagonal-only naturality; Dold uses separate variables and a separate free W.')]:
 b.events.append([sid,b.DATE,'GPT-6 Astra Pro; effort not exposed by runtime; SA08/late','targeted proof check',outcome+' Evidence: work/late/root_peer_review.md.'])
# Problem selection records actual question marks, cancelled proposals, hopes or unfinished steps.
rows=[
(90,'Euler class and the factor of two',[901],'Worth resolving in the scan edition: identifying the represented circle fixes a normalization affecting the entire geometric example.'),
(91,'Coherent divided-power enrichment of convolution',[903],'Worth isolating: the flat case is established here, while the exact nonflat axiom system still controls the scope of the proposed reconstruction.'),
(92,'Integral replacement for the cancelled symmetric-power argument',[904],'Worth a short historical check: universal polynomial laws explain the repair, without treating the crossed-out rational argument as an integral proof.'),
(93,'From binomial rank identities to natural decompositions',[907],'Worth testing on low simplicial degrees: ranks alone leave naturality and extension classes completely undetermined.'),
(94,'Normalized elementary objects and their indices',[908],'Worth an editorial verification: the normalized and unnormalized modules have different ranks, so the brackets and shifts matter.'),
(95,'Reconstruction from cochain tests and double duals',[909,910,911,912],'Worth formulating with a precise test category and finiteness or continuity condition; the unrestricted versions have explicit counterexamples.'),
(96,'Interchanging realization limits with Hom',[913],'Worth a compactness audit of the exact source objects; arbitrary Hom does not commute with these filtered colimits.'),
(97,'The torsor realization and its homotopy type',[914,915],'Worth a small dedicated run only after the realization category and comparison map are fixed; the circle example does not settle the general question.'),
(98,'Do the differential operators admit a normal basis?',[916],'Worth a bounded algebraic investigation: the checked relations prove a rewriting strategy but not independence of ordered monomials.'),
(99,'Splitting the divided-power simplex sequence integrally',[917],'Worth examining the actual extension class: the displayed lift composes to multiplication by the weight, which is not invertible in general.'),
(100,'Extending the half differential algebra product',[918,919,920],'Worth separating existence from indeterminacy and coherence: the first Ext obstruction is already visible before associativity is imposed.'),
(101,'Coherence among all natural cochain operations',[926,927],'Worth comparing exact operation complexes with established E∞ constructions; a single arity resolution does not supply all composition data.'),
(102,'The unfinished sign in the power-operation formula',[928],'Worth checking on the scan before any mathematical extension; a blank exponent is not a specified operation.'),
(103,'Extending nonlinear functors from one-degree objects',[929,930],'Worth restating through projective simplicial resolutions; the derived décalage theorem is established but does not authorize an arbitrary complex-level formula.'),
(104,'The questioned low Adem relation',[935],'Resolved mathematically by a degree-one test; only the ink and intended composition convention remain to check.'),
(105,'Stable symmetric-power weights',[939],'Worth recovering the omitted stability and positive-weight qualifications from the cited source before proposing a new theorem.'),
(106,'The two Bocksteins and conjugate generators',[945],'Worth a convention table tied to the actual coproduct; changing generators without changing left/right actions creates false relations.'),
(107,'Cartan symmetry and its stable range',[946],'Worth locating the exact range and coefficient hypotheses; the unqualified unstable statement is false.'),
(108,'The connectivity bound and the meaning of smash',[948],'Worth a typing audit first: the ordinary space-smash interpretation has an explicit counterexample below the proposed bound.'),
(109,'Coefficient extension before defining sheaf operations',[949],'Worth recording the needed finiteness hypothesis; the countably discrete counterexample blocks unrestricted tensor/product interchange.'),
(110,'Frobenius semilinearity in every power operation',[950],'Worth fixing conventions at the start of the construction: standard positive powers are semilinear as well as P0.'),
(111,'Frobenius torsion of higher additive-group Ext',[951,952],'Resolved in the precise Fp-linear big-site setting by Breen; useful work now would compare the manuscript route with that proof, not announce the theorem again.'),
(112,'Vanishing after passage to the perfect site',[953],'Resolved in the stated perfect étale setting; its value here is clarifying coefficient categories and the effect of inverting Frobenius.'),
(113,'Vanishing of the induction edge map',[954],'Worth a bounded comparison with Breen’s spectral sequence: the global Ext answer does not prove the specific handwritten edge map vanishes.'),
(114,'Extending the P0 calculation to higher powers',[955],'Worth checking the exact chain-level compatibility: the written proof covers only index zero.'),
(115,'The exponent in the final Ext formula',[956],'Resolved against the printed primary formula, subject to an ink check of the missing plus one.'),
(116,'The unfinished bar/Koszul computation and products',[957],'Worth identifying the exact product assertion before work begins: Breen’s group calculation and his conjectural Yoneda algebra are distinct.'),
(117,'Preserving PD ideals under a functor',[905],'Worth an explicit axiom audit: Hom preserves injections, whereas a general additive functor need not.'),
]
for n,title,ids,worth in rows:
 cs=[C[i] for i in ids]
 occ=[{'claim':c['id'],'cote':136,'scans':c['scans'],'lines':c['lines']} for c in cs]
 b.problems.append(dict(id=f'MP-SA08-{n:02}',title=title,occurrences=occ,as_he_states=' | '.join(c['his_statement'] for c in cs),plausible_today=' | '.join(c['statement'] for c in cs),state_of_art=' | '.join(c['fate'] for c in cs),why_open='The supplied leaves record the step or doubt. No opened source identifies a personal reason for abandoning this particular step. Where the result was later established, the exact scope and date are stated above; this is not a claim that it remains open today.',worth=worth,refs=list(dict.fromkeys(r for c in cs for r in c['refs']))))
 b.events.append([f'MP-SA08-{n:02}',b.DATE,b.WHO,'used and rechecked in this run','Problem extracted from the full transcription and compared with the claim-specific primary sources; the separate plausible formulation is this run’s reconstruction.'])
def read(scan,line,old,alt,evidence,weight='essential',confidence='High mathematical alarm; ink undecided'):
 b.readings.append([136,scan,line,old,alt,evidence,weight,confidence])
read(330,'112','Γ*(X)⊗Γ*(Y)→Γ²(X×Y)','Γ* on the target, if total divided-power degree is intended','The displayed map contains every bidegree; degree two alone cannot receive it.')
read(333,'227','All factors replaced by ordinary powers','Retain a divided power on one factor in the PD product rule','γ_n(ab)=a^n γ_n(b); replacing the last divided power loses n!.')
read(334,'317','γ_pγ_q coefficient (pq)!/((p!)^q q!)','(pq)!/(p!(q!)^p), or reverse the nesting','p=2,q=3 distinguishes coefficients10 and15; root_checks.json.')
read(335,'349','λ^p x^p','λ^p x^(p)','The surrounding polynomial-law calculation uses γ_p(λx)=λ^pγ_p(x).')
read(337,'429','Ambiguous p−1 / pq in the shifted binomial coefficient','p−1 in the Pascal expansion','The independent factorial identity and1,080 shift tests agree; a numerical identity does not prove a natural decomposition.')
read(338,'484','Rank-one object identified with unnormalized Λ^(m+1)k^(m+2)','Insert the normalization/intersection of face kernels if intended','The displayed exterior power has rankm+2; its normalized piece has rank1.')
read(341,'678','Inconsistent nonzero/zero conditions and i+1 index','Check i−1 versus i+1 and the inequality in the second case','Adjacent clauses overlap or miss a case; no choice is made without the scan.')
read(345,'72–73','dim Ψ_m=m+1','dim Ψ_m=m','The split exact sequence0→kT→k^(m+1)→Ψ_m→0 fixes the rank.')
read(349,'388–390','Heisenberg matrix bottom-right entry0','Entry1 if this is the group element','Determinant would otherwise be0; scan351 writes1. The exact donor page is being collated, not used to silently edit this reading.')
read(357,'651–652','dℓ+ℓd for a degree-two homotopy','dℓ−ℓd under the ordinary homological convention','D(f)=df−(−1)^|f|fd; an alternative grading convention must be explicit.')
read(357,'704','Extra factor(−1)^i in Alexander–Whitney','No extra factor under the conventional total differential','The degree-one chain-map equation fails by twice a nonzero vertex difference; root_checks.json.')
read(361,'907','The sign exponent in the definition of P^i is blank','Leave blank pending the scan and the author’s conventions','There is no fully specified formula to verify.','Formula cannot be used as written','Certain blank in supplied text; ink undecided')
read(365,'200','Sq1 Sq2=Sq3+Sq2 Sq1 (?)','Sq1 Sq2=Sq3 for the usual composition convention','Apply both sides to t∈H1(RP∞;F2): the extra term gives t4.')
read(367,'311','L Sym^r=0 unless r=p^s','A stable positive-weight formulation with its range','r=0 and one-degree degree-zero objects rule out the unrestricted reading; surrounding lines invoke stabilization.')
read(371,'527–533','Entirely prime torsion without the positive stable-degree qualification','Exclude the fundamental group H_n and retain the stable range','H_n(K(Z,n);Z)=Z, and K(Z,2) has free even homology. This may be an omitted qualifier rather than a misread symbol.')
read(372,'649','Z+[S^m]=K(Z,n)','K(Z,m)','The free simplicial abelian group on the m-sphere represents degree m integral homology.')
read(373,'687–717','∧ and Z^G left untyped in the connectivity estimate','Distinguish ordinary space smash, simplicial tensor, and free abelian group','The ordinary space-smash reading fails for n=p=4,G=Z in degree10<11; no replacement is silently chosen.')
read(374,'721','H(X,R)=H(X,Fp)⊗R without a finiteness condition','Add sufficient finite-type/finite-dimensional hypotheses if intended','For countably discrete X and R=Fp[u], the sequence(u^n) is outside the tensor-product image.')
read(374,'727','P_R^i=P^i⊗1 for positive i','P^i⊗F for usual semilinear operations, or specify a different linear extension','At p=3, P1(uz)=u³z³, not uz³; root_checks.json.')
read(376,'903','F^v_p(i) in the denominator of Ext^(2i)','F^(v_p(i)+1) in Breen’s matching category','Breen1978 printedp40 andp116 were visually checked; the written exponent would incorrectly make Ext2 zero.')
# Both ends are supplied leaves or opened primary passages. Relatedness is labelled, never asserted as an identical theorem.
def link(kind,src,dst,what,evidence):b.links.append([kind,src,dst,what,evidence,'Codex continuation; no NOTES_INDEX verdict id'])
link('folder','cote136 scans326–327','cote136 scan328','Curve/flat-bundle example continues with an Euler-class normalization','Both supplied transcriptions read; the canonical nonsplit jet bundle in the modern comparison is distinct from the split bundle on the leaf.')
link('folder','cote136 scans320–325','cote136 scans329–335','Convolution and divided-power operations','Both transcriptions read; the later leaves spell out the Γ-valued operations and compatibility equations.')
link('folder','cote136 scans301–318','cote136 scans337–343,355','Additive cocompletion and reconstruction through test objects','Both ends read; the rank, Yoneda, bidual and colimit questions refine distinct parts of the program.')
link('folder','cote136 scans222–241','cote136 scan346','Euler contraction, weight operators, and filtered PD forms','Both ends read; total weight includes differential generators and controls the failed splitting factor.')
link('folder','cote136 scans095–141','cote136 scans348,350,352','Cochain products versus products defined only on cycles','Both ends read; the latter half differential algebra is a weaker structure, not an automatically equivalent construction.')
link('folder','cote136 scans189–234','cote136 scans362–363','Symmetric, exterior and divided-power derived shifts','Both ends read; the corrected décalage is a derived statement with the required projectivity hypotheses.')
link('published work','cote136 scan353','Sullivan1975 author PDF p8, TheoremD; Sullivan1977 §8 Th8.1','English donor model and homotopy interpretation','Exact typewritten passage matched to the author-hosted1975 text; finite/nilpotent hypotheses of the later homotopy interpretation retained.')
link('published work','cote136 scans349,351','Sullivan1975 author PDF pp9–10; Sullivan1977 §10 Th10.1','Heisenberg periods and the tower of nilmanifolds','Scan351 matches author PDFp9; PDFp10 continues to the nilmanifold tower and Hodge model, but the intervening wording on scan349 differs from this hosted version. Source relationship is established; exact349 wording and its bottom-right matrix entry are not decided from this version.')
link('published work','cote136 scans374–376','Breen1978 Th1.3 p47; §IV; §VII pp116–125','Fp-linear sheaf Ext, Frobenius and extended operations','Opened primary theorem, category hypotheses and exponent; the page’s edge-map proofs remain distinct checks.')
link('published work','cote136 scan375','Mathew2022 AppendixA ThA.1','Perfect-site higher Ext vanishing','Exact perfectFp-algebra and bigperfectétale-site hypotheses matched; does not compute the nonperfect case.')
link('published work','cote136 scan362','BMT2016 §3.4 Prop3.5 p270 eq3-9','Multiplicative derived décalage','Primary formula read with M finitelygeneratedprojective and all homological degree shifts.')
link('published work','cote136 scan370','Quillen1973 §7 Th5.4,5.11,5.19','Gersten, coniveau and Bloch formula','Regularity and finite-type-over-a-field scope retained; the unqualified scheme phrase is not an adequate hypothesis.')
b.add(958,'K136-02',[346],'306–315','\\Gamma^s\\Psi_* !?',
 'For the standard simplex quotient Psi=Phi/k, the simplicial divided powers Gamma^s(Psi) compute the appropriate nonadditive derived functor L Gamma^s(k[1]); they are not generally the single Eilenberg–Mac Lane object k[s]. Over Z, normalized Gamma^2(Psi) is Z in degrees2 and1 with differential multiplication by2, hence H1=Z/2; normalized Sym^2(Psi) has differential a unit. This distinguishes the objects explicitly queried on the leaf.',
 'open on the pages: the divided-power object is followed by two question marks',
 'Direct degree2 calculation: choose Psi2 basis e1,e2. In Gamma2, the normalized kernel is generated by e1e2; d0 sends it to -2e^(2). In Sym2 it sends it to -e^2. This agrees with the middle package computation and the derived décalage convention.',
 'E','Dold–Puppe derived functors and BMT2016 Proposition3.5 give the framework; the specific quadratic normalization is independently checked here. Search: root_web_014–021,034–035; middle primary audit of BMT2016 and scan229. The question is not a general theorem that Gamma^s preserves quasi-isomorphisms.',{'antecedent':'1961','modern_explicit_comparison':'2016'},['DoldPuppe1961','BMT2016'],'high','independent re-proof')
c=b.claims[-1]
b.problems.append(dict(id='MP-SA08-118',title='What is the divided-power simplex quotient?',occurrences=[{'claim':c['id'],'cote':136,'scans':[346],'lines':c['lines']}],as_he_states=c['his_statement'],plausible_today=c['statement'],state_of_art=c['fate'],why_open='The leaf asks for the object but gives no reason for leaving it unfinished. Its quadratic case already distinguishes Gamma from exterior and symmetric powers.',worth='Worth retaining as a resolved diagnostic calculation and a pointer to derived functors, not as an unqualified Eilenberg–Mac Lane guess.',refs=c['refs']))
b.events.append(['MP-SA08-118',b.DATE,b.WHO,'used and rechecked in this run','Question read at346:306–315 and its quadratic case checked explicitly.'])
read(360,'875–890','The X-variable Hom complex is a free Sigma_n-resolution of Z','Dold’s multivariable natural-Hom acyclicity plus a separate free resolution W','Dold1961 pp259–262 distinguishes the two objects. Diagonal-only naturality has at least four independent H0 classes for n=2; root_diagonal_ops.json. This is a hypothesis/object alarm, not a decision about ink.')
read(359,'800','Sigma_n times Sigma_n = Sigma_n','Check whether a subgroup, wreath product or different subscripts were intended','For n>=2 the two finite groups have different orders; the next diagram uses a wreath-type construction. No intended replacement is decided.')
read(359,'824,832–838','Sigma_n and W_n in a p-fold operation','Sigma_p and W_p if the operation has arity p','The displayed diagonal has p factors, and the next line identifies H*(Sigma_p). The cohomological degree n is a different index.')
read(361,'897–898','Sigma_n action on X^p followed by K(Sigma_p,1)','Use the arity-p group consistently if this is the same construction','The adjacent source/target formulas disagree on the acting symmetric group.')
b.write()
