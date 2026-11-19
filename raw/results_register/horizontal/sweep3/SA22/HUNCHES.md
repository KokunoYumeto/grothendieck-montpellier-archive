# SA22: hunches (sweep 3)

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. Each hunch gives what may be true, its grounds (the
pages), and its links. "From memory" marks literature not opened tonight.

## Cote 66, the thesis problems of 1964

**H22-1. Subject 21 is the affine analogue of proper base change, proved thirty years later.**
- *What it says:* for X = Spec A with A I-adic, separated and complete, he asks when H*(X, F) → H*(X₀, F₀) is an
  isomorphism in étale cohomology.
- *Grounds:* 66/004.
- *The answer:* for a henselian pair (A, I) and torsion coefficients the map is an isomorphism. Gabber, "Affine analog
  of the proper base change theorem", Israel J. Math. 87 (1994); Fujiwara, Duke Math. J. 80 (1995). From memory.
- *Link:* the "Pour mémoire" diagram on the same sheet (purity, regular base change, finiteness) is the programme Gabber
  completed.

**H22-2. Subject 15 asks for homotopy groups of topoi with infinitesimal coefficients.**
- *What it says:* the homotopy type of a topos "incluant une définition des π_i à [coefficients, struck] … infinitésimaux".
- *Grounds:* 66/003. The word before "infinitésimaux" was read on the image: "nouveaux" or "noyaux"; it has no
  descender, so "noyaux" is less likely; not decided.
- *What it anticipates:* Artin–Mazur did the étale part (his margin says so). The infinitesimal part points to de Rham
  and crystalline homotopy types: Toën's schematic homotopy types, and Katzarkov–Pantev–Toën. From memory.
- *Links:* Pursuing Stacks; subject 8's "lien avec 'cristaux'".

**H22-3. The "pb du carré" (subject 25, first question) has a negative answer by exterior products.**
- *The argument* (from memory):
  - On E × E, for an elliptic curve E over C, pr₁*(p − q) and pr₂*(p′ − q′) are algebraically trivial divisors.
  - Their product is the 0-cycle (p − q) × (p′ − q′). It is Albanese-trivial.
  - Such products generate the Albanese kernel T(E × E), which is nonzero by Mumford.
  - So some products of two algebraically trivial cycles are not rationally trivial, and the square of
    x = pr₁*(p − q) + pr₂*(p′ − q′) is 2·(p − q) × (p′ − q′).
- *Grounds:* 66/005; his own margin "faux, cf Mumford" is on the neighbouring question.
- *To check:* Bloch, *Lectures on algebraic cycles* (1980), lecture 1.

**H22-4. Subject 24, second question, is still open.**
- *What it says:* numerical against homological equivalence for 2-cycles on fourfolds. This is the standard conjecture D
  in its first open case.
- *Grounds:* 66/004, the inserted line "En dim 4, cycle de dim 2 équiv. num = équiv. hom ??".
- *Assessment:* a famous open problem, not material for a run tonight.

**H22-5. The list is a map of the SGA programme in 1964, and its margins of about 1968–71 record its progress.**
- *What it is:* subjects 1–10 became SGA 4, 5 and 6 and their sequels; 11–13 Néron models (Raynaud); 14, 15 and 22
  topoi, étale homotopy and Tannakian categories; 27 and 28 adèles and motives over a base.
- *What it is good for:* a historical deliverable in its own right, for Part V of the handbook.

## Cote 67, conformal surgery (1976–78, 1983–84)

**H22-6. The 1984 capping is the cusp-coordinate and decorated picture, and his g = 0 worry dissolves.**
- *What may be true:*
  - At each puncture a of a hyperbolic surface, the complete metric has a cusp coordinate z, unique up to rotation, in
    which it reads |dz|²/(|z| log|z|)². Its derivative gives a canonical Hermitian norm on T_{X,a}.
  - This is the "canonical Euclidean metric on T_{X,a_i}" that he expects on 069–070. It exists for every hyperbolic
    punctured surface, a sphere with ν ≥ 3 punctures included.
  - His principal (R*⁺)^I-bundle TB_{g,I} → T_{g,I} with a canonical section has the shape of Penner's decorated
    Teichmüller space (a horocycle at each puncture, 1987), with the section given by the cusp norms.
  - The norms are the Hermitian metrics on the tautological lines ψ_i studied by Wolpert and by Takhtajan–Zograf.
  - All literature here is from memory.
