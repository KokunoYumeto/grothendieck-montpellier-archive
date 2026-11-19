"""Manually authored scholarly records for the supplementary Codex transcriptions.

This program serializes explicit, individually written judgments. It does not
infer verdicts, mathematical status, or literature fate from keywords. Source
note verdicts are owned by the three package readers; Codex leads take none.
"""
import csv,json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'root_records'
OUT.mkdir(exist_ok=True)
claims=[];problems=[];readings=[];links=[];events=[]
WHO='GPT-6 Astra Pro; effort not exposed; SA07-part3/root'
DATE='2026-11-19'

def C(n,file,scans,lines,his,statement,status,computation,cls,fate,date,refs,confidence='high',event='used and rechecked in this run',outcome=None,search=None,origin='manuscript claim'):
    ident=f'CL-SA07-{n:03d}'
    if origin.startswith('this run'):
        status='Not a manuscript statement; this run’s explicit refinement. Its proof is supplied in the audit, not on the archival page.'
    claims.append(dict(id=ident,items=[],cote='15',scans=scans,lines=f'{file}_transcription.tex:{lines}',his_statement=his,statement=statement,status_on_pages=status,computation=computation,**{'class':cls},fate=fate,fate_date=date,present_status=f'As of 2026-11-19: {fate}',refs=refs,confidence=confidence,origin=origin,search_ids=search or []))
    events.append([ident,DATE,WHO,event,outcome or 'Compared the complete cited passage and the stated hypotheses with the opened reference; no independent proof of the external theorem is claimed.'])

# Deuring categories, localization, gerbes, and Brandt categories.
C(701,'B15-01',[59],'3-35','« F ↦ F(X) »; « générateur strict »',
  'Let C be A-linear with a strict generator X, o=End_C(X), and let its objects be the indicated P⊗_o X with P finite projective (or locally rank one, in the Deuring case). Evaluation identifies admissible A-linear functors C→C′ with o-objects X′ for which all the required P⊗_o X′ exist. This is the restricted universal property of the projective envelope, not an equivalence for arbitrary functors or an arbitrary generator.',
  'proof sketched','root_computations.md §1: evaluation and idempotent splitting.', 'E',
  'The projective-generator mechanism is classical Morita theory (1958, §3); Abrams–Ruiz–Tomforde §1 gives its precise ring form. Etingof et al. Theorem 9.6.4 verifies the finite abelian special case. The manuscript uses a restricted additive envelope.',
  'Morita: received 1957-11-11; published 1958. Modern verification: arXiv 2022-05-14; journal 2023.', ['Morita1958','AbramsRuizTomforde2022','EtingofRepresentation'],event='targeted proof check',search=['root016','root017','root019'])
C(702,'B15-01',[59],'19-25','« P⊗_o X ≃ Hom_o(̌P,X) »',
  'For a finite projective right o-module P, dualizing P and applying the corresponding idempotent to a finite power of X gives P⊗_o X ≅ Hom_o(P^∨,X), whenever the indicated objects exist. Variances are fixed by P being a right module.',
  'stated without proof','root_computations.md §1: dual-basis identity, then idempotent summands.', 'E','Established finite-projective tensor–Hom duality; the dual-basis proof checks the exact restricted statement. No assertion for arbitrary nonprojective P is retained.','Classical module theory before the 1965 folder date.',['AbramsRuizTomforde2022'],event='independent re-proof',search=['root019'])
C(703,'B15-01',[59],'27-35','« un foncteur pleinement fidèle canonique »',
  'The representable functor X↦Hom_C(−,X) embeds C fully faithfully into the indicated category of coadmissible A-linear functors, provided representables belong to that category. Full faithfulness is Yoneda; the coadmissibility restriction must first contain those representables.',
  'stated without proof','Natural transformation is determined by its value on id_X; see root_computations.md §1.', 'E','Yoneda lemma; Stacks Project, Lemma 4.3.5 (Tag 001P).','Classical before 1965; current Stacks version opened 2026-11-19.',['Stacks001P'],event='independent re-proof',search=['root011'])
C(704,'B15-01',[63],'56-69','« catégorie A-linéaire jolie ⇔ limite inductive »; « et inversement ? »',
  'The page proposes characterizing its undefined/uncertain “jolie” A-linear categories as filtered unions of full strict monogenic subcategories equivalent to full subcategories of finite projective modules containing the regular module. The exact closure axioms defining “jolie” are not recoverable from this fragment.',
  'open on the pages','No numerical computation. The filteredness assertion needs the missing closure axioms.','F','Morita theory identifies the monogenic pieces, but cannot determine the missing definition or prove the displayed biconditional with its present quantifiers. Exact-title and Deuring-category searches did not identify this particular terminology.','No exact identification established by 2026-11-19.',['AbramsRuizTomforde2022'],confidence='low',search=['root015','root016','root019'])
C(705,'B15-01',[81,82],'85-111','« localisable sur A »; « P⊗_R X »',
  'Assume the A-linear category C, localized on affine opens of Spec A, is a stack. If P is a right R-module locally isomorphic to R and X has an R-action, descent constructs P⊗_R X. If R→End_C(X) is an isomorphism, the twisting functor is fully faithful with image the local forms of X. For additive C the same holds for P locally finite free, with image local forms of finite powers of X.',
  'proof sketched','root_computations.md §1: glue local copies using transition matrices and identify Hom locally.','B','This is effective descent of objects and morphisms in a stack, applied to local forms. Modern bitorsor formalism verifies the change-of-trivialization mechanism (Ferrand §1). The assumed stack property is indispensable.','General descent formalism developed in SGA and Giraud; Ferrand notes dated May 2012.',['Ferrand2012'],event='targeted proof check',search=['root015','root016','root018'])
C(706,'B15-01',[82],'109-111','« stable par facteurs directs (=karoubienne) »',
  'For additive idempotent-complete C, a finite projective right R-module P represented by e∈M_n(R) yields P⊗_R X as the image of e acting on X^n. When R=End_C(X), this realizes the finite-projective envelope fully faithfully, without a stack assumption.',
  'stated without proof','root_computations.md §1: Hom(eX^n,fX^m)=f M_{m,n}(R)e.','E','The idempotent description is the classical projective-envelope part of Morita theory, preceding the manuscript.','Morita 1958; exact algebra checked in this run.',['AbramsRuizTomforde2022'],event='independent re-proof',search=['root019'])
C(707,'B15-01',[82],'111-123','« pour A′ … une A-algèbre … est équivalente »',
  'The literal assertion that scalar extension of the category of R-actions agrees with R-actions after arbitrary A→A′ is false even on Hom. Take A=Z, R=Z[T]/(T(T−2)), X=Z with T=0, Y=Z with T=2, and A′=F₂. Then Hom_R(X,Y)=0 while the scalar-extended R-modules have Hom=F₂. R is finite free of rank 2 and X,Y are finite free over A. The page’s stronger localization over Spec R is separately left unproved.',
  'false as stated','root_computations_output.json:R_action_base_change; complete hypothesis check in root_computations.md §1.','C','Flat base change repairs the finite-kernel Hom calculation (CL-SA07-708); it does not by itself guarantee that every new action descends from a global object. The literal arbitrary-base-change statement is refuted here.','Counterexample recorded 2026-11-19; underlying tensor exactness is classical.',['AbramsRuizTomforde2022','Stacks0C6I'],event='refuted, with refined statement CL-SA07-708',outcome='Exact finite-free counterexample: 2c=0 over Z has zero kernel, while modulo 2 all c commute. No scan reading is changed.',search=['root004','root016','root019','root027','root028'])
C(708,'B15-01',[82],'111-123','Refinement of the preceding scalar-extension assertion; not a replacement reading.',
  'If R is finitely generated as an A-algebra and A′ is flat over A, the R-linear Hom condition is the kernel of finitely many commutator maps, so base change preserves it. A stack C also gives a stack of R-actions when those actions are defined fibrewise. This does not assert essential surjectivity from the category with only globally defined R-actions: for R=Z[T], the rank-one action T=1/2 over Z[1/2] need not lift to rank one over Z.',
  'proof sketched','root_computations.md §1: kernel proof and the rank-one nonlifting example.','B','Established flatness/descent mechanism. Stacks Lemma17.22.5 gives the analogous flat pullback of sheaf Hom under its finite-presentation hypotheses; the action-category assertion is checked here by the finite commutator kernel. Only the specified part of CL-SA07-707 is repaired.','Classical exactness/descent; refinement formulated 2026-11-19.',['Ferrand2012','Stacks0C6I'],event='independent re-proof',search=['root015','root018','root027','root028'],origin='this run’s explicit refinement of a manuscript claim')
C(709,'B15-01',[82],'123-127','« Notre raisonnement ne prouve pas … localisable sur R »',
  'For commutative R, the R-linear action category is considered over Spec R. The author explicitly says his Spec A argument does not establish localization over Spec R. A valid stronger theorem requires a specified construction over R-opens and effective descent there.',
  'open on the pages','No computation; the two bases and two sites are kept distinct.','C','General stack descent supplies criteria, but does not settle the unspecified extension of the given C to Spec R. No exact unconditional theorem matching this fragment was identified in Deuring-category searches.','Searched through 2026-11-19.',['Ferrand2012'],confidence='medium',search=['root015','root016','root018'])
C(710,'B15-01',[82],'125-127','« apparentés (ou A-apparentés) »',
  'Under the localizability assumption, restriction to an affine open again gives a localizable category. Being locally isomorphic on Spec A is an equivalence relation; the full subcategory of forms of a fixed X is locally modeled by its endomorphism algebra and gives the stated Deuring category.',
  'proof sketched','Reflexivity, symmetry and transitivity localize; descent of forms and morphisms is inherited.','B','Standard descent and forms-of-an-object construction. Ferrand Lemma 1.1 describes the torsor/outer-isomorphism mechanism; the manuscript’s exact category name is retained.','General descent formalism; current verification 2026-11-19.',['Ferrand2012'],event='targeted proof check',search=['root015','root018'])
C(711,'K15-01',[34],'5-69','« gerbe sur A de lien G_m »; « représentations … poids 1 »',
  'The page relates rank-n weight-one representations of a G_m-gerbe to a Deuring–Brauer category; a determinant/norm datum leads to a μ_n-band. After choosing X and O=End(X), self-equivalences preserving the norm datum are modeled by invertible O-bimodules P with N(P)≅A. Automorphisms of the identity object are central units λ with λ^n=1. Full equivalence requires the stated splitting/Azumaya and descent hypotheses; the preceding Ex. 2 is absent.',
  'proof sketched','For a central scalar λ, its rank-n determinant is λ^n; hence Aut(1)=μ_n(A).','B','The gerbe/band and bitorsor formalism is established; Ferrand Proposition 1.2 and §2 verify the categorical mechanism. This does not reconstruct the missing Ex. 2 or assert all ramified orders are Azumaya.','Giraud 1971 as backward reference; Ferrand May 2012 opened directly.',['Ferrand2012','Voight2021Orders'],confidence='medium',event='targeted proof check',search=['root015','root016','root018'])
