# SA22: research packages, in concept (sweep 3)

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. These are concepts only; no prompt is written tonight.
Each gives the question, why it matters, what it rests on, the strongest known reduction, and the material a run would
need.

## R22-1. The fates of the 28 thesis problems of 1964 (a literature run)

- **Question:**
  - For each of the 28 subjects on 66/002–005, and each item of the "Pour mémoire" diagram, who settled it, where (exact
    locators), and what remains open.
  - Settle in particular subjects 21 (Gabber, Fujiwara?), 25 (the "pb du carré") and 24 (second question).
- **Why:** a primary document of the SGA programme in 1964, annotated by him around 1968–71. It belongs in Part V of
  the handbook and in the history of the fonds. The answers are scattered across forty years of literature.
- **Rests on:** SA22-0, H66-01 (four sheets).
- **Strongest known reduction:** the from-memory list in STUDY.md §1: Gabber 1994 and Fujiwara 1995; Saavedra 1972;
  Deligne 1990; Parshin 1976 and Beilinson 1980; Fulton 1984; Griffiths 1969; Mumford 1968; Artin–Mazur 1969;
  Raynaud's Néron and Picard work.
- **Material:**
  - the transcription and the four scan images;
  - the SGA 4, 4½, 5 and 6 indexes (our French-school corpus);
  - Raynaud's thesis (1970);
  - Bloch's *Lectures on algebraic cycles*;
  - Gabber's and Fujiwara's papers.

## R22-2. The conformal-surgery programme of 1984: capping, admissible discs, and the stable-curve maps of section 6

This is one cluster, so the welding correction goes into this package and not into a run of its own.

- **Question:**
  - (a) Is the (0,3) claim of 067/068, marked "?", true: in an admissibly capped pair of pants, does each disc depend
    only on its own boundary length ℓ_i? Settle it by an explicit computation with hyperbolic pants.
  - (b) The "Conjecture" of 068–069. For a hyperbolic punctured surface, is (D_i) ↦ (o(D_i)) a bijection from
    admissible disc systems to systems of Euclidean discs? Equivalently, is admissible capping TB_{g,ν} → T_{g,ν} a
    principal (R*⁺)^ν-bundle with a canonical section?
  - (c) Compare that bundle and its section with:
    - Penner's decorated Teichmüller space;
    - the cusp norms on the T_{X,a_i} (H22-6);
    - the g = 0 case he found strange.
  - (d) The maps of section 6, MDB_{g,ν} → M_stND_{g,ν} and MD_{g,ν} → M_stN_{g,ν} (074–082): are they isomorphisms?
    Compare with the plumbing constructions of the Deligne–Mumford compactification (Kra 1990, Earle–Marden, Wolpert,
    Hubbard–Koch 2014; from memory). Settle his key case (0,4) first, as the pages do.
  - (e) Write the welding statements of 059–061 and 071–073 in their correct form: quasisymmetric gluing for existence,
    removable seams for uniqueness.
- **Why:**
  - It is his own programme of January–April 1984, the analytic side of the Teichmüller tower in the Esquisse.
  - The letter to Bers shows he wanted it answered.
  - The answers decide whether the pages are an early form of plumbing and decorated coordinates or a different
    construction.
- **Rests on:** SA22-3, SA22-6, SA22-7, SA22-8; 067/016–021, 053–083; CORRECTIONS.tsv (the welding rows); H22-6, H22-7.
- **Strongest known reduction:**
  - Admissible capping is well defined: glue each unit disc along the arclength parametrization of the geodesic
    boundary.
  - So (b) is a fibre-by-fibre existence-and-uniqueness problem over T_{g,ν}.
  - (a) is its (0,3) instance.
- **Material:**
  - the transcriptions MPL_67_002-052 and MPL_67_053-101, with their notes and doubts files, and scans 016–021 and
    053–083;
  - Penner's decorated Teichmüller paper; Kra's horocyclic coordinates; Hubbard–Koch;
  - Lehto–Virtanen, ch. III.

## R22-3. The anabelian sheets of 15 January 1984 (067/048–051)

If the La Longue Marche anabelian packages already hold this question, merge it into them; one prompt per cluster.

- **Question:**
  - (a) Map 049 a), b) and c) and the NB of 048 onto the literature: what is proved, where, and what is open.
    - a): the anabelian conjecture for singular stable curves with a normal propagator.
    - b): recovering nodes and marks from the cyclotomically acted Ẑ-subgroups.
    - c): the anabelian compactification and its behaviour under specialization.
  - (b) Check the presentations of 050–051 (T⁺_{0,4}, T⁺!_{0,4} ≅ SL(2, Z)/±1, the Birman sequence) and his
    expectation of three kinds of presentation (pants, Lego, involutions) against the known presentations of the
    mapping class groups.
- **Why:**
  - A dated statement of the anabelian programme for stable curves, written in the weeks of the Esquisse.
  - The sheets connect the welding notes to La Longue Marche.
- **Rests on:** SA22-5; 067/048–051; H22-8; SA28, SA31-7, SA31-9.
- **Strongest known reduction:**
  - The SL(2, Z) and GL(2, Z) presentations on 050 are checked (CHECK_EVENTS).
  - The rest is from memory: Nakamura; Ihara–Nakamura 1997; Mochizuki 2006; Hoshi–Mochizuki 2011.
- **Material:**
  - MPL_67_002-052, with notes and doubts, and scans 048–051;
  - the La Longue Marche transcriptions of the same months;
  - the papers named, as arXiv sources where they exist.

## R22-4. Rearrangement inequalities for convolution on groups (68/015–022)

- **Question:**
  - (a) Do the axioms a)–d) of 68/017 imply Condition K (021) for the convolution-stable family they span? Equivalently,
    do f′ ≺ f, g′ ≺ g imply f′ ∗ g′ ≺ f ∗ g for the arranged functions?
  - (b) Which finite and discrete groups carry a system satisfying the axioms: cyclic groups, ℤ, and which others? Is
    the 2-torsion extension G̃ → G with kernel ₂G forced?
  - (c) Settle his symmetry doubt on 020 in general. The S₃ example settles one instance.
- **Why:**
  - His own open question on these sheets.
  - It sits between Hardy–Littlewood's rearrangement theorem and the discrete Riesz–Sobolev inequalities.
  - Finite, checkable cases exist, so computation can test it.
- **Rests on:** SA22-2; 68/015–022; H22-9; the notes R08–R12.
- **Strongest known reduction:**
  - The model case on 017 is checked: symmetric intervals are closed under convolution with nonnegative coefficients.
  - 022 reduces the general claim to a common point of the level sets of all A_i ∗ B_j.
- **Material:**
  - MPL_66+68_002-032, with notes, doubts and records/convolution_examples.json, and scans 015–022;
  - Hardy–Littlewood–Pólya ch. X; Gabriel (1932);
  - a computer search over small groups.
