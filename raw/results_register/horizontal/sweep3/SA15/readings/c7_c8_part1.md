# SA15, cote 7 (scans 1-72): stratified modules, the lectures of November-December 1966 on de Rham and p-adic cohomology, and the Čech computations

Claude Opus 5.5 at effort max (SA15-c7_c8-part1, sweep 3 reader), 18 Nov 2026, about 23:30 UTC. Launched by the SA15
c7_c8 reader (Claude Opus 5.5 at effort max) under agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max). Brief:
`sweep3/READER_BRIEF.md`. Companion files: `c7_c8_part1_CHECK_EVENTS.tsv` (26 events), `c7_c8_part1_CORRECTIONS.tsv`
(20 rows). What sweep 3 already did on SA15 (cotes 4, 6, 100) is in `sweep3/SA15/STUDY.md` and is not repeated here.

**Read:** all 70 transcribed pages, in full: scans 1, 3-19 and 21-60 from package `MPL_6_038-067+7_001-060`, scans 61-72
from `MPL_7_061-072+8_001-078` (first pass by GPT-6 Astra, ChatGPT Pro mode, 12 and 13 Nov). Scans 2 and 20 are blank
(DROPPED_SCANS_CHECK_20261112 rows 42-43). Ink checked on the scan images: 7:3 (date, heading insertion), 7:7, 7:17,
7:18, 7:21, 7:24, 7:36, 7:41, and the leaves 7:5, 7:6, 7:58, 7:59 and 7:15-19 for ink colour.

## 0. What the cote is

Three layers, in three inks, filed in reverse order of writing:

