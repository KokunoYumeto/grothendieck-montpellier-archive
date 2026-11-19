# Independent A.3–A.4 proof and input audit

Auditor: GPT-6 Astra, OpenAI, ChatGPT Pro mode, `part_c_algebra` agent, 19 November 2026. The root researcher owns these two sections. The only direct edits made in this audit are the explicitly authorized graph-vertex proof strengthening and source citations in `sections/part_a3.tex`. The parent owns the additional boundary-chart lemma and inherited A3/A4 input-ID events.

The eight actual check events are in `checks/part_a34_secondary_events.tsv`. Earlier direct Morera and welding checks are retained in `checks/part_a3_secondary_events.tsv`. The events use the required five-column schema and do not treat the same check as two independent proofs.

## A.3: circle, graph and slit welding

### Circle welding and removability

The orientation-reversing convention is correct for gluing oriented boundary components. Beurling–Ahlfors gives the local quasiconformal extension after an orientation convention on one side is changed. The coefficient transferred to a common seam coordinate has norm bounded below one; finite gluing gives a common bound. The measurable Riemann mapping theorem produces charts in which each open original piece remains holomorphic.

The removability proof is valid with the given uniform quasiconformal hypothesis. After straightening a quasiarc, a homeomorphism conformal off the original seam becomes quasiconformal with a uniform bound on the two sides of a line segment. On relatively compact rectangles the area formula bounds the integrals of its squared first derivatives. Fubini gives absolute continuity on almost all transverse lines; continuity glues across the one omitted point on such a line. Thus the straightened map is quasiconformal on the full rectangle. Returning through the straightening, it is quasiconformal and conformal off the original quasiarc; that arc has area zero because quasiconformal maps have the Lusin N property. Its Beltrami coefficient is therefore zero almost everywhere, giving conformality. No general claim that every arbitrary seam is removable is used.

I independently opened the local original PDFs and read Beurling–Ahlfors, *The boundary correspondence under quasiconformal mappings*, Theorem1, printed p126, and Bishop, *Conformal welding and Koebe's theorem*, §1 pp613–615 and §4 pp630–632. The latter is the actual location of the quasisymmetric construction. Actual LaTeX citations to these locators are now in the fragment.

**Scope correction to the input:** quasisymmetry is a sufficient condition for welding, not a necessary condition. Bishop's Theorem3, printed p614 (proved in §7), supplies log-singular weldings which are not quasisymmetric. Therefore the old phrase “existence needs quasisymmetry” must not be interpreted as an if-and-only-if. It is legitimate to replace the unsupported interval-rectifiability hypothesis by a sufficient quasisymmetric one. Uniqueness additionally follows from removability of the actual seam.

### Finite graph vertices: explicit compatibility construction

The displayed QC-compatible-star assumption is sufficient. It says that the topological quotient is an oriented surface and admits an orientation-preserving coordinate on the vertex star which is quasiconformal on every open incident sector, with a common finite bound. Transfer the complex structure to that whole star, give any coefficient on the finitely many rays and the vertex, and integrate. This directly includes the vertex and avoids an unnecessary punctured-neighborhood extension step. At a boundary vertex reflect the coefficient to the doubled half-disc. The image rays are quasiarcs.

The former short smooth-sector justification needed an explicit shared radial normalization. I replaced it by the following construction. If the incident angles are alpha_j>0, put A=sum alpha_j and c=Omega/A, where Omega=2*pi at an interior vertex and pi at a boundary vertex. Give sector j target angle c*alpha_j. A single radial coordinate on each quotient ray pulls back to two functions s_{j,-},s_{j,+} on the two original boundary rays; each has nonzero derivative and s(r)/r tends to a positive constant. For u=theta/alpha_j set

    log R = c*((1-u)*log s_{j,-}(r)+u*log s_{j,+}(r)),
    Theta = Theta_{j,0}+c*theta.

On a paired ray the maps agree because the same quotient radial parameter is raised to the **same** power c. In logarithmic polar coordinates the radial derivative of log R is bounded above and away from zero, while the angular derivative is `(c/alpha_j)*log(s_+/s_-)`, hence bounded. The angular derivative of Theta is c and its radial derivative is zero. The derivative matrices and their inverses are uniformly bounded. This proves quasiconformality for each sector, with one bound for the finite star. Smooth nonzero-angle corners can first be straightened bi-Lipschitzly. Independent powers for different sectors would not, by themselves, establish agreement on shared rays.

