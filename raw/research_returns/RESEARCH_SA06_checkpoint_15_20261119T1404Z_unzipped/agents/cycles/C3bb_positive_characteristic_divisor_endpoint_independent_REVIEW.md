# Independent complete proof and source audit: C.3bb

**Result: PASS.** We read the entire draft `agents/real_weil/C3_positive_characteristic_divisor_addendum_draft.tex`, independently checked its one-dimensional input and the r=1 specialization of the fully audited C.3ba argument, and freshly opened the exact primary statements listed below. No independent certificate rerun is claimed.

For every p>0, every algebraically closed k of characteristic p, and every local dimension N>=2, the result gives an integral ordinary divisor quotient surjecting onto additive k. The exponent-p image supplies no rational nonvanishing. Together with C.3ba this covers all 1<=r<=N-1, while N=1 and r>=N have zero positive-codimension Chow groups in the stated puncture setting.

The displayed plane curve has degree n=p(p+1)>=6. On its affine chart the y derivative is -1, and its unique point at infinity has W derivative -1. The plane exact sequence gives H^0(O_C)=k, so smoothness also gives integrality. Its genus is (n-1)(n-2)/2>=10. Thus L=omega_C is ample. The section eta is the identity of omega_C, not a purported nowhere-zero global differential on C; the draft correctly distinguishes these notions.

The cone and its actual total-space resolution inherit the verified full-section-ring construction without assuming degree-one generation. The split tensor restriction of Omega^1 retains the conormal line. The dlog map on actual Picard classes therefore defines the claimed trace functional. O_Z(C)=pi^*L^-1 has zero conormal component, so the full exceptional image is killed and localization descends the functional to the puncture.

The curves z=bt with the displayed etale y equation have an actual smooth selected germ. The closure, finite normalization, pointed strict-henselian branch selection, and proper closed-image argument are exactly the valid C.3as construction, now in dimension one. The selected curve is regular and hence Cartier in the regular surface. It has no other exceptional intersection. The actual divisor difference has supported dlog difference -b dt/z after tensor restriction. Identifying dt with the chosen canonical frame dz gives the principal part -b dz/z. Functorial Serre duality normalizes its trace to -b; reversing the common orientation gives b. This argument divides by no integer and applies also in characteristic two.

For the Segre extension, the map is on resolutions only. The arbitrary-coefficient freeness and ind-etale flatness proof of C.3ba applies unchanged, and flat inverse images of the actual Cartier divisors remain Cartier. The only conormal cohomology component needed is H^0(P^m,O(1)) tensor H^1(C,omega_C). The local coefficient z_0/z_j glues to z_0, so selecting that coefficient gives b. The zero-section image remains zero. The ordinary subgroup is p-divisible by its actual proper-curve correspondence description; hence the additive detector kills it. No family on a varying henselized product is substituted.

## Fresh primary reads

- Stacks Project, Lemma 53.9.3, Tag 0BYD, including its exact-sequence proof: https://stacks.math.columbia.edu/tag/0BYD (opened reference `turn739530423view0`).
- Stacks Project, Section 53.8, especially Lemma 53.8.4 and its proof: https://stacks.math.columbia.edu/tag/0BY6 (opened reference `turn739530423view1`).
- Stacks Project, Lemma 33.44.14, Tag 0B5X, and its proof: https://stacks.math.columbia.edu/tag/0B5X (opened reference `turn739530423view2`).
- Stacks Project, Section 48.27, Lemma 48.27.1 and Remarks 48.27.2-3, including the functorial trace pairing: https://stacks.math.columbia.edu/tag/0FVU (opened reference `turn739530423view3`).
- Coherent Kunneth, Tag 0BED, was freshly read in our immediately preceding C.3ba audit. Its Cech construction is compatible with the supported conormal calculation here.

No correction is requested. The endpoint is a genuine r=1 argument, rather than a formal invocation of a theorem whose original statement excluded that degree.
