# Independent audit of F.2a–b

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius. Date: 19 November 2026.

We read research/sections/F_state.tex, the two supplied source files, and the current Milne and published Debarre–Ein–Lazarsfeld–Voisin PDFs. The corrections and their proofs are sound. A minor scope clarification was suggested to the root: the elliptic curve in F.2b is over \(\mathbf C\), as required by the positive-form formulation.

## F.2a

Milne defines \(S^r\) using the generalized eigenvalue-one space of \(H^{2r}(-,\mathbf Q_\ell(r))\), printed p. 3. Theorem 1.6 on the same page instead prints \(S^{2d}(X\times X,\ell)\), while its proof explicitly uses \(H^{2d}(X\times X,\mathbf Q_\ell(d))\). The corrected sufficient hypothesis is therefore \(S^d\). We checked the independent linear-algebra argument: after extending scalars, a generalized Frobenius block \(V_a\) pairs with its Poincaré-dual reciprocal block, and the tensor is \(\operatorname{End}(V_a)\) with conjugation action. A nontrivial unipotent factor cannot act trivially by conjugation, because the centre of the full endomorphism algebra consists of scalars and a unipotent scalar is one. Partial semisimplicity at eigenvalue one thus forces every block to be semisimple.

The common-field extension powers on printed p. 2 are crossed: a \(p^{n_1}\)-Frobenius and a \(p^{n_2}\)-Frobenius satisfy \(\pi_1^{n_2N}=\pi_2^{n_1N}\) for some positive \(N\). Printed p. 4 uses uncrossed powers in the Tate-structure equivalence definition. The \(H^2(\mathbf P^1)\) test with eigenvalues \(p,p^2\) proves the incompatibility directly. Both errors also occur in the supplied TeX; they are not introduced by extraction.

## F.2b

The published Theorem 2.1, Corollary 2.2, and proof on pp. 1799–1801 say exactly what F.2b attributes to them. In particular Corollary 2.2 has the range \(2\le k\le n-2\), whereas the supplied early TeX prints the upper endpoint \(n\), despite correctly writing \(n-2\) in the preceding sentence.

The published proof expressly takes the closure of the convex cone of rank-one forms \(i\ell\wedge\overline\ell\) with coefficients in the CM order. The supplied proof instead infers generation of that cone from real positive generation of the vector space of one-forms. This inference is not valid without closure: a sum of positive semidefinite rank-one forms has rank one only if every nonzero summand has the same complex line, and an arbitrary line need not contain a vector with coefficients in the CM fraction field. The root's corrected approximation proof is exact. The fraction field is dense in \(\mathbf C\), simultaneous approximation and clearing denominators produce CM-order directions, and positive rescaling gives a convergent sequence of the corresponding rank-one forms. Each is the class, up to a positive real scalar, of the pullback of the origin under a homomorphism \(E^n\to E\). Closedness of the pseudoeffective cone supplies the limit.

## Opened sources

- Milne, J. S. (2007, author revision 3 November 2021). *The Tate conjecture over finite fields (AIM talk).* https://arxiv.org/pdf/0709.3040. Checked printed pp. 2–4, particularly the definition of \(S^r\), Theorem 1.6 and its proof, and the Tate-structure equivalence definition. The arXiv header retains an older upload date while the body states the 2021 revision.
- Debarre, O., Ein, L., Lazarsfeld, R., & Voisin, C. (2011). Pseudoeffective and nef classes on abelian varieties. *Compositio Mathematica, 147*, 1793–1818. https://doi.org/10.1112/S0010437X11005227. Opened full published primary PDF at https://www.math.stonybrook.edu/~roblaz/Reprints/Debarre.Ein.Laz.Voisin.PNAV.pdf. Checked Theorem 2.1, Corollary 2.2 and proof, pp. 1799–1801, and the equality of the positive-form cones at endpoint codimensions on p. 1794.
- Supplied primary source witnesses read: background/literature/milne_tate_conjecture_finite_fields/Tate2007.tex and background/literature/debarre_ein_lazarsfeld_voisin_pseudoeffective_nef/1003.3183.tex.