The existence theorem concerns that explicitly specified graph category. It does not claim that separate arc-wise quasisymmetry automatically settles all endpoint data, nor that an arbitrary topological quotient is a surface. Cutting retains both prime-end sides and all vertex incidence data, so it inverts welding in this category. Uniqueness is first local across the open edges, then across the isolated vertices.

### Slit uniformization and normalized converse

For a Jordan domain V and an attached Jordan arc I, the cut domain V\I is simply connected. Its prime-end compactification separates the two slit banks, gives the interior tip one preimage, and gives the boundary root two preimages. The compact union of a Jordan curve and attached Jordan arc is locally connected. The continuous boundary extension and the prime-end homeomorphism therefore apply without rectifiability. The three chosen prime ends have to be positively cyclically ordered, because the disc automorphisms preserve orientation. Their normalization is unique.

For the converse, gluing the two banks of the source disc gives a topological disc with one marked interior point (the tip) and one marked boundary point (the root). The QC-star hypotheses give the conformal structure. Normalization to tip0, root1 removes precisely the three real disc-automorphism parameters. The residual automorphism fixing0 and1 is the identity. Its interior image is D\I; consequently the source interior point0 cannot also map to the omitted tip0. The ambiguous input line at scan073 must not be silently read as `f(0)=0`.

The doubled-tip qualification is real. A map `h(t)=t^2` between individual half-intervals is quasisymmetric there, but the order-reversing doubled involution has `H(t)=-t^2` for t>=0 and `H(-t)=sqrt(t)` for t>=0. The lengths of the two image intervals adjacent to0 have ratio t^(3/2), tending to0. Hence that doubled involution is not quasisymmetric. The current statement explicitly imposes the missing compatibility rather than asserting it follows from the bank-wise condition. Quasislits need not be rectifiable, so the converse correctly does not conclude rectifiability.

For an exact opened boundary-extension reference, I opened the full author preprint of John Milnor, *Dynamics in One Complex Variable*, Stony Brook IMS preprint1990/5, partially revised5 September1991, from Harvard's public archive:

https://legacy-www.math.harvard.edu/archive/118r_spring_05/docs/milnor.pdf

Theorem15.9, printed p15-5 (PDF page93), proves the prime-end completion theorem. Theorems16.6 and16.7, printed pp16-2–16-4 (PDF pages95–97), state and prove the locally connected and Jordan boundary cases. Tool refs: `turn213714345view0`, `turn519186244view0`, `turn519186244view2`. The citation and its opened/version status are in `sources/part_a3_secondary.bib`. No theorem number from the revised1999 book is substituted. An attempted original1913 DigiZeitschriften link redirected to the service-closure notice (`turn788526048view0`); that original was not claimed opened.

### L5

Under the actual geodesic interpretation, boundary arclength coordinates are analytic and the seam pairing is theta->theta0-theta. Thus the circle-welding theorem applies without the uncertain interval-rectifiability assertions. Smooth **diffeomorphisms**, with smooth inverses, are bi-Lipschitz on each compact boundary circle, so the same conclusion holds. Mere differentiability of a homeomorphism does not imply a derivative bounded away from zero; a smooth flat increasing germ such as exp(-1/t) illustrates the distinction. The arbitrary-embedded-cut failure of the induced pointed-cap antiisomorphism is a separate issue, proved in `A1-nontoric-cut`; it is not hidden by L5's regularity statement.

## A.4: orange cells, jets, and the intrinsic action

### Independent orange-cell and extremal-length check

In the spherical metric for which0,1,infinity are equidistant, the Hermitian form is proportional to `[[1,-1/2],[-1/2,1]]`. It is positive definite and preserved up to scale by z->1-z, z->1/z and complex conjugation. The corresponding antiholomorphic reflections z->1-conjugate(z) and z->1/conjugate(z) fix the two relevant bisectors. Hence the cell containing0 is exactly

    Q0={|z|<=1, Re(z)<=1/2}.

If the canonical cap D0 of the (32,0,0)-pant lay in Q0, every point of D0 would have distance at most sqrt(7)/2 from-1/2. The annulus4/3<|z+1/2|<7/5 consequently misses D0; it also misses1, whose distance from its centre is3/2, and infinity. Its core encloses D0 and no other end, so it belongs to the correct boundary homotopy class. The generalized pant has two cusps and one geodesic boundary, area2*pi, and shortest length32 in that class.

For the family of loops in that class, enlarging the domain from the annulus to the pant gives `Ext_P<=Ext_A`. The logarithmic rectangle gives `Ext_A=2*pi/log(21/20)`; the hyperbolic metric gives `Ext_P>=32^2/(2*pi)`. The contradiction is exact:

    log(21/20)>1/21,
    1024/21>4*(22/7)^2>4*pi^2.

