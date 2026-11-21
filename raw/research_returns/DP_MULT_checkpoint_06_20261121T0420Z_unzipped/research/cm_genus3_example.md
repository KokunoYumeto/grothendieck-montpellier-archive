# DP22 (agent ABA-CM1): an actual one-dimensional CM factor of height three

Agent: `/root/archive_binomial`; model GPT-6 Astra Pro; effort not exposed by the runtime. Date 2026-11-21. This independently checks the root's proposed example. It does not modify the main paper.

## Statement

Let C be the smooth projective curve over Q with affine equation `y^2=x^7-1`, and let J be its Jacobian. Put E=Q(zeta_7). At p=11, over `A=W(F_(11^3))`, J has good reduction and an integral O_E-action. The integral idempotent decomposition of `J[11^infinity]` has two factors of height 3 and respective dimensions 2 and 1. Their Newton slopes are respectively 2/3 and 1/3. In particular the dimension-one factor is connected and yields an actual one-dimensional integral formal subgroup of the completed Jacobian, of height 3.

The normalized derivative along this factor satisfies DP1/DP3 (and also DP19). Its coefficient is `c_3(11)=66/665`, compared with `c_2(11)=11/120`, with exact ratio `144/133`.

## 1. Smooth proper model and genus

Over any ring in which 2 and 7 are invertible, glue the two affine charts

`y^2=x^7-1`,

`v^2=u-u^8`,

by `u=x^(-1)` and `v=y/x^4` on the overlap. The resulting curve is a finite degree-two cover of P^1, hence proper. On the first chart, simultaneous vanishing of the relative partial derivatives `2y` and `7x^6` would force x=y=0, contradicting the equation. The second chart outside u=0 is covered by the first; at u=v=0 its partial derivative in u is a unit. Thus the model is smooth, in particular over Z_11 and over A. The eight branch points are the seven simple seventh roots of unity and infinity; the degree-two Riemann--Hurwitz formula gives genus 3. Infinity is a section. Its relative Jacobian is therefore an abelian scheme over A, giving good reduction of J.

## 2. Integral full CM action and its type

The ring A contains the seventh roots of unity since 7 divides 11^3-1. The automorphism

`sigma(x,y)=(zeta_7 x,y)`

extends to the smooth proper model and fixes infinity. Let sigma_J be the **covariantly induced** Jacobian endomorphism, characterized on divisor classes by `[P-infinity] -> [sigma(P)-infinity]`. This convention fixes possible inverse-label ambiguity.

The basis of regular one-forms

`omega_i=x^(i-1) dx/y`, for i=1,2,3,

has eigenvalues zeta_7^i under pullback by sigma. These forms are regular at infinity: in a uniformizer v, their respective orders are 4,2,0. The Abel--Jacobi pullback identifies them with the regular forms of J and intertwines sigma_J. Consequently Phi_7(sigma_J) has zero differential on the characteristic-zero generic fibre, and hence is the zero endomorphism there. It is therefore zero on the abelian scheme. Since Phi_7 is irreducible and sigma_J is not the identity, its minimal polynomial over Q is Phi_7. This gives an injection

`O_E=Z[zeta_7] -> End_A(J)`.

Here `[E:Q]=6=2 dim J`, so this is a full CM action by the maximal order, which is all that the local construction needs. No assertion identifying every endomorphism of J with O_E is needed. The tangent action has the same eigenvalue multiset as the pullback action on cotangents, so its CM type is `{1,2,3}` with the stated convention.

## 3. The integral local factors

Since 11 is unramified in E and 11=4 modulo 7, the Frobenius orbits of the six embeddings are

`{1,4,2}` and `{3,5,6}`.

Both have length 3, and therefore

`O_E tensor Z_11 = O_(K_3) x O_(K_3)`,

where K_3 is the unramified cubic extension of Q_11. The integral O_E-action on the p-divisible group extends to this completed order. Its two integral idempotents split `J[11^infinity]` as an actual product of p-divisible subgroups over A. This is an integral direct-factor decomposition, not merely an isogeny decomposition.

