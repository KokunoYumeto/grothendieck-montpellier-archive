# A070 — both central zero-twist walls: full proof and independent certificates

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read G033, `work/root/all_order_zero_twist_report.md`, ZW.1–ZW.10 and all six sections, then reread the added stable-first-row and second-central-wall paragraphs. I also read the complete two cone constructors, their saved certificates, the residue-check implementation, and the unified evaluator including its partition wrapper. **PASS.**

The final cone A used throughout this audit is \(k=T+6+K\), not the superseded earlier parameter map. Both cones were reconstructed directly from full normal-subset traces; no affine transformation of an existing phase table was used as the independent calculation.

## 1. The actual module and the two cones

For cone A the displayed partition gap is \(X+K\); for cone B it is \(K\). Both maps have \(t<k\) and \(b>2(k-1)\). Hence all their parameters satisfy the exact degree hypothesis of the restriction complex and the rank-two pair comparison. FA.5 gives \(\alpha=(b+x,b)\), order \(k\), and sign \(\operatorname{sgn}^{d+b+x}\), exactly as in ZW.3.

The singleton straightening proof from A068 requires only nonnegative complete-function arguments, which follow here from \(b\ge k-1\). The pair comparison requires \(b\ge2(k-1)\), also satisfied. Consequently the ambient/singleton/pair phase polynomial remains the same literal trace expression after the displayed affine substitutions, even where its old chamber coordinate is negative. This conclusion follows from the underlying finite formulas and maps, rather than from extrapolation of an unproved representation identity.

The terms with four or more selected ideals vanish in the required high degree. The three-subset term is retained with its actual orientation.

## 2. Exact triple telescoping, high-tail reversal, and sign

Let \(M=3(k-1)\). When the normal first part \(p\ge b>2(k-1)\), the total-degree bound \(p+q\le M\) forces \(q<b\) and \(q<p\). Thus the extension of the \(q\)-sum used in ZW.4 introduces only zero coefficients and preserves every skew horizontal-strip condition.

With \(R_\eta(z)=P_\eta(\epsilon z,\epsilon)\), its \(z^p\) coefficient is \(\sum_qp_{p,q}\epsilon^{p+q}\). In the second Schur coefficient, the substitution \((p,q)\mapsto(p+1,q-1)\) preserves \(p+q\). It cancels each interior column of the sum, leaving exactly the columns \(b\) and \(a+1\). This proves ZW.4 with its stated exterior-line character.

For one selected cycle, write the exponent of its first variable as \(k-1-r\). The reversed factor is
\[
\epsilon^{\ell(k-1)}
\sum_{r=0}^{k-1}\sum_{j=0}^r
\epsilon^{\ell(j-r)}z^{\ell r}.
\]
Through deficit \(h<k\), the restriction \(r<k\) is automatic. Setting \(r=j+l\) produces the two geometric factors in ZW.5 because \(\epsilon^{-\ell}=\epsilon^\ell\). Multiplication over cycles yields the phase \(\epsilon^M\).