1. **The lectures of November-December 1966** (7:21-72, mostly blue ink). Pencil heading on 7:21: "Nov. Déc. 196-", the
   last digit corrected in red to 6 over a 7. Dated sheets: 7:36 "15.11.66" (first digit overwritten), 7:57
   "6.12.1966" (the date is drawn inside a margin figure in the Pro .tex). A plan on 7:60 lists eight paragraphs: §1 de
   Rham, §2 the l-adic theories and the wish for a p-adic one, §3 Washnitzer-Monsky, §4 stratifications and Gauss-Manin,
   §5 the crystalline and stratifying sites with a theorem and a conjecture in characteristic 0, §6 Čech computations
   (any characteristic), §7 comparison of de Rham and crystalline cohomology in characteristic 0, §8 back to
   characteristic p. The pages hold §1-§3 (7:21-35, his pages 1-15), a fresh start on 15 Nov (7:36-53: W-M, then
   Gauss-Manin), "§4 Topos stratifiant et topos cristallin" (7:54-56), a "Laïus" of 6 Dec (7:57-58), and §6 (7:60-72;
   7:68 is a struck start). This is the preparation of his IHÉS lectures written up by J. Coates and O. Jussila as
   "Crystals and the de Rham cohomology of schemes" (Dix exposés sur la cohomologie des schémas, 1968) (locator
   unverified; Michel Hua's project makes the same identification).
2. **"Anneaux simpliciaux canoniques et modules stratifiés"** (7:3-16 and the displaced leaf 7:59; black and brown ink),
   sections 1-6. Pencil date on 7:3: "Juillet-Août 1967" (checked; the third digit is barely formed, Michel Hua's project
   reads 1967 "par élimination").
3. **A blue layer**: the bracket inserted under the title on 7:3, the margin bubble and the "Remarque" on 7:16, and the
   pages "§ - Commentaires sur la définition d'une cohomologie p-adique en car. p > 0" (7:17-19).

**Reading order for an edition:** 7:3, 7:4, 7:5, **7:59**, 7:6, ..., 7:16 (the leaf 7:59, archive sheet 58, is a page
of the black text: same ink and paper, and the sentences run on at both joins, check event 7:59). The Pro notes and
Michel Hua's project read 7:59 as part of the 6 Dec 1966 lecture; that is wrong.

**Dating.** What the pages fix: the blue layer comes after the lectures, because 7:17 takes "d'après l'exposé précédent"
the limit over W_n and the independence of the lift, which are 6.3 of the lectures (7:65-66); and it comes after the
black text, whose doubt (7:16) it answers. Whether the black text is from summer 1967 (as the pencil says) or summer 1966
(before the lectures) the pages do not decide: the pencil dates were added afterwards and the one on 7:21 was first
wrong by a year in the same direction. See H1-1.

**Words.** On cote 7 "site cristallin" is the site of nilpotent thickenings **without divided powers** (7:55), and "site
stratifiant" its variant whose objects carry a map to X (7:60: "la restriction sur les objets du site stratifiant par
rapport à ceux du site cristallin"). In today's terms both are infinitesimal sites. An edition must say so: read with
Berthelot's divided-power site in mind, 7:17 would look false.

## 1. 7:1 - cover (SA15-12)

The IMAG cover sheet (Institut Montpelliérain Alexander Grothendieck). No content.

## 2. 7:3-16 and 7:59 - "Anneaux simpliciaux canoniques et modules stratifiés" (SA15-1)

**What he does.**
- **§1 (7:3-4).** For X -> S, X^[n] is the (n+1)-fold fibre product with the diagonal, X^[n]^ its formal completion
  along X, and P^n its structure sheaf as an N-pro-object of sheaves of rings on esp(X). The P^n form a cosimplicial ring
  P* with P^0 = O_X. Warning: it is not a cosimplicial O_X-algebra, since the two maps O_X => P^1 differ. The shift SP,
  (SP)^i = P^(i+1), carries alpha: P* -> SP*. Example: X = Spec A over Spec k with X -> X x_S X a nil-immersion
  (X radiciel of finite type): Gamma P^i = A tensored i+1 times, alpha^i(a_0 x ... x a_i) = a_0 x ... x a_i x 1.
- **§2 (7:5, 7:59).** P^i[M] = P^i tensor M over the extreme-right structure, a pro-object (a sheaf only in exceptional
  cases, e.g. M free of finite type with X locally noetherian and Omega coherent). For differential operators M -> N as
  morphisms, the construction is functorial only into P^(i-1)-modules, by restriction along alpha^(i-1); boxed on 7:59:
  Q^(i-1)[M] = P^i tensor M. So Q^0[M] is a functor on Mod(X/S) (modules, with differential operators of bounded order
  as maps) to pro-O_X-modules, with the "Artin-Riesz" [Artin-Rees] morphisms of pro-objects.
- **§3 (7:6-8).** Q*[M] is a cosimplicial module over P*; its terms are base changes of one another, so Q^0[M] is a
  stratified pro-module relative to S and the Q^i[M] are the components of its cosimplicial module. M is recovered as
  the sheaf of horizontal ("stationnaires") sections of Q^0[M], with its O_X-structure from the extreme right, and an
  operator D: M -> N is recovered from Q^0[D].
- **§4 (7:8-10).** Q*[M] is a resolution of M "comme X^[1] a une section sur X^[0]", with the doubts "les A.R.-pro-modules
  forment-ils une catégorie abélienne ?" and "s'il ne faut pas une hypothèse de quasi-cohérence"; then H*(X,M) =
  H*(X, lQ*[M]) with E_2^pq = H^p(i -> H^q(X, lQ^i[M])), and for complexes M. in D+(X/S), H*(X,M.) = H*(X_str,
  Q^0(M.)) (the "formalisation" of a complex of differential operators).
- **§5 (7:11-14).** Under flatness, V^q(M.) = H^q(lQ^0[M.]) are stratified modules and the boxed spectral sequence
  H*(X,M.) <= E_2^pq = H^p(X_str, V^q(M.)), with H^p(X_str, V) := H^p(X, C._str(V)) by definition. Corollary: if
  V^q = 0 for q != q_0, then H^n(X,M.) = H^(n-q_0)_str(X, V^q_0): the result depends only on the stratified module, not on
  the differential complex that "resolves" it.
- **§6 (7:14-16).** A stratified module V has a de Rham complex Omega.(V); for X/S smooth and S of characteristic 0 it
  is a differential resolution of V, hence H*_DR(X/S,V) = H*_str(X/S,V), "au second membre duquel il n'est plus question
  de formes différentielles !". In general there is a canonical map H*(X_str,V) -> H*_DR(X/S,V) (boxed, 7:15). On 7:16:
  "Je doute que ce soit tjrs un isom, même si X est lisse et projectif (p.ex. une variété elliptique) sur S spectre d'un
  corps ... de car p > 0; et V = O_X avec stratification canonique. ... il n'est pas même clair à priori que les H^i_str
  soient de dim finie, ni qu'ils soient nuls pour i grand. Situation à éclaircir !" The blue margin bubble answers:
  "C'est en effet faux ! (Calculs très amusants pour X/S elliptique ou abélien !)". The sweep-2 reader tool prints that
  bubble as "[figure]" (correction row). The blue "Remarque": H_str is the cohomology of a "site stratifiant", "dont une
  variante conduira à la coh. p-adique en car. p".

**What I checked** (check events 7:3-4, 7:5/59/6/8-9, 7:11-13, 7:14-16, 7:16):
- The P* facts and the radiciel example: right.
- The resolution: in the affine model Q^i = A^(i+1) x A, the map h(a_0 x ... x a_i x b) = a_0 x ... x a_(i-1) x a_i b is
  an extra codegeneracy (restriction to the diagonal: his "section"), right-O_X-linear and a ring map, so it preserves
  the powers of the diagonal ideal and passes to every truncation and to the limit. So **lQ*[M] -> M is contractible for
  every O_X-module M**: no quasi-coherence is needed, and the A.R. question does not arise for this statement.
- §5-§6 are right under the stated hypotheses (the characteristic-0 step is the formal Poincaré lemma, which divides by
  n!).
- **His doubt on 7:16 is right, and the answer is now explicit.** For X smooth and proper over k algebraically closed of
  characteristic p: the differential operators are the union of D^(n) = End of O_X over O_X^(p^(n+1)), an Azumaya algebra
  split by O_X, so by Morita Ext over D^(n) of (O,O) is H*(X,O) taken over the Frobenius twist, and passing to the
  limit gives
  **H^i_str(X/k, O_X) = lim of H^i(X,O_X) under Frobenius = H^i(X,O_X)_ss = H^i(X_ét, F_p) tensor k**
  (no lim^1, by Mittag-Leffler for finite-dimensional spaces with a p-linear map over a perfect field). So the H^i_str
  are finite-dimensional and vanish for i > dim X, and the map to de Rham is not an isomorphism: an ordinary elliptic
  curve has dimensions 1, 1, 0 against 1, 2, 1; a supersingular one 1, 0, 0. These are his "calculs très amusants".
  Degree 1 I checked directly as extensions of stratified modules; higher degrees use that the site cohomology is Ext
  over D. This agrees with what I recall of A. Ogus, "The cohomology of the infinitesimal site", Ann. Sci. ÉNS 8 (1975)
  (locator unverified).

**Wrong:** nothing in the mathematics. The name "Artin-Riesz" (7:7, 7:59 margin; in the ink) is his slip for
Artin-Rees. **Reading:** "Antipiants(?)" on 7:3 is "stratifiants" (checked on the scan).

**Open on the page:** the flatness criteria of 7:12 ("critères: dégager"); the abelian-category question for A.R.
pro-modules, which the statement no longer needs.

## 3. 7:17-19 - "Commentaires sur la définition d'une cohomologie p-adique en car. p > 0" (SA15-15, SA15-1)

**What he does.** X_0 over a perfect field k, S = Spec W(k). H*(X_0/S, cris; O) is a graded W-module, his "espoir
initial" for a p-adic theory. For X_0 smooth with a smooth lift, "d'après l'exposé précédent" it is lim_n of the
H*((X_n/W_n)_cris, O) (the ink has "k" and "k_n" where W and W_n are meant: his slip), and he hoped for de Rham of the
lift "peut-être modulo torsion" (there is a map). "C'est faux malheureusement": for X_0 an ordinary abelian scheme,
**H^i((X_0/S)_cris, O) = 0 for i > dim X_0**, while the limit of the de Rham cohomologies "est excellente". In the
affine case the trouble is that the projective limit does not commute with W -> W[1/p] = K. Proposal (7:18): "Je propose
d'essayer l'approche suivante" (reading checked; the sample check of 13 Nov had found it too): replace the crystalline
site by a bigger site of thickenings "pas purement infinitésimaux", with objects the triples (U_0, V~, i): U_0 an affine
open of X_0 with ring A_0, V~ "un espace affine de W-M sur W" corresponding to a W-M algebra B (reading checked:
"correspondant à une Alg. de W-M", not "complété d'une"), and i inducing a nilpotent immersion U_0 -> V~ x_S s, i.e. a
surjection B -> A_0 with B/pB -> A_0 of nilpotent kernel, with a Zariski-type topology. Decisive tests (7:19): a) X_0
smooth affine gives W-M; b) X_0 smooth proper with a smooth proper lift gives de Rham of the lift, at least mod torsion.
"Il faudra beaucoup l'assouplir ... sans supposer la platitude, et en fait sans qu'il y ait de corps de base du tout. Il
y a du pain en perspective !"

