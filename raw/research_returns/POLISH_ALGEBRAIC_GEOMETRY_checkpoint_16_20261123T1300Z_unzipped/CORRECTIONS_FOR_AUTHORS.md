# Source corrections, known errata, and exact scope

No author has been contacted. Every item distinguishes a false assertion, a proof-step objection, a citation repair, and an already published correction. This dossier is excluded from all research papers.

## Record: workbench/records/paper_4/CORRECTIONS_FOR_AUTHORS.md

# EGA comparisons: already published corrections

Date: 2026-11-23. These are source comparisons, not new corrections to send to an author. No message has been sent. The main paper cites the known corrections briefly and does not present their examples as new theorems.

## Generic formal fibre: EGAIII4.3.6

The supplied French source at `latex_sources/EGA_FR/source/ega3/ega3-1-fr.tex`, Proposition4.3.6, contains the fraction-field identity in its argument. The supplied French EGAIII second-part errata, `source/ega3/ega3-7-fr.tex`, Liste2, partA, entry(III,4.3.6), explicitly replaces K'=K⊗_AÂ by K'⊃K⊗_AÂ; the entry follows the edition's oldpage218 marker. This correction was already printed in EGA's errata. Do not identify editionpage218 with journalpage91 without a separate pagination check.

A direct witness of strictness is A=k[x,y]_(x,y), Â=k[[x,y]], and g(x)=sum_{n≥1}x^{n!}, omitting repeated exponents if necessary. The series is transcendental over k(x): if a nonzero P(x,Y) of Y-degree d vanished on g, then for its polynomial truncations g_N, the order of P(x,g_N) would exceed its degree once (N+1)!>deg_x(P)+dN!, forcing P(x,g_N)=0 for infinitely many distinct g_N, impossible over k(x). Put f=y−g(x). The prime ideal (f) in Â has zero contraction to A, because P(x,g(x)) is nonzero for every nonzero polynomial P. Consequently f is not invertible in (A\{0})^{-1}Â=K⊗_AÂ, whereas 1/f belongs to Frac(Â)=K'. The example refutes the identity, not the unibranch conclusion. The unibranch repair is not independently certified in this note.

## Meromorphic denominators: EGAIV20.1.3

Primary known correction: Steven L. Kleiman, *Misconceptions about K_X*, Enseign. Math. (2)25 (1979),203–206, DOI10.5169/seals-50379, official PDF https://www.e-periodica.ch/cntmng?bot=1&pid=ens-001:1979:25::101 . The PDF was opened through the provider's advertised crawler link and read. A separate byte download returned429, so no fabricated SHA-256 is recorded for it.

On p203 Kleiman gives exactly the family from which the proposed first example is obtained: take a domain A, a maximal ideal M, P^1_A and its closed fibre Y, and the square-zero ideal O_Y(−1). With A=k[t] and M=(t), global sections of the thickening are k[t] because H0(P1_k,O(−1))=0. Thus t is a nonzerodivisor on the global section ring. On an affine open meeting the closed fibre, its product with a nonzero square-zero section is zero. Restriction therefore does not preserve global nonzerodivisors. This is an exact specialization of Kleiman's published example, not an independent new counterexample.

On p204 Kleiman gives the square-zero ring B⊕bigoplus_{M⊃p}B/M, with p a nonzero nonmaximal prime that is the intersection of the maximal ideals containing it. Take B=k[x,y], p=(x), and k algebraically closed; the summands are B/(x,y−a), a∈k. At the point p the square-zero summands vanish after localization, so the local ring is B_p and its total quotient ring is k(x,y). The stalk of the meromorphic sheaf is B_p itself: a denominator regular on a neighborhood of p cannot be divisible by x, because such a neighborhood contains closed points of the line x=0 with surviving square-zero sections annihilated by x. Thus its image in B_p is a unit. In particular1/x is missing from the meromorphic stalk. This too is Kleiman's exact construction, specialized to an affine plane.

## Stacks comparison

Opened current primary pages: https://stacks.math.columbia.edu/tag/01X1 (meromorphic functions), https://stacks.math.columbia.edu/tag/01WY (regular sections), https://stacks.math.columbia.edu/tag/0EMG (meromorphic functions in the noetherian case), and https://stacks.math.columbia.edu/tag/01X3 (related example). The sheaf is localized at sections regular on all stalks, not merely nonzerodivisors of a global section ring. The noetherian theorem identifies the meromorphic stalk with the total quotient ring under its exact hypotheses; Kleiman's second example is nonnoetherian. This distinction prevents a false contradiction with the noetherian repair.

## Withdrawn lifting proposition

EGA0_IV19.3.12 is different: EGAIV fourth part, Err_IV8, p347, deletes it because the displayed spaces of lifts are not linear varieties. The new paper gives a proof of the same assertion by using linear compactness only for square-zero kernels. This restores a withdrawn assertion; it is not presented as a newly found false statement of EGA. The exact original hypotheses include openness of the square of every open ideal of the source, and that hypothesis is retained.

## Supplementary Paper1 search: existing Esnault–Kindler erratum

The author PDF of *Lefschetz theorems for tamely ramified coverings*, Proc. Amer. Math. Soc.144 (2016),5071–5080, Theorem6.1, omits the requirement that the curve be a complete intersection of ample divisors. Reading it in this run exposed that omission: for example a vertical P1 in a product of an elliptic curve and P1 cannot detect a nontrivial étale isogeny on the first factor. Before classifying this as a possible new error, a targeted search found the authors' **already issued erratum dated29September2016**. The erratum was opened and read at `https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf`; it restores exactly the missing hypothesis. The corrected theorem is sufficient for the boundary argument. This is recorded only to prevent reuse of the incomplete statement. No new correction, author-contact draft, or message is warranted. See BOUNDARY_LITERATURE.md for the source comparison.

## Possible minor Stacks copy correction: Tag07BV

Observed on23November2026 at `https://stacks.math.columbia.edu/tag/07BV`, Lemma10.158.11. The proof chooses a transcendence basis x_1,...,x_d and algebraic generators y_1,...,y_r. In the sentence declaring the P_i regular and presenting L, two occurrences of k(x_1,...,x_r) should read k(x_1,...,x_d). The preceding and following sentences use d correctly. A literal check with L=k(t), d=1 and r=0 makes the typo visible: the erroneous field would become k rather than k(t). This is a notation slip; the theorem and its proof mechanism are unaffected. The current tag page displayed no comments on that lemma; no exhaustive issue-history search was performed, so prior reporting is unknown. Suggested replacement: change r to d in those two rational-function-field subscripts. No comment or message has been sent, and this correction is not included in the paper.


## Possible new proof correction: Popescu2022, Section4

While comparing the arithmetic tower with Sever Angel Popescu, *Infinite algebraic extensions of Dedekind structures*, Math. Reports24(74)(2022),505–512, I noticed a false intermediate assertion in the proof of Theorem2, pp.510–511. The source is https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/3/14.pdf , SHA25630510243519fe67cb4676ab7eea3eddb6d650db198916e816f011e15b6b6141b. The argument introduces a selected family F of valuations in an infinite Galois extension and its enlargement F* to all conjugate prolongations. It asserts that the selected and full intersections are “simultaneously Dedekind domains”, and that finite selected fibres imply finite full fibres. The following explicit counterexample disproves those intermediate assertions; it does not disprove the stated Theorem2, which is the earlier valid valuation criterion.

