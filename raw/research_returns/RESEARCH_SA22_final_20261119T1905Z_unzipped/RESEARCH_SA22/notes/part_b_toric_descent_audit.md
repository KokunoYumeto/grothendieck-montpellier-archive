# Independent hand derivation: raw toric surgery and isotopy

Auditor: GPT-6 Astra (OpenAI), `part_b_cycles`. Date: 19 November 2026, 16:22 UTC. The parent and A567 requested an independent mathematical check of the new third-jet/plumbing proof. The calculations below were performed by hand in reasoning, not by a symbolic or numerical program. **No program was run, no numerical phase was evaluated, no runtime is invented, and no finite certificate is claimed.** No TeX was edited by this reviewer.

The completed fragment `sections/part_a567_toric_descent.tex` has been read in full. Its statements `A1-pant-third-jet`, `A1-four-point-plumbing-jet`, and `A1-toric-nondescent` all pass this review. The fixed-surface conclusion follows from the balanced geodesic comparator, rather than a dimension argument about the larger domain.

## 1. Independent Schwarzian computation and parameter typing

Let the one-boundary, two-cusp pant have boundary length `2*pi*lambda`, and normalize the capped sphere by `(cap centre, ordered cusps)=(0,1,infinity)`. Write `f_lambda:D→Y` for the cap map with `f_lambda'(0)=r(lambda)>0`, and `u_lambda=f_lambda^{-1}`. Thus

`g_lambda(z)=r(lambda)u_lambda(z)`

has derivative one at zero. The geometric toric welding `u_1 u_2=eta` is therefore exactly

`g_1(z)g_2(w)=t`, with `t=r_1 r_2 eta`.

There is no substitution of the unit-disc phase for the normalized plumbing parameter and no omission of the two radius factors.

Put `a=(1+lambda^2)/2`. The hyperbolic developing map continues across the analytic seam as a Möbius transform of `u_lambda^(i lambda)`. Its Schwarzian is single valued and has regular singularities at the three markings. The double-pole coefficients are a at zero and 1/2 at each cusp. On a three-pointed sphere these determine

`T(z)=a/z^2 + 1/(2(z-1)^2) - a/[z(z-1)]`

uniquely: no additional accessory parameter remains after imposing the order-two behavior and cusp coefficient at infinity. In particular

`T(z)=a z^(-2)+a z^(-1)+(a+1/2)+O(z)`.

The chain rule gives `T=a(g'/g)^2+{g,z}`. For

`g=z+b z^2+c z^3+O(z^4)`,

the coefficients in question are

`[z^(-1)]T=2ab`, and `[z^0]T=(4a+6)c-(a+6)b^2`.

Hence `b=1/2` and

`c=(5a+8)/(16a+24)=5/16+1/[16(lambda^2+4)]`.

This independently confirms the fragment's beta(lambda). The same Schwarzian identity is already supported by `A2-schwarzian`; the hand argument above also explains the three singular coefficients and the normalization. Strict monotonicity and `r((0,infinity))=(0,4)` come from the already proved one-active-cap radius theorem and its explicit endpoint, not from this jet calculation.

## 2. Independent general cubic plumbing formula

I checked the more general germs

`g_i(z)=z+b_i z^2+c_i z^3+O(z^4)`

before specializing to `b_1=b_2=1/2`. Let `h_i=g_i^{-1}` and set

`A_i=c_i-b_i^2`, `a=2b_1^2-c_1`.

Then

`h_1(v)=v-b_1 v^2+a v^3+O(v^4)`

and

`1/h_i(v)=v^(-1)+b_i+A_i v+O(v^2)`.

Normalize a meromorphic function F on the plumbed sphere to have its unique simple pole at the first infinity, leading coefficient one in z there, and value zero at the second infinity. On the retained components it has expansions

`F_1=z+B(t)+sum_{n>=1} C_n(t) z^(-n)`,

`F_2=sum_{n>=1} D_n(t) w^(-n)`.

The cross-ratio used in the fragment is `Lambda(t)=F_2(1,t)/F_1(1,t)`.

### Why the expansions and their orders are justified

On the central nodal genus-zero curve, the pole bundle has multidegree `(1,0)`, first cohomology zero, and two global sections. Evaluation at the second infinity and the prescribed principal coefficient at the first infinity are independent normalizations. Cohomology and base change therefore give the unique normalized meromorphic function holomorphically in the plumbing parameter, with central values `F_1=z`, `F_2=0`.

Near the node use `u=g_1(z)`, `v=g_2(w)`, so the total space is `uv=t`. F is holomorphic here and vanishes on the central second component `u=0`; it is divisible by u in the local analytic ring. In a series `sum a_ij u^i v^j` only `i>=1` occurs. At order `t^k` on the first component, substitute `v=t/u`: its pole order in u, hence in z, is at most `k-1`. On the second component substitute `u=t/v`: its pole order is at most k. Thus

`C_n(t)=O(t^(n+1))`, `D_n(t)=O(t^n)`.

This supplies a direct local explanation of the order paragraph in the saved fragment. It does not assume convergence of an arbitrary formal solution; the actual holomorphic family supplies the convergent functions first.

### Principal-part matching

Substitute `z=h_1(t/g_2(w))` in F_1. At order t, the normalized second-component function must be `t/w`. Comparing its expression in `v=g_2(w)` yields

`B_1=b_2`, `C_1(t)=A_2 t^2+O(t^3)`.

At order `t^2`, the only negative principal part before global normalization is `-b_1/g_2(w)^2`. Its negative Laurent part in w is

`-b_1 w^(-2)+2b_1b_2 w^(-1)`.

Comparing the constant term in v also gives

`B_2=b_1(4b_2^2-3c_2)`.

At order `t^3`, the only negative contributions are

