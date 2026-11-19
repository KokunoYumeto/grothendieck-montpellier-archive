# SA12, sweep 3: stretch c31_lead (cote 31, scans 2-102: "SGA A, résidus de rédaction")

Read by the SA12 lead, agent a65dbdc241d1a129a (Claude Opus 5.5 at effort max), on 19 Nov 2026. Reader B was interrupted at 29/187 before it reached cote 31, so this stretch was read by the lead.

**Sources.**
- Scans 2-51: the final Pro package MPL_31_002-051.
- Scans 52-102: the Codex-web transcriptions K31-01, K31-02 and K31-03.
- All pages were printed by `sweep3/SA12/_tools/readtex_sa12.py 31 2 102 --nodiag` and read in full, in page order.
- Scan images were not reopened here, except through the sweep-2 scan decisions on 31/020.
- Michel Hua's project was not used for this stretch.

**Places.** Item ids are SA12-n from `sweep2/SA12/OBJECTS.tsv`. Literature locators that I have not opened are marked "(locator unverified)".

## Items, in page order

### 1. 31/002-009: flat p-cohomological dimension of a field of characteristic p (SA12-41)
The even scans 4, 6 and 8 are a reused SGA 3 typescript (Exp. IX type, Théorème 5.1 and Corollaires 5.2-5.3: rigidity of central homomorphisms from groups of multiplicative type). They get one line here and are not studied.

His handwritten pages (odd scans, his pp. 1-8):
- **Definitions.** cd_p(k), for p-torsion fppf sheaves, and cd'_p(k), computed with finite commutative group schemes of p-power order. Such a group has a filtration G' ⊂ G'' = G⁰ ⊂ G, with pieces étale, radicial unipotent and radicial multiplicative.
- **Lemma 1.** cd'_p(k) ≤ n if and only if H^i(k,G) = 0 for i > n and every G of each of the three types.
- **31/005.** cd^ét_p(k) is 0 or 1.
- **Lemma 2.** cd^{t.m.}_p(k) ≤ n if and only if, for every torus T, H^i(k,T)(p) = 0 for i > n and H^n(k,T) is p-divisible.
  - Equivalently: H^i(k',G_m) = 0 for i > n and H^n(k',G_m) is p-divisible, for every finite separable k'/k. Extensions of degree prime to p suffice.
  - The proof (31/007-009) embeds G in tori, restricts to a p-Sylow fixed field, splits G into μ_p's and uses the Kummer sequence.
- **Lemma 3.** cd^{rad add}_p(k) is 0 if k is perfect and 1 if k is imperfect.

**What I checked.**
- **Lemma 3, re-proved.** From 0 → α_p → G_a → G_a → 0 (Frobenius) and H^i(k,G_a) = 0 for i ≥ 1, we get H¹(k,α_p) = k/k^p and H^i = 0 for i ≥ 2.
- **Lemma 2, "degree prime to p suffices", checked.** Over the fixed field k' of a p-Sylow of the image of Galois, the dual of G carries a p-group action, so G has a filtration with μ_p quotients. Then H^{n+1}(k',μ_p) = 0 follows from the p-divisibility of H^n(k',G_m) and the vanishing of H^{n+1}(k',G_m). Restriction and corestriction bring it down to k.
- **The dévissage, my remark.** He puts the unipotent piece G' below the multiplicative piece. Over an imperfect field, the canonical order is the multiplicative part first. For Lemma 1 the order does not matter, so this is no error in the lemma.

**Status.** Lemmas 1-3 are proved on the page, Lemma 2 in sketch. This is early work on flat cohomological dimension; its relation to Shatz and to Milne, Arithmetic Duality Theorems III (locators unverified), is left to the research package.

