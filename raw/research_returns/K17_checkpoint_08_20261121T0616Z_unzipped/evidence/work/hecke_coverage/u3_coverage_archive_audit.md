# Independent audit of compact U(3) coverage

Finding **K17-U3-COVERAGE**. Date: 2026-11-21 UTC. Checker: `/root/archive_kummer`, GPT-6 Astra Pro. **PASS for the stated automorphic coverage theorem, with the explicit Shin temperedness citation and the principal-series proof chain recorded below.** No Hecke-neighbor execution, class-number assertion, source Galois/automorphic translation, or K-group conclusion is certified by this audit.

## 1. Reviewed statement and proof

Read all of `u3_coverage_proof.md` and all of `u3_coverage_section.tex`, then independently reconstructed the proof. The statement concerns a conjugate-self-dual cuspidal representation of \(\mathrm{GL}_3(\mathbb A_E)\), \(E=\mathbb Q(\sqrt{-3})\), unramified at every finite place and with infinity parameter \(((z/\bar z)^6,1,(z/\bar z)^{-6})\). It asserts occurrence on the compact standard Hermitian unitary group, at the full standard lattice level and highest weight \((5,0,-5)\), with multiplicity one.

The source-branch interface is explicitly separate in the theorem. I did not infer its hypotheses merely from the existence of a definition named `Adm3`, nor audit that entire interface as part of this review.

## 2. Global theorem, sign, and multiplicity

Freshly read KMSW arXiv:1409.3731v3, §0.3.3 pp.17–18; §1.2.3 and Lemma1.2.5 pp.59–61, including the printed proof; Propositions1.3.1 and1.3.3 pp.67 and70–71 and the intervening complete parameter/component-group definitions; §1.7 pp.88–89; and the complete Theorem5.0.5 with its preceding hypotheses and printed proof on p.206.

The sufficient unconditional global theorem is indeed Theorem5.0.5: the preceding paragraph explicitly verifies both required local inputs for generic global parameters and pure inner twists. The unrestricted starred Theorem1.7.1 is not used. A Hermitian space over \(E\), rather than a division algebra over \(E\), gives a pure inner form by the exact paragraph on p.18. In odd dimension the nonsplit finite local unitary group is unique up to isomorphism; the global standard positive definite space is therefore quasi-split at every finite place and compact at infinity.

Each character \(\rho_k(z)=(z/\bar z)^k\), for \(k=6,0,-6\), is its own conjugate dual. An invariant conjugate pairing between the \(k\) and \(j\) spaces requires \(k=j\). Also \(\rho_k(-1)=1\), so its one-dimensional conjugate-dual pairing has positive sign. Since the characters are distinct, all three multiplicity spaces have dimension one; a nondegenerate negative-parity pairing is impossible. Propositions1.3.1 and1.3.3 therefore force positive global sign, which is the untwisted standard embedding in rank three.

The global parameter is simple and generic. The explicit component-group calculation on pp.69–70 gives trivial reduced component group. The product formula on pp.88–89 removes the unreduced central character. Hence arbitrary local packet choices at the specified inner form are permitted, and Theorem5.0.5 gives multiplicity one. There is no residual global packet-parity restriction.

Bellaïche–Chenevier, *Families of Galois representations and Selmer groups*, RemarkA.11.8 p.236, was read in full. Its explicit infinity criterion gives a unique discrete parameter for the three distinct integral exponents and relevance to every real inner form, including the compact form. Adding \(\rho=(1,0,-1)\) to the compact highest weight \((5,0,-5)\) gives \((6,0,-6)\), as needed. The surrounding hypothetical global Langlands-group discussion is not used.

## 3. Closing the bounded-packet scope precisely

KMSW Proposition1.5.2(5), read in context on pp.78–79, initially concerns Arthur/bounded packets. The general nonbounded extension is described in their §1.6.4 pp.86–88, which I also read completely, but no nonbounded-packet inference is necessary here.

The stated infinity parameter is regular algebraic: at each complex embedding its infinitesimal character is that of the algebraic highest weight \((5,0,-5)\), after adding the usual half-sum of positive roots. Thus the representation is cohomological. Shin, *Galois representations arising from some compact Shimura varieties*, Annals173 (2011), **Theorem1.2 and Corollary1.3, pp.1647–1648**, apply: the field is CM, the representation is conjugate self-dual and cuspidal, and rank three is odd, so no extra slight-regularity condition occurs. Every finite local component is tempered. I freshly read the complete theorem/corollary and the complete printed proof of its later form, **Corollary7.9 p.1728**. The primary PDF is saved as `shin_compact_2011.pdf` in this directory:

<https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p09-p.pdf>.

Consequently the inert-place spherical-packet assertion falls literally within KMSW Proposition1.5.2(5). The unramified extension of the base-change parameter has trivial inertia because the extension is unramified and the restricted parameter has trivial inertia. For example its inverse-stable determinant-one eigenvalues can be written \(\{a,1,a^{-1}\}\); the standard unramified unitary parameter with Frobenius dual component \(\operatorname{diag}(a,1,1)\) restricts to this multiset. The same parameter is the localization of the global parameter by injectivity in Lemma1.2.5. The standard selfdual lattice is hyperspecial, including at the inert prime two. Split places are ordinary \(\mathrm{GL}_3\) spherical representations.

