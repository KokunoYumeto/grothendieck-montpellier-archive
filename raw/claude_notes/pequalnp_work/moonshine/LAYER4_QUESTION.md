# Layer 4: the precise question (23 Nov 2026 ~22:1x UTC)

Claude Opus 5.5 at effort max (session 672ae3a0), for Codex and our own agents, at the user's question: [the user's words, omitted], after rereading the earlier discussion of the
layers (22 Nov, ~22:40-23:10 UTC). Hunches welcome, marked as such; no proofs expected.

## The frame from the earlier discussion (in standard terms)
- **Layers of the Grand RH = degrees:** 1 (GL1: zeta, Dirichlet, Hecke; Alpöge proves GL1 over Q), 2 (GL2: modular
  forms, modular curves), 4 (GSp4: spin L-functions of paramodular forms, abelian surfaces, Siegel threefolds), 27
  (E6, the Albert algebra).
- **The centres:** Alpöge's sign field as the centre mu2 = {±1} of SU(2) and SL2 (in his proof the one global sign that
  turns an alternating trace into an honest one); the ternary phase as mu3, the centre of SU(3), appearing on the GL1
  rung as cubic characters of Q(omega); mu6 = mu2 x mu3 = the units of Z[omega] (the hexagon).
- **"4 gets a weird Z2 thing":** Sp4 = Spin5 (B2 = C2); degree 4 is the spin representation, and the Z2 is the spin
  double cover.
- An earlier observation: paramodularity "is more layer 2 with hints of 3": the discriminant -3 appears inside
  paramodular forms, and genus-2 theta series indexed by binary quadratic forms connect the Euler product to the local
  spin factor.

## Tonight's identities at layers 2 and 3
- Metaplectic thetas: Alpöge's GL1/Q theorem is proved from a GL2 theta object, normalized quadratic Gauss sums on the
  double cover (layer 2, mu2); the next rung is the cubic version, cubic Gauss sums over Q(omega) as Fourier coefficients
  of the Kubota-Patterson theta on the 3-fold (with mu6, 6-fold) cover (layer 3, mu3).
- Planes and codes: PG(2,2) -> Hamming -> E8 (layer 2); PG(2,3) -> tetracode (Aut = GL(2,3)) -> ternary Golay -> Leech
  over Z[omega] (layer 3).
- Leech: centre mu2 of Co0 (the sign; the orbifold by -1 gives the Monster module); mu6 = mu2 x mu3 the centre of 6.Suz.
- GL(n): Sym^2 GL2 -> GL3; GL2 x GL3 -> GL6 (2 x 3 = 4 + 2 for Sym^2).
- The S6 Paper II example: six points over three branch values match six 2-torsion points of a genus-2 Jacobian
  (S6 = Sp4(F2)); 4-torsion breaks the symmetry.

## Layer 4 candidates, one per chain (to sketch and to test as one object)
1. **Automorphic:** GSp4 inside GL4: spin L-functions of genus-2 Siegel (paramodular) forms, abelian surfaces =
   Jacobians of genus-2 curves (paramodular conjecture; on disk: arXiv 2310.13179, 2412.14289, 2308.09824); also Sym^3:
   GL2 -> GL4 (Kim-Shahidi) and GL2 x GL2 -> GL4 (Ramakrishnan).
2. **Metaplectic:** the quartic (biquadratic) theta on the 4-fold cover over Q(i): Fourier coefficients involve quartic
   Gauss sums and are only partly known (Eckhardt-Patterson) [verify]; mu4 = units of Z[i], the square lattice and the
   (2,4,4) triangle group; the order-4 phase version of Alpöge's power-sum lemma (i^n in place of (-1)^n).
3. **Planes and codes:** PG(2,4) -> the hexacode over F4 (automorphism group 3.A6, with 3.S6 semilinear) -> the binary
   Golay code (sextet stabilizer 2^6:3.S6 in M24) -> Leech.
4. **The mod-2 shadow:** Sp4(F2) = S6: the S6 example's level-2 symmetry (genus 2), the S6 of the hexacode and sextets,
   the double-six stabilizer S6 x 2 in W(E6) (Albert side), and the umbral group 3.S6 at lambency 6+3 (Niemeier D4^6)
   [verify against Cheng-Duncan-Harvey].

## The questions
1. Sketch layer 4 in each chain. Are the four candidates one object: is the GSp4 (genus-2, paramodular) rung the
   automorphic face of the S6 = Sp4(F2) that appears in the hexacode, the double-six and lambency 6+3, the way layer 3's
   GL(2,3) sits in the tetracode and (if confirmed) lambency 6?
2. Where does the "weird Z2" (Spin5 -> SO5) enter on each chain: in the 2^6 of 2^6:3.S6, in the spin cover of the quartic
   theta, in the 4-torsion break of the S6 example?
3. What would the order-4 phase version of Alpöge's sign mechanism need, and does it land on GSp4 spin L-functions or on
   Hecke characters of Q(i)?
4. The earlier "paramodularity is layer 2 with hints of 3" (discriminant -3 inside paramodular forms): how does it sit
   with layer 4 = GSp4? Is the -3 the mu3 of layer 3 seen from inside layer 4?
