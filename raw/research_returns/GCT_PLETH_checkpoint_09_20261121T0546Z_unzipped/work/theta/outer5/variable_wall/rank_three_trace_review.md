# Exact rank-three trace review and a singleton correction

This independently reviews G034/(OW.4)–(OW.8), then records
the precise failed candidate in a proposed generic extension.
The complete G034/(OW.1)–(OW.14) proof and global routing were
also read and checked. The result is PASS; the finite
cone certificates have their separate execution/audit events.

## 1. The complete triple telescope

Letk≥1,c≥0,x≥0,a=b+x andb+c≥2k. Fix a selected
three-subset with cycle typeη⊢3 and complementary-line
eigenvalueε=±1. Its normal trace polynomial is

\[
P(U,V,W)=\prod_{\ell\in\eta}
\sum_{i+j+h<k}U^{\ell i}V^{\ell j}W^{\ell h}.
\]

PutM=3(k−1),N=a+b+3c. The actual Young projection to
normal shapeρ=(p,q,r) has trace given by the coefficient
ofU^pV^qW^r in

\[
P(U,V,W)(1-V/U)(1-W/U)(1-W/V).
\]

The complementary-line Pieri map is present exactly for
a+c≥p≥b+c≥q≥c≥r≥0, and has valueε^{N−p−q−r}.
DefinePε=P(εU,εV,εW) and
F=Pε(1−V/U)(1−W/U). The latter is symmetric inV,W,
has nonnegative exponents of these two variables, and
retains the total-degree boundM.

Forp≥b+c≥2k, every nonzero coefficient hasq+r≤k−3.
Thusq≤b+c is automatic. Writef_{p,q,r} for the
coefficients ofF. The exact inner sum is

\[
\begin{aligned}
\sum_{q\ge c,\ 0\le r\le c}
 (f_{p,q,r}-f_{p,q+1,r-1})
&=\sum_{q\ge c}f_{p,q,c}
  +\sum_{r=0}^{c-1}f_{p,c,r}\\
&=\sum_{q\ge0}f_{p,q,c}.
\end{aligned}
\tag{RT.1}
\]

The second equality uses the actualV/W symmetry, so both
boundary pieces are included. The negative-index entries
are zero. After this cancellation the remaining factor
1−1/U telescopes in p, giving

\[
\epsilon^N[W^c]
\bigl([U^{b+c}]-[U^{a+c+1}]\bigr)
P_\epsilon(U,1,W)(1-W/U).
\tag{RT.2}
\]

For a cycle of lengthℓ, reverse theU exponent atℓ(k−1)
and putz=U^{-1}. Writingi=k−1−j−h−s gives the phase
ε^{ℓ(k−1)} and the monomial
z^{ℓj}(Wz)^{ℓh}(εz)^{ℓs}. The needed reversal deficits
are at mostM−b−c≤k−3<k; hence the boundj+h+s<k
can be removed in these coefficients. Each cyclic factor
is exactly the product of three geometric series.

The remaining W-coefficient is

\[
[W^c]\frac{1-Wz}{\prod_{\ell\in\eta}(1-(Wz)^\ell)}
=z^c h_\eta(c),\qquad
h_\eta(c)=[u^c]\frac{1-u}{\prod_{\ell\in\eta}(1-u^\ell)}.
\tag{RT.3}
\]

Definet=M−b and
Aηε(h)=[z^h]∏ℓ[(1−z^ℓ)(1−ε^ℓz^ℓ)]^{-1},
with negative-index coefficients zero. Equations (RT.2)–(RT.3)
therefore give the exact selected-triple trace

\[
\epsilon^{x+c+k-1}h_\eta(c)
\bigl(A_{\eta,\epsilon}(t-2c)
      -A_{\eta,\epsilon}(t-x-2c-1)\bigr).
\tag{RT.4}
\]

