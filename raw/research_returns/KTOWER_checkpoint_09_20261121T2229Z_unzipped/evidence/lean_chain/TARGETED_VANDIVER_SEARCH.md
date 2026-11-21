# Targeted Vandiver certificates at the next three exceptional primes

## Outcome and scope

This bounded primary-literature and author-data search did **not locate a published evaluated cyclotomic-unit certificate** for any of the three requested components:

| Bernoulli index \(k\) | Prime \(p\) | Component needed |
|---:|---:|---|
| 34 | 151628697551 | \(A_p^{[34]}\) |
| 36 | 26315271553053477373 | \(A_p^{[36]}\) |
| 38 | 154210205991661 | \(A_p^{[38]}\) |

This records what was located and inspected. It is not a claim that no certificate exists, and it is not a mathematical nonexistence result. The negative endpoint remains −16. No \(O(p)\) scan, cyclotomic-unit product, new Hecke calculation, or message to an external researcher was initiated.

The exact numerator factorizations and primality of these three integers have already been proved by the separate small standard-library certificate negative_endpoint_certificate.py. A Bernoulli factorization establishes an irregular pair; it does not establish the positive class-component vanishing requested here.

## Exact primary orientation, including a printed correction

Buhler–Harvey, *Irregular primes to 163 million*, Section 4, author pages 4–5, identifies the component \(A_k\) with the corresponding \(\omega^k\) unit-index component. Their \(A_{p-k}\), indexed modulo \(p-1\), is \(A^{[1-k]}\); hence this agrees with the reflection convention used in the carried proof.

For an auxiliary prime \(q=Mp+1\), and a primitive \(p\)-th root \(z\) modulo \(q\), the **corrected** test is

\[
 V_{p,k}=\prod_{c=1}^{(p-1)/2}
    (z^{c/2}-z^{-c/2})^{c^{p-1-k}}\pmod q,
 \qquad V_{p,k}^{M}\ne1\pmod q.
\]

Here \(c/2\) is interpreted modulo \(p\). Success proves \(A_p^{[k]}=0\). The outer exponent is **\(c^{p-1-k}\)**. In particular, the test at \(k=34\) addresses the positive component 34, not the already-settled component −34.

Hart–Harvey–Ong, *Irregular primes to two billion*, Section 7, author page 13, explicitly corrects the earlier displayed exponents on \(z\) from \(c\) to \(c/2\). That entire section, author pages 13–14, was read. It does not change the outer exponent or the character orientation. The earlier expression is the corrected expression evaluated at the alternative primitive root \(z^2\), so it is also a sufficient non-power test; nevertheless the corrected printed convention is now used in the audit. No residue computation relied on the old display.

The complete Buhler–Harvey Section 4 and the relevant Section 6 implementation discussion were read. The cyclotomic-unit/class-component comparison is an explicitly imported primary criterion, not newly reproved here. The Hart–Harvey–Ong section separately corrects the Iwasawa-invariant test, reinforcing that its harmonic criteria must not be substituted for a Vandiver certificate.

Primary sources:

- Buhler–Harvey: <https://arxiv.org/pdf/0912.2121>.
- Hart–Harvey–Ong: <https://arxiv.org/pdf/1605.02398>, published DOI <https://doi.org/10.1090/mcom/3211>.

The former PDF is saved in primary/buhler_harvey_irregular_2009.pdf. The latter PDF and text are saved in primary/targeted_vandiver/.

## What the exact-number hits actually contain

1. **Mazur's author manuscript.** The exact-prime search finds *How can we construct abelian Galois extensions of basic number fields?*, Appendix II, author pages 57–58. Footnote 64 on page 57 lists \((151628697551,34)\) and \((26315271553053477373,36)\) as irregular pairs. The surrounding account of Stein's computations explicitly restricts them to \(p<10^7\) and weight below 8000. The discussion concerns Eisenstein-congruent newforms and the associated Hida algebra. It supplies no evaluated unit certificate for these two much larger primes. This whole local passage and its numerical scope were read; no full-paper proof review is claimed.

   Author PDF: <https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/a/189/files/2023/01/How-can-we-construct-abelian-Galois-extensions-of-basic-number-fields.pdf>.

2. **Harvey's current author data page.** The research page links the irregular-pair dataset associated with *Irregular primes to two billion*. The paper's abstract and Section 1 specify \(p<2^{31}\), which excludes all three requested primes. Section 7 says the unit-test values were independently computed twice and are available on request; that statement concerns the paper's tested range. The linked 557 MB irregular-pair dataset was not downloaded, since its stated range cannot contain the requested primes. The older data for the 163-million paper are marked as superseded. None of these statements is promoted to a claim about every existing dataset.

   Author page: <https://web.maths.unsw.edu.au/~davidharvey/index.php?page=research>.

3. **Kellner's author site and thesis.** The Bernoulli page provides numerator factorizations and higher irregular-pair information. Its displayed irregular-pair download is for primes below 20,000. In the thesis *Über irreguläre Paare höherer Ordnungen*, printed pages 95–96, the class-number conclusion explicitly assumes Kummer–Vandiver separately from the nondegeneracy condition on higher irregular pairs. These pages were inspected directly. Searches of the downloaded extracted text found none of the three exact decimal primes; this is only a text-search fact, not proof of their absence from every related publication or dataset.

   Author page: <https://www.bernoulli.org/>.
   Thesis: <https://www.bernoulli.org/~bk/irrpairord.pdf>.

4. **Other exact-number search hits.** The searches returned Bernoulli-numerator lists, irregular-pair tables, and occurrences of these numbers in unrelated mass-formula or modular-form calculations. These were used only to identify possible primary leads. None of the inspected primary leads supplied the required nontrivial residue \(V_{p,k}^{(q-1)/p}\).

## Search record and usable remaining target

The search included the exact decimal primes with “Vandiver,” “cyclotomic,” “unit,” and “class,” as well as the pairs of indices 34 and 38, author pages, and the relevant paper titles. The associated JSON records the query strings, primary-source paths and hashes, and the actual review scope. Search indexing and source availability limit this exercise.

The prior certificate already supplies a prime \(q=1819544370613=12p+1\) and an order-\(p\) root for the smallest target \(p=151628697551\). It supplies corresponding exact auxiliary inputs for the other two primes as well. What is still missing is an **evaluated nontrivial corrected unit residue**, or a different proved argument that kills the same positive component. Computing an opposite-character Bernoulli value, or merely knowing that the irregular numerator has valuation one, does not supply that missing conclusion.