**Checked** (check event 7:17): the vanishing holds for his site. The Čech-Alexander complex of X_n/W_n is flat over W_n
and reduces mod p to that of X_0/k, whose cohomology is H^i(X_0,O)_ss = wedge^i H^1(X_0,O) (Frobenius bijective: ordinary),
zero for i > g. Dévissage along p^j W_n and Mittag-Leffler in the limit give H^i = 0 for i > g, and H^g has rank 1 while
H^2g_DR = W. For Berthelot's divided-power site the statement is false (H^2g_cris = W): hence the note under §0.

**Status.** The site of 7:18 is the idea that rigid cohomology realized: tests a) and b) are theorems of rigid
cohomology (Berthelot; e.g. "Finitude et pureté cohomologique en cohomologie rigide", Invent. Math. 128 (1997)), and his
triples are close to the objects of B. Le Stum's overconvergent site (Mém. SMF 127, 2011) (both locators unverified).
H1-2.

## 4. 7:21-35 - "Cohomologie de De Rham des var. alg.", his pages 1-15 (SA15-15; SA05-2 on 7:31)

Boxed aim (7:21): to show the problems around the de Rham cohomology of algebraic varieties and propose a point of view
that groups them, "d'où un gros programme de travail".

**§1 Yoga (7:21-27).** The de Rham theorem for manifolds and its sheaf-theoretic proof; complex analytic spaces via
hypercohomology and the Hodge-type spectral sequence (*); for non-singular algebraic varieties, Zariski hypercohomology
of Omega. and the theorem "C'est un isom (X schéma loc. de type fini sur C)", proved "dans papiers bleus" (H1-6): for X
proper it follows from GAGA and the two spectral sequences ("essentiellement connu depuis Gaga de Serre"); the affine
case and the general case need resolution of singularities; the theorem reduces to the affine case by the Leray spectral
sequence of a covering. Critique in characteristic p: 1°) for X not proper, infinite dimensions, e.g. H^0_DR(X) =
H^0(X,O_X)^p; 2°) for X proper, dim H^1_DR(X) >= 2 dim Pic_X, sometimes with >, "dû vraisemblablement à des phénomènes
de p-torsion"; 3°) the coefficient field has characteristic p, so the Lefschetz formula gives numbers of fixed points only
mod p. b) De Rham is tied to non-singular varieties: **"même si X est une courbe, affine ou complète, sur C, p.ex. la
droite affine ou projective [avec] un pt de rebr. ordinaire, on n'obtient déjà pas pour dim H^1_DR(X) le premier nb de
Betti"** (the struck first version: "singulière (disons unibranche si on y tient)"; reading checked: "un point double" is
struck, the example is the ordinary cusp). A universal formalism needs Leray spectral sequences, hence coefficients
beyond de Rham complexes, including complexes of differential operators. c) Duality: for X smooth proper the usual
formalism, as he had done for Hodge cohomology at the Séminaire Bourbaki; but the reader "au courant des histoires f_!,
f^!" wants Hartshorne's formalism (Residues and Duality) for separated morphisms of finite type and for complexes whose
differentials are differential operators, which should also describe singular homology.

