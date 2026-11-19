# Independent audit of E.2.21: the finite transfer enlargement for all CM types

Auditor: OpenAI GPT-6 Astra, elliptic_splitting agent, inherited effort. Date:19November2026. Parent and generation agent proposed the argument audited below. Verdict: the exact transfer and field-enlargement argument for E.2.21 passes.

## 1. Input retained from the two-type calculation

Let σ fix Qcm. For every finite Galois totally real field F'/Q and L'=F'(i), the common-scalar integral CM comparison gives the two-type equations of the independent E.2.20 audit. Choose s'∈A_(f,L')× with Art_(L')(s')=σ restricted to(L')^ab. Comparing types differing at identity/conjugation gives

\[
 s'/c(s')\in (L')^\times.
\]

The explicit Hilbert90 argument yields s'=b t', with b∈(L')× and t'∈A_(f,F')×. Since L' is totally imaginary, a finite principal idele has trivial Artin image: complete it by its complex infinite components to a full principal idele, and the infinite components have trivial Artin image. Consequently

\[
 \operatorname{Art}_{L'}(t')=\sigma|_{(L')^{ab}}.       \tag{1}
\]

The common scalar cancels in the comparison of the two types. This input does not itself require that the scalar have already been proved globally±1.

## 2. A finite transfer quotient with totally real field

Fix a finite Galois totally real F/Q, set L=F(i), and choose an arbitrary finite abelian extension M/L. Define the continuous finite-image homomorphism

\[
 v:\Gamma_F^{ab}\xrightarrow{\operatorname{Ver}_{F\to L}}
       \Gamma_L^{ab}\longrightarrow\operatorname{Gal}(M/L).
                                                               \tag{2}
\]

There is no requirement that M/F be abelian or Galois. Restriction from Γ_L^ab to Gal(M/L) is defined because M/L is abelian, and transfer exists for the index-two inclusion Γ_L⊂Γ_F.

For every real embedding τ of F, choose the associated complex conjugation c_τ∈Γ_F. More explicitly, extend τ to an automorphism τ̃ of Qbar and put c_τ=τ̃^{-1}cτ̃. It fixes F, has order2, and acts nontrivially on i; hence it lies outside Γ_L. The transfer formula with right-coset representatives{1,c_τ} gives

\[
 \operatorname{Ver}_{F\to L}(c_\tau)=c_\tau^2=1
       \quad\text{in }\Gamma_L^{ab}.                       \tag{3}
\]

This formula can be checked in each finite quotient and then passed to the inverse limit. Therefore every real-place conjugation belongs to ker v.

Let N/F be the finite abelian extension corresponding to ker v. Since all real-place conjugations act trivially on N, every real place of F splits into real places in N. Thus N is totally real. This uses the exact infinite-place action, rather than a comparison with an unspecified CM division field.

## 3. The real field enlargement and its norm square

Take F' to be the normal closure of N over Q. It is finite Galois and totally real: it is the compositum of the real conjugate fields of the totally real N. It contains F because F/Q is Galois. Moreover F'/F is abelian. Indeed, each Q-conjugate of N contains F, is abelian over F, and their compositum is therefore abelian over F.

Put L'=F'(i). Then L'/Q is Galois CM, L'/L is abelian, and

\[
 F'\cap L=F,\qquad F'\otimes_F L\simeq L'.                \tag{4}
\]

The intersection equality holds since L/F is imaginary quadratic whereas F' is totally real. Apply the all-type input(1) to this particular L', obtaining t'∈A_(f,F')×. The base-change identity for field norms, from(4), gives

\[
 \operatorname{Nm}_{L'/L}(t')
   =\operatorname{Nm}_{F'/F}(t')=:u
       \quad\text{inside }\mathbb A_{f,L}^{\times}.         \tag{5}
\]

This is an identity on ideles, because the determinant definition of the field norm commutes with the scalar extension F→L at every finite place.

Norm reciprocity applied to(1), followed by restriction to M, gives

\[
 \sigma|_M
   =\operatorname{Art}_{L}
        (\operatorname{Nm}_{L'/L}(t'))|_M
   =\operatorname{Art}_{L}(u)|_M.                          \tag{6}
\]

The first equality remains valid even if M is not contained in L': its compositum with L' is abelian over L', and norm reciprocity applies to that finite compositum. Here one can also use the ordinary abelian tower because L'/L is abelian and lies in L^ab.

The inclusion of the idele u from F into L corresponds to transfer. Therefore

\[
 \operatorname{Art}_{L}(u)|_M
       =v(\operatorname{Art}_{F}(u)).                      \tag{7}
\]

Finally u=Nm_(F'/F)(t') and N⊂F'. Norm reciprocity says that Art_F(u) restricts trivially to N. Equivalently it lies in ker v, by the definition of N. Combining(6)–(7) proves σ|M=1.

The extension M/L was arbitrary, so σ fixes L^ab for every finite Galois CM field of the form F(i) with F totally real.

## 4. From these fields to every CM abelian extension

Every finite CM field K embeds in some such L. One explicit construction starts with the finite Galois CM normal closure K0, writes K0=K0^+(sqrt(−δ)) with δ totally positive, and takes a finite Galois totally real F containing K0^+ and sqrt(δ). Then K⊂K0⊂F(i)=L.

For a finite abelian M0/K, the extension M0L/L is abelian: its Galois group is a subgroup of Gal(M0/K). Thus M0L lies in L^ab. Since σ fixes that field, it fixes M0. Consequently σ fixes K^ab for every finite CM field K, and hence fixes their compositum Fcm.

Combined with the already established canonical integral CM comparison for Γ_Fcm and actual complex conjugation, this supplies the proposed exact all-CM Artin image. That final assembly uses the parent's specified CM+Artin diagram. It does not imply that every element of Γ_Fcm extends integrally to all abelian varieties or to the full pure diagram.

## 5. Primary source verification

The transfer definition, PropositionV.3.18 and the extension-of-ideals/transfer Artin diagram were independently opened in Milne, *Class Field Theory*,v4.03(6August2020), printedp162, at https://www.jmilne.org/math/CourseNotes/CFT.pdf (turn815839524view0/1). The local inclusion/transfer diagram is LemmaIII.3.2, printedp107, in the same opening. The global Artin product and norm diagram are PropositionV.5.2, p178; principal-idele reciprocity is TheoremV.5.3, p179 (turn141097007view0). The local diagrams, global product and continuity identify finite-idele inclusion with the profinite transfer used in(2) and(7).

The CM-type determinant-norm identities and existence of every CM type are exactly those independently opened and checked in `work/elliptic_audit_cm_types.md`; no new CM reciprocity convention is introduced here.

## 6. Audit verdict

The proof passes. In particular, passing to the finite field N attached to the **specific** finite quotient(2), and then to its totally real normal closure, removes the apparent residual2-torsion in a single-field transfer/commutator intersection. No assertion about that intersection vanishing in isolation is needed. All field inclusions, reciprocity maps, principal-idele changes and base-change norms used in the enlargement have been specified and checked.