`a/g_2(w)^3 + A_1 A_2/g_2(w)`.

The product term arises from `C_1(t)/h_1(t/v)`, specifically the `A_1 t/v` term in the reciprocal inverse germ. Higher C_n contribute only nonnegative powers of v at this order. Therefore

`D_1=t+2b_1b_2 t^2+[a(6b_2^2-3c_2)+A_1A_2]t^3+O(t^4)`,

`D_2=-b_1 t^2-3b_2 a t^3+O(t^4)`,

`D_3=a t^3+O(t^4)`.

For `b_1=b_2=1/2`, these give

`F_1(1,t)=1+t/2+(1/4-c_2/2)t^2+O(t^3)`,

`F_2(1,t)=t+[a(1-3c_2)+A_1A_2]t^3+O(t^4)`.

Division proves

`Lambda(t)=t-t^2/2+[9/16-(5/4)(c_1+c_2)+4c_1c_2]t^3+O(t^4)`.

Substitution of the pant jets cancels all terms linear in `1/(lambda_i^2+4)` and gives the symmetric coefficient

`C(lambda_1,lambda_2)=11/64+1/[64(lambda_1^2+4)(lambda_2^2+4)]`.

Two hand consistency specializations were also checked. If `g_1=z+c z^3` and `g_2=w`, the formula is `Lambda(t)=t-c t^3+O(t^4)`, agreeing with `g_1^{-1}(t)`. If both germs are `z/(1-z/2)`, so `b=1/2,c=1/4`, direct rational plumbing gives `Lambda=t/(1+t/4)^2`, with cubic coefficient `3/16`, exactly the displayed formula. These are algebraic specializations of the hand proof, not computer tests.

## 3. Honest holomorphic families through the phase circle

The cap collar theorem gives an embedded univalent extension whose normalized coordinate image has radius `r(lambda) exp(delta(lambda)/lambda)`, where

`delta(lambda)=arctan(csch(pi lambda))>0`.

The fragment deliberately uses the smaller radius

`a(lambda)=r(lambda) exp(delta(lambda)/(2lambda))>r(lambda)`.

Its closure is strictly inside the available collar, avoids both cusp markings, and is therefore a valid node-coordinate disc. Standard two-disc plumbing exists holomorphically for `|t|<a_1 a_2`. All four external marked sections remain distinct: they are outside the glued coordinate discs. Their normalized cross-ratio is a holomorphic function of t, extends at the central node, and agrees with the actual toric welding at `t=r_1r_2 eta`, `|eta|=1`.

For both pairs in the construction, this provides a common open t-disc strictly containing the complete actual phase circle. The identity theorem is therefore applied at an interior accumulation point, not at a boundary of holomorphy. No uniform remainder estimate at a varying cap radius is needed.

## 4. Exact unequal/balanced pair and unevaluated phase

A567's final no-search radius specification is correct:

`r_1=r(1)`, `r_*=r(1/2)`, `r_2=r_*^2/(4r_1)`, `r_0=r_*/2`, `R=r_0^2=r_1r_2`.

Since `0<r_*<r_1<4`, all radii lie in the permitted range and `r_2<r_0<r_*`. Thus `0<lambda_2<lambda_0<1/2`. With `h(lambda)=1/(lambda^2+4)`,

`h(1)h(lambda_2)<1/20`, while `h(lambda_0)^2>16/289`.

The exact difference is `16/289-1/20=31/5780`, so the cubic coefficient of

`Delta(c)=Lambda_U(Rc)-Lambda_G(Rc)`

is strictly less than `-31 R^3/369920`. In particular Delta is not identically zero. The reference pant lengths are exactly `2*pi` and `pi`; the remaining pants are uniquely defined by their displayed radii.

Because Delta is holomorphic on a disc `|c|<rho` with `rho>1`, it has only finitely many zeros on the unit circle. Hence the exact rule

`N=min{n>=1:Delta(exp(i/n)) != 0}`, `eta_*=exp(i/N)`

defines a finite positive integer and a phase. If no such integer existed, zeros would accumulate at the interior point c=1, contradicting the cubic coefficient. **N is neither numerically evaluated nor claimed computed.** This analytic selection is sufficient to specify the counterexample exactly.

## 5. Deterministic fixed-X isotopy failure

The balanced pair of radii `(r_0,r_0)` welded at eta_* has a geodesic seam and tensor `R eta_*`. The unequal pair `(r_1,r_2)` welded at the same phase has the same tensor, but the inequality `Delta(eta_*) != 0` proves that its underlying labelled four-punctured sphere X is not the balanced sphere X_G.

Take the actual analytic seam C on this **specific unequal X**, and let C_geo be the unique geodesic in its essential isotopy class on X. Both cuts are torically compatible. C caps to the unique ordered three-pointed sphere on each side. So does C_geo, because each component is a two-cusp pant. These identifications have no residual automorphism fixing the three labels.

If C_geo produced tensor `R eta_*`, the already proved unique geodesic reconstruction would identify its welded labelled surface with X_G. But its welded surface is X, whose cross-ratio differs. Therefore C and C_geo on this same fixed X have different tensors. This gives the requested isotopy failure without any dimension count, and without assuming that two fixed-target unequal weldings automatically lie on one fixed surface.

The theorem applies to raw surgery on actual compatible seams. It does not refute the separate functor that first replaces an isotopy class by its unique geodesic. All claims of finite automorphism, marking, and actual circle phase follow the earlier fixed graph conventions.

## Review outcome

All three new statements are approved for integration. The cubic formula, parameter factors, strict gap, collar domain, phase rule, and same-X conclusion have independent hand derivations above. Separate check events are saved in `checks/part_b_toric_descent_events.tsv`. There is no associated computational program or runtime because none was run.
