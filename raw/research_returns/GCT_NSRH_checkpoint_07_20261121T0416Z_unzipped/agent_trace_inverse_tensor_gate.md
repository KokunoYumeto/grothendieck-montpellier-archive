# F38 proposal: an inverse Euler trace is not a tensor inverse

Author/checker: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**Result: PASS for the proposed construction and obstruction, with the precise target category below.** A single finite-type stack gives the all-extension reciprocal of the \(\mathbb P^1\) trace. Its product with \(\mathbb P^1\) has unit Euler trace and nonunit actual cohomology. Moreover no actual tensor inverse of the usual \(R\Gamma(\mathbb P^1)\) exists in the usual unbounded derived category of Weil vector spaces. This excludes extending that specified realization through an object-level tensor localization; it does not exclude a different realization, a formal Euler-class localization, or scalar division at a fixed parameter.

## 1. The reciprocal stack and its actual cohomology

Over \(\mathbb F_q\), put
\[
\mathcal Z=\mathbb A^1\times\mathbb G_m^2\times B\mathrm{GL}_2,
\qquad \mathcal W=\mathbb P^1\times\mathcal Z.
\tag{TI1}
\]
These are smooth finite-type Artin stacks with affine stabilizers. Their dimensions are \(-1\) and zero, respectively. The same torsor and column-count calculation as F35 gives, for \(Q=q^n\),
\[
\#\mathcal Z(\mathbb F_Q)
=\frac{Q(Q-1)^2}{Q(Q-1)^2(Q+1)}=\frac1{Q+1},
\qquad
\#\mathcal W(\mathbb F_Q)=1.
\tag{TI2}
\]
Mass is groupoid mass, not a count of isomorphism classes without automorphism weights.

Let \(c_s=\lfloor s/2\rfloor+1\). Sun's exact compact cohomology of \(B\mathrm{GL}_2\), Example7.4, p.109, and the compact-support Künneth formula give
\[
H_c^j(\mathcal Z_{\overline{\mathbb F}_q},\mathbb Q_\ell)
\simeq
\bigoplus_{\substack{0\le b\le2,\ s\ge0\\j=-2-b-2s}}
\mathbb Q_\ell(b+s+1)^{\oplus\binom2b c_s}.
\tag{TI3}
\]
Indeed the affine factor contributes degree2 and twist\(-1\), the torus contributes degree\(4-b\) and twist\(-(2-b)\), and the classifying factor contributes degree\(-8-2s\) and twist\(s+4\). Their sums give exactly (TI3). In particular these groups are nonzero in arbitrarily negative degrees.

Let
\[
H=R\Gamma(\mathbb P^1_{\overline{\mathbb F}_q},\mathbb Q_\ell)
\simeq \mathbb Q_\ell\oplus\mathbb Q_\ell(-1)[-2],
\qquad K=R\Gamma_c(\mathcal Z_{\overline{\mathbb F}_q},\mathbb Q_\ell).
\tag{TI4}
\]
This is the ordinary projective bundle calculation already used in F15/F16. Properness of \(\mathbb P^1\) and Künneth give
\[
R\Gamma_c(\mathcal W)\simeq H\otimes K,
\qquad
H_c^j(\mathcal W)
\simeq H_c^j(\mathcal Z)\oplus H_c^{j-2}(\mathcal Z)(-1).
\tag{TI5}
\]
Thus \(H_c^0(\mathcal W)=\mathbb Q_\ell\), but
\[
H_c^{-1}(\mathcal W)=\mathbb Q_\ell(1)^{\oplus2}\ne0.
\tag{TI6}
\]
The complex is unbounded below and cannot be the one-dimensional unit. Its nonzero negative-degree groups are actual direct summands in (TI5), so they cannot cancel as cohomology.

## 2. Exact trace cancellation and convergence

For \(x=q^{-n}\), (TI3) has Euler series
\[
x\frac{(1-x)^2}{(1-x)(1-x^2)}=\frac{x}{1+x}
=\sum_{j\ge0}(-1)^j x^{j+1}.
\tag{TI7}
\]
Every positive real eigenvalue moment converges absolutely. At moment \(t>0\), the ungrouped sum is
\[
\frac{q^{-t}(1+q^{-t})^2}{(1-q^{-t})(1-q^{-2t})}
=\frac{q^{-t}(1+q^{-t})}{(1-q^{-t})^2}<\infty.
\tag{TI8}
\]
Sun's trace theorem therefore applies directly, and the explicit convergence also justifies regrouping. Since \(H\) has Euler trace \(1+x^{-1}\),
\[
\operatorname{Tr}(F^n\mid H\otimes K)
=(1+x^{-1})\frac{x}{1+x}=1.
\tag{TI9}
\]
Within the algebra of these convergent trace sequences, the trace of \(K\) is the multiplicative inverse of the trace of \(H\). Within the ordinary derived category, \(H\otimes K\) is not the unit by (TI6).

