# Exact checks for cote 84, scans 146–193

These are this run's checks of the supplied transcriptions. They do not decide the ink. The accompanying `programs/recompute.py` performs exact polynomial and matrix calculations; `outputs/recomputed.json` records every residual and the finite enumerations. The order of a tensor basis is always stated. Source line numbers below refer to `pro/MPL_84_146-193_transcription.tex`.

## 1. The fourth tensor component is essential

For a locally split extension (E_i=L_i\oplus M_i), write

\[
P_i=\begin{pmatrix}\chi&\tau_i\\0&0\end{pmatrix},\qquad
Q_i=\chi I-P_i=\begin{pmatrix}0&-\tau_i\\0&\chi\end{pmatrix}.
\]

These represent (\alpha_i\pi_i) and (\varpi_i\psi_i). They satisfy (P_i+Q_i=\chi I), (P_iQ_i=Q_iP_i=0), and (P_i^2=\chi P_i), integrally. The displayed matrices at 146 have the same identities with (\chi=2), in a different ordering. Also

\[
(I-\gamma P_i)^2-I=\gamma(\gamma\chi-2)P_i.
\]

Thus (\gamma\chi=2) is sufficient for an involution. It is not necessary for every individual degenerate operator. The second ansatz on 148 imposes (\lambda^2+1=\chi), (\lambda\mu=-1), (\mu^2=\gamma). Its consequence is (\gamma(\chi-1)=1); combining it with the first ansatz adds a hypothesis and forces (\gamma=1,\chi=2). The corrected scalar identity on 152 is identically (\chi=\chi), not a contradiction (2\chi=\chi).

In the ordering (LL,LM,ML,MM), put

\[
F=\alpha I+\beta(P_1\otimes I+I\otimes P_2)+\delta P_1\otimes P_2,
\quad \alpha=-\chi(1-\delta\chi),\quad\beta=1-\delta\chi.
\]

The full matrix is

\[
F=\begin{pmatrix}
\chi&\tau_2&\tau_1&\delta\tau_1\tau_2\\
0&0&0&(1-\delta\chi)\tau_1\\
0&0&0&(1-\delta\chi)\tau_2\\
0&0&0&-\chi(1-\delta\chi)
\end{pmatrix}.
\]

Its first three columns satisfy the pushout boundary conditions displayed on 158 and 164. The missing fourth column must also satisfy the pullback conditions. For a comparison fixing both endpoints, its required lower entries are (-\tau_1,-\tau_2,\chi). The residuals are

\[
(2-\delta\chi)\tau_1,\quad(2-\delta\chi)\tau_2,
\quad\chi(\delta\chi-2).
\]

The universal coefficient choice therefore works when (\delta\chi=2). At (\chi=2,\delta=1), this is exactly (I+(I-P_1)\otimes(I-P_2)). The source's partial three-column calculation does not establish the fourth condition. Conversely, special modules can kill the residuals without forcing the scalar equality. Scans 158 and 164 must not be interpreted as legitimizing cancellation of (\chi), of a nonfaithful module, or of the image of (\pi_i). Explicit counterexamples over (\mathbb Z/4) are saved in the output.

## 2. A conditional counterexample with every hypothesis checked

This tests the interpretation of the labels on 168 as identity maps and of the sentence on 170, lines 1313–1315, as a map of extensions fixing the endpoints. Codex K84-11 reads the labels as `1`; Pro leaves `1|parallel`. A sign on an endpoint would change the claim being tested.