### 2. 31/010-018: "Généralités sur les pro-objets adiques" and a module construction (SA12-43)
- The cover on 31/010 reads "4p". The even scans 12-18 are reused typescript pages (manuscript numbers 30, 29, 28, 27); they get one line.
- **The construction (31/011-017).**
  - A is a ring, for example regular local of dimension 2. f is A-regular, g is regular on B = A/fA, and B/gB ≠ 0.
  - He builds E_{n+1} as the extension of B by E_n given by ξ_n with ξ̄_n = (ḡ,0).
  - M = lim E_n then has M = ∪ _{f^n}M, every _{f^{k+1}}M/_{f^k}M ≅ B (so M is "fA-cofini"), and M/fM ≅ (B/gB)^{(ℕ)}, which is not fA-cofinite.
- **Checked.**
  - (c_{n+1}), by computation: (B × (B/gB)^{n-1} × B)/B·(g,0,0) ≅ B × (B/gB)^n.
  - The (b_{n+1}) step on 31/013: hη_n = 0 ⇒ h ∈ fA. This needs η_n to be regular in _fE_n ≅ B, which holds when B is a domain, as in his suggested regular case.
- **Status.** A complete construction of a counterexample: the property "fA-cofini" does not pass from M to M/fM.
- **Link (my inference).** This is the cofiniteness question of Hartshorne's "Affine duality and cofiniteness" (Invent. Math. 1970, locator unverified). Hartshorne's letter of 4 Aug 1969 on that paper is in cote 37 (H37-01, 37/054-055).

### 3. 31/019-023: M. Artin's theorems on cohomological dimension (SA12-44)
**31/020, Th. 1 (K finitely generated over Q, X a model).** These conditions are equivalent:
- −1 is a sum of squares;
- K is not orderable;
- X has no simple real point;
- dim X(ℝ) < tr.deg;
- X(ℝ) is rare;
- cd_2(K) < ∞;
- cd_2(X) < ∞.

His margin asks: "suffit-il de degré de transcendance fini ??" (an open question of his).

**31/020, Cor. 1 (X of finite type over ℤ).** X(ℝ) = ∅ ⟺ cd_2(X) < ∞ ⟺ cd_2(X_ℚ) < ∞ ⟺ cd_2(X_ℝ) < ∞. Then:
- cd(X) ≤ 2 dim X + 1. The ink has "<", his slip (decided on the scan in sweep 2, F4).
- cd(X_ℚ) ≤ 2 dim X_ℚ + 2. The ink has "+2"; the transcription misreads it as "+1" (F32).
- cd(X_ℝ) ≤ 2 dim X.

**31/022.**
- Cor. 3 (X over ℝ): X(ℝ) = ∅ ⟺ cd_2(X) < ∞. Then H^i(X,F) ≅ H^i(X(ℂ)/(ℤ/2),F) and cd_2(X) ≤ 2 dim X.
- Th. 2 (k a field, r a prime): cd_r(k') = cd_r(k) + tr.deg(k'/k) for every finitely generated k'. The exceptional case is "k ordonnable, r = 2" (cd_2(k) = ∞), with the margin's sufficient conditions.

**31/023, Corollary (A a noetherian local domain).** cd_r(K) ≥ cd_r(k) + dim A, except possibly in two cases:
- (a) r = char K > 0;
- (b) r = 2 and some κ(x) is orderable with cd_2 κ(x)(√−1) finite.
- NB: if A is catenary and universally japanese, exception (b) narrows to "k itself a corps réel coulant(?)".
- NB: if A is regular, the exception is harmless; his margin asks "cette restriction est-elle inutile ???".

**Checked.**
- **His marginal example, computed.** A = ℝ[x,y]/(x²+y²), localized at the origin, is a domain, with K = ℝ(x)(ix) = ℂ(x), cd_2(K) = 1, k = ℝ and cd_2(ℝ) = ∞. So cd_2(K) = 1 < ∞ = cd_2(k) + dim A, and exception (b) is needed.
- **Reading.** "corps réel coulant(?)" is very probably "corps réel clos". The mathematics asks for an orderable field κ with κ(√−1) of finite cd, which is the real-closed situation. This is a suspected misreading; I did not open the scan.

