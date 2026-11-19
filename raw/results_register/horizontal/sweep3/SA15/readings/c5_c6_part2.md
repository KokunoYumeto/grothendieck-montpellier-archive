# SA15, cote 6, scans 1-21 and 28-37 (stretch c5_c6_part2): the letter to Tate of May 1966 (chapters 1-2.3 and 2.7-3.2) and "Réduction des courbes elliptiques"

Claude Opus 5.5 at effort max, c5_c6_part2 reader (sweep 3), launched by the SA15 stretch reader c5_c6 (Claude Opus 5.5
at effort max), 18 Nov 2026 (UTC). Package MPL_5+6_001-037, cote 6. Read in full, in page order: scans 1-21 and 28-37
(31 scans), with the Pro notes of each page (notes.md lines 927-1474 and 1595-1786) and the scan images where a reading
carried weight. Scans 22-27 are not reread: they are worked through in sweep3/SA15/STUDY.md §2, which I read first.
Michel Hua's project (6.modern.tex) was consulted as a credited witness on four points, named where used.

**What the stretch is.** Scans 2-32 are one document: a typescript with Grothendieck's ink corrections, a letter
("Cher John", margin "Pise, Mai 1966", folios 1-30), on the letterhead of the Istituto Matematico "Leonida Tonelli",
Università di Pisa (6:3 is the letterhead face). It is the letter to John Tate in which crystals are introduced. My scans
2-21 are folios 1-19 (chapters 1 and 2.1-2.3); scans 28-32 are folios 26-30 (the end of 2.7, 2.8, chapter 3). Scans 33-37
are a separate handwritten dossier, "Réduction des courbes elliptiques et T_p(E)" (6:33 its cover), five leaves.

**The thickenings question, answered once.** Every definition in folios 1-19 uses the category C of 1.0: R-schemes T
with a closed immersion S -> T defined by a (locally) nilpotent ideal, with **no divided powers**, and in 1.16 the
Zariski-local version (U open in S, U -> T nilpotent): this is the infinitesimal site Inf(S/R). The margin of 1.17
(6:18, in his hand) records the turn: "marche en car. 0, et pas en car p>0 (faut[e] d'introduire les puiss. div.)".
The table at the end gives, for each statement, the verdict: true as stated (infinitesimal site), true only with divided
powers, or false.

---

## 1. Documents (6:1, 6:3) — SA15-12

- **6:1** archive cover "IMAG / Institut Montpelliérain Alexander Grothendieck". No mathematics.
- **6:3** the letterhead face of folio 1-2: "Università di Pisa, Istituto Matematico 'Leonida Tonelli'", folio 2, and
  the typed text of 6:2 showing through reversed (Pro note 003.1). No new text.

## 2. Crystals on nilpotent thickenings: 1.0-1.9 (6:2, 6:4-7) — SA15-1

**What he does.** "Chapitre 1. La notion de cristal", with the terminological comment (a crystal is rigid and grows in
a suitable neighbourhood). 1.0: the category C above. **Definition 1.1:** a crystal of quasi-coherent modules on S
relative to R is a cartesian section of the fibred category of quasi-coherent modules over C; more generally an
F-crystal for any fibred category F over (Sch)/R ("cristal absolu" when R = Spec Z). 1.2 tensor operations. 1.3 the two
variances; the inverse image along S' -> S through the pushout T = S ⊔_{S'} T'. 1.4 evaluation at S ("valeur en S"),
not even faithful. 1.5-1.7 three examples; 1.8 n-connections, pseudo-stratifications, stratifications and the functor
crystals -> stratified objects; 1.9 a digression on stratifications in characteristic 0 and Cartier's descent in
characteristic p.

**What I checked.**
- **1.5 (6:4-5), S = Spec k, k perfect of characteristic p, R = Spec Z.** A thickening Spec B of Spec k has p nilpotent
  in B, and W_N(k) -> B lifting k is unique (W_N(k) is formally étale over Z/p^N because L_{k/F_p} = 0 for perfect k).
  So every value of a crystal is M_{W_N} (x) B and a crystal is a p-adic system (M_n) with M_{n+1} (x) W_n = M_n;
  finitely presented ones are the finitely generated W-modules; evaluation is (x)_W k, not faithful (multiplication by p
  on W). True as stated, no divided powers needed. His phrase "W-algèbres locales, annulées par une puissance de
  l'idéal maximal de W" is loose (a local W_N-algebra with residue field k need not have nilpotent maximal ideal, e.g.
  k[[x]]); the right category is W-algebras with a nilpotent ideal of residue ring k. The characteristic-0 clause
  "supposons k algébrique sur Q" is exactly what is needed: k lifts uniquely to every nilpotent thickening iff k is
  formally étale over Q iff Omega_{k/Q} = 0 iff k is algebraic over Q (this answers Pro note 004.4).
- **1.6 (6:5).** For S étale over R, the identity of S extends uniquely to T -> S over R for every object S -> T of C
  (infinitesimal lifting for étale maps), so S is final in C and crystals are quasi-coherent O_S-modules. True.
