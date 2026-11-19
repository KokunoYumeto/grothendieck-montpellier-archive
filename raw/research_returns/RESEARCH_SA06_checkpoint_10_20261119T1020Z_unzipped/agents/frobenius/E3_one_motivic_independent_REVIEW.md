# Independent audit of E.3s: the large one-motivic quotient

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, /root/frobenius.

Owner file: research/agents/cycles/one_motivic_quotient.tex.

**Verdict: passed after the nonproper-parameter wording correction, now applied by the owner.**

## Primary source

Ayoub, J., & Barbieri-Viale, L. (2009). 1-motivic sheaves and the Albanese functor. *Journal of Pure and Applied Algebra, 213*(5), 809–839. https://doi.org/10.1016/j.jpaa.2008.10.002

**[OPENED]** Author version arXiv:math/0607738v2, dated 21 October 2008, https://arxiv.org/pdf/math/0607738. The version-qualified PDF request failed; the unqualified PDF succeeded, and the abstract page confirms that v2 is current. The owner's local primary PDF and text were read independently.

Exact author locators: §1.3.1 and Lemma1.3.3 pp.16–17; Corollary1.3.5 p.18; Theorem1.3.10 pp.23–24; Proposition1.3.11 and Lemma1.3.12 pp.24–25; Remark1.3.15 p.25; Theorem3.1.4 p.49; Remark3.3.6 p.52.

The characteristic exponent inverted in §1.3.1 equals one over \(\mathbb C\); this is an integral argument.

## Proof checks

The sum of Yoneda maps indexed by actual Chow sections surjects onto the associated sheaf. Smooth quasi-projective parameters suffice because smooth affine opens cover the site. Thus no global cycle representative is assumed for an arbitrary sheafified section.

After quotienting by the images of the Serre–Albanese kernels, the result is a quotient of a coproduct of Serre–Albanese schemes. Cocompleteness and the Serre property place it in the one-motivic category. Lemma1.3.12 gives the universal property. This uses cokernels and epimorphisms, not left exactness of arbitrary colimits.

Evaluation at \(\operatorname{Spec}\mathbb C\) is exact because étale covers of this point split. It commutes with sums, and sheafification does not change the value at the point. The kernel is therefore exactly the finite sums of images of the free-zero-cycle kernels \(K_T(\mathbb C)\), without saturation.

A smooth projective compactification \(\overline T\) sends a Serre–Albanese-zero cycle on \(T\) to a degree-zero Albanese-zero cycle on \(\overline T\). Chow localization extends the actual cycle, and refined point pullback agrees on the open. Conversely every defining generator of \(N^i(X)\) uses a proper smooth parameter. Both inclusions are integral.

The original sentence claiming factorization through ordinary \(\operatorname{CH}_0(T)\) for arbitrary nonproper \(T\) was too broad: a constant family on \(\mathbb A^1\times X\) already disproves that assertion. The owner replaced it by the correct statement for the smooth projective compactifications. The proof only uses free zero-cycles before compactifying, so no mathematical step was lost.

The component identity follows from successive left-adjoint universal properties. Theorem3.1.4 identifies the component quotient with cycles modulo algebraic equivalence; exact evaluation gives the connected-point statement. The example \(B/\mathbb Zb\) for a nontorsion point of an elliptic curve is a valid connected one-motivic sheaf which need not be an abelian variety. No finite-dimensional representability or Walker comparison is implied by E.3s.

Remark3.3.6 only anticipates a comparison with the full morphic Abel–Jacobi construction. The distinction between that construction and the finite-dimensional Walker Jacobian must be retained in subsequent revisions.