**Status.** These are Artin's results (SGA 4 X, §§2-7, locators unverified) as he recorded them. Two things here are his own:
- the lower bound for local domains (Hua finding 31-local-ring-cd-lower-bound);
- the two margin questions.

### 4. 31/024-033: Cartan's lemma, a variant, and the SGA 2 typescript (SA12-45, SA12-46)
**31/025-027, Cartan's lemma for a site.** M is stable under finite products, and coverings by objects of M are cofinal (or efface the classes of H^q for 0 < q ≤ n). Then these are equivalent:
- (i) H^i(S,F) = 0 for 0 < i ≤ n;
- (ii) Čech H^i(𝒰,F) = 0;
- (iii) lim Čech H^i(𝒰,F) = 0.

The proof uses the Čech-to-derived spectral sequence and induction on n.
- Checked: (iii) ⇒ (i) uses E_2^{0q} = 0 for q > 0 (effacement), the induction hypothesis for 0 < q < n, and (iii) for q = 0. Agrees; this is the standard lemma (SGA 4 V 4.3; Stacks, Cartan's criterion; locators unverified).

**31/029-031, a variant with H̄^q.** The H̄^q are the colimits of Čech cohomology over coverings. It comes with the bis forms and a "schéma logique". The n / n+1 boundary in condition (ii) stays a reading question (Pro N042).

**The SGA 2 typescript, reused with his corrections and remarks (31/026, 028, 030, 032).**
- Th. 2.1-2.2, Cor. 2.2-2.4: comparison with formal completion, and the Lefschetz condition (Lef).
- **On 31/028, his instruction to correct EGA 0_III 13.7.7, page 78: delete three phrases (lines 6, 13, 23).** The printed erratum EGA III₂ Err_III 24 also adds a finiteness hypothesis on R^{n+1}T(A_k) (Pro N048). This is his own correction to EGA, recorded in one line.
- Remarques 5.10 on 31/026: purity and parafactoriality hypotheses would give equivalences of categories of étale covers and of invertible modules. With "résultats récents de MURRE", Picard schemes should exist for certain non-proper schemes. This is a programme statement (Pro N045-N047).

31/033 is a cover: "Calculs divers … 4 p polycop + 3 + 6".

### 5. 31/035-039: π₁ of an orbit space of a simplicial set (SA12-47)
ENS stationery, hand not identified, with the margin "GRÖTHENDIECK.".
- **Th. 1.** G acts on a connected simplicial set E, with B = E/G. Then im(π₁E → π₁B) is normal, π₁B/im ≅ G/S where S is generated by the vertex stabilizers, and E/S is the corresponding covering. This is Armstrong's theorem (Pro P14).
- **Lemma 3 (31/038)** asserts: "si g ∉ S, g transforme tout simplexe en un simplexe disjoint". This is **false as stated**: an edge [x, gx] meets its translate [gx, g²x]. It is also **not needed**: G/S acts freely on the simplices of E/S, and for simplicial sets that suffices for E/S → E/G to be a covering.
- **Th. 2 (31/039), re-proved.** For |G| = n, the image of p_* : H_*(E) → H_*(B) contains n·H_*(B). The G-sum θ of a lift is a cycle: within each orbit the coefficients of ∂ sum to zero, weighted by the common stabilizer order. And p(θ) = nζ.
- **Th. 3.** E contractible and S finite of order n ⇒ π_i(B), for i > 1, are torsion groups with exponents dividing powers of n. Checked: E/S is the universal cover, H_i(E/S) is killed by n for i > 0 by Th. 2, and the Hurewicz theorem mod the Serre class gives the claim.

### 6. 31/042-045: trace, inertia and the local norm criterion (SA12-48)
**31/042, Proposition.** B is a ring with a finite group G, A = B^G. These are equivalent:
- a) A = Tr_G B;
- a') 1 ∈ Tr_G B;
- b) Ĥ(G,M) = 0 for all (B,G)-modules M;
- b(q)) the same in one degree q.

