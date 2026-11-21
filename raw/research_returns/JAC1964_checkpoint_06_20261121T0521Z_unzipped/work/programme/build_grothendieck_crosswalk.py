"""Render an authored locator crosswalk; only coverage checking is automated.

Run JAC1964-20261121. Author /root/programme_audit, GPT-6 Astra Pro.
No archive-image or formal-proof verification is claimed.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path("/workspace/scratch/77a2c5da2d9d")
OUT = BASE / "work/programme"
STAMP = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

ARCHIVE = {
 "A123": "cote 44, scan 2, Th. 1–3 (incidence kernel, dimension bound, quotient and duality); scan 8, letter to Serre of 12 August 1964, first paragraph",
 "A4": "cote 44, scan 2, Th. 4; scan 8, primitive-decomposition margin; scan 9, normalized family z and divisor D=r_*(p*z·q*z)",
 "A5": "cote 44, scan 4, Th. 5 (algebraically trivial restrictions and height/intersection formula), including the margin on general fibrations and a local variant",
 "A6": "cote 44, scan 4, Th. 6: 2i≤n−1 isogeny, 2i=n fixed factor, 2i≥n+1 surjectivity, and the deleted critical finite-kernel clause",
 "A7": "cote 44, scan 6, Th. 7 (numerical equivalence = τ-equivalence; τ is not defined on this leaf)",
 "AODD": "cote 44, scan 8, first paragraph: T_l(J^i) as an odd-cohomology subquotient and dim J^i≤b_(2i−1)/2",
 "LSTR": "cote 16 no. 7, scan 33, B(4), and scans 34, 36, 38, 40: normalized Lefschetz lowering and primitive strings",
 "LSEC": "cote 16 no. 7, scan 40, boxed Λ_Y=φ*Λ_X²φ_*; scan 45, (iv) and (iv bis), algebraic left/right inverses",
 "LMOT": "cote 16 no. 7, scan 49, algebraic inverse corollary and semisimple-motive paragraph; scan 50, weak-Lefschetz variants",
}

SGA = {
 "S6tau": (
  "SGA 6, Exp. XIII, 4.1, printed p. 643, and 4.4, p. 644",
  "Definition/saturation convention for τ; not a theorem identifying higher-cycle numerical and algebraic equivalence",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf",
  "Original printed pages visually checked in this run"),
 "S6div": (
  "SGA 6, Exp. XIII, Theorem 4.6, printed pp. 645–646",
  "Numerically trivial divisors are τ-trivial, in every characteristic",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf",
  "Original printed pages visually checked in this run"),
 "S6index": (
  "SGA 6, Exp. XIII, Theorem 7.1, printed p. 662",
  "Surface divisor index theorem; it is not higher-codimension or arithmetic Hodge index",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf",
  "Original printed page visually checked in this run"),
 "S7exist": (
  "SGA 7 II, Exp. XVII, 2.2 and Theorem 2.5.1, printed p. 217; characteristic-two qualification on printed p. 219",
  "Lefschetz-pencil definition and existence for degree-d multiples, d≥2; even ambient dimension avoids the stated degenerate-quadratic exception",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original existence and qualification pages visually checked; definition also read in primary-content transcription"),
 "EGAaxis": (
  "EGA IV_4, 17.13.7, as explicitly cited in SGA 7 II, Exp. XVII, 2.2",
  "Transverse axis background only",
  "https://grothendiecksga.com/read/sga7/fr/17-2.html",
  "Secondary locator verified in SGA; EGA original theorem was not independently inspected and is not used as a substitute for a proved step"),
 "EGAbc": (
  "EGA III_2, Theorem 7.7.5(I–II), printed pp. 67–68 (continuous pp. 199–200); Proposition 7.7.10, p. 71 (203); Proposition 7.8.4, pp. 73–74 (205–206)",
  "Coherent semicontinuity and base change; on the reduced parameter bases, constant h0 gives local freeness and arbitrary base change, and hence the required section lifting",
  "https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf",
  "Original statements and proof read; statement pages visually checked in this run"),
 "S7cond": (
  "SGA 7 II, Exp. XVIII, 5.3.2, printed p. 287; 5.3.4–5.3.5, p. 288; Proposition 6.2, p. 319",
  "Condition A, extension of direct-image sheaves, and its relation to nontrivial local inertia",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original printed pages visually checked in this run"),
 "S7gauss": (
  "SGA 7 II, Exp. XVIII, Corollary 6.4, printed pp. 320–321, and Lemma 6.4.2.3, p. 321",
  "High-degree condition A and the Euler-characteristic/Chern-class calculation",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original printed pages visually checked in this run"),
 "S7van": (
  "SGA 7 II, Exp. XVIII, Theorem 6.6, printed pp. 323–325",
  "Spanning and conjugacy of vanishing cycles, with the stated dimension/characteristic hypotheses",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original critical statement and proof pages visually checked in this run"),
 "S7irred": (
  "SGA 7 II, Exp. XVIII, Corollary 6.7.2, printed p. 326; finite-index proof, p. 327",
  "Absolute irreducibility after finite-index monodromy restriction in even ambient dimension",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original statement and proof visually checked in this run"),
 "S7inv": (
  "SGA 7 II, Exp. XVIII, 6.6.4, referring to 5.6.10",
  "Ambient-image/invariant-cycle framework; this does not by itself algebraize a trace-factorization correspondence",
  "https://grothendiecksga.com/read/sga7/fr/18-6.html",
  "Primary-content transcription read; no unverified printed-page number supplied"),
 "S7pl": (
  "SGA 7 II, Exp. XV, 3.3.3, printed p. 191; 3.3.4–3.3.6, p. 192",
  "Vanishing generator up to sign and Picard–Lefschetz coefficient (−1)^(r+1) for relative dimension 2r+1",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original printed pp. 191–192 visually checked in this run"),
 "S7biext": (
  "SGA 7 I, Exp. VIII, 4.12.1 and 2.3.11",
  "Symmetric biextension δ(L)=m*L−pr_1*L−pr_2*L and the anticommutative Cartier-duality comparison",
  "https://grothendiecksga.com/read/sga7/fr/8-4.html",
  "Primary-content transcription read; no unverified printed-page number supplied"),
 "S7toric": (
  "SGA 7 I, Exp. IX, 5.5.1–5.5.8, printed pp. 378–379; 9.1–9.2, pp. 418–421; 10.2.3–10.2.8, pp. 440–441; 10.3.5, p. 443; Theorem 10.4, p. 444; 12.5–12.7",
  "Integral all-prime toric monodromy pairing, polarization positivity, ramification factor, and curve normalization",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf",
  "Original lattice, inertia, polarization and positivity pages visually checked; 12.5–12.7 read in primary-content transcription"),
 "S7Griff": (
  "SGA 7 II, Exp. XX, Theorem 4.1, printed p. 355; Remark 4.3, p. 356; §5.1",
  "High-degree hyperplane Griffiths-group obstruction under the theorem's hypotheses; the present application is in characteristic zero",
  "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf",
  "Original theorem and remark visually checked; §5.1 read in primary-content transcription"),
 "S7ret": (
  "SGA 7 II, Exp. XX, 3.3–3.4",
  "Algebraic-retraction condition B and the Lefschetz-lowering mechanism",
  "https://grothendiecksga.com/read/sga7/fr/20-3.html",
  "Primary-content transcription read; no unverified printed-page number supplied"),
}

ROWS = []
def add(ident, title, scope, archive, relation, sga, role, modern, proof):
    ROWS.append({
        "finding_id": ident,
        "finding": title,
        "proved_scope_or_remaining_gate": scope,
        "archive_locator": " | ".join(ARCHIVE[x] for x in archive),
        "archive_relationship": relation,
        "SGA_EGA_FGA_locator": " | ".join(SGA[x][0] for x in sga) if sga else "None used directly; no SGA/EGA/FGA statement of this modern finding is asserted",
        "role_of_SGA_EGA_FGA": role,
        "modern_primary_inputs_and_locators": modern,
        "proof_file": "work/" + proof,
        "SGA_source_keys": ";".join(sga),
    })

direct = "Repaired/proved form of the indicated 1964 programme claim; the new proof is not asserted to occur in Grothendieck"
modern = "Not a statement in Grothendieck; a modern application to the indicated cote/scan"
support = "Not a separate statement in Grothendieck; technical support for the indicated programme claim"
obstruction = "Counterexample or scope obstruction to an unqualified reading of the indicated claim; not attributed to Grothendieck"
none = "No direct SGA/EGA/FGA input. The archive connection is as stated, not an invented source attribution."
saito = "H. Saito, Nagoya Math. J. 75 (1979): Definition 3.1, pp.108–109; Theorem 3.6(i), pp.110–111; §4.1, p.112; Proposition 4.4 and (4.4.2), pp.112–113; Theorem 4.6, pp.113–115"
accepted = "Accepted 032, Corollary 8.4, printed p.50 (abelian Hodge standard and numerical=homological)"
chowlef = "Künnemann, Invent. Math. 113 (1993), Theorems 5.1–5.2 and Corollary 5.3, printed p.96"
height = "Künnemann, Ann. Sci. ENS 34 (2001), §1.2–§1.4, Theorem 1.6 and Corollary 1.7; Amer. J. Math.118 (1996), Lemma 4.1, §5 equation (18), Theorems 6.1 and 8.2, equation (23)"
kahnheight = "Kahn, Refined height pairing, arXiv:2009.00533v7: Proposition 3.8, pp.19–20; Theorem 4.14, p.31; Theorem 5.6, pp.33–35; Lemma 6.1, p.38; Theorem 6.2, pp.38–39; Theorem 6.6, pp.41–42"
kimura = "Kimura (2005), Corollary 7.3 and Example 9.1 (cited background); exact use also checked in Laga–Shnidman, Theorem A proof, author p.8/published p.3026"
powers = "Künnemann (1994), Theorem 3.3.1, as explicitly stated in Ancona–Enright-Ward–Huber (2015), Theorem 4.2.3(3), p.825, and Remark 4.2.1, p.824; the latter primary statement was directly read"
bloch = "Bloch, J. reine angew. Math.350 (1984), Lemma 3.1, p.99; Theorem 4.1, p.104 (infinite order, not only nonzero modulo algebraic equivalence)"
zhang = "Zhang, Gross–Schoen cycles and dualising sheaves (2010): Theorem 1.3.1, p.5; Theorem 1.5.6, p.14; Lemmas 2.1.1 and 2.3.1, pp.17 and 23; Theorem 2.3.5, p.27; Conjecture 2.4.1, p.28"

# The five primitive-incidence results.
add("JAC-T4.1", "Algebraic primitive projector and nondegenerate incidence summand", "Odd-dimensional abelian varieties in every characteristic; rational correspondences and the isogeny category", ["A4","LSTR"], support, [], none, saito+"; Kleiman (1968), Theorem 2A11", "root/T4_proof.tex")
add("JAC-T4.2", "Curve-test transfer to J(C)×A with exact factor (g−1)!", "Algebraic mixed primitive classes; strict signed positivity after accepted 032", ["A4","LSTR"], support, [], none, accepted+"; algebraic h¹(C)≅h¹(J(C)) and Jacobian autoduality, explicitly rederived in the proof", "root/T4_proof.tex")
add("JAC-T4.3", "Signed primitive incidence gives a rational polarization", "P^m(A)_prim for dim A=2m−1, all characteristics; sign (−1)^m and diagonal factor 1/2; no integral/principal claim", ["A4"], direct, ["S7biext"], "Related normalization only; SGA's biextension convention is not the positivity theorem. Positivity is the curve-test deduction.", accepted+"; "+saito+"; Mumford, Abelian Varieties, II §6 Application 1, p.60; III §16 index theorem, p.155", "root/T4_proof.tex")
add("JAC-T4.4", "Actual codimension-two regular representative on abelian threefolds", "Primitive Ab²(A)→P²(A) is an isogeny and its signed incidence class is ample; no universal-representative assertion in every codimension", ["A123","A4"], direct, [], none, "ACMV, Astérisque 455 (2025), §1.1 and §1.3, pp.3–7, Lemmas 1.3–1.4, pp.6–7, Proposition 8.1, pp.41–42; "+accepted, "root/T4_algebraic_representative.tex")
add("JAC-T4.5", "Descent of the primitive incidence polarization", "Arbitrary base fields, including imperfect fields, in the rational/isogeny category", ["A123","A4"], support, [], none, "JAC-P00; Conrad, Abelian Varieties notes, Example 4.2.14, p.38; rational Galois descent, Frobenius twist and norm constructed in the proof", "root/T4_proof.tex")

# Programme deductions P00--P20.
add("JAC-P00", "Rational descent of incidence quotients and Poincaré families", "All fields, including mixed separable/inseparable finite-definition extensions; descent is up to isogeny", ["A123","A6"], support, [], none, saito+"; Conrad, Example 4.2.14, p.38", "programme/sections.tex")
add("JAC-P01", "Odd-cohomology detection of incidence homomorphisms", "A homologically zero relevant odd component acts as zero on P^p; normalized families depend only on H¹(parameter)⊗H^(2p−1)", ["A123","AODD"], direct, [], none, saito+"; faithfulness of rational Tate modules on abelian homomorphisms; divisor-correspondence argument written out", "programme/sections.tex")
add("JAC-P02", "All three Lefschetz restrictions and the critical fixed trace", "B(X) implies low isogeny, critical finite kernel and trace=image, and high surjectivity; all characteristics; critical proof uses actual spread cycles", ["A6","LSEC","LSTR"], direct, ["S7inv","S7ret"], "Related cohomological/algebraic-retraction framework; the trace assertion is proved by rational families plus the blowup formula, not inferred merely from invariant cohomology.", saito+"; Fulton, Intersection Theory, Proposition 6.7(e)", "programme/sections.tex")
add("JAC-P03", "Explicit E³ test: unsigned incidence is indefinite", "Two algebraic families give opposite signs; quotient by the kernel or a common sign does not repair the nonprimitive claim", ["A4"], obstruction, ["S7biext"], "Sign convention only: P=Δ−axes induces the negative of the usual O(0) polarization. The E³ counterexample is computed directly.", "Explicit Chow correspondences z_±=P_(t,1)(a₂±a₃), with divisor incidences ±2P", "programme/sections.tex")
add("JAC-P04", "E⁴ hyperplane restrictions expose the homological/algebraic domain gap", "Characteristic zero and sufficiently high-degree Lefschetz sections; primitive α=(a₁−a₂)(a₃−a₄) restricts homologically but not algebraically trivially", ["A5","AODD"], obstruction, ["S7Griff","S7gauss","S7irred"], "Direct application of XX Theorem 4.1/Remark 4.3 with their hypotheses verified; not an all-characteristic Griffiths claim.", "Explicit α²=4 and hα=0 calculation; abelian hard Lefschetz and algebraic retraction", "programme/sections.tex")
add("JAC-P05", "CM Fermat counterexample to numerical=τ in characteristic zero", "Fermat-quartic Jacobian: rationally nonzero Griffiths class; τ interpreted as saturation of algebraic equivalence", ["A7"], obstruction, ["S6tau","S6div"], "XIII supplies the τ convention and its divisor boundary only. The higher-cycle counterexample is Bloch's, not a theorem of SGA.", bloch, "programme/sections.tex")
add("JAC-P06", "Algebraically trivial cycles over Fbar_p are torsion", "Integral algebraically trivial classes become zero rationally; this is a preliminary fact, strengthened by P15 to full CH=num for abelian type", ["A7"], support, ["S6tau"], "Interpretation of τ as saturation only; the torsion argument uses curve Jacobians over finite fields.", "Finite fields contain every point of an abelian variety over Fbar_p; curve-family description of algebraic equivalence", "programme/sections.tex")
add("JAC-P07", "Automatic condition A for genuine abelian Lefschetz pencils", "All characteristics, even ambient dimension n≥2: dim E=h^n−Catalan_n>0, hence all local vanishing cycles are nonzero", ["A5","A6"], support, ["S7cond","S7gauss","S7van","S7irred"], "Direct use of Euler characteristic, spanning/conjugacy and condition A; the Catalan formula and positivity estimate are the deduction.", "Abelian Betti numbers and Riemann–Roch h^n=n!h⁰(L); explicit binomial identity", "programme/H9_T6a.tex")
add("JAC-P08", "Algebraic lowering for complete intersections and products", "All characteristics; supplies B(X) in the specified complete-intersection/product cases, not a new Hodge-standard assertion", ["LSEC","LMOT","A6"], direct, [], none, "Weak and hard Lefschetz, explicit algebraic Lefschetz strings and tensor-product lowering; comparison with cote16 normalized convention", "programme/H9_T6a.tex")
add("JAC-P09", "Geometric-generic high-degree axis has no variable algebraic classes", "Degree d≥3 in the stated ordered-pair construction; all characteristics; geometric generic axis only, not every k-valued member", ["A5","A6"], modern, ["S7van"], "Vanishing-cycle framework only; the required large orthogonal monodromy is Katz–Pandharipande, not XVIII finite-index symplectic irreducibility.", "Katz–Pandharipande, Inequalities related to the vanishing cycles of Lefschetz pencils, Theorem 0, p.2, Corollaries 2–3, p.3; finite-orbit argument proved here", "programme/generic_axis.tex")
add("JAC-P10", "Exact stable Fermat Hodge-lattice index and Faltings-height gap", "At 2, determinant gain 7/4 and h_F(J)−Σh_F(E_i)=log(2)/4; no node-thickness value is inferred", ["A5"], modern, [], none, "Liu, Algebraic Geometry and Arithmetic Curves, Proposition 10.4.37, p.547, Example 10.4.39, pp.548–549; Rémond (2021), Proposition 2.1, pp.2–3; explicit local-chart and differential calculation", "programme/fermat_hodge_lattice.tex")
add("JAC-P11", "Positive two-dimensional CM orbit plane", "Qη⊕QTη is positive and independent even modulo algebraic equivalence; this does not span the whole Chow group by any proved assertion", ["A5","A7"], modern, [], none, "AR-13; Milne, Abelian Varieties (2008), Proposition 14.2, p.61, Theorem 14.3, p.62; exact Chow action T²=−1", "programme/fermat_cm_orbit.tex")
add("JAC-P12", "The tautological ring does not enlarge the primitive grade-one line", "For the hyperflex-normalized Fermat curve, its ordinary tautological primitive grade-one part is the indicated Ceresa line; not the whole Chow group", ["A5","A7"], modern, [], none, "Polishchuk, arXiv:math/0504448v3, Theorem 0.2(i), p.2, Remark 2 after Corollary 0.3, p.3, grading conventions p.4", "programme/fermat_cm_orbit.tex")
add("JAC-P13", "Canonical actual invariant Chow summand N=h³(J)^G", "Exact Chow idempotents, Q(i)-module and Hermitian form on all CH²(N); finite-dimensionality gives no dimension bound on that group", ["AODD","LMOT","A5"], modern, [], none, kimura+"; "+chowlef, "programme/fermat_motive_structure.tex")
add("JAC-P14", "Full endomorphism algebra acts on N through its determinant", "On the exact Chow summand, a matrix with determinant u+iv acts as u−vT; the End⁰(J) orbit of η remains its one Q(i)-line", ["AODD","LMOT","A5"], modern, [], none, powers+"; "+kimura+"; exact tensor projector calculation", "programme/fermat_motive_structure.tex")
add("JAC-P15", "Finite-field rational Chow=numerical for geometric abelian type", "Accepting full abelian Tate from 032/Milne: finite fields and Fbar_p, all codimensions, and the stated rational higher-K vanishing over finite fields; no assertion CH=num after an arbitrary transcendental extension", ["A7","LMOT"], direct, ["S6tau"], "τ convention only. The finite-field theorem is Kahn plus the accepted Tate input, not SGA XIII's divisor theorem.", "Kahn, Ann. Sci. ENS 36 (2003), Definition 1/Theorem 1, p.978; Proposition 1.5, Lemma 1.6, Proposition 1.7, p.981; Lemma 1.9, Theorem 1.10, Corollary 2.2, p.982; accepted 032 Corollary 8.3, pp.49–50, and supplied Milne Theorem 3.1, p.6", "programme/finite_field_chow.tex")
add("JAC-P16", "B(X) and numerical=homological for geometric abelian-type varieties", "All fields and all powers X^a; all-prime algebraic Künneth projectors and ample Lefschetz inverses over the ground field; no positivity of X's own primitive form inferred", ["LMOT","LSEC","A6"], direct, [], none, accepted+"; Jannsen, Invent. Math.107 (1992), Lemma 1/Theorem 1, p.448, semisimplicity proof p.449; trace and finite-definition descent written out", "programme/abelian_type_lefschetz.tex")
add("JAC-P17", "Actual fields of definition of N, η and T", "N and η descend to Q; the relevant CM action T is defined over Q(i); exact plus/minus twist and invariant/anti-invariant Chow decomposition", ["AODD","A5"], modern, [], none, "BDP (2017), §5.2, author pp.24–25; exact Fermat automorphisms, torsion translations, norm descent and Chow correspondences; P13–P14", "programme/fermat_field_descent.tex")
add("JAC-P18", "A curve-times-J fourfold obstruction to algebraic-radical vanishing", "A nonzero algebraically trivial class of N gives nonzero homologically trivial Z in (π₁C⊗π_N)CH²(C×J), supported in product π₄; Murre(D) there would suffice, no converse", ["A123","AODD","A5"], modern, [], none, "ACMV, Parameter spaces for algebraic equivalence, Proposition 3.5/Lemma 3.9, author pp.4–7; exact projector argument; Xu–Xu arXiv:1110.0668 Corollary 3.9, p.9, only supplies A/B, not the missing D", "programme/fermat_fourfold_radical.tex")
add("JAC-P19", "An ample complete-intersection axis has no abelian rational domination", "Every characteristic, positive-dimensional smooth geometrically integral ample complete intersections in an abelian variety. This rules out one geometric transfer route; it neither excludes abelian-type motives nor closes the fixed-axis sign gate.", ["A5"], obstruction, [], none, "Milne, Abelian Varieties v2.00(2008), ChapterI Theorem3.2,p17 and Corollary3.7,p19; adjunction from the conormal sequence; actual finite-cover primitive-form identity stated separately as a conditional transfer criterion", "programme/axis_abelian_domination.tex")
add("JAC-P20", "Actual total-cohomology injection from an abelian-type Chow splitting", "An actual Chow splitting into twisted abelian motives yields an algebraic injection into one abelian product using distinct elliptic Kunneth tags. Hodge-standard transfer is stated only conditionally on Milne2022 Proposition4.2, whose form-compatibility step was not re-established in this audit; no main-gate closure.", ["A5","A6","LMOT"], modern, [], none, "Milne LFF v1.1(2022), Proposition4.2,pp7-8 and Theorem4.5,p8; Kleiman1968 Section1.3,pp364-365 and Theorem3.11,pp380-381; Saavedra1972 VI4.2.0,p363, VI4.4.2,p373, AppendixA3,pp400-401. Original references directly checked; their extra geometric-positivity assumptions are retained in the audit.", "programme/milne_transfer_audit.tex")

# Geometric heights, local corrections and monodromy.
add("H9-C1", "Ordinary quadric pencil refutes the uncorrected height identification", "All characteristics in the displayed ordinary-pencil model: nonzero primitive intersection, zero rational generic restriction, two nonzero local corrections", ["A5"], obstruction, ["S7exist","S7cond"], "The pencil satisfies the precise Lefschetz definition but has zero vanishing cohomology; geometrically integral fibres alone do not remove higher vertical cycles.", "Direct quadric Chow/ruling calculation; local correction matrix rederived", "h9/H9_results.tex")
add("H9-T1", "Corrected height formula with a vertical intersection matrix", "Admissible extensions; higher-dimensional vertical cycles included; signed correction to the naive ambient intersection", ["A5"], direct, [], none, "Kahn, Refined height pairing, Definition 2.2, Proposition 2.8 and equation (2.9); Shioda, On the Mordell–Weil lattices, Theorem 8.6, equations (8.11)–(8.15), p.228, for the curve case", "h9/H9_results.tex")
add("H9-T2", "Specialization injectivity removes local height corrections", "All characteristics under the stated H^(2m) specialization injection; condition A suffices, and P07 makes it automatic for genuine abelian pencils", ["A5"], direct, ["S7cond","S7pl"], "Direct local-cohomology input; cap-product admissibility and the height identity are proved in the fragment.", accepted+"; admissible geometric height construction", "h9/H9_results.tex")
add("H9-T3", "Exact quotient/radical statement and the domain correction", "A proved comparison with a polarized Lang–Néron quotient gives rad=kernel; no map from all homologically trivial cycles to the algebraic incidence quotient is assumed", ["A123","A5"], obstruction, ["S7Griff"], "XX Theorem 4.1/Remark 4.3 supports the explicit domain obstruction; the positive-quotient implication is linear algebra plus Néron–Tate positivity.", "Lang–Néron and Néron–Tate positivity; JAC-P04", "h9/H9_results.tex")
add("H9-T4", "Polarization of the fixed primitive part of a smooth ample section", "Any smooth ample Y in an even-dimensional abelian X, all characteristics; only the fixed primitive incidence factor", ["A4","A6","LSEC"], direct, ["S7inv"], "Fixed/variable cohomological framework; the sign is transferred to J(C)×X and uses accepted 032, not an HSC assumption for Y.", accepted+"; "+saito+"; explicit algebraic retraction j*L^−1j_*", "h9/H9_results.tex")
add("H9-T5", "One out-of-range Newton slope kills the variable incidence factor", "Conditional on a smooth finite-field fibre with a variable slope outside [m−1,m] and the stated finite-index irreducibility; existence of such a witness is not proved", ["A4","AODD"], support, ["S7irred"], "Monodromy hypothesis has this exact standard-pencil locus. The Newton exclusion is a separate Frobenius/good-reduction argument.", "Néron–Ogg–Shafarevich criterion and integrality of Frobenius eigenvalues γ and q/γ; no complex-absolute-value inference", "h9/H9_results.tex")
add("H9-L1", "A rational scalar locally square at almost every prime is positive", "Elementary all-prime square-class lemma; one l-adic square alone never determines a real sign", ["A4"], support, [], none, "Direct bounded-partial-sums/Euler-product proof using a nonprincipal quadratic Dirichlet character; no GRH", "h9/H9_monodromy.tex")
add("H9-L2", "Positive rational rank-one toric monodromy coefficient", "Semistable abelian reduction of toric rank one: N_l(x)=−q₀E₀(x,v₀)v₀ with one q₀∈Q_>0 for all l", ["A4","A5"], support, ["S7toric","S7biext"], "Direct derivation from the integral pairing, the precise polarization direction and the curve normalization; q₀=u/s=(us)/s².", "No additional conjectural input; the coordinate/sign conversion is the deduction", "h9/H9_monodromy.tex")
add("H9-T6", "Variable incidence polarization from all-prime monodromy", "All characteristics under the explicitly stated projector, absolute-irreducibility and nonzero-vanishing-cycle hypotheses", ["A4"], direct, ["S7pl","S7irred","S7toric","S7biext"], "Direct all-prime comparison a_l²=q₀/(ec) plus H9-L1 forces the single rational incidence scalar c>0.", saito+"; H9-L1 and H9-L2", "h9/H9_monodromy.tex")
add("H9-T6a", "Concrete generic-pencil primitive polarization theorem", "All characteristics: variable part when B(X) holds; full primitive part for abelian X accepting 032; full P^m for even-dimensional projective complete-intersection ambient X", ["A4","A6","LSEC"], direct, ["S7exist","S7van","S7irred","S7pl","S7toric"], "Direct verification of the hypotheses of H9-T6; d≥2 multiples supply genuine pencils; a separate condition A assumption is unnecessary when the variable incidence factor is nonzero.", accepted+"; JAC-P08 for complete intersections; "+saito, "programme/H9_T6a.tex")
add("H9-T7", "Whole original-pencil height quotient equals ambient plus axis forms", "Every homologically trivial generic cycle is admissible; quotient by globally homologically trivial restrictions is A_X⊕A_B with signed intersection forms; arbitrary-axis sign remains separate", ["A5","A6","LSEC"], modern, ["S7cond"], "Condition A controls all vertical classes and admissibility, automatically available for the abelian pencil by P07.", "Fulton, Intersection Theory, Proposition 6.7(e); "+accepted+"; explicit vertical-class lemma and algebraic Lefschetz correction", "h9/H9_full_height.tex")
add("H9-T8", "Complete all-homological height positivity for abelian-fourfold pencils", "Original rational pencil field, all characteristics: the axis is a surface; exact radical is the globally homologically trivial restriction group", ["A5"], modern, ["S6index","S6div","S7cond"], "Direct all-characteristic surface index theorem and numerical=homological for divisors, combined with H9-T7.", accepted, "h9/H9_full_height.tex")
add("H9-T8a", "Arbitrary original-pencil axes in characteristic zero", "All dimensions in characteristic zero, including large algebraically closed fields via finite-type descent; exact radical from H9-T7", ["A5"], modern, ["S7cond"], "Only the admissibility input is SGA. Positivity of the axis form is classical Hodge–Riemann, not a new SGA consequence.", "Griffiths, Publ. Math. IHES 38 (1970), §2 (2.3)', p.132, VI (2.7), p.133", "root/H9_characteristic_zero_axis.tex")
add("H9-T8b", "Exact reduction of the fixed-axis sign to finite fields", "In each positive characteristic and dimension, strict positivity or weak nonnegativity on the actual axis Gysin kernel over all algebraically closed fields is equivalent to the corresponding finite-field-axis test. No finite-field sign is proved.", ["A5","LSTR"], modern, [], "Smooth proper base change and cycle-class compatibility are used through the exact primary Milne exposition listed; no unverified original SGA locator or reverse algebraic specialization is asserted.", "Milne, Polarizations and Grothendieck's standard conjectures (2002), Theorem3.3 proof,pp607-608; Milne, Lectures on Etale Cohomology v2.21, Theorem20.2,p127, Proposition20.3,p128, Section23 Theorem23.4 and properties(a),(b),p142; explicit lisse Gysin-kernel persistence", "root/H9_finite_field_axis_reduction.tex")
add("H9-T9", "Incidence height descends exactly to the Lang–Néron quotient", "Algebraically trivial cycles whose incidence image lies in a polarized factor B; all characteristics; radical is the preimage of the K/k-trace points", ["A123","A4","A5","A6"], direct, [], "No direct SGA result replaces the height comparison. The primitive-polarization input may be supplied upstream by H9-T6/T6a.", kahnheight+"; degree-zero adjointness reduced using T×P^(m−1); JAC-P00", "h9/H9_incidence_height.tex")
add("H9-T10", "Actual Ab² for generic threefold sections", "Generic Lefschetz threefold sections of an abelian fourfold, all characteristics; actual regular representative comparison and primitive polarization up to isogeny", ["A123","A4"], direct, ["S7pl","S7irred","S7toric"], "Inherited directly through the repeated variable-factor monodromy proof; no unproved all-codimension representative is substituted.", "ACMV, Astérisque 455 (2025), Lemmas 1.3–1.4, pp.6–7, Proposition 8.1, pp.41–42; "+accepted, "h9/H9_regular_threefold.tex")
add("H9-T11", "Elliptic-product reduction with an exact numerical kernel", "Conditional on an algebraic primitive projector and primitive incidence positivity for X×E; yields positivity modulo numerical equivalence, and HSC only with D(X)", ["A4","LMOT"], direct, ["S7biext"], "Curve sign convention only; the separate D(X) requirement is not inferred from incidence positivity.", "Explicit Z⊠P_E family and incidence testing against every complementary cycle; accepted 032 supplies D only in its proved range", "h9/H9_elliptic_reduction.tex")
add("H9-T12", "Finite-base-change norm decomposition and preserved primitive trace", "Purely inseparable rational Chow invariance; general finite-extension norm splitting on admissible groups; all-hom admissibility for separable covers unramified above critical values", ["A5","A6"], modern, ["S7cond"], "Condition A controls admissibility of those separable covers. No full-hom positivity after every finite cover is claimed; T17 refutes it.", "Kahn, Proposition 3.9, pp.20–23, equations (3.13)–(3.14); Proposition 4.12(c), p.30; Theorem 4.14(b), p.31; explicit res–norm identities", "h9/H9_base_change.tex")
add("H9-T13", "Primitive polarization for generic odd complete intersections", "Any smooth preceding section chain in an abelian variety and a genuine terminal Lefschetz pencil; all characteristics; m=2 includes actual Ab²", ["A4","A6","LSEC"], direct, ["S7exist","S7van","S7irred","S7pl","S7toric"], "Terminal-pencil monodromy plus fixed-part transfer with factor (g+c−1)!/c!; no application to the nonample product-axis construction.", accepted+"; ACMV Lemmas 1.3–1.4 and Proposition 8.1 for m=2; algebraic inverse of L^c on the abelian ambient variety", "h9/H9_complete_intersections.tex")
add("H9-T14", "Constant finite-field varieties after arbitrary extension", "P15 plus spreading gives numerical=homological=algebraic equivalence for constant abelian-type varieties over every extension of Fbar_p, and the stated geometric-isogeny variant; constant odd abelian primitive height quotient is Hom(J(C),B)_Q", ["A7","A5","A6"], modern, ["S6tau"], "τ interpretation only. Rational Chow=numerical is not claimed over arbitrary transcendental extensions; algebraic equivalence is the conclusion.", "Kahn (2003), Theorem 1.10, p.982, via P15; ACMV, Parameter spaces, Theorem A.1(1),(4), p.17, Lemma 3.8(2), p.6; H9-T9", "h9/H9_constant_finite_field.tex")
add("H9-T15", "Conductor-correct CM Selmer rank", "Actual Fermat character over Q(i) and induced motive over Q; uses the proved Katz unit, not a theorem whose conductor hypotheses fail", ["AODD","A5"], modern, [], none, "Castella, Katz p-adic L-functions (2025), §2.1 pp.5–6, Theorem 2.2.1 pp.7–8, Theorem 4.2.1 p.16, Theorem 4.3.1 p.17; BDP §5.2 pp.24–25; AR-19", "h9/H9_conductor_selmer.tex")
add("H9-T16", "Semistable axis degeneration and precise nonlifting obstruction", "Corrected normal-crossing model and surviving cohomological/Chow blocks; no inference that a special algebraic cycle lifts to the generic fibre", ["A4","A5","LSEC"], obstruction, [], "No exact SGA/EGA/FGA reverse-Chow-specialization theorem is asserted; the relevant weight-complex inputs are the modern sources listed.", "T. Saito, Weight spectral sequences and independence of l, Corollary 2.2.4 p.21, Proposition 2.2.6 pp.23–24, specialization Proposition 2.4.4 pp.35–36; T. Ito, Theorem 1.1(1), p.2; Stacks 0GU4 for the Chow envelope sequence", "h9/H9_semistable_axis.tex")
add("H9-T17", "Finite covers can create an indefinite norm-zero height plane", "All characteristics: explicit E⁴ cover has orthogonal norms 4d and −12d³; full all-hom semipositivity after arbitrary covers is false. General positive Albanese-primitive side remains characteristic zero.", ["A5"], obstruction, ["S7cond","S7exist"], "SGA supplies genuine pencils and admissibility after covers unramified above critical values, not a positivity theorem for every finite cover.", "Zhang, Hodge index for algebraic cycles on threefolds, arXiv:1001.4788, Theorem 1 (characteristic zero); Kahn Lemma 6.1 and Theorems 6.2, 6.6; direct Poincaré intersections and norm calculation", "h9/H9_threefold_cover_sign.tex")
add("H9-T18", "Finite-cover primitive positivity is exactly a variable fourfold form", "Abelian-fourfold pencils with the stated separable covers: fixed primitive part is positive by 032, remaining sign equals the algebraic form on ker k_* in H⁴ of the incidence fourfold", ["A4","A5","LSEC"], modern, ["S6index","S6div","S7cond"], "Divisor index and condition A enter the correction/primitive argument; no HSC for the variable incidence-fourfold block is inferred from its abelian-type ambient space.", accepted+"; Kahn Theorems 6.2 and 6.6; H9-T12; exact correction and converse constructions", "h9/H9_cover_variable_gate.tex")
add("H9-T19", "Geometric-generic tame cyclic rational covers add no height directions", "t=y^N+s, N prime to the characteristic, s transcendental: h_L=N^−1 h_K(cor,cor), entire norm kernel in the height radical; no special-cover or Chow-kernel-vanishing assertion", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Condition A and finite-index irreducibility are direct inputs. New moving-branch irreducibility uses Katz middle convolution, not an invented SGA orthogonal-monodromy theorem.", "Katz, Rigid Local Systems, corrected author manuscript: Theorem 2.9.7 ch.2 p.30/PDF67; Corollary 3.3.6 ch.3 pp.14–16/PDF107–109; Theorem 4.3.11 ch.4 p.9/PDF122; §5.1.1–5.1.7 ch.5 pp.1–4/PDF123–126", "h9/H9_generic_cyclic_cover.tex")
add("H9-T19a", "Full geometric-generic degree-N rational-map cover extension", "Geometric generic point of Hom_N(P¹,P¹) unramified above critical values; exact height norm formula via the lisse projector and cyclic subfamily; not every rational map", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Inherited direct SGA inputs through T19; the passage from cyclic subfamily to generic rational maps is a separate projector/monodromy deduction.", "Katz locators of H9-T19; finite push–pull projector 1−Q*Q_*/N and finite-orbit argument; parent review status recorded separately", "h9/H9_generic_cyclic_cover.tex")
add("H9-T20", "Generic positive-genus Kummer covers have the exact height norm formula", "u^N=(t−s)∏(t−b_i), B=Nq₀, N prime to p, s geometric generic; genus B(N−1)/2; exact height norm/radical, including the fixed ambient H¹(C) term; full generic branch-space extension and every generic hyperelliptic genus when p≠2", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Inherited condition-A and monodromy inputs from T19. Both fixed and variable moving Kummer pieces require the separately cited Katz middle-convolution argument; no result for every specialized cover is asserted.", "Katz, Rigid Local Systems, Theorem 2.9.7, Corollary 3.3.6, Theorem 4.3.11 and §5.1.1–§5.1.7 at the exact manuscript/PDF locators of T19; explicit tame normalization and push–pull calculation; independent root and programme whole-proof checks passed", "h9/H9_generic_positive_genus_cover.tex")
add("H9-T21", "Wild rational scaling and every generic rational-cover degree", "In characteristic p, t=(y^p−y)/s has the exact height norm/radical; lisse-kernel tower induction then proves the formula for the geometric generic degree-N rational map for every N≥2 in every characteristic. No claim for every specialized cover.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "SGA supplies the old pencil's condition A, transvections and finite-index irreducibility. Wild moving-parameter monodromy is the Fourier-transform theorem of Katz listed separately.", "Katz, Exponential Sums and Differential Equations, corrected manuscript: §7.3.3–7.3.6 ch.7 pp.10–12/PDF210–212; Theorem 7.3.8 and Lemma 7.3.9 pp.12–13/PDF212–213; Theorem 7.4.3, Corollary 7.4.3.1, Theorem 7.4.4 pp.16–18/PDF216–218; Lemma 7.5.1, Theorem 7.5.4 pp.19–22/PDF219–222; exact Chow and lisse-tower deduction", "h9/H9_wild_rational_covers.tex")
add("H9-T22", "Wild simple-pole covers and every generic hyperelliptic genus", "Degree-p Artin–Schreier covers with b+2 simple poles have genus (p−1)(b+1) and exact height norm/radical; full char2 double-cover presentation space gives every geometric generic hyperelliptic genus. Together with T20 this is all characteristics; special-cover counterexamples remain.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Old-pencil SGA inputs are inherited through T21; Fourier-monodromy, the actual wild normalization, and the full double-cover parameter argument are distinct steps, not an attributed SGA theorem.", "Katz ESDE, Theorem 7.3.8(3), Lemma 7.3.9, Corollary 7.4.3.1/Theorem 7.4.4 and Theorem 7.5.4 at the precise T21 locators; explicit rank-two algebra splitting by H¹(P¹,O(g+1))=0, branch charts, and Cartier basis", "h9/H9_wild_positive_genus_covers.tex")
add("H9-T23", "Cyclic triple-cover families of every genus at least two", "Every characteristic and every g≥2: explicit geometric-generic degree-three cover families have the exact 1/3 norm-height formula and corestriction radical. No genus-one cubic or full Hurwitz-space assertion.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Inherited condition A, transvections and finite-index irreducibility concern the original pencil. Moving Kummer or Artin–Schreier monodromy is supplied by Katz, not by a new SGA assertion.", "Katz Rigid Local Systems, Theorem 2.9.7, Corollary 3.3.6, Theorem 4.3.11, §5.1.1–5.1.7 at the T19 locators; Katz ESDE, Theorem 7.3.8(3), Lemma 7.3.9, Corollary 7.4.3.1, Theorems 7.4.4 and 7.5.4 at the T21 locators; explicit characteristic-three double-pole normalization and different exponent six", "h9/H9_triple_cover_families.tex")
add("H9-T23a", "Composite positive-genus cover families in degrees 2M and 3M", "Every characteristic: degree 2M and every genus g≥1, or degree 3M and every g≥2, with exact inverse-degree norm-height formula. Geometric-generic composite families only, not all Hurwitz components.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl"], "Inherited condition A, transvections and finite-index irreducibility concern the original pencil. Moving Kummer or Artin–Schreier monodromy is supplied by Katz, not by a new SGA assertion.", "H9-T20–T23 and the Katz loci recorded there; actual lisse trace-kernel decomposition, section-surjectivity on fundamental groups, and generic-fibre monodromy argument written in the proof", "h9/H9_triple_cover_families.tex")
add("H9-T24", "Full generic triple-cover space in every genus at least two", "Every characteristic and g≥2: the fixed-target smooth connected triple-cover stack unramified over the pencil critical set is irreducible with a dense balanced cubic-form parameter space; its geometric generic cover has the exact 1/3 norm-height formula. No genus-one or every-special-cover assertion.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl","EGAbc"], "Original-pencil condition A and finite-index monodromy are inherited through T23. Direct EGA coherent base change supplies local freeness and the lift of a cubic section along the balancing extension.", "Wood, Algebra & Number Theory5:8(2011), Theorem2.1 and equation(1), printedpp1073–1074; Conrad, Applications of base change for coherent cohomology, Theorem1.1 and Corollary1.2,p1; the prior T23 Katz loci; explicit splitting, extension-class balancing and lisse-kernel proof", "h9/H9_generic_triple_covers.tex")
add("H9-T25", "Full generic covers above the nonspecial degree bound", "Every characteristic: N>2g−2, with even N and g≥1 or 3 dividing N and g≥2. The full fixed-target smooth-cover stack is irreducible and its geometric generic cover has exact 1/N norm height and norm-kernel radical. No arbitrary-special-cover assertion.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl","EGAbc"], "The original-pencil monodromy is inherited through T23a. Direct EGA coherent base change makes the two-section parameter a vector bundle and permits its universal construction.", "Deligne–Mumford (1969), The irreducibility of the space of curves of given genus, §1,p78 and §3,pp92–96; Stacks Project Lemma105.6.1,tag072T; T23a and the actual ordered-divisor parameter proof", "h9/H9_generic_high_degree_covers.tex")
add("H9-T26", "Full generic elliptic triple covers by Radon transform", "Every characteristic, geometric generic genus-one degree-three cover unramified over the original pencil's critical set: exact 1/3 norm height and corestriction radical. No assertion for every specialized cover.", ["A5","A6"], modern, ["S7cond","S7irred","S7pl","S7exist"], "The original pencil uses condition A and finite-index irreducibility. The ordinary-node formula is tensored with the lisse coefficient stalk; cubic-pencil existence and monodromy handle the fixed ambient block. Radon simplicity is a separate modern input.", "Laumon, Transformation de Fourier homogene, Bull.Soc.Math.France131(2003), Section1.2,p529, Proposition1.6,p532, Lemma5.6,pp547-548, Proposition5.7,p549, Corollary5.8,p550; actual global constant splitting and local-coefficient node calculation proved in the fragment", "h9/H9_generic_elliptic_triple_covers.tex")

# Arithmetic height deductions. These are modern continuations, not SGA statements.
add("AR-1", "Primitive Beauville-grade reduction of the height question", "Odd-dimensional abelian varieties over number fields: only grade one can contribute to the middle self-height; exact reduction, no general negative-grade vanishing assumed", ["A4","A5","LSTR"], modern, [], none, chowlef+"; "+height, "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-1a", "No extra lower-grade radical on an abelian threefold", "Fourier grading eliminates the possible negative/irrelevant grades in codimension two; does not prove grade-one AJ injectivity", ["A5","LSTR"], modern, [], none, "Beauville, Math. Ann.273 (1986), Fourier grading/inversion; Künnemann (1993), §2, p.88; explicit degree argument", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-2", "Exact orthogonal Picard Chow summand and remaining complementary gate", "CM abelian varieties under accepted032: actual Chow splitting M⊥N, strict positivity on the Picard part, remaining primitive grade-one height on CH^m(N)", ["A123","A4","A5","LMOT"], modern, [], none, "Accepted 032 Theorem 1.1, Lemma 8.1, Corollary 8.2 and its proof; Milne, AV110, Proposition 16.10 p.65; "+height+"; "+chowlef, "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-3", "Explicit CM group-algebra complementary motive", "Actual rational Chow projector in a CM elliptic cube, with rank-two (3,0)+(0,3) realization and homologically trivial grade-one CH²", ["AODD","A5","LMOT"], modern, [], none, "Explicit finite group average and abelian Chow–Künneth action; "+chowlef, "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-4", "Elementary analytic central-sign lemma", "Under its holomorphy, functional-equation and zero-free/right-half-line assumptions; not a general motivic L-function theorem", ["A5"], modern, [], none, "Direct complex-analysis/real-sign argument; supplied GRH input is used only when its own character/range hypotheses apply", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-5", "Conditional implication from a positive-normalization height identity", "If a proved identity h=C·L'(center), C>0, and AR-4's hypotheses hold, then the asserted height sign follows; the identity is an explicit remaining hypothesis", ["A5"], modern, [], none, "AR-4; no unproved Fermat automorphic-height identity is promoted to a theorem", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-6", "Exact arithmetic slope-method gate", "A specified metrized height line and comparison/norm estimate would imply the sign; construction alone does not give the estimate", ["A5"], modern, [], none, "Bost, Publ. Math. IHES 93 (2001), §4.1.4, Propositions 4.5–4.6, equations (4.11),(4.14); AR-10 supplies the actual line", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-7", "A nonzero Fermat class in the complementary motive", "Actual rational codimension-two class, infinite order modulo algebraic equivalence; nonvanishing itself supplies no height sign", ["A7","AODD","A5"], modern, ["S6tau"], "τ convention only; the nonzero Griffiths class is Bloch's theorem.", bloch+"; Beauville Fourier grading; AR-2", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-8", "Exact Fermat symmetry and Gross–Schoen height formula", "η=Fourier(X₁) lies in the exact complement and h(η,η)=h(Δ)/6=7Ω/24−Φ/6; hyperflex normalization essential", ["A5"], modern, [], none, zhang+"; explicit μ₄² action and torsion-translation Chow argument", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-9", "Positive finite-local Fermat contribution", "Stable star (0eee) at 2: b_v≥δ_v/21, φ_v=4δ_v/3, global h(η,η)≥D₂/6+7A∞/2; node thickness is not guessed", ["A5"], modern, [], none, "de Jong, On the height of Gross–Schoen cycles in genus three (2018), Theorem 8.2, Lemma 11.2, Example 5.4; Zhang (2010), Proposition 4.4.1, pp.58–59; Liu Example 10.4.39, pp.548–549", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-10", "Actual canonical adelic line representing the primitive height", "Exact arithmetic-degree realization of the signed middle height; does not itself prove that degree positive", ["A5"], modern, [], none, "Gu, arXiv:2609.33223v2, Theorem 1.3, Proposition 5.3, §2.2 and Corollary 1.6; exact convention comparison in the proof", "root/AR10_adelic.tex")
add("AR-11", "Positive central derivative of the actual Fermat L-function", "Conductor 64 rank-two CM motive: elementary L'(M,2)>7/20, independently enclosed numerical refinement; no L'-height comparison asserted", ["A5","AODD"], modern, [], none, "BDP (2017), §5.2, author pp.24–27, actual Hecke characters/conductors/root number; Mellin and elementary tail estimate proved here", "arithmetic/FERMAT_LDERIVATIVE_SIGN.tex")
add("AR-12", "Exact archimedean theta-integral reduction and Fermat period matrix", "All constants fixed; correct symmetric period matrix obtained from the general formula, not the asymmetric specialized printed display", ["A5"], modern, [], none, "de Jong (2020), Theorem A and equation (5), pp.1389–1390; §4.5 p.1401, §5.1–5.4 pp.1404–1406; de Jong (2018), §§3,8; Guàrdia (2001), Proposition 5 p.160; DLMF 19.8.11–12", "arithmetic/FERMAT_THETA_GATE.tex")
add("AR-13", "Certified strict positivity of the specified Fermat cycle", "Normalized real height h(η,η)>1/100 via exact finite lattice and one-sided enclosed theta estimates; not the whole CH²(N)", ["A5"], modern, [], none, "AR-8/AR-9/AR-12 and P10; de Jong theta identities at the locators in AR-12; deterministic Arb certificate and independently checked tail/mean bounds", "arithmetic/FERMAT_THETA_CERTIFICATE.tex")
add("AR-14", "Positive arithmetic subspace containing a Griffiths class", "Orthogonal Picard-positive subspace plus Qη (and subsequently the CM plane of P11); no statement that these exhaust all cycles", ["A123","A4","A5"], modern, [], none, "AR-2 and AR-13, with the exact self-transpose Chow splitting", "arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex")
add("AR-15", "Algebraically trivial complementary cycles lie in the entire height radical", "No level-one Hodge substructure in N; signed height descends to Griff^m(N); strict positivity would also require algebraic radical=0", ["A123","A5","A7","AODD"], modern, [], none, "ACMV, Astérisque 455 (2025), §3.2.4 equation (3.5), pp.17–18; "+height+"; only divisor AJ injectivity on an auxiliary curve is used", "arithmetic/FULL_CHOW_GATE.tex")
add("AR-15a", "Grade-zero parameter-Jacobian obstruction for the algebraic radical", "Curve families project to a specific homologically trivial grade-zero correspondence on a Jacobian product; no general Murre(D) or AJ injectivity inferred", ["A123","AODD","LMOT"], modern, [], none, "Abelian Chow–Künneth/Fourier grading; Vial's A/B/C'/D scope is audited separately; P18 gives the sharper C×J fourfold obstruction", "arithmetic/ALGEBRAIC_RADICAL_GRADE_ZERO.tex")
add("AR-16", "Scalar-extended Abel–Jacobi injectivity would close the rank gate", "A criterion over a field with the actual N,T,η defined; Selmer dimension alone is insufficient without injectivity of CH²(N)⊗Q_p→H¹_f", ["AODD","A5"], modern, [], none, "Nekovář, p-adic Abel–Jacobi maps and p-adic heights, Proposition 2.5, Theorem 3.1(i), §4.1 (finite condition, not injectivity); AR-19/H9-T15 and P17", "arithmetic/FULL_CHOW_GATE.tex")
add("AR-16a", "Exact rational-field injectivity criterion", "Over Q the actual one-dimensional Selmer target and nonzero η make scalar-extended injectivity the remaining condition; no rational or real-height splitting is inferred", ["AODD","A5"], modern, [], none, "P17; H9-T15; AR-23; restriction/norm and conjugation decomposition", "arithmetic/RATIONAL_INJECTIVITY_GATE.tex")
add("AR-17", "Audit of CM Abel–Jacobi theorems and conductor restrictions", "Scope finding: checked Dee/Castella/BDP statements do not prove the required whole-Chow injectivity; the rank statement is separately repaired in H9-T15", ["AODD","A5"], modern, [], none, "Dee, arXiv:math/9901155, Theorem 5.1.2 p.28, Theorems 1.0.2 p.3 and 5.1.5 p.29; Castella §5 standing hypotheses p.21/Theorem 5.2.1 pp.23–24; BDP Proposition 5.2.1 pp.26–27", "arithmetic/FULL_CHOW_GATE.tex")
add("AR-18", "Height sign equals an ordering of sum and difference surface heights", "Every primitive odd class has an effective representative V with h(Ce(V))=(H_−(V)−H_+(V))/(12h⁰(L)); separate nonnegativity of H_± does not order them", ["A5"], modern, [], none, "Gu (2026), Theorem 1.3, Proposition 5.3, §2.2; Zhang, Small points and adelic metrics, Theorem 2.4(b), author pp.11–12; canonical Deligne-pairing cancellation proved here", "root/AR18_sum_difference.tex")
add("AR-19", "Explicit nonzero Katz moment at 5", "Actual Fermat ray-class normalization and critical congruent character; exact primitive 4-torsion coefficient gives a p-adic unit", ["AODD","A5"], modern, [], none, "Bannai–Kobayashi, arXiv:math/0610163v4, Theorem 1.17 p.17, Corollary 2.17 p.30, §3.3 Definitions 3.8–3.9 pp.40–43, Theorem 3.11 pp.44–46; exact torsion/character calculation", "arithmetic/FERMAT_KATZ_NONVANISHING.tex")
add("AR-20", "Finite-specialization route has an exact obstruction", "Umbrella for AR-20a/20b: rational good-reduction specialization annihilates all complementary N cycles, including a positive nonzero global class", ["A7","A5"], modern, ["S6tau"], "τ convention only; the specialization vanishing uses modern Kahn plus accepted full Tate, not SGA XIII's divisor theorem.", "P15; AR-13; specialization compatible with the exact N projector", "arithmetic/SPECIALIZATION_OBSTRUCTION.tex")
add("AR-20a", "Every good finite-field specialization of N has zero rational Chow group", "CH²(N_v)_Q=0 under the accepted finite-field Tate input; statement about the specified summand, not every degree of the full Jacobian", ["A7","AODD"], modern, ["S6tau"], "Convention only; no direct SGA finite-field Chow theorem is claimed.", "Kahn (2003), Theorem 1.10 p.982 via P15; absence of the relevant Tate eigenvalue/odd-degree homology", "arithmetic/SPECIALIZATION_OBSTRUCTION.tex")
add("AR-20b", "A positive global class is invisible in every good finite specialization", "η≠0 and h(η)>1/100, while every good rational specialization vanishes; finite-field cycle-class tests cannot prove global strictness by injective specialization", ["A7","A5"], modern, [], none, "AR-13 and AR-20a; exact specialization/norm compatibility", "arithmetic/SPECIALIZATION_OBSTRUCTION.tex")
add("AR-21", "Every odd rational class comes from one geometrically integral curve", "Umbrella for AR-21a/21b; curve may contain a prescribed rational point over the original number field; denominator stated explicitly", ["A5"], modern, [], none, "Stacks Project tags 0FD4, 0BGJ, 01OF, 01VG; exact surface/resolution/Bertini construction in AR-21a", "arithmetic/INTEGRAL_CURVE_REDUCTION.tex")
add("AR-21a", "Integral-curve replacement with an even ample correction", "Effective one-cycle V becomes one geometrically integral W with [W]=MV+bL², preserving a prescribed rational point; no unproved Chow-moving injectivity", ["A5"], modern, [], none, "Stacks 0FD4, Lemmas 33.47.1 and 33.47.3; 0BGJ, Theorem 54.14.5; 01OF, Lemma 31.33.4; 01VG, Lemmas 29.38.7–29.38.8", "arithmetic/INTEGRAL_CURVE_REDUCTION.tex")
add("AR-21b", "Single-curve Ceresa representation of any odd codimension-two class", "z=M^−1 Ce(W) over the original number field, M>0; W may pass through 0; follows from the even correction and AR-21a", ["A5"], modern, [], none, "AR-21a; Fourier grading and exact inversion parity", "arithmetic/INTEGRAL_CURVE_REDUCTION.tex")
add("AR-22", "Divisor Hodge-index bounds leave the desired cubic sign unoriented", "For the C² curve test, the full one-parameter inequality family gives |B₃| bounds and is symmetric under B₃↦−B₃; no geometric negative example asserted", ["A5"], modern, ["S6index"], "Classical geometric surface index supplies t≥0 only; the arithmetic inequality is Yuan–Zhang, not SGA.", "Yuan–Zhang, Math. Ann.367 (2017), Theorem 3.2, pp.1134–1135, conventions §3.1; AR-18 canonical mixed-term cancellation", "arithmetic/DIVISOR_HODGE_INDEX_BOUND.tex")
add("AR-23", "The actual Fermat cycle spans the proved Selmer target", "After tensoring with Q₅, AJ(η) spans over Q and AJ(η),AJ(Tη) span over Q(i); no rational Chow or real-height decomposition follows", ["AODD","A5"], modern, [], none, "Bloch (1984), Theorem 4.1/proof p.104, nonzero projected β₅ and vanishing H⁰(Q₅/Z₅(2)); P17; AR-19; H9-T15; Fourier/cycle transport proved explicitly", "arithmetic/FERMAT_REGULATOR_SURJECTIVITY.tex")
add("AR-24", "Every complementary height is a projected Gross–Schoen height", "Single integral W generates A; after finite extension choose actual basepoint above 0; exact self-transpose projector E_N on C³ and positive factor δ/(36M²)", ["A5"], modern, [], none, zhang+"; AR-21; generically finite push–pull and the grade-one coefficient 27−24+3=6", "arithmetic/PROJECTED_GROSS_SCHOEN_REDUCTION.tex")
add("AR-25", "Exact Fermat tensor-diagonal and sixteen-intersection reduction", "Actual Chow projector on E³ and C³; height equals 1/(16DM²) times the sixteen specified triple admissible intersections; Zhang's required sign remains conjectural", ["A5","AODD","LMOT"], modern, [], none, "Zhang (2010), Theorem 2.3.5 p.27 and Conjecture 2.4.1 p.28; "+kimura+"; exact U=[1+i]* Chinese-remainder projector; AR-21 actual basepoint", "arithmetic/FERMAT_TENSOR_DIAGONAL_REDUCTION.tex")
add("AR-26", "The full Hermitian divisor-HI system has a sign symmetry", "Exact all-symmetric-divisor primitivity on N, determinant cubic and σ-stable PSD pullback cone; all stated divisor inequalities preserve the cubic sign ambiguity. The changed functional is a mixed height from (f,−f), never a negative self-height.", ["A5","AODD","LMOT"], modern, [], none, "Yuan–Zhang (2017), Theorem 3.2, pp.1134–1135; Zhang (2010), Lemmas 2.2.1–2.2.4, pp.20–22, correspondence composition p.23; Gu Theorem 1.3/Proposition 5.3 through AR-10; exact CM polynomial identities", "arithmetic/HERMITIAN_HI_OBSTRUCTION.tex")
add("AR-27", "The projected-height test can use actual canonical base points", "Umbrella for AR-27a/b: every Fermat test class has a parametrized-curve presentation with K_C proportional to its actual marked point; exact positive height factors preserve sign and nonvanishing, with the projector retained", ["A5"], modern, [], none, "Explicit quadratic-cover construction; Stacks Project §53.12, Tag 0C1B, Lemmas 53.12.2–53.12.4; AR-24/AR-25 height adjunction", "arithmetic/CANONICAL_POINT_COVER.tex")
add("AR-27a", "Original-field quadratic cover with a canonical marked point", "For a pointed genus-g curve over a number field and n≥3g−1, a smooth geometrically integral double cover has ρ*e=2e′, g(C′)=n+1 and ω_C′=O(2ne′), all over the original field", ["A5"], modern, [], none, "Degree-2g+1 very-ampleness criterion and Bertini as in AR-21; Stacks Tag 0C1B, Lemmas 53.12.2–53.12.4; B=O(ne)⊗ω_C^−1 and branch section constructed explicitly", "arithmetic/CANONICAL_POINT_COVER.tex")
add("AR-27b", "Exact projected-diagonal pullback and one-half height factor", "r=ρ³ gives r_*Δ_e′=2Δ_e and E_C′Δ_e′=r*(E_CΔ_e)/4; its height is one half, compensated by δ′=8δ and M′=2M. The new map is a parametrization, not required to normalize its image.", ["A5"], modern, [], none, "AR-27a; Zhang (2010), Lemma 2.3.1 p.23 and the checked AR-24/AR-25 correspondence adjunction; termwise seven-diagonal pushforward and degree-eight push–pull", "arithmetic/CANONICAL_POINT_COVER.tex")
add("AR-28", "Exact adelic nef cone for the canonical diagonal metric", "For the specified admissible metrics, nef iff δ₁,δ₂≥0 and δ₁δ₂≥g²t²; the larger geometric-bigness range does not give nef metrics. The J(C) pullback cone can exceed the E³ cone of AR-26.", ["A5"], modern, [], none, "Yuan, Arithmetic bigness and a uniform Bogomolov-type result, author version 21 Aug.2024, Theorem 2.9(1) pp.35–36 and Theorem 2.10(1)–(2) pp.37–38 (published Annals203 (2026)); Yu–Yuan–Zhou, §2.5 pp.29–33 and Proposition 3.7 pp.37–38, shifted bigness only; exact metric constants and curvature matrix computed in the proof", "arithmetic/DIAGONAL_CANONICAL_NEF_CONE.tex")
ar29source = "Zhang (2010), Lemmas2.2.1–2.2.4 and Theorem2.3.5,pp20–27; Yuan, Theorems2.9–2.10,pp35–38; Faltings–Hriljac normalization as stated in Yu–Yuan–Zhou Theorem2.5,p32; exact projector, metric and curve calculations in the proof"
ar29parts = [
 ("AR-29", "Full-Jacobian diagonal decomposition and constraint boundary", "Umbrella for parts a–g. Identifies the additional complementary terms and proves the stated constraint symmetries; neither full arithmetic positivity nor a negative self-height is obtained."),
 ("AR-29a", "Exact elliptic quotient and orthogonal Jacobian complement", "Rosati-self-adjoint rational projectors split h1(C) in Chow, and the full diagonal has an additional two-A/one-B height term."),
 ("AR-29b", "Opposite-CM Tate–Picard block and remaining higher-level block", "The opposite-character motive is Tate² with self-height 4 times Neron–Tate; the same-character tensor has types30/03 when B is nonzero, so no entire level-one replacement follows."),
 ("AR-29c", "Canonicalization creates no one-new-Prym term", "Diagonal deck invariance kills two-old/one-new-Prym projections; the exact corresponding triple-intersection factors are2 and4."),
 ("AR-29d", "Scalar-vertical diagonal constraints admit cross negation", "The specified canonical nef/Hodge-index constraints and their even data are invariant; independently specified Picard self-heights are not all preserved."),
 ("AR-29e", "Block reflection retains two-A/one-B Picard data", "On block-diagonal cross operators and scalar verticals, the reflection reverses A³ while preserving A²B data; arbitrary off-diagonal coefficients are excluded."),
 ("AR-29f", "Canonical one-A/two-B Lefschetz contraction vanishes", "Exact target primitivity and the canonical-point beta identity give p beta_q=0; no vanishing for every extra algebraic class in h2(B) is asserted."),
 ("AR-29g", "Canonical base point does not kill every Picard contraction", "An explicit genus-two elliptic quotient, followed by canonicalization, gives a nonzero opposite-character Picard contraction with positive self-height. The two elliptic maps coincide; no full three-quotient presentation or negative example is claimed."),
]
for ident,title,scope in ar29parts:
    add(ident,title,scope,["A5"],modern,[],none,ar29source,"arithmetic/FULL_JACOBIAN_DIAGONAL_SPLITTING.tex")

PATTERN = re.compile(r"(?<![A-Za-z0-9])(?:JAC-T4\.[0-9]+|JAC-P[0-9]{2}|H9-[A-Z][0-9]+[a-z]?|AR-[0-9]+[a-z]?)(?![A-Za-z0-9])")
observed = {}
for group in ("root", "programme", "h9", "arithmetic"):
    for path in sorted((BASE/"work"/group).glob("*.tex")):
        for ident in set(PATTERN.findall(path.read_text())):
            observed.setdefault(ident, []).append(str(path.relative_to(BASE)))
authored = [r["finding_id"] for r in ROWS]
if len(authored) != len(set(authored)):
    raise RuntimeError("Duplicate authored finding ID")
missing = sorted(set(observed)-set(authored))
extra = sorted(set(authored)-set(observed))
if missing or extra:
    raise RuntimeError(f"Crosswalk coverage mismatch: missing={missing}; extra={extra}")
for row in ROWS:
    path = BASE/row["proof_file"]
    if not path.exists() or row["finding_id"] not in path.read_text():
        raise RuntimeError(f"Missing proof occurrence: {row['finding_id']} {path}")
    row["proof_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    row["inventory_timestamp_UTC"] = STAMP

columns = list(ROWS[0])
with (OUT/"GROTHENDIECK_CROSSWALK.tsv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t")
    writer.writeheader()
    writer.writerows(ROWS)

def mdcell(value):
    return value.replace("|", " / ").replace("\n", " ").replace("\\", "\\\\")

intro = f"""# Finding-to-Grothendieck locator crosswalk

