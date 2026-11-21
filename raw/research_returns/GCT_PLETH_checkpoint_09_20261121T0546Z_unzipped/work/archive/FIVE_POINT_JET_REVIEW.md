# Five-point jet characters and independent positive-formula checks

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

## A-033. Exact jet maps and complete independent review of G-019

**Status: PASS.** I read the entire report work/root/five_point_symmetric_quotient_report.md, including (SQ.1)–(SQ.16), every endpoint, the full zero set and the stated framework transport. I independently reconstructed all 403,200 fixed coefficients by the following geometric calculation.

### 1. A uniform equivariant jet description

Let \(E=\mathfrak h_5\), let \(\ell_i=e_i-\frac15\mathbf1\), and let \(Z\) be the five corresponding projective points. Use the invariant inner product to write
\[
E=\mathbf Q\ell_i\oplus W_i,\qquad
\alpha_i(v)=\frac{\langle v,\ell_i\rangle}{\langle\ell_i,\ell_i\rangle}.
\]
The affine chart \(\alpha_i\ne0\) is identified with \(W_i\) by
\[
[v]\longmapsto v/\alpha_i(v)-\ell_i.
\]
This map and its inverse \(w\mapsto[\ell_i+w]\) commute with the stabilizer \(S_4\) of the point. The degree-\(c\) line bundle is trivialized on this chart by \(\alpha_i^c\). These choices are transported exactly when the five points are permuted.

Consequently the order-\(k\) jets of \(\mathcal O(c)\) at this point are the actual module
\[
\bigoplus_{j=0}^{k-1}\operatorname{Sym}^j(W_i^*).
\]
The quotient by the \(k\)-th power of the coordinate maximal ideal gives this decomposition directly. The invariant form identifies \(W_i^*\) with \(W_i\), and \(E=\mathbf1\oplus W_i\) under the stabilizer. The complete five-point jet module is induced from this stabilizer module. This specifies the action for every integer \(c\); there is no scalar rescaling of the affine representatives.

For \(g\in S_5\), let \(m_1(g)\) be its number of fixed letters, and put
\[
h_r(g)=\operatorname{tr}(g\mid\operatorname{Sym}^rE),\qquad h_r=0\quad(r<0).
\]
Only fixed points contribute to the trace on the five-point direct sum. At any such point,
\[
\sum_{j=0}^{k-1}
\operatorname{tr}(g\mid\operatorname{Sym}^jW_i)
=h_{k-1}(g).
\]
This identity is the decomposition of \(\operatorname{Sym}^{k-1}(\mathbf1\oplus W_i)\). Therefore the exact jet character is
\[
\boxed{\operatorname{tr}\bigl(g\mid
H^0(\mathcal O/\mathcal I_Z^k(c))\bigr)
=m_1(g)h_{k-1}(g).}
\tag{J.1}
\]
For \(k=0\), both sides are zero.

### 2. The two scalar Euler terms and the symmetric quotient map

The restriction sequence
\[
0\longrightarrow\mathcal I_Z^k(c)
\longrightarrow\mathcal O(c)
\longrightarrow\mathcal O/\mathcal I_Z^k(c)
\longrightarrow0
\]
is equivariant. Its cohomology, with the complete vanishings in A-029, gives
\[
\operatorname{tr}(g\mid C_k)
=h_{2k}(g)-m_1(g)h_{k-1}(g),
\tag{J.2}
\]
and
\[
\operatorname{tr}\bigl(g\mid
H^0(\mathcal I_Z^k(2k-1))-H^1(\mathcal I_Z^k(2k-1))\bigr)
=h_{2k-1}(g)-m_1(g)h_{k-1}(g).
\tag{J.3}
\]
The notation in (J.3) denotes the exact representation-group class of the displayed cohomology sequence.

These equations include the endpoints. At \(k=0\), (J.3) is zero. At \(k=1\), it is \(-\mathbf1\), since \(h_1(g)=m_1(g)-1\); the actual groups are \(H^0(\mathcal I_Z(1))=0\) and \(H^1(\mathcal I_Z(1))=\mathbf1\). At \(k\ge2\), the latter cohomology vanishes by A-029. In degree \(2k\), \(H^1\) vanishes for every \(k\), including the direct degree-two evaluation check at \(k=1\).