Checked: the dimension shift b(q) ⇒ b(q±1) through M ⊗ ℤ[G] with the diagonal action, which is induced, agrees.

Corollary: for B normal over local A, the conditions hold when the inertia order is invertible (tame). Agrees.

**31/043.** The relative version, with Tr_{G/G'} and stable elements Ĥ(G',M)^G, and the Sylow application.

**31/044.** For a semi-local O:
- a) T_{G/G_i}x = 1 for some x, so Ĥ(G,M) = Ĥ(G_i,M)^{G/G_i}. The next word, read "Doute(?)", is very probably "Donc" (suspected misreading). The sentence then reads: 1 ∈ T_G O ⟺ p ∤ [G_i:e].
- b) G_i = 1 ⇒ H¹(G,O*) = 1.
- He then asks, with his own "?", whether H¹(G,O*) → H¹(G_i,(O/m)*) is bijective in general, and about GL(n).
  - **Checked for a totally, tamely ramified extension of a DVR**, by computation. U¹ is uniquely e-divisible, so H¹(G,O*) ≅ H¹(G,k*) = Hom(G,k*). The map is bijective.
  - The wild case is open on the page.

**31/045.** L/K is unramified ⟺ U_K ⊂ N(L*). This is local class field theory, valid for abelian L/K, as my remark.

### 7. 31/047-051: cohomological dimension of a field for algebraic groups; Tsen (SA12-49, SA12-50)
**31/047, Proposition.** For a field k, these are equivalent:
- a) H^i(k,G) = 0 for i > n and all commutative algebraic groups;
- b) the same for finite Γ;
- b') the same for irreducible 𝔽_l[Galois]-modules;
- c) the same for tori;
- c') the same for the units of separable algebras.

**The proof of b ⇒ a over perfect k.**
- Reduce to complete, semisimple or unipotent G. The decomposition "G = G_u × G_s, à vérifier" is his own self-flag.
- G/U, with U the torsion, is uniquely divisible, so H^i(G) = lim H^i(U(m)). Checked: agrees.

**Unipotent G in characteristic p (31/049).** He filters by p^iG and then argues "G ≅ k̄^n sur k̄, donc aussi sur k (car H¹(k,Gl(n)) = 0)". **The reason is insufficient.** In characteristic p, Aut(G_a^n) is not GL_n, since it contains the additive (p-)polynomials (Pro N079-N080). **The conclusion is still right over a perfect k**, because smooth connected unipotent groups are k-split there (Borel, Linear Algebraic Groups 15.5, locator unverified). The arbitrary-field branch "Supposons que k soit quelconque …" is left unwritten.

**c' ⇒ b' (31/050).** Through the norm-one units of k̄(Γ). The step "on vérifie facilement" is not written out.

