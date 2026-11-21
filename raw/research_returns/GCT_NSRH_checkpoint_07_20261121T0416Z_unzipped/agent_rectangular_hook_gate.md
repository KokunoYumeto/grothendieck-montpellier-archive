# F28: a hook obstruction to signed Young orbits for actual rectangle squares

Author: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC. The new deduction here is the precise failure of the signed-Young-stabilizer sufficient condition on an entire actual rectangular family. The decomposition theorem and the elementary positive formula for that family are known results of Manivel and are cited as such. No priority claim is made.

## 1. Primary statement and exact parity translation

Laurent Manivel, *A note on certain Kronecker coefficients*, arXiv:0809.3710v1 (22 September 2008), **Theorem 1, p.1**, states that for \(d\ge1\),

\[
[(d,d)]\otimes[(d,d)]
=\bigoplus_{\substack{\nu\vdash2d\\\ell(\nu)\le4\\
                         \text{all parts even}}}[\nu]
 \ \oplus\
 \bigoplus_{\substack{\nu\vdash2d\\\ell(\nu)=4\\
                         \text{all parts odd}}}[\nu].
\tag{RH1}
\]

Both sums are effective and every listed constituent has multiplicity one. The theorem is on p.1; its geometric invariant-theory proof is §3, pp.3–4. Primary URL: <https://arxiv.org/pdf/0809.3710>. The theorem and its immediate conventions were read directly in the primary PDF; the proof is cited rather than presented as a new result.

For \(\ell(\nu)\le4\), pad \(\nu\) by zeros to four parts. Then RH1 is exactly

\[
g(\nu,(d,d),(d,d))
=\mathbf1_{\nu_1\equiv\nu_2\equiv\nu_3\equiv\nu_4\pmod2}.
\tag{RH2}
\]

Indeed, if the common parity is even, all nonzero parts are even and the length is at most four. If the common parity is odd, none of the padded parts can be zero, so there are exactly four odd parts. Conversely each of the two cases in RH1 has the stated common parity. For length greater than four the coefficient is zero. The same statement holds for the square of the transposed rectangle \((2^d)\), since transposition tensors each Specht module with sign and the two signs cancel.

### A full restricted rational-point rule

For \(\ell(\nu)\le4\) define the affine point

\[
P_\nu=
\left\{\left(
\frac{\nu_1-\nu_4}{2},
\frac{\nu_2-\nu_4}{2},
\frac{\nu_3-\nu_4}{2}\right)\right\}\subset\mathbf R^3.
\tag{RH3}
\]

The three equations \(2x_i=\nu_i-\nu_4\) show that

\[
g(N\nu,(Nd,Nd),(Nd,Nd))
=\#(NP_\nu\cap\mathbf Z^3)\qquad(N\ge1).
\tag{RH4}
\]

Each side is one exactly when all three differences \(N(\nu_i-\nu_4)\) are even. This is a homogeneous exact Ehrhart model for the entire height-two rectangular family, with ambient dimension three, affine dimension zero, denominator at most two, and a description and separation test polynomial in the binary input length. For \(\ell(\nu)>4\), choose the empty polytope; stretching does not change length, so the zero formula remains exact. This is a cited known-formula consequence, not a new route from spectral purity or theta lifting. The parameter restriction to height two (or width two by transposition) remains essential.

## 2. An explicit hook-multiplicity lemma

Let \(n\ge2\), and let

\[
H=S_{a_1}\times\cdots\times S_{a_r}\le S_n,\qquad
a_i\ge1,\quad \sum_i a_i=n,
\]

be a Young subgroup with \(r\) nonempty blocks. Let
\(\chi=\chi_1\boxtimes\cdots\boxtimes\chi_r\), with each factor trivial or sign. For a singleton block those characters coincide; either designation is allowed and contributes zero to the integer

\[
s=\sum_{\chi_i=\mathrm{sgn}}(a_i-1).
\]

Then, for \(0\le k\le n-1\),

\[
\left[
\operatorname{Ind}_H^{S_n}\chi:
[(n-k,1^k)]
\right]
=\binom{r-1}{k-s},
\tag{RH5}
\]