- **1.7 (6:5).** For S = V(J) closed in R and an object S -> T with ideal I, I^N = 0: J O_T is in I, so T -> R factors
  through S_{N-1} = V(J^N), uniquely since S_n -> R is a monomorphism; the S_n are cofinal and a crystal is a compatible
  system on the S_n, coherent on the formal completion when R is locally noetherian. True. (He writes "le n.ème
  voisinage infinitésimal de R dans S": read "de S dans R", correction 3.) With divided powers this example changes: the
  cofinal family becomes the PD envelopes of S in R.
- **1.8 (6:6-7).** Crystals = stratified objects when S -> R is formally smooth: true on the infinitesimal site
  (Grothendieck 1968, "Crystals and the de Rham cohomology of schemes", §4; Berthelot-Ogus 1978, Prop. 2.11, as cited by
  the Pro note 006.7; locators unverified by me). In the formally unramified case the target category is F_S, not F_R
  as the typescript says (correction 4, agreeing with Michel Hua's project, "F_R read F_S").
- **1.8, the flat case (6:7): "Sauf erreur, on a encore une équivalence ... si S -> R est plat et localement de
  présentation finie ... mais je n'ai pas écrit de démonstration."** Open on the page. Test (mine): S = Spec k[e]/(e^2)
  over a field k. Crystals depend only on S_red = Spec k, so coherent crystals are finite k-vector spaces. On the other
  side, (e1 - e2)^3 = 0 in k[e1,e2]/(e1^2, e2^2), so the neighbourhoods of the diagonal stop at S x S and a
  stratification is an fpqc descent datum along the faithfully flat S -> Spec k: again finite k-vector spaces. The claim
  survives this test; I have not decided it in general (the point is that a thickening of a non-smooth S has no local
  retraction to S: for the node xy = 0 and T = V((xy)^2) none exists).
- **1.9 (6:7), characteristic 0.** "Stratification = integrable connection" needs R to be a Q-scheme, not merely of
  characteristic 0. Independent re-proof of the Pro note 007.13 example: over R = Spec Z[x], E = O e with nabla e = e dx
  (integrable, base of dimension 1). A 2-connection inducing it is e -> (1 + xi + b xi^2) e with xi the diagonal
  coordinate; the cocycle condition on the triple diagonal gives (1 + (xi12 + xi23) + b(xi12 + xi23)^2) =
  (1 + xi12 + b xi12^2)(1 + xi23 + b xi23^2) mod degree 3, so 2b = 1: no stratification over Z[x] (correction 5).
- **1.9, characteristic p.** "connexion sans torsion compatible aux puissances p-ièmes" <-> descent along Frobenius: this
  is Cartier's theorem (Katz 1970, Thm 5.1, as cited by the Pro note 007.10); "Il y a loin de là à une stratification !"
  is right: stratified bundles in characteristic p are the F-divided sheaves, an infinite sequence of descents
  (Gieseker 1975, Thm 1.3, Pro note 007.11).

**Wrong on the pages.** Only slips (corrections 3-5). **Open.** The flat case of 1.8 and his two "J'ignore" questions of
1.9 (necessity of smoothness; the analogue for arbitrary fibred categories).

## 3. p-crystals, bicrystals, isocrystals: 1.10-1.12 (6:7-12) — SA15-2

**What he does.** 1.10: for S of characteristic p, p-crystals (M, F: M^(p) -> M), p^{-1}-crystals (V: M -> M^(p)),
bicrystals of weight 1 = "cristaux de Dieudonné" (FV = p, VF = p), bicrystals of weight i (FV = VF = p^i), the Tate
bicrystal of weight 2i (the unit crystal with F = V = p^i). 1.11: isocrystals (the quotient by p-torsion objects),
p-isocrystals, bi-isocrystals (F an isomorphism; dual (M, tF^{-1})), the fully faithful functors
IsBicr(S,i) -> IsBicr(S,i+1) -> ... -> Isbicr(S). 1.12: over a perfect field, Dieudonné modules, and the essential image.

**Readings decided on the image (6:9, typescript).**
- The typed relation reads "FV = p.id_M, VF = id_M(p)": the factor p is missing in VF in the typescript itself. It must
  be VF = p.id_{M^(p)} (weight 1 of FV = VF = p^i on the same page, and 1.12) (correction 1; Michel Hua's project notes
  the same).
- He corrected "poids i" to "poids 2i" in ink in the Tate bicrystal, but the next sentence still says "la puissance
  tensorielle i.ème du bicristal de Tate de poids 1": read "de poids 2" (T^1, F = V = p; 1.12 and 2.2 use weight 2 and
  T^d of weight 2d) (correction 2).

**What I checked.**
- **1.11 (6:9-10).** For crystals on S of characteristic p, multiplication by an integer prime to p is invertible on
  every value (p is nilpotent there), so torsion objects are p-torsion objects; the Hom groups are limits of
  Z/p^n-modules, hence Z_p-modules, and localizing at Q or Q_p is the same. The functor (M,F,V) -> (M,F,pV) sends weight
  i to weight i+1; after inverting p, V = p^i F^{-1} is forced, so morphisms of bi-isocrystals of weight i are the
  F-compatible ones and "oubli de V" is fully faithful. True (targeted check).
- **1.12 (6:11-12), the essential image over a perfect field.** Independent re-proof: with V = p^i F^{-1} the
  noncommutative monomials in F, V are p^{ib} F^{a-b}, so bounded orbits mean all Dieudonné-Manin slopes lie in [0, i];
  a lattice stable under F and V exists then (for slope r/s, 0 <= r <= si, take F e_j = p^{a_j} e_{j+1} with
  0 <= a_j <= i and sum a_j = r; descend from the algebraic closure). Hence: some i works iff all slopes >= 0 iff every
  F-orbit is bounded, as he says; F -> pF (Tate twist of weight 2) preserves this, F -> p^{-1}F does not, and every
  bi-isocrystal is T^{-i} (x) N with N effective. True.

**Wrong.** Corrections 1-2 (slips of the typescript). Nothing open here.

## 4. S smooth over a perfect field; lifts; the transcendental principle; rigid spaces: 1.13-1.14 (6:12-16) — SA15-1, SA15-2

**What he does.** The category C does not change if Spec Z is replaced by Spec W; crystals on S = compatible systems of
stratified objects on smooth lifts S_n over W_n (restriction from S_n to S_0 is an equivalence: invariance of the
infinitesimal site under nilpotent immersions); for a proper smooth lift X over W, coherent crystals = coherent O_X-modules
with stratification relative to W (EGA III 4-5), and a functor to stratified (= integrable connection) bundles on X_K.
The bracket of 6:14: if X_C^an is simply connected, every coherent crystal is isogenous to a constant one, every
p-crystal and every bicrystal of weight i is isogenous to a constant one: "un principe d'approche transcendante pour
l'étude des familles de groupes formels". Isocrystals -> stratified bundles on X_K is fully faithful; "Cela me semble un
peu trop optimiste" that it is an equivalence, and the ink margin "effectivement, ça ne marche pas !". 6:15: for a formal
lift X, X_K is the rigid-analytic generic fibre (Tate's rigid spaces); the question of the essential image, and of a
"groupe plus ou moins discret jouant le rôle du groupe fondamental"; noetherianity of coherent crystals; torsion-free
crystals are locally free. 1.14: M -> M^(p) through a lift f_X of Frobenius, independent of the choice up to canonical
isomorphism.

**What I checked.**
- The proper-lift statements (6:13) are true for infinitesimal crystals: formal GAGA applies to every neighbourhood of
  the diagonal of X x_W X, which is proper over W. In "Modules cohérents sur X_K, stratifiés relativement à X_K" read
  "relativement à K" (correction 6; Michel Hua's project reads the same).
- **The transcendental principle (6:14), targeted check.** For X proper smooth over W with X_C^an simply connected,
  Riemann-Hilbert and GAGA make every integrable connection on X_C trivial, and horizontal sections descend to K, so
  (M_K, nabla) = (O^r, d); then O_X (x) H^0(X, M)^nabla -> M is an isogeny. A Frobenius structure is a horizontal map
  between trivial connections on a connected proper X_K, hence constant: (M, F) is isogenous to a constant p-crystal.
  True as stated, under his hypotheses.
- **The margin "effectivement, ça ne marche pas !" (6:14), independent re-proof.** Counterexample to the essential
  surjectivity: X an elliptic curve over W (k algebraically closed), omega an invariant differential, a in W, and the
  integrable rank-1 connection (O_{X_K}, d + a omega). A stratified lattice would be p^m O_X (torsion-free stratified
  lattices are locally free, by his own 6:15, and a line bundle with trivial generic fibre on X is p^m O_X). On the
  residue disk of a point, the stratification of O_X is the series chi_a(z_1 -_E z_2) with chi_a = exp(a log_E) and
  z_1 -_E z_2 = xi.(unit) for the formal group law of X; so it is integral iff chi_a has coefficients in W, i.e. iff
  chi_a is a homomorphism from the formal group of X to G_m^ over W. For supersingular reduction the only one is 0
  (heights 2 and 1), so every a != 0 gives a stratified bundle on X_K outside the essential image; for ordinary
  reduction exactly the a in one Z_p-line qualify (the formal group is G_m^ over W). The ink margin is right. (A first
  version of this check looked only at a^p/p! and was wrong: for the ordinary canonical lift (1 + z)^a is integral for
  every a in Z_p.) The natural answer to his question is the theory of
  convergent and overconvergent isocrystals (Ogus 1984; Berthelot's rigid cohomology), as the Pro notes say; his
  "groupe fondamental" question points to the Tannakian groups of isocrystals (hunch H4).
- 1.14: two Frobenius lifts agree mod p, so (f, f') maps X into the formal neighbourhood of the diagonal and the
  stratification identifies the two pullbacks. True (infinitesimal site; on the crystalline site the same argument uses
  the PD envelope).

**Status.** True as stated for infinitesimal crystals; on the crystalline site the analogues hold for (convergent)
isocrystals, which is where the theory went (his own 6:28: "c'est à condition de prendre partout des isocristaux").

## 5. Bicrystals over an arbitrary base: 1.15 (6:16-17) — SA15-2

A bicrystal of weight i on any S: a crystal M with, for every prime p, a bicrystal structure (F_p, V_p) on its
restriction to S_p = V(p); isocrystals by inverting all n > 0. Over S of finite type dominating Spec Z "la notion
envisagée est d'une nature essentiellement arithmétique", the F_p playing the role of Frobenius, and in weight 1 the
crystal "permet de relier entre eux les groupes formels en les diverses caractéristiques". Definitions only; nothing to
check beyond consistency (in characteristic 0 the extra structure is empty, as he says).

## 6. The "site cristallogène" and the key test: 1.16-1.17 (6:17-19) — SA15-1

**What he does.** 1.16 "Un retour en arrière": Definition 1.1 and 1.3 are "un petit peu canulés": C must consist of
U -> T with U open in S, F must be a Zariski stack, and the pushout of 1.3 is only reasonable for affine S, S' ("sans
restriction sur S' -> S, la construction envisagée de somme amalgamée fait sortir de la catégorie des préschémas").
Then the site: objects (U -> T), Zariski coverings, sheaves = systems F_{U->T} with transition maps that need not be
isomorphisms; O_C; quasi-coherent crystals = quasi-coherent O_C-modules; a morphism of topoi Topcr_{S'/R} -> Topcr_{S/R}
although there is no morphism of sites. 1.17 the key test: for S smooth (and proper in characteristic p) over a field
R, H*(site, O_C) should be de Rham cohomology; relatively, the value of R^i f_{cris*} O should be R^i f_* Omega^._{S'/S}
with its Gauss-Manin connection; the margin: "marche en car. 0, et pas en car p>0 (faut[e] d'introduire les puiss.
div.)". 6:19: if the site does not give the right answer, take derived functors in the category of quasi-coherent
crystals instead, "?".

**What I checked.**
- The pushout remark is right: pushouts of a thickening along an affine morphism exist in schemes, and affineness is
  the hypothesis under which the construction is known (Ferrand 2003; Stacks, pushouts of schemes; locators unverified).
- The site is the infinitesimal site (Grothendieck 1968, §4). Its O-cohomology is de Rham cohomology in characteristic 0
  for smooth S and not in characteristic p: his margin, and the later theory (Grothendieck 1968, §§5-7; Berthelot 1974).
  The typed insertion (image read) says "valeur en S'" de R^i f_cris*(O_C'): read "valeur en S" (the sheaf lives on the
  site of S, and its value at the object S of that site is the de Rham sheaf on S; cf. 1.4) (correction 13). On the same
  page "site cristallographique" is corrected in ink to "cristallogène".
- **The alternative of 6:19 fails too in characteristic p (independent re-proof, mine).** Quasi-coherent crystals on a
  smooth S over an algebraically closed k of characteristic p are stratified bundles, i.e. F-divided sheaves (Katz's
  theorem in Gieseker 1975). An extension of O by O among them is a sequence of classes c_i in H^1(S, O) with
  F*(c_{i+1}) = c_i. For a supersingular elliptic curve F is zero on H^1(S, O), so every c_i is 0 and Ext^1 = 0, while
  H^1_DR has dimension 2. Derived functors in the category of crystals do not give de Rham cohomology either; his "?"
  is justified.

## 7. "La cohomologie de De Rham est un cristal": 2.1-2.3 (6:19-21) — SA15-1, SA15-15

**What he does.** 2.1: "une hypothèse ou un voeux pieux, mais je suis convaincu qu'elle est essentiellement correcte".
Indications: a) Washnitzer-Monsky, with two imperfections (local invariants only, global only in dimension 1; invariants
only up to isogeny, through denominators): "Il n'est pas exclu ... que dans le titre du Chapitre il faille remplacer
'cristal' par 'isocristal' (et 'est' par 'définit')"; the decisive test is that of 1.17. b) the Gauss-Manin connection,
"que j'ai vérifié pour n'importe quel morphisme lisse", integrability verified only transcendentally; no stratification
for non-proper f in characteristic p. c) "le problème que j'avais signalé dans mon papier bleu sur De Rham": an algebraic
interpretation of the Leray spectral sequence of a smooth proper family over C. 2.2 the theory wanted: a perfect complex
of crystals DR(f) for f smooth proper, compatible with base change, Künneth, a duality DR(f) x DR(f) -> T^d[2d] with T^d
the Tate crystal of weight 2d, and DR(f)(S) = Rf_* Omega^._{X/S}. 2.3 Frobenius F_p on the restrictions to S_p.

**Verdicts.**
- The title: **true only with divided powers**: for f proper smooth, Berthelot's crystalline cohomology gives a perfect
  complex of crystals on the nilpotent PD site, with base change, whose value is de Rham cohomology and whose connection
  is Gauss-Manin (Berthelot 1974, ch. V; Berthelot-Ogus 1978, §7; locators unverified). **False** for arbitrary nilpotent
  thickenings: 2.7 (STUDY.md §2) and, more directly, the p-curvature computation of item 8 below.
- 2.1 b): integrability was proved algebraically by Katz-Oda (1968) (J. Math. Kyoto Univ. 8, 199-213; Pro bibliography).
  His bracket "il n'y a pas d'espoir que la connexion provienne toujours d'une stratification: c'est faux en
  caractéristique p > 0" is true, and for a stronger reason than the one he gives (non-proper families): the computation
  of item 8 shows it fails already for the proper Legendre family.
- 2.2, "Comme les cristaux de modules sur un préschéma S forment une catégorie abélienne": the inclusion of crystals into
  O_C-modules is not left exact (multiplication by p on the unit crystal over a perfect field has sheaf kernel
  p^{n-1}W_n on W_n, which is not cartesian); the category of crystals is abelian when S is smooth over a perfect field
  (1.13: stratified modules on smooth lifts, flat projections) and in the later theory one works in the derived category
  of O-modules with crystal cohomology (correction 7; Michel Hua's project raised that the statement needs hypotheses).
- 2.1 c): the "papier bleu" is presumably "On the de Rham cohomology of algebraic varieties" (Publ. Math. IHÉS 29, 1966)
  (hunch, locator unverified). The algebraic interpretation of that spectral sequence was given by Katz-Oda (1968).

## 8. After 2.7: isocrystals, the cancelled conjecture 2.8, the ordinary case (6:28-30) — SA15-16

**What he does.**
- 6:28 (end of 2.7): "il faut en rabattre": the title and 2.2 survive only with isocrystals everywhere, and perhaps his
  notion of isocrystal is still too restrictive (characteristic-0 stratifications that do not extend over the whole
  formal scheme over W; "une analyse soigneuse du calcul-clef de Washnitzer-Monsky").
- 2.8: for which abelian schemes do 1º and 3º of 2.4-2.6 hold, outside characteristic 0? A block, **cancelled by a
  single diagonal stroke** (image read): "J'aurais assez tendance à croire que si A est une VA définie sur un corps k de
  car. p > 0, alors ... l'indépendance de G(B) d'un relèvement infinitésimal choisi B de A est vrai, pour tout anneau
  artinien de corps résiduel k, si et seulement si A est 'ordinaire'", with filtration-lifting as the description of
  liftings and an appeal to "le tapis Serre des relèvements canoniques (et des modules)". Ink margin: "Faux, ce n'est
  jamais vrai en car p>0 !".
- 6:29: what survives: "Il n'est pas exclu entièrement" that in characteristic p, for A everywhere ordinary, G(A) does not
  vary infinitesimally; then H^1_DR would have a canonical stratification on the ordinary locus which does not extend to
  the modular curve; "ce drôle de comportement ... semble assez canularesque". The bracket on the "infinite" nature of
  stratifications: H^1_DR of the modular family over Z has a stratification over S_Q which does not extend over any
  S_U ("ou presque": Frobenius-compatibility unclear).
- 6:30: a canonical stratification on the ordinary locus cannot come from a crystal (all infinitesimal extensions, "pas
  néc. de car. p"), at least if its connection is Gauss-Manin, by gluing with the characteristic-0 stratification over
  the p-adic completion; "celle de cristal elle-même semble irrémédiablement trop fine, même en se restreignant à des
  familles de VA 'ordinaires'"; at most a base reduced to a point; or impose restrictions "consistant à imposer la
  variation infinitésimale du G(A)" (to impose = to prescribe; this resolves Pro reading question 030.4: compare 6:32
  "quand on se fixe celles de G(phi) à l'aide d'un cristal en groupes"), "assez proche du point de vue de Serre".

**What I checked.**
- **The cancelled conjecture is false for every ordinary elliptic curve over a perfect field (independent re-proof,
  confirming his margin).** Let E_0 be ordinary over k perfect, E'_0 = E_0^(p), Lambda = k[t]/(t^{p+1}), and suppose the
  universal extensions G(B) of the lifts B form a crystal over all nilpotent thickenings, functorial and compatible with
  base change (the hypotheses of 2.4-2.7). In the Serre-Tate coordinate a lift of an ordinary curve over an artinian ring
  is a q in 1 + m; the quotient of the lift E_q by its canonical subgroup is the lift of E_0^(p) with coordinate q^p
  (Katz, "Serre-Tate local moduli", LNM 868, 1981; locator unverified; directly: pushing the extension of Q_p/Z_p by
  mu_{p^infty} out along the p-th power map multiplies its class q by p, i.e. gives q^p). Write D = Lie G =
  M (x) Lambda in the basis (e_mult, e_et) of the canonical splitting over k, with Fil = Lambda(e_et + l(q) e_mult),
  l(1) = 0. The lift of Frobenius E_{1+s} -> E'_{(1+s)^p} over Lambda' = k[s]/(s^{p(p+1)})
  maps Fil onto the line of e_et (D(F) is 0 on Lie), so l'((1+s)^p) = 0. By base change along the injective map
  t -> s^p, (1+s)^p = 1 + s^p is the image of 1 + t, so l(1+t) = 0: the lift E'_{1+t} has the split filtration. Restrict
  to k[t]/(t^2): there the thickening carries (trivial) divided powers, and the universal extension is rigid
  (Hom(E, G_a) = 0), so the assumed crystal agrees with Messing's, and Grothendieck-Messing separates E'_{1+e} from the
  split lift by its filtration. Contradiction. The failure sits at k[t]/(t^{p+1}), the first thickening of k[t] without
  divided powers (for p >= 3, k[t]/(t^p) carries nilpotent ones). With 2.7 (supersingular) this confirms "jamais".
- **The p-curvature computation (6:29-30).** A stratification relative to k has p-curvature 0 (d^p acts as p!
  d^[p] = 0). I computed the p-curvature of the Gauss-Manin connection on H^1_DR of the Legendre family (Picard-Fuchs
  operator lambda(1-lambda)D^2 + (1-2 lambda)D - 1/4, companion system) for p = 3, 5, 7: nonzero, nilpotent (psi^2 = 0,
  trace 0), with denominators powers of lambda and lambda - 1 only (sympy; script in the reader's scratchpad). So in
  characteristic p no stratification relative to k induces Gauss-Manin on H^1_DR over any open subset of the lambda-line,
  **the ordinary locus included**. This is Katz's theorem in an instance (the p-curvature of Gauss-Manin is nilpotent and
  nonzero when the Kodaira-Spencer map is; Katz 1970, 1972; locators unverified). Consequences: 6:30's exclusion is
  right, and holds without the gluing argument; 6:29's hope is possible only for a stratification whose connection is not
  Gauss-Manin. Such a one exists on the ordinary locus (hunch H2).
- The "ou presque" of 6:29 (does the char-p stratification respect Frobenius?) is made moot by the p-curvature argument
  when the connection is Gauss-Manin.

**What he keeps, changes and withdraws after 2.7.** Withdrawn: the crystal version of 2.2 and of 2.4-2.6 over arbitrary
nilpotent thickenings (6:28, and the cancelled 2.8 conjecture with "Faux"). Changed: to isocrystals (6:28), possibly to
a weaker notion; and, for the groups, to prescribing the variation of G(A) by a crystal in groups (6:30, 6:32). Kept: the
universal extension G(A) and its first-order rigidity, carried to p-divisible groups in chapter 3. Kept as a question:
the ordinary case over a point (6:30). The resolution came with divided powers (1º-3º on nilpotent PD thickenings:
Messing 1972, Mazur-Messing 1974, BBM 1982).

## 9. Chapter 3, p-divisible groups: 3.1-3.2 (6:31-32) — SA15-16

**What he does.** 3.1 "je dois en rabattre sur les groupes formels": the construction of G(A) of 2.6 carries over to a
p-divisible group phi over S with all residue characteristics p: Hom(phi, formal G_a) = 0 (no infinitesimal
automorphisms); the H^2 of phi with values in formal G_a is locally free of rank g* = dim phi*, isomorphic to Lie(phi*)
(suggested by Lubin-Tate on moduli of formal groups); the universal extension G(phi) of phi by a formal vector group,
with Lie sequence (*) 0 -> t_{phi*}^dual -> H(phi) -> t_phi -> 0, functorial and compatible with base change. G(phi)
varies "moins que phi" but is not independent of infinitesimal variations "(à l'exception, probablement, de celles du
premier ordre)", except perhaps for phi an extension of an ind-étale group by a toric one over a point "(?)". 3.2: (*) is
an invariant over complete noetherian adic rings; over a complete DVR A (possibly of mixed characteristic) with phi_0
ordinary over a perfect k, liftings of phi_0 to A "soit entièrement équivalente" to liftings of the Hodge filtration of
M (x)_W k to a filtration of type (g, g*) of M (x)_W A; "Il serait bien intéressant d'essayer de déterminer, en termes
d'une telle donnée, quel est le module de Tate correspondant à la fibre générique de phi !".

**What I checked.**
- Hom(phi, G_a) = 0 over a base where p is locally nilpotent: f(x) = f(p^N y) = p^N f(y) = 0 since phi is p-divisible
  and p^N kills G_a. True (targeted check). The rank-g* Ext and its identification with Lie(phi*), and (*): this is
  Messing's universal extension, 0 -> omega_{phi*} -> Lie E(phi) -> Lie phi -> 0, omega_{phi*} = t_{phi*}^dual (Messing
  1972, ch. IV; locator unverified). The prose "le groupe formel (covariant) de t_{phi*}" against (*) with the dual
  (Pro note 031.3): (*) is the right one; the prose matches it if V(t_{phi*}) is meant in EGA's contravariant
  convention, as in 2.6.
- "à l'exception, probablement, de celles du premier ordre": true, because a square-zero ideal carries the trivial
  divided powers, and Messing's crystal covers nilpotent PD thickenings. The "(?)" exception (ordinary phi over a point,
  all nilpotent thickenings) fails: the argument of item 8 is an argument about ordinary p-divisible groups over a
  perfect field (the Frobenius isogeny is the endomorphism diag(p, 1) of mu_{p^infty} x Q_p/Z_p).
