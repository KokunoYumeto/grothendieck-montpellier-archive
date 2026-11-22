# Field variation: exact source scope

Run KTOWER; 2026-11-21 UTC; author `/root/geometry_tower`; model GPT-6 Astra Pro; effort not exposed.

The proved reduction is in `field_variation_nonvanishing.tex`. It removes an artificial original-weight cutoff, but does not prove existence of an auxiliary quadratic field. The independent peer review covers the entire elementary reduction and its certificate. The literature audit below was performed by the author and is separately classified.

## 1. Wiles and the class-number factor

Andrew Wiles, *On class groups of imaginary quadratic fields*, Journal of the London Mathematical Society 92(2) (2015), 411–426; DOI [10.1112/jlms/jdv031](https://doi.org/10.1112/jlms/jdv031).

Primary accepted manuscript: [Oxford repository PDF](https://ora.ox.ac.uk/objects/uuid%3A120f2970-8027-4bc5-bd93-b72a7fbc91ff/files/m0f7a4c0d075ccdcf1aa54ad58d333763). The main result is Theorem A in the publication, Theorem 0.0.1 on manuscript p.1, followed by the equivalent L-value formulation on p.2.

For an odd prime ell and disjoint finite sets of odd primes S+, S0, S−, the respective restrictions are: S+ contains no prime −1 modulo ell; S0 contains no prime 1 modulo ell; S− contains no prime simultaneously 1 modulo ell and −1 modulo4. The theorem produces a quadratic imaginary field with ell-unit class number and the requested split, ramified, inert behavior. The original statement does **not** exclude ell itself from the local sets; asking that ell split is permitted. It controls B1χ_D only.

Inspection: exact primary statement and introductory discussion retrieved and read. Full proof not reread. Direct PDF download and screenshot returned403; the web service supplied the primary PDF text. Relevant web locator: `turn135818045view0`, lines12–29. Do not claim a visual or whole-proof check.

Olivia Beckwith, *Indivisibility of class numbers of imaginary quadratic fields*, Research in the Mathematical Sciences4 (2017), article20; DOI [10.1186/s40687-017-0109-x](https://doi.org/10.1186/s40687-017-0109-x). [Author arXiv manuscript](https://arxiv.org/pdf/1612.04443), v4.

Theorem1.1 and Corollary1.2, manuscript pp.4–5, quantify class-number nondivisibility with the local restrictions. The Wiles restatement on p.3 explicitly excludes ell from the local sets. The lower bound concerns one class-number value, not simultaneous higher values. Inspection: introduction and exact theorem/corollary statements read; full proof not read.

## 2. Bruinier and individual half-integral coefficients

Jan H. Bruinier, *Nonvanishing modulo ell of Fourier coefficients of half-integral weight modular forms*, Duke Mathematical Journal98 (1999), 595–611; DOI [10.1215/S0012-7094-99-09819-8](https://doi.org/10.1215/S0012-7094-99-09819-8). [Author PDF](https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/fcmodl.pdf).

Theorem3 (author PDF p.11) assumes an integral Hecke eigenform f of weight k+1/2 and level N, v_ell(f)=0, ell∤N, prescribed primes p_j∤N, and ell outside every A0(p_j,lambda_j). It gives infinitely many squarefree indices with the prescribed Legendre symbols and unit coefficient. For a Cohen series, substitution yields the exact exception product in FV.9. Thus prescribed primes2 and ell are unavailable at level4, and the theorem's own criterion can fail under GD.

Theorem2 (p.10) uses a specified positive-index unit coefficient. Theorem6 (pp.12–13) is explicitly a real-quadratic, even-k statement with a zeta-value unit seed; the following remark only indicates an odd-k analogue. Theorem7 (pp.13–14) treats imaginary quadratic class numbers. None asserts simultaneous units for two different Cohen series.

Inspection: complete statements and provided proofs of Theorems2–4, Lemma5, and the section5.2 application including Theorem6; Theorem7 and its provided proof read. Earlier lemmas used by those published proofs were not all reread. Theorem3 p.11 also visually inspected. Source explicitly leaves one induction detail to the reader. This is not a new proof of Bruinier's results.

## 3. Burungale–Sun and unrestricted character families

Ashay Burungale and Hae-Sang Sun, *Quantitative non-vanishing of Dirichlet L-values modulo p*, Mathematische Annalen378 (2020), 317–358; DOI [10.1007/s00208-020-02017-1](https://doi.org/10.1007/s00208-020-02017-1). [Primary publisher PDF in NSF repository](https://par.nsf.gov/servlets/purl/10184486).

Theorem5.2 (PDF pp.28–29) assumes a fixed periodic function psi of period N, zero mean, psi(−F) nonzero modulo p, p∤F phi(F) N, and gcd(F,N)=1. For fixed nonnegative k it counts nonzero L(−k,chi psi) among **all** characters modulo F. Corollary5.4 (pp.30–31) specializes to fixed Dirichlet characters and the trivial fixed character. There is no p>k hypothesis.

The quadratic restriction is absent. For prime F, even many successful characters can miss the unique quadratic one. Applying the theorem after FV.2 with fixed psi=omega^e is also excluded by p|N. TheoremsC/CorollaryD concern fixed-base-character towers of auxiliary prime-power order; those twists do not vary quadratic fields.

Inspection: introductory results and exact statements read; complete displayed proof of Theorem5.2 read. Its underlying Proposition5.1 and the full42-page argument are imported, not independently re-proved. Corollary5.5 is not used.

## 4. A tempting divisibility paper has the wrong conductor hypothesis

Antal Balog, Henri Darmon, Ken Ono, *Congruences for Fourier coefficients of half-integral weight modular forms and special values of L-functions*, Analytic Number Theory, Vol.1 (1996),105–128. [Author PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/14.Ono/paper.pdf).

Its quadratic Bernoulli divisibility example forms a discriminant containing the target prime p. That violates the present requirement p∤D. It was inspected as a possible obstruction and is not used in FV.2 or in any field-existence assertion. Read scope: introductory statements and relevant Cohen-series formula, not whole proof.

## 5. Concrete remaining requirement

For each admissible pair (ell,e mod ell−1) and the prescribed local family, one needs a **single** negative fundamental D, ell∤D, for which the three factors in FV.8 are all units. Under GD, the character chi_D omega^e has ell-part order greater than2. Separate infinite sets of unit coefficients do not provide this intersection. Ordinary series multiplication gives a coefficient convolution and does not encode that intersection.

No existence theorem with these exact hypotheses was found in the checked primary sources. This sentence reports the scope of the search, not a universal literature claim. Moreover, obtaining these units would still require a separate automorphic converse and stable rank-three exclusion; Fretwell–Roberts3.6 alone has the opposite direction.

## 6. Saved source hashes and check provenance

All local PDFs below are under `literature/field_variation/`.

| File | SHA256 |
|---|---|
| Bruinier_1999.pdf | 77dd2fe2d24607331ff41046c3ee02fc6b86efb49fac18cf47e2b3734ce94497 |
| Beckwith_2017.pdf | f7427d289711eddd1321b6311801260604b395d07181e6c3aa2d5ddc2083f12b |
| Quantitative_Dirichlet.pdf | bd623eebb33c619c462fa7bedb41e5a94eeddae2ddf6cd509f831ea5337fc42a |
| Balog_Darmon_Ono_1996.pdf | bb984e7f57b97cc3db0e18e3cfd34c983dccfc3d8265b199e0f0d051fbeb2610 |

The exact certificate compares Bernoulli-polynomial sums over f with Teichmuller-lift sums over f ell. It passed171 small character cases and a separate progression containing the weight21 at ell7. This is a normalization check, not a proof of the universal statement. Lean-chain's independent whole-proof review passed FV.2 and its corollary; its fresh replay used a byte-identical copy, so that numerical replay is not a second implementation. The separate literature-scope audit is not included in that peer pass.