C(712,'K15-01',[36],'75-90','« 0 → H¹(S,μ_n) → π₀ … → Ram(C/A) → 0 »',
  'The norm-preserving Picard category is asserted to have an exact sequence with kernel H¹(S,μ_n) and quotient the ramification group ⊕_p Z/e_p(C)Z. The exact norm-trivialization hypotheses are inherited from the incomplete preceding examples; they cannot be erased. Its unnormalized maximal-order analogue is treated separately in CL-SA07-723.',
  'stated without proof','Automorphisms and norm scalars checked; no universal proof of the displayed norm-refined surjectivity is claimed.','C','Voight §18.4 verifies the unnormalized maximal-order sequence. It does not alone prove this norm-refined sequence for every category intended by the manuscript; the precise inherited hypotheses remain to be recovered.','Classical order theory; modern exact comparison 2021.',['Voight2021Orders','Ferrand2012'],confidence='medium',search=['root004','root015','root018'])
C(713,'K15-01',[36],'92-123','« une équivalence canonique »; « À vérifier !! »',
  'Equivalences between two fixed structured categories form a bitorsor under their self-equivalence group categories. If these group categories are Picard categories, transport by an equivalence identifies them up to coherent isomorphism; commutativity removes conjugation on isomorphism classes. A strict equality of functors without coherence data is stronger than this.',
  'open on the pages','root_computations.md §2: changing a chosen equivalence conjugates; the Picard constraint supplies the comparison.','B','The bitorsor-to-band construction gives the precise coherence-level formulation (Ferrand Lemma 1.1, Proposition 1.2). It verifies the formal step, not a canonical choice of an object in the bitorsor.','Giraud 1971; direct verification Ferrand 2012.',['Ferrand2012'],event='targeted proof check',search=['root015','root018'])
C(714,'K15-01',[38],'129-164','« Supposons qu’on ait pu associer canoniqt … un objet T »',
  'Assuming a canonical norm object T associated to the equivalence class of C, the author constructs a splitting of structured versus unstructured self-equivalences and a quotient comparison torsor independent of the representative C. Existence of that canonical T is a hypothesis, not a theorem on this page.',
  'open on the pages','root_computations.md §2: a splitting yields the stated quotient action; no construction of canonical T supplied.','C','Modern nonneutral Tannakian classification has precise uniqueness levels (Milne, §3, especially 3.19–3.20), but does not identify this particular integral norm object. Exact Deuring/gerbe searches found no matching unconditional canonical construction.','Milne manuscript 1992-10-16; publication 1994; corrected 2019.',['Milne1994Finite','Ferrand2012'],confidence='medium',search=['root014','root015','root016','root018'])
C(715,'K15-01',[40],'170-205','« la classe de p modulo des carrés »',
  'In the intended definite quaternion case B_{p,∞}, the two-sided prime ideal over p has reduced norm p and represents the ramification generator. After inverting p its norm trivialization contributes [p] in units modulo squares; locally the stated structured group is Z_p^×/Z_p^{×2}×Z/2. For odd p the unit-square quotient has order 2; p=2 must be kept separate. The opening transcribes “2” where the following text uses general p.',
  'proof sketched','root_computations.md §2: ideal norm, square classes and Hensel lifting; finite residue checks in root_computations_output.json.','B','The two-sided-ideal and ramification calculations agree with Voight §18.4 under maximal-order hypotheses. The norm refinement is checked directly in the stated local model.','Classical quaternion order theory; opened 2021 exposition.',['Voight2021Orders'],event='targeted proof check',search=['root004','root006'])
C(716,'K15-01',[42,44],'211-322','« f = (p,(0,1),p) »; quotient par f',
  'In the displayed product of prime-to-p square classes, a p-adic unit-square factor times Z/2, and real square classes, quotienting by f=(p,(0,1),p) removes the Z/2 coordinate. Since p>0, its real square class is trivial. This constructs the quotient group acting on a comparison torsor; it does not choose a point of that torsor.',
  'proof sketched','root_computations.md §2: (a,u,e,r) ↦ (a·p^(−e),u,r·p^(−e)); kernel generated by f.','B','A direct quotient-group calculation verifies the assertion; the torsor interpretation is standard bitorsor formalism. Canonical group identification must be distinguished from canonical trivialization.','Calculation rechecked 2026-11-19; general formalism established.',['Ferrand2012'],event='independent re-proof',search=['root015','root018'])
C(717,'K15-01',[44,46,50],'269-355;417-467','« à un signe près »; earlier canonical-equivalence language deleted',
  'The proposed unique canonical Deuring equivalence is explicitly weakened: the comparison is a connected groupoid with a residual μ₂ automorphism. Later construction depends on a chosen local class ξ_p and retains a sign ambiguity. The deleted descent to F_{p²} is not retained as a claim.',
  'corrected by himself later','No arithmetic computation; the automorphism group μ₂ explains why uniqueness up to unique isomorphism fails.','C','Established Deuring equivalence uses a base supersingular curve (Voight Theorem 42.3.2). Modern nonneutral classification makes the same distinction between equivalence, isomorphism class, and unique isomorphism; it does not restore the deleted canonicity.','Deuring 1941 background; Voight 2021; Milne 1994/2019.',['Voight2021Supersingular','Milne1994Finite'],event='targeted proof check',search=['root004','root006','root014','root018'])
C(718,'K15-01',[46],'358-365','« F_{p^n} = F_p[T]/Φ_{p^n−1} »',
  'The cyclotomic-quotient recipe is false as a universal construction of F_{p^n}. For p=2,n=3, Φ₇(T)=(T³+T+1)(T³+T²+1) over F₂, with distinct irreducible factors. The quotient is F₈×F₈, of cardinality 64. Thus the proposed compatible canonical algebraic closure does not follow.',
  'false as stated','root_computations_output.json:cyclotomic_quotient; factor identity and irreducibility proved in root_computations.md §3.','C','Finite fields are obtained from an irreducible polynomial of degree n, as in Conrad Theorem 1.1 and Example 1.2; an entire cyclotomic polynomial generally has several factors. Refined construction: CL-SA07-719.','Classical finite-field theory; explicit refutation 2026-11-19.',['ConradFiniteFields'],event='refuted, with refined statement CL-SA07-719',outcome='Exact factorization over F₂ and the Chinese remainder theorem certify a product of two fields, not one field.',search=['root007','root008'])
C(719,'K15-01',[46],'358-365','Refinement of the proposed finite-field construction.',
  'Choose an irreducible factor of Φ_{p^n−1} over F_p; every such factor has degree n because the multiplicative order of p modulo p^n−1 is n (with the trivial small case interpreted separately). This gives an abstract field F_{p^n}. A nested algebraic closure additionally requires compatible embeddings; no distinguished compatible system is selected by the formula alone.',
  'proof sketched','root_computations.md §3: Frobenius orbit and the inequality 0<p^d−1<p^n−1 for d<n.','E','Conrad Theorems 1.1 and 1.10 and the cyclicity of the multiplicative group supply the precise standard construction. Choice of presentation is separate from uniqueness up to isomorphism.','Classical finite-field theory before 1965.',['ConradFiniteFields'],event='independent re-proof',search=['root007','root008'],origin='this run’s explicit refinement of a manuscript claim')
C(720,'K15-01',[48,50],'373-405;417-467','« π₀=π₁=0, π₂=Z/2 »; « réfléchir/révérifier »',
  'The author describes a connected comparison 2-groupoid with the remaining μ₂ at the automorphism-of-identity level and asks whether a second sign remains. Pinning a local comparison class is proposed to rigidify it. The full coherence and independence assertions are not proved in the fragment.',
  'open on the pages','The hierarchy of automorphisms is distinguished from π₀; no formal 2-category certificate is claimed.','C','Gerbe and bitorsor theory provide the correct framework; Milne §3 proves different, precisely axiomatized uniqueness results. The exact two-sign calculation and integral pinning here have not been identified with a published theorem.','Searched to 2026-11-19; general formalism 1971–1994.',['Ferrand2012','Milne1994Finite'],confidence='medium',search=['root014','root015','root016','root018'])
C(721,'K15-01',[52],'477-517','« la gerbe sur R est non triviale »',
  'For the definite quaternion component, the real gerbe of two-dimensional fibre realizations is nonneutral: its division algebra at infinity is Hamilton’s H, which cannot act faithfully on a two-dimensional real vector space. A comparison to a nonneutral model gerbe is possible and must not be described as a real fibre functor.',
  'stated without proof','root_computations.md §2: every nonzero finite-dimensional H-module has real dimension divisible by 4.','B','The supersingular endomorphism algebra is ramified at p and infinity (Voight Theorem 42.1.9); the real obstruction follows directly. This matches the independent real-neutrality doubt at 15/207, with all geometric endomorphisms available.','Deuring 1941; current source Voight 2021.',['Voight2021Supersingular'],event='independent re-proof',search=['root004','root006','root014'])
C(722,'K15-01',[52],'477-517','« catégories des courbes elliptiques supersingulières »; quaternionic lines',
  'After fixing a supersingular base curve E₀ over F̄_p and O=End(E₀), Hom(−,E₀) gives the contravariant Deuring equivalence with invertible left O-modules; the opposite variance uses right modules. The page’s norm/polarization enhancement needs its chosen comparison datum and retains scalar signs.',
  'proof sketched','Variance and endomorphism-ring side checked against the exact modern theorem; no new proof of Deuring’s theorem.','B','Voight Theorem 42.3.2 and Corollary 42.3.7 establish the category and ideal-class correspondence. They do not supply the manuscript’s stronger unchosen polarized equivalence.','Deuring 1941; modern statement 2021.',['Voight2021Supersingular'],event='targeted proof check',search=['root004','root006','root016'])
C(723,'K15-02',[68],'3-34','Brandt action; quotient by Pic(A)',
  'For a maximal order O over a Dedekind ring R in a suitable central simple algebra, invertible two-sided O-ideals act on one-sided ideal classes; orbit/order identifications require distinguishing conjugacy from isomorphism of orders. In the quaternion global maximal-order case, 0→Cl(R)→Pic_R(O)→∏_{p ramified}Z/2→0. This is the unnormalized sequence, separate from CL-SA07-712.',
  'stated without proof','root_computations.md §2: central scalar ideals and valuation modulo ramification index.','B','Voight §18.4, especially (18.4.9), proves this precise maximal quaternion-order sequence; §42.3 connects ideal classes with supersingular curves. Nonmaximal orders require different hypotheses.','Classical order theory; exact modern statement 2021.',['Voight2021Orders','Voight2021Supersingular'],event='targeted proof check',search=['root004','root006'])
C(724,'K15-02',[70],'83-125','« Aut … / … ≃ Z/e »; Frobenius; j=0,1728',
  'For a maximal order over the relevant local DVR, normalizers modulo inner units give the cyclic ramification quotient Z/e. In the supersingular quaternion case, the prime above p acts by Frobenius on curve classes. Stabilization corresponds to j∈F_p; generally one or two curves can share an abstract maximal order. The transcribed automorphism orders at j=0 and 1728 are reversed in characteristic >3: they are 6 and 4, respectively.',
  'proof sketched','Quaternion ideal valuation checked; the elliptic-curve automorphism calculation is in root_computations.md §2.','B','Voight §18.4 and Lemma 42.4.1 give the order/Frobenius comparison; Example 42.3.11 confirms the exceptional unit orders. The truncated question about o* is not completed.','Classical Deuring/order theory; 2021 verification.',['Voight2021Orders','Voight2021Supersingular'],event='targeted proof check',search=['root004','root006'])