Take D=Z_(3), K=Q, and choose infinitely many distinct rational primes q_i≡1(mod3). Set L=Q(sqrt(q_i):i≥1). Independence of the rational square classes makes L/K an infinite multiquadratic Galois extension. Each q_i is a square in Q_3 by Hensel's lemma, so every finite subextension has3 completely split. Choose one embedding L→Q_3 and let V=L∩Z_3. Its value group is Z because it is a subgroup of v_3(Q_3^×)=Z and contains v_3(3)=1. Thus V is a DVR, with fraction field L.

Put F={V}. Its intersection A=V is Dedekind and has exactly one selected valuation over(3). The enlarged intersection A* is the integral closure of D in L. The prime(3) has at least2^n distinct prolongations already in Q(sqrt(q_1),...,sqrt(q_n)); each prolongs to L by integrality, so A* has infinitely many maximal ideals containing3. A nonzero element of a Dedekind domain belongs to only finitely many maximal ideals. Hence A* is not Dedekind and the full fibre F* over(3) is infinite.

The invalid inference is that finite generation of a maximal ideal in A implies finite generation of its contraction in A*: A is not finite over A*, and contraction does not preserve that property. Theorem2 can instead use the earlier Popescu–Vraciu1985 theorem directly (or its finite-character proof). This has no effect on the Section5 eventual-inertness example used as literature context, and no correction is inserted into any paper. This counterexample was derived by paper_4 from the primary text on23November2026,03:00UTC. Root subsequently completed a full targeted second check against the primary passage and a limited title/author erratum search at03:20UTC; see records/ROOT_CORRECTIONS.md. The argument passed; no erratum was located in that limited search. No claim of exhaustive prior-reporting search is made. No author contact or public posting has occurred.


## Record: workbench/records/papers_2_3/CORRECTIONS_FOR_AUTHORS.md

# Current status update — 23 November 2026, 03:35 UTC

The ordinary all-Artinian flatness and explicit first-order Albanese-fibration obstruction have now received the full targeted geometric check. Chai’s exact target primary text was opened through indexed official retrieval; Katz, GIT, Partsch and Chai–Oort inputs were checked. See ../igusa_corrections/FULL_CHECK.md, SOURCE_ACCESS.json and COMPUTATION.json. The supersingular extension and miniversal/algebraization claims are not certified by that check. The earlier entries below record the narrower state before this update and do not remain the current gate. No author has been contacted.

# Corrections and objections under examination

Date: 2026-11-23. These records are not letters and have not been sent to anyone. They are excluded from the papers. A precise objection to a proof step is distinguished from a verified counterexample to the theorem.

## Nonsmooth torsors and tangent dimensions

Source target: Ching-Li Chai, *Mumford's example of non-flat Pic-tau*, Theorem2.4(iii), pp6--7, and Remark(1), p7, according to the attached report. Both official author PDF URLs (mumford_ex.pdf and mumford_ex_v2.pdf) were tried in this run and returned403; the current-run primary opening of that exact text is therefore **not complete**. The related published conclusion in Chai--Oort, *Life and Work of Alexander Grothendieck*, Notices ICCM5(1)(2017), section3.9(iv), printed p35, was opened at https://research-portal.uu.nl/ws/portalfiles/portal/254168358/Life_and_Work_of_Alexander_Grothendieck.pdf, PDF page15 including repository cover. It asserts nonflatness for the universal first-order equicharacteristic deformation of an Igusa surface.

Verified elementary objection. Over an algebraically closed field k of characteristic2, let R=k[e1,e2,e3,e4]/(ei ej for all i,j), and let P=Spec R[z]/(z^2-e1). It is finite free rank2. With u=1+z it is the Kummer torsor u^2=1+e1 under mu2; adjoining a root of a unit gives a faithfully flat torsor even in characteristic2. Its cotangent space has basis z,e2,e3,e4 because e1=z^2, hence dimension4. The trivial torsor mu2_R has cotangent dimension5. The tangent map for P has image de1=0; the trivial torsor's tangent map is surjective. Product with a smooth elliptic curve gives dimensions5 and6, while preserving the torsor. No R-point exists, since every principal unit in R has square1. Thus neither unequal absolute tangent dimensions, unequal tangent-map ranks, nor absence of an R-point excludes a flat torsor under a nonsmooth group.

Status: the algebraic objection is proved in this run. It is not by itself a refutation of the cited geometric nonflatness claim. The attached report's complete ordinary-Igusa calculation is located at source/ours/RESEARCH_SA14_SA19/sections/D.tex:454--659 (D4o); its Serre--Tate source dependencies still require current-run verification before certifying that stronger correction.

## An etale-to-connected infinitesimal map

Opened source: H. Partsch, *Deformations of elliptic fiber bundles in positive characteristic*, Nagoya Math.J.211(2013),79--108, DOI10.1215/00277630-2141608, publisher PDF https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B95794564B38C458B5571618768725E9/S0027763000010795a.pdf/deformations_of_elliptic_fiber_bundles_in_positive_characteristic.pdf. Exact targets: Proposition6.6 pp102--103, final paragraph of proof p103; Theorem6.7 p104; Proposition6.9 p106.

The last trace argument on p103 passes from killing connected parts to a statement about an etale quotient. The following obstruction prevents an inference based only on etaleness of the source. For R=k[epsilon]/epsilon^2 in characteristic2 there is a nonzero homomorphism (Z/2)_R -> mu2_R sending1 to1+epsilon. The identity (1+epsilon)^2=1 verifies the group law; its special fibre is zero. Therefore a morphism from an etale group to an infinitesimal connected target is not determined by its special fibre.

Status: this finite-group objection is proved. A current-run certification that the geometric lifting assertions themselves are false awaits the full audit of the explicit deformation D4a and the argument D4b, source/ours/RESEARCH_SA14_SA19/sections/D.tex:1040--1218. No claim about other cases of Partsch's classification is made.

## Abelian torsors are not all components of the unchanged dual Picard scheme

Date: 2026-11-23, about06:36UTC. Source: Jeffrey D. Achter and Sebastian Casalaina-Martin, *Putting the P back in Prym*, author PDF dated18December2024, §1.7.2, printed/PDF p13, final two paragraphs. Primary URL: https://www.math.colostate.edu/~achter/math/prym1224.pdf . Exact fetched file: tmp/e4_continuation/Achter_Casalaina_Martin_prym.pdf, 484143 bytes, SHA256 9f6800c822c19c6d93d92bdbedeed7f5090891ef042ba66af9fbe00d3570ec90. The standing base convention at §1, p3 is a connected locally noetherian scheme. The adjacent §1.7.1 is on p12. Agent p_fresh and root have both read these exact pages.

**Precise claim under objection.** The end of §1.7.2 asserts that a torsor T under an abelian scheme X can be identified with a component of Pic_{X∨/S}; if a global Poincaré line bundle is unavailable, it proposes making an étale base change and descending the same conclusion. The following example refutes this last assertion even over the real field. It does not refute the canonical equality Pic^0_{T/S}=X∨, nor the schematicity assertion at the beginning of that subsection.

**Explicit counterexample.** Let

C={y²+x⁴+z⁴=0} ⊂ P_R(1,1,2),

where x,z have weight1 and y has weight2. The weighted-projective singular point x=z=0 does not lie on C. The two charts x≠0 and z≠0 cover C, and there the equation has the form v²+u⁴+1=0. Its two partial derivatives, 2v and4u³, cannot vanish simultaneously on the curve. Thus C is smooth over R. The map C→P¹_R given by [x:z] is finite of degree2. Over C it is branched at the four distinct zeros of x⁴+z⁴; this also makes the double cover geometrically connected, since the defining rational function is not a square. Riemann–Hurwitz gives 2g(C)-2=2(-2)+4=0, so C has genus1.

