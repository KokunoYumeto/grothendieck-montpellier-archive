# F57 pure point-complex supplement: independent whole-proof and fragment review

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

Complete targets freshly read:

- `agent_pure_point_complex_trace.md`, SHA256 `898004d1f39261f402f35f0955e34f692d81690f8494f741f83c3f2941a65f17`.
- `finding_F57_pure_complex.tex`, SHA256 `b7886ec64f74c13b337a37ca97e4660a8821975ed055f0c3d79495c7dcc9d4ae`.

**Whole mathematical proof and full report-to-fragment match PASS.** A source-setting precision was requested for the proper-pushforward sentence: state a proper morphism of schemes of finite type over the finite field, the exact setting of the cited BBD statement. No mathematical correction to the displayed theorem or constructions is required.

## Independent reconstruction

I checked the necessary condition by grouping all nonzero Frobenius roots in the finite Euler trace and using the consecutive-large-exponent Vandermonde matrix. A visible root `lambda^e` in a point complex pure of weight `w` must lie in degree `e-w`, so its coefficient has sign `(-1)^(e-w)` times a nonnegative integer. This yields exactly `(-1)^w f(-v)` effective. A root not in the target spectrum also has only one permitted degree, so it cannot be hidden by opposite-parity cancellation. Arithmetic Jordan blocks do not change any power trace used in the argument. Eventual equality and the inverse parameter convention have been checked separately.

I checked the converse with `L_e[-(e-w)]`: the line lies in cohomological degree `e-w`, its weight is `e`, and its coefficient is the required sign. All conjugates of the chosen power of the positive algebraic square root have the required absolute value. The line is also a continuous point representation: the chosen eigenvalue is an ell-adic unit, its powers have compact profinite closure, and the cyclic homomorphism extends continuously from the dense integers to the procyclic Galois group. Odd exponents are explicitly arithmetic coefficient lines, with no asserted geometric half-Tate object.

For the actual F57 polynomial, all exponents are even and the coefficient signs are mixed. Therefore neither parity of the one total weight is possible. The argument excludes any bounded amplitude, not merely one cohomological parity, but still concerns scalar Euler traces of Frobenius itself. The specified additional five-dimensional full-algebra summand, the two-row exclusion and the inserted-endomorphism exception remain unchanged.

For `c_0=v^2+v^-2-2`, I independently recomputed compact torus cohomology from the affine-line localization sequence. The two copies of `G_m` give degrees2,3,4 with untwisted Tate exponents0,-1,-2; twisting by1 gives precisely `Q_l(1)`, two copies of `Q_l`, and `Q_l(-1)`. The Euler trace is `q^-n-2+q^n`. The pure sheaf `Q_l(1)[2]` on the smooth surface has weight zero, while its compact pushforward is mixed: the degree-minus-weight differences are not constant. Thus this example accurately separates source purity from a pure point complex after a nonproper map.

I reconstructed the state-potential corollary for every path. The intermediate terms telescope to `sum w_i+t_b-t_a`, all summands in one matrix entry have that same weight, and all diagonal entries have weight `sum w_i`. Tensor Kunneth preserves the displayed cohomological weight shifts, so the closed-word trace object is pure of one weight. The F57 comparison then contradicts the proved scalar criterion. This is an extra pure-kernel and trace-comparison premise; no IV/VIII source axiom or variable-rank categorification is inferred.

## Primary-source and dictionary scope

I freshly read the entire original BBD text at Sections5.1.5 and5.1.8, pp125--127, and Sections5.1.11--5.1.14, pp127--128, using the locally retrieved primary PDF text. The smooth/lisse clause in5.1.8 applies on the point. Section5.1.11 supplies the geometric-versus-arithmetic Frobenius convention. Sections5.1.13--14 give the upper bound under `f_!` and lower bound under `f_*` for separated finite-type morphisms of finite-type finite-field schemes; properness makes them the same functor. The suggested precision states this ambient setting explicitly.

The separate dictionary uses the already inspected EGA/SGA/archive vocabulary and correctly restricts lambda/sigma language to coefficient representation classes. It does not claim a lambda-ring structure on the noncommutative word algebra. The bounded complex framework, added Weil action, grading-to-weight comparison, point purity and mixed nonproper pushforward remain distinct.

The known source definitions and cohomological operations are inputs; this review is not a new proof of BBD or the original IV representation classification. No main TeX or shared master event file was edited. A final source-setting-only delta can be checked separately.

## Final two-delta match

Final report SHA256 `5b408530f1d991b384d1ceb925a8e47d2c1029dffaad6f0143f919e6ac39fc13` and final fragment SHA256 `fb184f00be88fbfdf5cd0ce59c52a24f526c5fe44f2f9e9719d202ba52e5b63a` were read in both changed passages. The proper finite-type finite-field setting is now explicit. The added factor corollary is correct: if a nonzero Laurent polynomial is divisible by `v-v^-1`, it vanishes at minus one, while the pure-complex criterion would make `(-1)^w f(-v)` a nonzero effective character and hence strictly positive at one. That value is the total cohomology dimension of the constructed pure realization. The claim is conditioned on the displayed variable-to-weight rule, and does not reject positivity of a source's stripped factor. **Both deltas and final-target match PASS.** The full prior proof review remains applicable; no other mathematical change was reported or found in the changed passages.

## Citation-only final delta

The report at SHA256 `84165e6ae2f50acac81f14c5e170634abb1b174c789d9e036a6c4057c67e93a9` and fragment at SHA256 `f325c80aeb83cf64fdcb83da05e559d257481b816e39db7041d4af1044c20155` add only exact compact-cohomology operation citations. I read every changed citation and freshly read the original local Milne contexts: Proposition18.4(b), pp121--122, for the compact-support long exact sequence; Theorem22.1 and Remark22.3(b), pp135--136, including the subsequent ell-adic passage, for compact-support Kunneth; Theorem24.1(a),(b), p144, for the trace and duality normalization. These locators support exactly the attributed operations. **Citation-only delta PASS; no mathematical proof change.**