- **3.2.** True when the divided powers of m_A are topologically nilpotent, i.e. e < p - 1 (Grothendieck-Messing over
  the PD thickenings A/p^n -> k and passage to the limit; for ordinary groups the bijection is q -> log q, from the lifts
  1 + m_A to the filtrations m_A). False as stated for large ramification (correction 12): once zeta_p is in A (e >= p - 1), the
  logarithm identifies the distinct lifts q = 1 and q = zeta_p, and the comparison D(phi)_A = M (x)_W A on which the
  statement rests is not defined without nilpotent divided powers. The classification over arbitrary complete DVRs needed Breuil-Kisin modules (Breuil 2000; Kisin 2006;
  locators unverified). Michel Hua's project also restates 3.2 under e < p - 1. His question about the Tate module of the
  generic fibre is the "foncteur mystérieux" (Grothendieck, ICM 1970), answered by Fontaine's theory (Fontaine 1982;
  Fontaine-Laffaille 1982; Colmez-Fontaine 2000; locators unverified). Its first worked case is on the next pages: 6:34-35
  compute it for ordinary elliptic curves.

## 10. Reduction of elliptic curves over a complete DVR (6:33-37) — SA15-17

**The leaves.** 6:33 a cover: "Réduction des courbes elliptiques et T_p(E)", "(cf. aussi livre de Serre 'Abelian l-adic
representations')". 6:34 "Courbes elliptiques sur un corps local à car. résiduelle p > 0: étude infinitésimale": A a
complete DVR, K its fraction field, k its residue field of characteristic p. **Reading order:** 6:37 ends "Je conjecture"
and 6:36 begins "que cet élément a une image non nulle dans Z_p" (both read on the images): the order is 34, 35, 37, 36
(Michel Hua's project reads the same; Pro note 037.5 left it as a hypothesis). The archive folios follow the scan order
and do not decide it.

**1º) K of characteristic 0.** a) Good ordinary reduction: T_p(E_K) is canonically an extension of an unramified L of
rank 1 by L^dual (x) T_p(G_m) = L^dual(1); the class lies in H^1(K, L^{-2} (x) T_p(G_m)); for k separably closed it is
in H^1(K, T_p(G_m)) (x) L_0^{-2} = (lim K*/K*^{p^n}) (x) L_0^{-2} = Hom(L_0^2, K*^), and it is "bien ramifié": it lies
in Hom(L^2, A**) = L^{-2} (x) A**, A** the principal units ("Eins-einheiten"); "[NB. Ça fait donc qu'on a un invariant à
déterminer mod exponentiation par un carré de unités p-adiques]". Margins: "L'extension T_p(E_K) peut être triviale
(relèvements de Serre) ou non. Cas intéressant: s'il est d'ordre fini ..." and "En tous cas, on aura une opération
abélienne [...]".
- **Checked (independent re-proof).** The kernel of reduction is isotropic for the Weil pairing, so it is L^dual(1); the
  class is in Ext^1(L, L^dual(1)) = H^1(K, L^{-2}(1)); for k separably closed L is trivial and H^1(K, Z_p(1)) = K*^ by
  Kummer theory and Mittag-Leffler. The class comes from the extension 0 -> E^ -> E[p^infty] -> E[p^infty]^et -> 0 over
  A, so it lies in the image of Ext^1_A(Q_p/Z_p, mu_{p^infty}) = lim A*/A*^{p^n} = A*^. This equals the principal units
  1 + m_A when k is perfect (k* is then p-divisible); for k separably closed but imperfect the residue units survive
  and the subgroup is A*^, not A** (correction 8; the Pro note 037.4 raised the imperfect field at 6:37). A change of
  generator of L_0 by u in Z_p* changes the invariant q to q^{u^2}: his NB is right. This q is the Serre-Tate parameter
  of the lift (Lubin-Serre-Tate 1964; Katz 1981; locators unverified): q = 1 exactly for Serre's canonical lifting.