Thus all geometric hypotheses of the input's credited finite example are rechecked, not only its decimal values. The final contradiction is not a numerical approximation. The exact arithmetic was already covered by the root's certificate; this audit does not introduce a duplicate computational run.

### Independent jet check

For a fixed pointed domain with centered coordinate U, the coordinate on its concentric subdomain is U/lambda. Dividing by lambda changes the linear coefficient but leaves the normalized quadratic coefficient b unchanged. The two positive-length pants used in `A2-independence` have b=1/2 and b=5/4. Therefore no three fixed pointed discs with independent concentric scalings can describe all canonical pants. This refutation does not rely on the particular orange spherical cells or on permitting degenerate discs.

### Grafting, action and zero-length strata

I re-read `sources/mondello/Triang-submitted.tex`, lines3494–3550: the construction skips cusp ends, and Theorem5.4 says the grafting/length map is an equivariant homeomorphism preserving topological type and a real-analytic diffeomorphism on every finite topological stratum. The cylindrical coordinate `u=exp(2*pi*i*(s+i*y)/ell)` identifies infinite grafting with the exact canonical capping operation. Restricting to finite nonnodal strata and forgetting the decoration direction when all lengths vanish gives the ordinary product with [0,infinity)^n.

Coordinatewise multiplication by that product homeomorphism gives the asserted continuous intrinsic monoid action, including mixed cusp and boundary-circle strata. The units act freely and transitively on each **positive-length** capping fibre. Multiplication by the all-zero vector is the canonical retraction; multiplication by1-t is the strong deformation retraction and fixes every point already in the punctured locus. Mapping-class equivariance, including simultaneous permutation of labelled ends, follows from the same equivariance in Mondello's theorem. No identification with arbitrary tangent radii or a pants-coordinate scaling is made.

## Exact input corrections and qualifications for A.3–A.4

All paths in this table are relative to `/workspace/scratch/9c53b536a97f/inputs/`. Line numbers refer to the unchanged input files.

| Exact input file and line(s) | Manuscript location | Corrected or qualified use in this run |
|---|---|---|
| `RESEARCH_SA22_study/study/CORRECTIONS.tsv:2` | 67/059–060,072–073 | “Needs quasisymmetry” is sufficient, not necessary. Existence, removable-seam uniqueness and vertex compatibility are separate assertions. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:270–296` | Théorème4,67/059 | Replace the unsupported interval-rectifiability equivalence by the specified oriented QC-compatible graph category; retain all incidence and prime-end bank data. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:338–359` | Lemma3,67/060–061 | Parts(a),(b) require welding hypotheses; part(c), continuous-function removability, has a complete direct Morera proof. The word at line358 is interpreted as holomorphic/analytic off C, not merely continuous. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:634–646,669–694` | Lemma4A,67/071 | Rectifiability is unnecessary for Jordan-slit uniformization and the described continuous boundary extension. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:699–705` | NB1,67/072 | Triple uniqueness is retained with positive cyclic order and prime-end, not repeated geometric-root, points. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:707–729,745–781` | Lemma4B and Scholie,67/072–073 | Impose doubled-tip quasisymmetry and vertex compatibility. Do not infer rectifiable slit from quasisymmetry. At line745, the handwritten `omega|0` remains uncertain; the type-correct replacement is f(1)=0 for the source boundary tip. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:799–810` | section6,67/074; L5 | Smooth diffeomorphic seam pairings satisfy welding. Pointed-cap antiisomorphisms require the additional toric/geodesic property; arbitrary embedded analytic cuts can fail it. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex:558–562` | letter67/017 | Intrinsic multiplicative length action and zero retraction are proved through canonical grafting, without fixing unrelated pants coordinates. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex:585–595` | letter67/019 | Radius injectivity is proved by A2b-energy; independent upper bounds do not describe the joint image. A2b-image supplies all support inequalities. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex:597–608` | letter67/019–020 | The orange/concentric model, including its explicit permission for degenerate discs at line606, is false. A4-orange-extremal and A4-orange-jets give independent refutations. |
| `RESEARCH_SA22_study/study/CORRECTIONS.tsv:22` | credited orange example | The exact geometric and extremal-length argument is independently verified above. |
| `RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex:618` | letter67/021 | The collar-metric question imposes no additional definition of nodal external-disc admissibility; the general moving-boundary metric analysis is in the root's separate collar theorem. |

Additional A1/A2 corrections with exact input locators are recorded in `notes/part_c_input_audit.md`. The finite-program scope/count/runtime table is `notes/part_c_program_scope.md`.
