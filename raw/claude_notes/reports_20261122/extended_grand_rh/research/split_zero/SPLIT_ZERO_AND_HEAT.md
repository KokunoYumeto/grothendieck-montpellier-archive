# What the split-zero boundary can detect

## The original workshop

The 28 September and 7 October exports of *Split Zero cohomology research* contain the same workshop through line 21647, aside from two header dates. The October export adds a final exchange on the flow of weights. The later file is thus a continuation of one conversation. In both exports, lines 1035–1066 distinguish the new generic support point from the original closed prime points. Lines 1457–1477 give the precise pole-plane discussion. In the explicit formula the pole term is \(2\operatorname{Re}(a\bar b)\), which has signature \((1,1)\). The original local note specifies that identifying the theta zero term with the “prime 0” is a naming convention. The unchanged Euler product has the original zeta function. Calling this plane part of an arithmetic surface would require constructing the surface, intersection pairing and positivity comparison.

The original note is under Documents/math/work/claude_orientation_20260922/PRIME_ZERO_AND_WEIL_POSITIVITY.md, especially lines 229–331, 363–409 and 447–467. Theorem D constructs a meromorphic competitor with the same pole term, reflection, reality and off-line zeros. The competitor lacks the required zeta Euler product. This shows what the pole data alone can decide. Interpreting the sign of one indefinite plane as classical or grand RH would overlook the rest of the explicit formula.

In the October transcript, lines 2324–2339 identify the quadratic sign flip with the local Newman collision and lines 2467–2480 show what happens under inversion of the supported zero. The localization becomes the two-element Boolean semifield. All supported scalars become one, so that localization loses the original continuous heat parameter. Lines 4993–5005 propose a finite Hodge-index comparison. Lines 21678–21685 distinguish a positive functional in modular theory from a Deligne weight and request an actual Bost–Connes KMS calculation. The term Erdős–Straus is confirmed there. The reported modular flow of its Proposition 8.3 is an input to that proposed comparison, which this note does not assume.

The September retrospective gives a substantive positive result: tensoring before quotienting retains mixed all-prime boundary classes that every endpoint tensor evaluation kills. See REPORT.md in RH_Retrospective_Audit_20260923.zip, lines 116–164. A finite-space example in lines 188–219 records extra negative directions of the eight-state form. Lines 307–315 identify the three objects needing comparison: boundary homology, its actual connecting image, and the intended interior. Later original sources construct additional intermediate maps, including the separated normal receiver, so the September audit alone understates what was ultimately done.

## An obstruction for the computed boundary and a precise alternative

Let \(B_{r,m,j}\) be the weight-\(2m\) summand of the algebraic all-prime boundary homology. Take the idele \(u=(a,1,1,\ldots)\) with \(a>1\) at the real place. BW14 gives \(T_a=a^m I\) and BW21 gives the identical action on the actual image of the connecting map. A diagonal rational prime has adelic norm one and would be the wrong test element. On a zero jet of length \(e\) the later supported construction gives
\[
T_a=a^\rho\exp((\log a)N),\quad N=\mathrm{multiplication\ by}\ (s-\rho),\quad N^e=0.
\]
On an integer twist \(k\) the exponent is \(\rho+k\). In particular the paper's designation \((-1)\) corresponds to \(k=1\).

**Consequence.** Every dilation-equivariant linear map from the computed boundary homology or its connecting image to any such integer-twisted nontrivial zero jet is zero. This uses only the classical open strip \(0<\operatorname{Re}\rho<1\). The source exponent is integral while \(\operatorname{Re}(\rho+k)\) lies strictly between consecutive integers. Consequently \(T_a-a^m I\) has nonzero scalar part on the target, with nilpotent error, and is invertible. Equivariance makes this invertible operator annihilate the image. The same result holds into the original quotient when its coordinate evaluations on the zero jets are jointly faithful as in CW1.15 and CW7.8. Here the word “original” specifies the actual Mellin generator \(s\).

A vector in a finite-weight tensor product, dual of a scalar sector, integer twist or finite extension satisfies a polynomial in \(T_a\) whose roots are integral powers of \(a\). For a given source made by finitely many such operations, take the product over its finite spectrum with powers sufficient for its extension length. The same polynomial is invertible on every target jet under discussion. A topological completion with dense algebraic source still has zero continuous image in a Hausdorff jet. These extensions of the obstruction apply under the indicated algebraic and topological hypotheses.

**How much would a fractional twist buy?** Let \(V_{\sigma,d}\) be a single length-\(d\) Jordan jet for all positive dilations \(a^{\sigma}\exp((\log a)N_d)\). Between \(V_{\sigma,d}\) and \(V_{\rho,e}\), equivariance for every \(a>0\) is equivalent to intertwining the infinitesimal generators. The equivariant Hom space vanishes unless \(\sigma=\rho\). If they are equal, the image of a cyclic generator is any vector in \(\ker N_e^d\); its dimension is \(\min(d,e)\), and a surjection exists exactly when \(d\ge e\). A scalar half twist supplies the modulus of an on-line zero. It must also supply that zero's imaginary frequency to match its character. A matching semisimple character can reach only its one-dimensional eigenspace. Under a full idele-class action, a genuinely nontrivial norm-one twist is an additional obstruction from a boundary sector with trivial norm-one action. The supported jet source used here establishes a positive-real dilation action. A specific Hecke receiver would need its full equivariant construction.