**§2 l-adic tour (7:27-33).** H^i(X,Z_l) = H^i(X^an,Z) x Z_l over C (boxed); over a field of characteristic 0:
finiteness, rank independent of l, torsion for finitely many l, characteristic polynomials of endomorphisms integral and
independent of l. In characteristic p: finiteness proved only for X proper or dim X <= 2; even for X projective smooth it
is unknown whether rank H^2 is independent of l, "le plus important pas restant en direction d'une solution des
conjectures de Weil". Rationality of the coefficients reduces (X projective non-singular) to "un pb de cycles algébriques
du type Lefschetz" (SA05-2); even so one only gets Z[1/p], "de ce qu'il manque une théorie cohomologique p-adique";
p-torsion (Tate's Bourbaki talk on the Brauer group); Serre's argument that no functor to Z_p- or Q_p-modules with the
right Betti numbers exists, already for H^1 of abelian varieties of dimension <= 2; the natural coefficient ring is W(k).

**§3 (7:33-35).** "Revue des essais": flat cohomology with p-group coefficients works "magnifiquement en dim 1" (duality,
geometric class field theory; "On espère que Raynaud tirera au clair cette théorie"), but Artin remarked that cohomology
with constant p-group coefficients vanishes above n + 1, so a definition independent of flat cohomology is needed. The
W-M approach starts: lift X_0 to X proper smooth over W; H^i_DR(X/S) is of finite type over W (boxed).

**Checked** (check events 7:23, 7:24, 7:28-29, 7:31, 7:32, 7:34): the characteristic-p critiques 1°)-3°), the l-adic
consequences, the Z[1/p] point, Serre's argument and Artin's remark are right.

**Wrong: the curve example of 7:24.** For the ordinary cusp the naive (Kähler) de Rham complex gives the right Betti
numbers. Affine y^2 = x^3: the ring C[t^2,t^3] is weighted homogeneous, the Euler derivation E = 2x d/dx + 3y d/dy
satisfies L_E = d i_E + i_E d = multiplication by the weight, every form of positive degree has positive weight, so
H*_DR = C in degree 0 = H*(point). Projective cuspidal cubic: the same homotopy on convergent series gives the analytic
Poincaré lemma at the cusp, and GAGA gives H*_DR = C, 0, C = H*(S^2); check: chi(O) - chi(Omega^1) + chi(Omega^2) =
0 - 0 + 2 = 2 (the torsion of Omega^1 at the cusp has length tau = 2, Omega^2 = C[x]/(x^2) dx^dy). The node is
homogeneous too. The defect he wants exists at non-quasi-homogeneous singularities (K. Saito, Invent. Math. 14 (1971);
the first counterexamples are Reiffen's (1967); locators unverified), e.g. the unibranch curve x^4 + y^5 + x^2y^3 = 0
(mu = 12, tau = 11). So his struck first wording, "une courbe singulière (disons unibranche si on y tient)", was right
as an existence statement, and the example he put in its place is not. Michel Hua's project reads "avec un point double
ordinaire" (the struck words); the claim is false for that reading too.

**Since 1966.** Finiteness of l-adic cohomology in general: Deligne, SGA 4½ [Th. finitude]; independence of l of the
Betti numbers of smooth projective varieties: Deligne, Weil I (1974); p-integrality of the characteristic polynomials
through crystalline cohomology: Katz-Messing (1974) (all locators unverified).

## 5. 7:36-47 - the lecture of 15.11.66: Washnitzer-Monsky (SA15-15)

**What he does.** Recap: complex cohomology is algebraic de Rham cohomology, which makes sense for any scheme but has
the defects listed; a p-adic theory is wanted. H_DR(X/S) and Rf_*(Omega_{X/S}) for any relative scheme (coherent if f
is proper and smooth, or proper over a noetherian base). "L'idée de W-M": H_DR of a lift is independent of the lift, up
to canonical isomorphism, hence an invariant of X_0 (margin: "'Some questions(?)' Journal Indien(?) 63/64", not
identified). Remarks: a) formal lifts suffice; b) W-M have invariance only after tensoring with K, and only for affine
X_0, using liftings "qui ressemble[nt] à une variété rigide-analytique à la Tate"; by oral communication W. would have
global invariants over W from the de Rham complex on the site of W-M lifts of affine opens; c) the comparison theorem
gives the right Betti numbers, those of the generic fibre. 7:39-40: the naive lift fails: for the affine line, 𝔛 =
Spf W{t}, H^1 = W{t}/(derivatives) has infinite rank, since sum a_n t^n is a derivative iff v(a_n) - v(n+1) -> infinity.
7:41: W-M replace W{t} by overconvergent series W^†{t}, "|a_n| = O(1) rho^n pour un rho > 1", and W-M algebras, quotients
of W^†{t_1,...,t_n} by closed ideals ("les idéaux sont-ils automatiquement fermés"). 7:42-43: "Il semble que le théorème
suivant soit vrai": a) a smooth A_0 has a flat W-M lift A; b) unique up to non-unique isomorphism; c) Omega^1 of a W-M
algebra by the universal property for finite modules; u^* on H(Omega.(A/W)) depends only on u_0; Cor: H(Omega.(A/W))
depends only on A_0. W-M prove this for "special" A_0 and only mod torsion; they define sheaves H*_X0, then (recently) a
site of W-M lifts of special affine opens and its hypercohomology, which gives back the formal de Rham cohomology in the
liftable case. 7:44-47, critique: an important new idea relating de Rham in characteristic 0 to the p-adic theory, with
coefficients W(k); it gives a notion of p-adic torsion "peut-être la bonne: est-ce la torsion p-adique de la fibre
générique géométrique ?" (asked by Tate "l'an dernier" for H^1; on families of cycles, "cf mes papiers aux Inventiones
à paraître prochainement", H1-7); but differential forms limit it to smooth X_0, there are no Leray spectral sequences,
and W-M cannot yet prove finiteness, duality or Künneth; yet they get a Lefschetz-Weil expression for zeta, "proche de
celui de Dwork, que je ne connais pas".