The author and parent were sent this precise Shin citation for insertion. It also makes the lifted unramified \(\mathrm{GL}_3\) principal series at three irreducible immediately: all inducing characters are unitary, whereas the exceptional reducibility ratios have absolute value different from one. Thus the proof need not rely on an unexamined stronger generic-spherical assertion.

## 4. The ramified place three

Freshly read Adler–Lansky, arXiv:0807.1528, the full relevant setup in §4.1 pp.10–11, §4.2.1 pp.11–12, the entire principal-series part of §4.4 pp.14–15, §4.5 p.16, §6.1 p.21, and §7.1 p.28, including the printed proof.

The central-character argument is correct: finite unramifiedness and trivial infinity character force the central character to factor through the class group of the Eisenstein integers, which is trivial. Thus the local unramified Frobenius multiset is inverse-stable with determinant one, hence \(\{a,1,a^{-1}\}\), allowing repetitions and \(a=-1\).

The proposed torus character has \(\lambda_1=\chi\) unramified and \(\lambda_2=1\) in the actual formula(4.4.1). Its stable lift is \((\chi,1,\chi^{-c})=(\chi,1,\chi^{-1})\). The complete reducibility list leaves only the nontrivial unramified quadratic character as a possible reducible case. The absolute-value case is incompatible with the irreducible tempered GL principal series. The case involving \(\omega_{L/F}\) is impossible because it is ramified on units, whereas the restriction of \(\chi\) is unramified. In the remaining quadratic case both constituents lie in one packet, with the asserted stable base change by Propositions6.1 and7.1.

There is a useful source nuance: §4.5 says the paper assumes Hypothesis1.5 on depth preservation throughout. I therefore followed the principal-series proof back rather than silently dropping that hypothesis. The earlier Adler–Lansky paper, arXiv:math/0601695v1, **Proposition5.1 and its complete proof, printed pp.19–20** (the published numbering referenced by the ramified paper is Proposition4.1), derives precisely cases(i),(iii),(iv) directly from Rogawski Proposition4.10.2 and the paragraph before Theorem13.2.1. No depth-preservation assumption, finite-field character comparison, or lower bound on residue size enters that argument. The principal-series packet list is likewise explicitly attributed to Rogawski §12.2. This verifies the needed independence from Hypothesis1.5 and from the separate supercuspidal exclusions \(q>3\), \(q\ne7\). It was sent to the author as an exact explanatory citation, not as an unresolved mathematical objection.

The lattice comparison was reconstructed: a unit square root of \(-2\) in \(\mathbb Z_3\) gives an integral primitive isotropic vector; pairing with an integral vector and dividing its norm by two produces an integral hyperbolic plane. The complement has unit norm \(d\), with \(-d=N(\det B)\), and scaling by \((\det B)^{-1}\) gives norm \(-1\). This proves an integral isometry with the displayed Adler–Lansky Gram matrix. Their stabilizer at \(y\) is the full standard lattice stabilizer, whose reduction is \(O_3(k)=SO_3(k)\times\{\pm1\}\).

The full-stabilizer fixed-vector argument is correct. Iwasawa decomposition at this special vertex gives \(G=BK\); it can also be seen directly because the same integral hyperbolic-plane construction makes \(K\) transitive on isotropic lines. The torus factor of \(B\cap K\) has \(\alpha\in O_L^\times\), so \(\lambda\) is trivial there, and the modulus is trivial on a compact subgroup. Thus the induced representation has exactly one \(K\)-fixed vector. Exactness of compact-open invariants over \(\mathbb C\) puts a nonzero fixed vector in an irreducible constituent of the required packet. No passage from connected-parahoric fixed vectors to full-stabilizer fixed vectors is being assumed.

## 5. Assembly and limits

The selected finite members and the compact infinity member form a restricted tensor product in the simple global packet. The proved generic pure-inner multiplicity formula places it in the discrete spectrum with multiplicity one. Compactness at infinity and anisotropy modulo center give exactly the corresponding algebraic modular forms at this coefficient and full lattice level.

This completes the stated coverage theorem after the explicit citation clarifications above. I did not reread the entire trace-formula construction, reproduce the local classification from scratch, or use the corroborating Pappas–Rapoport/Zhu passages as additional necessary hypotheses. I did not check the parent-owned source-conductor interface or infer a numerical trace/K-group conclusion from coverage alone.

## 6. Final revision readback

The author inserted both precise citations. I read the entire original TeX and then every changed passage plus both new bibliography entries. The resulting reviewed TeX has SHA256 `4b3f91bab7b67b6408dd5facd06b69313be16d7ad2029b42ce427dc5805f0790`; the corresponding MD has SHA256 `b74a560ce4c45117c82b4977b35f67a47a890cfadce25a2563d1b93ffca7ffd1`. The review verdict is **PASS with those refinements incorporated**, not a request for a new arithmetic hypothesis.