BW20–22 already constructs a connecting map to a test-space kernel; the vanishing above concerns any subsequent equivariant projection of its image onto the nontrivial original jets. The later CSL7.1 source has genuine supported maps between terms with the same spectral characters. Those maps have compatible spectra. The new comparison pinpoints which older boundary object cannot itself provide the missing interior. It gives no restriction on an intermediate image possessing other characters, and no obstruction to a geometric weight bound on that image. The underlying representation-theoretic argument is elementary; no priority claim is made.

**Original local sources.** Beneath Documents/math/work:

- boundary_weight_publication_20260923/release/github_files/workbenches/splitzero-tandem/continuations/20260923-retained-source-readers/all-prime-boundary-weights/ROOT_BOUNDARY_WEIGHT_HOMOLOGY.tex, BW13–14 at lines 239–263, BW21 at lines 399–418, and the interior comparison at lines 471–486.
- boundary_winding_publication_20260925/edition/CC_ACTUAL_WEIGHT_LIFT_COMPARISON_BODY.tex, CW6.1–5 at lines 505–536, joint faithfulness and the earlier separated-character comparison at lines 672–684, and the achieved normal receiver at lines 969–985.
- boundary_winding_publication_20260925/edition/CC_SUPPORTED_LOCALIZATION_AND_WEIGHT_MAPS_BODY.tex, CSL7.1 at lines 369–391.

## A connection that survives for prompt 62

The source HTML *Split-Zero and de Bruijn–Newman heat flow* exhibits the moving zero algebra. Its equations (H3)–(H10) distinguish multiplication by \(s^2\) in Mellin space, differentiation twice in \(s\) for Newman time, and the generator of Hurwitz translation. The heat image of a representative of the zeta ideal need not lie in the ideal generated by the heat-evolved zeta function. Equations (Z5)–(Z7) give the local Hermite model and its full discriminant. For a multiple zero, the trace pairing on the original fiber loses nilpotents. The subsequent time-dependent trace forms have exact information about their lengths.

The accompanying heat_subdiscriminants.tex works on the true moving zero algebra in the height variable \(z\) with \(H_t=-H_{zz}\). Write \(D_k(t)\) for the \(k\)th leading minor of its trace matrix in the monomial basis. Its entry in coordinates \(i,j\) is the Newton sum of degree \(i+j\) over a fixed contour. If the endpoint multiplicities are \(m_1,\dots,m_r\), then \(\operatorname{ord}_0D_k-\operatorname{ord}_0D_{k-1}\) is the \(k\)th smallest integer in the pooled lists \(0,\ldots,m_i-1\). Thus two doubles give successive orders \(0,0,1,2\) and a triple plus a simple zero gives \(0,0,1,3\). The note computes every leading coefficient and bounds the valid negative-time interval when contour data are supplied. Newton's identities already recover multiplicities from the full exact endpoint moments, so this contribution describes the deformation rather than improving the cost of finding exact endpoint zeros.

Prompt 62's heat_theorems.tex, lines 24–51, proves the required Hermite splitting. Its finite_detection.tex and multiplicity_detection_equivalence.tex concern global Toeplitz minors; orbital_detection_constants.tex obtains their constants through a unitary orbit. Those global matrices are distinct from the fixed-contour trace matrices. There is no height-uniform transfer in the new calculation. The two short explicit counterexamples at the end of the first-negative-minor section quantify why fixed finite-time observations cannot furnish it alone. A useful future question is whether arithmetic information controls the condition numbers of those contour moments at growing heights, at a rate that genuinely changes an existing global detection estimate.

The exact test program constructs the deformed integer polynomials, computes Newton sums in the monomial basis, forms every principal minor, interpolates each polynomial in \(t\) and checks its predicted first nonzero coefficient. It passed all 66 partitions and 416 minors of degrees one through eight. A separate instance independently derived the residue slope, multiplicity-order formula and Hermite constants.

## Evidence file identities

The following files were read from the ordinary Downloads directory. The two archive CRC checks passed.

| Original filename | SHA-256 |
|---|---|
| Claude-Split Zero cohomology research-20260928-0343.md | 557b0772cac8f23a5ff34c4309fae1563bcf246935db64161541d783d736f4ca |
| Claude-Split Zero cohomology research-20261007-0444.md | df033c0fb5b804fc33e144f17d37cba02de493b7aa99c8a60613de7786144f00 |
| split_zero_newman_openai_report.html | 5d4a6310c412c9c93b444be67bb0e07da8fdb72d6b95041333c78ad4364d5485 |
| RH_Retrospective_Audit_20260923.zip | 7a63220256747d04416a080f28f17022983910571a11154f5b891c8b2be31623 |
| NS_to_RH_transfer_analysis.zip | 1f0e7773c72049d722abd51c479ea7236b211b547994c7888bdbb4999237404c |

The last archive's source, sections beginning at lines 262, 287 and 337, distinguishes the Hilbert quotient losing modes, forward smoothing preserving every zero and the genuine zero-moving flow. For external normalization and the classical subdiscriminant identity, see [Rodgers and Tao](https://arxiv.org/abs/1801.05914v5) and [Roy, Proposition 1](https://doi.org/10.4230/DagSemProc.05021.20).

