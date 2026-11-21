# JAC-P20 and Milne Proposition 4.2: precise audit status

Run JAC1964-20261121; /root/programme_audit; GPT-6 Astra Pro; effort not exposed.

**Status:** Milne 2022 v1.1 Proposition 4.2, printed pp. 7–8, explicitly asserts that an algebraic injection of total cohomology into a variety satisfying Hodge standard transfers Hodge standard. The asserted proposition can be cited as an additional input. Its transfer of the particular geometric form was **not re-established in this audit** from the two references in its one-line proof. This is not a refutation.

## Directly checked primary locators

| Source | Exact locator | What is stated and used |
|---|---|---|
| Milne, *Grothendieck's standard conjecture of Lefschetz type over finite fields*, 14 July 2022 v1.1 | Proposition 4.2 pp. 7–8; Theorem 4.5 p. 8 | The transfer is explicitly asserted; the proof cites the following two passages. |
| Kleiman, *Algebraic cycles and the Weil conjectures* (1968) | §1.3 pp. 364–365 | Algebraic correspondences act on total cohomology; the inhomogeneous notation has its usual meaning. |
| Same | Theorem 3.11 pp. 380–381 | Algebraicity of the geometric star-adjoint assumes B(X), B(Y). Strict positivity of Tr(u'u) additionally assumes I(X×Y) for the product ample class. |
| Saavedra Rivano, *Catégories tannakiennes*, LNM265 (1972) | VI4.2.0 p. 363 | Standard conjectures are assumed, and this convention persists through 4.3–4.6. |
| Same | VI4.4.2 p. 373 | The geometric forms define a compatible canonical polarization under that convention, using Appendix A3.3 and Kleiman3.11. |
| Same | Appendix A3 pp. 400–401, especially (3.3.1) p. 401 | The trace positivity is again under the standard-conjecture assumption. |

The Kleiman pages 380–381 and Saavedra pages 363, 373, 400–401 were visually inspected in the original scans. Local PDFs and rendered extracts are in this directory. Milne was read from the primary author PDF.

## Checked actual injection, as distinct from positivity

Let h(X) split by actual rational Chow correspondences into a finite direct sum of h(A_i)(n_i). After forgetting degree/Tate labels, its component correspondences give an injection H*(X) → ⊕H*(A_i). Put Y=(∏A_i)×E^s. Insert the ith component in its A_i factor, with units in the other A factors, the point class in elliptic factor E_i, and units in all other elliptic factors. Distinct elliptic Künneth multidegrees separate the components. The sum is therefore an algebraic, possibly inhomogeneous, injection into H*(Y).

Consequently the exact additional assertion of Milne4.2, **if used as an input**, transfers accepted032 Hodge standard for Y to every geometric abelian-type X. This construction closes the actual-injection issue and does not rely on a mere isomorphism of realizations.

It does not independently close the form-compatibility issue. A positive form on an abstract summand and its negative have the same adjoint involution; nondegeneracy and semisimplicity alone do not identify the geometric form with the positive one. No geometric counterexample follows from this formal observation. JAC-P16's separately proved B and D statements are unchanged.

Paper-ready source audit and the full conditional argument: `milne_transfer_audit.tex`.

Primary URLs:

- https://www.jmilne.org/math/articles/LFF.pdf
- https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf
- https://www.math.columbia.edu/~dejong/tannakian/1972_Book_Cat%C3%A9goriesTannakiennes.pdf

JAC-P20 labels the proved actual-injection lemma and its explicitly conditional transfer corollary. No main fixed-axis sign gate is counted as closed by this audit.