Run **JAC1964-20261121**. Authored by **/root/programme_audit**, GPT-6 Astra Pro; effort setting not exposed. Inventory snapshot: **{STAMP}**.

This is an authored semantic crosswalk for **{len(ROWS)} stable finding IDs**. The accompanying script checks enumeration and proof-file occurrences; it does not infer historical relationships, validate mathematics, or formally verify proofs. The TSV contains one row per ID, including the umbrella IDs AR-20 and AR-21 and each separately named sub-result. Proof-file hashes identify the exact snapshot. Later additions require rerunning the coverage check and authoring a new row.

## How to read the mapping

The cote references identify the original question or method to which a finding responds. **“Not a statement in Grothendieck” is intentional:** a modern Fermat, Selmer, theta, Chow-motive, or arithmetic-height result is not attributed to SGA, EGA, FGA, or the 1964 leaves merely because it advances their programme. The independent SGA/EGA/FGA column gives an exact result that is actually used, or says that none is used directly. “Related framework” or “normalization only” must not be read as a proof of the new conclusion.

The only available cote sources are the supplied TeX transcriptions. Their contents were read and mathematically audited; **the original cote images were unavailable, so no palaeographic verification is claimed**. Scan numbers refer to supplied scan numbering, not inferred manuscript pagination. Cote44 scans 3, 5 and 7 are unrelated interleaved material and are not used as sources for this programme. The normalized lowering convention in cote16 differs from the weighted sl₂ convention unless explicitly adjusted.

