# R34 author whole-proof check

Date: 2026-11-21T06:39:59.249276+00:00
Author: /root/rectangular_bridge; GPT-6 Astra Pro; effort inherited/not exposed.
Final standalone SHA256: `26d4b2597f4a13b3c776caf4be08ffba50f94940983124d481a939efd4d8575e`
Root-reviewed mathematical fragment: `0dc6c1d850e692dae351e6b991d7c9fa17b2abea02d2bcb225868700521b2b01`.

PASS after complete statement, six-part proof, quantitative construction and scope reread/rederivation. The final change explicitly restricts the last all-integer occurrence sentence to no-scaling cases, matching the unchanged main theorem. No new finite computation is claimed.

1. The clock-shift commutation and monomial conjugation preserve both determinant and permanent exactly. The finite characters are distinct for every modulus, including composite/even moduli. Every pure-power coefficient is nonzero, and monomial support has zero label sum.
2. Every possible source of the infinitesimal coefficient x_s^(m-1)x_t is accounted for: a pure power, an absent almost-pure monomial, or x_s^(m-2)x_t x_u. The last source requires2s=t+u, including u=t. Strong progression-freeness excludes all of them, forcing every off-diagonal Lie entry zero; the pure powers force one scalar.
3. The Fermat triple has precisely the two perfect matchings, with the written determinant cycle sign and product(x+zeta^i z)=x^m-(-z)^m. Eisenstein at a simple linear factor proves irreducibility, which lifts to the full homogeneous polynomial under specialization.
4. Finite diagonal unitary symmetry forces diagonal full moments even after positive diagonal rescaling. The log-norm Hessian is a covariance; pure exponents make it positive on the zero-sum hyperplane. The explicit max-coordinate bound is coercive for every strictly positive mu. The constrained zero gradient gives the full moment because both coordinate sums equal m.
5. The two witnesses are separate. Ordered padding has exactly the central full moment; finite q stabilizer gives stable ordered tensors and every-1PS minimum transfers stability through multiplication. Fixed irreducible q plus a generic stable padding line gives a projectively free padded form even at a1. The central exponent is divisible by r. For unpadded forms, all directions have stable points but only nonrectangles use the generic auxiliary flag to remove periods.
6. The base-three digit set has no carries and lies in[0,(m-1)/2], so modular equality is integer equality and includes repeated endpoints. Its Cartesian square has the exact stated size and retained Fermat triple. The power bounds, m27 example and uniform2187 threshold are correct.

This proof imports no additive-combinatorial density theorem or unproved moment-polytope theorem. The only external invariant-theory inputs retain their previously checked exact locators.
