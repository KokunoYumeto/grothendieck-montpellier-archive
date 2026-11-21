# DP40: independent combined review of cyclic displays and the Fourier comparison

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Complete review interval **02:19:25–02:21:48 UTC**. Events **ABA-CE39** and **ABA-CE40**. No main-paper edits.

## Outcome

**PASS for both complete memos identified below.** I read every statement, proof and scope qualification in the cyclic-display model memo and the cyclic-type sum memo, independently checked their algebra and their common interface, and confirmed that the final files have the same hashes as the fully read versions. The model theorem realizes the directional quantities as sharp slopes for actual dual cyclic displays, including arbitrary Witt-unit arrow coefficients. The Fourier theorem bounds their total over the type together with its dual by \(h c_2\), with equality precisely for even alternating type.

No mathematical correction was required in these versions. The CM application is conditional on the explicit integral eigenspace and Hodge-filtration normal form. The result concerns an equally weighted local directional sum; it is neither a componentwise bound nor a theorem identifying that sum with a global theta cost.

## 1. Integral display and actual dual

The normal-decomposition linearization is a monomial matrix with unit entries, so it is invertible. The defining semilinear relations on L and IT are consistent. A full cycle contains exactly \(h-m\) explicit p factors, while the dual cycle contains m. Because both numbers are positive, their repeated cycles meet the required nilpotence conditions at every fixed base/Witt truncation. Passing through the compatible reductions therefore supplies the intended connected formal p-divisible groups.

I directly read **Zink Theorem 5, printed p. 131**: it gives height equal to the Witt-module rank. The tangent-space identification with \(P/Q\) is in the preceding exponential paragraph and is also the later Theorem 81/(155) identification. Thus height h and dimension m are justified by exact cited statements.

For the dual basis, the proposed matrix has the same cyclic permutation and coefficient \(u_i^{-1}p^{1-\epsilon_i}\). I checked that this gives

\[
\langle Fe_i,F'e_j^*\rangle=p\delta_{ij}
\]

and the other normal-decomposition pairing identities. The selected and unselected submodules exchange. I reread **Definition 19 and (22), printed p. 143**, and **Theorem 122, printed p. 247**, including its p-nilpotent-base and nilpotent-nilradical hypotheses. The bases \(W(k)/p^n\) meet those hypotheses, and both display nilpotence conditions hold here. The cited duality identifies the complementary reciprocal-unit model with the actual Cartier dual, rather than merely with a group of complementary slope.

## 2. Arbitrary Witt units and the full logarithm

For a Witt unit \(u_i\), every ordinary ghost \(w_n(u_i)\) is a unit in R. This follows already because the ghost is a unital ring homomorphism; the memo's reduction modulo p is a valid additional verification in the stated local ring.

The divided-ghost operator is correctly indexed:

\[
(d z)_n=B_nz_{n+1}-z_n.
\]

Its logarithmic projection uses the prefix product \(B_0B_1\cdots B_{n-1}\), in that order. Substituting d into this prefix sum telescopes. The unit entries vary with the ghost index, but each product still follows a unique cyclic path. Each complete cycle contributes exactly \(h-m\) powers of p, giving convergence in the completed quotient by the same uniformly bounded divided-ghost argument established in DP41.

A path between successive selected positions has exactly one selected starting arrow and \(g_j-1\) unselected arrows. Its ghost denominator is \(p^{g_j}\), leaving one denominator p. A path through k selected gaps therefore has coefficient \(\eta_{j,k}/p^k\) with \(\eta_{j,k}\) a unit. For a fixed starting coordinate, output and ordinary degree, the path is unique, so this exact coefficient cannot cancel with another path.

When all arrows equal one, these path contributions are exactly the iterates in (CD6). With general units the memo correctly retains only the exact unit valuation; it does not incorrectly replace the logarithm by iterates of a fixed monomial map in characteristic zero.

## 3. Contraction and the sharp inverse witness

The weights are positive and less than \(s=1/(p-1)\). I checked the cyclic wrap in

\[
p^{g_j}r_{\mathrm{prev}(j)}-r_j=1.
\]

Exactly the selected endpoint j wraps from exponent \(h-g_j\) to h; every other selected term stays in the corresponding non-wrapping arc. The argument includes the singleton type, whose gap is h.

The first selected-gap coefficient becomes a unit after scaling. For k gaps, iterating this identity in the correct backward order gives

\[
1+p^{g_1}+p^{g_1+g_2}+\cdots+p^{g_1+\cdots+g_{k-1}}-k.
\]

It is strictly positive for every \(k\ge2\), including p=2. Thus the reduced contracted logarithm is exactly \(\operatorname{Id}+M_\eta\), with all indicated coefficients nonzero.

The map \(M_\eta\) is additive in residue characteristic p, even though its coefficients need not be Frobenius-fixed. The formal geometric inverse \(\sum(-1)^k M_\eta^{\circ k}\) is valid for that additive map; its increasing degree makes every fixed coefficient a finite sum. Returning from a selected coordinate to itself requires a multiple of m selected arrows. After mr arrows the degree is exactly \(q^r\), with coefficient a product of nonzero residue units and their Frobenius powers. No other iterate contributes to that same coefficient after all other input coordinates are set to zero. This proves the exact inverse coefficient valuation (CD14), for arbitrary unit arrows and every prime.