The phase isε^{N+M}, equal to the displayed exponent
modulo two. Multiplying by(−1)^{#cycles(η)} includes
the restriction-complex sign and its orientation line.
All steps are finite coefficient reindexings of the actual
normal Young and complementary Pieri projections. Atk=1,2
the required deficits are negative; these equations give zero
without an additional endpoint convention.

This independently proves the exact algebraic identity
used in G034. Its source-side coefficient meaning is fixed
by G027's actual restriction maps; no unidentified
cohomology rank has been replaced by a character guess.

## 2. The complete G034 routing check

Forc=1, the actual complementary partition has raw order
k′=b+1−k, quotient parametersx′=2b+x+3−5k,b′=1,c′=b,
and outer twistsgn^H,H=λ1. A negative raw order is corrected
by multiplication byu^{k−b−1}, with exactly that first-row
degree and no new determinant sign. Atb≤2k−2 the resulting
c′ is at least2k′. Atb=2k−2+s,1≤s≤3, the defect is
exactlys. These are the stated previously proved branches.

Forb≥2k+2, the upper chamber is T055; its boundary strip
b=3k−4 forcesk≥6 and is T056. In the remaining range,
τ=3k−5−b≥0. Forx≥τ, the inverse cone coordinates are
(x−τ,τ,k−τ−7), with last coordinateb−2k−2≥0. Forx<τ,
they are(x,τ−x−1,2b+x+3−5k). Direct substitution recovers
the original parameters. The initial λ2<n stable map and
the complementary λ3−λ4=1 wall preserve all labels through
the printed actual determinant and section maps. No gap was
found in any routing endpoint.

## T-057. the exact generic-singleton candidate that fails

For normalizedb+c≥2k, one proposed simplification was

\[
\sum_{l=0}^{\min(c,k-1)}
\det(V)^{c-l}\Theta_{V,k-l}(a+l,b+l),
\qquad \dim V=3,
\tag{RT.5}
\]

whereΘ uses the polynomial two-row Jacobi–Trudi convention
h_j=0 forj<0. This is valid for0≤c<k, as proved in §4.
It is false throughout the larger normalized domain.

Takek=5,c=8,b=2,x=0, soα=(10,10,8) andb+c=2k.
The actual singleton Pieri sum has onlyi=0,0≤j≤2 and
0≤l≤4−j. Its identity dimensions, grouped byj, are

\[
(6+10+15+21+28)+(8+15+24+35)+(6+15+27)
=210.
\]

The proposed expression (RT.5) is220. Its missing term is
the full three-row determinant at(i,j,l)=(0,4,0):

\[
s_{(10,6,8)}(V)=-s_{(10,7,7)}(V),
\qquad \dim s_{(10,7,7)}(V)=10.
\tag{RT.6}
\]

Removingdet(V)^8 from this nonpartition sequence would
give the polynomial two-row determinant s_{(2,-2)}, which
is zero. That loses the actual−10 term. Thus the rejected
step is an unjustified determinant removal before the
second/third-row straightening. The nearbyx=1 example gives
actual525 versus proposed540; the missing dimension is15.
The finite check also reproducedk=6,c=9,b=3,x=0 as560
versus575. These are exact rational/integer counterexamples,
not a claimed obstruction to every generic formula.

## 4. Correct singleton formulas on both stated domains

The actual horizontal-strip sum is always

\[
\sum_{\substack{i,j,l\ge0,\ i+j+l<k\\
                 i\le x,\ j\le b,\ l\le c}}
s_{(a+c-i,b+c-j,c-l)}(V).
\tag{RT.7}
\]

For0≤c<k andb+c≥2k, one hasb≥k+1. Hencej≤b
is automatic in this sum. For each fixedl, the involution
(i,j)↦(x+j+1,i−x−1) removes thei≤x cutoff by exact
two-row determinant cancellation. Every shifted second
partb+l−j is at leastb−k+1+2l≥2. The full-height
column pairing can therefore remove det(V)^{c−l}
without crossing a negative-part boundary. This proves
(RT.5) on the entire stated0≤c<k domain, with the actual
Pieri and exterior maps retained.

Forc≥k, a different exact expression is the full
three-row Jacobi–Trudi simplex

\[
\sum_{i,j,l\ge0,\ i+j+l<k}
s_{(a+c-i,b+c-j,c-l)}(V),
\tag{RT.8}
\]

with the unshifted three-row polynomial determinant kept.
Indeed \(h_n(V\oplus u)=\sum_{j\ge0}h_{n-j}(V)u^j\). Multilinearity
in the three determinant rows expands sα(V⊕u) into this
simplex at coefficients ofu-degree less thank. Its actual
line-branching map is the same horizontal-strip sum (RT.7).
Here all removall satisfy l<k≤c, so no additional third-row
truncation is present. This proves (RT.8) exactly. It does
not license the failed termwise determinant removal (RT.5).

Thus both subdomains have exact formulas: the smaller
determinant/triangle expression for c<k, and the full
three-row determinant expression for c≥k. The generic
positive conversion remains a separate active task.
