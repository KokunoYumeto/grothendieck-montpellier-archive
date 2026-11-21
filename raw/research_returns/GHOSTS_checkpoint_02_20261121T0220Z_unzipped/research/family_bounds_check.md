# Independent check of R10--R11 and the family extension R13

GHOSTS-20261121. Checker: GPT-6 Astra Pro, inherited effort not separately exposed, `/root/bounded_specialization`. Date: 2026-11-21. The complete root draft `root_family_bound.md` through R11 was read. The conclusions below are ordinary mathematical proof checks, not formal verification.

## Verdict

R10 and R11 pass with their stated principal-polarization, integral O_K-action, and nonzero effective surface hypotheses. R13 is proved in `sections/family_uniform.tex`, with finite type over C expressly required for the countable-union step. Its explicit and non-effective conclusions are separated. No approval of R12's proposed numerical D0 follows merely from this check.

## R10: projector, integral cycle and lattice checks

On wedge^a V_sigma tensor wedge^(4-a) V_barsigma, R=[omega]^* has eigenvalue omega^(2-a), and S=[sqrt(-3)]^* has eigenvalue 9(-1)^a. Thus (9+S)(2-R-R²) is54 for a0,4 and zero for the other weights. The Rosati-compatible flat metric makes R unitary; S/9 is a self-adjoint involution on H⁴, because S²=[-3]^*=81 and adjoint S equals [-sqrt(-3)]^*=S in even degree4. The two spectral projectors commute. Their product is the orthogonal projector e_W.

Expanding the numerator gives 18Z+2S*Z on the positive side and 9R*Z+9R²*Z+SR*Z+SR²*Z on the negative. Unit maps preserve theta, and S multiplies a codimension-two pullback degree by9. Both effective degrees are at most36D0. Isogenies are finite flat, so their pullbacks are effective integral cycles with the correct multiplicities. Consequently u=54e_W[Z] is integral and nonzero.

The Weil plane is primitive: after splitting K, theta has character content (1,1), and theta wedge wedge⁴V_sigma=0 since dim V_sigma=4; similarly for the conjugate. It has Hodge type(2,2), so the middle Hodge star is +1 there and its intersection form is positive definite. R is an isometry with 1+R+R²=0 on W. Hence Gram(u,Ru)=[[d,-d/2],[-d/2,d]], where d=u²>0. This d is even: in the integral middle exterior lattice wedge⁴Z⁸, a basis monomial wedges with itself to zero, and the cross terms of a self-pairing occur twice. The two vectors are a rational basis since R has no rational eigenvalue.

## R11: mass estimate and constants

For a principal polarization, theta⁴/4!=1. Choose the corresponding translation-invariant flat Kahler metric. Harmonic forms are translation invariant, so a harmonic4-form of L² norm1 has pointwise exterior norm1. Its comass is at most that norm. Integration over an effective complex surface, including its multiplicities and ignoring the measure-zero singular locus, is therefore bounded by its calibrated volume, theta²[Z]/2. Applying this to the Hodge star of every unit harmonic form shows ||[Z]||<=D0/2.

Orthogonal projection gives d=||54e_W[Z]||²<=54²D0²/4=729D0²=M. There is no omitted factor4! or2!; the ambient volume is1 and the surface volume is D0/2. This is the main normalization check.

Let delta t be integral, T=t²>0, p=(delta t,u), q=(delta t,Ru). They are integers. With Delta=3d²/4, Cramer's rule gives Delta delta t=a u+b Ru, a=dp+(d/2)q, b=(d/2)p+dq. Evenness of d makes a,b,Delta integers. Positive-definite Cauchy--Schwarz gives |p|,|q|<=delta sqrt(Td), hence |a|+|b|<=3delta sqrt(T)d^(3/2).

The effective numerator degree is at most36D0(|a|+|b|), which is <=108delta D0 sqrt(T)M^(3/2). The multiplier is N=delta Delta<=delta M². Since729²=531441 and108*729^(3/2)=2125764=4*531441, both are bounded by the stated integer C=531441delta D0⁴(1+4ceil(sqrt(T))). The bound is conservative but correct. It is a sufficient certificate and has no minimality claim.

## R13: precise family result

The full proofs are in `sections/family_uniform.tex`.

1. For an Eisenstein integral action, H¹_Z is a torsion-free rank4 O_K module and thus free. Monodromy lies in GL4(O_K). On W=wedge⁴_KH¹ it is determinant_K, hence belongs to O_K^×=mu6. The kernel gives a connected finite etale cover of degree at most6. This sharpens the positive-definite-lattice proof of finite monodromy.
2. A flat rational section has one constant denominator-clearing integer delta and constant norm T because integral parallel transport and cup product are preserved.
3. B01 works over a finite-type complex base. Relative cycle classes are locally constant on each connected component of the proper bounded parameter scheme. Algebraic and analytic connected components agree. Therefore S_C is Zariski closed.
4. If the same explicit C works on a Zariski-dense subset, closedness extends exactly that C to the whole base. The analogous conclusion from a numerator degree bound alone uses B06.
5. If every complex fiber is rationally algebraic, the nested closed sets S_C cover all complex points. On each irreducible component, a closed ball in the smooth analytic locus is a Baire space and cannot be covered by countably many proper algebraic subsets. Thus one S_C is the entire component; finitely many components give one uniform maximum. This supplies no numerical C and requires finite type over an uncountable field (here C), rather than noetherianity alone.
6. The non-effective assertion applies independently of R12 whenever a correctly scoped known algebraicity theorem applies at every point. The explicit R10--R11 bound extends only after the numerical degree D0 and its dense locus are proved.

## Source locators read

SGA1, Expose XII, Theorem5.1, original p.333, recomposed p.251, exact equivalence between finite etale covers of a locally finite-type C-scheme and its analytification; XII, Proposition2.4, original p.318, recomposed p.243, equivalence of algebraic and analytic connectedness/irreducibility. Primary re-edition: https://arxiv.org/pdf/math/0206203 . Web refs `turn213481465view0` and `turn213481465view1`. Statements and their immediately displayed proof openings were read. The full Riemann-existence proof is background.

## Check events

statement_id	date	who_model_effort_run	type	outcome	method_or_locator
R10	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Projector eigenweights and orthogonality, both degree36D0 bounds, primitiveness, Gram matrix, and even integral self-pairing rederived; no fault found	root_family_bound.md R10; this memo
R11	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Mass/comass and factorial normalization checked; Cramer integrality and all numerical constants rederived; no fault found	root_family_bound.md R11; this memo
R13a	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Monodromy det_K lies in mu6, finite etale cover degree<=6, integral denominator and cup-product norm constant	sections/family_uniform.tex
R13b-R13c	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Closed bounded loci and Baire argument proved for finite-type C base; explicit versus non-effective conclusion separated	sections/family_uniform.tex
SGA1-XII-T5.1-P2.4	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	used and rechecked in this run	Exact primary re-edition statements read; finite-cover algebraization and analytic/algebraic connectedness apply; full source proofs background	arXiv math/0206203, original pp318,333