C(725,'K15-02',[70],'83-125','locally inner automorphisms and Pic(A)',
  'For an order O, local conjugating elements for an A-algebra automorphism differ on overlaps by central units. Their line-bundle class is the obstruction to a global conjugator; the relevant subgroup of Pic(A) maps trivially to the torsor set H¹(A,O^×). Global innerness does not follow from local innerness unless this obstruction vanishes.',
  'proof sketched','root_computations.md §2: the overlap cocycle of conjugators.','B','The normalizer/ideal description in Voight §18.4 and the bitorsor descent calculation in Ferrand Lemma 1.1 verify the obstruction mechanism.','Classical descent; direct verification 2026-11-19.',['Voight2021Orders','Ferrand2012'],event='independent re-proof',search=['root004','root015','root018'])
C(726,'K15-02',[72],'165-199','Brandt/Brauer 2-groupoid; invertible bimodules',
  'Under the page’s explicit assumption that automorphisms of the generic algebra E are inner, equivalences of its order categories are represented by invertible bimodules. Generic embeddings are determined up to central units. A choice of generator gives a Morita description, but not a natural strict quasi-inverse independent of all choices.',
  'proof sketched','root_computations.md §1–2: evaluation, bimodule tensor composition and central automorphisms.','B','Morita theory and the bitorsor/band formalism establish this reconstruction under the innerness hypothesis. Dropping that hypothesis would add outer automorphism data.','Morita 1958; Ferrand 2012 verifies coherent transport.',['AbramsRuizTomforde2022','Ferrand2012'],event='targeted proof check',search=['root015','root018','root019'])
C(727,'K15-02',[74],'236-277','« condition C »: commuting two-sided ideals',
  'The manuscript imposes commutativity of the relevant two-sided ideals before transporting a strictly commutative Picard structure to the Brandt category. It is not a claim for arbitrary orders. Maximal orders in the Dedekind/semisimple setting satisfy the needed commutativity; nonmaximal orders need not.',
  'proof sketched','root_computations.md §2: multiplication of invertible two-sided ideals and transported symmetry.','B','Voight Theorem 18.1.2 supplies commutative factorization for maximal orders; §18.5.7 shows the limitation for nonmaximal orders.','Classical maximal-order theory; 2021 verification.',['Voight2021Orders'],event='targeted proof check',search=['root004','root006'])
C(728,'K15-02',[76],'313-337','« indépendante du générateur »; inner-equivalence check',
  'With the commuting-ideal hypothesis, replacement of a generator by an invertible connecting bimodule P transports a two-sided ideal L to PLP⁻¹. The manuscript checks compatibility with tensor multiplication and its chosen symmetry; the inner-equivalence independence is marked and then addressed. This is not an entirely unproved canonicity claim.',
  'proved there','root_computations.md §2: (PLP⁻¹)(PMP⁻¹)=P(LM)P⁻¹ and unit compatibility.','B','Voight (18.4.7) gives the same conjugation transport on ideal/Picard groups; the page supplies the higher categorical compatibility under its additional condition.','Classical Morita transport; modern verification 2021.',['Voight2021Orders','Ferrand2012'],event='targeted proof check',search=['root004','root018'])
C(729,'K15-02',[78],'376-407','canonical Brandt Picard category; change of base',
  'The constructed Brandt 2-category is described by torsor categories under its Picard automorphism category, with compatibility under base changes preserving the local order, admissibility, and commuting-ideal hypotheses. The page does not justify arbitrary nonflat preservation of all those hypotheses.',
  'proof sketched','Associativity and the invertible-bimodule composition are checked formally; no arbitrary base-change theorem inferred.','B','Ferrand §1–2 establishes the underlying groupoid/bitorsor mechanism; the stated preservation hypotheses remain part of the reconstruction.','General gerbe/bitorsor theory established; 2012 direct source.',['Ferrand2012','Voight2021Orders'],confidence='medium',event='targeted proof check',search=['root015','root018'])
C(730,'K15-02',[84,86],'431-439;460-480','« φ(u)φ(u)′=ε(u) »; compact torus',
  'For a polarized faithful realization of a commutative motivic group, its commutative image algebra B with positive involution controls the norm-one group. Over R, the identity component of that norm-one group is a compact torus. This conclusion is not valid for the norm-one group of a general noncommutative End algebra A; for A=M₂(Q) with transpose, the full orthogonal group is not a torus.',
  'proof sketched','root_computations.md §4: B_R≅R^r×C^s and norm-one identity component (S¹)^s.','B','Milne CM Proposition 1.39 gives the commutative positive-involution classification needed for the conclusion. The passage from A to the commutative generated algebra B is essential.','Classical CM theory; author notes first 2006, checked 2020 version.',['MilneCM2020'],event='targeted proof check',search=['root005','root006','root017'])
C(731,'K15-02',[86],'460-480','« produit de corps de type CM »',
  'The literal assertion that every factor of the commutative positive-involution algebra B is CM misses fixed totally real factors. The unit object has B=Q with identity involution and positive trace form, so it is a counterexample unless the page imposes an unstated exclusion of weight-zero/fixed factors.',
  'false as stated','root_computations.md §4: B=Q, Tr(x x*)=x²>0; Q is totally real, not CM.','C','The correct classification allows totally real identity factors and CM conjugation factors (CL-SA07-732; Milne Proposition 1.39).','Positive-involution theory established; counterexample recorded 2026-11-19.',['MilneCM2020'],event='refuted, with refined statement CL-SA07-732',outcome='The tensor unit supplies the omitted totally real factor. This is a mathematical qualification; the ink is not emended.',search=['root005','root006'])
C(732,'K15-02',[86],'460-480','Refinement of the CM-factor assertion.',
  'A finite-dimensional commutative Q-algebra with positive involution is a product of totally real fields with identity involution and CM fields with complex conjugation. Its real norm-one group has finite ±1 factors and circle factors, so the identity component is compact. No assertion of connectedness of the entire group is made.',
  'proof sketched','root_computations.md §4: real-factor calculation; algebra classification used from Milne, not independently re-proved.','B','Milne CM Proposition 1.39 is an exact match to this refinement.','Version checked dated 2020-07-14; first notes 2006-04-07.',['MilneCM2020'],event='targeted proof check',search=['root005','root006'],origin='this run’s explicit refinement of a manuscript claim')
C(733,'K15-02',[86],'460-480','ε and j to be recovered from norm operations',
  'The page asks how the similitude/weight character ε and the real involution j can be recovered intrinsically from the commutative norm algebra. The positive-involution classification supplies necessary structure, but does not by itself specify a unique motivic character or a canonical descent datum.',
  'open on the pages','No numerical computation; character/cocharacter and involution data remain distinct.','C','CM and Mumford–Tate theory describe the norm and Hodge data (Milne CM §§1,4), but the fragment lacks sufficient hypotheses for the proposed intrinsic reconstruction.','Searched through 2026-11-19.',['MilneCM2020'],confidence='medium',search=['root005','root017'])
C(734,'K15-02',[85],'443-456','big/small étale comparison; universe footnote',
  'For a scheme X and the standard morphism between its big and small étale topoi, inverse image from the small site is fully faithful and the corresponding cohomology comparison holds for abelian sheaves. Universes must be chosen compatibly; the manuscript footnote makes that qualification.',
  'stated without proof','The inverse/direct image adjunction and the exact published proposition were compared; no fresh proof of the full topological theorem.','A','Exact published counterpart: SGA 4, Exposé VII, Proposition 4.1 and its universe footnote. The retyped source preserves this locator.','Seminar 1963–1964; SGA 4 tome 2, LNM 270, publication 1972; retyped edition 2024.',['SGA4VII'],event='used and rechecked in this run',search=['root005','root006'])

# The analysis leaves and remaining mathematical collateral are appended below.
C(735,'B15-02',[37],'87-91','« f(x)=g(x) … pour tout x∈P∩Q »',
  'For K=R or C and Banach-valued convergent power series on intersecting polydiscs, equality on a nonempty open subset implies equality on their connected intersection. The reduction to a real line segment uses the one-variable identity theorem. This scope does not include arbitrary locally analytic functions over a disconnected non-Archimedean field.',
  'proved there','root_computations.md §5: propagation of zero Taylor coefficients; continuous linear functionals separate Banach vectors.','E','Classical identity theorem; modern locator: Lebl, Theorem 1.2.7 and §3.1.','Classical before 1965; opened edition 2026-05-31.',['Lebl2026'],event='targeted proof check',search=['root009','root010','root011','root012'])
C(736,'B15-01',[62],'40-46','« une fonction f, holomorphe dans A=⋃A_α »',
  'For K=R or C, analytic functions on domains A_α glue if each nonempty pairwise overlap is connected and the two functions agree on a nonempty open subset of that overlap. The identity theorem first makes the functions agree on the whole overlap. A disconnected overlap does not suffice.',
  'proved there','root_computations.md §5: identity theorem plus pointwise gluing.','E','Classical analytic continuation; the needed identity theorem is Lebl Theorem 1.2.7.','Classical before 1965.',['Lebl2026'],event='independent re-proof',search=['root009','root010','root012'])
C(737,'B15-01',[62],'48-52','« en vertu du th. de Zorn … un élément maximal »',
  'A given analytic function on a domain has a maximal single-valued extension to some larger domain, by taking unions of chains of extensions and applying Zorn. The extension on any fixed connected maximal domain is unique. Distinct maximal domains may exist; this is not a unique universal continuation space.',
  'proved there','root_computations.md §5: chain union is a domain and the chain functions agree.','E','Classical analytic-continuation argument; uniqueness uses the identity theorem. No unique-domain assertion is retained.','Classical before the manuscript.',['Lebl2026'],event='independent re-proof',search=['root009','root010','root012'])
C(738,'B15-01',[64],'75-79','square-root branches agree on H and disagree on the other component',
  'The displayed branches of sqrt(z) on two slit angular domains agree on one component of the overlap and differ by sign on the other. The second printed H must be checked against H′ on the scan; the branch formulas themselves establish why connectedness was required.',
  'proved there','root_computations.md §5: θ′=θ+2π yields equality for the chosen second branch; θ′=θ yields the opposite sign.','E','Standard branch/monodromy example, verified directly from the exponential formulas.','Classical before 1965.',['Lebl2026'],event='independent re-proof',search=['root009','root010'])
C(739,'B15-01',[64],'77-79','real-slice uniqueness; one-variable accumulation criterion',
  'Holomorphic functions in C^p agreeing on a relatively open piece of a translated real p-plane agree locally and hence on the connected overlap. For K=R or C in one variable, equality on a set with an interior accumulation point also suffices. The one-variable criterion is not extended to several variables.',
  'proved there','Taylor coefficients on the real slice coincide; the one-variable first nonzero coefficient gives isolated zeros.','E','Lebl §3.1 and Appendix B, Theorem B.7, are the matching modern locators.','Classical before 1965.',['Lebl2026'],event='targeted proof check',search=['root009','root010','root012'])