The incidence quotient in these results is **Saito's higher Picard variety, up to isogeny**. The universal regular algebraic representative is a different construction, identified only in the stated codimension-two cases. No exact FGA locator for a general higher-codimension representative is claimed. The transverse-axis EGA reference is explicitly cited by SGA and its original text was not independently inspected. The separate EGA III coherent-base-change statements were directly read and their statement pages visually checked. Neither an invented FGA theorem nor a vague “SGA standard conjectures” citation fills a missing input.

The 032/Milne results are accepted inputs as instructed, not theorems reproved in this run. “Proved” or “deduction” in the scope column is relative to each row's stated accepted and classical inputs. The table is not a claim of historical originality. Scope and proof-review details remain in the proof files and CHECK_EVENTS ledgers.

## Original archive loci

| Key | Exact supplied locator |
|---|---|
"""
for key, value in ARCHIVE.items():
    intro += f"| {key} | {mdcell(value)} |\n"
intro += """

## Every stable finding

Each entry below is individually enumerated. The TSV additionally separates archive relationship, source role, full modern locators, proof path, and proof hash into dedicated columns.
"""

groups = [
 ("Primitive incidence: JAC-T4.1–JAC-T4.5", lambda i:i.startswith("JAC-T4.")),
 ("Programme deductions: JAC-P00–JAC-P20", lambda i:i.startswith("JAC-P")),
 ("Geometric heights and monodromy: H9", lambda i:i.startswith("H9-")),
 ("Arithmetic heights and exact remaining gates: AR", lambda i:i.startswith("AR-")),
]
body = intro
for title, predicate in groups:
    body += f"\n### {title}\n\n"
    body += "| Finding ID and result | Exact archive link and relationship | SGA/EGA/FGA locus and its role | Scope and actual modern input |\n|---|---|---|---|\n"
    for row in ROWS:
        if not predicate(row["finding_id"]):
            continue
        link = f"[{row['finding_id']}](sandbox:{BASE/row['proof_file']})"
        cells = [
            link+" — "+row["finding"],
            row["archive_locator"]+" **"+row["archive_relationship"]+".**",
            row["SGA_EGA_FGA_locator"]+". "+row["role_of_SGA_EGA_FGA"],
            row["proved_scope_or_remaining_gate"]+". **Inputs:** "+row["modern_primary_inputs_and_locators"],
        ]
        body += "| "+" | ".join(mdcell(c) for c in cells)+" |\n"

body += """

