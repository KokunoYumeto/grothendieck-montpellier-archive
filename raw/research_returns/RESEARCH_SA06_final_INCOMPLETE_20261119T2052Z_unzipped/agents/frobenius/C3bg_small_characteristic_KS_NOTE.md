# C.3bg: explicit characteristic-two and characteristic-three cup certificates

This is auxiliary finite verification of the already proved generic construction in C.3bg. It does not replace the all-prime proof, the Picard-extension calculation, or the actual proper-family descent. The calculation is the actual Serre-dual normal-boundary cup form; it is **not** the derivative of a Hasse–Witt matrix.

## 1. Exact residue formula

Let \(F\) be a smooth plane quartic over a finite field \(k\), with \(F(0,0,1)\ne0\), and suppose the polynomial \(f_0(y)=F(1,0,y)\) is separable. Write
\[
f(x,y)=F(1,x,y),\qquad f_1(u,v)=F(u,1,v),
\quad u=x^{-1},\ v=y/x.
\]
Find polynomials \(R,A,B\) with
\[
Rf_1+A(f_1)_u+B(f_1)_v=1.
\]
Existence follows from smoothness of the affine curve in the \(z_1=1\) chart. The program solves a finite coefficient linear system and verifies this polynomial identity exactly.

For a quartic \(H\), put \(H_1(u,v)=H(u,1,v)\). A normal lift on that chart is
\[
AH_1\partial_u+BH_1\partial_v.
\]
Its \(x\)-component on the overlap is \(-x^2A(x^{-1},y/x)H(x^{-1},1,y/x)\). Choose any regular normal lift on the \(z_0=1\) chart. The difference is a tangent cocycle representing \(\delta(H)\). Under the adjunction identification \(K_C=\mathcal O_C(1)\), use \(\omega=dx/f_y\) on the latter chart. The tangent generator dual to \(\omega\) is \(f_y\partial_x-f_x\partial_y\). Therefore pairing the tangent cocycle with a quadratic \(q\), viewed as \(q(1,x,y)\omega^2\), gives the differential
\[
-\frac{x^2A(x^{-1},y/x)H(x^{-1},1,y/x)q(1,x,y)}{f_y(x,y)^2}\,dx,
\]
up to the single common sign determined by the order of the Čech charts. The lift regular on the \(z_0\)-chart contributes no residue at \(x=0\), since \(f_0\) is separable. Serre trace is the sum of these residues over the points above \(x=0\).

Set \(B_0=k[y]/(f_0)\). The implicit solution \(y(x)\in B_0[[x]]\) exists uniquely with constant term the class of \(y\), because \(f_y(0,y)\) is a unit. Thus the pairing is the algebra trace \(\operatorname{Tr}_{B_0/k}\) of the coefficient of \(x^{-1}\) in the displayed Laurent expression after substitution. This computes all six values of the symmetric cup matrix. The program verifies the implicit equation and inverse series to the precise finite order required by the pole bound, retaining the bound in its JSON output.

The common sign has no effect on nondegeneracy. The chosen convention gives the identity matrix for the pairs below. Independently, it gives minus the identity for the characteristic-five Fermat deformation already certified in C.3bf.

## 2. Explicit pairs

All coefficients in each pair are reduced modulo its stated characteristic. The full ordered coefficient arrays, six-by-fifteen normal-boundary matrix, Bézout identity, smoothness Gröbner certificates, Hasse matrix, and residue-field modulus are in the retained JSON.

### Characteristic 2

```text
F = z0**4 + z0**3*z2 + z0**2*z1**2 + z0**2*z1*z2 + z0**2*z2**2 + z0*z1**3 + z0*z1*z2**2 + z1**3*z2 + z2**4
H = z0*z2**3 + z1**4 + z1*z2**3
```

The Hasse–Witt matrix is `[[1, 1, 0], [1, 0, 1], [0, 0, 1]]`, with determinant 1; the cup matrix is the identity. All three projective affine-chart singular ideals have Gröbner basis `[1]`. The residue fibre is separable, and the normal-boundary matrix has rank six.

### Characteristic 3

```text
F = 2*z0**3*z1 + z0**3*z2 + 2*z0**2*z1**2 + z0**2*z2**2 + z0*z1**3 + z0*z1**2*z2 + 2*z0*z1*z2**2 + z0*z2**3 + z1**2*z2**2 + 2*z1*z2**3 + z2**4
H = 2*z0**2*z2**2 + 2*z1**2*z2**2 + z1*z2**3 + 2*z2**4
```

The Hasse–Witt matrix is `[[2, 1, 1], [2, 0, 2], [0, 2, 0]]`, with determinant 2; the cup matrix is the identity. All three projective affine-chart singular ideals have Gröbner basis `[1]`. The residue fibre is separable, and the normal-boundary matrix has rank six.

## 3. Independent consistency checks and limits

For each pair the program checks that the cup form vanishes on the trivial normal deformations \(F\) and all nine polynomials \(z_j\partial F/\partial z_i\). This checks the normal-boundary quotient directly, in particular in characteristic two where Euler's relation does not express \(F\) in its Jacobian ideal. The characteristic-five calibration uses the **specific** \(H=z_0^2z_1^2+z_0^2z_2^2+z_1^2z_2^2\) from C.3bf and returns the six coordinates \((4,0,0,4,0,4)\).

No floating-point arithmetic or extension-field sampling proves smoothness: the three affine singular ideals are checked symbolically over the prime field. The exact code uses modular Gaussian elimination for the normal lifts and the six-by-fifteen cup map, and a finite étale four-dimensional residue algebra for the trace. The optional earlier 26-case certificate is separate and has a deliberately weaker finite scope.

Final strengthened certificate run: 2026-11-19T14:12:45.842840+00:00 to 2026-11-19T14:12:47.206643+00:00, elapsed 1.3638054240000201 seconds. The earlier initial run was14:11:18.254905UTC,0.926939306s; the new run adds the ten trivial-direction checks per curve and the fixed Fermat-five calibration.

Files: `code/find_small_characteristic_picard_pairs.py`, `output/C3_small_characteristic_KS_pairs.json`, and `output/C3_small_characteristic_KS_pairs.out`. Full auxiliary proof/source assessment is independent of the computational outcome; no priority claim is made.

## Independent targeted formula and code audit

Recorded at14:18:07.748199UTC from the peer message (the exact peer completion time was not separately exposed): real_weil reported a complete read of the residue derivation and code through Laurent extraction: PASS. The x-component transforms as−x²AH; contraction of qω² is v_x q dx/f_y²; the regular U0 lift has no residue atx0; the two-chart cover is valid because C avoids(0,0,1). The code index i+j+ha+hc−qb−3 is exactly the required x^-1 coefficient, and its finite truncation bound exceeds all pole orders. Finite etale trace and the characteristic-two normal-boundary checks were verified. No independent program rerun is claimed.