- **The margins.** If q has finite order, its Kummer class dies on G_{K(mu_{p^infty})}, so the cocycle factors through
  the cyclotomic character and the image of Galois is abelian: the left margin ("une opération abélienne") holds in that
  case. Finite order means q a root of unity; that these lifts are the ones isogenous to the canonical lift is my hunch H5.

**b) Good supersingular ("hypersingulière") reduction. "J'ai envie de conjecturer que alors la représentation de pi_1(K)
dans T_p(E_Kbar) est ½-simple, voire que l'image de pi_1(K) dans Aut(T_p(E_Kbar)) est un sous-groupe ouvert ... ??"**
- **Reading (image, 6:35).** The ink is "½-simple": shorthand for "semi-simple", the contrast with case a), where the
  representation is a non-split extension (Pro transcription: "\frac12(?)-simple").
- **Exact statement and decision.** (i) V_p(E) is semisimple: **true**, indeed irreducible over every finite extension
  of K (k perfect). Proof (independent re-proof): V_p(E) is crystalline with D_cris the isocrystal of E_k, isoclinic of
  slope 1/2; a G_{K'}-stable line would be a crystalline character, whose D_cris is a rank-1 sub-isocrystal over
  W(k')[1/p], of integral slope: impossible (Fontaine's theory; the same holds over every finite K'/K). Semisimple, as
  irreducible. (ii) "voire ... un sous-groupe ouvert": **false in general** (correction 9). The
  counterexample (Pro note 035.6, checked): E: y^2 = x^3 - x over K = Q_3(i) has good supersingular reduction and
  K-rational complex multiplication (x, y) -> (-x, iy), so the Galois image lies in the units of Q_3(i), a non-split
  torus. It is **true exactly when the formal group of E has no extra endomorphisms over any finite extension of K**: by
  Sen's theorem (Sen 1973) the Lie algebra of the image contains, after (x) C_p, the Sen operator with eigenvalues 0 and
  1; an irreducible proper algebraic Lie subalgebra of gl_2(Q_p) with that property is a non-split Cartan subalgebra,
  i.e. formal complex multiplication by Tate's theorem; otherwise the Lie algebra is gl_2 and the image is open (Serre,
  "Sur les groupes de Galois attachés aux groupes p-divisibles", 1967, for dimension 1; locators unverified).
- (a'+b') potentially good reduction: a') potentially ordinary: the image is "métabélienne": **true** (the line of the
  formal group of the Néron model over a finite Galois extension is G_K-stable, so the image is in a Borel subgroup);
  b') "les conclusions de cette conjecture valent aussi": true for both parts (semisimplicity descends from a normal
  subgroup of finite index in characteristic 0; openness passes to the larger group).