C(740,'B15-02',[27,29,31],'6-12;19-25;34-46','« domaine contractile »; « expression différentielle fermée »',
  'On a connected open subset of R^n or C^n in which every loop is null-homotopic, a closed analytic one-form with Banach-valued coefficients has an analytic primitive, unique up to a constant. Here the author defines “contractile” to mean the loop condition, i.e. simply connected, not modern contractibility. Polygonal path integration and local primitives prove the result.',
  'proved there','root_computations.md §5: path independence, local differentiation, and uniqueness.','E','Classical primitive theorem; Lebl Appendix C, Theorem C.6, supplies the smooth Stokes comparison.','Classical before 1965.',['Lebl2026'],event='targeted proof check',search=['root009','root011','root012'])
C(741,'B15-02',[31,33],'30-59','homotopy invariance; « seulement … continument différentiables »',
  'The integral of a closed analytic one-form is invariant under endpoint-fixed path homotopies. The proposed real C¹ extension is valid: local primitives exist by the elementary Poincaré integral formula, and a subdivision of a compact homotopy makes local primitive increments cancel. The interpolation in the displayed proof has a denominator error, separately flagged.',
  'proof sketched','root_computations.md §5; root_computations_output.json:interpolation.','E','Classical C¹ closed-form theorem. Lebl Theorem C.6 verifies its smooth Stokes form; the C¹/local-primitive extension is re-proved here.','Established before the manuscript; check 2026-11-19.',['Lebl2026'],event='independent re-proof',search=['root009','root011','root012'])
C(742,'B15-02',[29,35],'23-25;64-72','polygonal routes, star-shaped contraction, homotopy relation',
  'Open connected subsets of R^n are polygonally connected; compact paths in an open set admit endpoint-fixed homotopies to polygonal paths. The displayed star-shaped contraction is valid. Homotopy is an equivalence relation. Concatenating two chosen homotopies requires matching their common endpoint throughout. This last valid construction warning is this run’s qualified reconstruction; the stronger literal existence remark is separated in CL-SA07-771.',
  'proved there','root_computations.md §5: finite convex-ball subdivision and straight interpolation; separate free-path warning in CL-SA07-771.','E','Elementary homotopy and open-set geometry. Hatcher §1.1 pp.25–26 gives the endpoint-fixed concatenation result.','Known before 1965.',['Lebl2026','Hatcher2002'],event='targeted proof check',search=['root009','root011','root012','root030','root031','root032','root033'])
C(743,'B15-02',[39],'98-130','Frobenius mixed-partial condition and w′=Aw',
  'For analytic functions U_ij(x,y) over R or C satisfying ∂_xk U_ij+Σ_h U_kh∂_yh U_ij=∂_xi U_kj+Σ_h U_ih∂_yh U_kj, solve the radial ODE v′_j=Σ_iδ_iU_ij(x₀+tδ,v). The defect w_kj=∂_δk v_j−tU_kj satisfies a homogeneous linear ODE and zero initial data, hence vanishes. This yields the local integrable solution family.',
  'proved there','root_computations_output.json:Frobenius_chain_rule; full indexed derivation in root_computations.md §6; parallel K15-02 15/069:44-79.','E','Classical Frobenius theorem; exact Banach-valued formulation and the variation-of-ODE method occur in Penot, Theorem 1.1.','Classical theorem before 1965; Penot published 1970.',['Penot1970'],event='targeted proof check',search=['root011','root012'])
C(744,'B15-02',[41],'137-147','« u(x₀,x,y)=y₀ »; inverse flow',
  'For a local analytic ODE over R or C, solutions depend analytically on initial time, initial value and parameters; after shrinking to suitable neighborhoods, the time-change maps are local inverses. The supremum bound in the proof requires a bounded smaller domain, not an unproved maximum on an arbitrary open product.',
  'proved there','root_computations.md §6: uniqueness yields the flow composition and inverse identities.','E','Classical parameter-dependent ODE theory; Penot Theorem 1.1 includes the relevant parameter construction.','Known before 1965; opened primary 1970.',['Penot1970'],event='targeted proof check',search=['root011','root012'])
C(745,'B15-02',[43,45],'154-164;169-197','« par récurrence … de façon unique »',
  'In characteristic zero, coefficient comparison for y′=f(x,y,z), y(0,z)=0 uniquely determines a formal solution: divide the coefficient at x^(m−1)z^μ by m, using only coefficients of smaller total degree. Products must use the component j corresponding to each y_j factor, and parameter exponents need the ℓ index. Formal uniqueness alone says nothing about convergence or uniqueness among merely locally analytic functions on a fixed p-adic domain.',
  'proved there','root_computations.md §6: coefficient convolution and degree inequality; parallel K15-02 15/071:133-158.','E','Classical formal ODE recursion. Kedlaya’s power-series differential-equation framework preserves the distinction between formal and convergent solutions.','Classical before 1965; source edition inspected 2026-11-19.',['KedlayaFoundations'],event='targeted proof check',search=['root010','root011'])
C(746,'B15-02',[47],'215','« corps valué complet de caractéristique 0 »',
  'Reconstructed valid version: a finite analytic ODE system over a complete, nontrivially valued characteristic-zero field has a unique formal solution for fixed initial data and a convergent solution germ on a sufficiently small polydisc, with finitely many analytic parameters. For non-Archimedean K the scaled integral-coefficient derivation D gives coefficients D^n(y)/n!, bounded by an exponential; this proves convergence after shrinking. Discretely valued fields are included. Literal uniqueness among all locally analytic functions on a fixed p-adic open set is separated in CL-SA07-747.',
  'proof sketched','root_computations.md §6 contains the complete independent scaled-derivation and factorial-bound proof; no optimal-radius theorem is claimed.','B','Established convergent-germ ODE theory, independently re-proved here. Kedlaya Chapter1 §3 supplies the radius-loss comparison. The historical Lutz reference was checked bibliographically only, not as a proof of this full parameter formulation.','Classical p-adic theory; Lutz publication1937; precise independent proof2026-11-19.',['KedlayaFoundations','Lutz1937','PintoDosSantos2007'],event='independent re-proof',outcome='After rescaling the analytic vector field to integral coefficients, exp(sD) supplies the formal flow and the bound |1/n!|≤A^n proves joint local convergence; formal uniqueness gives germ uniqueness.',search=['root010','root011','root025','root027'],origin='this run’s explicit refinement of the manuscript ODE theorem')
C(747,'B15-02',[47],'215','« un système et un seul … holomorphes dans U×W »',
  'With “holomorphic” defined merely by a local power series at every point (B15-03, 15/057), uniqueness on a fixed open p-adic U is false. On Q₃, both 0 and the function equal to 3^N on 1+3Z₃ and 0 on the other residue classes solve y′=0 on Z₃ with y(0)=0. They are locally constant and locally analytic. On every smaller ball 3^mZ₃ use the clopen subball 3^m+3^(m+1)Z₃ and choose the amplitude inside V. They define the same germ at 0, so germ uniqueness survives.',
  'false as stated','root_computations_output.json:locally_analytic_ODE; all domain, initial-value and size conditions checked in root_computations.md §6.','C','Restricting to power-series germs or a specified convergent power series on the disc gives CL-SA07-746. The locally constant obstruction is already standard in p-adic ODE introductions; this run supplies its complete counterexample.','Explicit check 2026-11-19.',['KedlayaFoundations'],event='refuted, with refined statement CL-SA07-746',outcome='Locally constant solutions satisfy every literal local-analytic and initial-value condition; the theorem needs a germ/global-power-series qualification.',search=['root010','root011'])
C(748,'K15-02',[71],'133-158','coefficient majorants after division by m',
  'The ordinary real positive majorant recurrence cannot simply be used with real 1/m over a non-Archimedean field. For y′=1+y, y(0)=0, the coefficient of x² is 1/2, of 2-adic norm 2, larger than the real majorant coefficient 1/2. Absolute-value control needs |1/m|_K and a corresponding radius shrink.',
  'false as stated','root_computations_output.json:padic_majorant_failure; root_computations.md §6.','C','Kedlaya Chapter 1 §3 gives the p-adic exponential radius p^(−1/(p−1)); it demonstrates the exact kind of loss ignored here. Refined statement: CL-SA07-746.','Classical p-adic exponential; check 2026-11-19.',['KedlayaFoundations'],event='refuted, with refined statement CL-SA07-746',outcome='The coefficient x² in the scalar example disproves the claimed ordinary-real majorization over Q₂.',search=['root010','root011'])
C(749,'B15-03',[49],'7-34','equations (9), (10); square-root expression for v',
  'For the real nonnegative majorant system, all v_i coincide. Put a=qμ(1+qMμ), b=M((1−μΣt_j)^(−1)−1); the reduced equation is v−av²=b, with branch v=(1−sqrt(1−4ab))/(2a), v(0)=0. It converges near zero and provides the majorant in the implicit-function argument. Local uniqueness follows from the strict small-increment estimate, with equality u_i=w_i, not an inequality.',
  'proved there','root_computations_output.json:implicit_majorant; symbolic substitution has residual 0.','E','Classical analytic implicit-function theorem; modern complex locator Lebl Theorem 1.3.8. The displayed algebra is independently verified.','Known before 1965.',['Lebl2026'],event='computation or formal certificate',outcome='Exact symbolic substitution verifies the quadratic solution; convergence and uniqueness are checked by the stated small-neighborhood argument.',search=['root009','root010','root012'])
C(750,'K15-02',[79],'413-425','« (1−Σ binom(2n,n)x^n)²=1−4x »',
  'The transcribed central-binomial square-root identity is false: the x² residual is −8. The correct formal expansion is sqrt(1−4x)=1−Σ_{n≥1}(binom(2n,n)/(2n−1))x^n. This is a candidate scan reading, not a change to the source. B15-03 15/049 also has a binomial-variable/sign error: sqrt(1−w)=Σ binom(1/2,n)(−w)^n.',
  'false as stated','root_computations_output.json:square_root_display; generalized-binomial proof in root_computations.md §7.','C','The corrected formal binomial identity is classical and underlies CL-SA07-751. The literal displayed equation is refuted at degree 2.','Classical binomial theorem; exact check 2026-11-19.',['Lebl2026'],event='refuted, with refined statement CL-SA07-751',outcome='Degree-2 residual −8 disproves the literal identity; the finite degree-8 check of the candidate is not presented as its general proof.',search=['root009','root010'])
C(751,'K15-02',[79],'413-425','local square root in a complete normed algebra',
  'In a commutative complete normed algebra over a complete valued field of characteristic ≠2, the root near 1 of y²=1+x is locally unique and analytic on a sufficiently small neighborhood. The radius must account for the absolute values of binomial denominators. This local implicit-function statement, not a radius-one assertion in every valuation, is the retained theorem.',
  'proof sketched','root_computations.md §7: solve at y=1 where derivative 2 is invertible; formal binomial recurrence.','E','Classical implicit-function special case; the complex version is covered by Lebl Theorem 1.3.8. Non-Archimedean radii need the valuation qualification.','Known before the manuscript; exact local formulation checked 2026-11-19.',['Lebl2026','KedlayaFoundations'],event='targeted proof check',search=['root009','root010','root011'])