**31/051.**
- Lemma 1: Tsen's theorem (C1).
- Cor. 1: Ĥ^i(K',G_m) = 0.
- Cor. 2: H^i(K,Γ) = 0 for i > 1, through roots of unity "mod p", with his own margin "est-ce … un vrai isomorphisme?", and then Artin-Schreier for p.
- All are known results (Serre, Cohomologie galoisienne II.3, locators unverified).

### 8. 31/052-062: fields of transcendence degree n; injective sheaves restricted to closed sets (SA12-38)
- **Lemma 2 and the Corollary (31/052).** H^i(K,Γ) = 0 for i > n+1 when K/k has transcendence degree 1 and k satisfies the bound n. This comes from Hochschild-Serre with Lemma 1. The Corollary gives tr.deg n over an algebraically closed field ⇒ cd ≤ n. Standard; agrees.
- **31/054** is a cover: "Th. fondamental des morphismes propres … Théorème d'échange. Questions marginales" [6 p].
- **31/055-059.** "F faisceau injectif sur X, est-il vrai que H^i(Y,F|Y) = 0 pour i>0 ? Réponse négative."
  - Examples 1-3 show that sections need not extend and that F|Y need not be flasque.
  - Example 4: Y = Y₁ ∪ Y₂, meeting in two points a and b of an irreducible X. F is the sheaf of all maps to ℚ, a product of skyscrapers, hence injective. The class (0,1) ∈ F_a × F_b is not a difference f₁ − f₂, by irreducibility. So H¹(Y,F|Y) ≠ 0.
  - It extends to irreducible Y of dimension 2 in X of dimension 3.
  - Checked: the Mayer-Vietoris argument needs only that (0,1) lies outside the image, which his irreducibility argument gives. Agrees.
- **31/060-062, Proposition.** For a sheaf F on a space X, these are equivalent:
  - (i) H¹(U,F) = 0 for all open U;
  - (i bis) the same for all H^i;
  - (ii) the Čech H¹ of two opens vanishes (X noetherian);
  - (ii bis) all the Čech H^i vanish.
  - Re-proved: (i) ⇒ (i bis). Embed F in an injective C⁰. By (i) the sequence is exact on sections, so C¹ is flasque, the resolution is flasque, and H^i = 0 for i ≥ 2.
- **31/061** is a note on p-bases, with δ(L/K,k/l) = 0 ⟺ k ⊂ l(K^p). It is poorly legible and not studied.

### 9. 31/063-069: "cd des affines" (17 p): ℓ-elementary sheaves and the φ-criterion (SA12-38)
- **31/065.** Every noetherian ℓ-torsion sheaf has a composition series of strict ℓ-elementary sheaves. Cor. 1 and Cor. 2 express cd_l(Y) ≤ φ(Y) through H^{n+1}(Y, i_*G) = 0, by noetherian induction.
- **31/067-068, Lemma.** φ satisfies:
  - (a) φ(x) ≥ cd_l k(x);
  - (b) φ(y) < φ(x) − cd_l(K_ȳ) for y in the closure of x, y ≠ x, where K_ȳ is the total ring of fractions of the strict localization.
  - Then H^i(X,F) = 0 for i > sup φ on Supp F.
- **Checked** (Leray for g: x → X). R^q g_* G is supported where q ≤ cd_l K_ȳ, so φ(y) < φ(x) − q. By induction E_2^{pq} = 0 for q > 0 and p + q ≥ φ(x). Hence H^n(X,g_*G) ≅ H^n(x,G) = 0 for n ≥ φ(x)+1.
- **Reading.** The page has "E_2^{pq} = 0 si p−(?)q ≥ φ(x)". The argument needs **p + q** (Work K31-01 S68b). It is a misreading or his slip.
- **31/069, NB.** φ(x) ≤ φ(y) + 2 tr.deg k(x)/k(y) for f of finite type.

### 10. 31/070-071: a general bound and the henselian question (SA12-38, SA12-39)
**The Corollary.** Assume cd_ℓ K_{Y,ȳ} ≤ dim O_{Y,ȳ}, which he expects is "probablement tjrs. le cas, du moins si X est 'bon'". Then cd_ℓ(X) ≤ φ(X), with φ(x) = sup_{y∈x̄}(cd_ℓ k(y) + 2 dim O_{x̄,y}).

His examples:
- algebraic schemes;
- number fields;
- "(conjecturalement) ouvert de Spec A, A strictement local";
- affine schemes of dimension 1.

The margin question: for A henselian local noetherian integral with cd_ℓ k < ∞, is cd_ℓ K ≥ dim A + cd_ℓ k? This is the henselian form of 31/023.

31/071 is a boxed lemma of sufficient conditions for cd_ℓ(X) ≤ n.

**Hunch.** His "probablement tjrs" is a form of Gabber's bound for strictly henselian quasi-excellent local domains (Illusie-Laszlo-Orgogozo, Travaux de Gabber, Exp. XVIII-A, locator unverified).

### 11. 31/072, 084: reused typescripts (SGA 3 VIII/IX type)
X/G for G of multiplicative type, the graph immersion, and monomorphisms as closed immersions (31/072), and the cancelled Th. 3.1-3.2 (31/084). One line.

### 12. 31/074-081: Artin's affine Lefschetz, in his own sequence of theorems (SA12-39)
**The theorems.**
- **Th. 1_n.** A strictly local noetherian of dimension n, X = Spec A[t], and F an ℓ-torsion sheaf vanishing in codimension < m. Then H^i(X,F) = 0 for i > n+1−m.
- **Th. 2_n.** For U = (Spec A)_f, cd_ℓ(U) ≤ n.

**The lemmas.**
- **Lemma 1:** 2'_{n+1} ⇒ 1_n. It goes through the closure in ℙ¹_A and the dimension count dim S̄_x + codim ≤ n+1. Checked: agrees.
- **Lemma 2:** 1'_n + 2'_{n+1} ⇒ 2'_{n+2}, for rings essentially of finite type over a field.
- **Lemma 3:** cd_ℓ(X) ≤ dim X for affine X essentially of finite type over a separably closed field (Artin).
- He extends the theorems to rings essentially of finite type over a noetherian ring of dimension ≤ 1 (31/078-080). The margin: "Prouvé pour l'instant pour les anneaux ess. de type fini sur un anneau de dim ≤1".

**The open "Th" on 31/080.** For X affine of finite type over a strictly local Y, is cd_ℓ(X) ≤ sup(dim X₀, dim X'+1)? For non-affine X the bound would be sup(2 dim X₀, 2 dim X'+1). 31/081 attempts an induction on the number of variables; it breaks off.

**Status.** 2_n is proved on his pages under the essentially-finite-type hypothesis. The general strictly local case is Gabber's affine Lefschetz theorem (Travaux de Gabber, Exp. XV, locator unverified). Whether that also settles the "Th" of 31/080 is left to the research package.

### 13. 31/082: his question and his own counterexample (SA12-39)
- **The question.** X is noetherian affine, ℓ is prime to the residue characteristics, and n = sup_x[cd_ℓ k(x) + dim O_{X,x}]. He asks whether n is also the sup of the cd_ℓ of the affine opens of X, "la partie vache" being cd_ℓ(X) ≤ n.
- **His answer:** "Mais c'est faux déjà pour l'anneau des entiers d'un corps de nbres car on a n=2 s'il est tot. imag., alors que cd(X)=3 !".
- **My check: the counterexample does not apply under his own hypothesis.**
  - On Spec O_K the prime ℓ is a residue characteristic, at the primes above ℓ.
  - With ℓ invertible, the test case is U = Spec O_K[1/ℓ], K totally imaginary. There n = 2: at the generic point cd_ℓ K = 2, and at the closed points 1 + 1.
  - cd_ℓ(U) = cd_ℓ(G_S) = 2 (Serre, Cohomologie galoisienne II §6; Milne, ADT II 2.9; locators unverified).
  - "cd = 3" holds for Spec O_K only when torsion at the residue characteristic is allowed, which is the Artin-Verdier H³.
  - So the question as he posed it is **not refuted** by this example. It is open on the page.
- **31/083.** He shows cd_ℓ(X) ≤ dim X + 1 for affine X of finite type over ℤ with ℓ invertible, when ℓ ≠ 2 or X_ℚ lies over a totally imaginary field. For such X with function field of transcendence degree d−1, his n equals d+1 = dim X + 1, so 31/083 is consistent with the question.

### 14. 31/085-087: "Conjectures sur la cohomologie des schémas affines" (SA12-39)
X is a good affine integral scheme with generic point x.
- **1°)** If ℓ is invertible: cd_ℓ(X) ≤ cd_ℓ(k(x)). His margin asks whether this becomes an equality for small enough opens.
- **2°)** If ℓ is neither invertible nor nilpotent: cd_ℓ(X) ≤ sup(cd_ℓ k(x), δ(V(ℓ)) + 3), where ℓ^{δ(k)} = [k:k^ℓ].
- **3° (unnumbered, between 2° and 4°).** If some prime ℓ' is invertible on X, then cd_ℓ(X) ≤ cd_ℓ(k(x)) for every prime ℓ. It replaces a cancelled bound sup(cd_ℓ k(x), δ(V(ℓ)) + 1) and a cancelled "1° bis" (X over Spec ℤ[1/ℓ']); a cancelled margin asked "A-t-on tjrs cd_ℓ(k(x)) ≥ δ(V(ℓ)) + 1".
- **4°)** A is a good henselian local integral ring with char K = 0, and U an affine open of Spec A: cd_ℓ(U) ≤ dim A + δ(k) + cd_ℓ(k).
- 31/087: "Pour les bons anneaux locaux henséliens de car. résiduelle nulle, tout est vérifié grâce à Artin."