Work over a smooth projective elliptic curve (X) over a field (k) of characteristic zero, and choose a nonzero class (e\in H^1(X,\mathcal O_X)). Such a class exists because the genus is one. The identification (\operatorname{Ext}^1(\mathcal O_X,\mathcal O_X)=H^1(X,\mathcal O_X)) is the one in [Stacks, Tag 0B3A](https://stacks.math.columbia.edu/tag/0B3A); the genus convention is [Tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6). Let (E_1) represent (e) and let (E_2=\mathcal O_X\oplus\mathcal O_X) be split. All four endpoints are (\mathcal O_X). Both extensions are locally split because their quotients are locally free. Their middle terms are vector bundles of rank two, and their inclusions remain injective after every tensor product, as required by the margin on 170.

Set (\chi=0), (\pi_i=\psi_i:E_i\to\mathcal O_X=L_i), and (\varpi_i=-\alpha_i:M_i=\mathcal O_X\to E_i). Then

\[
\alpha_i\pi_i+\varpi_i\psi_i=0,\qquad
\pi_i\alpha_i=0,\qquad\psi_i\varpi_i=0.
\]

Thus all three displayed trivialisation identities hold. Relative to any local section (s_i) of (\psi_i), the parameter (\tau_i=\pi_i s_i) is 1.

More generally replace (s_i) by (s_i+u_i). Then (\tau_i'=\tau_i+\chi u_i). The pushout extension has local lift represented by (s_1\otimes s_2); its transition is

\[
t=u_1\tau_2+\tau_1u_2+\chi u_1u_2.
\]

The pullback has a local lift represented in the tensor module by

\[
w=\chi s_1\otimes s_2-\tau_1\otimes s_2-s_1\otimes\tau_2,
\]

with quotient coordinate 1. Direct substitution gives transition (-t). These signs are checked independently in the code, with all basis-change matrices displayed. For (E_2) split, (\chi=0), and (\tau_1=\tau_2=1), the two extension classes are (e) and (-e). They are unequal because (2e\ne0). A morphism inducing the identity on the endpoints would be an isomorphism and would equate these classes. Therefore no such morphism exists.

The conclusion refutes that particular universal strict comparison, not the existence of either extension, the earlier pushout multiplication on scans 67–80, or every possible sign-adjusted comparison. For a shear (k) between local lifts, the gluing equation is (k'-k=2t). The candidate (k=\delta\tau_1\tau_2) has defect ((\delta\chi-2)t), explaining the condition already found in the fourth tensor column.

## 3. The quadratic algebra and its tensor image

For a commutative ring (R), let (A_i=R[u_i]/(u_i^2+b_i u_i+c_i)), and set

\[
V=2u_1u_2+b_2u_1+b_1u_2,\quad b=b_1b_2,
\quad c=b_1^2c_2+b_2^2c_1-4c_1c_2.
\]

Reduction by the two monic relations gives (V^2+bV+c=0) over the integer polynomial ring. Also (b^2-4c=(b_1^2-4c_1)(b_2^2-4c_2)). The abstract algebra (A=R[U]/(U^2+bU+c)) is always free of rank two. The algebra map (i:A\to A_1\otimes A_2), (i(U)=V), need not be injective.

In tensor order (1,u_2,u_1,u_1u_2),

\[
i=\begin{pmatrix}1&0\\0&b_1\\0&b_2\\0&2\end{pmatrix},\qquad
q=\begin{pmatrix}2&-b_2&-b_1&b_1b_2\\0&0&0&1\end{pmatrix}.
\]

Thus 
\[
\ker i=\operatorname{Ann}_R(2,b_1,b_2)U.
\]

This follows by equating all four coefficients, so it holds over arbitrary rings. An (R)-linear left inverse exists exactly when ((2,b_1,b_2)=R): its second row supplies a Bezout identity, and conversely any such identity supplies a left inverse. Injectivity alone is weaker. Over a field, failure occurs exactly in characteristic two with (b_1=b_2=0). Over (R=\mathbb Z/4), (b_i=c_i=0), the nonzero element (2U) is killed, although the ring does not have characteristic two. Hence the source's exception at 172 is complete only with a field-like hypothesis.

For standard conjugations (\sigma_i(u_i)=-b_i-u_i), the code verifies

\[
iq=I+\sigma_1\otimes\sigma_2=T,\qquad qi=2I_A,\qquad T^2=2T.
\]

The coefficient calculation on 176 gives (q(u_1u_2)=U+b_1b_2); the cancelled coefficient 2 is not retained. Under (u_i'=a_i u_i+r_i),

\[
b_i'=a_i b_i-2r_i,\quad c_i'=a_i^2c_i-a_i b_i r_i+r_i^2,
\]
\[
U'=a_1a_2U+a_1b_1r_2+a_2b_2r_1-2r_1r_2.
\]

All transformed coefficients agree exactly. Units (a_i) are required for generator changes to be isomorphisms. For (\lambda U+\mu), the multiplication matrix has trace (2\mu-\lambda b) and determinant (\mu^2-\lambda\mu b+\lambda^2c), mathematically supporting the minus branch at 190 without deciding the ink.

## 4. A perfect pairing without division by two

This resolves a precise quadratic specialization of the task on 178–188. It does not identify all of the ambiguously drawn maps in those pages.

Take (E_i=A_i^\vee), with dual bases ((x_i,e_i)) to ((1,u_i)). Let (B=A_1\otimes A_2), (C=E_1\otimes E_2=B^\vee). Let (S_A=A_1+_R A_2\subset B), with its consistent boundary trace (\mathrm{Tr}(1)=2,\mathrm{Tr}(u_i)=-b_i). Let (S_E=E_1\otimes Re_2+Re_1\otimes E_2\subset C), with boundary map (\pi(x_1e_2)=b_1e), (\pi(e_1x_2)=b_2e), (\pi(e_1e_2)=2e). Form the two module pushouts

\[
A=(B\oplus R)/\{(s,-\mathrm{Tr}(s)):s\in S_A\},
\quad E=(C\oplus Re)/\{(z,-\pi(z)):z\in S_E\}.
\]

Write (\varphi:B\to R) for the (u_1u_2)-coefficient and (\psi:C\to R) for the (x_1x_2)-coefficient. Define

\[
h((f,\lambda),(x,\ell e))=\langle Tf,x\rangle+\varphi(f)\ell+\lambda\psi(x).
\]

For (s\in S_A), (Ts=\mathrm{Tr}(s)(1\otimes1)) and (\varphi(s)=0). For (z\in S_E), (T^t z=\pi(z)e_1e_2) and (\psi(z)=0). These identities kill both relation submodules, including their intersections, so all four pairing blocks descend. The saved matrices verify both annihilation identities, not merely one boundary.

Choose (1_A) from the scalar summand and (U=q(u_1u_2)-b_1b_2); choose (x=q_E(x_1x_2)) and (e) from the scalar line. The induced pairing matrix in ((1_A,U)) and ((x,e)) is (I_2). It is perfect over every commutative (R). The formula uses intrinsic evaluations, conjugations and quotient maps, so compatible local descriptions glue for line bundles. The tensor pairing restricted through (i) and (q^t), by contrast, is twice this abstract pairing, since (qi=2I). Its possible characteristic-two degeneracy is not failure of abstract duality.

The raw Pro expression (f-f^{\leftrightarrow}=\mathrm{Tr}(f)1) at 178 is false if (f^{\leftrightarrow}=Tf): take (R=\mathbb Q), (b_i=0,c_i=1,f=u_1\otimes1). Then (Tf=0), the boundary trace is zero, but (f\ne0). Codex instead reads a plus and a conjugation-like superscript. The two transcriptions remain separate in Stage 4.

## 5. Formal and finite checks

A difference between two existing strict extension morphisms factors uniquely through a map from the quotient to the subobject; existence is not supplied by this observation. A compatible map of short exact sequences inducing isomorphisms on both endpoints is an isomorphism. The scalar-endomorphism triangular model has conjugation (u\mapsto(\lambda(u)+\mu(u))I-u), an anti-involution checked by multiplication; it is only a reconstruction of the unfinished (\mathcal H) paragraph on 148.

For finite projective modules, tensor duality follows locally from dual bases and glues; [Stacks, Tags 00NV](https://stacks.math.columbia.edu/tag/00NV) and [0FNJ](https://stacks.math.columbia.edu/tag/0FNJ) give the precise finite-projective/dualizability framework. This formal statement does not itself identify a novel product with its dual.

The earlier run's local groupoid has objects (\tau\in R), arrows (a:\tau\to\tau+\chi a), and product of arrows (a\sigma+\tau b+\chi ab). Target, composition interchange, associativity, symmetry and unit laws are checked as polynomial identities. An object is invertible up to isomorphism exactly when ((\tau,\chi)=R). Its automorphism group is (\operatorname{Ann}(\chi)); a Bezout equation proves multiplication by an invertible object's parameter acts invertibly on that annihilator. This is an explicitly attributed local reconstruction, not a substitute for checking global categorical identifications.

The finite grids reproduce the earlier note: over (\mathbb F_2,\mathbb F_3,\mathbb F_5), respectively 16,81,625 coefficient tuples; the tensor maps have ranks ((4,12),(0,81),(0,625)) for ranks one and two. Root-count triples are ((2,12,2),(18,45,18),(200,225,200)). Separate small-ring kernels are enumerated. These are illustrations after the universal proof. The 64 six-bit sequences, 14 listed semantic pairs, 24 reused leaves, and Sunday 17 October 1976 are also independently counted. No psychological, historical or medical proposition is certified by those counts.
