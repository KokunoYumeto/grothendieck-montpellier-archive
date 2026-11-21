# Sixth symmetric power: primary-source scope audit

**Run:** 21 November 2026 UTC, GPT-6 Astra Pro,
effort setting not exposed, /root/rectangular_cases.

The lead is the same OpenAI manuscript already recorded in
work/root/current_ranges.md:
*Foulkes' conjecture for the sixth symmetric power*,
25 September 2026. This review does not introduce a new
mathematical statement or count its restatement as a new result.

## 1. Exact locators and relation to the current map ranges

| Primary locator | Exact result used in this comparison |
|---|---|
| Theorem 1.1, printed p.1 | An equivariant injection exists from \(\operatorname{Sym}^6\operatorname{Sym}^bV\) into \(\operatorname{Sym}^b\operatorname{Sym}^6V\) for every \(b\ge6\), equivalently the stated multiplicity inequalities. |
| Equation (1) and Corollary 2.1, printed p.3 | The normalized multiplication map is \(\mu_{a,b}=h_{b,a}\). The companion yields surjectivity at \(b\ge a(a-1)\), hence \(b\ge30\) for \(a=6\). |
| Lemma 2.3 and Corollary 2.4, printed pp.4–5 | The chart places the complete relevant weight space in the multiplication image for tail degree \(D\le b\). |
| Lemma 2.5, Corollary 2.6, Proposition 2.7, printed p.6 | The independent common-polarization/module argument gives full canonical surjectivity for \(b\ge a(a-1)^2\). |
| Finite verifications 5.1 and 6.1; §7 final proof | Exact coefficient comparisons complete the finite range; the source supplies two complete C++ programs and recorded reference streams. |

The existing register already has canonical surjectivity for \(a=6,b\ge25\)
from the fully read Sra theorem.
R-046 also covers the paper's first-row range:
\(t\le D\le b\) gives \(\lfloor(D+t)/2\rfloor\le b\).
Thus the listed actual-map ranges add no new range to that register.
The full sixth-power multiplicity theorem remains a cited source result.

## 2. The precise multiplicity-space morphisms

Let
\[
F_\lambda=\operatorname{Hom}_{GL(V)}
 (S_\lambda V,\operatorname{Sym}^6\operatorname{Sym}^bV),\qquad
Q_\lambda=\operatorname{Hom}_{GL(V)}
 (S_\lambda V,\operatorname{Sym}^b\operatorname{Sym}^6V).
\]
The prescribed canonical map has blocks
\[
h_{b,6}=\bigoplus_\lambda
 1_{S_\lambda V}\otimes M_\lambda,\qquad
M_\lambda:Q_\lambda\longrightarrow F_\lambda.
\]
The normalized tensor averaging in §2.1 is the same scalar-one
multiplication map used in R-037 EP.4.

At each label where the canonical map is onto, choose an invariant
complement to its kernel. Restriction there is an isomorphism, and its
inverse is an actual equivariant section. In a multiplicity-space basis
this means choosing a right inverse \(J_\lambda\) with
\(M_\lambda J_\lambda=1\).
This is precisely the section construction in Corollary 2.1.

The finite coefficient calculation supplies
\(\dim Q_\lambda\ge\dim F_\lambda\).
Choosing ordered bases then gives the explicit coordinate inclusion
\(J_\lambda(e_i)=f_i\), and
\(\bigoplus_\lambda1\otimes J_\lambda\) is an equivariant injection.
The finite algorithm computes these dimensions; it does not compute
the matrices \(M_\lambda\).

The exact square example already in the register fixes the map relation:
at \(b=6\), the label \((20,7,6,1,1,1)\) has both multiplicities one,
and Cheung–Ikenmeyer–Mkrtchyan Theorem 6(c) gives \(M_\lambda=[0]\).
An equivariant injection on that common line has matrix \([1]\).
These are explicit morphisms between the same representation spaces;
the register retains the proven zero rank of the specified canonical map.

## 3. Completed reading and verification scope

I read the entire mathematical text of §§1–7 in the retained
primary TeX and the matching manuscript PDF, and read both complete
C++ source files fetched anew from the official repository.
The review checked:

- the normalized invariant-ring map, dimensional specialization,
  determinant shifts, chart denominator clearing, and full
  common-polarization/module-generation proof;
- the signed-strip determinant, containment inequalities, monotone
  source bound, and both exact Newton recurrences;
- the entire triangulation/sumset proof and the leading-monomial
  multiplicity construction, including its capped affine dimension;
- the residue grid, all lower-bound propagation and transport maps,
  and the exhaustive finite range reduction;
- the seven degree-independent band numerators, the \(b=26,k=27\)
  zero boundary, all Laurent shifts and alternant signs, the entire
  stored exponent window, and conversion to arbitrary precision;
- the indexing, signed-integer bounds, loop ranges, barriers, and
  correspondence of both C++ implementations with those formulas.

No mathematical fault was found in that reading.
The numerical assertions produced by complete program execution are
retained at the source's stated verification scope.

I also downloaded and ran the official read-only command
`verify_computations.py --check`.
It passed the primary source/reference-stream hashes,
all 62 recorded table rows, manuscript-table matching,
and the arithmetic/index inequalities.
The exact output is
`sixth_source_audit/SIXTH_REFERENCE_CHECK.txt`.
It explicitly records
`certificate_programs_executed: false`.
Neither C++ certificate program was executed in this review,
and no Lean proof was run.

The freshly retrieved official lean/docs/210.md states the exact
formalization scope: canonical surjectivity at \(b\ge a(a-1)\),
and its equivariant section consequence; the sixth specialization
is \(b\ge30\). Its scope does not include the finite \(6\le b\le29\)
coefficient computation. This audit does not extend that claim.

## 4. Primary paths and retained receipts

The official source directory is:

https://github.com/openai/math/tree/main/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026

Primary PDF:

https://raw.githubusercontent.com/openai/math/main/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf

Official formalization scope:

https://raw.githubusercontent.com/openai/math/main/lean/docs/210.md

The initial lead and accessible manuscript rendering were:

https://mathcommunity.github.io/oai-math-revised/papers/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/

https://mathcommunity.github.io/oai-math-revised/papers/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf

Every new primary fetch has its URL, byte count and SHA256 in
`sixth_source_audit/PRIMARY_FETCH.json`.
The official certificate sources, manifest, streams, two table-bearing
TeX sections, verifier, README and Lean scope note were read under
`sixth_source_audit/`; their exact fetch locations and hashes are retained
in the delivered manifest. The full mathematical TeX already present under
`work/external/sixth_sections/` was read in this review.