C(752,'B15-03',[51],'41-52','quadratic remainder bounded by Mt² times a dimensionless sum',
  'With M=sup||b_nm||r^(|n|+|m|), the displayed quadratic remainder estimate is missing r^(−2). In one variable choose f(z)=z², u=0, r=1/4, w=t=1/16. The actual remainder is 1/256, while even summing the displayed full geometric upper bound gives 1/1536. Inserting r^(−2) repairs the dimensional calculation.',
  'false as stated','root_computations_output.json:missing_scale_factor; root_computations.md §7.','C','The corrected estimate establishes the standard strict differentiability statement CL-SA07-753. The theorem survives the missing constant, but the printed inequality does not.','Correction inferred 2026-11-19; scan verification remains pending.',['Lebl2026'],event='refuted, with refined statement CL-SA07-753',outcome='Exact rational counterexample includes the entire geometric sum, not only its first term.',search=['root009','root010','root012'])
C(753,'B15-03',[51,53],'54-60;76-82','« Toute fonction holomorphe … indéfiniment différentiable »; estimate (6)',
  'A locally absolutely convergent Banach-valued power series is strictly differentiable near each point: the increment differs from Df(a)(u−v) by at most ε||u−v|| after shrinking. Termwise derivatives are locally convergent power series, so the function is indefinitely differentiable. The repaired remainder constant in CL-SA07-752 is enough; no false fixed-radius assertion is required.',
  'proved there','root_computations.md §7: geometric sums, smaller-radius coefficient bounds, and iteration.','E','Standard analytic calculus; compare Lebl §§1.2–1.3.','Known before the manuscript.',['Lebl2026'],event='targeted proof check',search=['root009','root010','root012'])
C(754,'B15-03',[53],'67-74','weighted series « converge en même temps » at the displayed radius',
  'Convergence at a specified boundary radius is not preserved by multiplying coefficients by polynomial weights. At r=1, a_n=1/(n+1)² is summable, while (n+1)a_n is not. The manuscript’s local primitive argument needs convergence on strictly smaller polyradii, not this false equality of boundary convergence.',
  'false as stated','root_computations_output.json:boundary_convergence; root_computations.md §7.','C','The smaller-radius theorem is CL-SA07-755. It repairs the proof of local analytic integration without asserting identical boundary behavior.','Classical power-series convergence; exact check 2026-11-19.',['Lebl2026','KedlayaFoundations'],event='refuted, with refined statement CL-SA07-755',outcome='The p-series/harmonic-series pair refutes the literal same-radius convergence assertion.',search=['root009','root010','root011'])
C(755,'B15-03',[53],'67-74','coefficient relations n_k b_n=c_{k,n−e_k}',
  'For a closed analytic one-form in characteristic zero, compatibility of its partial derivatives determines a formal primitive by n_k b_n=c_{k,n−e_k}, with chosen constant. Since |1/n|_K is bounded by a polynomial in n for an ordinary rank-one absolute value on a characteristic-zero field, any smaller polyradius absorbs the division factors. Hence the primitive converges locally. The claim concerns power-series germs, not uniqueness on disconnected p-adic domains.',
  'proved there','root_computations.md §7: boundedness of n^β(ρ/r)^n and coefficient compatibility.','E','Classical local power-series integration; the radius qualification is standard.','Known before the manuscript; refined proof recorded 2026-11-19.',['Lebl2026','KedlayaFoundations'],event='independent re-proof',search=['root009','root010','root011'])
C(756,'B15-03',[55],'91-99','composition, continuous multilinear products, componentwise holomorphy',
  'Absolutely convergent power series may be substituted on a sufficiently small polydisc; continuous multilinear maps applied to analytic functions remain analytic, and a map to a finite product is analytic exactly when its components are. Completeness and absolute-summability estimates justify regrouping; arbitrary substitutions without a convergence neighborhood are excluded.',
  'proved there','root_computations.md §7: ||B(v₁,…,v_m)||≤||B||∏||v_i|| and absolute Cauchy products.','E','Standard convergent-power-series calculus; Lebl §§1.2–1.3 give the scalar complex comparison.','Known before 1965.',['Lebl2026'],event='targeted proof check',search=['root009','root010','root012'])
C(757,'B15-03',[57],'110-120','re-expansion at an interior point; local definition of holomorphic',
  'An absolutely convergent power series can be re-expanded at an interior point on a smaller polydisc by the binomial formula and absolute regrouping; its coefficients are the corresponding derivatives divided by factorials in characteristic zero. The local definition at every point is weaker than representation by one series on a whole disconnected p-adic domain.',
  'proved there','root_computations.md §7: radius inequality and binomial regrouping.','E','Standard power-series re-expansion; compare Lebl §1.2. The distinction in the final sentence is essential for CL-SA07-747.','Known before 1965.',['Lebl2026','KedlayaFoundations'],event='targeted proof check',search=['root009','root010','root011'])
C(758,'B15-02',[47],'202-209','inverse-function corollary; x^n on |x−1|<1/2',
  'An analytic map with invertible differential has an analytic local inverse. A nonvanishing derivative on a real interval gives global monotonicity, whereas it does not force injectivity on a complex domain: z↦z¹³ on |z−1|<1/2 takes both 1 and exp(2πi/13) to 1, and its derivative never vanishes there.',
  'proof sketched','root_computations_output.json:power_map_example gives 2sin(π/13)<44/91<1/2.','E','Classical analytic inverse theorem; Lebl Exercise 1.3.6 and Theorem B.15. The explicit exponent 13 is this run’s witness.','Known before 1965; witness checked 2026-11-19.',['Lebl2026'],event='targeted proof check',search=['root009','root010','root012'])
C(759,'B15-02',[47],'211','« théorème de dépendance … à jacobien identiquement nul »',
  'The author asks for a theorem on dependence of holomorphic functions whose Jacobian vanishes identically. A precise valid local formulation is the constant-rank theorem near a point of maximal rank r: in suitable local analytic coordinates the map depends on r variables. The fragment does not specify global analytic, algebraic, or germ-wise dependence, and these are not interchangeable.',
  'open on the pages','No unconditional global dependence theorem is inferred from the sentence.','C','Local analytic rank theory follows from the inverse theorem. A global polynomial relation is not implied by a vanishing Jacobian (e.g. coordinate functions z and exp z as a map of rank 1).','Classical local theory; ambiguity retained as of 2026-11-19.',['Lebl2026'],confidence='medium',event='targeted proof check',search=['root009','root010','root012'])
C(760,'B15-01',[171],'215-227','Q/3P, O₅(F₃), orders 25920 and 51840',
  'Reconstruction: the truncated exercise concerns E₆. Its root lattice Q modulo 3P is a nondegenerate 5-dimensional quadratic space over F₃. The 72 roots inject and are its norm-one vectors; the Weyl group has order 51840 and its determinant-one subgroup order 25920. Adding −1 gives the full orthogonal/root-automorphism group of order 103680; the rotation subgroup is the simple group PSp₄(3). The identification of the missing root-system name is explicitly ours.',
  'stated without proof','root_lattice_checks_output.json:E6_reconstruction certifies root counts, quotient action, orders and −1; root_computations.md §8 separates arithmetic from simplicity.','B','Exact published parallel: Bourbaki, ChapterVI §4 Exercise2(a–c), pp.242–243 in the2002 English translation, with Q/3P and the distinguished index-two subgroup. Hamm §7.1 gives the PSp₄(3) identification. Collective Bourbaki authorship does not establish sole Grothendieck authorship.','French publication1968; English translation2002. Hamm preprint2014-09-01, publication2016-07-27.',['BourbakiLie4to6','Hamm2016'],event='computation or formal certificate',outcome='Exact root generation and group orders verify the E₆ model; the published exercise matches the truncated opening, but no archival reading is changed and simplicity is used from the source.',search=['root010','root011','root028','root029'])
C(761,'B15-01',[171],'229-238','« E₇ »; « W⁺ ≃ Sp₆(F₂) »',
  'For E₇, Q/2P is a 6-dimensional symplectic space over F₂. The Weyl action maps onto Sp₆(F₂) with kernel {±1}; because −1 has determinant −1 in rank 7, W⁺ maps isomorphically. Thus |W⁺|=2⁹·3⁴·5·7=1451520 and |W|=2903040. The alternative E₈/O₇(F₂) route is a suggested exercise route, not a second proof written on the sheet.',
  'stated without proof','root_lattice_checks_output.json:E7; root_computations_output.json:root_group_orders; root_computations.md §8.','B','Exact published parallel: Bourbaki, ChapterVI §4 Exercise3(a–c), p.243, Q/2P, kernel{±1}, and W⁺≅Sp₆(F₂). Hamm §8.1 supplies a later comparison. Collective authorship is not converted into a personal-publication attribution.','French publication1968; English translation2002. Hamm2014 preprint /2016 publication.',['BourbakiLie4to6','Hamm2016'],event='computation or formal certificate',outcome='Generated126 roots; exact action has image order1451520 and kernel order2, containing−identity; published exercise read at its exact locator.',search=['root010','root011','root028','root029'])
C(762,'B15-01',[188],'265-293','cohomology inequality after a vanishing assumption',
  'The page uses the exact segment H^i(V,O_V(−E_φ)[nE])→H^i(V,O_V[nE])→H^i(V,K[nE]). Assuming H^i(V,K[nE])=0 for i≥1 and n≥n₀(K), and O_V(−E_φ)≅O_V(−E), the first arrow is surjective. For finite-dimensional cohomology this gives h^i(O_V[nE])≤h^i(O_V[(n−1)E]). K is the quotient in this segment, not its kernel. No unconditional vanishing theorem or missing final conclusion is supplied.',
  'proof sketched','root_computations.md §9: the relevant long-exact-sequence segment; missing hypotheses are explicit.','E','Long exact cohomology is standard; Stacks Tag01DZ identifies sheaf cohomology as a universal δ-functor. This does not establish the fragment’s geometric vanishing assumption.','Known before the manuscript.',['Stacks01DZ'],confidence='medium',event='targeted proof check',search=['root012','root030','root031'])
C(763,'B15-01',[170],'163-208','« VA à la Weil »; Hodge–Riemann and reduction to divisors',
  'The agenda seeks positivity and Hodge–Riemann-type structures, especially in odd weight, and suggests reducing positivity to divisor statements using blowups/flag varieties. It gives no complete reduction theorem or precise universal quantifiers. The standard conjecture of Hodge type, the abelian/divisor cases, and a hypothetical reduction of all higher codimension are kept distinct.',
  'open on the pages','No new reduction is performed; the proposal is not treated as a theorem.','C','Grothendieck’s standard-conjecture program is developed in his 1969 paper. Milne §2.47–2.48 distinguishes motivic polarizability from the stronger geometric algebraicity/positivity requirement. A universal divisor reduction is not established by these sources.','Grothendieck 1969; Milne manuscript1992/publication1994, corrected2019.',['Grothendieck1969','Milne1994Finite'],confidence='medium',search=['root013','root014','root015','root019'])
