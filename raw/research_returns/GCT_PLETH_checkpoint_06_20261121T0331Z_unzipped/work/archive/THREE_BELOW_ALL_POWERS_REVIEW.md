# Independent audit of the complete three-below family

Statement **A-056**, reviewing T-051,
`work/theta/outer5/three_below_all_powers_report.md`,
ET.1–ET.13, every section and the full endpoint certificate code.
Checked 21 November 2026 by GPT-6 Astra Pro,
run `/root/archive_audit`; effort setting not exposed.

**Complete proof PASS.** All 3,049,200 fixed endpoint constants
were independently reconstructed. The actual pair and triple
modules, their signed restriction map, all omitted-partition
endpoints and the parity of the balanced flag identification check.

## 1. Validity, jet maps and cohomology

Write \(a=b+x\), \(c=2k-3\), and
\(\alpha=(a+c,b+c,c)\). The first partition inequality in
ET.1 is exactly \(2b+x+k\ge9\); its size is
\(5(d+a+k-3)\), and its second-row excess is \(k\).
Furthermore \(|\alpha|=2b+x+6k-9\ge5k\), so the entire
degree used in the G-027 restriction complex is in its proved
exact range. The rank-three determinant identity is
\[
S_\alpha Q=(\det E)^c\mathcal O(c)S_{(a,b)}Q
=\operatorname{sgn}_5\mathcal O(c)S_{(a,b)}Q.
\]
The chart sign is therefore \(\operatorname{sgn}^{d+a}\),
as stated, since \(\lambda_2=d+a+c\) and \(c\) is odd.

Because \(c\ge k-1\), every scalar homogeneous tangent jet
of order less than \(k\) occurs as the leading jet of a section
of \(\mathcal O(c)\). Global sections of \(S_{(a,b)}Q\)
generate its fiber. Multiplying these sections and correcting
jets successively gives the canonical surjection onto each full
point-jet module. This is the individual point map; its direct
sum has exactly the cokernel computed by the arrangement complex.
G-027's normal-order substitution identifies its kernel with the
displayed Schur component of the point ideal power.

The ambient bundle is acyclic, and a finite point-jet sheaf has
no positive cohomology. Thus its restriction cokernel is precisely
\(H^1\) of the ideal-twisted bundle, with every higher group
zero. The exact degree-\(|\alpha|\) arrangement complex now
identifies this cokernel with the kernel of the actual signed
quotient \(K_2\to K_3\). Its later terms vanish in the proved
degree range. This establishes ET.4 with the stated maps, not
only its character identity.

## 2. Complete two-slot calculation

The two truncated slots have total degree at most \(c+1\),
and the two-dimensional complementary Cauchy factor cannot supply
the third row of length \(c\). Only normal degrees \(c\)
and \(c+1\) occur.

At degree \(c\), the slot degrees are \((k-1,k-2)\)
and its reverse. Multiplication onto \(\operatorname{Sym}^cF\)
and the nonzero determinant highest-vector map identify these
two copies with the endpoint permutation module times
\(S_{(a,b)}W\). The complement determinant character, the
selected-subset orientation and the global sign have exactly the
cancellation in ET.6. The map in ET.7 is an equivariant isomorphism
for the endpoint \(S_2\)-action from \(P\) to
\(\det P\otimes P\); substitution of its nontrivial
permutation verifies this directly.

At degree \(c+1\), both slots have degree \(k-1\).
The normal types \((c+1)\) and \((c,1)\) have exchange
signs plus and minus, respectively, by the two displayed highest
polynomials. Removing one extra top-row box gives both types
when \(x>0\); it is disallowed when \(x=0\). Removing
one extra second-row box gives both when \(b>0\). At
\(b=0\), the vertical adjacency forces only \((c,1)\).
These are the complete skew shapes in this degree.

The dual rank-two Pieri map identifies their complementary
factors with \(W^*\otimes S_{(a,b)}W\), together with
the separately displayed polynomial removed-box factors.
At \(b=0\), the actual factor
\((\det W)^{-1}\operatorname{Sym}^{a+1}W\) remains;
omitting it would give an incorrect endpoint. The determinant
and multiplication maps in T-047 identify it, and the exchange
sign computed above gives its \(\det P\)-twist. This proves
all four summands of ET.6 for every stated endpoint.

## 3. Triple modules and quotient signs