The characteristic-zero rational Tate module is rank one over `E tensor Q_11`, so each local factor has height 3. Equivalently this is the height count in Tate, exposé 352, Theorem 3, p.107. The two Lie dimensions are the counts of the tangent type in the two orbits: `|{1,2,3} intersect {1,2,4}|=2` and `|{1,2,3} intersect {3,5,6}|=1`. The Lie lattices are integral direct summands, and these ranks persist over A.

## 4. Connectedness and formal subgroup

Tate's local CM formula (10*) and Theorem 3, §5, pp.106--108, give the slope of a local CM factor as its dimension divided by its height. Thus the two factors have slopes 2/3 and 1/3. In particular the dimension-one factor has no slope-zero part and hence no étale quotient. Its special fibre is connected. Over the complete local ring A it is consequently the p-divisible group of a smooth one-dimensional formal group. The idempotent projection realizes this formal group as a direct formal factor of the completion of J along the identity. It has height 3 and an integral embedding into that completion.

One can also check the slope assertion directly on the Dieudonné module after an unramified splitting extension. The unramified cubic order gives three rank-one eigenspaces. Frobenius permutes them cyclically. The sum of the three Frobenius valuations is the dimension (1 for the selected factor), so the third Frobenius iterate has valuation 1 on each line. Thus its slope is 1/3. This is the usual Newton-slope convention in which the multiplicative p-divisible group has slope 1.

The local order acts on the rank-one Lie lattice through one embedding `O_(K_3)->A`, so the strict hypothesis of DP19 also holds. Choosing any generator of this integral Lie lattice gives a normalized tangent direction. The inclusion into Lie(J) is primitive because it is split by an integral idempotent; there is no unrecorded nonunit scalar or isogeny denominator.

## 5. Numerical gain and scope

Direct arithmetic gives

`c_3(11)=1/10-1/1330=66/665`,

`c_2(11)=1/10-1/120=11/120`,

`c_3(11)/c_2(11)=144/133`.

This is an actual higher-height CM example, so failure of the old interface cannot be attributed to nonexistence of a one-dimensional height-three CM factor. The unchanged older interface has an even-length, alternating local-type hypothesis and a height-two one-variable logarithm. The length-three orbits here do not satisfy those hypotheses. An unramified base extension or an isogeny cannot turn Newton slope 1/3 into 1/2. A new global theta construction may have different dimension, period and denominator costs; the example does not calculate those costs and does not establish a shorter global inequality chain.

The root's other agent `/root/step2_higher` independently verified the orbit counts, ratio, and precise older-interface restriction (`LocD.d_even`, `LocD.Alternating`, and the fixed height-two logarithm). Those checks are distinct from this memo's geometric construction and connectedness argument.

## Primary source and check scope

John Tate, *Classes d'isogénie des variétés abéliennes sur un corps fini*, Séminaire Bourbaki, exposé 352 (November 1968), collected pp.95--110: §5, definition p.106, formula (10*) and Theorem 3 p.107, proof through p.108. Primary PDF: https://www.numdam.org/item/SB_1968-1969__11__95_0.pdf . Its local CM decomposition/count and slope formula were inspected in this run. The explicit curve, differentials, orbit counts and numerical ratio are derived above; they are not claims to be quotations from Tate.

The exact primary inputs are now supplied and checked in `cm_genus3_primary_inputs.md`: Grothendieck FGA V, Theorem 3.1, pp.148--149; FGA VI, Corollaries 1.7 and 2.3 and Proposition 2.10(ii), pp.229,232,236, for the relative Jacobian; and Tate, *p-Divisible Groups*, section 2.2 Proposition 1, p.162, and section 2.3 Examples b), p.166, for the connected-formal correspondence and the identification with the completion. The application verifies their hypotheses. This is not an independent reproof of those general theorems or of Tate's local CM theorem.

Whole-proof self-reading completed at 2026-11-21 00:29:50 UTC. The explicit curve, endomorphism action, local factors, connectedness and ratio were all included. Event ABA-CE17 records that scope. Tate's printed p.107, including (10*) and Theorem 3, was inspected in the primary PDF. The older-interface observations also have the separately attributed check by `/root/step2_higher`.
