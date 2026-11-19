# SA10, Espaces stratifiés: research packages, in concept

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

These are concepts only. No prompt is written tonight.

## P1. The gluing theorem for tubes, corrected (H1, H2)

**The question:**
- For which stratified spaces is X the colimit, in topoi, of the diagram of its strata, its tubes and its deleted tubes?
- Which stones are needed: all pairs i < k, the V^j_{i,k} of 151/60, or an iterated gluing?
- Does his van Kampen principle (151/43) hold for that colimit? It says that the homotopy type of a glued topos is the colimit of the homotopy types.

**Why it matters:**
- It is the theorem the 1981 stratified topos is built for.
- As stated on 151/69 it is false (SA10-S3-K3), and the page gives no proof.

**What it rests on:** 151/32-75 (read in full; SA10-16, SA10-17); 151/1-31 (SA10-15); the normal-crossings pieces of "Str_∞ p. 84" (probably cote 150, SA10-12).

**Strongest known reduction:**
- The two-stratum case is formal for germ topoi: Sh(X) is the fibre product of Sh(X ∖ Y) and Sh(germ of X along Y) over Sh(deleted germ).
- The successor-pair diagram is refuted by ℂ ⊃ ℝ ⊃ {0}.
- The unzipping of Ayala-Francis-Tanaka is a known iterated framework.

**Material:**
- the MPL_151_032-075 and MPL_150_085-099+151_001-031 `.tex`, with the 151 scans;
- the cote-150 `.tex` for Str_∞;
- Treumann 2009; Lurie, *Higher Algebra*, App. A; Ayala-Francis-Tanaka 2017;
- SGA 4, Exposé IV §9 (recollement).

## P2. The stratified homotopy type of M̄_{g,n} from Teichmüller groupoids (H3, H5)

**The question:** carry out the programme of 151/44 for M̄_{g,n}, as an orbifold or stack:
- its homotopy type (or profinite homotopy type) from the Teichmüller groupoids of the strata;
- the inertia-decomposition data (151/34, (14)) at each boundary stratum;
- the gluing of P1.

The poset of strata lacks infima in general (EXIT_TOWER A.2). What replaces the half-simplicial formalism of 151/45-56?

**Why it matters:**
- It joins the stratified-spaces material of the archive to La Longue Marche, on which the research runs stand.
- It is his own stated motivation.

**What it rests on:**
- 151/32-44 and 57-69;
- cote 150, folios 9 and 15-16 (EXIT_TOWER);
- La Longue Marche (the Teichmüller tower);
- the Esquisse §2-3.

**Strongest known reduction:**
- EXIT_TOWER A.1-A.3 and A.12 are proved; A.11 and A.13 are refuted.
- The strata of M̄_{g,n} are products of moduli spaces M_{g′,n′}, which are K(π,1) orbifolds.

**Material:** the EXIT_TOWER return; the 150-151 `.tex` with the scans; the Longue Marche edition; the literature on the Teichmüller tower and on the boundary of M̄_{g,n}, to be chosen by the main session.