**Checked** (check events 7:39-40, 7:41): the infinite rank (explicit independent classes omega_j = sum_k p^k
t^(p^(q_j^k)-1) dt, q_j the j-th prime); overconvergent series are integrable.

**Wrong: the bound on 7:41.** "|a_n| = O(1) rho^n pour un rho > 1" (in the ink: no minus sign) admits a_n = 1. His own
next sentence (convergence on a disc of radius rho > 1) needs |a_n| = O(rho^(-n)) for some rho > 1. With that bound,
|a_n| / |n+1|_p <= C (n+1) rho^(-n) -> 0, which is the integrability he wants.

**Status.** a) and b): Monsky-Washnitzer, "Formal cohomology I", Ann. of Math. 88 (1968), with Elkik's lifting theorem
(1973) for existence in general (locators unverified). The corollary mod torsion: Monsky-Washnitzer. Integrally: H1-3.
His question on torsion: **not in general**. Crystalline torsion of the special fibre bounds the étale torsion of the
geometric generic fibre: "dim_Fp H^i_ét(X_C, F_p) <= dim_k H^i_dR(X_k)", with the same for lengths of torsion (Bhatt,
"Algebraic geometry in mixed characteristic", ICM 2022, Corollary "Torsion inequality", citing Bhatt-Morrow-Scholze;
opened, TeX lines 196-202), and Bhatt notes (line 151) that "this question was already stressed by Grothendieck in his
Algerian letter to Deligne in 1965". Equality fails in general (Bhatt-Morrow-Scholze, Publ. IHÉS 128 (2018), their
example; locator unverified). Finiteness: Berthelot (1997) for rigid cohomology (locator unverified).

## 6. 7:47-53 - Washnitzer-Monsky and Gauss-Manin (SA15-15, SA15-1)

**What he does.** "Caractère assez surprenant" of W-M invariance: if X_0 is the fibre at t_0 of a smooth proper Y over M
of finite type over S, sections g of M through t_0 give lifts X_g, and Rf_g*(Omega_{X_g/S}) = g^*(K.) with K. =
Rf_*(Omega_{Y/M}) (derived base change), hence R^i f_g* = g^*(H^i) "de même manière triviale". W-M invariance thus says
the g^*(H^i) for g through t_0 are canonically isomorphic mod torsion: a transitive system of isomorphisms, "d'espèce
voisine à une structure de descente". A stratification relative to S gives such a system (plan: 2. stratifications and
connections; 3. the transitive system over a complete local ring; 4. Gauss-Manin). 7:51: in characteristic 0 an
integrable absolute connection on H*; Manin's stability result for H^1 of curves; 3.5: by Cartan's formula d i_X + i_X d
= Theta_X, (i) for f formally smooth and affine the action of a lift of a derivation of S on f_*(Omega_{X/S}) is
independent of the lift up to homotopy, which gives integrable connections relative to T when S is smooth over T; (ii)
for f smooth, quasi-compact and quasi-separated, Rf_*(Omega_{X/S}) carries a canonical absolute connection in the derived
sense (appendix announced), and the R^i f_* individually when S has characteristic 0 and f is proper smooth (base change
for the R^i f_*); the compatibility with the transcendental connection is "triviale". Remark (7:52-53): one could hope that
these connections come from canonical stratifications, which would explain W-M invariance a priori: "C'est bien vrai si
S est de car. zéro, mais malheureusement c'est faux en car p > 0, même si on considère ... des familles de courbes
elliptiques". Summary: a puzzle combining a) a cohomology of complexes of differential operators, b) stratified
structures, c) Washnitzer-Monsky.

**Checked** (check events 7:51, 7:53): the Cartan-formula argument (two lifts differ by a vertical eta, and L_eta = d i_eta
+ i_eta d with i_eta O_S-linear; bracket gives integrability; Katz-Oda 1968, locator unverified); the failure in
characteristic p (functoriality makes Frobenius and F^2 horizontal; on the connected modular family F^2 has rank 1 at
ordinary and 0 at supersingular points, impossible for a horizontal map of locally free stratified modules). This is the
same obstruction as 6:27 (2.7), checked in sweep 3 (STUDY.md, SA15-S3-5). That a stratification relative to S gives the
transitive system: g and g' agree mod p, p is topologically nilpotent, so (g,g') factors through the completion of M x_S M
along the diagonal: right.

**Gap:** "de même manière triviale" for the R^i f_g* holds only when the R^i f_*(Omega_{Y/M}) are locally free and commute
with base change; he states the conclusion mod torsion, which is what the argument uses. **Wrong:** nothing else.

## 7. 7:54-56 - "§4 Topos stratifiant et topos cristallin" (SA15-1)

4.1: a stratification of F on X/S is the same as a coherent system of extensions of F to the infinitesimal neighbourhoods
Y' of maps Y -> X over S to which the map extends (automatic for X/S formally smooth). 4.2: the crystalline and
stratifying sites and topoi ("C'est pareil si X form. lisse sur S"), ringed topoi without final object; special sheaves
(base-change maps isomorphisms) of modules on the stratifying site = modules with stratification. 4.3: **Th.** S of
characteristic 0, X smooth over S: H*_cris or strat(X/S, O) = H*_DR(X/S). **Conj.** X locally of finite type over C:
H*_str or cris(X/C, O) = H*(X^an, C); proved for X smooth by the theorem and the comparison theorem of the first lecture
(margin: "Ceci donne une explication").