Multiplication by the tautological line gives the exact, locally split symmetric-quotient sequence used in (SQ.4). Tensoring with the ideal preserves it. Its cohomology, including the \(k=1\) connecting term, therefore gives
\[
\boxed{\begin{aligned}
\operatorname{tr}(g\mid M_{a,k})
={}&h_a(g)\bigl(h_{2k}(g)-m_1(g)h_{k-1}(g)\bigr)\\
&+h_{a-1}(g)\bigl(m_1(g)h_{k-1}(g)-h_{2k-1}(g)\bigr).
\end{aligned}}
\tag{J.4}
\]
This independent formula uses the standard representation and the actual Taylor maps. It does not require the cubic presentation or G-017's fixed character table.

The flag comparison in G-019 has point order \(k\), first-line gap \(2k\), and relative weight \((a,a,0)\). Its first-line weight after the full determinant is \(a+2k\). The exterior pairing contributes \((\det Q^*)^a\), giving \(\mathcal O(2k)\) and sign \(\epsilon^{d+a}\). Thus (SQ.3) and its parity convention agree with the actual local frame maps. At \(a=0\), the second term in (J.4) is zero. At \(a=k=0\), the module is trivial before the determinant twist, including the empty-partition endpoint.

### 3. Independent reconstruction of every fixed coefficient

For each of the seven cycle types, I formed
\[
\det(1-tg\mid E)=
\frac{\prod_{\ell\in\operatorname{cycles}(g)}(1-t^\ell)}{1-t}
=1+d_1t+\cdots+d_4t^4.
\]
The exact recurrence
\[
h_0=1,\qquad
h_r=-\sum_{j=1}^{\min(4,r)}d_jh_{r-j}
\]
computes all required characters through degree 478. Equations (J.2) and (J.3) give the two scalar arrays, and (J.4) gives their products with \(h_a,h_{a-1}\).

I computed the order-zero through order-three step-60 differences of each separate array. Multiplying those differences according to (J.4), followed by the seven fixed character inner products, gives the mixed differences directly. This differs from computing a two-dimensional multiplicity grid and then taking differences of that grid.

All 403,200 resulting integers agree exactly with the complete root table. Every entry is nonnegative. The \((3,3)\) entries are zero. The other fourteen positive-order positions have strictly positive minima for every label, as stated in the report.

The rational-function verification was independent as well. With \(H(x)=1/\det(1-xg\mid E)\), the even and odd subsequences are
\[
\sum_{k\ge0}h_{2k}t^k
=\left.\frac{H(x)+H(-x)}2\right|_{x^2=t},
\quad
\sum_{k\ge0}h_{2k+1}t^k
=\left.\frac{H(x)-H(-x)}{2x}\right|_{x^2=t}.
\]
Using these expressions in (J.2)–(J.3), I checked all 28 one-variable factors against the common denominator \((1-t^{60})^4\). Their numerators are polynomials of degree at most 239. This proves the residue-polynomial argument from the first nonnegative quotient value, including its initial zero binomial terms.

The two-variable Newton identity consequently holds for all \(a,k\), with degree at most three in each quotient variable. Its bounded polytope conversion uses the two fixed residue equations, one bounded multiplicity coordinate, and two increasing subset chains. The claimed upper bounds of 57,600 tags and nine variables are valid. The constant number of arithmetic operations and the quadratic schoolbook bit-cost bound follow because all binomial degrees and table dimensions are fixed.

I also verified the dimension identity (SQ.15). The common factor
\[
C_k+\bigl(M_k-4C_k\bigr)=(k+1)(2k+1)
\]
at the level of dimensions gives exactly the displayed expression after applying Pascal's identity in \(a\). The exceptional \(k=1\) term is retained.