C(764,'B15-01',[170],'163-208','motivic fundamental group; « places arithmétiques » (uncertain)',
  'The page lists an extension of the motivic fundamental-group discussion and a relation with class field theory. Several nouns are uncertain and no exact extension, base field or quantifier is specified. It supports an agenda entry, not identification with a particular modern Galois-extension theorem.',
  'open on the pages','No formula with sufficient data to recompute.','F','General Tannakian/motivic class-field structures exist, but searches for the exact Deuring/motivic-place formulation did not identify a determinate theorem from this sentence.','Search recorded through2026-11-19.',['Milne1994Finite','Milne2012Dream'],confidence='low',search=['root013','root014','root015','root016'])
C(765,'B15-01',[170],'163-208','finite fields and positive/real-valued structures (uncertain wording)',
  'The finite-field agenda can be compared to a nonneutral category of pure motives with Frobenius, local fibre realizations and polarizations. This is a reconstruction of a research topic, not an exact theorem extracted from the uncertain words. In particular it cannot be read as asserting an ordinary real fibre functor for all motives.',
  'open on the pages','No numerical computation; compare the real quaternion obstruction CL-SA07-721.','C','Milne Theorems3.19–3.20 give precise classification results under axioms tied to the Tate conjecture. Their hypotheses and uniqueness levels cannot be removed.','Manuscript1992-10-16; published1994; corrected2019-11-02.',['Milne1994Finite'],confidence='medium',search=['root013','root014','root015','root018'])
C(766,'B15-01',[170],'163-208','« fonctions L », functional equations, « hypothèse de Riemann »',
  'The agenda names L-functions, functional equations and a Riemann hypothesis without a full formulation. For smooth projective varieties over F_q, the Frobenius-weight statement is now Deligne’s theorem. The unrestricted number-field motivic L-function program is a different, much broader question and is not settled by Weil I.',
  'open on the pages','No explicit L-function or functional equation appears on this leaf to recompute.','C','Deligne, Weil I, Theorem1.6 proves finite-field Frobenius weights q^(i/2), with integral ℓ-independent characteristic polynomials. Milne2012 §8 identifies the broader motivic L-function program; no global settlement is inferred.','Deligne Cambridge lectures July1973; publication1974. Milne lecture2009/version2012.',['Deligne1974WeilI','Milne2012Dream'],confidence='medium',search=['root013','root014','root016','root017'])
C(767,'B15-01',[170],'163-208','comparison of canonical lattices in Hodge and ℓ-adic realizations',
  'The agenda asks about comparison of integral structures across realizations. The leaf supplies no specified lattice, coefficient ring or canonical comparison map. Rational/adelic classification of fibre functors is not automatically an integral canonical-lattice theorem.',
  'open on the pages','No explicit lattice map to compute; related precise assertions are indexed from the Pro packages.','C','Milne1994 §3 concerns rational and adelic fibre-functor comparisons. It does not settle this unspecified integral comparison problem.','Published1994; corrected2019; exact fragment searched2026-11-19.',['Milne1994Finite'],confidence='medium',search=['root013','root014','root015','root018'])
C(768,'B15-01',[170],'163-208','« topologie sur Z » and uncertain auxiliary axioms/structures',
  'The remaining agenda labels involve a topology on Z and uncertain “practical/positive/p-adic” structures or axioms. There is insufficient data to select a topology, an axiom system, or a modern conjecture. These are retained as unidentifiable leads rather than expanded into invented problems.',
  'open on the pages','Not applicable: fragment contains no determinate formula.','F','Exact wording/topic searches and comparison with the opened motives surveys did not identify a precise claim. This is an identification limit, not evidence that no related theory exists.','Searched through2026-11-19.',['Milne2012Dream'],confidence='low',search=['root013','root014','root015','root016'])
C(769,'K15-02',[77],'368','« −1 … non carré … p≡−1 mod4 »',
  'For an odd prime p, −1 is a square in F_p exactly when p≡1 mod4; equivalently it is nonsquare exactly when p≡−1 mod4. Characteristic2 is excluded.',
  'stated without proof','root_computations.md §3: cyclic group criterion; root_computations_output.json gives sample residues, not a proof by sampling.','E','Elementary finite-field cyclicity; Conrad Lemma1.6 is the precise opened input.','Classical before the manuscript.',['ConradFiniteFields'],event='independent re-proof',search=['root007','root008'])
C(770,'B15-02',[27],'10-12','« principe général de prolongement analytique »; final hypothesis cut off',
  'The page begins a monodromy-style principle for compatible families of local solutions with uniqueness from a shared value, but the final condition and conclusion run off the supplied leaf. A complete global continuation theorem cannot be recovered from this fragment alone.',
  'stated without proof','No computation; the missing final hypothesis is not filled in.','F','Classical analytic continuation explains the setting, but does not identify the omitted theorem’s exact quantifiers. The fragment is retained as an incomplete formulation.','Classical context; incomplete statement as of2026-11-19.',['Lebl2026'],confidence='low',search=['root009','root010','root012'])

C(771,'B15-02',[35],'68','« il ne s’ensuit nullement … déformé … juxtaposition »',
  'The literal remark asserts that separately deformable path pieces need not have deformable concatenations. With unrestricted homotopy of interval maps this is false: H(t,s)=γ((1−s)t) contracts every path to its initial point, and the hypothesis places all relevant paths in the same path component. With endpoint-fixed individual homotopies concatenation is also valid. The narrower warning that two prescribed homotopies cannot be pasted unless their common endpoint tracks agree is valid (CL-SA07-742). A loop-preserving or prescribed-track interpretation would need an additional restriction absent from the supplied sentence.',
  'false as stated under the unrestricted path-homotopy reading','root_computations.md §5: explicit free-path contraction and endpoint-track distinction.','C','Classical homotopy theory; Hatcher §1.1 pp.25–26 treats fixed endpoints explicitly. The source’s missing definitional context prevents an unconditional allegation about the intended notion of deformation.','Classical before the manuscript; exact interpretation checked2026-11-19.',['Hatcher2002'],confidence='medium',event='refuted, with refined statement CL-SA07-742',outcome='Refutation is conditional on the literal free-path interpretation. The valid construction warning is labeled a reconstruction, and a scan/context alarm is retained.',search=['root030','root031','root032','root033'])

# Stage 3–5 records are appended before serialization.

def P(n,title,occ,as_he,today,art,why,worth,refs,cls):
    problems.append(dict(id=f'MP-SA07-{n:02d}',title=title,occurrences=occ,as_he_states=as_he,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs,claims=[f'CL-SA07-{x:03d}' for x in cls]))

P(301,'Recover the axioms of a “jolie” A-linear category',
 ['15/063, B15-01:56-69'],
 'The biconditional with a filtered union of strict monogenic projective-module subcategories is written with an inverse-direction question mark.',
 'If an additive idempotent-complete category is generated, on finite sets of objects, by their finite direct sums, each such additive envelope is modeled by finite projectives over an endomorphism ring; the exact manuscript category may require fewer objects.',
 'Morita projective-envelope theory is established (Abrams–Ruiz–Tomforde §1); it cannot identify the missing “jolie” axioms.',
 'The supplied fragment omits the definition and marks the converse with a question; no documentary explanation for later abandonment was found.',
 'Worth a short archival reconstruction only after adjoining the neighboring definitional leaves; not a new Morita theorem.',
 ['AbramsRuizTomforde2022'],[704])
P(302,'Localizability of an action category over Spec R',
 ['15/082, B15-01:111-127'],
 'The Spec A argument explicitly does not prove that Mod(R,C), for commutative R, is localizable over R.',
 'Specify the fibrewise stack of R-actions over R-opens and prove effective descent under a chosen base-change construction. Flatness alone repairs Hom, not lifting of all actions.',
 'Ferrand §1–2 verifies descent through torsors/bitorsors; CL-SA07-707 gives an exact nonflat obstruction and CL-SA07-708 the restricted repair.',
 'The page itself identifies a mismatch of bases; no source documents a later solution of this exact setup.',
 'Worth one focused run because a precise definition and counterexamples can delimit the strongest valid statement.',
 ['Ferrand2012'],[707,708,709])
P(303,'Canonical transport between Picard automorphism categories',
 ['15/036, K15-01:113-123','15/074–078, K15-02:236-407'],
 'A self-flagged “À vérifier!!” asks whether the two automorphism Picard categories of a bitorsor are canonically equivalent.',
 'Transport is canonical up to coherent isomorphism; after passage to a Picard band, commutativity kills inner conjugation. A strict unchosen functor is not implied.',
 'Ferrand Lemma1.1 and Proposition1.2 establish the bitorsor/band formulation; K15-02 then checks generator transport under commuting-ideal condition C.',
 'The doubt is local to coherence and choice; the later supplied pages partly answer it, so it is not an untouched open problem.',
 'Worth a short explanatory lemma in the folder commentary, with coherence conventions made explicit.',
 ['Ferrand2012','Voight2021Orders'],[713,727,728,729])
P(304,'Canonical norm object and integral Deuring comparison torsor',
 ['15/038, K15-01:129-164','15/044–050, K15-01:269-467'],
 'Assume an intrinsic norm object T can be attached to the equivalence class of C, then seek a canonical comparison construction independent of its representative.',
 'For a specified maximal-order category and norm/polarization datum, classify the groupoid of choices, identify its torsor class and residual automorphisms, and state exactly which pinning makes it neutral.',
 'Voight42.3.2 gives a Deuring equivalence after a base curve is fixed. Milne3.19–3.20 treats rational/adelic classification with explicit axioms, not the same integral norm object.',
 'The manuscript withdraws unique canonicity and introduces local choices and signs; no later exact publication was identified in the recorded Deuring/gerbe searches.',
 'Worth developing because the missing datum can be formulated as a concrete torsor problem, without claiming a choice-free answer.',
 ['Voight2021Supersingular','Milne1994Finite'],[714,717,720,722])
P(305,'The second sign in the Deuring 2-groupoid',
 ['15/048, K15-01:373-405','15/050–052, K15-01:417-517'],
 'The author explicitly asks whether another sign persists after arranging π₀=π₁=0 and π₂=Z/2.',
 'Model the structured equivalence 2-groupoid with its μ₂-band and compute the effect of fixing ξ_p and a real polarization comparison, retaining all 2-automorphisms.',
 'General bitorsor theory is available (Ferrand §2); nonneutral Tannakian uniqueness results of Milne are related but do not compute this exact sign.',
 'The surviving marginal instruction is the documentary evidence; no historical motive for leaving it unresolved is asserted.',
 'Worth a bounded coherence calculation after MP-SA07-304 fixes the objects and morphisms.',
 ['Ferrand2012','Milne1994Finite'],[720,721])