**Checked on test cases.** Conjecture 1° holds for:
- affine varieties over algebraically closed fields: Artin gives cd ≤ d = cd of the function field;
- Spec O_K[1/ℓ]: 2 = 2;
- strictly local A: cd = 0.

**2° and 3° fit Artin-Verdier exactly, checked** (K a totally imaginary number field; Milne, Arithmetic Duality Theorems II §2-3, locators unverified).
- Spec O_K has cd 3 for all torsion sheaves, and δ(V(ℓ)) = 0 since the residue fields are finite. So 2° gives sup(2, 0 + 3) = 3, sharp.
- Every proper open U ⊊ Spec O_K, on which some prime is invertible, has H³(U,F) = 0 for every torsion constructible F. In the sequence ⊕_{v∉U} H²(K_v,F) → H³_c(U,F) → H³(U,F) → 0, the first map is dual to Hom_U(F,G_m) → ⊕_{v∉U} Hom_{K_v}(F,G_m), which is injective. So cd(U) = 2 = cd K, as 3° says.
- This explains 31/082: there he had in mind the cd of Spec O_K for all torsion sheaves, which his own hypothesis on ℓ excludes. On 31/085 he builds that case into 2° and 3°.

**Status.** Conjectures 1°, 2°, 3° and 4° are open on the page. They are among the main research questions of this topic.