**NB (6:37): "Si l'invariant j est entier, alors on peut conjecturer que E_K a bonne réduction ssi il en est de même de
T_p(E_K), le groupe p-divisible associé"** (margin "?"; "de même" written m-bar). **True**, and without the hypothesis on
j: an abelian variety over K of characteristic 0 has good reduction iff its p-divisible group extends over A (SGA 7 I,
Exposé IX, §5, via Tate's theorem; for a generic fibre of characteristic p, de Jong 1998; locators unverified). The
theorem is in cote 100 itself (SA15-19: STUDY.md §3, the typescript "Modèles de Néron et groupes p-divisibles" and its
corollary), which places these leaves before that dossier or alongside it (hunch H6).

**c) j not integral (6:37).** "Alors le modèle de Néron est tel que E_k^0 est une forme de G_m" ("forme de" inserted);
in p^nu E there is a canonical subgroup, a form of mu_{p^nu} (struck: "fini et"; margin "[qui n'est pas fini sur A en
gén]", on the p^nu-torsion of the Néron model); hence in T_p(E_K) a sub-module, "une forme finiment tordue de T_p(G_m)"
("[donc un T_p(G_m) défini au signe près]"); "Donc si k est sép. clos, on trouve que T_p(E_K) admet un sous-module
isomorphe (de façon canonique mod signe) à T_p(G_m) = Z_p(1), quotient étant nécessairement isomorphe à Z_p [car det
T_p(E_K) = Z_p(1)]"; the extension is given by a canonical element of K*^, an extension of Z_p (from K*/A*) by A**.
"Je conjecture [6:36] que cet élément a une image non nulle dans Z_p, donc que l'extension ne provient pas d'une
extension de groupes p-divisibles sur A. Question: Quel est l'élément obtenu de Z_p ! est-ce tjrs un entier, voire un
entier > 0 ?"
- **Refuted, with the refined statement.** E_k^0 is a form of G_m only when E has multiplicative reduction. If E is a
  ramified quadratic twist of a Tate curve, the reduction is additive (type I_n*) and E_k^0 = G_a; then p^nu E^0 is not
  quasi-finite and there is no such subgroup over A. The Pro note 037.2-3 gives the example over Frac W(F_5bar): Tate
  curve with q = 5 twisted by d = 5, v(c_4) = 2, v(Delta) = 7. In that case, even with k separably (algebraically)
  closed, the sub-module of T_p(E_K) is Z_p(1) (x) chi with quotient chi, chi the ramified quadratic character, and it
  is not isomorphic to Z_p(1). Refined statement: T_p(E_K) is an extension of chi by Z_p(1) (x) chi, chi the quadratic
  character of the twist (chi trivial iff split multiplicative reduction; for k separably closed, iff multiplicative
  reduction) (corrections 10-11). His "forme finiment tordue ... défini au signe près" is exactly this twist; the error
  is only in the passage through the Néron model and in "k sép. clos" as the condition for untwisting.