No real point exists. Any real point maps to a real point of P¹; choosing x=1 or z=1 would give v²=-(u⁴+1), which has no real solution. Let E=Pic^0_{C/R}. Then E is an elliptic curve with its rational identity, and C is its nontrivial scheme torsor. The principal polarization identifies E∨ with E. The connected components of Pic_{E/R} are Pic^d_{E/R}, d∈Z; each contains the real point represented by O_E(d·0). If C were isomorphic over R to any component of Pic_{E∨/R}, it would have a real point, a contradiction.

**What fails in the proposed descent step.** A local Poincaré construction depends on trivializing the torsor. Changing that trivialization changes the induced map by translation. Its target descent datum must be twisted as well. Descending the source torsor does not give an isomorphism into an unchanged component of Pic of the dual. The correct full-Picard construction is the contracted product Pic_{X/S}×^X T (Raynaud's identity, also printed as Alexeev Theorem3.0.3, p664), with the translation action explicitly retained.

**Status.** The explicit real counterexample and the failed descent inference have been independently checked by root and p_fresh. The first-paragraph full-Picard schematicity assertion is a located precedent and is not claimed as a new theorem in this run. This correction is kept outside the manuscript; no author has been contacted. No claim is made about the other results of the source.


## Record: workbench/records/igusa_corrections/FULL_CHECK.md

# Ordinary Igusa deformations: full targeted check of the correction

Date: 23 November 2026, 03:35 UTC. Checker: GPT-6 Astra, root of this run, inherited reasoning setting. This is a complete targeted proof check after exposure to the supplied argument, not a fresh statement-only reconstruction. It supersedes the earlier current-run gate on the ordinary flatness and explicit Albanese-fibration obstruction. It does not certify the separate supersingular calculation, the miniversal hull, or formal algebraization.

These observations belong only to the correction dossier. No message has been sent to an author. No priority claim is made.

## 1. Exact claims and opened sources

Chai, *Mumford's example of non-flat Pic-tau*, Theorem 2.4(iii), printed p. 6, asserts nonflatness of the torsion Picard scheme of the universal first-order equicharacteristic deformation when both elliptic factors are ordinary. The final argument and Remark (1) are on p. 7. The two official PDF addresses returned HTTP 403 to direct downloading, but the web retrieval subsequently opened the indexed primary text, including the complete target theorem, proof ending, and remark. This is a primary-text opening, not a downloaded or visually inspected PDF. Its PDF byte hash is unavailable.

Chai–Oort, *Life and Work of Alexander Grothendieck*, Notices ICCM 5(1) (2017), §3.9(iv), printed p. 35, repeats the first-order nonflatness assertion. Its primary PDF was downloaded, the complete relevant text read, and printed p. 35 visually inspected. The ordinary case below is already enough to refute that unqualified assertion.

Partsch, *Deformations of elliptic fiber bundles in positive characteristic*, Nagoya Math. J. 211 (2013), 79–108, Proposition 6.6 pp. 102–103, Theorem 6.7 p. 104, and Proposition 6.9 p. 106, assert the stated universal lifting of the elliptic/Albanese fibrations. The publisher PDF was opened and the target statements and proof read. Printed pp. 102–104 were also visually inspected. The objection below concerns these universal assertions, not every case of the article's classification.

The source URLs and available SHA-256 hashes are in SOURCE_ACCESS.json. The source-run proof is in ours/RESEARCH_SA14_SA19/sections/D.tex, D4o and D4a–D4b. The proof below states all steps needed for the correction; it does not require the source-run proof as a mathematical input.

## 2. Every Artinian deformation in the ordinary case has flat Pic-tau

Let k be algebraically closed of characteristic 2, let E0 and F0 be ordinary elliptic curves, and choose a nonzero P in F0[2](k). Write

\[
A_0=E_0\times F_0,\quad \sigma_0=(-1,1),\quad
\tau_0=t_{(0,P)}\sigma_0,\quad X_0=A_0/\langle\tau_0\rangle.
\]

Let R be any local Artinian W(k)-algebra with residue field k and let X/R be a smooth proper deformation of X0. We prove that Pic-tau(X/R) is flat over R.

### The cover is an abelian deformation

The finite étale double cover A0→X0 and its deck action lift uniquely over X. This is topological invariance of finite étale covers under nilpotent immersions; Stacks, §59.45, Tag 04DY, was opened. The lifted A/R is smooth and proper. Smoothness over the Artinian local base lifts the origin to a section.

Mumford–Fogarty, *Geometric Invariant Theory*, second edition, Proposition 6.15, pp. 124–126, equips A with its abelian scheme structure by successive small extensions. The complete statement was opened in the primary-book text: it assumes smooth properness, a section, and an abelian structure on the reduction. Theorem 6.14 is an alternative once projectivity is established. For completeness, choose an ample line bundle on A0. Across a small extension with kernel annihilated by the maximal ideal, the obstruction to lifting a line bundle lies in H²(O) tensored with that kernel and is killed by 2. Its square therefore lifts. Repeating this finitely many times lifts a power of the original ample bundle. Ampleness across a nilpotent thickening is EGA II, Proposition 4.5.13, checked in the attached French LaTeX. Thus A is projective.

Write its deck map as τ=t_cσ, where c=τ(0) and σ fixes the origin. Rigidity makes σ a group automorphism, and uniqueness of lifting a homomorphism gives σ²=1. The equation τ²=1 becomes (1+σ)c=0.

### The translation equation kills one off-diagonal parameter

Choose étale 2-adic Tate bases e1,e2 of A0 and e1-dual,e2-dual of its dual, with e2/2=P. Katz, *Serre–Tate local moduli*, Theorem 2.1(1),(3),(4), pp. 148–149, classifies abelian deformations by the bilinear pairing

\[
q_{ij}=q_A(e_i,e_j^\vee)\in1+\mathfrak m_R,
\]

identifies duality with transposition, and characterizes lifting homomorphisms by compatibility of the pairings. The exact statements and the construction on pp. 150–152 were read, and all five pages inspected.

Applying the morphism criterion to σ0 gives q12²=q21²=1. The formal group of A is canonically the torus Hom(T2(A0-dual), Gm-hat); σ acts on its coordinates by (z1,z2)↦(z1^{-1},z2).

Choose compatible points Pn in F0[2^{n+1}](k) with 2^n Pn=P. For n sufficiently large, multiplication by 2^n kills the formal group on the maximal ideal of R. For any lift of Pn to A(R), set c0=[2^n]Pn-tilde. Changes of lift lie in the killed formal group. Compatibility of the Pn shows independence of sufficiently large n. The same reasoning shows σc0=c0.

Katz's pushout recovery, pp. 151–152, now gives

\[
[2]c_0=(q_{21},q_{22}).
\]

Indeed doubling c0 applies the recovery homomorphism to the Tate generator e2. This checks the row convention directly, without assuming that a point lifts through a torsion isogeny.

Every lift of (0,P) has the form c=c0+z with z=(z1,z2) in the formal torus. Consequently

\[
(1+\sigma)c=(q_{21},\,q_{22}z_2^2).
\]

The involution equation forces q21=1 and q22 z2²=1. Only q21=1 will be needed for flatness.

### The fixed subgroup of the dual is flat

Let E-dual and F-dual be the elliptic deformations with diagonal parameters q11 and q22. Applying Katz's criterion to the original inclusion and projection, using transposition and q21=1, gives an exact sequence

\[
0\longrightarrow E^\vee\longrightarrow A^\vee
  \xrightarrow{\rho}F^\vee\longrightarrow0.
\]

To justify exactness beyond the special fibre: the projection is smooth by the fibrewise smoothness criterion for the two smooth R-schemes; its kernel is a smooth proper relative elliptic curve. The lifted inclusion maps into this kernel, and its reduction is an isomorphism. It is therefore an isomorphism, by the fibrewise criterion for morphisms of smooth proper schemes over this Artinian base. Compositions vanish by rigidity. The automorphism σ-dual acts by −1 on the kernel and by +1 on the quotient.

Put G=ker(1−σ-dual) in A-dual. Given a section b of F-dual, lift it fppf locally to a section a of A-dual. The error (1−σ-dual)a lies in E-dual. Multiplication by 2 on the elliptic scheme is finite faithfully flat, so this error has a half h fppf locally. Then a−h is fixed. The kernel of G→F-dual is E-dual[2]. Thus

\[
0\longrightarrow E^\vee[2]\longrightarrow G
  \longrightarrow F^\vee\longrightarrow0
\]

is exact as a sequence of fppf sheaves. It makes G→F-dual a torsor under the finite locally free rank-four group E-dual[2]. In particular G is flat over R.

### Descent identifies the torsion Picard scheme

Pullback along π:A→X gives

\[
0\longrightarrow\mu_2\longrightarrow
\operatorname{Pic}^{\tau}_{X/R}\longrightarrow G\longrightarrow0
\]

as fppf sheaves. Here is the full surjectivity argument. A section of G is, fppf locally on the test scheme T, represented by a line bundle L on A_T. Translation acts trivially on A-dual, so its class is invariant under τ. Trivializing the possible line bundle from T gives an isomorphism α:τ*L→L. The composite α∘τ*α is a base unit, because A is an abelian scheme and its global functions are universally the functions of the base. Adjoining a square root of that unit is a finite faithfully flat extension. After rescaling α, the cocycle equation holds, and finite étale descent produces a line bundle D on X_T.

The norm identity gives D²=Nm(L) as relative Picard classes. Fibrewise the norm carries the connected abelian variety A-dual into the neutral Picard component of X, so D is in Pic-tau. Conversely a Pic-tau class pulls back into A-dual: the Néron–Severi group of an abelian variety has no torsion. These statements characterize the respective open subgroup functors after every base change.

Finally, linearizations of the trivial line bundle are exactly the characters of the constant group C2, namely μ2. This is the asserted kernel; effectiveness and faithfulness are statements of line-bundle descent, not statements only about geometric points.

The morphism Pic-tau(X/R)→G is consequently a μ2-torsor, finite locally free of rank two. Its composition with G→F-dual is finite locally free of rank eight. Since F-dual is flat over R, Pic-tau(X/R) is flat over R.

This proves the contrary of Chai Theorem 2.4(iii) in its ordinary setting, and disproves the universal assertion in Chai–Oort §3.9(iv). No calculation of a versal hull is needed.

## 3. The explicit first-order deformation does not lift its Albanese fibration

Take R=k[ε]/ε² and choose the ordinary abelian deformation with

\[
(q_{ij})=\begin{pmatrix}1&1+\epsilon\\1&1\end{pmatrix}.
\]

Katz's classification supplies A/R. The off-diagonal squares are 1, so σ lifts. In the preceding translation calculation take z1=z2=1. Both involution equations hold, giving τ. Its fixed locus has empty special fibre and hence is empty over the Artinian base. The free constant-group quotient exists as a scheme by Stacks, Lemma 66.14.2, Tag 07S7, whose hypotheses were checked. It is smooth and proper by étale descent, and projective by descending an invariant ample line bundle. Thus X=A/C2 is a smooth projective deformation, with the flat Pic-tau just proved.

Set Y0=F0/⟨P⟩ and let φ:F0→Y0 be the étale 2-isogeny. The morphism X0→Y0 has a section induced by {0}×F0 and is the Albanese elliptic fibration. The special-fibre reduced neutral Picard group is Y0-dual; under pullback to A0-dual its inclusion is

\[
f_0=(0,\phi^\vee):Y_0^\vee\longrightarrow E_0^\vee\times F_0^\vee.
\]

This identification is also in the opened Chai–Oort §3.9(iii), p. 35; it follows directly from pullback on the quotient fibration.

Suppose an abelian scheme B/R admitted a homomorphism to Pic-tau(X/R) whose reduction was this Picard-variety inclusion. Compose with π*. The composite lands in A-dual because it does so on the special fibre and the Artinian thickening has the same underlying topological space. We obtain f:B→A-dual lifting f0.

The kernel of φ-dual is μ2, so φ-dual induces an isomorphism on the étale Tate modules. Choose x in T2(Y0-dual) mapping to eF-dual. The dual map f0-dual=(0,φ) kills eE. Katz's necessary condition for lifting f0, evaluated at x and eE, is

\[
q_B(x,0)=q_{A^\vee}(e_F^\vee,e_E).
\]

The left side is 1 and the right side, by transposition, is qA(eE,eF-dual)=1+ε. This contradiction holds for every possible deformation B, independently of its own parameter. Therefore no such abelian homomorphism exists.

If the Albanese fibration lifted to a smooth proper genus-one curve C/R, pullback from the elliptic abelian scheme Pic0(C/R) would be exactly such a homomorphism, with the required reduction. It follows that the fibration does not lift. This refutes the indicated universal assertions of Partsch.

For a fully specified special fibre, one may use two copies of y²+xy=x³+1 over F2-bar and P=(0,1). Inversion is (x,y)↦(x,y+x), so P has order two. The affine singularity equations force x=0 and y=0, which is not on the curve; the point at infinity is smooth. The coefficient of xy is nonzero, so the elliptic curve is ordinary.

## 4. The precise inference errors remain separate

The flat μ2-torsor Spec R[z]/(z²−e1) over R=k[e1,e2,e3,e4]/(ei ej) has absolute tangent dimension four, while μ2_R has dimension five. Taking a product with a smooth elliptic curve gives the dimensions five and six used in Chai's argument. The tangent images in the base differ too. The torsor is finite free of rank two and has no R-point. Hence those tangent differences and failure of lifting a section do not imply nonflatness or factorization through a proper closed base subscheme.

For the final trace inference in Partsch p. 103, the nonzero homomorphism (Z/2)_R→μ2_R given by 1↦1+ε has zero special fibre. Étaleness of the source alone does not imply the required rigidity. This finite-group observation does not substitute for the geometric counterexample in §3.

All three supplied finite certificates were rerun successfully in disposable copies. The new program check_igusa_correction_matrices.py repeats the relevant arithmetic through regular-representation matrices and Gaussian elimination. Its output, source hashes, and precise computational scope are in COMPUTATION.json. Neither computation is presented as a certification of the geometric proof.

## 5. Scope of the current check

Current verdict: the ordinary all-Artinian flatness proof, the explicit first-order incompatibility, the Albanese-fibration nonlifting, and the two elementary inference objections pass a complete targeted check. The stronger supersingular/all-Igusa claim is not certified here. The miniversal hull and algebraization assertions of the source run are not used or certified by this check. The pre-existing first-order incompatibility in FGA, Exp. VI, Remark 3.4 is credited; no novelty claim is made for it. The exact ordinary flatness correction has not been given an independent fresh-worker reconstruction in this run and is not a main theorem of any paper.


## Record: workbench/records/ROOT_CORRECTIONS.md

# Additional source corrections checked by root

Date:23November2026. GPT-6 Astra, inherited reasoning settings; effort
metadata not exposed. No human has checked these arguments. No message,
issue, comment or author contact has been sent. These observations remain
outside every research paper. Prior reporting is not claimed to be excluded.

## Popescu2022: the selected/full valuation-family inference

Primary source: S.A.Popescu, *Infinite algebraic extensions of Dedekind
structures*, Math.Reports24(74)(2022),505–512, section4,pp510–511.
URL:https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/3/14.pdf .
SHA256:30510243519fe67cb4676ab7eea3eddb6d650db198916e816f011e15b6b6141b.
Root read the complete relevant primary passage and compared the following
argument with paper_4's construction. This is a full targeted second check,
not an additional statement-only reproof claim.

The disputed step enlarges an arbitrary selected family F of prolongations
to the family F* of all conjugate prolongations and asserts that their
intersections A and A* are simultaneously Dedekind, and that selected and
full fibres are simultaneously finite. Both implications from selected to
full fail.

Let D=Z_(3). Choose distinct rational primes q_i congruent to1 modulo3 and
put K_n=Q(sqrt(q_1),...,sqrt(q_n)), L=union K_n. The q_i have independent
classes in Q*/Q*²: in a product of distinct q_i, each occurring prime has
odd valuation. Therefore [K_n:Q]=2^n and L/Q is Galois. Each polynomial
X²−q_i has two distinct roots modulo3; Hensel's lemma lifts both roots to
Q_3. Consequently K_n embeds in Q_3, compatibly for all n, and3 splits
completely in K_n. Fix such a compatible embedding and set V=L∩Z_3.

The restricted3-adic valuation has value group exactly Z: it is contained
in Z and takes value1 on3. Its nonnegative ring V is a DVR with uniformizer3.
Every x in L becomes an element of V after multiplication by a power of3,
so Frac(V)=L. Its residue field is F_3. Thus F={V} is an admissible selected
family; A=V is Dedekind and the selected fibre above(3) has one element.

The full intersection A* is the integral closure of D in L. There are2^n
distinct primes above3 in the integral closure of D in K_n. Each extends
to a prime of A* by lying over, and distinct contractions remain distinct.
Thus A* has infinitely many maximal ideals containing3. A nonzero principal
ideal in a Dedekind domain has only finitely many prime divisors; since3 is
nonzero and noninvertible, A* cannot be Dedekind. This also directly shows
that the full valuation fibre is infinite. All the valuation rings in the
full family are nevertheless DVRs, so the source's separate discreteness
assertion is not contradicted.

The proof's inference from finite generation of a prime in A to finite
generation of its contraction in A* is invalid for this nonfinite overring.
The stated selected-family criterion of Theorem2 is not refuted: the
Popescu–Vraciu1985 criterion already proves it. Section5's eventual-inertness
example is also unaffected. Searches for the exact title with “erratum” and
“correction”, and for the author's name plus those terms, returned the
official paper and issue page but no correction on23November2026. This
limited negative search is not proof that the issue is unreported.

## Stacks0BTP: an fppf citation used for an fpqc step

Primary current page:https://stacks.math.columbia.edu/tag/0BTP ,
Proposition41.20.6, proof paragraph beginning with the henselization A^h.
It invokes More on Morphisms, Lemma37.57.1 to justify fpqc descent for
separated etale morphisms. That lemma is Tag02W8,
https://stacks.math.columbia.edu/tag/02W8 , and its statement and proof
assume an fppf cover; its openness argument explicitly uses finite
presentation. The henselization cover in the cited step need not be of
finite presentation.

The desired descent statement is true. Replace that reference by
Tag0AP9, Lemma37.66.8 (a separated locally quasi-finite morphism is
ind-quasi-affine), followed by Gabber's Tag0APK, Lemma40.15.3
(effective descent for ind-quasi-affine morphisms under arbitrary fpqc
covers). These prove exactly the needed separated-etale assertion.
This is a citation repair, not a counterexample to Proposition41.20.6.
All four primary statements/proofs were opened and compared. Their byte
hashes and addresses are in ROOT_CORRECTION_SOURCE_RETRIEVAL.json. The
0BTP page showed no comments; an exhaustive issue-history audit is not
asserted. No paper uses the insufficient reference as its fpqc input.
# Numerical entries in the abelian-surface table of Liedtke's author version

Date: 2026-11-23. This concerns the author preprint, not an assertion that
the published chapter has the same entries. No author has been contacted.

Source: C. Liedtke, Algebraic surfaces in positive characteristic,
arXiv:0912.4291v4, printed p.27, section 7.1, displayed table of invariants.
URL: https://arxiv.org/pdf/0912.4291v4 .
SHA-256: 17309a48dad424540f3f25e1e0cb35e898c3e7f79d7f5bb8aab20ec32f6c1776.
The page was opened as PDF bytes and visually inspected.

The table gives chi(O_S)=1 and b2=2 for abelian surfaces. The correct values
are 0 and 6. An explicit check uses S=E times E for any elliptic curve over
an algebraically closed field, with an auxiliary prime ell different from
the characteristic. Coherent Kunneth gives (h0(O),h1(O),h2(O))=(1,2,1), so
chi(O)=1-2+1=0. Etale Kunneth gives
b2(S)=b2(E)b0(E)+b1(E)b1(E)+b0(E)b2(E)=1+4+1=6.
More generally the exterior-algebra description of the cohomology of an
abelian variety gives these values for every abelian surface.

The c2=0 entry used in the surface obstruction is correct. No correction
to its classification argument is needed. A bounded search for a Liedtke
surface-survey erratum did not locate one; that search does not establish
that the typographical errors have never been noted. The published chapter
was verified bibliographically but its typeset table was not opened, so
the correction is confined to this exact author version.


# An incompatible premise in Cotner–Zavyalov Example3.4.6(ii)

This is a clarification of a vacuous conditional, not a counterexample to its implication. In *Lefschetz theorems in flat cohomology and applications*, Example3.4.6(ii) and its footnote6, the proposed pair also satisfies Example3.3.6. The latter requires H1(V,O(-D)) nonzero; the former adds smoothness of D and an isomorphism H0(Omega1_V)->H0(Omega1_D). Those hypotheses cannot coexist over the stated perfect field. Frobenius iteration gives a nonzero alpha_p-torsor trivial on D, and differentiating its local equations gives a nonzero global1-form restricting to zero on D. The complete proof, exact source URLs, author-page locators12–13and18, byte hash, and same-model targeted-check scope are in ROOT_DIFFERENTIAL_PICARD_EXCLUSION.md. The published primary HTML and the full author page18 were opened. Example3.4.6(i) and the general Picard-point question are unaffected. No author has been contacted.

### Provenance clarification for the differential Picard exclusion

The same source-premise exclusion was already present in the attached A-CZ346ii (label a:cz-vacuity). The current ROOT:Picard-differential-exclusion gives its explicit negative-cohomology corollary and a fresh targeted proof/source check, not a newly discovered correction. The inherited general functorial alpha_p proposition has now also been read and checked in full.


### Published-version locator confirmation — 23 November2026,07:43UTC

The Cambridge published PDF has now also been retrieved and read directly: Example3.3.6 is on printedp1862; Example3.4.6 and its full proof are onpp1867–1868, with footnote6 onp1867. Root read those complete extracted passages after the separate worker located them. They agree with the previously inspected primary HTML and author text; this is a source-locator extension of the same correction, not a new correction or a new mathematical result. Published PDF URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8556201EDB51D7F2F76F5950A800CD64/S0010437X24007231a.pdf/lefschetz_theorems_in_flat_cohomology_and_applications.pdf . Bytes987695; SHA2564c6c3263ff5a77636d5771b8fedbfac91e2153f0b5fd67ce9339ece55a44f5a1. The PDF and its extraction remain outside the deliverable. No author was contacted.


# Two interchanged Euler-characteristic subscripts in a canonical-bundle proof

Inspected source: F.Cossec, I.Dolgachev and C.Liedtke, *Enriques Surfaces I*, author-hosted version dated19April2024, proof of Theorem4.1.6, printedp366 (physicalPDFp382), first two displayed lines. URL https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf . SHA2563c6bf1d54954e28728935bbe1f4b1e38435fe469cf2b8543d657087815a2f526;3483048bytes. Root read the extracted passage and visually inspected the full printedpp365–366 on23November2026. This correction is confined to those bytes; no claim is made about a later printing or errata list.

Write R¹f_*O_X=L⊕T as in the source. In the first display onp366, the middle expression must be h⁰(T)+deg L+χ(O_C), whereas the printed expression has χ(O_X). The following conclusion must be deg L=−χ(O_X)−h⁰(T), whereas the printed expression has χ(O_C). Theorem4.1.6(1), printedp365, already states the correct conclusion.

Proof of the repair: on the smooth base curve, Riemann–Roch gives χ(L)=deg L+χ(O_C), and a torsion sheaf has χ(T)=h⁰(T). Leray and f_*O_X=O_C give χ(R¹f_*O_X)=χ(O_C)−χ(O_X). Cancelling χ(O_C) gives the correct formula. For an explicit counterexample to the two literal displays, take X=E×P¹ with E an elliptic curve and f the second projection. Then L=O_{P¹},T=0,deg L=0,χ(O_X)=0 andχ(O_C)=1. The erroneous middle expression is0 instead of1, and the erroneous final expression gives degree−1 instead of0.

These are typographical errors in the proof, not a refutation of the canonical-bundle theorem. The current quasi-elliptic route calculation rederives the correct identity from Leray. This source correction stays in the dossier and is not a new-paper result. No author has been contacted.


## Record: workbench/records/ROOT_SOURCE_CORRECTIONS_09.md

# Source corrections checked during the ninth-hour continuation

Date: 23 November 2026. These are dossier-only source corrections. No author has been contacted, and neither correction is presented as a result in a research paper.

## Milne, Abelian varieties, Remark 8.5: a nonsplit p-torsion group scheme

**Exact claim and editions.** The remark asserts that the group scheme A[p] over an algebraically closed field is a product of r copies of Z/p, s copies of mu_p, and t copies of alpha_p, with r+s+t=2g (and r=s). This product assertion is false; the preceding assertions that A[p] is finite of length p^(2g) and killed by p are unaffected.

The inspected author revision is J. S. Milne, *Abelian Varieties*, dated 2 January 2022, Remark 8.5, printed/PDF p.14, https://www.jmilne.org/math/xnotes/AVs.pdf . It has 575,091 bytes and SHA-256 `bffdf81c57c77420b5454b31270007989d12f332abea62424be15c424079fc7c`. A fresh official-host fetch at 09:17:30 gave the same hash. The original chapter in *Arithmetic Geometry*, Springer, 1986, pp.103–150, has the same assertion in Remark 8.5 at printed pp.116–117: https://jmilne.org/math/articles/1986b.pdf , 3,833,583 bytes, SHA-256 `86259344a576e4ef75a9d81e9bf43143f872a72b14cf8fcc2703f3aea6349136`. Root visually checked the current page and both original pages. This is not an OCR inference.

**Counterexample with complete short proof.** Over k=algebraic closure of F_2, let E be the plane cubic

\[
Y^2Z+YZ^2=X^3,\qquad O=[0:1:0].
\]

The partial derivatives are X², Z² and Y², with no common projective zero. The cubic is smooth and integral, and has genus one, so (E,O) is an elliptic curve. On its affine part, inversion is (x,y)↦(x,y+1): the vertical line has the two indicated intersections and O. No affine point equals its inverse, so E[2](k)={O}. If the asserted product decomposition held, r=0. Its length is four, so s+t=2. But each factor mu_2 or alpha_2 has one-dimensional tangent space at the identity, giving a two-dimensional tangent space for that product. In contrast,

\[
\operatorname{Lie}(E[2])=\ker(d[2]:\operatorname{Lie}E\to\operatorname{Lie}E)
=\operatorname{Lie}E
\]

has dimension one, since d[2]=0 in characteristic two. This contradiction requires no classification of finite group schemes.

There is also an explicit underlying-scheme calculation. The tangent line at (x,y) is v=x²u+y². Its intersection polynomial factors as

\[
u^3+x^4u^2+x^2u+x^6=(u+x)^2(u+x^4).
\]

The third intersection is (x⁴,y⁴), so [2](x,y)=(x⁴,y⁴+1). Homogeneously this is [X:Y:Z]↦[X⁴:Y⁴+Z⁴:Z⁴]. At O put t=X/Y and w=Z/Y, with w+w²=t³ and ord_t(w)=3. Then [2]*t=t⁴/(1+w⁴). Thus E[2] is supported at O with completed local ring k[[t]]/(t⁴), and hence underlying finite scheme Spec k[t]/(t⁴). The proposed connected product has local ring k[u,v]/(u²,v²), with embedding dimension two. No assertion that the Hopf algebra is that of alpha_4 is made.

**Repair and verification scope.** Delete the product decomposition, or replace it by a statement that does not assert splitting. A description by appropriate filtrations is different from the asserted direct product. The valid length and annihilation statements may remain. More generally, the product hypothesis together with Lie(A[p]) of dimension g and r=s would force the ordinary case r=g, s=g, t=0, which already shows why it cannot cover supersingular elliptic curves.

The separate worker was given only the target locator and suspicion, not the counterexample; it independently derived the same example, tangent-space contradiction and explicit doubling calculation. Its full 168-line proof was frozen before root comparison and then read entirely by root: `papers_2_3/MILNE_AV_REMARK_8_5_CORRECTION.md`, SHA-256 `595a092220270a4bcad40d9728855fe3479f7b4b0da8e28dccb7011f4b1f09b7`. Root independently checked the group law, local parameter and tangent argument. This is a same-model independent derivation of a targeted counterexample, not a new discovery claim.

The worker searched the official author errata page and the linked Barthel and Tiwari lists in their relevant full scopes; no matching correction was located in that bounded search. Exact URLs, hashes, failures and reading scope are in `MILNE_AV_REMARK_8_5_SOURCE_RECEIPTS.json`. Prior reporting is not exhaustively settled. The paper's use of Milne is confined to the translation/Picard facts in Section 9 and Proposition 10.1, and is unaffected.

## Ekedahl, Canonical models, p.112: two omitted inverse signs

**Exact source.** T. Ekedahl, *Canonical models of surfaces of general type in positive characteristic*, Publ. Math. IHES 67 (1988), 97–144, DOI https://doi.org/10.1007/BF02699128 ; https://www.numdam.org/article/PMIHES_1988__67__97_0.pdf . Inspected PDF: 6,025,593 bytes, SHA-256 `0e53d89911bd563cdc5e8a38abc47dc4e990a75e77cbd05055812f6d63b30776`. The error is in the first paragraph of printed p.112, in the proof of I.2.4(ii)(d), where the alpha-torsor line bundle is denoted mathcal N. Root and the separate auditor visually checked the displayed formulas at high resolution.

To avoid confusing this line bundle with the covering surface, call it A and write beta:V→X for the finite flat purely inseparable double cover. The paragraph prints beta*A isomorphic to beta*omega_X, followed by A² isomorphic to omega_X². Both right sides need inverse powers. The correct formulas are

\[
\beta^*A\simeq\beta^*\omega_X^{-1},\qquad
A^{\otimes2}\simeq\omega_X^{\otimes(-2)}.
\]

**Complete repair.** The article's own Proposition I.1.7, formula (1.9), printed p.107, gives omega_V=beta*(omega_X tensor A) in characteristic two. At this point of the proof the resolution is K3 and V has rational double points, so omega_V is trivial. The first corrected identity follows. For finite flat beta of degree two, taking the norm of beta*(A tensor omega_X)=O gives (A tensor omega_X)^2=O, which is the second identity. The preceding page's foliation identity L=A^{-2} tensor omega_X^{-1} then gives L=omega_X, exactly the conclusion correctly stated in I.2.4(d). The printed positive powers would not give this conclusion.

This is a proof-formula typo, not a counterexample to I.2.4 or to its present application. Root read the entire statement and proof on pp.109–115 and the referred II.1.7 proof on pp.126–127; the separate auditor did the same before freezing its report. The complete audit is `a3_a2_ekedahl_audit/AUDIT.md`, SHA-256 `fbc12fb946cc733601c22fbb28afc9331a3df0e199ac3f35787a97f7c8a8dafd`. Its Section 8 gives the same repair. The theorem, numerical bounds, and identification of the Kummer normalization remain valid. This dossier does not claim an exhaustive audit of the article or a priority determination. A bounded official errata search is being recorded separately; its completion must not be inferred from this entry.

## Supplement completion —09:44UTC

Root read the full new Milne formal-secant computation report and its entire Python implementation, then reran the standard-library program successfully. It derives [2](t)=t^4+t^16+t^40+O(t^64) from two independent formal points before diagonal specialization; the method differs from tangent factorization. The local kernel and putative connected product both have length4, with embedding dimensions1 and2 respectively. Exact output agrees with the frozen worker receipt. This computation does not replace the separate proof of smoothness and global support.

Root also read the complete EKEDAHL_P112_OFFICIAL_ERRATA_SEARCH.md. Its bounded checks of Numdam, Springer, the original issue and two search engines found no matching official erratum; the failed DOI route and unproductive author-search link are recorded explicitly. No priority inference is made. Both supplements were frozen09:35:52 in MILNE_EKEDAHL_SUPPLEMENT_FROZEN.json, SHA25691ecd36a03db11d9c83c53879761746bfba64ad66dfb4af5f5481e207df2f804. Earlier freezes remain unchanged.
# FGA Exposé 221, Lemma 3.5: an already published correction

Additional check, 23 November 2026, 10:37 UTC. This is a known author correction, not a new result or a newly discovered error.

Root read the attached French Exposé 221, printed pp.259–267, including the full proof of Theorems 3.1–3.2 and the quasiprojective Hilbert variant. In the proof of Lemma 3.5 on printed p.263 (original exposé p.15), the sentence at local lines707–709 says that distinct eventual rank and comparison polynomials imply eventual emptiness of the rank-bound open sets. That intermediate assertion is too strong: for S=Spec k, the graded module k[t] has constant graded rank Q=1, whereas P=2 gives every such open equal to S. The stationarity lemma and Hilbert representability are unaffected.

The exact repair is already in Grothendieck's *Erratum à l'exposé n°221*, Séminaire Bourbaki 7 (1961/62), p.302, at the corrections to original p.15 lines13 and15. It replaces inequality of polynomials by eventual strict order P<Q, and handles the other case by eventual P(n)≥Q(n). For the first case the rank condition eventually fails everywhere; in the other case all sufficiently late inequalities hold everywhere and only finitely many earlier conditions remain. Together with the finite flattening stratification in the original proof, this gives the asserted stationarity.

Root read the complete attached e221.tex, not a scan. Source221.tex SHA256: 2485e1297c5aff1346ce7dcb031d5637778a974b47532a13de19a034d9754ee7. Erratum e221.tex SHA256: ba1f156eea41e72646b75c956d6caf2482cedabea46911278588e1d7e103075a. The official bibliographic record is https://numdam.org/item/SB_1961-1962__7__302_1/ . Both search engines were queried for the exposé, lemma and errata; the official author erratum was located and checked in the required attached edition. No source copy or extraction is included in the deliverable, and no author contact occurred. The second unsuccessful normal-bundle attempt's conditional Hilbert arguments use this corrected known theorem; their main NOT PROVED verdict remains unchanged.



## Record: workbench/records/ROOT_SOURCE_CORRECTIONS_10.md

# Source correction checked on 23 November 2026

## Stacks Tag0AGS: reversed quotient in the proof diagram, theorem unchanged

Source: The Stacks Project, Lemma54.3.4, Tag0AGS, proof of part(4), the two-row diagram immediately after the exact sequence for O_X(n), O_X(n-1), and O_E(n-1).
Official page: https://stacks.math.columbia.edu/tag/0AGS
Official history: https://stacks.math.columbia.edu/tag/0AGS/history

The top row has successive terms m^max(0,n) and m^max(0,n-1), in that order, but prints their quotient in the same order. Since the first ideal is contained in the second, the displayed quotient reverses the required numerator and denominator. It must be m^max(0,n-1)/m^max(0,n). Already n=1 would otherwise ask for m/A instead of A/m. The corrected row is the usual exact ideal-inclusion sequence.

For n positive, the corrected quotient is m^(n-1)/m^n, identified by the associated graded ring of a two-dimensional regular local ring with the degree-(n-1) homogeneous polynomials in two variables. Its dimension is n, exactly H0(P1,O(n-1)). For n nonpositive both terms are A and the quotient is zero. This restores the claimed right vertical isomorphism and descending-induction proof. The statement of Lemma54.3.4 is not refuted. The almost-ruled proof uses the separate regularity lemma54.3.2, so it does not depend on this misprinted quotient.

Root read the entire current proof and the complete displayed tag history. The history lists a2015spelling edit and the2014creation/tag assignment; it shows no later mathematical quotient correction. Root also searched `"Stacks" "0AGS" quotient typo` and `"54.3.4" "quotient" correction` with the complementary engine. No separate correction was identified in that bounded search. This does not establish that nobody previously noticed or reported it. No author or maintainer was contacted.

Cached official page:19359bytes, SHA256111f550496dac0318506f1d5171f275443bf5a69faf0065d46667a9bcdd4ef35.
Cached official history:7797bytes, SHA25647eb26a5bf7482e33f2fc56e97ef10a0dd678fb9171bacf2756728621b7adff1.
The broader official0AGPsection previously cached for the proof has31167bytes, SHA256ad20185fbfa9644c5d6eb26db7df9eaf6a54a71881293453840f417a0a5cc705.
Only this original correction note and source metadata belong to the deliverables; all downloaded source bytes remain outside them. This correction is not counted as mathematical movement on any research gate.

## Attached EGA edition: composition order in IV8.10.5(xii)

Identifier: ROOT:EGA8105-attached-composition-order. Status: exact notation correction in the supplied LaTeX edition only. The printed scan was not consulted, and no attribution to the published original or novelty claim is made.

Locator: EGA IV3, proof of8.10.5, case(xii), following Proposition8.10.5.1, printed-page marker40; attached `source/latex_sources/EGA_FR/source/ega4/ega4-8-fr.tex`, lines2948–2954. Full source-file SHA2567908d23b23da054a54baba8bf1b5fb5dd13b056307bc014ee41cce8fb579d2cc. The exposed auditor reported the notation; root read the entire relevant Chow proposition, its proof and case(xii) at lines2895–2962 and checked the domains and codomains.

The diagram has j_lambda:X'_lambda→P_lambda, p_lambda:P_lambda→S_lambda, g_lambda:X'_lambda→X_lambda, and f_lambda:X_lambda→S_lambda. The valid commutative equality is f_lambda composed with g_lambda = p_lambda composed with j_lambda. The attached display reverses the two factors on the right. They are not composable in that order. Restoring their diagram order gives the proper composite used by the ensuing descent argument. The theorem and its use in the paper are unchanged. No author has been contacted; no manuscript correction claim is inserted into a paper.

## Attached EGA edition: cocycle composition order in IV8.5.2(ii)

Identifier: ROOT:EGA852-attached-cocycle-order. This is a notation finding in the attached LaTeX edition only. Root read the whole applied proof, including the delayed part(ii), at lines1248–1605 of the same file and SHA256 given above. No printed scan was consulted, no claim about that unread edition or priority is made, and no author has been contacted.

The maps at lines1448–1459 are explicitly directed theta_ij:F_i→F_j. On triple overlaps the displayed compositions at lines1468 and1473 therefore have their factors reversed. The composable cocycle is theta_jk composed with theta_ij = theta_ik, and the pulled-back equality at the finite stage must use the same order. This follows by checking the domains and codomains: F_i→F_j→F_k. The finite-presentation argument descending the equality is unchanged. Theorem8.5.2 is not refuted, and the line-bundle descent in our proof uses the correctly ordered cocycle. This edition-only correction stays in the dossier and does not count as mathematical movement.


## Stacks 54.12 case-I ambient projective space (23 November2026)

Classification: typographical dimension error, not a false rational-double-point theorem. Exact locator: Section54.12, Tag0BGB, paragraph “Resolution in case I”, display immediately after q(t1,t2,t3)=q(t2,t3). Official URL https://stacks.math.columbia.edu/tag/0BGB . Retrieved HTML SHA256ad46f92798507936c3aa5ae03a0c38bf13491cc5cf78fc3939570e2c576b2909; extracted-text SHA256c1f978849efdfa3a19f9b6ebf962ecbdd3bd49c31ad8e835ebe55e43ee40e410. Root and separate audit read the complete section, including both resolution cases and footnotes.

The displayed exceptional conic is placed in P^1. It must be placed in P^2: the preceding calculation uses three homogeneous coordinates, the chart has two affine coordinates, and the following description is a union of two lines meeting at the singular point (or the nonsplit analogue). The zero locus of a nonzero homogeneous quadratic in P^1 is zero-dimensional and cannot have that description. Replace only the ambient superscript1 by2. The proof's preceding rational-Gorenstein multiplicity calculation and subsequent intended conic geometry are unchanged. No author has been contacted; no claim is made about an uninspected historical version.


## Record: workbench/records/papers_5_6/CORRECTIONS_FOR_AUTHORS.md

# Corrections and definition repairs found during the current check

Date: 2026-11-23. Checker: GPT-6 Astra, ChatGPT Pro mode; inherited effort not separately exposed. These are source-comparison observations, not research-paper claims and not messages sent to the author.

## Milne, Gerbes and Abelian Motives (author version 1.1, 21 February 2003), p. 23

Source: https://www.jmilne.org/math/articles/2003b.pdf. SHA-256: b1e841b7447ffc46587aea3e1e8ff7bb00fc5bd1001572113dff1e4a40bac743. The displayed definition of a Weil p^n-number on p. 23 specifies the complex absolute values but omits integrality after multiplication by a power of p. The omission matters if the displayed definition is read literally, because equation (26) on the same page uses injectivity of the valuation/weight map.

Counterexample to the literal definition followed by that injectivity: take p=2, K=Q(i), and u=(3+4i)/5. Both complex conjugates have absolute value 1, so the displayed absolute-value condition holds with weight zero. The numerator has norm 25, and the denominator is 5; u is a unit at every prime over 2. Hence its normalized 2-adic valuation function and its weight are both zero. But u is not a root of unity: u+u^{-1}=6/5 is not an algebraic integer, whereas the sum of a root of unity and its inverse is integral. Therefore its class survives every power transition of the direct limit, and it is a nonzero germ mapped to zero by the advertised valuation/weight injection. The algebraic identities are independently recomputed in scalar_identities.py, output SCALAR_IDENTITIES.json; the integrality argument is the proof.

Repair and prior occurrence: add that p^N u is integral for some integer N. This is already explicit in Milne, Motives over finite fields, Definition 2.5(b), corrected author text p. 13, https://www.jmilne.org/math/xnotes/Seattle1.pdf, SHA-256 4344a61cb7c3a6525b520754afa40c08dc138bfaf736931e104b042dfa5b4548. It excludes the example. The intended protorus can also be specified directly by the finite-level exact sequence (26). The comparison note uses this complete definition and makes no claim of a new repair theorem.

The same p. 23 transition display prints its target as W(p^{nn'}) while indexing n|n' and mapping a to a^{n'/n}. The compatible target is W(p^{n'}). For example n=2,n'=4,a=p has weight one at level p^2, whereas a^2=p^2 would have weight one-half at the printed level p^8. This is a typographical target-index error; the subsequent direct-limit construction determines the intended transition.

No claim is made that either observation is previously unreported. The full current corrected author materials beyond the versions cited have not been exhaustively searched for an erratum.

## Archive locator correction (not an author's mathematical error)

The task's label “letter of cote 14, sheet 38” merges two different items. Direct visual examination of https://grothendieck.umontpellier.fr/14.pdf shows Theorem 3.1 on archive sheet 37, its continuation on sheet 38, and the letter to Serre dated 27 August 1965 beginning on sheet 43, with Conjecture A there, Conjecture B on sheet 44, and finite-generation consequences on sheet 45. PDF page numbers are one greater. This is recorded as a locator correction and used in paper05 §1. Source SHA and retrieval details are in COTE14_RETRIEVAL.md.

## Literature-scope correction for E.3q (not an error attributed to Bloch or Srinivas)

The surface-support theorem identified as Bloch–Srinivas Theorem1(ii) by the opened Fu–Tian Remark2 concerns integral codimension-two Griffiths-group vanishing. It is not, by that citation alone, the integral quotient by Albanese equivalence asserted in E3q. The latter combines the diagonal factorization with the whole Walker-kernel divisibility theorem, credited to Suzuki in ACMV Theorem2.3, and Saito's codimension-two comparison. BS_SOURCE_COMPARISON.md records the opened exact inputs and proof audit. The original1983 full text and its actual printed-page locator remain unverified; no author error or novelty claim is inferred. Paper05 does not assert E3q as a main theorem, so its final TeX/PDF required no change.

## Small notation issue in the downloaded Voisin book manuscript

In the author manuscript dated 3September2013, printed p.41/PDF p.49, the explanatory paragraph after Theorem3.14 says that CH²(X)/alg is torsion under surface support. The intended group in that sentence is CH²(X)_hom/alg: the theorem concerns the Griffiths group, and the next-page proof begins with a homologically trivial cycle. The unrestricted group cannot be torsion, since the square of an ample divisor has nonzero rational cohomology. The theorem itself has the correct scope. This observation concerns only the opened prepublication version (URL and SHA in BS_COMPARISON_SOURCE_HASHES.json); the published edition and any erratum were not checked, and no claim of a previously unreported correction is made.