The exact zero list has 44 triples \((\nu,a,k)\), all in the first 60-by-60 square, and agrees entry by entry with the report. Strict positivity of the \((1,0)\) and \((0,1)\) coefficients on every residue excludes any further zeros. This proves the stated complete support, including both axes and all determinant parities.

The independent script is work/archive/check_symmetric_quotient_by_jets.py. The full receipt, including target hash, separate coefficient minima and maxima, all rational bounds and all 44 zeros, is work/archive/SYMMETRIC_QUOTIENT_JET_RECEIPT.json.

## A-034. Complete review of T-040 and a second jet reconstruction

**Status: PASS.** I read all of work/theta/outer5/q_plus_report.md, equations (QP.1)–(QP.23), including the matrix presentation, its equivariant splitting, every Newton coefficient formula and the complete support argument.

The ordinary/saturated comparisons in (QP.5) use precisely the proved degree ranges of A-029. The degree-one part of the Rees presentation is the cokernel of \(\mathsf B\); the identity \(\mathsf B\mathsf Q=FI_4\) shows that its additional \(F\)-relations already lie in that image. All five maximal minors are the stated \(-FT_i\), and the primitive column \(T\) generates the entire polynomial kernel. The sign labels follow from the actual change of basis in the T-038 resolution.

The tautological sequence gives the exact injection
\[
\mathcal A_k\longrightarrow E\otimes\mathcal C_k,\qquad
s\longmapsto\sum e_i\otimes x_i s.
\]
The quotient is \(\mathcal N_k\) because \(H^1(\mathcal I_Z^k(2k))=0\), including \(k=0,1\). This identifies the cokernel in (QP.13) with the section module.

In the kernel proof, the three-by-three minor \(AD(E_0-B)\) is not divisible by the irreducible cubic \(F\). Thus \(\mathsf B\) has rank three modulo \(F\). From \(Y\mathsf B^t=hI_4\), passage to the fraction field of \(R/(F)\) proves \(F\mid h\). Subtracting \((h/F)\mathsf Q^t\) leaves rows in \(RT\). Multiplication by \(\mathsf B^t\) then proves injectivity of the first map. The report's averaging of the quadratic lift gives the asserted equivariant free decomposition of this kernel; changing that lift only adds a vector in the preceding \(rT^t\) summand. All maps and characters therefore agree.

The negative highest coefficient after multiplying the dimension series by the four parameter factors gives the stated concrete obstruction to regularity of that particular parameter sequence. It does not interfere with the subsequent exact resolution and positive Newton count.

For an independent character calculation, the same jet map (J.1) gives
\[
\boxed{\operatorname{tr}(g\mid\mathcal N_k)
=e_g h_{2k+1}(g)-h_{2k}(g)
-m_1(g)(e_g-1)h_{k-1}(g),}
\tag{J.5}
\]
where \(e_g=m_1(g)-1\). This follows from the actual quotient-bundle exact sequence, with the scalar jet terms substituted. It includes \(\mathcal N_0=\operatorname{End}(E)/\mathbf1\).

I derived its seven rational series by even/odd extraction from \(H(x)\). They agree exactly with (QP.16), and every numerator over \((1-t^{60})^4\) has degree 238. The recurrence calculation from (J.5) reproduces all 1,680 Newton constants, their three closed positive difference formulas, their maximum 197280 and all seven support sets. The coefficient bounds used in the positivity proof are valid because the absolute character values are at most the representation dimensions.

The fixed-residue interpolation applies from \(q=0\), and its degree-three Newton basis gives the displayed positive count. The bounded multiplicity coordinate contributes exactly the fixed integer coefficient; the increasing chain counts the appropriate binomial coefficient. The limits of 240 tags, five variables and four active tags are correct, and the determinant parity gives exactly the two symmetric-outer thresholds.

The independent check script is work/archive/check_q_plus_by_jets.py. Its executed receipt is work/archive/Q_PLUS_JET_RECEIPT.json. The five signed maximal minors and the specified rank-three minor were also independently expanded. The earlier A-029 certificate already independently verifies \(\mathsf B\mathsf Q=FI_4\).