- **The conjecture "image non nulle dans Z_p" is true, and the Question has a positive answer.** The class lives in
  H^1(K, Z_p(1) (x) chi (x) chi^{-1}) = K*^ (the twist cancels) and is the Kummer class of Tate's parameter q, with
  v(q) = -v(j) (Tate 1959, published 1995; Silverman, Advanced Topics, ch. V; locators unverified; Pro note 036.2). Its
  image in Z_p is v_K(q) = -v_K(j), always a positive integer; and since classes from p-divisible groups over A lie in
  A*^ = the kernel of the valuation, the extension does not come from A. Proved (independent re-proof, from Tate's
  uniformization).

**2º) K of characteristic p (6:36).** T_p(E_K) is no longer described by Galois modules alone; A) j integral: if E_k is
ordinary, E_K is ordinary, and the p-divisible group is an extension of L_K by L_K^dual (x) T_p(G_m) with an invariant in
L^{-2} (x) A** ("(si k alg. clos)"); the sentence breaks off at "(pas nul dans L^{-2} (x)". **Checked**: the Serre-Tate
theory holds over artinian and complete local rings of characteristic p with perfect residue field, and the extension
class is in Ext^1(Q_p/Z_p, mu_{p^infty}) over A = 1 + m_A (k algebraically closed); in characteristic p this group is
p-adically complete (for A = k[[t]] it is a product of copies of W(k) by Artin-Hasse). True as far as it goes.

