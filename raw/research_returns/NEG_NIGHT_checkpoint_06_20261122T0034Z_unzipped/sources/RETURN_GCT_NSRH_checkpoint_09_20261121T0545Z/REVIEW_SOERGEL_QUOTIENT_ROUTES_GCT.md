# Independent whole-proof review: F59 quotient-route tests

Reviewer: /root/gct_statements, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC, approximately 05:32.

## Verdict and frozen scope

**PASS on the complete mathematics and source-normalization scope.** I read the entire report, independently reconstructed both constructions and every displayed cohomology/Tor calculation, and freshly read the original ordinary Soergel shift/reflection context. No mathematical correction is required. A formatting-only control character in QR6 was reported to the author; it has no mathematical effect and its corrected hash will be recorded below.

Target: `agent_soergel_quotient_route_tests.md`, SHA256 `77ca49fbc4f16db2a19b6f6e13d8124e77c1d639486bf1432c6950f58f50e478`.

This is a full mathematical proof review and primary-text check. I did not run a proof assistant, symbolic program, numerical test, or PDF compile for this target. No final-fragment match is claimed until the generated fragment is supplied and read.

## 1. Actual coinvariant normalization and Frobenius duality

For A=k[x,y], degrees two, the full independent-reflection invariant ring is S0=k[x²,y²]. Its central fiber is B=k[x,y]/(x²,y²), with basis1,x,y,xy and Hilbert polynomial (1+v²)². The coefficient-of-xy pairing is nondegenerate and symmetric; its degree is -4. This gives B≅B^*<4> and Hom_B(M,B)≅Hom_k(M,k)<4> with the appropriate right action. The resulting B-duality is exact; no ordinary regular-ring projectivity inference is being used over this nonregular B.

I checked the source shift convention directly: B(1)^i=B^{i+1}, so (1) lowers displayed internal degree by one. The ordinary reflection object is A⊗_{A^s}A(1), with cyclic generator degree -1. For the two independent reflections, eliminating the middle x and y coordinates identifies their product with (A⊗_{S0}A)(2). Reducing the central S0 variables gives exactly L0=(B⊗_k B)<-2>. Thus the shift in the countermodel is the actual longest-object normalization, not a numerical choice made to force its Euler polynomial.

## 2. The bounded bifree quadratic is an actual chain comparison

The map x:B<2>→B has internal degree zero, with terms in cohomological degrees -1 and0. Its kernel is (x)<2>≅T<4> and its cokernel is T=B/(x). Adding K and K[1] to B produces the report's complete cohomology table for L, namely T<4> in degree-2, T<4>⊕T in degree-1, and B⊕T in degree0.

L and its B-dual are bounded free complexes on their respective sides. Therefore Z⊗_B^L Z is computed by the ordinary tensor complex. Reassociation gives L⊗_k(L^∨⊗_B L)⊗_k L^∨ with total shift-4; moving the middle scalar k-complex past L by the actual Koszul symmetry gives E⊗_k Z. The two outer B-actions stay on L and L^∨, so the comparison is a B-bimodule chain isomorphism. This check uses the full tensor expression, not merely equal Euler dimensions.

The termwise free-rank Euler polynomial of L is1 because the summands K and K[1] cancel. Dualizing reverses internal and cohomological degrees, leaving its free-rank Euler polynomial1 as well. Consequently E has actual k-Euler polynomial v^-2 h_B=δ², and Z has v^-2 h_B², of Euler dimension16. The report correctly makes no acyclicity claim from these Euler cancellations.

## 3. Both nonprojective cohomology calculations

Exact Frobenius duality gives Hom_B(T,B)=(x)≅T<2>. Applying it to the complete L table reverses cohomological degrees and yields exactly QR11, including the T<-2> shifts from dualizing T<4>.

Kunneth over k gives H^-2(Z)=T<4>⊗_k(B⊕T<2>)<-2>. As a left module it is T<2>⊕T<4>^3⊕T<6>^2. It has dimension12, is nonzero and is annihilated by x, which cannot happen to a nonzero finite free B-module. Since B is local, finite projectives are free; the report supplies the usual residue-basis/splitting/Nakayama argument. Hence this group is nonprojective and nonflat.

The right extreme H²(Z) is (B⊕T)⊗_kT<-2><-2>, giving T<-4>²⊕T<-2>³⊕T, again nonzero and annihilated by right x. This proves the corresponding right-side failure. Convolution of the ungraded dimension lists (2,4,6) and(6,4,2) gives (12,32,56,32,12), whose alternating sum is16. All these are actual cohomology calculations, not deductions from total Euler data.

## 4. The countermodel does not have the designated target class

Every term of Z is a sum of shifts of B⊗_k B. Its termwise split-Grothendieck Euler class is [L0], because the two free-rank Euler polynomials are1. The designated reduced nonstandard expression is instead 2[L0]-δ[Bbar1]-δ[Bbar2]+δ²[B].

