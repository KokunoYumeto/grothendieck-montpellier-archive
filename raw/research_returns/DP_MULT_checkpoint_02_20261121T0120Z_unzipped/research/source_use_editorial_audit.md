# Source-use editorial audit

Agent: `/root/archive_binomial`; model: GPT-6 Astra Pro, inherited; reasoning effort: not exposed by the runtime. Date: 2026-11-21 UTC. Editorial reading began at 00:38:57 UTC; the revised short DP11 and DP12 were read in full at 00:43:36 UTC and checked by 00:46:08 UTC. This is a source-use audit and a check of the replacement arguments, not a new independent whole-paper proof verification.

## Result

The original long proof of DP11 unnecessarily re-proved the known torsion-free binomial/Fermat criterion and the special lambda identities. Its local residue-ring/digit-lifting argument should be research documentation, rather than the main paper's proof of a new result. Likewise, DP12 need not re-prove the classical binomial basis by Newton interpolation.

The parent has now made exactly these changes. The current main paper cites Elliott's Theorem 4.1, with Horel's explicit cross-reference, and Borger's flat-scheme equivalence. It proves only the normalized combined formulation and functoriality used here. DP12 cites the standard basis and retains a short verification of the degree-associated graded Hopf algebra and the two calculus distinctions. Both revised proofs are correct under their stated hypotheses and satisfy the requested editorial rule. The removed arguments are retained in `research/binomial_background_reproof_retained.tex`; their earlier actual proof-check events remain historical events and must not be relabeled as new checks.

No further lengthy re-proof of a cited background theorem needs to be removed from the main text. The central coefficient bounds, ramified extensions, explicit counterexamples and CM construction are the work being established here; source-use discipline does not require deleting their proofs.

## Approved DP11 replacement

The following is the concise form checked in the actual revised paper. It cites, rather than re-proves, the classical equivalences. The statement must retain the torsion-free hypothesis, the requirement of every prime, and the word special for the lambda structure.

```latex
\begin{proof}
The equivalence (i)$\Leftrightarrow$(ii) is Elliott's criterion
\cite[Theorem 4.1]{Elliott}, recorded explicitly in
\cite[Remark 1.3]{Horel}. Since $\Spec S$ is flat over $\Z$,
commuting Frobenius lifts are equivalent to a special
$\lambda$-structure; apply Borger's supplied introduction and
\S1.1 to the commuting identity lifts \cite{Borger}.
This gives (ii)$\Leftrightarrow$(iii).

For the stated normalization, work in $S\otimes\Q$.
Newton's identity gives
\[
 \frac{d}{dt}\log\lambda_t(a)
 =\sum_{m\ge1}(-1)^{m-1}\psi^m(a)t^{m-1}
 =\frac{a}{1+t}.
\]
The constant term is one, so $\lambda_t(a)=(1+t)^a$,
proving uniqueness. A ring map preserves these rational
polynomials after tensoring with $\Q$; injectivity of the
torsion-free target into its rationalization proves the
claimed integral compatibility. This proves only the explicit
normalized and functorial form of the cited equivalence.
\end{proof}
```

The composite Adams operations are identity because Adams operations compose multiplicatively and each prime operation is identity. This standard consequence is implicit in the cited equivalence; a one-sentence reminder may be added if desired, but is not a missing proof. Newton's identity takes place in a rational power-series ring, so the logarithm, integration and constant term argument are valid. A ring homomorphism need not be injective: only the target's map to its rationalization is used. The zero ring causes no problem for this theorem.

The following explanatory paragraph already labels the criterion as known. It is acceptable to retain it for the contrast with torsion rings. The bibliographic tail formerly saying that the torsion-free form is proved in DP11 has now been removed. The entry accurately says that the original full proofs are cited rather than newly audited.

## DP12 check and attribution

Elliott, Lemma 2.2, is the exact binomial-basis locator. It is explicitly invoked in the proof of Horel, Proposition 2.2, author-PDF pp. 4--5, which also displays Vandermonde's formula. The current citation correctly refers to the proof, rather than pretending that the statement of Horel's Proposition 2.2 is itself a basis theorem.

The retained argument proves the specific combination needed here:

1. In the degree filtration, the leading term of `b_i b_j` gives the structure constant `binom(i+j,i)`.
2. Vandermonde's coproduct, evaluation at zero, and substitution `x -> -x` give the graded Hopf structure, including the sign of the antipode.
3. Pascal gives the integral finite difference, including the separate `n=0` case, while `b_2'(0)=-1/2` disproves integrality of ordinary differentiation.
4. The identity lift gives the usual p-derivation by a two-line expansion. In a nonzero torsion-free ring, `delta_p(p)=1-p^(p-1)` is nonzero; every ordinary derivation kills the integer subring. The nonzero qualification is essential to that last contrast.

The multiplication and coproduct respect the total degree filtration. The proof does not identify the filtered ring itself with a divided-power polynomial ring. These are short checks of the exact comparison form and of the proposed identification's failure, rather than a lengthy re-proof of general integer-valued-polynomial or delta-ring theory.