**Status.** The theorem: Grothendieck, "Crystals" (locator unverified); in substance it is §6.3 plus the formal Poincaré
lemma. The conjecture for the crystalline (infinitesimal) site is true: infinitesimal cohomology is computed by the de
Rham complex of a smooth Y containing X, completed along X (Grothendieck, "Crystals"), and that computes H*(X^an, C)
(Hartshorne, "On the de Rham cohomology of algebraic varieties", Publ. IHÉS 45 (1975), with the analytic formal Poincaré
lemma of Herrera-Lieberman, Invent. Math. 13 (1971); locators unverified). For the stratifying site see 7:70-72 and H1-4.

## 8. 7:57-58 - "Laïus", 6.12.1966 (SA15-1)

For F quasi-coherent stratified, the cosimplicial sheaf C^n(F) = lim_i F on the Delta^n(i) and the boxed H*(X_str,F) =
H*(X_zar, C*(F)). Two theories, Zariski and stratifying; "à première vue" the second is a Zariski hypercohomology with a
non-linear differential, not conversely, "on va voir pourtant que ... il en est bien ainsi": the pro-quasi-coherent
stratified Q^0(F), functorial for differential operators, whose stratifying cohomology is the Zariski cohomology of F;
in the radiciel case Q^0(F) = f^*f_*(F); so the Zariski hypercohomology of a complex of differential operators is the
stratifying cohomology of the corresponding stratified complex. These are the results of the black text (7:4-13).
Checked as part of check events 7:5/59/6/8-9 and 7:61.

## 9. 7:60-72 - the plan and "§6 Calculs Čechistes" (SA15-1)

**What he does.** 6.1 (7:60-62): in the stratifying topos the object X~ covers the final object, so a Čech spectral
sequence; X~^(nu+1) is the ind-object of the infinitesimal neighbourhoods Delta^(nu)(i) of the diagonal of X^(nu+1); for
X affine and F with quasi-coherent values inducing each other, H^q = 0 for q > 0 and H^0 = lim, hence H*(X_strat,F) =
H*(nu -> F(completion of X^(nu+1) along X)); for X not affine, the cosimplicial sheaf F^(nu) on X_zar and H*(X_strat,F)
= H*(X_zar, F*), with the boxed spectral sequence (written "X_inf(?)"). 6.2 (7:62-65): on the crystalline site X~ need
not cover the final object, but an immersion X in Y with Y formally smooth (always locally) gives Y~ = lim Y(i) covering
it, and the same formulas with the completions of Y^(nu+1) along X. 6.3 (7:65-66): for X_0 in X nilpotent and F coming
from X_0, H*(X_cris,F) = H*(X_0cris,F_0) (globally, by covering with affines; "[Il faudrait regarder si on peut se
débarrasser de l'hypothèse ... quasi-cohérence]"); for X smooth over S and S_0 in S nilpotent, H*(X_cris,O) =
H*(X_0cris,O): independent of the lift; in characteristic 0 it is H*(X_zar, Omega_{X/S}), which defines canonical
stratifications on de Rham cohomology for smooth quasi-projective f, and better, Rf_*(Omega_{X/S}) as an absolute crystal
on S. 6.4 (7:67, 7:69): for F = O, F* is a cosimplicial ring, an O_X-algebra in nu+1 ways, its coboundaries
differential operators of infinite order; "C'est via ces complexes de cochaines canoniques (plutôt que par les complexes
de De Rham) que les complexes d'op. différentielles s'introduisent dans la théorie de façon vraiment naturelle. Analogie
avec les cochaines de Čech(?)-Alexander" (the analogy is with Alexander-Spanier cochains: functions on X^(nu+1) near the
diagonal). 7:68: a struck start ("Cas de S = Spec C", "6.4. Soit X un espace analytique"). 6.5 (7:69-71): S = Spec C, X
proper: by Mittag-Leffler and GAGA, H*(X_strat,O) = H*(X^an, F^an*). **Conjecture (7:70):** for every complex analytic
space 𝔛, the complex F*_𝔛 (functions on the formal neighbourhoods of the diagonals) is a resolution of C_𝔛, "plausible,
en regardant les fibres formelles". **Th.:** X proper over C; if the conjecture holds for X^an, H*(X_strat,O) =
H*(X^an,C), and if X lies in a smooth Y, H*(X_cris,O) -> H*(X_strat,O) is an isomorphism too; "Cela donne donc des
espoirs à la conjecture de l'exposé précédent" (7:56). **Pb (7:71-72):** X flat and locally of finite presentation over
S, F as usual: is H*(X_cris,F) -> H*(X_strat,F) an isomorphism? Equivalently: is stratifying cohomology invariant under
nilpotent immersions X_0 -> X? Remark: over a complete non-archimedean field, the conjecture for analytic spaces
"flasques" (quotes in the ink; Michel Hua's project reads the same), "mais cela n'aurait pas d'implications globales si
remarquables".

**Checked** (check events 7:61, 7:63-66, 7:69-71): the Mittag-Leffler step, the covering by Y~, nilpotent invariance and
independence of the lift, 6.5 and the conditional theorem (the completion of Y^(nu+1) along X is the limit of those of
the Y(i)^(nu+1)). All right; the theorem is conditional on the conjecture.

**Open on the page:** the conjecture of 7:70 and the problem of 7:71-72 (H1-4).

## Hunches

- **H1-1 (dating of the black text).** The pencil "Juillet-Août 1967" may be a year late. Grounds: the pencil dates
  were added afterwards, and on 7:21 the same pencil first wrote 1967 for the 1966 lectures (corrected in red); the black
  text never uses sites (the sentence that says so is a blue insertion), while the lectures of Nov-Dec 1966 define the
  stratifying and crystalline sites and the "Laïus" of 6 Dec presents the black text's results (Q^0, functoriality for
  differential operators, the radiciel case) as things "on a vu"; the black text's open doubt in characteristic p
  (7:16) would be odd after the lectures, which planned §8 "Retour sur le cas de la car. p". Against: the pencil says
  1967, and a systematic write-up after the lectures is equally natural. Test: compare with the published "Crystals"
  (Dix exposés, 1968), whether it contains the P*/Q*[M] formalism and the char-p failure, and with any dated letter of
  summer 1966 or 1967.