I independently checked the separating additive invariant H(M)=Hilb Hom^bullet_{B-B}(M,B). These cyclic bimodules impose only relations already satisfied by the equal left and right actions on the commutative target B, so any image of the generator gives a bimodule map. Their generator degrees0,-1,-2 give h_B,vh_B,v²h_B, respectively. A source shift(1)=<-1> raises the degree of such a map by one, agreeing with multiplication by v in this additive invariant. Therefore the target-minus-longest image is

`(v²-2δv+δ²)h_B=v^-2h_B=δ²≠0`.

This proves the class distinction without assuming that reduction is injective on a Grothendieck group. It is the essential boundary: the construction invalidates the proposed numerical-only projectivity criterion, not a statement retaining the designated ambient target class.

## 5. The complete periodic Tor computation

The diagonal-involution invariant ring S_tau=k[a,b,c]/(ac-b²), with a=x²,b=xy,c=y², is different from S0. Its normal form and the even/odd decomposition A=S_tau⊕M are correct. Coprimality in k[x,y] proves that every even-coefficient relation px+qy=0 has p=yh,q=-xh with h odd; writing h=xu+yv with u,v even gives exactly the two columns of Phi=[[b,c],[-a,-b]]. This proves the full presentation, not just two visible relations.

Over the polynomial ring R=k[a,b,c], Phi²=-(ac-b²)I. If a kernel vector modulo f=ac-b² lifts to w with Phi w=fz, multiplication by Phi gives -fw=fPhi z. Cancellation in the polynomial domain yields w=-Phi z. Thus the same Phi gives an exact infinite free resolution over S_tau, with successive shifts2+4i. This is a direct proof of exactness; no unquoted hypersurface-resolution theorem is needed.

After tensoring with A, Phi_A=(y,-x)^T(x,y). Its kernel is A(y,-x)^T by the coprime syzygy of x,y, and its image is (x,y)A(y,-x)^T. Every positive homology is therefore one copy of k, with internal degree(2+4i)+2=4+4i. Since the even summand S_tau has no positive Tor, the same groups compute Tor_i^{S_tau}(A,A). Fixed spectator variables give A/(x,y) in the same shifts by the same calculation.

Thus the full derived singular correspondence has nonzero cohomology in every negative degree and cannot be quasi-isomorphic to a bounded complex. This does not identify it with the underived module, does not replace the actual target by a generic fiber, and does not exclude every different bounded nonflat/nonflat construction.

## 6. Fresh primary-source check and retained framework scope

I freshly read the whole original Elias--Williamson sections3.3–3.4, printed pp1105–1106, including the Hom grading, shift convention, reflection definition, generators of degrees-1/+1 and Bott–Samelson tensor normalization. These support exactly the ordinary shifts used here.

Primary paper: Elias–Williamson, *The Hodge theory of Soergel bimodules*, Annals of Mathematics180(2014),1089–1136, DOI https://doi.org/10.4007/annals.2014.180.3.6.

- `primary_sources/Elias_Williamson_Hodge_2014.pdf`, SHA256 `f704e80c427362c5714759e14fdd5ec8c20aa4050a68c2397df3873b999df68f`.
- `primary_sources/Elias_Williamson_Hodge_2014.txt`, SHA256 `91ca829296dbcd4c853c7345db5985f976cdfb2b720317b8ed0dc52b39fc29d0`.

I used the local original text; I do not claim a new visual PDF inspection. The EGA/SGA references remain the previously checked module/perfect-complex/action framework, not asserted proofs of the new explicit computations. The scope paragraphs correctly preserve the remaining designated-class, invariant-descended, nonflat/nonflat coefficient problem.

Only this review file was written. No target report, fragment, root master paper or shared check log was edited.

## 7. Corrected report and complete final-fragment match

I directly checked the QR6 formatting correction: the literal carriage-return character has been replaced by the intended `\rm`. Final report SHA256 is `d50900b1353ce0c01b43832283e7ea9464d976dac2e7853f7053004ee9014e9e`; there is no mathematical change.

I then read all 377 lines of `finding_F59_quotient_tests.tex`, SHA256 `020c4280c86e8da3297f7629675069cebf4f9e9fc632da7b8d77c36f9f3e3c28`. Full report-to-fragment match is **PASS**. The actual chain isomorphism, exact free-rank Euler cancellation, both cohomology tables and nonprojective extreme groups, additive Hom-class separation, complete presentation/exact periodic resolution, all positive Tor shifts and distinct invariant-ring scopes are present. The added explicit sentence that internal grading alone supplies no arithmetic purity is correct. The separate F59 dictionary and the remaining designated-class/nonflat route are accurately retained.

This final match is a direct whole-text mathematical check, not a reviewer compilation or visual PDF inspection. No correction is needed.

### Final environment-name delta

The author identified the change from the initially advertised fragment hash: two undefined proposition environments were replaced by the existing finding environment, with the explicit F59 titles and retained labels; the corresponding textual reference now says Finding. No proof changed. I read the entire current fragment again after receiving that explanation. Final whole-fragment match remains **PASS** at SHA256 `a6a354fc2ae0cb7f198709a746dd6ab648bb8ce7463c13f2b78d3cb4e3948265`. The author separately reports a successful four-page compile; I do not claim that compile as my own verification.