The translation argument correctly extends the factorial derivative bound from evaluation at zero to every coefficient of an integral function. Legendre's formula and \(s_p(q^r)=1\) give the exact sharp sequence (CD5). The right-hand valuation is indeed integral, since \(q^r-1\) is divisible by \(q-1\). The reciprocal-unit dual gives the complementary slopes, exactly matching the orientation in (CM1).

## 4. CM normal-form interface

The concluding CM statement is a sufficient interface, not an unproved classification assertion. It assumes the integral action, free rank-one eigenspaces, the cyclic semilinear permutation, and the componentwise Hodge filtration \(Q_i=IP_i\) or \(P_i\). Under those hypotheses, commutation forces the arrows into the next eigenspace, and invertibility of the normal-decomposition matrix forces their coefficients to be units. This gives (CD1) directly.

A geometric application must supply that integral data over the stated unramified base/coefficient extension. A decomposition only on the special fibre, or the height of an arbitrary deformation, does not supply this normal form. The memo expressly preserves that gate. It also does not require a global CM realization for every abstract binary type in order to prove the local model theorem or the universal combinatorial bound.

## 5. Fourier factors, gap, and equality

I independently checked the oriented crossing count. At displacement k there are exactly \(N_k\) unequal-type pairs. Each side of the type/dual partition contributes \(N_k/2\), because the two translated sets have equal cardinality. Therefore the total and half-total formulas contain the correct factors of two.

At the discrete hth-root frequencies, the finite geometric sum is

\[
\rho_h\sum_{k=1}^{h-1}p^kz^k=\frac1{pz-1}-\rho_h.
\]

The memo correctly restricts this identity to \(z^h=1\). Taking real parts gives the symmetric circulant eigenvalues. The stated derivative of their rational function of \(\cos\theta\) is positive, so their common lower bound is \(-1/(p+1)-\rho_h\), attained only at the alternating frequency. Parseval is normalized with total squared norm h, yielding exactly \(S_h\le h c_2\).

Equality forces every nonzero Fourier coefficient into the single alternating frequency; the binary values then force precisely the two alternating types. Conversely the alternating crossing count attains the bound. Odd h has no such frequency. This also handles h=1 and h=2 without adding an exceptional equality case.

Subtracting the minimum eigenvalue gives the factor in (CM9):

\[
\lambda_m-\lambda_*=
\frac{p(p-1)(1+\cos\theta_m)}{(p+1)(p^2-2p\cos\theta_m+1)}.
\]

The extra factor one-half in the gap follows from (CM5). Retaining the zeroth Fourier mode exactly gives the cardinality refinement \(4r(h-r)c_2/h\). Its only equality types are the constant types and the even alternating types. The proofs are valid for every real p>1 in the combinatorial statement; primality is required only in the formal-group application.

## 6. Height-six arithmetic and geometric scope

I recomputed all five crossing counts \((2,4,6,4,2)\), all six directional numbers, their factorization, the stated gap and ratio, and both numerical rows at p=3 and p=5. The last-direction excess is exactly

\[
\gamma_2-c_2=\frac{p}{p^3+1}>0.
\]

This confirms that the theorem cannot be interpreted componentwise. I also checked the two displayed Frobenius orbit orders modulo seven and their conjugation shift; they give the three-consecutive-selected word from the previously established CM type.

The full pair has h directions, so its equal-direction mean is at most \(c_2\). Each type's partial sum is half the total, but its number of directions can differ from its dual's. Thus the mean on an individual unbalanced type is not automatically bounded by the pair mean. Neither the model proof nor the Fourier proof identifies these sums with a theta main term, a weighted selected-operator cost, or a global lift count.

I did not rerun or claim authorship of the author's finite enumeration. The complete mathematical proof and the displayed small examples were independently checked manually.

## Exact checked files

| File and scope | SHA-256 |
|---|---|
| Complete cyclic-display model memo | `f4f5ac66f21eb2209657d937583d10932a1d6b249c58003808b90a9aef117cf6` |
| Model statements and complete proofs, §§1–6 | `385e33c39759ad683b2ea1178b87d18df2560a65fa88ab06ea5a11854a919451` |
| Complete cyclic-type/Fourier memo | `2dac0940b1859ca0f278f7727efe5e8172752cccc946dfad35d979c81ce4cae0` |
| Fourier statements, complete proofs and examples, §§1–5 | `d9f3335b645ba70224cbc3c759e0813a33e8df7435c01848d6c4204ab5c9700b` |

The snapshots are `late_proof_snapshots/DP40_models_complete_checked.md` and `DP40_fourier_complete_checked.md`, with exact scope metadata in `DP40_combined_check_metadata.json`. Final hashes equal those captured on the initial complete reads. These checks certify these memo versions, not a later integrated main-paper block or a machine formalization.
