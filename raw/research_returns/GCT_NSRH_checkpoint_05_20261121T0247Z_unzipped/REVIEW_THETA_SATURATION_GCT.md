# Independent full check of the theta/interlacing saturation note

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; inherited effort not exposed. Date: 2026-11-21 Europe/Berlin. Reviewed `GCT_NSRH_work/agent_theta_saturation.md` in full, then read the relevant attached IV and VI source contexts directly. This is a targeted full-proof/source-applicability check, not proof-assistant verification.

## Outcome

**PASS.** The homogeneous integral difference-constraint proposition, the exact small Kronecker obstruction, the full parity-ray deduction from IV equation (172), the rational Ehrhart model, and the distinction from VI's definition of strict saturation are all correct with the displayed scope restrictions. No blocker or mathematical correction was found.

## 1. Difference constraints

The identity `P(Nu)=N P(u)` follows because the constraint list and dimension are fixed and every endpoint function is homogeneous on the admissible lattice. For any real feasible vector, coordinatewise flooring preserves every inequality `x_i−x_j≤b` with integral b, including negative coordinates and inequalities involving x_0=0. Thus feasibility implies integral feasibility. Dividing an integral point at Nu by N and flooring gives a point at u; multiplying a point at u by N gives the converse. Boundedness is needed only to regard the cardinality as finite.

The argument also proves the stated fixed finite-sum extension. The restrictions excluding extra congruences, general sum constraints, nonintegral endpoints, changing lattices and nonhomogeneous maps are necessary to the claimed scope. The note does not assert that arbitrary GGP or theta data satisfy them.

## 2. Independent exact character check

At d=1, the three sign characters of S2 tensor to sign, so the invariant multiplicity is zero.

For S4, the three-pairing permutation representation minus its invariant line has character `(2,0,2,−1,0)` on the listed cycle types. Using class sizes `(1,6,3,8,6)`, its squared norm is `(4+12+8)/24=1`, so it is irreducible and is the two-dimensional Specht module of shape (2,2). Its pointwise square equals the sum of itself, trivial and sign. Equivalently its third moment is `(8+24−8)/24=1`. Thus g((2,2),(2,2),(2,2))=1. The stated pair of examples genuinely contradicts support saturation under rowwise scaling on the specified label lattice.

## 3. Direct source substitution in IV (172)

I read the attached source's column-count definition in §2.3, the invariant-removal equations (163)–(164), Theorem 18.2 and its adjacent proof, and the full discussion containing equations (172) onward in §18.3. The author checked the numbered primary PDF; this review independently checked the actual LaTeX formulas and their conventions.

The source writes the rectangle `(d,d)` as `[d,0]` when treated as a two-row weight and `[0,0,d,0]` when treated as a four-row output label. Its generating function is `g_[d,0],nu(x)=sum_mu g_[d,0],mu,nu x^(m_1)`. Hence the constant term of its displayed formula for `g_[d,0],nu(x^(1/2))` picks exactly m_1=0, which forces mu=(d,d) because the total size is 2d.

In equation (172), the constant term has k=0. The first inner sum has only j=0; the second sum starts at j=1 and is empty. The surviving indicator is exactly that n_3,n_2,n_1 are even and nonnegative. Substituting n_3=n_1=n_4=0 and n_2=d gives

\[
g((d,d),(d,d),(d,d))=1\quad\text{for even }d,
\qquad =0\quad\text{for odd }d.
\]

There is no hidden contribution from n_4 or from another k. The alternative invariant-removal check is consistent: the source's equation `e BWZ condition` has only type 0 available when n_1=n_3=0, and m_1=0 forces the remaining height-two column count to be zero, hence i_2=d/2. This retains precisely the parity datum described in the note.

I did not independently re-prove the entire two-row crystal theorem. The existing formula is the cited source input; the specialization to this ray is independently checked in full.

## 4. Ehrhart and VI saturation conventions

The rational point P={1/2} satisfies `#(dP∩Z)=1` exactly for even d, giving the claimed exact ray model. Its dimension is zero and its denominator is two. This does not meet the integral-endpoint premise of the difference-constraint obstruction, so there is no contradiction.

I read VI's source definition `dintrosat` directly, including its preceding residue-polynomial convention. Strict saturation there requires positivity of every non-identically-zero residue polynomial at all positive arguments, while permitting identically zero residue polynomials. For this ray the residue polynomials are 1 and 0, so the VI saturation index is indeed zero. The note correctly avoids calling this a counterexample to that definition.

## 5. Representation/K0 translation

The tensor map GL2×GL2→GL4 is defined integrally, and characteristic-zero restriction is an exact tensor functor inducing a positive representation-ring map. The coefficient of det_V^d⊗det_W^d in the restriction of S_(d,d)(V⊗W) is the same Kronecker coefficient by the usual Schur restriction decomposition. At d=1 the displayed exterior-square identity has no det_V⊗det_W constituent, which independently matches the zero. An effective K0 map does not imply homogeneous support saturation, and highest-weight scaling is not supplied by such an exact functor. These scope statements are correct.

## Check event

`THETA-SATURATION-INDEPENDENT`: complete targeted proof check of the note; independent S2/S4 character computation; direct applicability check and constant-term specialization of IV (172); direct VI saturation-definition check. Outcome PASS. No numerical approximation, new computer algebra, or formal proof assistant was used.
