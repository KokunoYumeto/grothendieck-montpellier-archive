# Full peripheral and arithmetic transport after E.2.30--31

19 November 2026. This note records the actual maps investigated after the proper-completion theorem and its one-cusp counterexample. No closure or strict reduction of the main E.2 gate is asserted here.

## FP1. The relative lifting map actually required

Let G=Fhat_2 with specified generators x,y and z=(xy)^(-1). Write Aut_per,1(G) for actual continuous automorphisms taking each of x,y,z to a conjugate of itself. Let pi:G→A5 be the actual quotient from E.2.29, R=ker pi, and P=G/closure[R,R]. Its kernel over A5 is the completed original affine lattice Lhat.

The exact relative map relevant to a finite construction is

\[
 \{\alpha\in\operatorname{Aut}_{\mathrm{per},1}(G):
        \pi\alpha=\pi\}
 \longrightarrow
 \{\gamma\in\operatorname{Aut}(P):
       \gamma|_{A_5}=1,\ 
       \gamma(t)\sim_P t\ (t=x,y,z)\}.
 \tag{FP.1}
\]

The matrices in the reverse-A5 construction define an element of the right-hand group after the rescaling below. Bleher--Chinburg--Lubotzky Corollary2.4, original v3 p5, supplies a preimage in the larger group of all continuous automorphisms of G preserving the quotient kernel. Its proof uses a generating-set lift from Gaschutz; the choices in that proof are not specified to belong to the three prescribed conjugacy classes. A preimage in the left-hand side of (FP.1) has not been constructed in this work. Nor has a preimage in the much smaller specified arithmetic image iota(Gal(Qbar/Q)) been constructed.

This is an exact additional map to solve; no blanket claim about unrelated relative lifting theorems is being made.

## FP2. All three peripheral classes at the actual one-cover quotient

This calculation uses the actual extension, not only its abelian kernel. Retain N=N_rev from work/A5_reverse_boundary_shear.md. Thus N is integral, N^2=0, N(B)=0, its image lies in the integral boundary lattice B, and AN=0 for the actual base exponent map. Let c be the actual section factor set and b0(h)=sum_k c(h,k), so delta b0=60c.

For a in Zhat with a_2=0 and a_p=1 for odd p, define

\[
 \gamma=I+3600aN,\qquad\eta(h)=60aN b_0(h).
 \tag{FP.2}
\]

The map on the actual extension coordinates is

\[
 (m,h)\longmapsto(\gamma m+\eta(h),h).
\]

The identity delta eta=(gamma−I)c proves it is an automorphism; its inverse follows from N^2=0. It fixes the original boundary lattice pointwise, has identity action on the original proper quotient, and is IA on the base. Its affine matrix is nonintegral because the entry N[0,1]=−1 gives the noninteger coordinate −3600a.

For a specified t in {x,y,z}, let d be its order in A5, so d is3 or5. Write t=(m_t,h_t), using the same fixed section. Under the unscaled integer map gamma0=I+60N, eta0=N b0, its displacement in L is

\[
 w_t=60N m_t+N b_0(h_t).
\]

The element t^d is its actual cusp boundary cycle. Since N kills B, this extension automorphism fixes t^d. The elementary formula for powers in an abelian-by-finite extension therefore gives

\[
 (1+h_t+\cdots+h_t^{d-1})w_t=0. \tag{FP.3}
\]

Put S_t=sum_(j=0)^(d−1) j h_t^j w_t. The literal telescoping identity is

\[
 (h_t-1)S_t=d w_t.
\]

The displacement for (FP.2) is 60a w_t. Since d divides60, the actual vector

\[
 v_t=-\frac{60}{d}\,a S_t\in\widehat L
\]

satisfies (1−h_t)v_t=60a w_t. Conjugation by v_t sends t to the image of t under (FP.2). This proves preservation of all three peripheral element conjugacy classes in P itself. The product relation xyz=1 is already preserved because (FP.2) is an actual extension automorphism. The map (FP.1), its compatibility over all covers, and its arithmetic preimage remain to be established.

## FP3. The precise tangential alignment issue

For an actual peripheral automorphism alpha satisfying all proper integral lattice conditions, E.2.30 proves that its global aligning conjugators form one orbit H_c h0. The equality C_G(x)=x^Zhat⊂H_c has the following exact consequence when alpha(x)=x:

an aligning inner adjustment ad(h)alpha also fixes x exactly when h lies in C_G(x). Such an h exists in the aligning orbit exactly when h0 lies in H_c, equivalently when alpha already preserves H_c.

