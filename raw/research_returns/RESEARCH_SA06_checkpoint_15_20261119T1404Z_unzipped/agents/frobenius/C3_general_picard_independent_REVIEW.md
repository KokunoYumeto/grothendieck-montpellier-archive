# Independent audit of C.3n: ordinary Picard injectivity with a coefficient field

## Outcome

We independently read `research/agents/real_weil/C3_general_picard_draft.tex` in full and pass its stated result. The scope is an excellent normal strictly henselian noetherian local k-algebra with its specified algebraically closed coefficient field, dimension at least three, and regular source and divisor punctures. Integral injectivity holds in characteristic zero; in positive characteristic the kernel is p-primary torsion, so injectivity holds after inverting p and with rational coefficients. No uniform exponent for the full kernel is asserted.

## The actual abelian-family lemma

The proof correctly avoids compactifying the puncture. For any connected regular noetherian k-scheme U and actual line bundle on U×T, completing only the smooth parameter curve gives U×C regular and noetherian. A rational divisor closes to a Cartier divisor because the product is regular. Geometric integrality of C and integrality of U justify the use of its function field.

The fibre degree over U is locally constant and therefore one integer. The two twists in the draft remove that degree and normalize the fibre at c0. A basis of the one-dimensional constant fibre of O_C(−dc0) handles the remaining scalar; no k-point of U is needed. The Picard universal property gives g:U→Pic0(C). Its validity on arbitrary bases follows by affine finite-presentation descent of the line bundle and its rigidification, followed by uniqueness and gluing.

Transposing the normalized curve Poincaré bundle gives h:C→Pic0(C)^dual. Pulling back the Poincaré bundle on J×Jdual along g×id yields an actual family over the abelian parameter variety Jdual whose fibre at h(c) is the original difference class. The degree-normalizing twist contributes only a constant one-dimensional vector space to each fibre class. The Poincaré tensor law makes the map to the Picard functor a group homomorphism. Finite products of these parameter varieties handle finite sums of ordinary algebraic-equivalence relations.

## Exact Boutot scope and functor issue

We freshly rendered and viewed the original printed p.VII of Boutot's 1978 introduction. Its starting hypotheses are an arbitrary noetherian local k-algebra with residue field k. Theorem1(i) gives a closed finitely presented unit section under depth at least two. Theorem1(ii) gives locally finite-type group-scheme representability when the first punctured coherent cohomology is finite-dimensional. The following paragraph explicitly says that normal completion of dimension at least three suffices. There is no assumption of finite type over k in these statements. Excellence supplies the normal completion needed here.

Boutot's functor uses henselized tensor products. An actual family on X×P pulls back to those products functorially. For A=k, strict henselian R is unchanged and étale sheafification over the algebraically closed field introduces no new point classes, so G(k)=Pic(X).

The image of the abelian parameter variety is indeed a proper connected reduced algebraic subgroup B. The source is proper, the target separated and locally finite type, and the quasicompact image lies in a finite-type open. Its scheme-theoretic image is reduced and proper. Over the perfect field k, a reduced algebraic group is smooth; a proper connected such group is an abelian variety.

For the finite normal local factors of R/(f), the relevant ideals differ by a nilpotent ideal in the quotient. This persists after arbitrary base tensoring. Henselization of the pair is unchanged under this nilpotent modification, so the restriction map of local Picard functors is well defined. No assertion that normalization commutes with arbitrary base change is used. Each target has depth at least two, giving the closed unit section even if the whole target functor is not represented by a finite-type scheme.

## Closed kernel and characteristic distinction

Pulling back the target unit gives a closed subgroup K of the proper abelian variety B. The previously audited prime-to-characteristic torsion theorem C.3k(i) excludes all nonzero ℓ-torsion in K(k) for ℓ different from the characteristic. A positive-dimensional reduced identity component of K would be an abelian variety and would have such torsion, so K is finite. In characteristic zero its point group is trivial. In characteristic p its point group is a finite p-group. Every ordinary kernel element belongs to one such K(k), proving exactly the stated p-primary conclusion.

The proof neither asserts integral injectivity in positive characteristic nor makes a claim over a mixed-characteristic local ring without a specified coefficient field.

## Opened source and local inspection record

Boutot, *Schéma de Picard local* (1978), introduction, Theorem1(i)–(ii) and following paragraph, printed p.VII. Primary URL independently opened earlier in this session: https://link.springer.com/content/pdf/bfm%3A978-3-540-35936-4/1 . The local primary PDF is `research/agents/real_weil/sources/boutot1978_introduction.pdf`; fresh independent rendering is `research/agents/frobenius/output/boutot1978_pVII_audit.png`.

Milne's *Jacobian Varieties* (2021 revision), Theorem1.1 and Lemma1.3, and *Abelian Varieties* sections9–10 supply the standard represented Picard and Poincaré properties used here. The arbitrary-base extension in the draft is separately justified by finite-presentation descent, rather than silently changing those notes' conventions.
