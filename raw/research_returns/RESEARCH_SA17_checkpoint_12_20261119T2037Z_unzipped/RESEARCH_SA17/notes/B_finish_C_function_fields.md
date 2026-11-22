# Actual imperfect function-field family

Run: RESEARCH_SA17_FINISH-20261119.
Model: GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Agent: dieudonne.
Status: complete written proof, independently audited by root and
descent_groups; promoted after checkpoint08 source freeze was released. No novelty or priority claim.

## Deliverables

- sections/C_finish_function_fields.tex
- references/C_function_fields.bib

Four numbered statements:

1. C:function-field-pth-roots: a finite linear system over C(t^p)
   decides p-th roots in every explicitly presented finite extension.
2. C:function-field-constant-bound: normalized absolute factors of a
   total-degree-D polynomial over Fq lie over F_(q^L), L=lcm(1,...,D).
3. C:function-field-factorization: actual terminating factorization
   through arbitrary separable and purely inseparable finite tower steps.
4. C:function-field-WG: complete ordinary algorithms for split WG and
   its exterior operations over every finite-dimensional coefficient
   algebra over any explicit finite tower over Fpbar(t), for odd p.

## Exact arithmetic and proof gates

The chosen algebraic closure is the coherent union of finite fields of
factorial degrees, with finite-search embeddings and first-unseen element
names. A rational function has normalized numerator and denominator.
Every finite tower has its explicit iterated power basis.

The p-root test does not use the factorization theorem being proved:
K has basis t^a e_i over k^p=C(t^p), while K^p is exactly the k^p-span
of the e_i^p. Coordinates are computed by multiplying a rational-function
numerator by denominator^(p-1), then grouping exponents modulo p.

The base factorization bound is a Frobenius orbit bound on normalized
absolute factors, not an assumed absolute-factorization oracle. There
are at most D distinct factors. Finite exhaustive factor search in the
single bounded constant field is consequently final.

For separable simple extensions, enumerate shifts until the norm of the
shifted SEPARABLE polynomial is separable; finitely many root collisions
are the only forbidden shifts. Norm factors and gcds recover the factors.
Arbitrary input is reduced by derivative/gcd recursion and p-root tests.
The draft explicitly distinguishes separability from having no repeated
irreducible factors over an imperfect field.

For an inseparable simple extension g(T)=h(T^(p^e)), factor first over
the separable intermediate E(alpha^(p^e)), then raise the input to p^e.
Each intermediate irreducible factor has a unique factor over K, of
p-power multiplicity; repeated coefficient-root extraction recovers it.
The proof of uniqueness and the multiplicity bound is included.

## Sources opened and scope

- Barry M. Trager, Algebraic Factoring and Rational Function Integration,
  ISSAC predecessor proceedings (1976), 219-226,
  DOI 10.1145/800205.806338.
  Original PDF opened at
  https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA19/TragerFactor.pdf .
  Section 2 opening p219 explicitly assumes characteristic zero.
  Theorems 2.1-2.3, Corollary2.5, pp220-221 supply the norm/gcd method.
  The draft proves the positive-characteristic separable version and
  the inseparable steps directly; it does not silently extend the source.
- Stacks Theorem59.67.10, Tag03RD, full proof opened:
  https://stacks.math.columbia.edu/tag/03RD .
  Tsen applies to every one-variable function field over Fpbar,
  irrespective of the separability of the chosen tower over C(t).
- Searched Allan Steel, Conquering inseparability, J Symbolic Comput40
  (2005),1053-1075, DOI10.1016/j.jsc.2005.03.002. Author homepage and
  examples page opened; publisher full paper returned403. Search text
  warns that Trager needs separable input, not merely squarefree input.
  No theorem from this unopened full paper is used as a proof dependency.

Parent owns compilation, inclusion, shared tables and durable checkpoints.
The draft was written during the checkpoint08 compiled-source freeze.

Promotion and author check UTC: 2026-11-19T17:41:38Z. All four root and DG written audits passed.
The two equation tags were changed to C.3.K1/K2 before promotion.