**SA16 links.** The invariant j and its integrality (SA16-2), the Tate curve at the cusp of the modular curve (SA16-13).
SA16-1 (Weierstrass coordinates) and SA16-19 (the exceptional j-values) are not used on these leaves.

---

## Verdicts on thickenings (folios 1-19 and 26-30)

| Place | Statement | Thickenings used | Verdict |
|---|---|---|---|
| 6:2, 1.0-1.1 | crystals as cartesian sections | nilpotent, no PD | definition (the infinitesimal site) |
| 6:4-5, 1.5 | crystals over a perfect field = W-modules | nilpotent | true as stated; also true with PD |
| 6:5, 1.6-1.7 | étale S: crystals = O_S-modules; S closed: formal completion | nilpotent | true as stated; 1.7 changes with PD (PD envelopes) |
| 6:6-7, 1.8 | formally smooth: crystals = stratified objects | nilpotent, ordinary stratifications | true as stated; with PD: PD-stratifications |
| 6:7, 1.8 | flat lfp: same equivalence | nilpotent | open; passes the test S = Spec k[e] |
| 6:7, 1.9 | char 0: stratification = integrable connection | — | true for Q-schemes; false for Z[x] |
| 6:12-14, 1.13 | smooth S: compatible stratified lifts; proper lift; transcendental principle | nilpotent | true as stated |
| 6:14 | isocrystals -> stratified bundles on X_K an equivalence? | nilpotent | false, as his margin says |
| 6:18, 1.17 | site cohomology = de Rham | nilpotent | true in char 0; false in char p; true with PD (Berthelot) |
| 6:19 | derived functors among crystals instead | nilpotent | false in char p (Ext^1 = 0 on a supersingular curve) |
| 6:19-21, 2.1-2.2 | de Rham cohomology is a (perfect complex of) crystal(s) | nilpotent | false (2.7; p-curvature); true with nilpotent PD (Berthelot) |
| 6:20, 2.1 b) | Gauss-Manin from a stratification in char p | — | false even for proper families (p-curvature nonzero) |
| 6:28, 2.8 (cancelled) | G(B) independent of the lift over all artinian rings iff A ordinary | nilpotent | false for ordinary curves (k[t]/(t^{p+1})); his margin "Faux" |
| 6:29 | canonical stratification on the ordinary locus | char p | possible only with a connection other than Gauss-Manin |
| 6:30 | no crystal on the ordinary locus inducing Gauss-Manin | nilpotent | true |
| 6:31, 3.1 | G(phi) constant along first-order variations | square-zero (trivial PD) | true (Messing) |
| 6:31, 3.1 | G(phi) a crystal for ordinary phi over a point (?) | nilpotent | false (argument of 6:28) |
| 6:32, 3.2 | lifts over a complete DVR = lifts of the filtration | PD on m_A | true for e < p - 1; false once zeta_p is in A |