### 15. 31/090-091: Lefschetz for hyperplane sections (SA12-40)
- X is projective and regular over a separably closed field, Y a regular hyperplane section, U = X − Y affine, so H^i(U,F) = 0 for i > n.
- Then H^{i−2}(Y, F_Y ⊗ Ť_ℓ) → H^i(X,F) is surjective for i ≥ n+1 and bijective for i ≥ n+2.
- Cor.: H^{2n}(X, μ_N^{⊗n}) ≅ ℤ/N, by induction on n.
- Cor. 2: by duality, H^j(X,F) → H^j(Y,F) is injective for j ≤ n−1 and bijective for j ≤ n−2.
- Checked: the Gysin sequence H^{i−1}(U) → H^{i−2}(Y)(−1) → H^i(X) → H^i(U), with purity for the regular pair, gives both ranges. Agrees.

### 16. 31/092-099, 101: "Théorème de Spécialisation" (9 p): local 1-asphericity of smooth morphisms (SA12-40)
- **Lemma 1.** A is local, a quotient of a regular ring, t is regular, the t-adic completion is normal and dim A ≥ 3. A finite normal B with B/tB a trivial covering off the origin is étale. The proof extends the étale cover of the punctured spectrum, using depth ≥ 2 and "condition des chaînes"; SGA 1962 is pencilled.
- **Lemma 2.** A smooth relative curve with a section, and a tame Galois cover that is étale on the generic fibre and split at the section point, is étale along the section.
- **Lemma 3.** A is regular local of dimension 2, and B is tame Galois, ramified only along V(x) and split over the closed point of V(y). Then B is étale.
  - Checked: by Abhyankar, B = A[T]/(T^n − x), so B ⊗ A/yA = A'[T]/(T^n − x') with x' a uniformizer. This is totally ramified unless n = 1, and splitting forces n = 1. Agrees.