- **H1-2 (7:18 anticipates rigid cohomology).** His triples (U_0, V~, i) with B/pB -> A_0 of nilpotent kernel are, up to
  passing to K and to overconvergent neighbourhoods, the objects of Le Stum's overconvergent site; I expect the
  cohomology of his site, tensored with K, to be rigid cohomology for smooth X_0, so that tests a) and b) hold. Links:
  SA15-15, the letter "sur coh. p-adiques" (cote 5).
- **H1-3 (integral W-M invariance, 7:42-43).** For two lifts u, u' of u_0 between W-M lifts, u' - u lies in pA, and the
  homotopy coefficients are p^(m+1)/(m+1), which are integral. So the integral statement of his corollary may hold for
  W-M lifts; what remains is overconvergence of the homotopy series. Literature to check: van der Put, "The cohomology
  of Monsky and Washnitzer" (Mém. SMF 23, 1986), Davis-Langer-Zink on overconvergent de Rham-Witt cohomology (locators
  unverified).
- **H1-4 (the stratifying site of a singular X; 7:70-72).** The intrinsic complex of 7:70 is the Čech nerve of
  X -> X_dR (X x_{X_dR} X is the completion of X x X along the diagonal). The question is whether that nerve computes de
  Rham (infinitesimal) cohomology when X is singular; for X with an embedding in a smooth Y the infinitesimal version is
  Herrera-Lieberman and Hartshorne. Test case: the cusp C[t^2,t^3], where the intrinsic complex can be computed by the
  weight grading. Status unknown to me.
- **H1-5 (a corrected 7:24).** For an affine curve over C with isolated plane singularities, dim H^1 of the Kähler de
  Rham complex should be b_1 + sum over the singular points of (mu - tau) (the local H^1 of the Kähler complex has
  dimension mu - tau; zero exactly for quasi-homogeneous germs, K. Saito). To be checked against Bloom-Herrera and Saito
  (locators unverified).
- **H1-6 ("papiers bleus", 7:22-26).** They are probably "On the de Rham cohomology of algebraic varieties" (the 1963
  letter to Atiyah), Publ. Math. IHÉS 29 (1966): it has the comparison theorem, the remark on the Hodge filtration and the
  suggestion of a de Rham description of homology for singular varieties, the three things he refers to (locator
  unverified).