P(306,'A canonical algebraic closure from cyclotomic quotients',
 ['15/046, K15-01:358-365'],
 'Construct F_{p^n} as F_p[T]/Φ_{p^n−1} and then a compatible algebraic closure.',
 'Only the version using an irreducible factor, together with chosen compatible embeddings, is valid. Canonical algebraic closure without choice is not supplied by this recipe.',
 'Conrad1.1,1.10 give finite-field quotient presentations; this run’s p=2,n=3 factorization refutes the literal recipe.',
 'This is a false construction, not an unsolved existence theorem. No later withdrawal occurs in the supplied fragment.',
 'Not worth a research run; record the counterexample and examine the ink before editing the companion.',
 ['ConradFiniteFields'],[718,719])
P(307,'The unfinished question about o*',
 ['15/070, K15-02:124-125'],
 'The sentence asks whether o* is always equal to an expression that is not supplied.',
 'No strongest true formulation is recoverable until the missing continuation is found; do not substitute the nearby j-invariant criterion for the absent predicate.',
 'Voight18.4 and42.4 clarify the neighboring unit/normalizer/Frobenius questions, but do not identify the missing words.',
 'The obstacle is a truncated statement, not a known mathematical obstruction.',
 'Worth archival completion only; no conjecture should be assigned to this fragment yet.',
 ['Voight2021Orders','Voight2021Supersingular'],[724,725])
P(308,'Intrinsic recovery of the weight character and real involution',
 ['15/086, K15-02:460-480'],
 'Recover ε and j from the commutative algebra and its norm operations.',
 'Given a polarizable CM-type realization, separate the positive involution, the weight character, and the Hodge cocharacter; determine which data recover the others and list the residual choices.',
 'Milne CM1.39 classifies positive commutative involutions; §4 supplies the Mumford–Tate/Hodge setup. Neither alone proves an unqualified canonical recovery of all three data.',
 'The page gives an agenda note, without a completed argument; no further documentary explanation was located.',
 'Worth a small rank-one and CM-product analysis after correcting the missing totally real factors.',
 ['MilneCM2020'],[730,731,732,733])
P(309,'Extend the closed-form integral theorem to real C¹ coefficients',
 ['15/031, B15-02:41'],
 'The author asks whether presenting the continuously differentiable real version is worthwhile.',
 'A closed C¹ Banach-valued one-form on a simply connected real domain has a primitive, and its path integrals are homotopy invariant.',
 'The smooth Stokes theorem is LeblC.6; the elementary C¹ local-primitive and subdivision argument is checked in root_computations.md§5.',
 'The wording is an expository choice, not a stated unresolved theorem.',
 'Include a concise editorial note; no research program is needed.',
 ['Lebl2026'],[740,741])
P(310,'Homogeneous or exterior-form formulation of Frobenius',
 ['15/069, K15-02:44-79'],
 'A marginal note suggests a homogeneous/exterior-form version of the inhomogeneous PDE calculation.',
 'For a constant-rank C^r distribution (r≥1, analytic if desired) on an appropriate Banach manifold, the involutivity/integrability condition yields local integral manifolds under the standard complemented-subspace hypotheses; finite-dimensional analytic Pfaff systems are the immediate case.',
 'Penot1970 Theorem1.1 gives the local analytic/Banach PDE theorem and subsequent sections the distribution formulation.',
 'The supplied text suggests an extension of exposition; it is not evidence of a still-open Frobenius theorem.',
 'Worth a short translation of the coordinate calculation, with rank and complement hypotheses stated.',
 ['Penot1970'],[743,744])
P(311,'Dependence from an identically zero Jacobian',
 ['15/047, B15-02:211'],
 '“Il faudrait faire ici … le théorème de dépendance” for holomorphic functions with identically zero Jacobian.',
 'Near a point of maximal rank r, an analytic map factors locally through r analytic coordinates. A single global polynomial dependence statement is stronger and false without further hypotheses.',
 'The local theorem follows by the analytic inverse/implicit theorem (Lebl1.3.8); the fragment does not identify a global dependence category.',
 'It is left for exposition; missing qualifiers prevent a unique interpretation.',
 'Worth a precise local formulation in the analysis appendix, not an attribution of a modern global conjecture.',
 ['Lebl2026'],[758,759])
P(312,'Incomplete general continuation principle',
 ['15/027, B15-02:10-12'],
 'A system of local analytic solutions with equality-from-one-value is introduced, but its final hypothesis and conclusion are cut off.',
 'A monodromy theorem may be intended, but neither simply connectedness nor the exact continuation condition should be inserted as his words.',
 'Classical identity/continuation theory (Lebl1.2.7) explains only the surrounding context.',
 'The supplied leaf is incomplete; no historical explanation is inferred.',
 'Worth retrieving the missing continuation before any mathematical task is formulated.',
 ['Lebl2026'],[770])

agenda_occ=['15/170, B15-01:163-208']
P(313,'Weil-style positivity and odd-weight motives',agenda_occ,
 'Agenda point0 asks for “VA à la Weil”, odd weights and Hodge–Riemann-type structures; some wording is uncertain.',
 'Formulate positivity for a chosen pure-motive category and a polarization, distinguishing algebraicity of the Lefschetz inverse from positivity of primitive algebraic classes.',
 'Grothendieck1969 states the standard conjectures; Milne2.47–2.48 distinguishes the stronger geometric polarization assertion from abstract polarizability.',
 'The page is an agenda, not a proof; the sources do not explain why this particular note was left undeveloped.',
 'High interest but a few-hour run can only compare formulations and known cases, not solve the standard conjectures.',
 ['Grothendieck1969','Milne1994Finite'],[763])
P(314,'Motivic group extension by arithmetic places',agenda_occ,
 'Agenda point1 suggests an extension of the motivic fundamental group involving uncertain “places arithmétiques”.',
 'No exact extension can be stated from this leaf; recover the intended base, kernel and quotient from neighboring manuscripts before selecting a modern model.',
 'Milne1994§3 supplies a related nonneutral motivic framework, not an identification of this phrase.',
 'Uncertain nouns and absent definitions block exact identification.',
 'Worth an archival identification task only.',
 ['Milne1994Finite'],[764])
P(315,'Motivic structures and class field theory',agenda_occ,
 'Agenda point2 calls for relations with class field theory.',
 'In a specified CM or Artin–Tate subcategory, compare the abelianized motivic group and its reciprocity data; do not infer a universal reciprocity theorem from the heading.',
 'Milne CM§4 and Milne1994§4 give precise CM-motive structures and conditional reduction comparisons.',
 'The agenda contains no conjecture with quantifiers; no documentary reason for noncompletion was found.',
 'Worth narrowing to a particular CM example after recovering the intended object.',
 ['MilneCM2020','Milne1994Finite'],[764])
P(316,'Finite-field motives and real/positive structures',agenda_occ,
 'Agenda point3 names finite fields and an uncertain positive or real-valued structure.',
 'Use a nonneutral category with Frobenius, local fibre realizations and polarizations; a real two-dimensional realization of a supersingular h¹ is obstructed.',
 'Milne3.19–3.20 supplies conditional axiomatic classification; Voight42.1.9 supplies the quaternionic obstruction.',
 'The handwritten program predates these developments; an exact phrase-to-theorem match is not established.',
 'Worth a comparison of the archive’s intended real structure with the nonneutral model.',
 ['Milne1994Finite','Voight2021Supersingular'],[765,721])
P(317,'Canonical integral lattices across realizations',agenda_occ,
 'Agenda point4 asks for comparison of canonical lattices attached to Hodge and ℓ-adic realizations.',
 'For a specified motive with specified integral models, determine a comparison torsor and its stabilizer; rational comparison alone does not provide a canonical integral lattice.',
 'Milne1994§3 treats rational/adelic fibre-functor comparisons. The exact integral datum in this agenda is not specified.',
 'Missing integral conventions are the documented obstacle; no historical explanation is supplied.',
 'Worth a bounded test on Artin, Tate or CM motives, after matching the precise Pro-package lattice questions.',
 ['Milne1994Finite'],[767])
P(318,'Comparison with uncertain auxiliary axioms',agenda_occ,
 'Agenda point5 proposes a relation with other axioms whose names are uncertain in the transcription.',
 'No determinate mathematical problem is defensible until the ink and the referenced axioms are identified.',
 'Opened motives surveys supply context only; exact searches did not resolve the phrase.',
 'Reading and identification are incomplete, not a proven lack of later development.',
 'Worth a scan-led identification task, with no conjectural expansion now.',
 ['Milne2012Dream'],[768])
P(319,'Functional equations of motivic L-functions',agenda_occ,
 'Agenda point6 lists L-functions and functional equations, without the completed L-factor or base field.',
 'Specify a pure motive, local factors and archimedean normalization before asking for analytic continuation and the functional equation; finite-field zeta functions are a separate established case.',
 'DeligneWeilI1.6 settles finite-field weights; Milne2012§8 describes the broader motivic L-function program without claiming it solved.',
 'The leaf gives only a heading, and no later source explains this note’s fate.',
 'High conceptual interest; a few-hour run can produce an exact formulation and known-case table only.',
 ['Deligne1974WeilI','Milne2012Dream'],[766])
P(320,'Uncertain practical/positive/p-adic structures',agenda_occ,
 'Agenda point7 contains uncertain adjectives for additional structures.',
 'No precise modern theorem is assigned before the manuscript reading is resolved.',
 'The opened motivic surveys do not disambiguate the adjectives; recorded searches returned broad related topics only.',
 'The statement is not identifiable from the supplied transcription.',
 'An archival reading check is useful; a research task is premature.',
 ['Milne2012Dream'],[768])
P(321,'A topology on Z',agenda_occ,
 'Agenda point8 reads as a topology on Z, without a definition or required properties.',
 'Recover the intended object: the ordinary ring of integers, an integral group, and another Z-notation would lead to different problems.',
 'No exact match was identified in the recorded motives/Deuring searches; Milne2012 is context rather than a solution.',
 'The leaf supplies no construction or universal property.',
 'Worth a scan/context identification task only.',
 ['Milne2012Dream'],[768])
P(322,'Riemann hypothesis in the motivic agenda',agenda_occ,
 'Agenda point9 names a Riemann hypothesis, without specifying its scope.',
 'For smooth projective X/F_q the exact weight theorem is |α|=q^(i/2). A number-field Riemann hypothesis must be formulated separately and is not a consequence of that theorem.',
 'DeligneWeilI Theorem1.6, circulated in Cambridge lectures July1973 and published1974, proves the finite-field statement.',
 'The source gives no historical explanation for the note beyond its programmatic role.',
 'The finite-field comparison is worth documenting; no claim of solving a number-field hypothesis is justified.',
 ['Deligne1974WeilI'],[766])
P(323,'Reduce Hodge-type positivity to divisors by modifications',agenda_occ,
 'A marginal proposal mentions blowups/flag varieties to reduce the positivity problem to divisors.',
 'Test a precisely stated reduction that preserves the primitive algebraic pairing and all signs; the general higher-codimension standard conjecture cannot be assumed to follow from the divisor case.',
 'Grothendieck1969 formulates the general conjecture; Milne2.47 explains why a motivic polarization alone is weaker than the required algebraic construction.',
 'No completed reduction appears on the leaf and no exact general theorem was found in backward comparisons.',
 'Worth a small formal obstruction analysis; a short run cannot certify a general reduction without a new argument.',
 ['Grothendieck1969','Milne1994Finite'],[763])

