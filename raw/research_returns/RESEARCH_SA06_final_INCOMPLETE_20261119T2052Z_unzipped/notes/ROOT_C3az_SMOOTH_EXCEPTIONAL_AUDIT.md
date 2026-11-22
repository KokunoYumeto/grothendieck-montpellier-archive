# Root full audit: C.3az

**PASS.** AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We read the entire four-page typed argument and independently rederived each step. We freshly opened all eight new primary Stacks inputs and read the relevant statements and proofs. The previously audited KST, Geisser–Hesselholt, Thomason–Trobaugh and Fulton inputs are reused with their exact locators from C.3ax; no fresh reread of those four sources is claimed in this event.

## Scope retained

The base is the strict henselization at a closed k-point of a normal local ring essentially of finite type over an algebraically closed field k of characteristic p>0. The dimension is d+1, with d>=1. A projective birational modification is regular and is an isomorphism away from the closed point. Its reduced exceptional fibre E is a single smooth connected Cartier divisor, and O_E(-E) is ample. These are genuine restrictions. There is no retraction from the modification Z to E. The theorem proves CH^d(Z)_Q ≅ CH_0(E)_Q, the exact quotient formula on the puncture, and B^d(Z)_Q ≅ Q with B^d(X)_Q=0 for actual ordinary algebraic equivalence.

## Independent derivation

1. Abstract blow-up pro-descent and K_0 of local rings give a monomorphism from the constant K_0(Z) pro-object to the infinitesimal exceptional fibres. Its kernel terms form a decreasing system of inclusions. A pro-zero such system has a zero term, so one finite stage detects K_0(Z). Nil-relative K-theory in characteristic p becomes zero after inverting p; finite affine Mayer–Vietoris descent gives injectivity into K_0(E)[1/p]. No uniform p-exponent over infinitely many infinitesimal stages is used.
2. The algebraizable strict-local hypothesis permits finite pointed-etale smooth models for Z. Regularity and properness over the local base allow removal of the image of any nonsmooth locus away from the marked point. The natural rational Chern-character ring isomorphism passes to the filtered limit and commutes with the Cartier pullback. This yields the required injective codimension-d Chow map.
3. A sufficiently ample complete-intersection curve C in E can be chosen smooth and connected through any prescribed points x,o. Relative Serre vanishing lifts its cutting sections to Z. Independence of the restricted differentials makes their common zero scheme W regular of dimension two along C. Any nonempty closed bad locus in the proper scheme W has image containing the closed point of the local base, which contradicts this regularity. The same properness argument excludes additional components. The induced conormal on C remains ample.
4. For an entire line bundle F on C×P, where P is a smooth connected projective parameter curve, the obstruction to the successive square-zero lift is H^1(C,L_C^n) tensor H^1(P,O_P). Serre vanishing kills every such group after one fixed index n_0. At the finitely many earlier indices, tensoring by p kills the additive obstruction. We can take the fixed total exponent p^(n_0−1) for the whole family. The preceding restrictions are raised together at each step; this gives a compatible formal system, rather than unrelated pointwise lifts or an unbounded sequence of powers.
5. The C-adic and closed-fibre-adic ideals have the same radical on the noetherian proper surface, hence cofinal powers. Projective Grothendieck existence over the completion algebraizes the line bundle. Algebraizing its inverse and their pairing verifies actual invertibility. Excellence makes completion a regular map. Popescu gives a smooth finite-stage algebra carrying the bundle. The residue-field point of that smooth algebra lifts to the henselian ring. Pullback gives an actual bundle on the fixed product W×P with the prescribed entire closed-fibre family. Preserving the residue-field map preserves that family, not merely its numerical class.
6. For P=C and the diagonal line bundle, the two fibre classes push from W to Z. Tor-independent Cartier base change sends their difference to p^e([x]−[o]) on E. Thus all degree-zero zero-cycles on E lift rationally to actual ordinary algebraically trivial classes on Z. Injectivity then identifies the exact ordinary kernel of the restricted degree map.
7. An exceptional curve D has restricted self-intersection −c_1(L)[D] of nonzero degree. It supplies the missing degree direction, proving surjectivity of the full Chow map. Localization gives the quotient by c_1(L)CH_1(E). The same boundary class spans B^d(Z)_Q and restricts to zero, proving B^d(X)_Q=0.

## Primary sources freshly opened and read

| Input | Exact locator and URL |
|---|---|
| Relative Serre vanishing | Stacks Lemma30.17.1, https://stacks.math.columbia.edu/tag/01XO |
| Prescribed-point smooth connected sections | Proof of Stacks Lemma45.8.3, https://stacks.math.columbia.edu/tag/0FH7 |
| Square-zero Picard obstruction homomorphism | Stacks Lemma37.4.1, https://stacks.math.columbia.edu/tag/0C6R |
| Projective existence and full faithfulness | Stacks Lemma30.24.3, with30.24.1, https://stacks.math.columbia.edu/tag/0885 |
| Popescu smoothing | Stacks Theorem16.12.1, https://stacks.math.columbia.edu/tag/07GC |
| Descent of an invertible sheaf | Stacks Lemma32.10.3(2), https://stacks.math.columbia.edu/tag/0B8W |
| Smooth lifting over a henselian pair | Stacks Lemma15.13.3, https://stacks.math.columbia.edu/tag/0H74 |
| Regularity of completion for a G-ring | Stacks Lemma15.51.14, https://stacks.math.columbia.edu/tag/0AH2 |

Root retrieval receipts are turn698371113view0–3 and turn181229075view0–3. Each stated application satisfies the hypotheses on the retrieved page. In particular the Picard obstruction result is used one square-zero step at a time, never for an arbitrary nilpotent thickening as a single additive sequence.

This is a restricted positive theorem, not a closure of the unrestricted rational top-group question and not a scheduled-review movement by itself. Reducible exceptional fibres are deliberately left outside its statement.

The complete independent review by /root/real_weil, completed2026-11-19T11:38:43.203963+00:00, was subsequently read in full by root. Its additional fresh KST/GH/TT checks agree with the inherited source audit and the whole-family proof above.