where the binomial coefficient is zero outside \(0\le k-s\le r-1\). In particular every hook degree in the consecutive interval
\(s,s+1,\ldots,s+r-1\) occurs positively.

### Proof

Let \(U_n\) be the standard representation, namely the sum-zero subspace of the permutation representation \(k^n\) over a characteristic-zero field. Its restriction to \(H\) is

\[
\operatorname{Res}_H U_n
\simeq \bigoplus_{i=1}^r U_{a_i}\oplus k^{r-1},
\tag{RH6}
\]

where the last summand is trivial and \(U_1=0\). This follows by separating the constant line from each permutation block and then removing the one global constant line.

Recall the classical identification
\(\bigwedge^jU_a=[(a-j,1^j)]\) for \(0\le j\le a-1\).
For completeness, it follows directly from the same Pieri rule used in the signed-orbit criterion: the oriented \(j\)-subset basis of \(\bigwedge^j k^a\) gives
\(\operatorname{Ind}_{S_j\times S_{a-j}}^{S_a}(\mathrm{sgn}\boxtimes1)\).
For \(1\le j\le a-1\), Pieri decomposes this as the two adjacent hooks
\([(a-j,1^j)]\oplus[(a-j+1,1^{j-1})]\).
Since \(k^a=k\oplus U_a\), its \(j\)-th exterior power is
\(\bigwedge^jU_a\oplus\bigwedge^{j-1}U_a\).
Starting with \(\bigwedge^0U_a=1\), induction in the semisimple category gives the claimed hook identification. When \(a=1\) only degree zero occurs.

Expand the \(k\)-th exterior power of RH6. To obtain the prescribed factor \(\chi_i\) from a nonsingleton \(U_{a_i}\), its exterior degree must be zero for a trivial \(\chi_i\), and \(a_i-1\) for a sign \(\chi_i\); the intervening hook modules are distinct irreducibles. On a singleton block the only available exterior degree is zero, as required under either designation. Thus the sum of the degrees forced by the nontrivial blocks is exactly \(s\). The remaining \(k-s\) degrees come from the trivial \((r-1)\)-space, whose corresponding exterior power has dimension \(\binom{r-1}{k-s}\). Frobenius reciprocity and \(\bigwedge^kU_n=[(n-k,1^k)]\) prove RH5. ∎

The interval always lies in the valid hook range: \(s\ge0\) and
\(s\le\sum_i(a_i-1)=n-r\), hence \(s+r-1\le n-1\).
No issue arises from singleton blocks or an empty exterior power.

## 3. Exact obstruction for the actual rectangle-square module

**Proposition RH-Y.** For every \(d\ge2\), the actual \(S_{2d}\)-module

\[
M_d=[(d,d)]\otimes[(d,d)]
\]

has no signed permutation basis for which every underlying-label stabilizer is conjugate to a Young subgroup.

### Proof

Write \(n=2d\ge4\). Suppose such a basis existed. The explicit orbit-module isomorphism proved in the signed-orbit proposition gives

\[
M_d\simeq
\bigoplus_O\operatorname{Ind}_{H_O}^{S_n}\chi_O,
\tag{RH7}
\]

with \(H_O\) a Young subgroup up to conjugacy and each \(\chi_O\) a product of trivial and sign characters. This is a direct sum of actual modules. In the representation Grothendieck group its coefficients in the irreducible basis are all nonnegative, so a constituent of any orbit summand cannot be canceled by another orbit.

By RH1, the hooks in \(M_d\) have precisely the degrees

\[
k=0\quad\hbox{and}\quad k=3.
\tag{RH8}
\]

To verify this explicitly, a hook \((n-k,1^k)\) has all parts even only if \(k=0\). It has exactly four odd parts only if \(k=3\); in that case its first part \(n-3\) is positive and odd because \(n\ge4\) is even. Both occur with multiplicity one.