The two deficits are \(t\) and \(t-x-1\). Both cones satisfy the necessary \(t<k\); a negative second deficit means that the original coefficient lies beyond the highest possible normal degree and is zero. In cone A this second argument is \(-X-1\); in cone B it is \(S\). Finally
\[
a+b+M\equiv x+k-1\pmod2,
\]
which gives exactly ZW.6. Complex degree times subset orientation gives \((-1)^{\#\operatorname{cyc}(\eta)}\). This checks every factor in the actual triple contribution.

The generating functions have at most six denominator factors and are proper. Their roots have periods dividing the full permutation's period. For \(\epsilon=-1\), the complementary transposition contributes the required factor two to that period. The fixed phase interpolation from index zero is therefore exact. The draft's wording “six denominator factors” was corrected to “at most six”; I reread the saved correction.

## 3. Independent reconstruction of the final phase polynomials

The independent script is `check_zero_wall_cones_independent.py`. For each cone and every cycle phase, it evaluates the complete normal-subset expression with unexpanded truncated rank-two monomials and the two literal Weyl coefficient shifts. This includes the triple terms directly; it does not import either root constructor or theta's phase evaluator.

The safe phase-degree bounds proved in A068 are still valid after the affine parameter maps. The additional triple sequences have degree at most five on the identity class, three on the transposition class, two on class \(221\), one on class \(311\), and zero on class \(32\); the other two classes have no stable triple. Thus the independent safe bounds are
\[
(5,3,3,2,0,2,0).
\]
The same binomial-basis unisolvent reconstruction therefore proves each full rational polynomial from its literal trace values.

All **898 phase polynomials**, reconstructed from **3,254** exact simplex traces, agree coefficient by coefficient with the final saved data. Their actual degrees are \((5,3,2,1,0,0,0)\), and their separate degree bounds are exactly within the stated \((3,3,4)\) and \((3,2,4)\).

I independently recomputed mixed differences by repeated step-sixty translations and rebuilt every coefficientwise phase maximum. All **46** margins in cone A and **33** in cone B match, with minimum constant margins **131,670** and **8,700**, respectively. All their coefficients are nonnegative. The identity coefficients are nonnegative, every omitted order vanishes, and every first-order margin is strictly positive.

The independently reconstructed polynomials are saved as `ZERO_WALL_CONE_A_POLYNOMIALS_INDEPENDENT.json` and `ZERO_WALL_CONE_B_POLYNOMIALS_INDEPENDENT.json`.

## 4. Both complete residue cubes and positive polytopes

Using these independently reconstructed polynomials, I evaluated both complete sixty-cubed residue domains with Python unbounded integers for polynomial products and character sums. All **3,024,000** constants agree with the supplied receipts. Every label-array hash, minimum, maximum, and zero set matches. Cone A has exactly **five** effective-label zero entries and cone B exactly **six**, at the parameters printed in §4.

The residue-cube calculation is independent of the source's int64 bound. I also checked that the source's static absolute monomial bounds dominate every prefix multiplication: its coordinate powers are bounded by powers of fifty-nine, so no zero-factor issue like the earlier G032 detail arises here.

The common Hermitian character bound and the exact positive margin imply all nonzero Newton differences are positive, uniformly in the nonnegative cone coordinates. Order-zero values are actual representation multiplicities. Hence the fixed Newton constants are nonnegative integers. Their subset-chain interpretation gives respectively 47 and 34 disjoint tags, with at most three quotient variables, one selector, and five chain variables. The total nine-variable bound is correct.

The exhaustive receipt, including both polynomial input hashes, is `ZERO_WALL_CONES_INDEPENDENT_RECEIPT.json`.

## 5. Exhaustion by the exact complementary and stable maps

For the complement, direct substitution gives
\[
\lambda^c=(3b+2x-5k,\ 3b+x-5k,\ 2b+x-5k,\ 2b+x-5k,\ 0).
\]
Its parameters are exactly those in ZW.10 when \(b\ge k\). When \(b<k\), the reported zero-order model has the same four tail parts and a first part smaller by \(5(k-b)\). Multiplication by \(u^{k-b}\) restores the original complementary component and preserves its \(S_5\)-action. The outer label is changed only by the stated determinant character \(\operatorname{sgn}^H\).

For \(k\le b\le2k\), the new twist is at least twice the new order. At \(b=2k+s\), \(s=1,2,3\), it is precisely \(2k'-s\). The validity inequality for the mapped boundary family reduces to the original \(x\ge0\), so no low-endpoint case is lost.

Outside the complementary range, \(b\ge2k+4\). Either \(b\ge3k-2\), giving T054, or \(t=3k-3-b\) satisfies \(0\le t\le k-7\). For \(x\ge t\), the inverse A parameters are \((x-t,t,k-t-6)\), all nonnegative. For \(x<t\), the inverse B parameters are \((x,t-x-1,2b+x-5k)\), all nonnegative. Substitution recovers \(x,b,k\) exactly. This proves the complete integer-domain exhaustion.

For a wall partition with \(\lambda_2=\lambda_3\) and \(n>\lambda_2\), the added stable paragraph correctly sets \(e=n-\lambda_2\). Its reduced first-row gap is \(2\lambda_2-\lambda_4-\lambda_5\ge0\), so it remains a partition. The actual chart multiplication by \(u^e\) restores the original module without a label twist. The resulting \(d,x,b,k\) satisfy ZW.1 exactly.

For the other central wall \(\lambda_3=\lambda_4\), complementary columns give \(\lambda^c_2=\lambda^c_3\), and the perfect pairing carries precisely the sign \(\operatorname{sgn}^{\lambda_1}\). This proves the full two-wall extension in the revised draft.

The partition wrapper implements these same maps, including empty partitions, determinant rectangles, and the vanishing above five rows from the actual tensor-power/Pieri inclusion.

## 6. Independent unified-evaluator checks

The script `check_zero_wall_routing_independent.py` checks **162** parameter cases across all ten executable branches. Their **1,134** class traces are computed directly from the unexpanded restriction formula. It verifies:

- **2,268** coefficients with both determinant parities;
- **2,268** corresponding partition-wrapper calls;
- **532** calls through the other central wall's complement;
- **56** stable first-row extensions;
- **14** exact zeros above five rows.

Additional continuation points in both new cones, including coordinates \((301,302,303)\), give **112** coefficient comparisons against the independently reconstructed polynomials. The returned new-cone polytopes pass **4,536** literal matrix checks and **2,822** witness checks. Each quotient equation, coordinate bound, selector bound, chain gap, and binomial count is verified. The receipt is `ZERO_WALL_ROUTING_EVALUATOR_RECEIPT.json`.

The older enlargement constructor now reads its fixed `VARIABLE_WALL_INITIAL_INPUT.json` rather than theta's subsequently enlarged output. I reread that repair; the independent phase reconstruction here and in A068 already verifies the final mathematical data without relying on the constructor's earlier input state.

The revised complete G033 proof and its executable routes pass. No proof-assistant verification is claimed, and the root's separate actual balanced-coefficient sweeps were not counted as mine.