This also shows exactly why F32's visible-spectrum uniqueness does not identify objects: after grouping the Euler roots of \(\mathcal W\), the only visible root is one with multiplicity one. The infinitely many other cohomology classes cancel between degrees. Uniqueness is a statement about that grouped spectrum, not a faithfulness theorem for the trace functor.

## 3. No actual tensor inverse in the specified realization category

Use the usual unbounded derived category of Weil \(\mathbb Q_\ell\)-vector spaces, with its algebraic derived tensor product, and the exact conservative forgetful functor to the derived category of vector spaces. All arguments below already hold after forgetting Frobenius. They do not concern completed tensor products with a different realization or a different trace functional.

**Tensor-invertibility lemma.** If an object in the derived category of vector spaces has a tensor inverse, its total cohomology is one-dimensional and is concentrated in one degree. In the Weil category a tensor-invertible object is therefore a one-dimensional Weil representation placed in one degree. Conversely such an object has its dual, with opposite shift, as a tensor inverse.

**Proof.** Over a field every complex splits as its cohomology with zero differential plus a contractible complex; the decomposition is available for unbounded complexes as well. Tensoring a contractible complex is contractible, and algebraic tensor totalization uses direct sums. Consequently Künneth gives
\[
H^m(A\otimes B)\simeq\bigoplus_{i+j=m}H^i(A)\otimes H^j(B).
\]
If \(A\otimes B\) is the unit, neither factor is zero. Choose a nonzero cohomology group of each. Two independent total cohomology vectors in either factor, whether in the same or different degrees, would give at least two independent total cohomology vectors in the product. Thus each total cohomology must have dimension one. It lies in a single degree, and the two degrees add to zero. In the Weil category, truncation identifies an object with its unique cohomology representation shifted to that degree; a one-dimensional Weil representation has an invertible Frobenius scalar and the asserted dual. ∎

For the particular \(H\) in (TI4), a still shorter argument suffices: if \(H^a(B)\ne0\), then \(H\otimes B\) has nonzero cohomology in both degrees \(a\) and \(a+2\). Direct sums cannot cancel either group. Therefore no nonzero \(B\), bounded or unbounded, can make \(H\otimes B\) the unit.

Let \(\mathcal C\) be any monoidal category with a strong monoidal realization \(R:\mathcal C\to D(\mathrm{Weil})\), and suppose \(R(P)=H\). There is no tensor localization making \(P\) an invertible object through which this specified realization still factors as a strong monoidal functor. Strong monoidal functors preserve inverses, contradicting the lemma. **Faithfulness is not needed for this fixed-image obstruction.** An abstract localization which changes or loses the realization is outside the assertion.

## 4. Consequence for the actual normalization factor

Under \(v=Q^{\pm1/2}\), the scalar \(D=(v+v^{-1})^2\) is
\[
D(Q)=Q+2+Q^{-1}=Q^{-1}(Q+1)^2.
\]
The ordinary Tate complex
\[
H_D=\mathbb Q_\ell(1)\otimes H^{\otimes2}
\]
has exactly this all-extension Euler trace, but has total cohomology dimension four and is not tensor-invertible. The convergent stack complex
\[
K_D=\mathbb Q_\ell(-1)\otimes K^{\otimes2}
\]
has trace \(Q/(Q+1)^2=D(Q)^{-1}\). Their tensor product has Euler trace one, and is still not the unit.

More generally, no tensor-invertible object in the specified derived Weil category can have trace \(D(q^n)\) for all \(n\): an invertible object's Euler trace is \(\pm\alpha^n\). The minus sign is impossible because both the first and second traces here are positive. With the plus sign it would require \(D(q^2)=D(q)^2\), whereas
\[
D(q)^2-D(q^2)=4(q+q^{-1}+1)>0.
\]
Thus the obstruction is not specific to the chosen projective-line representative of the trace.

This says nothing against multiplying a linear operator by the numerical scalar \(D(q)^{-1}\) at a fixed \(q\). That operation does not assert that a positive grading object has become tensor-invertible or that the scalar is reevaluated at \(q^n\). It also does not rule out the formal coefficient localization in F27. The excluded additional demand is an object-level tensor inverse compatible with the same usual derived Weil realization and the specified all-extension trace.

## 5. Sources and review scope

The stack input is exactly the primary material already inspected for F35: Sun, *L-series of Artin stacks over finite fields*, ANT6(2012), Theorem1.1 p49, Definition4.1 p84, Theorem4.2 p85, Example7.4 p109; Laszlo--Olsson II, PMIHES107(2008), Theorem11.0.14 p204. The \(\mathbb P^1\) calculation is the known projective bundle formula; the earlier inspected primary teaching text is Milne, *Lectures on Étale Cohomology*, v2.21, Example16.3 p109 and Theorem23.2 pp139--140. No general source theorem is claimed newly proved here.

All new claims (TI1)--(TI9), the tensor-invertibility lemma, the strong-monoidal fixed-image obstruction, and the \(D\)-trace corollary have the complete proofs above. Generalized completions, nonstandard generator correspondences, and alternative categorical traces are not excluded. A fresh independent review should be recorded before main-paper insertion.