If an orbit stabilizer had \(r\ge2\) nonempty blocks, RH5 would force at least two consecutive hook degrees in that summand. The set \(\{0,3\}\) contains no consecutive pair. At least one forced hook would therefore be absent from \(M_d\), contradicting effectiveness in RH7.

All orbit stabilizers must consequently have \(r=1\), so are the whole group \(S_n\). Such orbit summands are just the one-dimensional trivial or sign representations. But RH1 also contains the constituent \([(2d-2,2)]\), whose two positive even parts make it neither trivial nor sign for every \(d\ge2\). This is impossible in a direct sum of those one-dimensional modules, completing the proof. ∎

At the edge \(d=2,n=4\), the degree-three hook is the sign representation, and the remaining constituent is \([(2,2)]\). The consecutive-hook argument still excludes every proper Young stabilizer, and the final \([(2,2)]\) constituent still gives the contradiction. At \(d=1\) the module is trivial, so the hypothesis \(d\ge2\) is necessary.

In fact allowing arbitrary scalar phases on the basis does not change this conclusion **if its stabilizers are still Young subgroups**: every one-dimensional characteristic-zero character of a symmetric group is trivial or sign (and that of \(S_1\) is trivial), so every one-dimensional character of the product is of the form already covered. This is not a claim about arbitrary subgroups.

### What this excludes, and what it does not

The Young-stabilizer/Pieri condition in F23 is a sufficient positive-rule mechanism. RH-Y proves that this particular mechanism cannot describe the whole specified unprojected rectangle-square module, even though its exact positive decomposition is already known by RH1. It does not exclude other positive rules, non-Young stabilizers, a description after further projectors, a different representation carrying the same numerical multiplicities, or the existing two-row crystal rule.

The conclusion is an effective-representation obstruction. A virtual alternating sum of signed Young modules can cancel the forbidden hooks and is not subject to this proof. Replacing the direct sum RH7 by a virtual equality would also abandon the positive orbit-count conclusion that motivated the criterion.

## 4. A concrete non-Young signed model shows the scope is sharp

For \(d=2\), let \(S_4\) permute the three pairings of four letters. Its permutation module is \(1\oplus[(2,2)]\): subtracting the constant line leaves the two-dimensional irreducible with character \((2,0,2,-1,0)\) on cycle types \((1^4),(2,1,1),(2,2),(3,1),(4)\). The already checked character identity, or RH1 at \(d=2\), gives

\[
[(2,2)]^{\otimes2}\simeq k\{\text{three pairings}\}\oplus\mathrm{sgn}.
\tag{RH9}
\]

This is an actual signed permutation model with a three-element orbit and a sign line. The stabilizer of a pairing is \(S_2\wr S_2\), of order eight. A Young subgroup of \(S_4\) has order \(24,6,4,2\), or \(1\), so that stabilizer is not Young. Thus RH-Y does not even rule out a signed basis for the smallest nontrivial rectangle square; it identifies precisely why the additional Pieri stabilizer hypothesis fails. The equivariant isomorphism is a characteristic-zero representation isomorphism, not an asserted identification with a designated geometric component basis.

## 5. Check record and source boundaries

- RH1 is Manivel's known theorem. It is cited with its actual numbered statement and exact length/parity hypotheses; no new proof of the entire external theorem is claimed.
- RH2–RH4 are direct consequences: padding, three parity differences, and dilation were checked explicitly, including zero padding and the length-greater-than-four case.
- RH5 is fully proved by restriction of the standard representation and exterior powers. The required hook identification is also derived briefly from the classical Pieri identity, whose verified primary locator is Postnikov/Lian, Theorem 7.10, printed p.16, in primary_sources/Postnikov_Lian_315.pdf.
- RH-Y is fully proved from the effective orbit decomposition and RH5; it includes singleton blocks, the \(d=2\) edge and the exact limit on allowing non-Young subgroups.
- RH9 uses the explicit three-pairing action and the same S4 character already independently checked in the paper. It supplies a constructive restricted signed model without claiming a canonical basis comparison.
- A fresh independent review of the complete note has been requested separately. No Lean or other formal-kernel check is claimed.