- **H1-7 (the torsion question and cote 5).** The question of 7:45 is the one Bhatt attributes to "Grothendieck's
  Algerian letter to Deligne in 1965". The cote-5 letter docketed "Lettre Deligne / sur coh. p-adiques" (5:49-53, SA15-15)
  should be checked against that description by the cote-5 reader (it is filed as another's letter in sweep 2). The
  "papiers aux Inventiones à paraître" of 7:45 are probably "Un théorème sur les homomorphismes de schémas abéliens",
  Invent. Math. 2 (1966) (locator unverified).
- **H1-8 (the "calculs très amusants" and cote 4).** For an abelian variety A of p-rank f, H^i_str(A/k,O) = wedge^i of
  an f-dimensional space: the stratified (infinitesimal) cohomology sees exactly the étale p-part. I expect, for X_0
  smooth proper over k algebraically closed, H^i((X_0/W)_inf, O) = H^i_ét(X_0, Z_p) tensor W, the slope-0 part of
  crystalline cohomology. This is the same semisimple part H(X,O)_ss that drives the unit-root count of cote 4 (SA15-9,
  Lemma 8.4.3 in STUDY.md).

## Dependencies

- The black text (7:3-16, 7:59) uses EGA IV §16 (principal parts and differential operators; locator unverified) and
  nothing else from the dossier; the "Laïus" (7:57-58) and §6 (7:60-72) use it: SA15-1 internally.
- 7:17-19 uses §6.3 of the lectures (7:65-66, SA15-1) and the W-M material (SA15-15); it is the failure of SA15-1 in
  characteristic p that makes SA15-15 necessary.
- 7:31 uses SA05-2 (the Lefschetz-type standard conjecture), as sweep 2 says; 7:28-30 are the l-adic background, not
  SA05-2 itself.
- 7:47-53 uses SA15-1 (stratifications) and shares its characteristic-p obstruction with SA15-16 (6:27, section 2.7),
  i.e. the supersingular points (SA06-8 and SA05-18 in STUDY.md's "How it connects").
- 7:16-17 connects to SA15-9 (cote 4): both rest on the semisimple part of H(X,O) under Frobenius (H1-8).
- 7:45 connects to SA15-15 on cote 5 (H1-7).

## Reused material

None. Every page of cote 7 is in his hand; 7:1 is the IMAG cover sheet of the archive, not a reused leaf. No Bourbaki
or "Tribu" draft, no typescript, no other author's paper.

## Placements in sweep2/SA15/WHAT_IS_WHERE.md for cote 7

What is on the pages: 7:1 cover (SA15-12); 7:2 and 7:20 blank; 7:3-16 and 7:59 the stratified-modules text (SA15-1);
7:17-19 the p-adic commentary (SA15-15 and SA15-1); 7:21-53 the lectures on de Rham, l-adic and W-M cohomology and
Gauss-Manin (SA15-15; SA05-2 on 7:31); 7:54-72 the stratifying and crystalline sites and the Čech computations (SA15-1).
Wrong in WHAT_IS_WHERE: every cote-7 placement of **SA15-2, -3, -4, -6, -7, -8 and -13** (none of that material is on
cote 7; the lists equal the cote-8 lists cut at scan 78, and SA15-6, -7 and -8 name scans 73-78, which do not exist);
in **SA15-1** the scans 20, 24-25, 27-31, 33, 37 and 51; in **SA15-15** the scans 6 and 9; in **SA15-12** the scan 19.
One row each in the corrections file. Likely cause: entries from package MPL_7_061-072+8_001-078 filed under both cotes.

## Deliverable state

- **Passes.** First pass by GPT-6 Astra (ChatGPT Pro mode): package 31 (`MPL_6_038-067+7_001-060`, scans 1-60, 12 Nov)
  and package 32 (`MPL_7_061-072+8_001-078`, scans 61-72, 13 Nov), with research notes (cote 7: notes.md lines 293-1024
  and 13-88) and doubts files. Sample check of package 31 by Claude Fable 5.2 at effort max (13 Nov,
  `returns/MPL_6_038-067+7_001-060_check/SAMPLE_CHECK.md`): four pages, three of them on cote 7 (7:015, 7:018, 7:059),
  0.99 errors per 100 words overall; its three corrections on 7:018 are not applied to the page file. No Codex web folder
  covers cote 7. No second reading by Work: COVERAGE_20261118.md has no row for cote 7 under "Every cote with work since
  the cutoff". Michel Hua's project has a modernised reading of the whole cote (credited witness). This sweep-3 reading
  is the first full reading of the mathematics of cote 7.
- **Open readings.** Still marked doubtful in the Pro doubts file and not settled by me: the small introduction and the
  cancelled word on 7:021; the cancellations and margin of 7:023; the oblique Brauer note on 7:032; the clipped
  annotations of 7:036 and its margin "'Some questions(?)' Journal Indien(?)" on 7:037; the pencil calculation in the
  margin of 7:048 ("(k+1/2) log(k+1) - (k-1/2) log", unrelated to the text); the revisions on 7:053, 055, 057-058 and 060;
  the overwritten letters V~ on 7:018; 7:051 "H^1(X, Omega._{X/k})" in Manin's statement. Settled here: 7:003
  "stratifiants", 7:018 "essayer l'approche" and "correspondant à", 7:017 k/W (his), 7:024 cusp, 7:041 rho^n (his), the
  dates on 7:003, 7:021, 7:036.
- **Ready for an edition?** Nearly. Before editing: apply the corrections of this file and of SAMPLE_CHECK.md to the
  page files; move 7:59 between 7:5 and 7:6; render the margin figures that hold text (7:16, 7:57) as text; add editorial
  notes for his slips (7:17 k for W, 7:41 rho^n, "Artin-Riesz"), for the false cusp example (7:24), and for the meaning of
  "cristallin" without divided powers (7:17, 7:54-72). A second reading of the hard pages (7:021, 023, 032, 036, 048,
  053, 055, 057-058, 060) is advisable; the rest is ready.

## Literature route

Queries through `scripts/query_corpus.py --layer research_literature --limit-per-layer 5` (18 Nov, about 23:10 UTC):
1. "Grothendieck crystals de Rham cohomology of schemes infinitesimal site"
2. "Ogus cohomology of the infinitesimal site characteristic p"
3. "Monsky Washnitzer formal cohomology weakly complete algebras dagger"
4. "Hartshorne algebraic de Rham cohomology singular varieties formal completion"
5. "integral p-adic Hodge theory torsion crystalline cohomology etale cohomology generic fibre inequality"
6. "Monsky-Washnitzer cohomology overconvergent Kedlaya p-adic cohomology from theory to practice"
7. "Poincare lemma quasihomogeneous isolated hypersurface singularity Kahler differentials Saito"
8. "infinitesimal cohomology characteristic p stratified bundles F-divided etale cohomology" (no hit)
9. "Berthelot cohomologie cristalline des schemas de caracteristique p puissances divisees"
10. "Berthelot Ogus notes on crystalline cohomology Cech-Alexander complex"
11. "Dix exposes sur la cohomologie des schemas"

Opened: B. Bhatt, "Algebraic geometry in mixed characteristic" (ICM 2022, arXiv TeX in
`F:/user/Documents/arxiv_latex/_expanded_by_topic/perfectoid_padic_bundle/1bf789f20744fd45/ALGEBRAIC GEOMETRY IN MIXED
CHARACTERISTIC/bhatt-icm-2022-arxiv-dec2021.tex`), lines 151 (Grothendieck's torsion question, 1965) and 196-202
(Corollary "Torsion inequality", after Bhatt-Morrow-Scholze). Also searched, one level deep, the CSG list of unpublished
works (`Papors/OS/grothendieck_csg_unpublished_works_2026-06-01/metadata`): no copy of "Crystals". Not in the corpus,
hence cited "(locator unverified)": Grothendieck's "Crystals" (Dix exposés, 1968) and his Publ. IHÉS 29 paper; Ogus
(1975); Hartshorne (1975); Herrera-Lieberman (1971); Monsky-Washnitzer (1968); Elkik (1973); Berthelot (1974, 1997);
Le Stum (2011); K. Saito (1971); Reiffen (1967); Katz-Oda (1968); Katz-Messing (1974); Deligne (Weil I, SGA 4½);
SGA 4 X 5.1; SGA 5 V; EGA IV §16. The open literature questions are in H1-1 to H1-8.