A three-slot term needs at least \(b+4k-6\) normal boxes,
but at most \(3(k-1)\) are available. It vanishes exactly
in the range asserted in ET.8. The only sectors still to examine
are \((k,b)=(3,0),(2,1),(2,0)\).

For \((3,0)\), all slots have degree two and the required
normal type is \((3,3)\). Only the intermediate type
\((3,1)\) can acquire a horizontal two-strip to produce it,
so its multiplicity is one. Its highest polynomial
\([uv][uw][vw]\) changes by the selected three-letter sign.
The complementary degree is \(x+3\); the global determinant
sign changes its parity to \(x\). The two selected three-letter
signs from orientation and determinant cancel. The result is
the first induced module in ET.9.

For \((2,1)\), each slot has degree one, the normal type
is \((2,1)\), and its literal Young-projector multiplicity
module is \([2,1]\). Complementary degree \(x+2\), with
the global sign, gives exponent \(x+1\). For \((2,0)\),
normal degrees two and three both occur. The former is the
three choices of \(\Lambda^2F\), with multiplicity
\(\operatorname{Ind}_{S_2}^{S_3}\operatorname{sgn}_2
=[2,1]\oplus\operatorname{sgn}_3\). The latter has types
\((2,1)\) and \((1,1,1)\), each once, hence the same
multiplicity module. The two complementary parities are opposite,
giving \(\mathbf1\oplus\operatorname{sgn}_2\).
Validity forces \(x\ge7\) here, so the disconnected skew
shape used in this last step has no additional endpoint.

All these identifications use the stated highest polynomials or
Young projections. The map between them is retained as the
actual arrangement quotient, followed by those maps. Its
surjectivity follows from the exact complex. Literal induction
over fixed complementary pairs independently gives every entry
of the three seven-class traces ET.10.

## 4. Every fixed endpoint coefficient

The actual zeroth-cohomology trace is the Euler trace plus the
pair trace minus the triple trace. At \(k=2\), the smallest
scalar twist is \(-1\), where \(\mathcal O(-1)\) is
acyclic; the negative complete-function indices \(-1,-2\)
are exactly zero. No extrapolation is needed.

The six two-variable branches and fifteen one-variable branches
in ET.12 form a disjoint exhaustive partition of the valid
\(2\le k\le7\) parameters. The symbolic identity degree
is at most five, with separate degrees at most three and four.
The fixed-phase nonidentity degrees are bounded by three, three
and one, and the remaining classes are periodic. These bounds
prove the finite Newton identity for all parameters. The code's
positive ordinary identity coefficients and all phase formulas
were read and checked. A wording correction requested during
review now explicitly says to subtract the triple dimension.

The independent script
`check_three_below_endpoints_independent.py` does not use the
three-term Schur-complex Euler formula or the saved scalar
correction formulas. It uses the odd-sign-twisted ambient
\(3\times3\) Jacobi–Trudi character, subtracts the full
point jets, adds the literal four-summand induction ET.6 and
subtracts the literal three-summand cases ET.9. Standard
characters come from cycle denominators; the seven character
rows come from Murnaghan–Nakayama. Successive quotient-index
differences then reconstruct every constant using unbounded
Python integers.

All **3,049,200** constants pass. All **147** branch/label
hashes, minima, maxima, active orders and **38** zero residues
match the fixed certificate. The minimum positive active-order
constant is **941** and the maximum is **5,668,963,200**.
The largest absolute trace evaluated was **6,756,429,431,760**.
Signed 64-bit conversion is used only after the final exact
bound, for the comparison hash serialization. The complete
receipt is `THREE_BELOW_ENDPOINTS_INDEPENDENT_RECEIPT.json`.

The coefficient-interval and strictly increasing-chain maps give
exactly the stated bounded polytopes. The active orders have at
most five chain variables, together with two quotient variables
and one coefficient-interval variable, hence at most eight
variables, or five on a fixed-\(b\) branch. Positive first
differences confine all endpoint zeros
to the residue boxes. Their branch and determinant-parity
conversion gives the exact support stated in ET.13. The
\(k\ge8\) formulas and their seven valid exceptions are the
already completely audited T-048 result, rather than a new
computation claimed by this event. Likewise the author's 4312
evaluator comparisons and the rectangular agent's 1561 cases
are separate checks, not counted as this independent run.