## Hunches (mine; none is a statement of the pages)

**H1. This is the letter to Tate of May 1966, and its folios 1-30 are the earliest written source of most of crystalline
vocabulary.** Grounds: "Cher John", "Pise, Mai 1966", the Pisa letterhead (6:2-3); "cristal" with its terminological
comment, "p-cristal" (F-crystal), "cristal de Dieudonné", "bi-isocristal", the Tate crystal T^d, and the question of the
Tate module of the generic fibre (3.2) that became the "foncteur mystérieux". Michel Hua's project mentions an IHÉS
photocopy of the same sheets ("FG_IL_2_TATE66"); 2.7's counterexample reappears in the IHÉS lectures of December 1966
("Crystals and the de Rham cohomology of schemes", Dix exposés 1968, §3.5 as cited by Pro note 007.12, locator
unverified). Comparing the letter with those lectures would date each change.

**H2. 6:29's "drôle de comportement" is real: on the ordinary locus in characteristic p there is a natural
stratification of H^1_DR, different from Gauss-Manin.** Grounds: over the ordinary locus the Hodge and conjugate
filtrations are complementary; the conjugate line is (x) O of the étale Tate module of the étale part and the Hodge line
is dual to the multiplicative part, both F-divided, so H^1_DR = (Hodge) + (conjugate) is a sum of two stratified line
bundles; its connection has p-curvature 0 while Gauss-Manin's does not (computed above). It is the mod-p shadow of the
Dwork-Katz unit-root splitting (Katz 1973, "p-adic properties of modular schemes and modular forms"; Deligne, "Cristaux
ordinaires et coordonnées canoniques", 1981, local copy Papors/OS/Deligne/01_papers/38_...), and the failure to glue with
characteristic 0 is measured by the Kodaira-Spencer map.

**H3. The "principe d'approche transcendante" (6:14) holds for convergent F-isocrystals.** If S has a proper smooth lift
X over W with X_C simply connected, rigid GAGA for connections on X_K and Riemann-Hilbert make every convergent
isocrystal on S constant; with de Jong's full faithfulness (1995, 1998) every family of p-divisible groups over S would
then be isogenous to a constant one. Pages: 6:14-15.

**H4. His question on 6:15 (a "groupe fondamental" for stratified modules on rigid spaces) is the question of Tannakian
groups of (over)convergent isocrystals.** Grounds: the page asks for "un groupe plus ou moins discret"; the later answer
is Tannakian (Crew 1992, "F-isocrystals and their monodromy groups"; locator unverified); links SA15-6 (Tannakian
categories of crystals, cote 8).

**H5. "Cas intéressant: s'il est d'ordre fini" (6:35 margin) singles out the lifts isogenous to Serre's canonical lift.**
Grounds: q has finite order iff q is a root of unity; quotienting by the canonical subgroup sends q to q^p, so some
isogenous lift has q = 1; over k = F_pbar these are the lifts with complex multiplication (Deuring, Serre-Tate). To check
in Katz 1981 (LNM 868) and Messing's account of Serre-Tate theory.

**H6. The elliptic-curve leaves 6:33-37 lie between the Tate letter (May 1966) and the "Bonne réduction" dossier (cote
100, cover 14 March 1967), and the cover's reference to Serre's book (1968) is a later addition.** Grounds: the NB of 6:37
conjectures what cote 100 proves (SA15-19); the leaves compute, for elliptic curves, the Tate module asked for in 3.2;
Serre's "Abelian l-adic representations and elliptic curves" appeared in 1968 (its chapter IV appendix treats these local
cases; locator unverified).

## Dependencies (ids from sweep2 WHAT_IS_WHERE)

- SA15-1 (6:2-7, 6:12-21) uses EGA III 4-5 (6:13), Cartier's descent (6:7), Washnitzer-Monsky = SA15-15 (6:18-19,
  6:28), Katz-Oda style Gauss-Manin (6:18-20).
- SA15-2 (6:7-12, 6:16-17) uses SA15-1 ("en vertu de 1.5", 6:8).
- SA15-16, folios 26-30 (6:28-32), uses 2.4-2.7 (6:22-27, STUDY.md §2), 1.13 (6:28), SA15-1, SA15-2; the supersingular
  points of SA06-8 are the obstruction in the cancelled 2.8 (6:28) and in 6:29-30.
- SA15-17 (6:33-37) uses SA15-16 (p-divisible groups, Serre's liftings; 6:35), SA15-19 (the good-reduction criterion of
  cote 100 proves the NB of 6:37), SA16-2 (integrality of j; 6:35-37), SA16-13 (Tate curve at the cusp; 6:37).
- Used by: SA15-19 uses SA15-17 (the criterion conjectured on 6:37); SA15-18 (Tate-Hodge, 6:38-46) continues 3.2's
  question.

## Reused material

None. 6:1 is the archive cover, 6:3 the Pisa letterhead face; the letter (6:2-32) is his own typescript with his ink.

## Deliverable state

- **Passes:** Pro transcription and Pro notes (all 31 scans); no Codex web return for cotes 5-6; this sweep-3 reading
  (31 scans, with the images at 6:9, 6:28, 6:34-37); Michel Hua's project as a witness.
- **Open readings:** the lower-left margin of 6:28 (a slanted pencil insertion keyed by a caret before "fallait",
  inside the cancelled block, "[figure]" in the Pro transcription; not read at 300 dpi); the bracket of the left margin of 6:35 ("[dans le cas gén.]" in the Pro reading, possibly "[dans ce
  cas]"); the end of 6:36 ("pas nul dans L^{-2} (x)", unfinished on the page).
- **Ready for a transcription edition:** yes for 6:1-21 and 6:28-32 (a clean typescript; record the two typescript slips of
  6:9 and the slips of 6:5, 6:6, 6:13 as editorial notes); yes for 6:33-37 once the reading order 34, 35, 37, 36 is stated
  in the edition.