def R(scan,line,reading,alternative,evidence,weight='high',confidence='high mathematical alarm; ink undecided'):
    readings.append(['15',scan,line,reading,alternative,evidence,weight,confidence])
R(59,'B15-01:7','Hom dans A','Hom dans C','The category is C; its Hom sets carry A-module structures.','medium')
R(59,'B15-01:35','End_C(X′) in generator parenthesis','End_C(X)','The same sentence defines o from the fixed generator X, not an unrelated X′.','medium')
R(63,'B15-01:56-69','jolie; raisonnables; inversement?','Recover exact defining adjectives and whether ? survives','The characterization cannot be tested without its closure axioms; no replacement is decided.','high','low lexical confidence; ink required')
R(64,'B15-01:75','second H','H′','The two angular components give opposite signs; repeating H contradicts the branch formulas.','medium')
R(81,'B15-01:87,94','R-linear category/actions where A is base','A-linear, if the letter is a misread A','Scalars for the category are introduced as A; R is only the acting algebra.','medium')
R(82,'B15-01:111','objets de R munis d’une opération R-linéaire','objets de C munis d’une opération R-linéaire','R is an algebra; Mod(R,C) has objects of C carrying R-actions.','medium')
R(82,'B15-01:118','arbitrary A-algebra A′ in the equivalence','Check whether a flatness restriction or fibrewise definition was omitted','CL-SA07-707 refutes arbitrary Hom base change; flatness alone does not repair every object-lifting issue.','high','high counterexample confidence; no proposed silent emendation')
R(34,'K15-01:38-41','représentations de degré n, de rang 1','de rang n, de poids 1 (candidate)','The preceding margin says degree n, weight1; rank1 would not produce the intended degree-n endomorphism algebra.','high','medium interpretation; ink required')
R(36,'K15-01:77','son π₁ before a π₀ exact sequence','π₀, if the heading is not a slip by the author','Automorphisms of the unit were μ_n; isomorphism classes appear in the displayed extension.','high')
R(40,'K15-01:172','ramifié seulement en 2 et∞','p et∞ (candidate; preserve possibility p=2 specialization)','Every following ideal/Frobenius calculation uses general p; a specialization to2 cannot be excluded without ink.','high','medium')
R(46,'K15-01:364','F_p[T]/Φ_{p^n−1} called F_{p^n}','Check whether “a factor” or a chosen maximal ideal was omitted','p=2,n=3 gives F8×F8; mathematics alone cannot decide whether this is ink, transcription or author error.','high')
R(70,'K15-02:104','quaternion algebra split at p and∞','ramified at p and∞ (candidate)','The adjacent supersingular division algebra and Frobenius ideal require the definite B_{p,∞}.','high')
R(70,'K15-02:112','j=0,1728 with unit orders4,6','j=0,1728 with orders6,4 for p>3','Aut(y²=x³−1) has6 elements, Aut(y²=x³−x) has4; characteristic2,3 need separate treatment.','high')
R(84,'K15-02:431-439','unitary group in A=End(E) called a torus','Check passage to the commutative image algebra B used on86','A general endomorphism algebra can have a noncommutative unitary group; the torus argument uses commutative B.','high','high hypothesis issue; ink undecided')
R(86,'K15-02:460-480','B product of CM fields','Check whether fixed totally real factors were excluded','B=Q with identity positive involution is a counterexample to the unqualified wording.','high','high hypothesis issue; no emendation decided')
R(29,'B15-02:25','B is introduced, then S⊂C and C open/closed','B in both later places','The polygonal-reachability proof refers to the same subset throughout.','low')
R(29,'B15-02:25','route d’origine A','route d’origine a','The fixed endpoint is a point a, not the entire domain A.','low')
R(33,'B15-02:55','(t−t_α)/(t_{α+1}−t)','(t−t_α)/(t_{α+1}−t_α)','Literal formula diverges at the endpoint; corrected affine interpolation reaches it.','high')
R(35,'B15-02:68','nonexistence of a homotopy between concatenations of separately deformable paths','Check for a loop-preserving condition, prescribed endpoint tracks, or a warning about the chosen homotopies only','CL-SA07-771: free paths in one path component are always homotopic, whereas pasting chosen homotopies requires equal intermediate endpoint tracks.','high','high conditional mathematics; intended definition and ink undecided')
R(39,'B15-02:110','U_jh in the mixed-partial condition','U_ih','The chain rule contracts the direction index i with the y-derivative; checked against15/069.','high')
R(41,'B15-02:147','M maximum on U×C','Check notation and an omitted bounded/compact smaller domain','A continuous function need not attain a finite maximum on an arbitrary open domain.','medium','mathematical qualification; lexical alternative uncertain')
R(43,'B15-02:155','ν_kj in μ_ℓ equation','ν_kjℓ','The parameter coordinate ℓ is needed to match the next displayed total-degree sum.','high')
R(43,'B15-02:162','U∈W','U×W','The solution variables range over a product of neighborhoods.','low')
R(45,'B15-02:194; K15-02:147-153','product factors h_i / H_i indexed over j','h_j / H_j','The substitution of y_j^r_j requires coefficients of the jth solution, not always the ith equation.','high')
R(47,'B15-02:215','one unique locally holomorphic solution on U×W over every complete valued field','Check whether “power-series germ” or a global series-on-disc condition was intended','Locally constant p-adic solutions give CL-SA07-747; no word is supplied from conjectured intent.','high')
R(49,'B15-03:21','sqrt(1−w)=Σbinom(1/2,n)v^n','Σbinom(1/2,n)(−w)^n','The binomial theorem requires both the correct variable and the minus sign.','high')
R(49,'B15-03:29','u_i≤w_i (alternative already unsure)','u_i=w_i','The following small-o uniqueness argument concludes equality, not an ordering over general K.','high')
R(51,'B15-03:49','Mt² before the geometric sum','Mr^(−2)t²','Exact f=z² counterexample with r=1/4; the bound M already includes r².','high')
R(53,'B15-03:67-74','weighted and unweighted series converge at the same radius','Check a missing smaller-radius qualification','a_n=(n+1)^−2 at r=1 becomes harmonic after multiplication by n+1.','high')
R(71,'K15-02:154-158','α sufficiently small for (1−αt)^−1 coefficient domination','α sufficiently large','The nth coefficient is α^n; increasing α controls a fixed exponential coefficient growth.','high')
R(71,'K15-02:133-158','real factor1/m in valued-field coefficient bound','|1/m|_K, with a revised majorant','For y′=1+y overQ2 the x² coefficient has norm2, not1/2.','high')
R(77,'K15-02:343-359','f_i with y_1,…,y_p where q unknowns were introduced','y_1,…,y_q','The implicit-function system has q dependent variables.','medium')
R(79,'K15-02:413-425','central binomial coefficient binom(2n,n) in sqrt expansion','binom(2n,n)/(2n−1)','Literal square has x² residual−8; generalized binomial identity supplies the candidate.','high')

def L(kind,frm,to,what,evidence,ids='Codex lead; no indexed verdict row'):
    links.append([kind,frm,to,what,evidence,ids])
L('folder','15/059 B15-01:3-35','15/072 K15-02:165-199','Strict generators and invertible-bimodule realization of admissible equivalences','Both passages read; first gives evaluation, second applies Morita transport under generic innerness.')
L('folder','15/081–082 B15-01:85-127','15/068 K15-02:3-34','Local forms and the Brandt/Picard action','Both endpoints read; related construction, not a claim of identical global hypotheses.')
L('folder','15/034–036 K15-01:5-123','15/074–078 K15-02:236-407','Picard commutativity and its explicit ideal-theoretic condition','Both endpoints read; the later condition C prevents an unconditional commutativity attribution.')
L('folder','15/044 K15-01:269-322','15/046 and050 K15-01:328-355;417-467','Withdrawal of canonical uniqueness, replaced by a sign and local choices','Both endpoints read, including deletions; CL-SA07-717.')
L('folder','15/048 K15-01:373-405','15/052 K15-01:477-517','Residual sign and the nonneutral real model gerbe','Both endpoints read; a model-gerbe equivalence is not a real fibre functor.')
L('folder','15/052 K15-01:477-517','15/207 MPL_15_195-228+18_002-017:259-261','Quaternionic obstruction to real neutralization','Codex endpoint read by root; Pro endpoint read by p15 and compared with its exact real-place assertion. Requires all relevant geometric endomorphisms.','MPL_15_195-228+18_002-017#15')
L('folder','15/039 B15-02:98-130','15/069 K15-02:44-79','Parallel Frobenius defect calculation','Both formulas read; index cancellation redone in root_computations.py.')
L('folder','15/043–045 B15-02:154-197','15/071 K15-02:133-158','Parallel formal ODE recursion and majorants','Both passages read; common component-index and valuation-factor issues flagged.')
L('folder','15/049 B15-03:7-34','15/077–079 K15-02:343-425','Implicit majorants and binomial square-root identity','Both endpoints read; quadratic solution valid, literal binomial coefficients require a scan check.')
L('folder','15/084 K15-02:431-439','15/086 K15-02:460-480','Endomorphism algebra A versus commutative generated algebra B','Both pages read; only the commutative algebra supports the compact-torus conclusion.')
L('folder','15/195,197,199,201,203,205 K15-08','same scans in MPL_15_195-228+18_002-017','Parallel diplomatic transcriptions of motivic comparisons, conjugation and Hodge-level questions','All K15-08 pages read by root and all corresponding Pro pages by p15; substantive claims remain in the Pro package, with no extra Codex verdicts.')
L('published work','15/085 K15-02:443-456','SGA4 VII Proposition4.1 and universe footnote','Big/small étale comparison','Both manuscript and exact retyped published proposition read; URL and edition details in SGA4VII bibliography record.')
L('published work','15/171 B15-01:215-227','BourbakiLie4to6 ChapterVI §4 Exercise2(a–c), pp.242–243','E₆ lattice Q/3P and finite orthogonal realization','Both endpoints read. Exact construction and group orders match; French1968/English2002 edition dates distinguished. Collective authorship does not prove personal attribution.')
L('published work','15/171 B15-01:229-238','BourbakiLie4to6 ChapterVI §4 Exercise3(a–c), p.243','E₇ lattice Q/2P and symplectic quotient','Both endpoints read. Exact quotient, kernel{±1} and determinant-one restriction match; no new claim of sole authorship.')


if __name__=='__main__':
    for name,rows in [('claims',claims),('problems',problems)]:
        (OUT/f'{name}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    for name,header,rows in [
        ('readings',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings),
        ('links',['kind','from','to','what','evidence','note_ids'],links),
        ('CHECK_EVENTS',['statement_id','date','who','type','outcome'],events)]:
        with (OUT/f'{name}.tsv').open('w',newline='') as f:
            w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
    print(json.dumps({'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links),'events':len(events)},indent=2))