- *Grounds:*
  - 067/061–070: projective and toric structures on boundary circles, the shadow o(D), admissible disc systems, the
    "Conjecture" of 068–069, and "semble étrange" for g = 0 on 070;
  - the letter to Bers (016–021) asks the same questions.
- *Links:* SA30-9 and SA30-10 (cote 146, sewing in the Teichmüller tower); the Lego of the Esquisse.

**H22-7. Nothing after 073 depends on "rectifiable"; with smooth gluing the programme of 074–082 stands as written.**
- *What may be true:*
  - The welding statements (Th. 4, Lemma 4 B, the Scholie of 073) are right for quasisymmetric gluing maps: existence by
    the fundamental theorem of conformal welding (Pfluger 1960; Lehto–Virtanen, ch. III), and uniqueness because
    quasicircles are removable.
  - For "rectifiable" only the uniqueness half survives: rectifiable seams are removable (his Lemma 3 c).
  - From 074 on he glues smooth (even real-analytic) boundary circles. There the glued complex structure comes from
    charts and Schwarz reflection, with no welding theorem at all.
- *Grounds:*
  - 067/059–061 and 072–073 (the "rectifiable suffit" clauses);
  - 074 ("avec la condition différentiable").
- *What would refute it:* a step after 073 that uses a non-smooth seam. I found none in 074–083.

**H22-8. The anabelian sheets of January 1984 ask for what later became combinatorial anabelian geometry.**
- *What may be true:*
  - 049 b), recovering the nodes and marked points of a stable curve from the Ẑ-subgroups on which π₁(K) acts through
    the cyclotomic character, is the group-theoretic recognition of cuspidal and nodal inertia. This is the subject
    of:
    - Nakamura's Galois rigidity (1990);
    - Mochizuki's semi-graphs of anabelioids (2006);
    - Hoshi–Mochizuki on nodally nondegenerate outer representations (2011).
  - 048, the Teichmüller isomorphism for Y with a normal propagator and its failure to be Galois-equivariant, is the
    tangential base point at a boundary point of M̄_{g,ν}, as in Ihara–Nakamura on maximally degenerate curves and
    Oda's problem (1997).
  - 049 c), "compactification anabélienne … comportement par spécialisation", has no single answer in the literature
    that I know of.
  - All from memory.
- *Grounds:*
  - 067/048–051;
  - the dating (15.1.1984) puts them in the weeks of the Esquisse and of the welding notes.
- *Links:* SA28, SA31-7, SA31-9 (the anabelian parts of La Longue Marche), and the research runs on those.

## Cote 68

**H22-9. The axioms of 68/017 are meant to give "Condition K"; his question asks which groups carry such a system.**
- *What may be true:*
  - A system of totally ordered families 𝒜(g̃) of finite sets, symmetric up to translation and closed under
    convolution into the cones C(g̃h̃) (017 a)–d)), gives Condition K for the convolution-stable family it spans
    (021–022).
  - Then the rearrangement inequality for three functions, Σ f(a)g(b)h(c) over a + b + c = 0 maximized by the
    arranged functions, holds in every group with such a system.
- *Grounds:*
  - the model case on 017, symmetric intervals in a cyclic group;
  - the proof begun on 022, which stops where a common point of all level sets is needed;
  - the S₃ example of the notes, which shows the property is not general.
- *Literature, from memory:* Hardy–Littlewood–Pólya, Inequalities, ch. X (ℤ); Gabriel 1932 (cyclic groups); discrete
  Riesz–Sobolev results on ℤ/pℤ (Lev's name comes to mind; unverified).
- *Links:* the convolution scratch strings of 015–016; SA23-39 (H0DS) for the games of the same folder.

**H22-10. The games are a complete, choice-based proof of positional determinacy for reachability games, written as a
course.**
- *What may be true:*
  - The second draft (024–034) proves the Zermelo and Gale–Stewart theorem for reachability games with positional
    strategies, by a well-order device in place of ordinal ranks.
  - With the kernel characterization on 034 it is a finished teaching text.
- *Grounds:* 026–030, re-derived tonight; 048 restarts with N players.
- *Use:* a deliverable for the edition, not a research question.
