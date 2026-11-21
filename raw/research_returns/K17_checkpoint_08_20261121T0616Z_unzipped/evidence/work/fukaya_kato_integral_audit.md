# Independent check: Fukaya–Kato's integral conclusion and the reflected character

Reviewer: /root/tripod_integral, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**PASS for the source chain inspected here.** I independently read the entire proof of Fukaya–Kato §10.2.3 and its supporting Lemma 10.2.2, the entire Fitting/characteristic argument in §7.1.3, the finite-level passage in §§7.1.8–7.1.10, and the statements and assumptions of Theorems 7.2.3 and 7.2.8. I also read Wake–Wang-Erickson Proposition 2.2.6 and its proof, Corollaries 5.1.1–5.1.2 and their proofs, the running character assumptions, and the Stickelberger observation in the proof of Lemma 5.2.7. The proposition's distinction between the ramified module frakX and the unramified module X was checked visually on the author's PDF p.4.

This audit treats the established deeper inputs of those papers as cited theorems. It is not an independent reconstruction of their entire modularity and regulator arguments. The standard implication from level-one Vandiver to vanishing of the whole plus Iwasawa module is being separately checked by /root/archive_kummer.

## 1. Why the conclusion is integral, including repeated roots

Use FK notation

    P = (H_theta^- / I_theta H_theta^-)/(p-primary torsion),
    A = (Lambda_theta/(xi))[1/p],
    S = X_(Np-infinity,chi),
    f = Upsilon o varpi : P -> P.

The hypothesis C(h) and FK §7.2.10 give P[1/p] free of rank one over A. Consequently every A-linear endomorphism of this module, including 1−f, is multiplication by an element a of A. The derivative identity of Theorem 7.2.3 gives xi' a=0.

After extending scalars to split the relevant polynomial, each local factor of A is L[t]/(t^n). The derivative of a polynomial with a root of multiplicity n is a unit times t^(n−1) in that factor: the scalar n is nonzero and invertible in characteristic zero. Thus xi' a=0 forces a to belong to (t), the nilpotent maximal ideal. This proves the nilpotence conclusion of FK Lemma 10.2.2 even when roots repeat. No inverse of xi' on the entire ring is asserted.

Choose N with (1−f)^N=0 after tensoring with Q_p. The lattice P has no p-torsion, so its map into P[1/p] is injective. Therefore (1−f)^N=0 already as an integral endomorphism of P. The finite sum

    1 + (1−f) + ... + (1−f)^(N−1)

is an integral inverse to f. This is stronger than saying that f has finite cokernel. There is no denominator or saturation step being silently discarded.

For completeness, the passage from invertibility of f to invertibility of both maps is as follows. Replace Upsilon by f^(-1) Upsilon, obtaining an actual left inverse to varpi. Hence S is the direct sum of varpi(P) and a module K. FK §7.1.3 proves Char(P) subset (xi), while the main conjecture gives Char(S)=(xi). The direct-sum equality forces Char(K)=(1), so K is finite. The source S has no p-torsion, and hence its finite submodule K vanishes. Thus varpi is an integral isomorphism and the original Upsilon is also an integral isomorphism. Their being mutually inverse is a stronger assertion not needed for cup-product surjectivity.

This checks exactly FK Theorem 7.2.8, which concludes the isomorphisms and finite-level cyclotomic-symbol generation under C(h). Simplicity of roots is an alternative sufficient hypothesis, not an additional requirement in this argument.

## 2. Reflected-character bookkeeping in Wake–Wang-Erickson

Take tame level N=1 and p>=5. Fix an allowed even character theta, so theta is neither 1 nor omega^2, and put

    chi = omega^(-1) theta,
    theta' = omega^2 theta^(-1) = omega chi^(-1),
    chi' = omega^(-1) theta' = chi^(-1).

The reflected theta' is even, nontrivial, and different from omega^2. Thus it satisfies the same running assumptions. If X^+=0, both X_theta and X_theta' vanish.

