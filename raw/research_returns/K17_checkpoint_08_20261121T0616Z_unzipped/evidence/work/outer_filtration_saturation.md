# K17-OUT-SAT: exact integral and rational outer filtrations for free pro-p groups

**Statement.** Let p be any prime and Pi a finitely generated free pro-p group of rank at least two. The positive graded quotients of the lower-central outer-automorphism filtration are torsion-free Z_p-modules. Consequently, for an arithmetic outer action to which Hain--Matsumoto Proposition 8.2 applies, its integral lower-central pullback filtration agrees exactly with the pullback from the rational unipotent completion, starting at degree one.

Reviewer: GPT-6 Astra Pro, /root/archive_kummer; effort setting not exposed. Full proof read and checked, 2026-11-21 UTC. This is a paper proof, not a formal certificate.

## Proof

Hain--Matsumoto Proposition 8.2 alone gives finite kernel and cokernel on the graded comparison. That statement was reread in full and is not silently strengthened. For the free geometric fundamental group, the following additional elementary argument upgrades it to equality of filtrations.

Let Pi be a finitely generated free pro-p group of rank at least two, Gamma_n its closed lower central series, and L_n=Gamma_n/Gamma_(n+1). The primary input is Koch--Kukkuk--Labute, *Nilpotent local class field theory*, Theorem 2.1: gr(Pi) is the free Lie algebra over Z_p on Pi_ab, for every prime p. The complete statement and proof were freshly read in the author PDF, pages 4--5; the journal locator is Acta Arithmetica 83 (1998), 45--64, pages 48--49. Author URL: https://www.math.mcgill.ca/labute/papers/kkl.pdf .

Put A_n=ker[Aut(Pi)->Aut(Pi/Gamma_(n+1))], n>=1. The degree-n Johnson map sends alpha to the homomorphism

    Pi_ab -> L_(n+1),    x -> alpha(x)x^(-1) modulo Gamma_(n+2).

The commutator identities show that this is Z_p-linear, additive in alpha, and has kernel A_(n+1). Thus A_n/A_(n+1) injects into Hom_Zp(L_1,L_(n+1)).

Let O_n=ker[Out(Pi)->Out(Pi/Gamma_(n+1))]. Every class in O_n has a representative in A_n: lift the element of Pi/Gamma_(n+1) giving its inner action and compose by the inverse of that integral inner automorphism. Moreover an inner conjugation by g lies in A_n exactly when g lies in Gamma_n. For the nontrivial direction, a first nonzero degree k<n of g would centralize every degree-one generator in the free Lie algebra, which is impossible.

For completeness, the free Lie algebra over any field has zero center in positive degree. Embed it in the free associative algebra. A polynomial commuting with one free letter X contains only powers of X: compare coefficients and move all leading X's to the right to see that every word containing a different letter has zero coefficient. Commuting with a second independent letter then forces the polynomial to be scalar, and a positive-degree scalar is zero. The same conclusion over Z_p follows by tensoring with Q_p.

It follows that O_n/O_(n+1) injects into

    Hom_Zp(L_1,L_(n+1)) / ad(L_n).

Indeed the ambiguity in an A_n representative is exactly an inner element of Gamma_n, and if its Johnson class is ad(z), choose a lift of z in Gamma_n and adjust it to kill that class. The submodule ad(L_n) is primitive: reduction modulo p has zero kernel because the free Lie algebra over F_p has zero center. More explicitly, if ad(z) is divisible by p, then z is divisible by p; dividing and iterating proves that the displayed quotient has no p-torsion. Hence every positive outer graded quotient is torsion-free, and so are the graded quotients of any arithmetic subgroup with the induced filtration.

Let I^n be the pro-p outer-action filtration and J^n its rational pullback. They agree at n=1, since identity on integral abelianization is equivalent to identity after tensoring with Q_p. Suppose I^n=J^n. By Hain--Matsumoto Proposition 8.2 the map gr_I^n to gr_J^n has finite kernel; its source is torsion-free by the preceding argument, so that kernel is zero. Every element of J^(n+1) belongs to I^n and maps into this kernel, hence belongs to I^(n+1). The reverse inclusion is known. Induction proves I^n=J^n for all n, including p=2.

This supplies the exact lattice identification required for the finite arithmetic conclusion. It does not assume a general torsion-freeness statement for fundamental groups of arbitrary varieties.