## Other sections: retain/cut decisions

| Main-paper material | Decision | Reason and exact boundary |
|---|---|---|
| DP1--DP4, including normalized coefficient estimates, digit iteration and sharpness | Retain full arguments | These establish the stated coefficientwise, exact-floor and affine-operator forms. A cited Lubin--Tate or Hurwitz-number special case does not by itself give these precise formulations. The few lines recalling the normalized logarithm are short setup. |
| DP5 distributions and associated graded | Retain the coordinate calculation and counterexamples | General principal-parts/distribution formalism is cited to EGA IV and SGA 3. The short leading-symbol check establishes the particular one-dimensional normalized comparison used here. It can be labeled a coordinate verification without changing the mathematics. |
| DP6 and DP21, source-interface statements | Retain with source labels | These identify the exact old bound and explain what its theorem says. They do not re-prove the cited Katz theorem. |
| DP7, DP9, DP17, DP18, DP23, DP24 | Retain | They are specific deductions, obstructions or interface checks required by the question, not proofs of a general cited theorem. |
| DP8 CM dimension counts | Retain short application | Tate's CM formula is cited, not established anew. The optional sentence explaining rank-one Tate modules may be deleted for economy, but is not a long re-proof. Keep the complementary-type arithmetic and the multidimensional counterexample. |
| DP19 strict unramified CM action over a ramified base | Retain full argument | Integral action, Teichmuller averaging, support congruences and floor rounding prove the particular extension needed. The proof is not a re-proof of Lubin--Tate classification. |
| DP20 ramified deformation counterexample | Retain full argument | Lubin--Tate 1966 Proposition 1.1 is an exact cited existence input. The specialization, contraction and valuation calculation are the new application being checked. |
| DP22 explicit genus-three CM example | Retain computations | Picard existence/smoothness/properness, the CM slope formula and the formal p-divisible correspondence are cited to exact primary locators. The two charts, CM action, type, Frobenius orbits and one-dimensional factor are the concrete construction. |
| DP10 Cartier/de Rham/restricted-power comparison | Retain the Cech compatibility calculation | Oda, Mazur--Messing and SGA 3 supply the known identifications. The short symbolic p-power calculation verifies compatibility of their actual operations in the combined statement; it does not re-prove those theorems. The additive/multiplicative derivation checks are necessary to interpret the archive correctly. |
| Crystalline, SGA 4/5 and weights paragraphs | Retain as cited context | They state known results with locators and make the boundary of the local derivative theorem explicit. No new proof or recovery theorem is claimed. |
| DP11 old local digit/Fermat proof and rational-polynomial lambda identities | Remove from main; retain research | Already classical and exactly cited. This change has been applied. |
| DP12 Newton interpolation proof | Remove from main; retain research | The binomial-basis theorem is exactly cited. This change has been applied. |
| DP13 Horel reconstruction | Retain short application | Model structure and reconstruction are cited to Horel Theorems 3.7 and 5.4. The pointwise operations and derived-adjunction direction are the application being made. No reconstruction proof is reproduced. |
| DP14 formal-disc and ordinary-derivative obstructions | Retain | Two short explicit counterexamples delimit the proposed bridge. They do not claim impossibility of every richer comparison functor. |
| DP15 exterior divided powers and DP16 Chern/binomial coefficients | Retain | The subset expansion, genus-three Smith obstruction and coefficient calculation are short, targeted checks of the exact archival formulas. They are not a general proof of Lefschetz theory or Riemann--Roch. |

## Source checks and their limits

- The supplied Borger LaTeX was directly read in its introduction and section 1.1, General Lambda-spaces. It explicitly gives the flat-over-Z equivalence between lambda structures and commuting prime-indexed Frobenius lifts. The source also identifies the affine notion with the usual lambda-ring notion.
- Horel's [author PDF](https://geoffroy.horel.org/binomial.pdf) was directly read at Definition 1.1 and Remark 1.3 (author-PDF p. 3), and at the proof of Proposition 2.2 (pp. 4--5). These verify the exact Elliott cross-references used above. The reconstruction locators had already been read and checked in the prior archive work.
- Elliott's original 2006 publisher page was located, but its full original article returned HTTP 403 in this run. No claim is made to have independently audited its original full proofs. The exact Theorem 4.1 and Lemma 2.2 locators are cross-confirmed by Horel's primary paper. The present DP11 proof's lambda direction uses the directly inspected Borger statement, rather than depending on unseen details of Elliott Proposition 8.3.
- The FGA bibliography previously used the inaccurate lead title "Techniques de construction...". The parent has corrected it to "Technique de descente et theoremes d'existence en geometrie algebrique", followed by the exact Picard exposé titles. This is a bibliographic correction, not a mathematical change.

The editorial check read the theorem/proof sections DP1--DP24 and relevant attribution/context paragraphs. It did not independently re-prove the cited theorems, and it does not replace the separate proof-check records. No main-paper edits were made by this agent.