Apply Proposition 2.2.6 to theta'. Its rank-one free ramified module is

    frakX_(chi'^(-1))^#(1) = frakX_chi^#(1).

The sharp involution and Tate twist transport the action along isomorphisms of the relevant Iwasawa algebra components, so preserve freeness and cyclicity. The natural ramified-to-unramified quotient then makes X_chi cyclic. The original X_theta=0 and this cyclicity satisfy Corollary 5.1.1, which gives the cuspidal Hecke algebra Gorenstein, and Corollary 5.1.2, which states that varpi is an isomorphism. Its proof explicitly invokes FK C(h) and Theorem 7.2.8. No extra class-group cyclicity assumption remains after all-plus vanishing.

The excluded theta=1 and theta=omega^2 correspond respectively to chi=omega^(-1) and chi=omega. The proof of WWE Lemma 5.2.7 explicitly records that these unramified Iwasawa components vanish by Stickelberger, using B_2=1/6. FK §7.2.14 independently describes the corresponding Eisenstein quotients as zero.

## 3. Finite level and the exact odd cup condition

FK Conjecture 7.1.8, which Theorem 7.2.8 proves under C(h), is explicitly generation by cup symbols of two cyclotomic p-units. Sections 7.1.9–7.1.10 identify and specialize its target. At r=1 and N=1 the mod-p target is

    H^2(O_F[1/p], F_p(2))_theta
      = (A_F/p A_F tensor mu_p)_theta,
    F=Q(mu_p).

The two exceptional theta components just discussed are zero. Therefore all of the plus target is generated by these unit cups. Under Vandiver, A_F has only minus part, so the entire twisted target is plus.

Now use the already independently checked parity lemma. The minus part of p-units modulo p is the one-dimensional mu_p. Mixed plus/minus cups have zero target, and the alternating pairing on the one-dimensional minus part is zero for odd p. Hence the plus p-units alone supply the full target. Untwisting each H^1(mu_p) by mu_p gives the odd part of H^1(F_p). This is exactly the cup-surjectivity hypothesis of K17-POLE-GENERAL.

For the relation character convention, an actual Galois generator x_a has character omega^a, its Kummer dual has character omega^(1−a), and a relation of character omega^e has twisted cup target theta=omega^(2−e). Thus chi=omega^(1−e), and the reflected theta' is omega^e. All parity and reflection signs agree.

Consequently the inspected source chain, together with the separately checked Vandiver-to-Xplus step, removes the extra cup hypothesis for every Vandiver prime. The prime 3 belongs to the known odd regular case and does not require the p>=5 FK/WWE setup.

## Primary sources and exact locators

- Fukaya–Kato, *On conjectures of Sharifi*, author version dated 15 August 2012, https://www.math.ucla.edu/~sharifi/sharificonj.pdf. Local work/fukaya_kato_sharificonj.pdf and .txt. §6.1.4–6.1.5 p.76; §7.1.3 pp.84–85; §§7.1.8–7.1.10 p.86; §7.2.5 p.88; Theorem 7.2.8 and §§7.2.10–7.2.12 p.89; §7.2.14 p.90; Lemma 10.2.2 and full §10.2.3 proof p.107. Retrieval turn710454012view0, exact find results turn876640550view1, turn876640550view2, turn876640550view3.
- Wake–Wang-Erickson, *Ordinary pseudorepresentations and modular forms*, author's version dated 7 September 2017, https://sites.pitt.edu/~caw203/pdfs/opmf.pdf. Running assumptions pp.2–3; Proposition 2.2.6 p.4; Corollaries 5.1.1–5.1.2 p.11; Stickelberger observation in Lemma 5.2.7 proof p.13. The local work/wake_wang_erickson_ordinary.pdf is arXiv v4 dated 30 January 2017; corresponding statements were compared with the current author PDF. Retrieval turn848982646view0, exact find results turn928900337view0 and turn928900337view1, page-4 screenshot turn928900337view2.
- Author's publications page verifies publication metadata: *Proceedings of the AMS, Series B* 4 (2017), 53–71, https://sites.pitt.edu/~caw203/pubs.html, retrieval turn263934823view0.

The FK author version supplies the exact locators used here. Search metadata identifies the later publication in *Kyoto J. Math.* 64 (2024), 277–420, DOI 10.1215/21562261-2023-0018, but the publisher DOI page was not accessible during this check. No journal-page locator has been inferred from the preprint pagination.
