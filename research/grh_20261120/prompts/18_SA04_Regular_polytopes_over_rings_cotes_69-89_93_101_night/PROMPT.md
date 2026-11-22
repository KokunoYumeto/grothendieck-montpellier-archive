**The attached files.** Besides this file there is one ZIP, `SA04_Regular_polytopes_over_rings_cotes_69-89_93_101_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA04_broad.zip` is the folder `RESEARCH_SA04_broad/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA04: his arithmetic theory of regular polytopes over rings (cotes 69-89, with cotes 72, 75 and 81 of SA01), with the open questions of 93/55-66 and of his 1958 notes (cote 101)

**To be settled:** the "théorie arithmétique des polyèdres réguliers" that he sketches on 70/122-123 and works out in cotes 70-79: the scheme of realizations of a regular type over Z, its invariant quadric and the places where it degenerates, the general regular icosahedron over a ring (75/33), his congruence triangulations of level n and his regular polygons over Z; then the graphs, nets, trees and incidence structures of cotes 69-89 and 81, the Euler characteristics of 93/55-66, and his 1958 characterizations of Gorenstein rings (cote 101). A.1 is the main question.

Three neighbouring questions are asked in separate prompts and are not part of this one: his good-reduction theorem of 100/003 (RESEARCH_SA15), his notes on the mysterious functor on 161-5 (RESEARCH_SA23), and cotes 94, 97 and 98 (the working-through prompts). The characteristic-p questions of cote 93 (the Schwarzian of 93/72-84, the torsor device of 93/234-236, and 93/92-134) go with the rest of cote 93 into RESEARCH_SA03. His quadratic covers over a base (cote 77) go with cotes 83 and 84 into RESEARCH_SA02.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA04`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It leads topic SA04 in sweep 3 (wave 1) and swept the topic in sweep 1. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA04_study.zip`: our study of the topic.**
  - `study/STUDY.md` (it lists the stretches not yet read in full), `study/HUNCHES.md`, `study/RESEARCH_PACKAGES.md`, and the tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the readings of three readers, each Claude Opus 5.5 at effort max: cotes 69-74 (69, 70, 72, 73 and 74 in full); cotes 76-79; cotes 80-89 with 161-6; cote 93 (scans 47-91 and 221-236) with cote 161-5; cotes 94-102.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA04-1 to SA04-40.
  - `study/SA01/`: the sweep-3 study of topic SA01 (STUDY, HUNCHES, RESEARCH_PACKAGES, the tables, and the readings of cotes 71 and 75, 72 and 81), by the same lead and readers; its cote-72 rows carry SA04 ids.
  - `study/stage_A_dossier_SA04_v2/`: the stage-A topic dossier of cotes 93, 98, 100 and 161-5, made by GPT-6 Astra (ChatGPT Pro mode) on 19 Nov 2026 (`SA04_dossier.md`, `SA04_directions.md`, `READ_ME.md`); its claim ids C-SA04-n and MP-SA04-n refer to its own tables, which are not attached.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA04_transcriptions.zip`: the AI transcriptions (LaTeX) of his pages, with their notes.**
  - `transcriptions/Codex/K<cote>/`: the Work returns of batch K for cotes 69-102, 161-5 and 161-6, with their mathematical notes, by GPT-6.2 Astra at reasoning effort max for most folders and GPT-6 Astra at reasoning effort max for the others (`transcriptions/Codex/AUDIT_K_RETURNS_20261118.tsv` gives the model of each folder). They are the only witnesses of cotes 69-89 except 72/35-81, and of cote 101. `transcriptions/Codex/J71`, `J75`, `J81` and `K83` hold SA01's cotes 71, 75, 81 and 83 from the same batch.
  - `transcriptions/Pro/`: by GPT-6 Astra (ChatGPT Pro mode), each with its notes and doubt table: 72/35-81 and 93/47-91.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where two witnesses disagree, the readings say which one the ink supports, when a reader looked at the scan. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA04_broad.zip`: the neighbouring topics,** so that you see the connections:
  - the sweep-2 maps of SA01 (regular polyhedra over rings: cotes 71, 72, 75, 81, 83 and 93/92-134), SA02 (quadratic algebras: cotes 84, 90, 91/2-18) and SA03 (deformations, cote 91; characteristic p and crystals, 93/2-46 and 135-220);
  - the sweep-3 studies of SA15 (crystals), SA21 (his 1986 axiomatics of forms, cote 156), SA23 (the EGA drafts and the dossiers 161-162, with SA23's own readings of 161-5 and 161-6) and SA11 (pseudolines, cote 154).
- Fetch the literature yourself. It is listed under "Sources" below.

## Where this comes from

His pages are in the Grothendieck archive of the University of Montpellier. They were transcribed by AI (above) and studied in our horizontal sweeps by Claude Opus 5.5 at effort max.

- **Cotes 69-79 (1976-1978; reused sheets of 1976-1977).**
  - 69 and 74: the graph of the 27 lines, characterized by axioms and rebuilt from torsors; E6 from the graph; 3-nets and loops; the series of "graphes trialitaires" 𝒯_ν (the GQ(2, c) with c = 0, 1, 2, 4).
  - 70: "n-polyèdres réguliers en coordonnées affines universelles"; the invariant quadric of a regular {p, q} over a ring; the icosahedron in characteristic 5; "Position du pb des 2-polyèdres réguliers" (70/114-119) and the "Programme provisoire d'une théorie arithmétique des polyèdres réguliers" (70/122-123).
  - 72 and 73: pinned regular realizations, the invariant form, continuants, invariant subspaces and Stiefel-Whitney classes; pentagons from their corner triangles.
  - 76: incidence complexes with the diamond axiom and the n-cartographic groups G_n; flag geometries; the combinatorial cube.
  - 77: quadratic forms over a base; "Extensions quadratiques" (quadratic covers, the discriminant, the mixed characteristic); the invariants of the groups of the regular spherical polyhedra; orthogonal group schemes.
  - 78: a course on regular polygons (Nov-Dec 1977): pinnings, D_n and D_∞, the vertex polynomials F_n, cyclotomic polynomials mod p, regular systems of vertices over Z.
  - 79: congruence triangulations SP_M of level n, their automorphisms, and his axiomatics of "structures triangulaires congruentielles" and of the graphs "à homothéties".
- **SA01's cotes (1976-1986).** 71: a manuscript of 15 July 1976 on three good vertices of a plane polygon (another hand), with his margins; 72: pinned regular realizations, continuants, Stiefel-Whitney classes; 75: the DEA course "Géométries combinatoires" (1977-78), ending with "le n-polygône régulier le plus général" and the general icosahedron (75/31-33); 81: special Belyi functions, binary decompositions, ordered models ("maquettes ordonnées"), non-crossing partitions and edge gluing; 83: SL(2, Λ), the icosahedron over F₄ and the bi-icosahedra.
- **Cotes 80-89 and 161-6 (1977-1986).** Pseudoline arrangements (80); rank-3 quadratic modules and the forms of SO(3) = PGL₂ (82); Schwarz systems and operations on them (85); incidence geometries, the axioms of abstract polytopes, regular maps and 3-3 sets (86-89); graphs in surfaces (161-6).
- **93/55-66:** axioms for χ and χ_! on locally conical spaces.
- **Cote 101, "Notes antiques 1958":** the canonical module ("module fondamental"), local duality, deficiency modules, and characterizations of Cohen-Macaulay and Gorenstein rings by Ext^i(k, ·).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of some of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA04-R70-01 to -07; SA04-K70-01 to -05).** In universal coordinates, requiring every σ_i to be a reflection leaves one parameter α_i per i, the trace of σ_iσ_{i+1} on a face plane, and the order condition is his half-cyclotomic F_p(α) = 0 (70/15-26, 68). For a regular {p, q}: f = x² + y² + z² − γyz − βzx − βxy − (x+y+z) with γ = (α+2)(β+2) − 2, δ'(f₀) = −(α+2)(α+β)(β+2)², δ(f) = (α−2)(α+2)(β+2)², centre (α, −1, −1)/(2(α+β)) and f(o) = (2−α)/(4(α+β)), all verified symbolically; δ' = 4(α+2)(β+2)²·det Gram[p, q]. His table of 70/70 checks, up to two slips (the dodecahedron's δ is −3(β+1)⁴; the pentagram's δ' is α²). Γ⁰_{n,3} ≅ SL(2, Z/n)/±1 exactly for n ≤ 5. In characteristic 5 the 31 directions of the icosahedron are the points of P²(F₅).
- **R2 (SA04-R72-01 to -08; SA04-K72-01 to -07).** Cote 72: the ink "+1" of 72/36 is his slip (the coherent form is β = 4cos²θ, α = 2cos 2θ); δ_n(B) = B₀ⁿ B₁^(n−1) ··· B_(n−1) L_n(B₁, ..., B_(n−1)) with a continuant recursion for L_n, computed for n ≤ 5; the invariant-subspace theorem of 72/80-83 holds; his guess that the ten cohomology classes are independent is false (η_i² = εη_i). The Pro and Codex witnesses agree on the mathematics.
- **R3 (SA04-R69-01 to -19; SA04-R74-01 to -09; SA04-K69, SA04-K74).** On 69/3-11 he proves that a graph with 27 vertices, regular of degree 10, in which every edge lies in exactly one triangle, is the graph of the 27 lines; his Lemma 1 is the generalized-quadrangle axiom, so this is the uniqueness of GQ(2,4) from scratch. The bound |S| ≥ 3(ν − 1) of 69/17 holds, with equality exactly for the GQ(2, t). All his counts agree with |W(E6)| = 51840. On 74/19 and 74/121-124 he names the series himself (c = 2^ν). On 74/128-130, for a vertex of 𝒯_ν, the map u = id + δη on V = F₂^I satisfies u² = id + |I|δη; it is bijective for ν = 0, and otherwise ker u = {0, z} and im u = Ker η; the page proves φ: Y → E injective only for ν = 0. 74/63 answers his question of 69/40: relative to a bitriangle, the 120 bitriangles split 1 + 2 + 27 + 54 + 36.
- **R4 (SA04-R74-01).** His closure condition (f₃f₂f₁)² = id at every point (74/14-16) holds on the 3-net of the Moufang loop M(S₃, 2) of order 12, which is not a group, and fails for a generic loop of order 5: it does not make a net a group net.
- **R5 (SA04-R76-01 to -10; SA04-K76-01, -03).** The manifold criterion of 76/7 is false (the suspension of a triangulated torus satisfies it; checked on the scan); the essential image claimed in Th. 1 of 76/39 is right for n ≤ 2 and false for n ≥ 3, as he suspects himself on 76/43. His questions on δ-connectivity under heredity and on the automorphisms of hemicubes for n even are answered.
- **R6 (SA04-R77-01 to -12; SA04-K77-02, -04, -05).** His open "Étudier la nullité du dit déterminant" has the answer Δ = α(α+1)²(α−2)⁵(α+2)². The calculus of quadratic covers and the uniqueness and existence arguments of the mixed-characteristic theorem (77/53-64, 77/74-86) were re-derived; on 77/74 condition b) should read γ(b₀) ≡ Δ mod 4. His normalization on 77/101 is wrong (μ = 2, not 1/2), and so is the identity on 77/117 (two signs).
- **R7 (SA04-R78-01 to -08; SA04-K78-01, -02, -05, -06).** u_α^n = id ⇔ F_n(α) = 0 holds over every ring, though his Bezout pair is wrong; the order corollary fails for p = 2; on 78/38 all regular n-gons are isomorphic when p | n, so his Question has the answer yes for n = p ≥ 5 and n = 2p ≥ 10 (his sentence reads inverted as transcribed; the reading was not checked on the scan).
- **R8 (SA04-R79-01 to -17; SA04-K79).** For M free of rank 2 over Z/n, his SP_M has (s₀, s₁, s₂) = (N'/n, N'/2, N'/3) and genus 1 + N'(n − 6)/(12n): it is the Farey map of level n (computed for n = 3, ..., 12), and his automorphism theorems (79/43, 78, 90) hold. His question of 79/115-116 has the answer yes: the torus map {3,6}_(3,0) is regular and orientable and has 9 triangles that are not faces, so his axiom T₀4 (the faces are the 3-cliques of the graph) does not follow from regularity. M is the "enveloping group" of its triangulated structure with antipodism for Λ = Z/n, n = 3, ..., 8 (computed; 79/83). His operation ν is special to congruence structures: the star-power operation fails on the Hurwitz maps with group PSL(2,13) (79/141-143). To "J'ignore si cette condition est tjrs satisfaite !" (79/184) the answer is no: an antipodism fails (H1) on one PSL(2,13) Hurwitz map, while (H1) holds on the congruence maps. B_H ∩ N_H = T_H (164) holds, as he proves. Part of his table of |Z'_n| on 79/143 is wrong (his, as the scan shows), and GP(1, Z/5Z) is A₅ × {±1}, not his "S₅ ?" (79/273).
- **R8a (SA01-R75-01 to -05; SA01-K75-01).** Over O_p = Z[2cos(2π/p)] the general regular p-gon of 75/33 degenerates (4 − α² = 0) exactly at the primes above q when p = q^k or 2q^k, and nowhere otherwise (the norm of 4 − α² computed for p = 3, ..., 30). The discriminants of 70/69 at the solids: tetrahedron 2 and −3, octahedron 4 and −12, cube 2 and −4, icosahedron φ² (a unit) and −3φ⁴, dodecahedron 1 and α² − 4 (of norm 5). A₅ = PGL(2, F₄) = SL(2, F₄) and S₅ = PGL(2, F₅) (computed). On 75/9 "u transitif ⇔ tous les n_i sauf un au plus sont nuls" is false; u is transitive iff Σ n_i = 1.
- **R8b (SA01-R81-01 to -13; SA01-K81-01 to -07).** Cote 81: the special Belyi functions f = P/Q and the Galois action on them check (81/2-6); the binary decompositions defined by a tree satisfy (*) and (**); the Proposition of 81/40 (C_{≥x} and C_{≤x} totally ordered in an ordered model) is false, already for the tripod, among the maquettes of all 18,247 labelled trees with 3-7 vertices; the four characterizations of non-panaché pairs (81/43-44) hold (computed for 27,474 pairs); the onglets of a non-crossing partition (81/49-50) check for N = 3, ..., 9; his gluing formulas of 81/54 hold as the ink has them (g = g' + g'').
- **R8c (SA01-R83-01, SA01 cote-83 reading).** On 83/003-016 the icosahedron over F₄ is checked exhaustively (12 vertices; edges Tr(uv) = α); 83/052-062: I° is the great icosahedron and the hemi-icosahedra are complementary.
- **R9 (SA04-R80-01, SA04-R82-01 to -03, SA04-R85-01 to -03, SA04-R86-01, -02, SA04-R87-01, SA04-R88-01, SA04-R89-01, -02).** A survey reading of cotes 80, 82 and 85-89: his vertex counts of pseudoline arrangements, the bracket of a rank-3 form, the flag counts and the list of spherical C_{p,q} check.
- **R10 (SA04-R93-01 to -13).** Both of his "j'ignore" questions on 93/066 have positive answers: (g) holds on E_∞ without the restriction to relative polyhedra (compact members of C_∞ are ANRs, hence of finite CW homotopy type), and (a)-(e) characterize χ and χ_! on all of E_∞. His doubt about compact triangulability is right from dimension 4 on. The stage-A dossier reached the finite-homotopy-type argument independently, under compactness, metrizability and recursive local contractibility, and refuted the broad preliminary fibration formula by a telescope example, not the narrowed conical question (C-SA04-50 to -70, §3.3 of `SA04_dossier.md`).
- **R11 (SA04-R101-01 to -03).** His question on 101/016 has a positive answer for every complete local noetherian domain A ≠ K: Ext^i_A(K, A) = 0 for every i (A is pure-injective, hence cotorsion). Corollary 2 and Proposition 10 of the 1958 notes are right.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1 (A.1).** The scheme of pinned realizations of a regular {p, q} degenerates exactly over the Coxeter discriminant (the factor α + β, which puts the centre at infinity), the squared Gram entries (α + 2, β + 2) and the factor α − 2 of δ, which his remark on 70/70 attaches to the circumscribed quadric through a vertex; for [p₁, ..., p_n] the same holds with det Gram[p₁, ..., p_n] and the continuant L_n of R2.
- **L1a (A.1).** The invariant-subspace theorem of 72/80-83 is the pinned analogue, over any field, of Vinberg's irreducibility criterion for linear Coxeter groups: the tridiagonal matrix of 72/14-17 is a Cartan matrix, β_i = 0 is decomposability, and ρ is its determinant. Over S₀ the relations η_i² = εη_i leave at most seven of his ten classes independent; whether Br(f_V) ≠ 0 at the generic point is a Hilbert-symbol computation over Q(β₀, β₁), the first case of his open problem of 72/113.
- **L2 (A.2).** His axioms To 1-To 8 with (H1) for every element of Z'_n, or the multigraph axioms of §XI with the isomorphy and homogeneity conditions, characterize the congruence triangulations SP_{M,i} (Λ = Z/n) among the regular triangulations of type {3, n}; the criterion amounts to Wohlfahrt's level and the generation of the cartographic group mod n. His §XI.3 turns a homogeneous graph with homotheties into pinned group data (H, U₀, T_H, N_H) with the conditions a)-d) of (163), so the question becomes one about these data for H = PSL(2, Z/n) against the other quotients of the (2, 3, n) triangle group.
- **L3 (A.3).** For p ≥ 5 there is no regular system of p vertices over Z with an étale regular p-gon at p: the rotation group is a ±1-twist of μ_p, whose Galois module χ_cyc·ε cannot be unramified at p unless p − 1 | 2. Likewise there is no SR(2p)S over Z[1/2] for p ≥ 5.
- **L5 (A.4).** The essential image in Th. 1 of 76/39 is the class of free G_n-sets whose ⟨σ₀, ..., σ_{n−1}⟩- and ⟨σ₁, ..., σ_n⟩-orbits realize spheres, recursively; it is decidable for n ≤ 4 (crystallization theory; 3-sphere recognition) and undecidable for large n (Novikov).
- **L6 (B.1).** If φ: Y → E of 74/128-130 is injective for every ν, then φ(Y) is a union of free orbits of im u, so |im u| divides |Y| = 4c, with |im u| = 2^c when c + 1 is odd and 2^(c+1) when c + 1 is even; that leaves exactly c ∈ {0, 1, 2, 4}, a proof of the classification of the GQ(2, c) by his own torsors, without Higman's inequality.
- **L7 (B.2).** His closure condition is the Bol closure condition of web geometry: the 3-nets satisfying it are those of the left Bol loops, as his derivation of (b(xb))c = b(x(bc)) on 74/14-16 suggests.
- **L7a (B.5).** His ordered models ("maquettes ordonnées", 81/38-40) are the finite nested poc-sets, i.e. compatible split systems, and every one is the ordered model of a unique finite tree, recovered from its intervals, which are chains. His (28 a) is the form of nestedness in which exactly one of the four relations holds up to σ.
- **L8 (B.3).** The "Opérations sur systèmes de Schwartz" (85/082-094), with S₃ and Ẑ^× acting on triples (h₀, h₁, h₂) with h₀h₁h₂ = 1, are the operations on regular maps and hypermaps of Jones and Thornton (1983).
- **L9 (C.1).** On E_∞ his χ_! agrees with the o-minimal Euler characteristic of locally closed definable sets, whose one-point compactifications are locally conical by definable triangulation.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for every dimension
proved in low dimension without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made
and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA04_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. His arithmetic theory of regular polytopes (cotes 70, 72, 76-79). The main question is A.1.**
- **A.1 (main).** The "Programme provisoire d'une théorie arithmétique des polyèdres réguliers" (70/122-123), for every regular type τ = [p₁, ..., p_n].
  - (a) Define his functor of k-realizations of τ (possibly degenerate: a projective space P of dimension n with a section s₀, a hyperplane at infinity, and a set Φ of projective subspaces ordered like Φ_τ, with his conditions 1)-4)) on all rings, prove that it is represented by a scheme of finite type over Z, and determine that scheme, starting from his universal pinned realization over Z[α₁, ..., α_n] cut out by the half-cyclotomic conditions (70/4-26, 68; cote 72).
  - (b) For every n, determine the invariant quadratic function and its discriminants (R1 for n = 2, R2 for n ≤ 5), and settle L1: determine the locus of Spec Z[α₁, ..., α_n] where the realization degenerates, with the five Platonic solids, the star polyhedra, the infinite polyhedra and the icosahedron in characteristic 5 as test cases.
  - (c) Settle his two open questions of cote 70: whether D_i(Π) → Grass_i(E) is injective (70/22), and his question (26) of 70/118-119, whether the maps N\Φ_H → Ψ_H(P) are bijective for a split regular polyhedron P over a base.
  - (d) The general regular icosahedron of 75/33: construct the universal pinned realization of {3, 5} and {5, 3} over Z[φ], or over the ring it requires, with its invariant quadric, and determine its fibres in characteristics 2, 3 and 5 (R8a). Relate the fibre in characteristic 2 to A₅ ≅ SL(2, F₄) and the icosahedron over F₄ of 83/003-016, and the fibre in characteristic 5 to P²(F₅) (R1) and the bi-icosahedra of 83/052-062 (R8c).
  - (e) His open problem of 72/113: determine the total Stiefel-Whitney class and the Brauer class of the generic smooth invariant form, starting with n = 2, and settle L1a, including the invariant-subspace theorem of 72/80-83 as a pinned Vinberg criterion.
- **A.2.** Cote 79, the congruence triangulations SP_M and his axiomatics of "structures triangulaires congruentielles" (§§VI-VIII, To 1-To 8) and of the graphs and multigraphs "à homothéties" (§§IX-XI).
  - (a) Settle L2: determine whether his axioms characterize the SP_{M,i} among the regular triangulations of type {3, n}, that is, whether every regular map of type {3, n} that satisfies them is a congruence quotient of the Farey map; work through his pinned group data (H, U₀, T_H, N_H) of §XI.3 (R8; SA04-R79-05, -06, -09, -13, -17 are the evidence so far).
  - (b) Prove that M is the enveloping group of its triangulated structure with antipodism for every n ≥ 3 and for Λ = Z (79/83; computed for n = 3, ..., 8).
  - (c) Prove or refute his bound "distance 0, 2 or 3" of §X.1.
- **A.3.** Settle his questions b) and c) of 78/48-49: prove or refute L3, and prove that regular systems of n vertices exist over Z for n = 3 and 4 and over Z[1/2] for n = 6, with explicit examples.
- **A.4.** Determine the essential image of the functor of Th. 1 (76/39) from his finite n-manifolds with regular filtrations to free G_n-sets, for every n, and settle L5.

**B. Graphs, nets and incidence structures (cotes 69, 74, 80, 85-89).**
- **B.1.** Prove or refute that φ: Y → E of 74/128-130 is injective for every graph satisfying his Axioms 1-2 of 74/93 (every edge in a unique triangle; every point off a triangle linked to exactly one of its vertices), and with it settle L6. Then prove, for each c ∈ {0, 1, 2, 4}, the uniqueness of 𝒯_ν by his reconstruction from a base triangle (74/93-106, Props 1-5), answering the two questions to which he reduces the classification on 74/103-104.
- **B.2.** His questions on 74/6-13: is the functor φ from groups with bitorsors to 3-nets an equivalence onto a subcategory he can name, and which 3-nets does it reach? Determine the class of 3-nets satisfying his closure condition (f₃f₂f₁)² = id at every point, and settle L7.
- **B.3.** From the text of 85/082-094, state what he proves about the operations on Schwarz systems, prove or refute each statement, and settle L8.
- **B.4.** Cote 80: state precisely and prove or refute his counts of affine pseudoline arrangements ("n = 4: 1, n = 5: 6"), against the known enumeration, and his reconstruction statement of 80/071 (the map is determined by the oriented arrangement when no line bounds a monogon or a bigon).

- **B.5.** Cote 81. Settle L7a: prove or refute that the ordered models of 81/38-40 are exactly the finite nested poc-sets and that each is the ordered model of a unique finite tree, with the true form of his abandoned Proposition of 81/40 (R8b). Then determine whether the ordered models and non-crossing partitions of 81/26-53 and the edge gluing of 81/54 supply the local data of the surface of relative positions of 154/46-76 ("rives", birive and monorive edges, folded maps, polygon structures, polygonal transport): for each statement of 154/46-76 that uses such a structure, prove its counterpart in the language of cote 81, or show that cote 81 has none.

**C. Euler characteristics of locally conical spaces (93/55-66).**
- **C.1.** Write the complete theorem of 93/066 on E_∞, with both of his questions answered (R10; check SA04-R93-11 and -12 in full). Then settle L9: for every o-minimal expansion of the real field, does E_∞ contain the locally closed definable sets, and does his χ_! agree there with the o-minimal Euler characteristic?

**D. His 1958 notes on local cohomology (cote 101).**
- **D.1.** State each characterization of 101/031-043 precisely: Propositions 13-16, the closing theorem, Problem C, and his margin that no two of the three conditions on Ext^{n−1}, Ext^n and Ext^{n+1}(k, M) are enough. Prove or refute each. For the margin, give for each pair of conditions a module satisfying the pair and not the conclusion, or prove that the pair is enough. Compare with Bass (1963) and Roberts (1983).

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- J. E. Humphreys, *Reflection groups and Coxeter groups* (CUP, 1990), ch. 2 and 6; H. S. M. Coxeter, *Regular polytopes* (3rd ed., Dover, 1973).
- P. McMullen and E. Schulte, *Abstract regular polytopes* (CUP, 2002); M. Ferri, C. Gagliardi and L. Grasselli on crystallizations (1986); J. H. Rubinstein (1995) and A. Thompson (1994) on recognizing the 3-sphere.
- H. S. M. Coxeter and W. O. J. Moser, *Generators and relations for discrete groups*, ch. 8; G. A. Jones and D. Singerman, "Theory of maps on orientable surfaces", Proc. London Math. Soc. 37 (1978); G. A. Jones and J. S. Thornton, "Operations on maps, and outer automorphisms", J. Combin. Theory Ser. B 35 (1983); K. Wohlfahrt, "An extension of F. Klein's level concept", Illinois J. Math. 8 (1964).
- M.-A. Knus, *Quadratic and Hermitian forms over rings* (Springer, 1991); O. Loos, Math. Z. 257 (2007); J. Voight, J. reine angew. Math. 657 (2011); M. M. Wood, "Gauss composition over an arbitrary base", Adv. Math. 226 (2011).
- F. Oort and J. Tate, "Group schemes of prime order", Ann. Sci. ENS 3 (1970).
- É. B. Vinberg, "Discrete linear groups generated by reflections", Izv. Akad. Nauk SSSR Ser. Mat. 35 (1971), §§1-2.
- P. Buneman (1971) on compatible splits; M. J. Dunwoody (1979) on nested sets; M. Roller, "Poc sets, median algebras and group actions" (1998); M. Sageev (1995).
- S. E. Payne and J. A. Thas, *Finite generalized quadrangles* (1984; 2nd ed. 2009), §§1.2, 5.3, 6.1.
- W. Blaschke and G. Bol, *Geometrie der Gewebe* (Springer, 1938); H. O. Pflugfelder, *Quasigroups and loops: introduction* (Heldermann, 1990).
- A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler, *Oriented matroids* (2nd ed. 1999), ch. 6; D. E. Knuth, *Axioms and hulls*, LNCS 606 (1992).
- O. Hanner (1951) on ANRs; J. E. West, Ann. of Math. 106 (1977); L. van den Dries, *Tame topology and o-minimal structures* (CUP, 1998), ch. 4 and 8.
- H. Bass, "On the ubiquity of Gorenstein rings", Math. Z. 82 (1963); P. Roberts, "Rings of type 1 are Gorenstein", Bull. London Math. Soc. 15 (1983); W. Bruns and J. Herzog, *Cohen-Macaulay rings*, ch. 3.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the axioms assumed, the class of structures, finiteness and dimension
   hypotheses). Do not replace it by a convenient special case. If you prove a special case, name it as one and keep
   the general statement on your list.
2. Type every map and relation you introduce: source, target, the category or ordered set in which it lives, and each
   extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "refine to") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories or of fibred categories; a scheme against the functor it represents; isogeny against isomorphism; homotopy equivalence; an isomorphism of graphs or maps against an isomorphism of their flag systems.
5. Check the edge cases in scope: characteristic 2 and 3 and the primes dividing the discriminants; non-reduced, non-noetherian, non-normal and non-excellent bases; depth and etale depth exactly 1 and 2; rank one; the degenerate realizations (alpha = +-2, beta = -2); the small cases n <= 4; infinite families and non-compact spaces.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA04_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA04_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA04_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA04_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
  statement number); then what you read, what you computed (every program with its scope, counts and run time), and
  every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as SA04-R93-11; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA04_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
