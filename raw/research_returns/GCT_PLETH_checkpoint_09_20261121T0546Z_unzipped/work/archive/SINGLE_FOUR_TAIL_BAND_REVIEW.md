# A-084. Whole-proof review of R044

**Status: PASS.** I read the complete `work/rectangular/single_four_tail_canonical_band.md`, SF.1–SF.14 and all five sections, including the full invariant-algebra support exhaustion. I also reread the exact HO.3–HO.7 generator/Pfaffian maps and the finite-row maps used here. The claimed full-isotypic surjectivity for $n\ge a\ge2$, $\lambda_2\le4$, $\lambda_3\le3$ passes.

## 1. Exact finite-degree reduction

The dehomogenization $F=u^nf(y_i/x_i)$ is injective on the dense first-coordinate chart. The first-coordinate highest equations are exactly common translation invariance of $f$, so the actual centered-row map factors it through $\mathfrak h_a$. The remaining highest equations and rational Young projector select $S_\nu\mathfrak h_a$, and row permutations select its invariant space.

The inverse on the subspace of separate row degree at most $n$ is the explicit homogenization. Thus the finite-degree highest space injects into the stated invariant space, and each supplied row-degree-bounded generator extends by the actual map. No stable-dimension equality is needed.

The finite-row power-sum map
$\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)\otimes\Lambda(\Lambda^3T)\to
(\Lambda(\mathfrak h_a\otimes T))^{S_a}$
is surjective by the already proved equality-partition induction. Repeated odd row types have zero invariant average; the remaining stabilizers supply nonzero factorials. The projection kills singleton power sums. Its skew-Cauchy Young maps identify the desired invariant multiplicity with that of
$\gamma=(1+p+q+s,1+p+q,1+p,1)$.

## 2. Complete support exhaustion

The Pfaffian/standard-minor decomposition supplies exactly the paired shapes $(P,P,Q,Q)$, with their actual column maps. The complementary-column contractions give exterior factors
$1$, $\Lambda^3T$, $\det(T)\Lambda^2T$, $\det(T)^2T$, $\det(T)^3$.
Since $\gamma_4=1$, the last two cannot contribute.

For exterior degree zero, equality of the paired first and last parts forces $s=p=0$. For exterior degree one, the vertical three-strip indicators have sum three. When $Q=0$ and the fourth indicator is one, partition order forces the third indicator one, then the remaining addition lies in row one; this gives $p=0,s=1$. When $Q=1$ and the fourth indicator is zero, all first three indicators are one; this gives $p=1,s=0$.

For exterior degree two, its existing determinant factor forces the extra determinant exponent and the bottom paired part to be zero. The fourth indicator is zero. The permitted vertical two-strips occupy rows $(1,2)$ or $(1,3)$, giving respectively $p=s=0$ or $p=s=1$. The first has $q\ge1$. Every other indicator pattern either violates partition order or has fourth part at least two.

The exact surjection and Young maps therefore prove that only
$(4,2^q)$, $(4,3,2^q)$, $(4,2^q,1)$, and $(4,3,2^q,1)$
can occur. This is exhaustive at every finite row count, so every omitted single-four tail has zero target multiplicity.

## 3. Exact blocks and all ordered endpoints

The parameter translations in SF.9 are correct:

| Tail | Previously checked block | Parameter |
|---|---|---|
| $(4)$ | R038 | binary |
| $(4,2^q)$, $q\ge1$ | R041 | $m=q+1$ |
| $(4,3,2^q)$ | R043 | $m=q+2$ |
| $(4,2^q,1)$ | R039 | $m=q+2$ |
| $(4,3,2^q,1)$ | R040 | $m=q+3$ |

The first three ranks are the exact full matrix ranks, including the finite one- and two-dimensional spans. The last two use the explicitly nonzero normalized scalars and their reciprocals. In each row the finite target dimension is nondecreasing in the slot count; hence $n\ge a$ makes the proved rank equal to the entire target multiplicity. The displayed transpose conventions and inverse matrix order agree with the actual grid pairing.

For $n=2$, the ordered degree is too small for second part four. For $n=3$, only $a=3$ can occur, and the only two partitions are $(5,4)$ and $(4,4,1)$. The binary weight difference for $(5,4)$ is $3-3=0$. The latter is the unit block with $m=2$, whose actual scalar is $-1/9$. These exhaust all small ordered endpoints.

The second-row-at-most-three case is the already independently checked R035/R036 result (A065/A066). Combining it with the four-family exhaustion and the exact moment blocks proves the full asserted band.

## 4. Full-isotypic and geometric transport

The rational highest-space maps have full multiplicity rank. Equivariance extends each reached highest vector to its entire irreducible Schur summand, and complete reducibility separates copies. The tensor maps and matrices are defined over $\mathbb Q$ and are natural in $V$, so extension to any characteristic-zero field preserves the conclusion. For insufficient ambient rank, the actual column antisymmetrizer gives zero.

The Chow-coordinate pullback and frame-associated maps are the same already verified EP.3–EP.5 and R036 §5 morphisms. The proof obtains surjectivity from the explicit maps and inverses, not merely from an equality of classes.

## 5. Verification scope

This is an independent complete proof reading, with explicit reconstruction of the exterior-degree case split and every finite parameter translation. The new R042/R043 scalar calculations are in the separate A082/A083 receipt. The source's 122 target/source coefficient comparisons and its cited historical binary reference were read as attribution; no additional numerical sweep or fresh historical-source verification is claimed in this event.