- **Theorem.** A smooth f is locally 1-aspherical for finite groups of order prime to the residue characteristics. These are SGA 4 XV and XVI (locators unverified).
- **Applications.** Smooth base change; invariance under separably closed extension ("Étendre au H¹ et H² non commutatifs"); relative purity.
- **31/099.** Equivalent conditions for local constancy, via duality, with the question "normal crossings??".
- **31/101.** The open problem: for G locally constant on V = X − Y only, when are R^i h_* G locally constant? "Le Pb. ne semble pas facile … wild ramification". There is no trouble if codim ≥ 2. A link to Deligne's finiteness and semicontinuity results (SGA 4½, Th. finitude; locators unverified).

### 17. 31/100, 102: reused typescript n°339 (Krull rings, VII-7 and VII-9)
Bourbaki-type, Commutative Algebra VII §1 (my identification, unverified). One line.

## Hunches
1. **Conjecture 1° of 31/085.** cd_ℓ(X) ≤ cd_ℓ(K) for good affine integral X with ℓ invertible, with equality on small opens. It holds in every case I could test.
   - It probably reduces to Gabber's affine Lefschetz theorem plus a fibration argument, at least for X of finite type over a field, a Dedekind ring or a strictly henselian quasi-excellent ring.
   - It may fail without excellence.
2. **The question of 31/082.** cd_ℓ(X) ≤ sup_x[cd_ℓ k(x) + dim O_{X,x}] with ℓ invertible is not refuted by his number-ring example. The same tools may prove it for quasi-excellent X.
3. **"probablement tjrs. le cas" (31/070).** cd_ℓ K_{Y,ȳ} ≤ dim O_{Y,ȳ} is Gabber's theorem for quasi-excellent strictly henselian domains. Without excellence it may fail.
4. **The henselian question of 31/070 and the Corollary of 31/023.** The lower bound cd_ℓ K ≥ dim A + cd_ℓ k for henselian domains with cd_ℓ k < ∞: is the restriction to regular A needed? His margin asks this. Test singular normal surfaces over a finite field.
5. **31/044.** H¹(G,O*) ≅ H¹(G_i,(O/m)*) holds in the tame case. In the wild case it probably fails; a test is a wildly ramified ℤ/p extension of a complete DVR. The GL(n) version is open.
6. **31/011-017 and H37-01.** His fA-cofinite example bears on Hartshorne's cofiniteness problem (local cohomology modules H^i_I(M) being I-cofinite).
7. **31/101.** The local constancy of R^i h_* G for G on the complement of a smooth divisor is governed by the Swan conductors along the divisor (Deligne-Laumon semicontinuity, locators unverified).

## Dependencies
- Items 9-14 use 3 (Artin's cd theorems) and 12 (affine Lefschetz).
- Item 14 uses item 1: the p-degree δ and cd_p of fields of characteristic p.
- Item 15 uses 12 (affine vanishing, H^i(U,F) = 0 for i > n).
- Item 16 uses SA12-6 (Bertini) and SA12-19 (Abhyankar, cote 29/100), and the Lefschetz theorem of SGA 2 (SA12-46).
- Item 2 links to cote 37, H37-01 (SA12-67).

## Deliverable state
**Passes.**
- Pro MPL_31_002-051 (scans 2-51), with notes and doubts.
- Codex-web K31-01, K31-02, K31-03 (scans 52-102), with notes and math notes.
- Sweeps 1-2.
- This full reading.

**Open readings.**
- 31/020, "+1" → "+2": decided, to correct.
- 31/023, "coulant" → "clos"?
- 31/044, "Doute" → "Donc"?
- 31/068, "p−q" → "p+q".
- Cartan's variant on 31/029, n vs n+1.
- 31/061 (p-bases), poorly legible.

**Readiness.** Ready to be edited as a transcription edition once these six readings are settled on the scans. The reused typescripts (SGA 3, SGA 2 and n°339) should be marked as such.

**Unread.** None in cote 31. The scans absent from the tool's output (34, 40, 41, 46, 53, 64, 73, 89) are not in any transcription folder.
