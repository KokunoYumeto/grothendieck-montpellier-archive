# Topology proof notebook — 19 November 2026

## Scope and conventions

We study a finite labelled arrangement of distinct PL pseudolines in RP2 with pairwise unique transverse intersections and rank three (not a pencil). Multiple intersections are allowed. The active surface is the later variant X2 of scans 154/5 and 7, with all non-supercritical positions as faces and exceptional sweep edges. X0, X1, X1-prime have another Euler characteristic; X3 is homeomorphic to X2 after adding collars. Keeping the variant explicit is mandatory.

## Established input readings

The local polygon construction of 154/31–40 first attaches transition intervals and then caps inertia circuits. Scan39 specifies the reflection gluing and claims length4; scan40 specifies one GG corner, oneSS, two mixed. The word 'surface' in the initial ribbon construction does not prove that all corner circuits have length4 or that a face closure embeds. Scan45 gives all non-supercritical positions, ordinary immediate arrows, exceptional sweeps, ordinary diamonds, and exceptional original-line flags. Scan7 identifies X2 with X1 after removing supercritical face interiors and identifying boundary antipodes.

## Candidate global formula (proof gates remain)

Let c_j be the number of unoriented non-supercritical single-element extensions with j zero old vertices; let b=sum_i n_i=sum_v mu(v), where n_i counts vertices on linei. Each ordinary j-extension has exactly2j immediate generizations. Hence the ordinary incidence graph has sum_j2j c_j edges. Exceptional sweeps count2b. If every glued vertex is quadrivalent, then

F=sum c_j, E=2sum j c_j+2b, V=sum j c_j+b,
chi(X2)=sum(1−j)c_j−b.

The extension agent is deriving the two exact Euler identities Fpolynomial(−1)=1−n and Fpolynomial'(−1)=b, by a cubical CW model and constrained extensions through a fixed old vertex. Together these imply

chi(X2)=1−n−2sum_{j odd,j≥3}(j−1)c_j.

The correction vanishes precisely if there are no extensions through three old vertices: every larger zero set has three-zero generizations. For n≤5 this holds by disjointness of incident-line sets; rankthree and distinct old lines imply n≥3.

## Finite evidence already available

The exact six-line example has dual coefficient vectors (1,0,1),(2,0,1),(0,1,1),(0,3,1),(1,1,1),(4,4,1). All20 old determinants are nonzero. New element (0,0,1) has zero determinants exactly12,34,56. Complete sign enumeration gives c=(80,150,75,10), F315. Full signed basis exchange checked all315 survivors,1,089,945 tests. Literal boundary GG arcs300; original flags60; V360, chi−45. This is independently counted, not merely inferred from quadrivalence. Fixed-realization straight positions instead give F229,V234,chi−5.

## Remaining main proof gate

Prove every ordinary inertia circuit is a four-cycle with four distinct disklabels; prove the exceptional sector normal form and all boundary circles. Local commuting resolutions at disjoint oldvertices are straightforward. Need prove the selected reflection keeps the inertia gap adjacent after each move, and prove that every SS or mixed corner belongs to one such diamond, unless it is an exceptional corridor corner. Only then use the no-zigzag criterion to claim face closures embed.

An exact fallback that does not settle the4-valent claim is signed-ribbon permutation construction: it always gives a compact surface after capping all boundary circles, and its cycle counts determine topology. This is not a substitute for the required proof of quadrivalence.

## SA10 audit

Read and rechecked A4.3 in sections_A.tex lines628–662: the finite no-zigzag criterion is valid, by finite simple index paths and closed saturations. Its cartesian-meet alternative is not automatically available for the disk diagram. We will use the exact no-zigzag criterion.

Read C3.04 in C_sections.tex sectionC3.04: local manifoldness must be checked separately. In this task we will provide explicit interval/circle links; no shape-colimit claim is used.