## Exact SGA/EGA source register and verification boundary

Printed page numbers below are original-volume pagination. Where only a section was checked, no page number has been guessed. The web transcriptions occasionally corrupt degree labels and dual symbols; the recorded original-page inspections take priority.

| Key | Exact locus | What it supplies | Source and check scope |
|---|---|---|---|
"""
for key,(locator,role,url,check) in SGA.items():
    body += "| "+" | ".join(mdcell(x) for x in (key,locator,role,f"[Primary source]({url}). {check}"))+" |\n"
body += """

## Main guardrails the crosswalk preserves

1. The raw unsigned middle incidence class of cote44 scan9 is not generally a polarization. The repaired result uses the primitive part and the sign (−1)^m, with its curve calibration and diagonal factor 1/2.
2. Cote44 scan4 Th.5 explicitly requires algebraically trivial restrictions. A homologically trivial class need not define a point of that incidence quotient. Geometrically integral fibres alone do not remove vertical height corrections.
3. The critical fixed-trace assertion is proved by a spread family and an algebraic retraction. An invariant-cohomology statement by itself is not silently upgraded to a cycle correspondence.
4. For Th.7, τ is interpreted by the standard saturation convention, because scan6 does not define it. The characteristic-zero CM counterexample and the finite-field positive theorem have different, explicitly stated scopes. Over an arbitrary extension of Fbar_p, the constant-variety conclusion is numerical/homological/algebraic equivalence, not rational Chow=numerical.
5. The exact Chow complement N, its Q(i)-action, a positive orbit plane, and a one-dimensional Selmer target do not imply that the full Chow group is one-dimensional. The required scalar-extended Abel–Jacobi injectivity remains a distinct gate.
6. Full homologically trivial height positivity survives the stated original-pencil and geometric-generic-cover situations. It fails after arbitrary finite covers: H9-T17 gives an explicit indefinite norm-zero plane. Positive-characteristic special-axis and general variable-fourfold forms retain their stated gates.
7. Zhang's tensor-admissible-intersection sign conjecture is not presented as a theorem. AR-24/AR-25 give exact reductions, including projectors and positive factors, without claiming that a projection preserves an unproved positivity cone.