Proof: an intersection H_c h0∩C_G(x) is nonempty if and only if h0 belongs to H_c C_G(x)=H_c. The final equivalence follows from the self-normalizer of H_c in E.2.30. Thus one cannot silently use the existence of an arbitrary aligning conjugator to retain a chosen tangential normalization. E.2.31 shows the analogous one-cusp membership test does not remove this freedom.

## FP4. Solenoid theorems and their actual input maps

Opened original primary Bering--Studenmund, *Topological models of abstract commensurators*, EMS2024 online-first PDF, DOI10.4171/GGD/786, https://ems.press/content/serial-article-files/47388. Exact Theorem4.5 p9, Proposition5.4 and Lemma5.5 pp11--12, and Theorem5.6/proof pp12--13 were read.

For a finite connected aspherical CW model X, Theorem5.6 identifies pointed homotopy self-equivalences of the full finite-cover solenoid with Comm(pi1 X). Its proof uses the actual map

\[
 \operatorname{Aut}_{\mathrm{pro\text{-}Htop}_*}\{X_H\}
  \xrightarrow{\pi_1}
 \operatorname{Aut}_{\mathrm{pro\text{-}Grp}}\{\pi_1(X_H)\}
  \simeq\operatorname{Comm}(\pi_1X),
\]

with a termwise aspherical-space correspondence between pointed homotopy maps and discrete group homomorphisms. Applying it here requires actual compatible homotopy maps between the covers, or equivalently the discrete group maps appearing in that display. The integral maps on compactified H1 constructed in E.2.30 do not by themselves supply those maps in the argument. The unresolved object is the lift of the specified actual alpha to that displayed pro-homotopy automorphism, not an abstract comparison of group names.

Opened original Dzambic--Gonzalez-Diez arXiv2006.02817v1, https://arxiv.org/pdf/2006.02817. Section4.1 and Propositions8--9 pp15--16, Theorem10 p17, were read. It constructs the coordinatewise algebraic map of solenoids

\[
 (q_n)_n\longmapsto(\sigma(q_n))_n
\]

and conjugates each algebraic inverse-system automorphism by it. The proof of Proposition9 obtains the new holomorphic maps by applying sigma to the defining equations. This gives an isomorphism of the completed holomorphic commensurator groups and maps the actual profinite deck group onto the conjugate one. It does not produce the pointed continuous homotopy self-equivalence required in the preceding display; the source explicitly discusses the failure of continuity of the coordinatewise point map in Section4.1 p15.

For the present quartic-moving sigma, that continuity obstruction can also be checked directly. A continuous field automorphism of C is identity or complex conjugation: it fixes Q, hence R by density and continuity, and sends i to ±i. Such an automorphism fixes every real algebraic number. Our sigma moves two real quartic roots, so any extension to C is discontinuous. If its coordinatewise map on a compact curve solenoid were continuous, write pi for the first projection, choose a nonconstant algebraic map lambda:C→P1 and its conjugate lambda_sigma:C_sigma→P1, and use lambda_sigma∘pi_sigma∘sigma_sol= sigma_P1∘lambda∘pi. The left side would be continuous, and lambda∘pi is a continuous surjective quotient map from a compact space to P1. This would force sigma_P1 to be continuous. Thus the canonical pointwise map cannot serve as the requested continuous lift. A different continuous homotopy representative remains a separate construction to be proved.

## FP5. Proper Reidemeister pairings retain the actual-loop premise

Reopened Boggi--Zalesskii original arXiv1111.2373v5,13June2024, https://arxiv.org/pdf/1111.2373. Definition2.1 pp2--3 and Theorem2.3/Corollary2.4 p4 use actual closed curves gamma on the given surface; their elevation modules are the integer spans of actual lifted loops. Theorem3.3 pp6--7 produces a cover in which elevations of a specified non-power nonperipheral closed curve become nonseparating simple loops.

For the proposed application, the required input is an actual discrete curve representative for the conjugacy class alpha(gamma), compatible with the original surface. The completed homology classes of its powers and lifts are already well-defined, and all cup/intersection pairings are preserved by an actual cyclotomic-kernel Galois action. Promoting that finite-cover information to the actual-loop input of the cited theorem is precisely the missing map. Neither the source theorem nor the construction of E.2.30 is being used as a substitute for it.

## Current gate

The complete all-cover proper premise is the actual conjugacy-stabilizer condition of E.2.30 inside the arithmetic Galois image. No passage to all affine lattices, no relative peripheral lift over every cover, and no discrete solenoid or mapping-class representative has been established in this note. E.2.31 refutes one proposed intermediate implication. FP2 verifies that the three peripheral conditions at one actual quotient still allow the nonintegral boundary block. These are precise route checks; the main E.2 status remains unchanged.
