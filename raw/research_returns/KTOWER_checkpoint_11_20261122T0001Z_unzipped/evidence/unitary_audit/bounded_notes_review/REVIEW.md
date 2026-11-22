# Two bounded notes: independent whole-proof review

Reviewer: `/root/unitary_audit`, GPT-6 Astra Pro. Effort setting is not exposed.
No Lean kernel execution, new class-group computation, discriminant search,
or finite K-degree computation is claimed.

## KT-ORDER-FIVE-PDIV-WEIGHT

Entire proof read: `evidence/main_gate/order_five_pdiv_weight.tex`, SHA-256
`4f16d4a9ae9dcbc7b4118c779997cbc50bf4a4977b7071fe8400417645e07651`.
Result: PASS.

The condition p|e makes the coefficient D[p^2] trivial on G_Q(mu_p),
because the cyclotomic image is 1+pZ_p. Its remaining action factors
through the prime-to-p group Delta and is the unique Teichmuller lift.
The nontrivial residual order-five character makes global and p-local
H0(D) vanish. At every other inertia group, H0(D)=D is p^2-divisible.
The exact coefficient sequence therefore preserves all local conditions.
Restriction is injective, and the unramified homomorphism factors through
the ordinary ideal class group with the stated character orientation.

The target Hom group has order at most p by the already reviewed class
length bound. A finite cyclic group of order p^a has p^2-torsion of order
p^min(a,2), so a<=1. Full-group VK-PT transfers this conclusion to the
finite K-primary group. Its hypotheses and the explicit abstract-group
wording are correct. This is a conditional exponent refinement for p|e;
no additional character or prime is excluded.

## KT-COHEN-UP-REFORMULATION and KT-HECKE-SQUARE-CLASS-SCOPE

Entire proof read: `evidence/lean_chain/cohen_hecke_support.tex`, SHA-256
`965f5fc11fc630b18362b3fa050d9dba71a783a5abd2e09e23a6459ea5dae9b8`.
Result: PASS.

The full-series congruence includes all of the following checked cases:

- The constant term is the ordinary Kummer congruence from index p+3 to 4.
- The two forbidden plus-support residue classes vanish on both sides.
- Fundamental discriminant multiplication by -p is correct for odd and
  even D, both when p divides D and when it does not.
- D=-p gives D-dagger=1 and m-dagger=pm. The regularizer c=2 is a unit
  because its residue is -3. The trivial character is therefore included.
- For the other prime-to-p character factors, CRT supplies the common
  regularizing unit, and the two integrands coincide by Euler's criterion.
- Every p-local divisor-sum factor is 1 modulo p, including the extra
  power of p in m-dagger. All other local factors coincide directly.

The standard full divisor-sum expression at square indices is consistent
with the independent BMO normalization. At r=2 it is -P_2(1,m)/12.
For example, at a prime power m=l^s, their defining divisor sum is
-(1/12)[sum(i=0..s)l^(3i)-l*sum(i=0..s-1)l^(3i)], exactly the displayed
P-factor. No missing factor two or exceptional square term remains.

For the second proposition, I checked the recurrence both at l not
dividing m (including l|D) and at l|m. It is an exact geometric-sum
identity. The equation at n=0 is tautological. Consequently arbitrary
fundamental-square-class seeds do satisfy all the asserted formal
equations. The formal example's positive coefficientwise product with
H_3 is zero because beta_3 vanishes on its sole supported square class.
The proof correctly makes no modularity assertion for that formal series.
Fourier differentiation and the specified square-index operations cannot
create support in a previously absent fundamental square class.

## Primary-source read scopes

P. Guerzhoy, *Quadratic congruences for Cohen-Eisenstein series*, Glasgow
Math. J. 41 (1999), 141-144. PDF SHA-256
`d15347938f747a144a4101e2f78a078ced020d4e21033fc3a7e76d987a56dd9d`.
I read the entire extracted four-page text, including formula (1), exact
Propositions 1-2, equations (2)-(4), and the short deduction of Proposition
2 from the integral measure. These propositions allow conductor divisible
by p. The published construction of the Mazur measure is imported; no
fresh audit of its foundational references is claimed. The later quadratic
congruence theorem is not needed for the reviewed proof, which checks its
own two integrands by Euler's criterion.

A. Balog, W. J. McGraw and K. Ono, *The arithmetic of the coefficients of
half-integral weight Eisenstein series*, Acta Arith. 107 (2003), 337-344.
PDF SHA-256
`56ea86ca8b77ff7e5afcc375d8de162392294f764d79b11f98547aa4bbb0f903`.
I read definitions (1.2)-(1.4) and their complete surrounding setup on
printed pp. 337-338. The later main theorem is not used.

The earlier p=83, D=-43 exact beta-values are carried reviewed controls,
not a new computation in this review. These two notes are respectively a
consequence of the current cyclicity gate and a limit of a proposed
coefficient method. Neither resolves the remaining class obstruction or
the simultaneous-field unit problem.