## Mechanical coverage

The inventory scans authored TeX files directly under work/root, work/programme, work/h9 and work/arithmetic for the stable patterns JAC-T4.*, JAC-P followed by two digits, H9-[letter][number][optional suffix], and AR-[number][optional suffix]. AR-B1–AR-B3 are explicitly designated background conventions/results and AR-GATE is an equation label, so they are not new-finding IDs. References to an ID in several proofs do not create duplicate findings. Every matched new ID must have exactly one authored crosswalk row and occur in its designated proof file.

The separate coverage JSON records the complete ID set, all TeX occurrences, hashes of designated proof files, and the successful no-missing/no-extra comparison. This is a coverage audit only, not a formal proof check.
"""
(OUT/"GROTHENDIECK_CROSSWALK.md").write_text(body)

report = {
    "run": "JAC1964-20261121",
    "timestamp_UTC": STAMP,
    "count": len(ROWS),
    "missing": missing,
    "extra": extra,
    "ids": authored,
    "all_TeX_occurrences": observed,
    "designated_proofs": {r["finding_id"]: {"file":r["proof_file"],"sha256":r["proof_sha256"]} for r in ROWS},
    "scope": "ID coverage only; all semantic source links were authored explicitly",
}
(OUT/"GROTHENDIECK_CROSSWALK_COVERAGE.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"count":len(ROWS),"missing":missing,"extra":extra,"files":["GROTHENDIECK_CROSSWALK.tsv","GROTHENDIECK_CROSSWALK.md","GROTHENDIECK_CROSSWALK_COVERAGE.json"]},ensure_ascii=False))
