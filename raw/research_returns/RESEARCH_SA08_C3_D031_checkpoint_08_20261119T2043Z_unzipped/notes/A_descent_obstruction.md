# AT11–AT12: prescribed truncation completion obstruction

The complete proofs are in `sections/A_descent_obstruction.tex`.

AT11 constructs, for every length L, a locally finite graded free resolution of the ideal J=(p,I_1) in Γ_R(T). After reduction modulo p every free term is graded injective, because its generators have nonnegative locally finite weights and therefore its direct sum decomposition is also its graded product decomposition. The explicit p-power coefficient calculation proves that the inclusion of every tail I_M into J/pJ has no lift through the first free term. Dimension shifting makes the pullback length-L extension nonzero for every M. The top-cycle nullhomotopy must consequently have a nonzero last-syzygy component.

AT12 realizes L=2p−1 as the top arity of a truncated odd vertical disk. The bottom syzygy is in form zero; all new modules annihilate the old positive arity part. This gives a strict PD algebra with exactly one extra cohomology class, F_p in form 2p and weight p(p+1). It is constructed over Z[1/(p−1)!], so the lower arities contract. Orthogonal assembly over all odd primes gives a single integral flat algebra. Fiber products indexed by monotone triples give an admissible simplicial target A with explicit G→A→G.

The normalized triple indicator ε012 is a closed element in simplex degree two. Sending the top of a C21 D(2) parameter to x_p ε012 and its bottom to zero is a legitimate choice for the zero-cycle attachment in form one. All form-zero maps are chosen through G. This constructs an actual C21 partial model P→A,G with P_0=S.

An admissible local completion with the prescribed truncation in forms zero and one would make γ_p(d x_p) derived-nullhomotopic on a free resolution of a sufficiently delayed coefficient tail. The local coefficient module has the explicit length-one injective resolution (AT.45), so the relevant positive derived Hom group is zero. Composing the nullhomotopy with the displayed coordinate projection and a vertex map on the G factor makes its bottom component zero, because the entire prescribed form-zero image lies in S. AT11 proves that component must be nonzero. This excludes every depth at least two for the prescribed diagram at every odd prime.

The actual maps G→A→G demonstrate the precise scope. These results disprove universal completion of arbitrary prescribed C21 diagrams. They do not disprove the existence of a more suitable partial model or the integral common-source theorem.

Primary-source input: Nagpal–Snowden, *The module theory of divided power algebras*, arXiv:1606.03431v2, Theorem 7.1(a), printed p.39, proof p.41. The PDF and LaTeX source were fetched and opened in `sources/A_integral_Nagpal_Snowden/`; bibliography key `IC-nagpal-snowden`. The complete-base argument used for AT06 was independently proved earlier from that theorem.

Finite checks are in `code/A_integral_descent_check.py` and `logs/A_integral_descent_check.json`. Independent referee and a separate finite analogue certificate are supplied by lifting_audit in its scoped files. These checks supplement the written infinite-module proof.
