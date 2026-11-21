# DEG_L / faithful operations and the replacement-object gate

Run `DEG_L_20261121`, author `/root`, GPT-6 Astra Pro, effort not exposed. These findings strengthen DER2 and test broader attempts to repair an established full semiregularity kernel. They do not construct the successful replacement required by S-14.

## DER5. Nonzero-rank tensor and nonzero-Euler convolution preserve every full trace kernel

Let $A$ be a positive-dimensional complex abelian variety. For perfect complexes define derived Pontryagin convolution by
\[
 E*F=Rm_*(p_1^*E\otimes^{\mathbf L}p_2^*F),
\]
where $m$ is addition. If $\chi(A,F)\ne0$, this functor is injective on every morphism space:
\[
 \operatorname{Hom}(E,E'[j])\hookrightarrow
 \operatorname{Hom}(E*F,(E'*F)[j])\qquad(j\in\mathbf Z).
\tag{DER5a}
\]
It therefore injects $\ker\sigma_E$ into $\ker\sigma_{E*F}$. More generally, tensoring by a perfect complex of nonzero virtual rank has these same properties on every smooth connected projective complex variety.

In particular, for the ideal of the diagonal,
\[
 \operatorname{Ext}^j(E,E)\hookrightarrow
 \operatorname{Ext}^j(\Phi_{\mathcal I_\Delta}E,
                         \Phi_{\mathcal I_\Delta}E)
\tag{DER5b}
\]
for **every** perfect complex $E$ and every $j$. The evaluation-cone construction cannot remove a full semiregularity kernel even without the global generation, cohomology vanishing, or dimension-at-least-three hypotheses of DER2.

**Proof.** Let $K$ be perfect of constant virtual rank $r\ne0$ on a smooth connected complex variety $X$. Dualizability gives coevaluation and graded trace maps
\[
 \mathcal O_X\longrightarrow K\otimes^{\mathbf L}K^\vee
 \longrightarrow\mathcal O_X
\]
whose composite is $r\operatorname{id}$. Indeed, a bounded locally free presentation computes the trace of the identity as the alternating sum of its ranks. This local computation defines the global categorical trace. For $u:E\to E'[j]$, naturality identifies the composite through
$u\otimes\operatorname{id}_K\otimes\operatorname{id}_{K^\vee}$ with $ru$. If $u\otimes\operatorname{id}_K=0$, that composite vanishes; since $r$ is invertible over $\mathbf C$, $u=0$. This argument applies to complexes of either sign of virtual rank and in every morphism degree.

Let $\mathcal F:D_{\mathrm{perf}}(A)\to D_{\mathrm{perf}}(A^\vee)$ be the normalized Poincare Fourier--Mukai equivalence. Mukai, *Duality between $D(X)$ and $D(\widehat X)$ with its application to Picard sheaves*, Nagoya Math.J.81(1981), Theorem2.2 p156 and equation(3.7) p160, gives
\[
 \mathcal F(E*F)\simeq
 \mathcal F(E)\otimes^{\mathbf L}\mathcal F(F).
\tag{DER5c}
\]
There is no shift in this direction of the identity. The virtual rank of $\mathcal F(F)$ is $\chi(A,F)$: derived base change identifies its fibre at a degree-zero line bundle $P$ with $R\Gamma(A,F\otimes P)$. The Euler characteristic of this family is constant and at $P=\mathcal O_A$ equals $\chi(A,F)$. Apply the preceding tensor argument to $K=\mathcal F(F)$ and conjugate by the equivalence, proving (DER5a).

For the evaluation cone, use the flat difference map $d(x,y)=y-x$. Then $d^*\mathcal I_0=\mathcal I_\Delta$. The change of variables $(x,z)\mapsto(x,x+z)$ in the integral transform gives
\[
 \Phi_{\mathcal I_\Delta}(E)\simeq E*\mathcal I_0.
\]
Since $\dim A\ge1$, $\chi(\mathcal O_A)=0$ and the exact sequence of the origin gives $\chi(\mathcal I_0)=-1$. One can also see the sign directly from Mukai Theorem2.2 and Example2.6 p157: applying $\mathcal F$ to this sequence gives the triangle
\[
 \mathcal F(\mathcal I_0)\longrightarrow
 \mathcal O_{\widehat0}[-\dim A]\longrightarrow
 \mathcal O_{A^\vee}\longrightarrow.
\]
Its first term has virtual rank $-1$. Thus (DER5a) applies and proves (DER5b). Positive dimension is necessary, because the ideal of the origin is zero in dimension zero.

For each exact functor $\Psi$ under consideration, Perry, arXiv2604.00511v2, Remarks2.3 and2.5 p5, gives
\[
 \sigma_{\Psi(E)}(\Psi(u))=\Psi_*\sigma_E(u)
\]
for the full semiregularity map. Faithfulness makes the image of a nonzero kernel element nonzero, and the displayed identity keeps it in the kernel. This conclusion persists under composition with other such functors and with derived equivalences. No equivalence of the convolution functor itself is asserted. QED.

**Scope.** This concerns full object semiregularity. A map-level obstruction killed before reaching self-Ext is not covered. A different equivariant structure on a new object, or a functor not satisfying the displayed faithfulness criterion, is not excluded. The result closes the proposed repair by allowing arbitrary cohomology in the evaluation cone; DER2 is retained as its simpler bundle case.

**Primary source and Grothendieck placement.** Mukai's PDF is <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf>. The whole short proofs of Theorem2.2 and equation(3.7) were read. The convolution identity uses the Poincare biextension additivity of SGA7I, ExposeVII, section2.4 pp164--165 and Example2.9.5 p175. Virtual rank is the perfect-complex K-theory invariant used in SGA6, Expose0 section1 p1. This placement does not attribute the later Fourier--Mukai equivalence or semiregularity theorem to those earlier texts.

## DER6. A polarization-only tensor repair retains the kernel or loses the Weil component

Let $A$ be polarized of Weil type, of dimension $2n$ with $n\ge2$. Suppose a perfect $E$ has a nonzero full semiregularity kernel and
\[
 e^B\operatorname{ch}(E)=P(\theta)+\lambda t,
 \qquad\lambda\ne0,\quad\theta t=0.
\]
Let $K$ be a perfect complex whose entire Chern character is $Q(\theta)$. If $Q(0)\ne0$, the tensor product $E\otimes^{\mathbf L}K$ retains a nonzero full kernel. If $Q(0)=0$, its $B$-normalized character is a polarization polynomial and its Weil component is zero. Thus none of these tensor operations repairs full semiregularity while retaining the specified nonzero Weil component.

**Proof.** The constant coefficient $Q(0)$ is the virtual rank of $K$. If nonzero, DER5 gives the kernel injection. For either value of the coefficient,
\[
 e^B\operatorname{ch}(E\otimes^{\mathbf L}K)
 =P(\theta)Q(\theta)+\lambda Q(0)t,
\tag{DER6}
\]
since all positive powers of $\theta$ annihilate $t$. The polynomial part has zero Weil projection by B6. Hence when $Q(0)=0$ no Weil component remains. QED.

The same alternative holds on the Fourier--Mukai dual if the transformed input has the displayed polynomial-plus-Weil form there and the transformed convolution kernel has polarization-polynomial character. This qualification is necessary; no general assertion about an arbitrary $B$-field under Fourier transform is made. A correction using different non-Lefschetz data or a new equivariant structure is not excluded. Adding a direct summand likewise retains the original full kernel by the block-diagonal trace calculation underlying S-08.

The Chern-character product belongs to SGA6, Expose0 section1, equations(1.1)--(1.3), p1; the precise generic Weil projector is B6/B16. The conclusion is an obstruction for these specified constructions, not an assertion that all objects with the corrected K-class fail semiregularity.

## DER7. Adams--determinant untwisting gives a multiplier independent of the gerbe order in nonzero rank

Keep the successful-deformation hypotheses of DER4, and write
\[
 w=e^{B_0}\operatorname{ch}(E_0)=P(\theta_0)+\lambda t_0,
 \qquad P(x)=r+p_1x+\cdots.
\]
Assume the virtual rank $r$ is nonzero; it may be negative. Put $d=|r|$, $a=\operatorname{sgn}(r)$, and
\[
 \beta_0=(-1)^{n-1}(n-1)!\lambda,\qquad
 v=\int_{A_s}\theta_s^{2n}.
\]
Choose an integer $b>0$ with $b\beta_0\in\mathbf Z$. Then the single positive integer
\[
 N_*=v\,|b\beta_0|\,|r|^n
\tag{DER7a}
\]
works as a multiplier for signed integral representatives of $t_s$ on every fibre. A common degree bound is obtained by the bundle-generation construction below. Unlike the degree bound, this multiplier depends only on $r,\lambda,n$ and the fixed polarization volume, and not on the gerbe order, its enlargement for the group action, a bundle resolution, or its generation twists.

**Proof: exact weight cancellation.** On the local finite gerbe $\pi:\mathcal A\to A_U$ in DER4, let $F$ be the deformed weight-one perfect object. Its determinant is an invertible object of weight $r$: for a bounded vector-bundle presentation, the determinant is the alternating tensor product of determinants and its weight is the alternating sum of the ranks. The determinant construction is invariant under quasi-isomorphism and descends; an exact primary locator is Knudsen--Mumford, *The projectivity of the moduli space of stable curves I*, Mathematica Scandinavica39(1976), Theorem2 p42, as used in S-17.

The Newton expression for $\psi^d([F])$ is an integral virtual sum whose terms all have weight $d$, by DER4. Tensoring every term by $\det(F)^{-a}$ makes its weight
\[
 d-ar=|r|-\operatorname{sgn}(r)r=0.
\]
Thus it descends term by term to an ordinary integral perfect K-class $\xi$ on $A_U$. This is exact weight zero, not just weight zero modulo a particular band order.

On the central root gerbe write $F_0=\pi^*E_0\otimes T$. The factors of the tautological root cancel, so
\[
 \xi_0=\psi^d(E_0)\otimes\det(E_0)^{-a}.
\]
Comparing the degree-two component of $w$ gives $c_1(E_0)+rB_0=p_1\theta_0$. Consequently
\[
 \begin{aligned}
 \operatorname{ch}(\xi_0)
 &=e^{-a c_1(E_0)}e^{-dB_0}
       \bigl(P(d\theta_0)+d^n\lambda t_0\bigr)\\
 &=e^{-a p_1\theta_0}P(d\theta_0)+d^n\lambda t_0.
 \end{aligned}
\tag{DER7b}
\]
Here $ar=d$ cancels the B-field and $\theta_0t_0=0$ removes the exponential on the Weil term. The character formula is flat on the connected neighborhood, exactly as in DER4.

**Proof: integral cycles with the stated fixed multiplier.** Apply DER4's finite bundle resolution, addition of a negative polarization exponential and trivial summands, and positive generation twist to $\xi$. None of these changes the Weil coefficient. We obtain a globally generated ordinary vector bundle $V$ of rank at least $n$ with
\[
 c_n(V_s)=C\theta_s^n+d^n\beta_0t_s.
\]
Its general degeneracy cycle $Z_s$ is effective, has this class, and has degree $Cv$. The nonzero Weil component implies $Z_s\ne0$, hence $C>0$. Since $Z_s$ is an integral cycle, its degree is an integer:
\[
 Cv\in\mathbf Z_{>0}.
\tag{DER7c}
\]
This elementary integrality, rather than a denominator estimate on the entire polarization polynomial, suffices. Set $c=vb$. Then $cC=b(Cv)$ is a positive integer and $c d^n\beta_0$ is a nonzero integer. Let $W_s$ be a general intersection of $n$ polarization hyperplanes. We have
\[
 c d^n\beta_0t_s
   =\operatorname{cl}(cZ_s)-\operatorname{cl}(cC W_s).
\]
Both cycles on the right are effective integral and have the same degree
\[
 D=vb\,\deg Z_s=vbCv.
\tag{DER7d}
\]
Reverse the signs if necessary. The multiplier is exactly (DER7a). The generation construction fixes $C$ on the local neighborhood, hence fixes $D$. The fixed-$N_*$, fixed-$D$ projective closed-locus argument of DIV1 propagates these same integers from its dense etale image to every fibre. QED.

**Optional gcd refinement.** If the gerbe band is $\mu_M$, put $d_0=\gcd(|r|,M)$ and choose $a_0\in\mathbf Z$ with $a_0r\equiv d_0\pmod M$. Then $\psi^{d_0}(F)\otimes\det(F)^{-a_0}$ has weight zero modulo $M$ and descends. If $k=(d_0-a_0r)/M$, its central class is
\[
 \psi^{d_0}(E_0)\otimes\det(E_0)^{-a_0}\otimes L_0^k,
\]
where $T^M=\pi^*L_0$. Its character is
\[
 e^{-a_0p_1\theta_0}P(d_0\theta_0)+d_0^n\lambda t_0.
\]
Indeed the B-field exponent is $-d_0B_0+a_0rB_0+(d_0-a_0r)B_0=0$. The preceding cycle proof gives multiplier $v|b\beta_0|d_0^n$. Multiplying both effective cycles by $(|r|/d_0)^n$ recovers the same $N_*$ if desired. For virtual rank zero, take $d_0=M,a_0=0$; this is DER4, and no bound independent of $M$ is asserted in that case.

**Relation to S-17 and the remaining gate.** The Adams degree can be the absolute virtual rank, in place of the tensor exponent used by the tensor--determinant construction. The Weil coefficient grows by $|r|^n$, irrespective of the larger powers arising from a tensor expansion. All these operations occur after the successful deformation; their output is used for cycles and is not claimed semiregular. The required initial weakly equivariant semiregular object remains unconstructed in the open cases. The operation uses SGA6, ExposeV, Appendix7.1 pp360--361 and Proposition7.5 pp362--364, together with its determinant formalism and the FGA221 closed parameter spaces of DIV1.

## Check status

Root and the semiregularity agent have read all three complete proofs. DER5–DER6 passed the graded-trace, virtual-rank, no-shift convolution, origin-ideal and dimension-zero checks. DER7 passed the exact-weight cancellation for either sign of rank, central B-field calculation, integral coefficient argument, fixed-multiplier closure and gcd refinement. The events record actual whole-proof readings; no proof-assistant check is claimed.
