# FIND_ag — moonshine in the algebraic-geometry and Hodge places

By Claude Opus 5.5 at effort max (one agent of the moonshine swarm of 23 Nov 2026; domain: the user's algebraic-geometry
and Hodge places). Read-only on every source; nothing published, sent or pushed. Running notes:
`<local>/Documents\agent_notes\moonshine_find_ag_NOTES.md`.

**What an entry is.** One appearance of the structure (object, exact statement or formula as the source writes it, locator,
what the source uses it for). No entry is judged; nothing was dropped for looking peripheral. Name collisions that are not
the objects of the brief (Néron–Ogg–Shafarevich for "Ogg", "hyperelliptic genus" for "elliptic genus", summation indices
`j=0`, cusp singularities, punctures called cusps, `M_{12}` matrix entries, digits inside long certificate integers that
happen to contain 196883/196884/744) are listed once in §8 and not entered.

**Flags.** [read] = the passage was opened and read at the locator for this file. [scan] = the line was found by the bounded
scan and read in its line (and neighbours where quoted); the surrounding proof was not read. [mine] = a one-line arithmetic
remark of mine, checked by hand, not in the source.

**Path prefixes.**
- `RR\` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\`
- `LM\` = `<local>/Documents\longue_marche_pro_pilot_20261104\answers\`
- `PRO\` = `<local>/Documents\TO_SEND\PRO\1_Archive_research_by_topic\`
- `R20\`, `R22\`, `R23\` = `<local>/Documents\reports_20261120\`, `...\reports_20261122\`, `...\reports_20261123\`
- `HEX` = `<local>/Documents\field_experts\hexagon\HEXAGON_STATUS.md`
- `INT\` = `<local>/Documents\field_experts\intake_20261121\intakes\`
- `PAP\` = `<local>/Documents\recent_results_20261110\papers\` (PDFs read through `pdftotext`; line numbers are those of
  the text extraction)
- `FM\` = `<local>/pequalnp_work\fleet_map\maps\`

**Where the run names point.** Returns of the AG/Hodge prompts: HODGE_SIGN (32), TRACE_DET (33), DP_MULT (34), ZETA_TWO (35),
THETA3 (37), HECKE_DIV (38), GHOSTS (39), JAC1964 (40), DEG_L (41), GRH_ALGORITHMS(+_FINISH) (67, 67c), HODGE_BOUNDED_CYCLES
(70), HODGE_FINISH (70c), POLISH_ALGEBRAIC_GEOMETRY / POLISH_TOPOLOGY_PERIODS / POLISH_CRISTAUX (90-92), AN_GRH (30), K17 (31),
KTOWER, HODGE_DIVISION (46), SIGN_NEXT (45), ZETA_NEXT (43), ZETA_HEAT (62), C44_POS, ARCH_ALG, DELTA23 (29, pointed to by the
H17 records). Longue Marche runs pointed to by the H17 records: SECTION_GHOSTS, EXIT_TOWER, GT_TOWER_CHECK, LM7_PUSH,
DELTA_ON_GT. The models: the runs are GPT-6 Astra (ChatGPT Pro mode); the notes as their own headers state.

---

## 1. j, the j-line, CM curves, modular functions and forms, theta, Hecke

**AG-001** — modular group, the two elliptic points, the CM curves of j = 1728 and j = 0. [read]
"The modular group $B=B_3/\langle(uv)^3\rangle\cong C_2*C_3$ is the orbifold fundamental group of the moduli of elliptic curves
up to $\pm1$, based at the cusp. Put $s=uvu$, $r=uv$; they generate the stabilizers of the two elliptic points, the curves
$y^2=x^3-x$ and $y^2=x^3+1$ with complex multiplication by $\Z[i]$ and $\Z[\omega]$."
Locator: `R23\h17_note\h17_note_wb0007.tex:125-127` (Hexagon hexagon:2611.00940, WB-0007). Context: the frames of an element of
GT̂₀ at the two elliptic points are compared at level 12; Theorem 3 says the comparison character vanishes on normalized elements.

**AG-002** — the number $(3/4)^{1/4}$ and the division fields of the j = 0 and j = 1728 curves. [read]
"For a Galois element with $\lambda=1$ both record the sign by which it moves $(3/4)^{1/4}$: this number generates the
$4$-division field of the curve with $j=0$ and the field of the $x$-coordinates of the $3$-division points of the curve with
$j=1728$, over the cyclotomic field." "Of the facts behind them, only the equality of the second of the two fields with
$\Q(i,(3/4)^{1/4})$ has been verified independently."
Locators: `R23\h17_note\h17_note_wb0007.tex:148-156`; check event `R23\h17_note\REVIEW_ae4ae3dc_v1_CHECK_EVENTS.tsv:16`
("Q(x(E_4[3])) = Q(i,(3/4)^{1/4}) verified by hand; Q(E_3[4]) = Q(i,r0) ... not verified"); DELTA_SEXTIC Theorem A check:
"Q^ab((3/4)^{1/4}) = Q^ab(√√−3)" (`R20\delta_sextic\DELTA_SEXTIC_20261121.md:75-76`). Context: arithmetic meaning of the two
bits a₂, a₃ of the character δ (cited, unrefereed, not used in the proofs).

**AG-003** — the three-division quartic of every elliptic curve is the j = 0 curve; $j/1728=-Z(P)^3$. [read]
"For $E:y^2=x^3+a_4x+a_6$, the points $t_j$ are the roots of the $3$-division polynomial $3x^4+6a_4x^2+12a_6x-a_4^2$, the curve
$E'$ is $t^2=x^4+2a_4x^2+4a_6x-a_4^2/3$, and with $X=(t+x^2+a_4)/2$, $Z=X-a_4/3$, $Y=Xx+a_6/2$ one finds
$Y^2=Z^3+\tfrac1{108}(4a_4^3+27a_6^2)$, $O'=\infty$, $P'=(-a_4/3,-a_6/2)$. So $E'$ is always the curve $E_0:Y^2=Z^3+1$ up to
isomorphism, and $(E,O)\mapsto P'$ identifies the moduli of elliptic curves up to $\pm1$ with the quotient of $E_0\setminus O'$
by $\mu_6=\Aut(E_0)$."
Locators: `R23\h17_note\h17_note_wb0007.tex:814-825` (Step 5 of Prop. 18); the same identity as EXIT_TOWER (E.259),
`LM\EXIT_TOWER_checkpoint_28_20261116T1443Z_unzipped\extracted_20261116\sections\E_cm_parity_vanishing.tex:219-244` ("At
$b=0$, $P$ is a nonzero two-torsion point; at $a=0$ it is a nonzero three-torsion point ... $u=i$ induces the elliptic
involution, while $u=\zeta_6$ induces multiplication by $\zeta_3^2$"); and DELTA_SEXTIC §4: "So the 3-division quartic of every
elliptic curve is equianharmonic, and E ↦ P identifies the modular orbifold with (E₀ ∖ O)/μ₆, E₀: Y² = Z³ + 1, with
j/1728 = −Z(P)³. This is the fibre of M₁,₂ → M₁,₁ over the hexagonal point." (`R20\delta_sextic\DELTA_SEXTIC_20261121.md:106-111`).
[mine] With $\Delta_E=-16(4a_4^3+27a_6^2)$ the constant is $(4a_4^3+27a_6^2)/108=-\Delta_E/1728$ (16·108 = 1728).
Context: the "hexagonal self-similarity" (H) that carries GT̂ through genus one; it proves Δ = 0 on GT̂.

**AG-004** — the j-line minus {0, 1728, ∞}; the unit $1-1728/j$. [read]
"Set $X=\mathbb P^1_{\Q}\setminus\{0,1728,\infty\}$ and $u=1-1728/j\in\mathcal O(X)^\times$. Its Kummer class has geometric
boundary residues $(1,1,0)$ in $\Ftwo$, ordered as $(0,1728,\infty)$. ... This class is not by itself a comparison of the two CM
frames." Proof: "The divisor on the coarse projective line is $[1728]-[0]$, and $u(\infty)=1$."
Locator: `LM\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\sections\A.tex:123-146` (A.5). Context: the proposed
product formula for Δ as a third local sign.

**AG-005** — an explicit degree-5 cover of the j-line (the $A_4\subset A_5$ resolvent of $X(5)$). [read]
"The degree-five cover has model $j=t^3(t^2+5t+40)$, $j-1728=(t-3)(t^2+4t+24)^2$. The branch cycles on five letters have types
$3\,1^2$, $2^2\,1$, and $5$. Thus its orbifold has cone orders $2,3,3$, at $3,r_+,r_-$, and one cusp, where
$r_\pm=(-5\pm3\sqrt{-15})/2$. Its full profinite group is $C_2\amalg C_3\amalg C_3$." "Put $k=\mathbb Q(\sqrt{-15})$. The affine
coordinates $j'_\pm=1728(t-r_\pm)/(3-r_\pm)$ identify the first two filled orbifolds with the standard $(2,3,\infty)$ orbifold
over $k$." Before it: "The corresponding cover is $X(5)$ with its twelve cusps removed ... Explicitly they are $0,\infty$ and
$\zeta_5^i\varphi,\zeta_5^i\bar\varphi$, with $\varphi=(1+\sqrt5)/2$."
Locator: `LM\SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\sections\part_E_symmetry_audit.tex:380-438`.
[mine] check: $(t-3)(t^2+4t+24)^2=t^5+5t^4+40t^3-1728$. Context: resolvent homomorphisms used to show a residual group Z
acts faithfully (Belyi faithfulness).

**AG-006** — Hauptmodul of $X_0(6)$, its cusps and Atkin–Lehner involutions. [read]
A.42 (Known): "A rational Hauptmodul is $h(\tau)=\frac{\eta(\tau)^5\eta(3\tau)}{\eta(2\tau)\eta(6\tau)^5}$, $u=h+9$. Its four cusp
values in the $u$ coordinate are $0,1,9,\infty$. Thus $Y_0(6)\simeq\mathbb P^1\setminus\{0,1,9,\infty\}$ over $\mathbb Q$. The
Atkin–Lehner involutions are $w_2(u)=\frac{u-9}{u-1}$, $w_3(u)=\frac9u$, $w_6(u)=\frac{9(u-1)}{u-9}$ ... act on the ordered
cusp list $(0,1,9,\infty)$ as $(0\ 9)(1\ \infty)$, $(0\ \infty)(1\ 9)$, $(0\ 1)(9\ \infty)$." Maier (2009) Table 2 gives cusp
values $0,-8,-9,\infty$ for the reciprocal-scaled Hauptmodul; Colò (2022) App. A, p. 245.
A.43: "The geometric fibre of $\mathcal M_{0,5}\to\mathcal M_{0,4}$ over the ordered point $9$ is $\mathbb P^1\setminus\{0,1,9,\infty\}$
and its completed fundamental group is $\widehat F_3$. This yields the abstract identification with the completion of
$\Gamma_0(6)/\{\pm I\}$." A.44: "the level-six Atkin–Lehner defect is well typed".
Locator: `LM\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\sections\A.tex:1505-1569`; also
`...\DELTA_ON_GT\agent_five\research_notes.md:11`. Context: a candidate route from the five-point sphere to the modular group
for the invariant Δ; "No vanishing of Δ follows from A.42 alone."

**AG-007** — $X(3)$, $X(4)$ over the j-line; an orbifold cover $(3,3,2)\to(3,2,4)$. [read]
A.41: "The map $w=4z(1-z)$ is a degree-two orbifold covering from the sphere with weights $(3,3,2)$ at $(0,1,\infty)$ to the sphere
with weights $(3,2,4)$ at $(0,1,\infty)$ ... the orbifold Euler characteristics are $1/6$ and $1/12$. ... It must not be
identified without a comparison with a map of the principal modular covers $X(3),X(4)$ over the same $j$-line. Neither principal
subgroup contains the other: $T^3$ belongs to $\Gamma(3)$ but not $\Gamma(4)$, and $T^4$ belongs to $\Gamma(4)$ but not
$\Gamma(3)$. ... The subgroup $A_4\subset S_4$ gives the abstract spherical-orbifold map."
Locator: `LM\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\sections\A.tex:1486-1503`.

**AG-008** — η as a level-12 theta function; the character $\chi_{12}$ and the sign of Δ. [read]
A.27: "For $r\in\mathbf Z/12$ define $\theta_{6,r}(\tau,z)=\sum_{n\equiv r\;(12)}q^{n^2/24}e^{2\pi inz}$ ... All four units
$u\in\{1,5,7,11\}$ satisfy $u^2=1\pmod{24}$; thus they preserve the finite quadratic module $A=\mathbf Z/12$,
$q_A(r)=r^2/24\pmod{\mathbf Z}$. ... Euler's pentagonal identity gives
$\eta(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n)=\sum_{n\ge1}\chi_{12}(n)q^{n^2/24}=\theta_{6,1}(\tau,0)-\theta_{6,5}(\tau,0)$ ...
$P_u\eta=\chi_{12}(u)\eta$, $\chi_{12}(u(\Phi))=(-1)^{\delta(\Phi)}$." "the R2 element acts by $P_5$ and gives eta eigenvalue
$-1$; a lift with parities $(0,1)$ acts by $P_7$ and has the same eta eigenvalue."
Locator: `LM\DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\sections\A.tex:954-997`. Context: "This construction
packages the known character; it does not derive its restriction to $\widehat{\mathrm{GT}}$."

**AG-009** — the η multiplier, $\nu_{\eta^2}:\mathrm{SL}_2(\mathbf Z)\to\mu_{12}$, and its central table. [read]
A.31 (Known): "$\eta(M\tau)=\exp\!\left(\pi i\left(\frac{a+d}{12c}-s(d,c)-\frac14\right)\right)(c\tau+d)^{1/2}\eta(\tau)$ ...
$\eta(\tau+1)=\zeta_{24}\eta(\tau)$, $\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau)$. ... Its square descends to a character
$\nu_{\eta^2}:\mathrm{SL}_2(\mathbf Z)\to\mu_{12}$, with $T\mapsto\zeta_{12}$ and $S\mapsto\zeta_{12}^{-3}$. The attached exact
enumeration constructs a homomorphism $e:\mathrm{SL}_2(\mathbf Z/12)\to\mathbf Z/12$, $e(T)=1$, $e(S)=-3$. It enumerates all
$1152$ determinant-one matrices and verifies all $4608$ right-generator edges ... on the scalar centre the exact table is
$u$: 1, 5, 7, 11; $\nu_{\eta^2}(uI)$: 1, 1, −1, −1; $\chi_{12}(u)$: 1, −1, −1, 1; and the first row is $\chi_{-4}(u)$."
Locator: `...\DELTA_ON_GT\sections\A.tex:1159-1214` (Atiyah 1987, (1.3)-(1.4), Thm 5.60 cited; program
`...\agent_literature\check_eta_character.py`). Context: "It does not identify the actual frames with these central matrices:
A.25 refutes that identification."

**AG-010** — Masser's CM formula; $E_2^*,E_4,E_6$ and the zero set $\{j=0,1728\}$. [scan, statements read in registers]
RESEARCH_SA07 A.4.5: "For imaginary-quadratic tau with j≠0,1728, the modular-polynomial value gamma∈Q(j) gives
Psi=3E4E2*/(2E6)=9j gamma+3(7j−6912)/(2(j−1728)) and h=(g3/g2)Psi, while h=0 at j=0 and 1728"; A.4.6: "For every complex elliptic
curve in the fixed short-Weierstrass normalization, h=0 holds exactly at j=0 or j=1728"; A.4.8: "For j≠0,1728, the
almost-holomorphic modular function chi* satisfies chi*=(2/3)(j−1728)Psi and h=3g3 chi*/(2g2(j−1728))". Derivation note:
"Use j=1728 E4^3/(E4^3-E6^2), so j-1728=1728 E6^2/(E4^3-E6^2). ... (2/3)(j-1728) Psi = 1728 E2* E4 E6/(E4^3-E6^2) = chi*."
Locators: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped\notes\paper03_register_summaries.tsv:20-23`;
`...\notes\paper03_elliptic_statement_first_04.md:13-17`; `RR\ZETA_TWO_final_20261121T0032Z_unzipped\FLAG_AUDIT.tsv:124`
(source `RESEARCH_SA07/sections/A_elliptic.tex:199`). Context: Paper 3 of POLISH_TOPOLOGY_PERIODS (Grothendieck's period
conjecture, cote 18): algebraicity of the quasi-period invariant h.

**AG-011** — the Weierstrass mock modular form and the reduced theta function. [scan]
A.4.10: "In the specified optimal modular-elliptic normalization, the regularized lattice sum equals h and the holomorphic
Weierstrass mock modular form is zeta(E_E(q))−h E_E(q)". A.4.26: "The reduced theta function exp(−h u²/2)sigma(u) and Kronecker
function exp(−h uv)sigma(u+v)/(sigma(u)sigma(v)) have exact coefficient field k(h)".
Locator: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped\notes\paper03_register_summaries.tsv:24, 40`.
(Cross-listed under §4.)

**AG-012** — $y^2=x^3-x+1$, $j=-6912/23$: counterexample to Grothendieck's strong transcendence conjecture. [scan + HEX read]
"The real elliptic curve y²=x³−x+1 has nonintegral j=−6912/23 and is non-CM, so its dimensions are (g,b,l,u,v)=(4,3,2,1,0)";
certificate: "complex counterexample: discriminant=-368, j=-6912/23"; "This rational number is not an integer:
`6912=23·300+12`. A rational algebraic integer is an integer ... so `E` has no CM."
Locators: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped\notes\paper03_incorporation_crosswalk_186.tsv:10`;
`...\notes\paper03_new_certificate_output.txt:3`; `...\notes\paper03_joint_torsor_fresh_worker_frozen.md:573-588`;
`HEX` row P91a; prompt `PRO\SENT\91_POLISH_TOPOLOGY_PERIODS\PROMPT.md:74`.

**AG-013** — a non-CM curve with $j_0=1/(2+i)$. [scan]
A.3.4: "For j0=1/(2+i) and c=j0/(j0−1728), the curve y²=4x³−3cx−c has j-invariant j0, is non-CM, has no real model and is not
isogenous to its conjugate." Locator: `...\POLISH_TOPOLOGY_PERIODS_checkpoint_13...\notes\paper03_register_summaries.tsv:16`;
derivation `...\notes\paper03_broadening_statement_first_derivations_01.md:39` ("At the prime (2+i) of Z[i], j has negative
valuation").

**AG-014** — $E_6(i)=0$: erratum to Bhowmik–Pathak. [read, HEX]
"A counterexample to Bhowmik-Pathak 2024, Thm 1.11: at tau = i, E6 vanishes and the transcendence degree drops to 2".
Locator: `HEX:116` (row S07, stage N). Context: note to an author; source RESEARCH_SA07 cp12.

**AG-015** — the Fermat quartic is $X_0(64)$; its Jacobian is the cube of the j = 1728 curve. [scan]
"The Fermat quartic is \(X_0(64)\)"; "\(J\to E^2\times E'\), of degree a power of two, where \(E:y^2=x^3-x\) and \(E':y^2=x^3+x\).
Thus \(J\) is CM; over \(\overline{\mathbf Q}\) it is isogenous to the cube of a \(j=1728\) elliptic curve"; "$h_F(J)-3h_F(E_{1728})=\log(2)/4$";
"Bloch's isogeny gives $J\sim E^3$ geometrically, with $j(E)=1728$"; "All three elliptic quotients have $j=1728$".
Locators: `RR\JAC1964_checkpoint_06_20261121T0521Z_unzipped\JAC1964.tex:397, 8594-8596, 8951, 11364, 11602, 12105`.
Context: cote 44 (Grothendieck's 1964 Jacobians programme) in every characteristic.

**AG-016** — CM theta series of weight four, Fricke sign, generalized Heegner cycles, Frobenius' theta function. [scan]
"be the algebraic Hecke characters of the elliptic curves \(E:y^2=x^3-x\) and \(E':y^2=x^3+x\) ... Thus its normalized CM theta series
\(f(z)=\sum a_n e^{2\pi i nz}\) is a weight-four cusp form of level ..."; "The Fricke relation, with root number \(-1\) and weight four";
"The generalized-Heegner formula of Lilienfeldt--Shnidman"; "\(\phi\) is Frobenius' theta function with the normalization of de Jong
2020, Theorem 4.1, and \(a\) is any theta characteristic"; "\(\theta_2(i)=\theta_4(i)=2^{-1/4}\theta_3(i)\)".
Locators: `RR\JAC1964_checkpoint_06...\JAC1964.tex:11192-11232, 11308, 11646-11647, 11901, 12873-12879`.

**AG-017** — modular forms on $\Gamma_1(3)$: the theta series of $\mathbf Z[\omega]$, η-products, and the CM line. [read]
"$r_e=\dim S_e=\lfloor\frac{2e-2}{3}\rfloor$, $f_j=D a^{\,2e-5-3j}b^j\quad(0\leq j<r_e)$, where
$a=\sum_{\alpha\in\mathbf Z[\omega]}q^{N\alpha}$, $b=\frac{\eta(3\tau)^9}{\eta(\tau)^3}$, $D=\eta(\tau)^6\eta(3\tau)^6$." (Cléry–van der
Geer, arXiv:2110.00849, p. 12; Remark 15.2, p. 33: D is the weight-six cusp form.) Proposition KT-GL2-CM: "The CM subspace of
$S_e$ has dimension $c_e=1$ if $3\mid e$, $0$ if $3\nmid e$ ... When $3\mid e$, its unique normalized eigenform is the theta series
of the conductor-one Hecke character $\psi_e((\alpha))=\alpha^{2e}$ of $\mathbf Q(\omega)$. At a split prime $p=\pi\bar\pi$ its
eigenvalue is $a_p(\psi_e)=\pi^{2e}+\bar\pi^{2e}$." "The level formula forces the field to be $\mathbf Q(\omega)$".
Locators: `RR\KTOWER_checkpoint_11_20261122T0001Z_unzipped\KTOWER.tex:682-739`; same forms in K17 with
"$\psi=\eta(3\tau)^3/\eta(\tau)$" and "$D$ ... a weight-six cusp form": `RR\K17_checkpoint_08_20261121T0616Z_unzipped\K17.tex:3617-3661`.
Context: the GL₂ half of the K-groups-of-Z computation (Alpöge's step 17; HEX H18).

**AG-018** — algebraic modular forms on the compact unitary group $U(3)$ over $\mathbf Q(\omega)$. [scan]
"Write $E=\mathbf Q(\omega)$, where $\omega^2+\omega+1=0$, and $O=\mathbf Z[\omega]$. Let $G=U(h)$"; "algebraic modular forms of highest
weight $(e-1,0,1-e)$ at level $K$"; "At each split prime $p$, choose $\pi\in\mathbf Z[\omega]$ of norm $p$"; "Eisenstein integers: there
are six generators of each nonzero principal ideal". Locators: `RR\K17_checkpoint_08...\K17.tex:3151-3152, 4055-4058, 4173, 3697`;
prompt: "exact Hecke computations on compact U(3) over Q(√−3) and Q(√−7)" (`PRO\_superseded_65_K_GROUPS_OF_Z_inside_sent_75\PROMPT.md:22`).

**AG-019** — theta lifts of Hecke characters of a CM field to unitary groups: one machine for 032 and for Alpöge. [scan]
"Our expert found that the proof of Hodge for CM abelian varieties (032) and Alpöge's proof run on the same machine: theta lifts of
Hecke characters of a CM field to unitary groups." Locator: `PRO\SENT\37_HODGE_THETA_three_signatures\PROMPT.md:42-43`; sketch:
"Route 1. One machine in three settings: definite, signature (n,1), integral models (theta lifts of Hecke characters to unitary
groups)"; "splittings of the Weil representation, the Kudla–Millson kernels" (`R20\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md:28, 93, 103`).
THETA3 return: "step 8 iterated theta lifts on totally definite unitary groups, and step 12 a seesaw producing a Bessel period";
"Borade--Franzel--Girsch--Yao--Yu--Zelingher, On tori periods of Weil representations of unitary groups"
(`RR\THETA3_checkpoint_07_20261121T0604Z_unzipped\THETA3.tex:5850, 5897`).

**AG-020** — Alpöge's step 2: invariant derivation on a CM curve and the theta value. [read]
"Alp\"oge's announcement ... lists, as step 2 of its timeline, that $D^p\equiv0$ on a curve with complex multiplication at a prime
$p$ inert in the field of complex multiplication, and that $D^a\theta(0)/\Omega^a$ is divisible by
$p^{a/p+a/p^3+\cdots-O(\log a)}$". Locators: `R23\h09_note\h09_note_v4.tex:138` (Hexagon hexagon:2611.00938); Alpöge's remark,
step 2 (`RR\TRACE_DET_final_20261121T0218Z_unzipped\work\ALPOGE_remark.txt:127-131`); prompt 34: "On a CM curve the invariant
derivation D satisfies D^p ≡ 0 for p inert in K" (`PRO\SENT\34_DP_MULT_divided_powers_and_the_multiplicity_of_step_2\PROMPT.md:25`).
Also h09: Katz's "supersingular case of the Bernoulli--Hurwitz numbers of a curve with complex multiplication"
(`R23\h09_note\h09_note_v4.tex:55`).

**AG-021** — Alpöge's theta series' index (step 18) and the theta lifts (steps 8, 12, 16). [read]
"8. 11/15/26: Iterated theta lifts U (X0 ) → U (X1 ) → · · · → U (Xm ) between totally definite unitary groups, π ↦→ π ⊞ µj [t],
wins multiplicity m"; "12. 11/15/26: Seesaw: the period of the iterated lift is a Bessel period independent of the Hecke characters,
Rallis"; "16. ... via sixfold cover of GL5 automorphy of µ"; "18. 11/15/26: computation of covolumes, theta series' index,
congruences between lifts and forms." Locator: `RR\TRACE_DET_final_20261121T0218Z_unzipped\work\ALPOGE_remark.txt:182-207`
(copy also `RR\HODGE_SIGN_final_20261121T0057Z_unzipped\ALPOGE_remark_extracted.txt`). Our sketch: "The theta series' index of step
18 equals, up to explicit factors, the index of the span of ..." (`R20\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md:425`).
Chain length: "a chain of two lifts is excluded. Moreover $x^\epsilon>2^{300}$, $m>2^{7778}$ and $f>2^{33598}$"
(`R23\h30_note\h30_note.tex:38`).

**AG-022** — singular moduli on a special line of $Y(1)^2$. [scan]
"In $Y(1)^2$, the fixed special line $\{0\}\times Y(1)$ contains the full Galois orbits of $(0,j)$ for singular moduli $j$, with"
unbounded orbit sizes ("from the classical class-number description of singular moduli"); "This example persists at neat level. Fix a
lift of the first CM coordinate to a modular curve Y(N)".
Locators: `RR\HODGE_BOUNDED_CYCLES_final_20261123T0508Z_unzipped\HODGE_BOUNDED_CYCLES\workbench\work\UNFILED\v1\paper\galois.tex:30`;
`...\checks\records\galois_closed_locus_gate_report.md:40-42`. Context: "orbit size alone is insufficient" without the relative-Weyl
restriction.

**AG-023** — automorphisms and supersingularity at j = 0 and j = 1728. [scan]
SA06 A.8b: "For $p>3$, $O^*=\{\pm1\}$ except at $j=0$, where its order is $6$, and $j=1728$, where its order is $4$. These curves are
supersingular precisely ..." ; "forcing $u^4=1$ when $j=1728$ and $u^6=1$ when $j=0$"; "At $2$, use $y^2+y=x^3$ ... At $3$, use
$y^2=x^3-x$"; "Over $\overline{\mathbb F}_{11}$, the curves with $j=0$ and $j=1728$ ..." are supersingular.
Locators: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20_20261123T1600Z_unzipped\workbench\records\papers_5_6\STATEMENT_EXTRACTS.md:414-427`;
`...\REGISTER.tsv:271`; `...\QUESTIONS.tsv:150, 155`.

**AG-024** — counting supersingular j-invariants (Deuring, Eichler). [scan]
SA06 A.8a: "type number (s+r)/2 = s/2 + (h(-4p)+[h(-p)])/4 gives r = (h(-4p)+[h(-p)])/2 rational supersingular j-invariants"
(Deuring; Voight 2021, 30.9.2, 30.9.10). ZETA_TWO: "h(-p) and h(-4p) between √p/log log p and √p log log p up to constants; by
Deuring and Eichler the number of F_p-rational supersingular j-inva[riants]".
Locators: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\records\papers_5_6\INTAKE_CHECK_INDEX.tsv:383`;
`RR\ZETA_TWO_final_20261121T0032Z_unzipped\ANALYTIC_KEYWORD_HITS.tsv:8`; prompt 35: "SA06 A.8a: Littlewood bounds for supersingular
counts" (`PRO\SENT\35_ZETA_TWO_RH_for_schemes_and_motives_from_the_two_proofs\PROMPT.md:44`).

**AG-025** — the modular curve $X_0(11)$ and the curves of conductor 37 and 389. [scan]
"Take \[ E=X_0(11):\quad y^2+y=x^3-x^2-10x-20. \] Its discriminant is \(-11^5\), its conductor i[s 11]" (SA05:ex:B-X011, the counterexample in
R6 "without a BSD assumption"); "Let \(C/\F_2\) be the good reduction of the displayed \(X_0(11)\) model, and let \(A=C\times C\to C\)" (a
nonzero degree-two group on cote 12:78); "E_{11}:y^2+y=x^3-x^2-10x-20, E_{37}:y^2+y=x^3-x, E_{389}:y^2+y=x^3+x^2-2x" (different arithmetic
coranks). Locators: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\REGISTER.tsv:181, 183, 196, 215`.

**AG-026** — $c_4,c_6$ at the two supersingular points; the octahedral theorem in characteristic 5 (archive cotes 63-64). [read]
"... the characteristic-5 case of the octahedral theorem (64:50-53), his questions of 63:67 (when alpha = 0, and when alpha is
algebraic), and c_4, c_6 at the two supersingular points (63:99). The cote 63-64 corrections are carried as results R9-R12."
Locator: `PRO\ORDER.md:30`. Context: the SA16/SA18 night prompt on Grothendieck's elliptic-curve cotes.

**AG-027** — elliptic schemes with prescribed j; a cubic with 432 and 1728. [scan]
"Because J and J-1728 are units ... the standard short Weierstrass equation y^2=x^3 - (3J/(J-1728))x - 2J/(J-1728) defines an elliptic
scheme E(J) ... Its j-invariant is J, as follows directly from 1728*4a^3/(4a^3+27b^2)"; "An elliptic curve over k with j=u is ordinary,
since supersingular j-invariants are alg[ebraic]". B2 lifting: "$z^3-432tz-1728(t^3+1)$, whose roots are".
Locators: `RR\POLISH_CRISTAUX_checkpoint_18_20261123T1744Z_unzipped\audit\paper1\paper4_blind_attempt.md:47-57`;
`...\audit\continuation_cp13\B2_lifting\paper2_B2_insertion.tex:46`.

**AG-028** — the supersingular curve $y^2+y=x^3$ over $\mathbf F_2$ (j = 0) and its monodromy. [scan + HEX read]
"In the supersingular model $y^2+y=x^3$, the invariant derivation has $\partial x=1$, $\partial y=x^2$ and $\partial^2=0$";
"$E_{\rm s}:\ y^2+y=x^3,\qquad \omega=dx$" (`RR\POLISH_CRISTAUX_checkpoint_18...\audit\paper11\main.tex:154, 181, 328`).
HEX S15c: "the monodromy group in degree one is GL_8(F_2) on the supersingular product E x E for all odd degrees ... characteristic
polynomial T(T^8+T^7+T^5+T+1)"; S15l: "Full mod-2 monodromy groups GL_8(F_2) and GL_80(F_2) for hyperplane and cubic sections of the
supersingular cubic square" (`HEX:77, 107`). GHOSTS exact test: "$K=\Q(\omega)$, $\omega^2+\omega+1=0$, $E:y^2+y=x^3$, $A=E^4$"
(`RR\GHOSTS_final_20261121T0256Z_unzipped\GHOSTS.tex:56`).

**AG-029** — Galois orbits of CM points in $\mathcal A_g$; level-3 structure with a cube root of unity. [read]
"Every CM point $x\in\Ag(\Qb)$ satisfies" $|\mathrm{Gal}\cdot x|\ge c_gD_x^{1/(4g)}$; "Every CM point of $\mathcal A_2$ defined over $\Q$ has
$D_x<10^{80}$"; "Adjoin to the principally polarized variety $A_x$ a basis of its $3$-torsion, and a primitive cube root of unity. A
polarization-preserving automorphism fixing the $3$-torsion is the identity"; "For $g=1$ the truth is $D^{1/2+o(1)}$"; averaged
Colmez: "$2^{-r}\sum_\Phi h_W(A_\Phi)=-\frac12L'(0)/L(0)-\frac14\log(D_E/D_F)$".
Locators: `R23\h15_note\h15_note.tex:85, 119, 292, 371-372, 399`; prompt 66 (`PRO\_superseded_66_EFFECTIVE_CM_inside_sent_75\PROMPT.md:20-26`).

**AG-030** — Hecke orbits of CM points and bounded division (the Hodge line). [read prompt]
"Hodge holds on a special family exactly when the Hodge classes along the Hecke orbit of one CM point have algebraic ..."; "bounded
division on the Hecke orbit of E^8 (E = ℂ/ℤ[ω])". Locator: `PRO\SENT\38_HODGE_HECKE_DIVISION_bounded_division_on_Hecke_orbits\PROMPT.md:43, 81`.
Prompt 46 (v1): "Algebraicity on every fibre ⟺ c_t is bounded on a Zariski-dense set ⟺ on one Hecke orbit ⟺ on the CM points"
(`PRO\SENT\_superseded_46_HODGE_DIVISION_v1_20261121\PROMPT.md:24`). HEX H25: "bounded cycle degrees on reductions of CM points".

**AG-031** — theta constants and the second-order theta coordinates (theta eightfolds). [scan]
"the second-order theta coordinates form a matrix $(X_{uv})_{u,v\in G}$. The involution transposes this matrix, so its minus eigenspace
identifies with $\bigwedge^2V$"; "$\mathcal D_n=\{\tau=\begin{pmatrix}X&Y\\-Y&X\end{pmatrix}\in\mathfrak H_{2n}: X^{\mathsf t}=X,\ Y^{\mathsf t}=-Y\}$.
On a nonempty open subset, the only vanishing even theta constants are"; "the odd elliptic theta function has a simple zero at the
origin and each even elliptic theta constant is nonzero".
Locators: `RR\HODGE_BOUNDED_CYCLES_final_20261123T0508Z_unzipped\HODGE_BOUNDED_CYCLES\workbench\work\UNFILED\v1\paper\theta-eightfolds.tex:15, 107-171`;
`...\workbench\work\UNFILED\v1\STATEMENTS.tsv:47`. (The rank-24 theorem on these quadrics: AG-063.)

**AG-032** — theta characteristics (char 2 monodromy; the Poonen–Rains torsor; the fleet's gadget). [read]
HEX S15b: "Cote 4's question 8.6 for plane curves in characteristic 2: the monodromy on the theta characteristics is reducible for every
odd degree d >= 5 ... with the exact groups in every degree" (`HEX:59`). Fleet map AG-05: "for g = 2 there are 10 even and 6 odd";
"Symmetry: Sp_4(F_2) (≅ S_6) acts on the 16 characteristics preserving parity, the O^+(4,2) symmetry of the gadget"
(`FM\algebraic_geometry.md:47`). Poonen–Rains "Self cup products and the theta characteristic torsor" used in POLISH_ALGEBRAIC_GEOMETRY
Paper 2 (`RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\papers\paper_02\main.tex:437`). Also "There is just one geometric theta
characteristic because" (`RR\AN_GRH_final_20261121T0821Z_unzipped\final\recovered\ANABELIAN_A1_cp03_text\ANABELIAN_A1\ANABELIAN_A1_paper.tex:3849`).

**AG-033** — Weil representation, metaplectic cover, oscillator representation (032 and the theta runs). [scan]
OpenAI 032: "circle extension is obtained from the metaplectic double cover"; "For a product input the completed theta series multiply"
(`PAP\...txt` extraction of `032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf`, lines 1071, 1457);
van Hoften–Sempliner: "automorphic Weil representation ωψ of the metaplectic group" (`PAP\hodge_sources_20261121\Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf`, text l.706);
THETA3: "a nonzero quotient of the local oscillator representation" (`RR\THETA3_checkpoint_07...\THETA3.tex:10662`); DEG_L: "under the
direct-sum identification of Weil representations" (`RR\DEG_L_checkpoint_06_20261121T0517Z_unzipped\DEG_L\DEG_L.tex:430`); DP_MULT:
"Polishchuk, Analogue of Weil representation for abelian schemes, §1" (`RR\DP_MULT_checkpoint_06_20261121T0420Z_unzipped\DP_MULT.tex:5386`).
SIGN_NEXT: "whole oscillator representation by its multiaffine part" (`RR\SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped\SIGN_NEXT.tex:1377`).

**AG-034** — $y^2=x^3-x$ everywhere in the Hodge/sign runs (Frobenius, Z[i], supersingular at p ≡ 3 mod 4). [scan]
TRACE_DET: "For $E/\F_3:y^2=x^3-x$, the curve is smooth, $P_1(T)=1+3T^2$, and $U$ has eigenvalues $i,-i$. No nonzero scalar multiple of
its Frobenius can be positive." (`RR\TRACE_DET_final_20261121T0218Z_unzipped\TRACE_DET.tex:3864`); C44_POS: "Taking $E:y^2=x^3-x$ and
$p\equiv3\pmod4$ gives the same supersingular"; "class $R(i)$ on $E^2$, where $E:y^2=x^3-x$ and $i^2=-1$"; "$E_0:y^2=x^3-x$, with
$\mathcal O=\mathbf Z[i]$" (`RR\C44_POS_final_20261122T1020Z_unzipped\C44_POS.tex:6398, 10132, 10237`); SIGN_NEXT: "E:y^2=x^3-x over
Q(i)" (`...\SIGN_NEXT.tex:2050`); ZETA_NEXT NX-L01: "Glue two affine planes over Z along the complement of the vertical affine curve
y^2=x^3-x over F5" (`RR\ZETA_NEXT_final_20261121T0340Z_unzipped\IMPLICATIONS.md:57`); POLISH_AG SA05: "Let $E/\F_5$ have equation
$y^2=x^3-x$ ... its discriminant $64$ ... eight rational points, so geometric Frobenius has polynomial $T^2+2T+5$"
(`RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\records\papers_5_6\STATEMENT_EXTRACTS.md:20913`); SA07 F: "$U_0=E_0\setminus\{O\}$,
where $E_0:y^2=x^3-x$" (`RR\ZETA_TWO_final...\FLAG_AUDIT.tsv:191`).

**AG-035** — CM elliptic curve $y^2=x^3-x$ minus its origin and the Longue Marche common kernel. [read, HEX]
S07c: "for E0: y^2 = x^3 - x minus its origin, no nontrivial closed procyclic subgroup of the common kernel of all pro-l quotients has an
arithmetic normalizer with open image in G_Q(i)". Locator: `HEX:60`.

**AG-036** — real elliptic curves: rectangular and rhombic uniformizations; modular j under reciprocity. [scan]
"The rectangular and rhombic positive-parameter uniformizations classify pointed real elliptic curves and their two real forms, with
modular j invariant under recipr[ocity]" (RESEARCH_SA22). Locator: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13...\notes\paper04_register_summaries.tsv:87, 221`.
Evening digest: "Printed 97–98 classify the real structures on elliptic curves; the hexagonal case is C/Z[ω]"
(`R22\MATHEMATICS_OF_THE_EVENING_20261122.md:123`).

**AG-037** — modular curves in the papers of the recent_results folder. [scan]
"They also cover the smooth projective modular curves X0 (N ) and X1 (N )"; "= C(Q) for each of these projective modular curves"
(`PAP\019_The-p-adic-section-conjecture-October-6-2026.pdf`, text l.249, 1322); "Gonality of modular curves in characteristic $p$"
(`RR\AN_GRH_final...\final\recovered\ANABELIAN_SUCCESSOR_final_text\ANABELIAN_SUCCESSOR_paper.tex:760`); "$\mathrm{PSL}_2(\F_l)$, then solvable
covers of $X_0(l)$" (`...\ANABELIAN_A1_paper.tex:5206`).

**AG-038** — sextic CM periods and genus-three theta constants (algorithms). [scan]
"\section{Explicit primitive CM periods for the sextic construction}"; "The periods and all genus-three theta constants at \(\tau\)";
"\(\mathbb Z[\omega]\), where \(\omega=(1+s)/2\)"; "cubic character of conductor \(9\)"; "\section{Extracting a ninth root from sextic CM
Frobenius}". Locator: `RR\GRH_ALGORITHMS_FINISH_checkpoint_04_20261123T1744Z_unzipped\workbench\work\unfiled\v1\papers\grh_algorithms.tex:1857-1925, 2683`.
Context: HEX H29 (the CM-theta proof P126).

**AG-039** — THETA3's j-formula and the Gaussian test curve. [scan]
"Substitution in $j=1728\cdot4A_r^3/(4A_r^3+27B_r^2)$ and reduction"; "Take $E:y^2=x^3-x$, $\omega=dx/(2y)$, and $t=-x/y$"; "A second
instance over $\Q(\sqrt{-3})$"; "A theta operator on Picard modular forms modulo".
Locator: `RR\THETA3_checkpoint_07_20261121T0604Z_unzipped\THETA3.tex:12455, 15884, 17262, 8725`.

**AG-040** — the modular symbol map, the Eisenstein ideal, Ihara's question. [scan]
h06b: "the modular symbol map to the cyclotomic class module"; "analogue of Sharifi's theorem for once-punctured elliptic curves with
complex multiplication" (`R23\h06b_note\h06b_note_wb0006.tex:123, 1059`); gate: Sharifi 2011 "cup products of cyclotomic p-units vs. the
Eisenstein ideal"; "Ihara's relation in gr^{12} for p = 691" (`R23\h06b_note\GATE_H06b_ad855737_20261123.md:32, 36`). Literature in the
folder: Fukaya–Kato on modular curves $X_1(N)$ and the Eisenstein ideal (`R23\h06b_note\gate_fable_papers\fk.txt`, 22 "modular curve",
30 "modular form" lines).

**AG-041** — Hecke characters and modular forms in the zeta runs. [read prompt]
"since by Shimura-Taniyama the L-functions of CM abelian varieties are Hecke L-functions of algebraic Hecke ..."; "motives of positive
weight without CM, starting with elliptic curves without CM and modular forms"; "Faltings heights of CM elliptic curves, and Colmez's
formula for CM by Q(ζ_5)". Locator: `PRO\SENT\35_ZETA_TWO_RH_for_schemes_and_motives_from_the_two_proofs\PROMPT.md:45, 58-61`.

**AG-042** — Eisenstein series in Masullo's text (TRACE_DET work copy). [scan]
"arise of meromorphic vector-valued Eisenstein series. We will return to Sarnak's paper"; "relating them to certain functional families of
Eisenstein series"; "Uniformization Theorem. Let Γ ⊂ PSL2 (R) be a discrete subgroup".
Locator: `RR\TRACE_DET_final_20261121T0218Z_unzipped\work\masullo_full.txt:7596, 18643, 18670-18681`.

**AG-126** (added last; belongs to this section) — Eisenstein series and congruences in the K-tower. [scan]
"Put $k=b+1$ and take the normalized Jacobi Eisenstein series"; "level-one Siegel Eisenstein series with constant coefficient $1$, and set"; "coefficients are those of
the normalized Eisenstein series attached to"; cited: "Hilbert class polynomials and traces of singular moduli"; "Siegel modular forms of genus~2 modulo $p$"; gate:
"Fretwell--Roberts, *Newform Eisenstein congruences of local origin*, Ramanujan Journal 64 (2024), Theorem 3.6"; "the exact generalized Bernoulli values".
Locators: `RR\KTOWER_checkpoint_11_20261122T0001Z_unzipped\KTOWER.tex:2179, 8622, 8807, 9058, 9148, 9208`; `...\evidence\main_gate\REPORT.md:68`.
Context: the congruence (Eisenstein-ideal) side of the K-groups-of-Z computation.

## 2. Lattices and codes

**AG-043** — the Leech space and the Golay coordinates (prompt 78). [read prompt]
"... the character is U+8T, where U is the inflated regular character of the cyclic cubic quotient of A4 and T is the three-dimensional
tetrahedral character. The independent Golay-coordinate action on the 24-dimensional Leech space is 2U+6T. Its integral trace map is onto
Z³, but its invariant vectors have traces exactly 4Z³. Read the Jordan endpoint p[roof], the Leech invariant-lift ..."
Locator: `PRO\78_SIGNED_COUNTS_AND_WINDING\PROMPT.md:17`. Context: Paper I "Three winding signs and a quadratic Hecke character over a
cyclic cubic field" (l.24).

**AG-044** — the K3 lattice $U^{\oplus3}\oplus E_8(-1)^{\oplus2}$ and $T_P=U\oplus U(2)\oplus D_4(-1)$. [scan]
"Lemma 1.3. There is a primitive embedding of P in ΛK3 = U⊕3 ⊕ E8 (−1)⊕2 with orthogonal complement TP = U ⊕ U(2) ⊕ D4 (−1)"; "An
anti-isometry glues P ⊕ TP to an even unimodular lattice of signature (3, 19)"; "a triality automorphism exchanging the vect[or ...]" (type D4).
Locator: `PAP\032_Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026.pdf`, text l.215-222, 816.

**AG-045** — $T_0=U\oplus U(3)\oplus E_8(-1)^{\oplus2}$ (K3 existence, Q23). [scan]
"T_0=U\oplus U(3)\oplus E_8(-1)^{\oplus2}"; "T0 = U + U(3) + E8(-1)^2. Its associated K-Hermitian space W0 has rank ten". Q23: "resolved by
refuting the stated formal half-twist transfer and proving the refined conditional criteria and K3 existence"; UNFILED.080 (refuted):
"The order-three rank12 K3 half-twist supplies the particular canonical Clifford block needed by the Mumford argument."
Locators: `RR\HODGE_FINISH_final_20261123T1713Z_unzipped\workbench\checks\q23_final_fresh\INITIAL_PROOF.md:225`;
`...\workbench\checks\q23\q23_existence_addendum.md:32`; `...\workbench\work\UNFILED-B\v1\paper\main.tex:4680`; `...\README.md`;
`...\workbench\STATEMENTS.tsv:103`.

**AG-046** — the $E_8$ cover family; $W(E_8)\cup iW(E_8)$ (Q24). [scan]
"Starting from the E8 Cartan matrix, the simple reflections produce exactly 240 roots. Their permutation group has order `696729600`.
Adjoining the scalar `i` on the 480 vectors `R union iR` gives order `1393459200`"; "The source group is G=W(E8) union iW(E8), of order twice
696729600"; "The E8 lattice is unimodular, H0 is integral, and v is integral"; "algebraicity using an $E_8$ cover family"; "Every primitive
sixfold in the specified $E_8$ source component"; "unrefereed $E_8$ construction \cite{SevernGaussian} gives a nonsplit" Gaussian sixfold.
Locators: `RR\HODGE_FINISH_final...\workbench\checks\q24\Q24_INDEPENDENT_REPORT.md:91`; `...\checks\q24_final_fresh\INITIAL_PROOF.md:75, 114`;
`...\checks\fresh_final_packets\q24_statement.tex:8, 60`; `...\workbench\work\UNFILED-A\v1\paper\main.tex:225, 2429`.

**AG-047** — theta quadrics of rank 24 via $E_8$ (Paper B). [read statement]
"\label{thm:theta-rank} The combinations of \eqref{eq:theta-forced} that descend to the minus eigenspace form a vector space of dimension
$35$. Every nonzero form in this space has rank at least $24$, and rank $24$ occurs. In particular this space contains no rank-$10$ quadric."
Independent check: "sharp rank24 from an independent E8/integral-reduction proof"; "35-dimensional space,4200 E8 equations, rank24 example
and43180 affine sections"; "Let L be the E8 root lattice in R^8, and choose one root from each antipodal" pair; "plus the seven edge products
of the E8 Dynkin tree, and its Gauss sum is".
Locators: `RR\HODGE_FINISH_final...\workbench\STATEMENTS.tsv:58` (UNFILED.045, B.5.1); `...\CHECK_EVENTS.tsv:218`;
`...\workbench\checks\README.md:60`; `...\workbench\checks\b_theta_blind\initial_statement_only_analysis.md:52-69`.

**AG-048** — Gaussian and Eisenstein Hermitian lattices: $U\oplus U$, $I_{2,2}$, $U^3\cong I_{3,3}$, $U+U+\langle1,-3\rangle$. [read HEX + scan]
H25b: "every pairing-integral Z[i]-lattice of signature (3,3), class [-3], embeds isometrically in U + U + <1,-3>; hence 3 / Delta and
delta_W <= (Delta/3) B for nonsplit Gaussian sixfolds" (`HEX:63`). "For $K=\Q(i)$ the detector degree is at most $48$ on the even Hermitian
lattice $U\oplus U$, and at most $192$ on the odd lattice $I_{2,2}$. For $K=\Q(\sqrt{-3})$ it is" [36]; table "\Q(i)&U^3&746496 \\ \Q(i)&I_{3,3}&5971968
\\ \Q(\omega)&U^3\cong I_{3,3}&30375" (`RR\HODGE_BOUNDED_CYCLES_final...\workbench\work\UNFILED\v1\STATEMENTS.tsv:24, 27`;
`...\paper\sixfolds.tex:15-21`). "Every unimodular $\Z[\omega]$-Hermitian lattice of signature $(2,2)$ is" (hyperbolic)
(`RR\HODGE_FINISH_final...\workbench\checks\small_detectors_blind\independent_detector_proof.tex:189`); "Even unimodular lattices are
hyperbolic"; "An even unimodular lattice of rank six thus has determinant class" (`...\checks\gaussian_maximal_blind\INITIAL_PROOF.md:228-312`).

**AG-049** — Gaussian $E_8$ source of rank nine; $\mu_4W(E_8)$; Fermat-twelve hypersurfaces. [scan]
"independent calculations establish a dominant connected $\mu_4W(E_8)$"; "reduction D-GAUSS-01--03 now leaves only the scalar $E_8$
extension"; "Fermat-twelve hypersurfaces"; "## Gaussian E8 and the branch-exponent supplier ... The exact Hodge intersection is3009825/64";
"Gaussian determinant class3 now has connected dominant E8 source, rank9, and algebraic supplier".
Locators: `RR\HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped\HODGE_DIVISION.tex:46, 370-378`; `...\IMPLICATIONS.md:48-52`;
`...\LEDGER.md:89`.

**AG-050** — $E_8^0$ singularities on the exceptional K3 cover. [scan]
"In the non-almost-ruled alternative of Proposition~\ref{prop:normalized-mup-ekedahl}, every singularity of $N$ has type
$A_1,\ D_{2m}^{0}\ (m\geq2),\ E_7^{0},\ E_8^{0}$"; "$E_8^{0}&x^3+y^5&8$"; "The exceptional normalized cover has only A1, D_even^0, E7^0 and
E8^0 singularities, whose Dynkin indices sum to 12+Y². [After Matsumoto]".
Locators: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\papers\paper_02\k3_picard_constraints.tex:187-220`; `...\REGISTER.tsv:23`.

**AG-051** — K3 lattice and period theorem in the Mumford surfaces. [scan]
"\cite[Theorem~1.12.4, pp.~122--123]{Nikulin}. Extend the Hodge decomposition by declaring its orthogonal complement to have type $(1,1)$.
The K3 period theorem". Locator: `RR\HODGE_BOUNDED_CYCLES_final...\workbench\work\UNFILED\v1\paper\mumford-surfaces.tex:93`.

**AG-052** — the theta series of the Eisenstein lattice $A_2$. (See AG-017: $a=\sum_{\alpha\in\mathbf Z[\omega]}q^{N\alpha}$.) Locator:
`RR\KTOWER_checkpoint_11...\KTOWER.tex:692`. Also "Patterson's theta series" (cubic) in prompt 69 (`PRO\69_BEYOND_DIRICHLET\PROMPT.md:81`).

**AG-053** — the Eisenstein lattice modulo 269: 270 directions. [scan]
"in the Eisenstein lattice. Modulo 269 there are 270 projective directions. Ninety give weight \(+2\), and 180 give \(-1\). Multiplication by an
element of norm o[ne]"; "I used the unit-invariant cubic character on the 270 Eisenstein projective directions and its exact mean zero on
each norm fibre". Locators: `R22\extended_grand_rh\research\WORKSHOP.md:21`; `...\MATHEMATICS_LOGBOOK.md:21`.

## 3. Groups

**AG-054** — $\mathrm{PSL}_2(\mathbf Z/12)$, the level-12 frames, and $E_{12}=V_4\times\mathrm{SL}_2(\mathbf F_3)$. [read]
Lemma 12: "(a) Under $\Z/12=\Z/4\times\Z/3$, $E_{12}=V_4\times\SL_2(\F_3)$ ... $E_{12}$ does not contain $-I$ ... (b) The elements of $E_{12}$
whose class commutes with that of $R_+$ form $\{I\}\times(\langle-I\rangle\times\langle R_0\rangle)$. (c) Those whose class commutes with that of
$S_0$ form $\{I,U^2L^2\}\times\langle S_0\rangle$." Lemma 13: "There is a unique $t_F\in\Z/12$ with $\tilde q\circ\Phi_F=\Ad(U^{t_F})\circ\tilde q$
... $t_F\equiv0\bmod4$, and $t_F\equiv-\rho_2(F)\bmod3$." Definition: "$q_{12}(A_F)\bmod3\in(-I)^{a_3(F)}\langle R_0\rangle$,
$q_{12}(\beta_F)\bmod3\in S_0^{a_2(F)}\langle-I\rangle$, and $\delta=a_2+a_3$."
Locator: `R23\h17_note\h17_note_wb0007.tex:536-598`.

**AG-055** — orders and ranks at level 12: 1152, 576, 97, 96, 1728, 6912. [read/scan]
"$Q_{12}=\SL_2(\Z/12)/\{\pm I\}$, of order 576" (`LM\DELTA_ON_GT_checkpoint_05...\DELTA_ON_GT\sections\conventions.tex:34`); "Let B=C2 amalgam
C3, let q:B→Q=SL2(Z/12)/{±I} be the fixed quotient of order576, and let N=ker(q). Because q is injective on both finite factors, the
Bass–Serre quotient graph gives N free profinite of rank97" (`...\DELTA_ON_GT\agent_five\canonical_homology_audit.md:6`); [mine]
97 = 1 + 576(1 − 1/2 − 1/3). "The signed image of F̂ in SL₂(Z/12) has order 96 and its second derived group is {I, 5I}"
(`R20\delta_sextic\DELTA_SEXTIC_20261121.md:80-81`); "Thus $|J|=32\cdot54=1728$"; "orders \(576,96,32,54,1728\), all \(9216\) products"
(`LM\SECTION_GHOSTS_final...\SECTION_GHOSTS\sections\part_E_relative_cm_identity.tex:142, 288`); A.9: "The order-6912 candidate does not
determine $\Delta$" (`...\DELTA_ON_GT\sections\A.tex:241`).

**AG-056** — the centre of $\mathrm{SL}_2(\mathbf Z/N)$ and the units {1, 5, 7, 11}. [read]
A.6: "There is a continuous homomorphism on $\HH$: $u(h)\equiv(-1)^{a_3(h)}\pmod3$, $u(h)\equiv(-1)^{a_2(h)}\pmod4$. It takes values in
$\{1,5,7,11\}\subset(\Z/12)^\times$ and has image modulo the global sign equal to $\delta$" (table $(a_3,a_2,u,e,\delta)$: (0,0,1,0,0),
(0,1,7,9,1), (1,0,5,4,1), (1,1,11,1,0)). A.7 (Refuted): "The assertion that $\Ob(N)=Z(\SL_2(\Z/N))/\{\pm I\}$ is trivial at every prime
power is false. In particular $\Ob(8)\simeq C_2$. ... Its rank over $\Ftwo$ is $r+c(a)$, where $c(0)=c(1)=0$, $c(2)=1$, and $c(a)=2$ for
$a\ge3$." Locator: `LM\DELTA_ON_GT_checkpoint_05...\DELTA_ON_GT\sections\A.tex:148-205`. Moonshine-dictionary hunch: "For F in GT_0-hat of
multiplier one the image of the pair of frames of s and r in PSL_2(Z/12) lies in the image of the centre {1, 5, 7, 11} of SL_2(Z/12), and
Delta(F) is its class modulo +-1" (`<local>/Documents\pro_intake_20261114\PUSH_ITEMS_ORDER5_FRAME_before_ghost_lambency_20261114.md:128-130`).

**AG-057** — $A_4=\mathrm{PSL}_2(\mathbf F_3)$ as the quotient of $B$ with $\tau^3=1$; the binary tetrahedral group. [read]
"The quotient of G₆ by 2Λ̂ ⋊ {±1} is the unique quotient A₄ = PSL₂(F₃) of B with τ³ = 1" (`R20\delta_sextic\DELTA_SEXTIC_20261121.md:71-72`);
"In $\PSL_2(\F_3)=A_4$ the element $U^{-t}q(\beta)$ centralizes the involution $q(s)$, so it lies in the four-group, the image of the quaternion
group $Q_8\subset\SL_2(\F_3)$" (`R23\h17_note\h17_note_wb0007.tex:577-579`); "$q_3:B\to\operatorname{PSL}_2(\mathbb F_3)=A_4$"
(`LM\EXIT_TOWER_checkpoint_28...\extracted_20261116\sections\E_cm_parity_vanishing.tex:452`); DELTA23 "binary_tetrahedral_half_character":
"$SL_2(3)\twoheadrightarrow PSL_2(3)=A_4$" (`RR\DELTA23_checkpoint_06_20261121T0329Z_unzipped\agents\characters\proofs\binary_tetrahedral_half_character.tex:39`).

**AG-058** — $\mathrm{SL}_2(\mathbf Z)$ as the normalizer of the 3-torsion grid; $\Gamma_{1,1}$ and $\Gamma_{1,2}$ as braid quotients. [read]
"The normalizer of $H$ in $\Gamma$ is $H\rtimes\SL_2(\Z)$, the affine maps; its subgroup $\mathcal N_0=\SL_2(\Z)$ fixing the origin is mapped
isomorphically to $\Gamma_{1,1}$"; "On $\Gh_{1,1}=\Bh_3/\overline{\langle(uv)^6\rangle}$"; "On $\Gh_{1,2}=\Bh_4/\overline{\langle\Omega\rangle}$";
"the image of $uv$ in $\Gh_{1,1}$ has order six"; "$\Out(\Gh_{0,8})=\GT\times\mathfrak S_8$" (Hoshi–Minamide–Mochizuki).
Locator: `R23\h17_note\h17_note_wb0007.tex:680-702, 738-740, 782-786`. Runs: SECTION_GHOSTS E.184 "its completed normalizer is the full completion
of H semidirect SL2(Z)" (`LM\SECTION_GHOSTS_final...\SECTION_GHOSTS\notes\gt_translation_fusion_results.csv:2`).

**AG-059** — $\mathrm{PSL}_2(\mathbf F_5)$ on $X(5)$, the Klein quartic $\mathrm{PSL}_2(\mathbf F_7)$, levels 7 and 11. [scan]
"Smallest instance: X(5), the sphere punctured at the 12 vertices, with deck group `PSL_2(F_5)`"; "`N = 7` is the Klein quartic (Boggi, Theorem
A, ramified case)"; "in the stable tower the first is `PSL₂(F₇)` at the Klein quartic"; "(S5) Levels 7 and 11. The map `𝔗_T` of (R4) has
siblings at `p = 7` and `p = 11` (the index-`p` subgroups of `PSL₂(F_p)`)".
Locator: `<local>/Documents\pro_intake_20261114\PUSH_ITEMS_20261114_before_ghost_lambency_20261114.md:235, 287, 303, 313`.
SECTION_GHOSTS: "Their finite nonabelian composition factors remain PSL2(F_q) with q prime. The actual A7 quotient ..."
(`LM\SECTION_GHOSTS_final...\SECTION_GHOSTS\notes\symmetry_audit.md:104`); candidate orders `[60,168]`
(`...\code\check_symmetry_audit.py:104`).

**AG-060** — $\mathrm{PSL}_2(\mathbf F_q)$ bounded ramification, q = 4, 8, 16. [scan]
"parts/D/code/check_psl2_bounded_ramification_v2.py 31,222 exact assertions for q=4,8,16: fields, PSL2 generation, branch orbits, inerti[a]"
(RESEARCH_SA12). Locator: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\records\paper_1\REPORT_QUESTIONS.tsv:79`.

**AG-061** — $\mathrm{Sp}_4(\mathbf F_2)\cong S_6$ on theta characteristics. (Fleet map, `FM\algebraic_geometry.md:47`; quoted in AG-032.)

**AG-062** — Weyl groups $W(E_6),W(E_7),W(E_8)$; triality in rank four; the finite $K$-normalizer. [scan]
"This covers in particular triality in rank four"; "The remaining possibilities are $W(A_r)$ and $W(E_6),W(E_7),W(E_8)$"; "$E_7,E_8$ have no
diagram automorphism. Hence the finite $K$-normalizer"; "For $E_6,E_7,E_8$ we may assume genus zero"; "They lie in $371$ named tables and
nineteen" ($\Q(\sqrt{-3})$ rows). Locators: `RR\HODGE_BOUNDED_CYCLES_final...\workbench\work\UNFILED\v1\paper\finite-cover-eightfolds.tex:102-143, 677`;
same in Paper B: `RR\HODGE_FINISH_final...\workbench\work\UNFILED-B\v1\paper\main.tex:427-447`.

**AG-063** — sporadic groups in the Paper B character catalogue: $M_{24}$, $2^{11}{:}M_{24}$, $Co_1$, $2.Co_1$. [scan]
Catalogue: "Rational scan |2678 loaded tables;12479 selected character rows in1365 named tables; minimum scalar-budget margin28; no
survivor." Rows include "M24 3 45 -7 20 20 4 false", "M24 5 231 -15 111 111 4 false", "M24 7 252 112 112 192 168 false", "M24 9 483 224 224
363 322 false", "2^11:M24 60 276 120 120 204 184 false", "Co1 2 276 128 128 204 184 false", "Co1 3 299 128 128 221 199 false",
"NDG(2.Co1,5^2) 107 72 24 24 6 false", "NRS(M24,2^(2+2+4)a) 37 36 12 12 24 24 false".
Locators: `RR\HODGE_FINISH_final...\workbench\checks\catalogue\README.md:26`;
`...\catalogue\certificates\finite_quadratic_character_scan.tsv:824-827`; `...\finite_rational_scalar_scan.tsv:423-424, 985-990, 3949-3951, 7899-7900`;
`...\finite_gaussian_character_scan.tsv:26-29`; same rows in `RR\HODGE_BOUNDED_CYCLES_final...\workbench\work\UNFILED\v1\checks\certificates\`.
Context: the finite-cover proofs of Paper B (Mumford's exceptional classes); "No script output by itself is called a classification of all
finite groups."

**AG-064** — exceptional groups of Lie type and twisted triality. [scan]
"the symplectic row. The twisted triality groups ${}^3D_4(q)$"; "E_6(q),\ q\geq2&78&q&2"; "E_8(q),\ q\geq2&248&q&1".
Locator: `RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\records\paper_1\EXACT_STATEMENTS.md:10243-10396`.

**AG-065** — Coxeter numbers and $E_8$: normalizers of Coxeter cyclic subgroups; triality-$S_3$ counts in $D_4$. [scan]
RESEARCH_SA20 D.002: "The normalizer of a Coxeter cyclic subgroup surjects onto the units modulo the Coxeter number with cyclic kernel, and
this extension splits in types A, B, C, D, G2, and E7 but not F4, E6, or E8." D.026: "including the precise trivial, order-two, and
triality-S3 counts in D4 an[d ...]". Locator: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13...\notes\paper02_register_summaries.tsv:226, 250`.

**AG-066** — $E_8$ nilpotent classes in the archive's algebra (cote 123). [scan]
"Richardson computation, completed at $E_8(a_2)$ by later published"; "$E_8(a_1)$ has rank $7$, the omitted $E_6\subset E_8$ class has rank $3$,
the final regular $E_8$ exponent is $29$ rather than the printed $27$, and $E_8(a_2)$ has"; table row "$E_8$ & No & BR-123-OPPE8".
Locator: `RR\ARCH_ALG_final_20261122T0622Z_unzipped\research\cote123\companion.tex:123, 176, 367-392`.

**AG-067** — $G_2$ triality and $\mathrm{Sp}_4(3)$ Weil constituents (Hodge division). [scan]
"\input{agents/imprimitive/lie_small_fields/g2_triality_section.tex}"; "D-SPW-01--03 removes all higher odd-characteristic symplectic Weil
constituents and tensor powers, leaving only the explicit degree4/5 Sp4(3) endpoint".
Locator: `RR\HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped\HODGE_DIVISION.tex:143`; `...\IMPLICATIONS.md:144`.

**AG-068** — the affine-plane triality and $|AGL_2(3)|=432$. [scan]
"has order 432 = |AGL₂(3)|). It corrects my sweep-3 hunch ... Cameron 2015 §6, pp. 8–9 has the affine-plane triality".
Locator: `RR\ZETA_TWO_final_20261121T0032Z_unzipped\INTAKE_INVENTORY.tsv:523`.

## 4. Moonshine proper

**AG-069** — the twenty-three lambencies of Cheng–Duncan–Harvey computed as covers $X_0(N)\to X(1)$ (EXIT_TOWER D.14). [read]
"For each lambency in Cheng--Duncan--Harvey's Table~2, the following tables give the complete permutation cover $X_0(N)\to X(1)$, its cusps,
the action of the subgroup $S$ of exact divisors, and the signature of $\Gamma_0(N)+S$. The signature convention is $(0;e_2,e_3;c)$"; "the base
has generic inertia $\mu_2$ and elliptic inertia orders $4$ and $6$"; Riemann–Hurwitz "$g_0=1+\mu/12-e_2/4-e_3/3-c/2$"; cusp width
"$w_d=N/\gcd(d^2,N)$"; "$\frac{\mu}{6|S|}=-2+c+e_2/2$". Table rows ($\ell$, $\mu$, $g_0$, $\sigma_2$, $\sigma_3$, cusp widths, $(e_2,e_3;c)$):
2: 3, 0, $1\,2$, $3$, $1\,2$, (1,0;2) · 3: 4, 0, $2^2$, $1\,3$, $1\,3$, (0,1;2) · 4: 6, 0, $2^3$, $3^2$, $1^2\,4$, (0,0;3) · 5: 6, 0, $1^2 2^2$,
$3^2$, $1\,5$, (2,0;2) · 6: 12, 0, $2^6$, $3^4$, $1\,2\,3\,6$, (0,0;4) · 7: 8, 0, $2^4$, $1^2 3^2$, $1\,7$, (0,2;2) · 8: 12 · 9: 12 · 10: 18, (2,0;4) ·
12: 24, (0,0;6) · 13: 14, (2,2;2) · 16: 24 · 18: 36, (0,0;8) · 25: 30, (2,0;6) · 6+3: (2,0;2) · 10+5: (3,0;2) · 14+7: 24, $g_0=1$, (4,0;2) ·
18+9: (2,0;4) · 22+11: 36, $g_0=2$, (6,0;2) · 30+15: 72, $g_0=3$, (8,0;4) · 46+23: 72, $g_0=5$, (12,0;2) · 12+4: (0,0;4) · 30+6,10,15: 72,
$g_0=3$, (6,0;2).
Locators: `LM\EXIT_TOWER_checkpoint_28_20261116T1443Z_unzipped\extracted_20261116\sections\D_lambencies.tex:1-45`;
`...\extracted_20261116\code\d_lambencies_table.tex:1-27`. Intake: "D.14 | Proved | All passports, cusp fields, Atkin--Lehner actions, and
signatures ... a side line outside the tower" (`<local>/Documents\pro_intake_20261119\GENERAL_INTAKE_EXIT_TOWER_cp28_20261119.md:207`).
Context: Longue Marche run on the exit tower; the umbral covers are carried as a side computation.

**AG-070** — the umbral Hauptmoduln $T^X=1/\eta_{\pi^X}$, $q^{-1}-d^X+O(q)$ (EXIT_TOWER D.15). [read]
"For all twenty-three rows the exact modular function $T^X=1/\eta_{\pi^X}$ is $S$-invariant and descends to a $\mathbb Q$-coordinate on $X_0(N)/S$,
with a unique simple pole and expansion $q^{-1}-d^X+O(q)$"; Newman/Ligozat: "$\sum r_\delta=0$, $\sum\delta r_\delta\equiv\sum(N/\delta)r_\delta\equiv0\pmod{24}$,
$\prod\delta^{r_\delta}\in(\mathbb Q^\times)^2$"; "$\operatorname{ord}_{c_{d,a}}T^X=\frac N{24}\sum_{\delta\mid N}\frac{\gcd(d,\delta)^2r_\delta}{\gcd(d,N/d)d\delta}$";
"its next coefficient is $k_1=-d^X$, as checked against every root system of the opened CDH Table~2 ... This independently verifies the content
of CDH Proposition~2.1"; "For every nontrivial $e$, the function $j\circ W_e$ has pole order $e$ at infinity, while $j$ has pole order one. Hence $j$
does not factor through $X_0(N)/\langle W_e\rangle$." Tripod comparison: "$D\Gamma_0(4N)D^{-1}=\Gamma(2)\cap\Gamma_0(N)$ ($N$ odd),
$D\Gamma_0(2N)D^{-1}=\Gamma(2)\cap\Gamma_0(N)$ ($N$ even)".
Certificate (constant term, $q$-coefficient): 2: −24, 276 · 3: −12, 54 · 4: −8, 20 · 5: −6, 9 · 6: −5, 6 · 7: −4, 2 · 8: −4, 4 · 9: −3, 0 ·
10: −3, 1 · 12: −3, 2 · 13: −2, −1 · 16: −2, 0 · 18: −2, 0 · 25: −1, −1 · 6+3: −6, 15 · 10+5: −4, 6 · 14+7: −3, 3 · 18+9: −3, 3 · 22+11: −2, 1 ·
30+15: −2, 1 · 46+23: −1, 0 · 12+4: −4, 6 · 30+6,10,15: −3, 3. "All 23 rows pass".
Expansions: "## 2: A_1^{24} ... q expansion q^-1 through q^8: {'-1': 1, '0': -24, '1': 276, '2': -2048, '3': 11202, '4': -49152, '5': 184024,
'6': -614400, '7': 1881471, '8': -5373952}"; "## 6: A_5^4D_4 ... {'-1': 1, '0': -5, '1': 6, '2': 4, '3': -3, '4': -12, '5': -8, '6': 12, '7': 30, '8': 20}".
Locators: `...\EXIT_TOWER_checkpoint_28...\extracted_20261116\sections\D_lambencies.tex:47-89`; `...\code\d_lambencies.out:1-29`;
`...\code\d_lambencies.md:29-63` (full per-lambency cusp data and expansions).

**AG-071** — the umbral relation $(\ell-1)(p+1)=24$ and the order-5 frame. [read]
"For the record of the hunch, neither being an argument (the dictionary, S1 and S7): in the umbral table of lattices `A_{ℓ−1}^d` the relation
`(ℓ − 1)(p + 1) = 24` has `ℓ = p` only at 5; and twelve points of equal weight is the last case of Thurston's list."
Locator: `<local>/Documents\pro_intake_20261114\PUSH_ITEMS_20261114_before_ghost_lambency_20261114.md:315`.

**AG-072** — the moonshine dictionary as an input to the Δ line (14 Nov debate). [read]
"O.9 The frame as an element of the centre (the moonshine dictionary, item M1 (a); a hunch)" (AG-056); "Cheng–Duncan–Harvey on umbral
moonshine and the Niemeier [lattices]" attached in LaTeX; a function "which equals 1 at the cusps and has its zeros and poles at the two special
points (the moonshine dictionary, ...)"; "## Added in debate round 2 (14 November 2026, 17:28 UTC): `Δ` and E.3 from the moonshine dictionary".
Locators: `<local>/Documents\pro_intake_20261114\PUSH_ITEMS_ORDER5_FRAME_before_ghost_lambency_20261114.md:128-130, 178-180, 232`;
`<local>/Documents\pro_intake_20261113\PUSH_ITEMS_LM7_CONTINUED.md:281-283`. The dictionary itself
(`<local>/Documents\research_maps_20261114\MOONSHINE_DICTIONARY\MOONSHINE_DICTIONARY_20261114.md`) was not reopened here.

**AG-073** — Conway–McKay–Trojan in the anabelian run. [scan]
"\begin{claim}{A.55}{Proved; the Conway--McKay--Trojan test is outside the category}".
Locator: `RR\AN_GRH_final_20261121T0821Z_unzipped\final\recovered\ANABELIAN_SUCCESSOR_final_text\ANABELIAN_SUCCESSOR_paper.tex:4810`.

**AG-074** — "Moonshine" in Nakamura–Schneps (Conway–Hsu quilts). [scan]
"[CH] on Moonshine, although the objects they define as quilts are not the same as". Locator:
`<local>/Documents\results_register\delta_referee_20261118\papers\NS2000\newGT.txt:250` (the H17 referee's copy of Nakamura–Schneps 2000).

**AG-075** — "moonshine repair" in the split-zero corpus (prompt 93). [read prompt]
"Corpus papers 11-16 (moonshine repair, CUE-Hurwitz phase space and its extensions, archimedean support, projective". Locator:
`PRO\93_SPLIT_ZERO_AFTER_FGJM\PROMPT.md:153`.

**AG-076** — mock modular: the Weierstrass mock modular form (AG-011). Locator:
`RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13...\notes\paper03_register_summaries.tsv:24`.

**AG-077** — Hauptmoduln in a cancellation paper's bibliography. [scan]
"[23] W. W. Stothers, Polynomial identities and Hauptmoduln, Quart. J. Math. Oxford Ser. (2)". Locator:
`PAP\047_An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026.pdf`, text l.2004.

## 5. Triangle groups, the hexagon, GT̂, Z[ω], cubic and sextic characters

**AG-078** — relation (IV) on GT̂, the group Λ, and Δ = 0 (Theorems 1-3, Corollary 4). [read]
"\[ f(u,v^4)=v^{8\rho_2}\,f(u^2,v^2)\,u^{4\rho_2}\,(uv)^{-6\rho_2},\tag{IV} \]"; Theorem 1: "Relation $(\mathrm{IV})$ holds in $\Bh_3$ for every
$F=(\lambda,f)\in\GT$"; Theorem 2: "$\GT=\Lambda_0\cdot\GQ$ with $\Lambda_0\subset\Lambda$"; Theorem 3: "$\delta(F)=0$ for every normalized
$F\in\GT$"; Corollary 4: "Let $\Delta:\GT\to\F_2$ be a homomorphism that is trivial on $\GQ$ and equal to $\delta$ on $\Lambda_0$. Then $\Delta=0$."
"the two frames at the elliptic points can disagree on the hexagon group, and the pentagon relation forces them to agree."
Locator: `R23\h17_note\h17_note_wb0007.tex:90-158`; HEX row H17 (`HEX:25`). Runs: SECTION_GHOSTS E.177-E.191, EXIT_TOWER E.49
("$\Delta|_{\widehat{\mathrm{GT}}}=0$", `LM\EXIT_TOWER_checkpoint_28...\extracted_20261116\sections\E_cm_parity_vanishing.tex:3-17`), SECTION_GHOSTS
`...\sections\part_E_gt_cm_character.tex:1-9` ("The signed CM character on the full GT group").

**AG-079** — the GT̂ relations: two-cycle, hexagon, pentagon. [read]
"(I) $f(x,y)f(y,x)=1$; (II) $f(x,y)x^{m}f(z,x)z^{m}f(y,z)y^{m}=1$, where $xyz=1$ and $m=(\lambda-1)/2$; (III) the five-cycle (pentagon) relation in
the pure mapping class group $\Gh_{0,5}$. The pairs satisfying (I) and (II) form the larger group $\GTz$ of Harbater and Schneps".
Locator: `R23\h17_note\h17_note_wb0007.tex:78-84`. Kummer cocycle: "$\sigma(2^{1/n})=\zeta_n^{\kappa_2(\sigma)}2^{1/n}$" (l.301-302).

**AG-080** — the lattice of the group $(2,3,6)$: $\mathbf Z[\omega]\rtimes\mu_6$. [read]
"Let $\omega=e^{2\pi i/3}$, $\zeta=e^{2\pi i/6}$, $\mathcal L=\Z[\omega]$ ... The assignment $u\mapsto(0,\zeta)$, $v\mapsto(1,\zeta)$ defines a surjection
$\pi_6:B\to\mathcal L\rtimes\mu_6$ whose kernel is the second derived group $B''$; it maps $B'$ onto $\mathcal L$. One computes $\pi_6(s)=(\zeta,-1)$,
$\pi_6(x)=(0,\omega)$, $\pi_6(y)=(1+\zeta,\omega)$; so $\pi_6(F)\subset(1-\omega)\mathcal L\rtimes\langle\omega\rangle$ and $\pi_6(F')\subset3\mathcal L$."
Lemma 15: "$\Phi_F$ acts on $\Bh'^{\,\ab}=\widehat{\mathcal L}$ as multiplication by a unit $\nu_F$ of $\Zh[\omega]$ with $\nu_F\equiv1\bmod3$,
$\nu_F\equiv(-1)^{a_2(F)}\bmod4$"; "As $2\widehat{\mathcal L}\rtimes\{\pm1\}$ has index $12$, it is the kernel of $\kappa$" ($\kappa$ onto $A_4$).
Locator: `R23\h17_note\h17_note_wb0007.tex:600-627`.

**AG-081** — the hexagonal self-similarity (H) and the frame bits read modulo 4 and modulo 3. [read]
"the modular orbifold is identified with the quotient of the punctured hexagonal curve by its automorphism group $\mu_6$ ... the frame of $F$ at
the point of order three becomes a six-fold symmetry of a lattice, the frame at the point of order two a translation, and the two bits are read
off the same matrix modulo $4$ and modulo $3$"; proof of Theorem 3: "As $R_+$ has order six modulo $4$ and $R_+^3=-I$, this gives
$k\equiv3a_2\bmod6$ ... So $a_2(F)=a_3(F)$." Locator: `R23\h17_note\h17_note_wb0007.tex:211-221, 841-858`.
DELTA_SEXTIC: "(H), the hexagonal relation. For F = (1, f) ∈ GT̂ there is h ∈ G₃ with Ψ∘φ = Ad(h)∘φ∘Φ_F"; "The map φ: u ↦ ab, v ↦ cb is a
homomorphism B → Γ₁,₂ with φ(s) = Δ₄ (order 2), φ(r) = abcb (order 3)" (`R20\delta_sextic\DELTA_SEXTIC_20261121.md:113-132`).

**AG-082** — sextic reciprocity over $\mathbf Q(\omega)$: Δ as a product of two Hilbert symbols. [read]
"for every multiplier-one gentle F, (−1)^Δ(F) = (√−3, c)₂ · (√−3, c)_√−3, with c = ν_F / T_F, a product of quadratic Hilbert symbols over
K = Q(ω) at its places 2 and √−3"; Proposition 1: "GT̂₀ acts on the profinite (2,3,n) triangle group ... ν_F = 1 + ω φ_f ... ν_F ≡ 1 mod 3 and
N(ν_F) = 1"; Proposition 4: "The centralizer of R₀ in M₂(Z/12) is Z[ω]/12 ... **Δ(F) = 0 ⟺ T_F ≡ ± ν_F mod 4√−3.**"; "The product formula that Δ
needs is over Q(ω), for the pair (√−3, ·), at the places 2 and √−3, against the roots of unity μ₆ = Aut(E₀)."
Locator: `R20\delta_sextic\DELTA_SEXTIC_20261121.md:9-15, 47-55, 87-94, 172-174`.

**AG-083** — the CM character of $y^2=x^3+16$ ($w^3=\lambda(\lambda-1)$); the Fermat cubic. [read]
"Proposition 2 (Galois). The translation subgroup of the image of F̂ is the Tate module of w³ = λ(λ−1), which is y² = x³ + 16. For σ ∈ G_{Q(ω)},
ν_σ is the action of σ on it: the CM character of conductor 3 ... So ν identifies G_K^ab with 1 + 3Ẑ[ω] (class number one, units μ₆). The CM
character of y² = x³ + D is −(4D/π)₆⁻¹·π for π ≡ 2 mod 3 (Ireland–Rosen, ch. 18 §3, Thm 4); D = 16 gives 4D = 2⁶"; "On Galois it is the CM
character of y² = x³ + 16, not of y² = x³ + 1; the two differ by the cubic character of 2"; "n = 6 gives the CM unit ν of the Fermat cubic and
the bit a₂. The bit a₃ first appears at n = 12." Locator: `R20\delta_sextic\DELTA_SEXTIC_20261121.md:16-18, 61-65, 169-171`.

**AG-084** — the $(2,3,12)$ triangle group and $\mathrm{PSL}_2(\mathbf Z/6)$. [read]
"Proposition 3 (where a₃ lives). (a) In PSL₂(Z/12) the normal closure of q(τ⁶) has order 8 and contains the central element z₀ = [5I]; the
quotient is PSL₂(Z/6) ... So Ĝ₆ and PSL₂(Z/12) share only level 6 ... (c) ... So a₃ is not metabelian data: no formula in ν, in Jacobi sums, or in
Ihara's beta function can give it. (d) a₃ first appears in the (2,3,12) triangle group. ... (d) q(τ) has order 12."
Locator: `R20\delta_sextic\DELTA_SEXTIC_20261121.md:78-85`.

**AG-085** — Alpöge's $(2,3,6)$-triangle group trick and $\mathbf C/\mathbf Z[\omega]$ as $\mathrm{Weil}_5$. [read]
"their quiet inclusion of the Siegel argument, whose result was strictly dominated by the (2, 3, 6)-triangle group trick, again showed great
taste"; step 3: "qN = M k + R, using x1 · x2 + · · · + xk−1 · xk , wanting "automorphy" of N since µ is automorphic from θ on sixfold cover of GL5
as a period integral of thetas, quadric has natural interpretation on corresponding CM e.g. C/Z[ω] as Weil5 , put Poincaré bundle on the edges
to get θs." Footnote 3: "y the normalized Gauss sum of order #|µK | who lives via θ on the #|µK |-fold cover of GL2 , the reciprocity law of
y(c · c′ ) vs. y(c) · y(c′ ) showing some sort of complete graph, simplifying to the above "path" quadric".
Locator: `RR\TRACE_DET_final_20261121T0218Z_unzipped\work\ALPOGE_remark.txt:97-103, 132-136, 146-157` (Alpöge's remark, literature, as
copied into the run). DELTA_SEXTIC: "In Alpöge's note the sextic material is in step 3 and its footnote 3 (p. 3) and in step 16 (p. 4) ... the
#μ_K-th power reciprocity law (Eisenstein; Kubota)" (`R20\delta_sextic\DELTA_SEXTIC_20261121.md:33-37`). DELTA23: "attached note mentions
metaplectic reciprocity in connection with steps 3 and" (`RR\DELTA23_checkpoint_06...\IMPLICATIONS.md:96`).

**AG-086** — $(2,3,6)$, $E/\mu_6$ and Alpöge's curve (evening digest). [scan]
"(2,3,6) triangle group; its orientation-preserving half is the orbifold group of E/μ₆. That is the curve of Alpöge's"; "ρ = Ind_{Q(√−3)}^Q ψ for a
cubic character ψ, so ρ ⊗ χ = Ind(ψ·(χ∘N)), and L(s, ρ⊗χ) = L(s, ψ') is the L-function".
Locator: `R22\MATHEMATICS_OF_THE_EVENING_20261122.md:123-125, 191`.

**AG-087** — the hexagonal CM curve $\mathbf C/\mathbf Z[\omega]$ = the Fermat cubic, level 3 of the tower; $U(1,1)(\mathbf Z[\omega])$. [scan]
"T5. S the Weil family of abelian fourfolds for K = Q(ω), x₀ = E⁴ with E = C/Z[ω] (the curve of Alpöge's step 3)"; "On E^k, E = C/Z[ω], the bundle
⊗ P_{i,i+1} of step 3 has first Chern class"; "words in multiplication and Fourier transform, that is in the group U(1,1)(Z[ω])"; "hexagonal
curve of step 3 is the Fermat cubic, level 3 of the tower"; "note that C/Z[ω] is the Fermat cubic (Route 5)".
Locator: `R20\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md:137, 284-288, 389-395, 456, 522`.

**AG-088** — every algebraic class on $(\mathbf C/\mathbf Z[\omega])^n$ is a Lefschetz class (SG-04). [scan]
"Let $E/\mathbb C$ be the elliptic curve $\mathbb C/\mathbb Z[\omega]$. Every rational algebraic cohomology class on $E^n$ is generated by divisor
classes"; "**Statement.** If E/C is the elliptic curve C/Z[ω], every rational algebraic cohomology class on E^n is a Lefschetz class, i.e. a polynomial
in divisor classes"; "For the complex curve, End^0(E)=Q(ω)=K. Under the product polarization, End^0(E^n)=M_n(K) and Rosati is conjugate transpose."
Locators: `RR\HODGE_SIGN_final_20261121T0057Z_unzipped\HODGE_SIGN.tex:671-675`; `...\agent_sign_geometry.md:80-84`; prompt 32: "On powers of the
hexagonal CM curve every" (`PRO\SENT\32_HODGE_SIGN_sign-only_purity_as_the_Hodge_index_route_cotes_16_44\PROMPT.md:37`); ORDER.md: "the method in AG
(purity by positivity, theta-lift multiplicity, twisted Tate coefficients, hexagonal CM)" (`PRO\ORDER.md:32`).

**AG-089** — bounded division on the Hecke orbit of $E^8$, $E=\mathbf C/\mathbf Z[\omega]$ (HECKE_DIV). [scan]
"$K=\Q(\omega),\qquad \omega^2+\omega+1=0$"; "For $K=\Q(\sqrt{-3})$ a safe even choice in Markman's construction is $d=12$. The rank is $r=96$, the
quotient isogeny in Section~1.5 has degree $(d+1)^2=169$"; "\citet[Theorem~A]{Severn26}, version~1.5 dated 21 October 2026, proves that the Weil classes
on every split eightfold of Weil type for $\Q(\sqrt{-3})$ are algebraic"; "P2b integral Weil basis cycles have degrees80/80 onE4 and147456/175104 onE8,
with multiplier1. Raw Hecke transport grows as m4/m8"; "The principal balanced E⁸ datum has Δ=1".
Locators: `RR\HECKE_DIV_final_20261121T0204Z_unzipped\HECKE_DIV.tex:66, 511, 1572`; `...\LEDGER.md:70`; `...\IMPLICATIONS.md:27`.

**AG-090** — the $\mathbf Q(\omega)$ Weil-class numbers: $D_0=132{,}269{,}760$, 54, 36, 30,375, 10,125. [scan + read]
"Q(ω), n = 2, principal component: δ_W ≤ D₀ = 132,269,760 (GHOSTS R12, from Schoen 1988/1998, **published**)" (`PRO\SENT\_superseded_46_HODGE_DIVISION_v1_20261121\PROMPT.md:36`);
"C₄ = 531441·δ·D₀⁴·(1 + 4⌈√T⌉)" (`R20\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md:287`); "GHOSTS R10 gets the denominator 54 for Q(ω), n = 2, with two
operators: R = [ω]^* and S = [√−3]^*"; "| Q(ω), a = 3+ω (Nm 7) | 2 | 25,729,836,300 = 2²3⁷5²7⁶ | 193,904,039,700 |" (`R20\hodge_bridge\HODGE_DIVISION_ATTACK_20261121.md:207-211`);
"\delta_W\le30375\Delta\quad(K=\Q(\omega))"; "\delta_W(A,L)\le10125\,f^6\Delta^2 &&\text{if }K=\Q(\omega)" (`RR\HODGE_BOUNDED_CYCLES_final...\paper\sixfolds.tex:21`;
`...\STATEMENTS.tsv:28`); "| Q(ω) fourfolds, principal | 36 |" and "| Q(ω) eightfolds, split | (4D_G⁸Δ)⁸B₀ |" (`R22\paper_seeds\SEED_HODGE_DIVISION.md:254-259`);
"Run GHOSTS R12's Bézout scheme: W₄(C) ∩ T₀ in J(C) embedded by 3Θ, with deg W₄ = 3⁴·9!/5!, and (1 − σ²)^*Θ ≤ 4Θ" (prompt 46 v1, l.49);
"J is not the quantity (Theorem E): on the Q(ω) principal component, J_W is unbounded on CM points" (l.40).

**AG-091** — the split/nonsplit map of the Hodge line: "n = 4 split only over Q(ω)". [read prompt]
"n = 3 split for the nine class-number-one fields, with the inputs marked; n = 4 split only over Q(ω); no case for n ≥ 5. The first theorem needed is
split eightfolds over some K ≠ Q(ω)". Locator: `PRO\SENT\70_HODGE_BOUNDED_CYCLES\PROMPT.md:84-85`. "For $K=\Q(i)$ or $\Q(\omega)$ choose $\tau=i$ or
$\omega$, respectively; then $\kappa_K(\Delta)=1$"; "Outside $\Q(i)$ and $\Q(\sqrt{-3})$, the only r[oots of unity are ±1]"
(`RR\HODGE_BOUNDED_CYCLES_final...\paper\weil.tex:129, 237`).

**AG-092** — the Mumford fourfold over $\mathbf Q(\sqrt{-3})$; Eisenstein eightfolds; the Eisenstein trace network. [scan]
"Write $K=\mathbf Q(\sqrt{-3})$. Let $A$ be the Mumford fourfold" (`RR\HODGE_BOUNDED_CYCLES_final...\paper\mumford-coniveau.tex:22`); "Let $K=\Q(\sqrt{-3})$,
let $\mathcal O_f=\Z+f\mathcal O_K$ act" ... "including the nonzero minor $1728$" (`...\paper\eisenstein-eightfolds.tex:23, 76`); UNFILED.085 (proved):
"The Gaussian trace certificate transfers to an Eisenstein block-reflection network by the proposed Fourier-span argument"
(`RR\HODGE_FINISH_final...\workbench\STATEMENTS.tsv:108`).

**AG-093** — Weil-type eigenspaces under $\omega$ (fleet map HT-01). [read]
"the Z_q action multiplying row block a by omega^a satisfies S_k(g t) = omega^k S_k(t), so its omega-eigenspace is isotropic for every S_k with q ∤ k, the
same mechanism that makes Weil classes Hodge"; "H19 (split Q(omega) Weil eightfolds)". Locator: `FM\hodge_theory.md:22, 42`.

**AG-094** — cubic Kummer characters over $\mathbf Q(\omega)$; the field $\mathbf Q(\sqrt[3]{269})$. [read prompt + HEX + scan]
Prompt 69: "The K-groups of one cubic Kummer field in every degree [AC-G22, K10–K23]"; "RH for the cubic character"; "G185, the class number one of Q(ω,
ζ₇ + ζ₇⁻¹), re-proved"; "an identity with a cubic phase in place of Alpöge's sign, through Patterson's theta series"; "Alpöge's definite theta lifts over
Z[ω]"; "Theorems 1–3 express the same cubic character through the 3-torsion of 269a1 and a quartic–sextic zeta quotient ... including two primes congruent
to 7 modulo 12 whose individual real parts vanish. At shift 3 compare its marked coefficient with the actual Erdős–Straus divisor marks in the companion
SEXTIC_SHELL_WEIGHT.md" (`PRO\69_BEYOND_DIRICHLET\PROMPT.md:19, 57, 63, 81-82, 91`). HEX AC219: "Strict 7-adic Selmer groups of a cubic Kummer twist
family over Q(sqrt-3), L = K(cbrt 269): S_7(K, (E/O)(chi^j xi_7^a c_7^-e)) = O/7^{s(e)}" (`HEX:100`). Seed: "the strict 3-adic Selmer group over K = Q(ω)
of T/O(χε^(-e)), with O = Z_3[ω], T = Q_3(ω), χ the cubic Kummer character of 269" (`R22\paper_seeds\SEED_ALP_CONNES.md:91-92`). Extended Grand RH:
"Let $F=\Q(\sqrt[3]{269})$, $K=\Q(\sqrt{-3})$ and $E=FK$. The polynomial is Eisenstein at 269 and its discriminant is $-27\cdot269^2$"
(`R22\extended_grand_rh\research\cubic_prime_races.tex:25`); "Write $\omega=e^{2\pi i/3}$, $\OO=\mathbb Z[\omega]$, $q=269$. The cubic character $\xi$ of
$(\OO/q)^\times=\mathbb F_{q^2}^\times$" (`...\research\rough_composites.tex:49`); "On the elliptic curve \(y^2+y=x^3-2x-1\), the full 3-torsion realizes the
same cubic splitting field" (`...\research\SECOND_READING.md:31`); "a full sixth-root character over \(\mathbb Q(\zeta_{12})\) and descends to a conjugate pair
over \(\mathbb Q(\sqrt{-3})\)" (l.23).

**AG-095** — cubic Hecke character over $\mathbf Q(\omega)$, cubic reciprocity, tetrahedral frame (prompt 78). [read prompt]
"The attached cubic prime-window paper concerns an S3 extension and a cubic Hecke character over Q(ω)"; "the conjugate signs of product one, cubic
reciprocity or ray-class orthogonality"; "how far the three sign characters of the tetrahedral frame take the critical-line question".
Locator: `PRO\78_SIGNED_COUNTS_AND_WINDING\PROMPT.md:11, 19, 35`.

**AG-096** — Kummer theory at 3 and $\mathbf Z_3[\zeta_3]$ in the section-ghost run. [scan]
"$k=\mathbb Q(\alpha)$, $\alpha^3=3$, and put $A=649^8\alpha$, $U=\alpha^2-2$, $B=U^3$. At the unique place above three, the abelian pair modulo ninth
powers is neither an ordinary-point pair nor a cuspidal pair" (E.43); "$\mathcal O=\mathbb Z_3[\zeta_3]$"; "$\mathbb Z[\zeta_3]\rtimes\mathbb Z/3$";
"using $(\zeta_3-1)^2=-3\zeta_3$"; "the unique cubic character of conductor nine"; "Put \(K=\mathbb Q(\zeta_3)\). The maximal pro-three".
Locators: `LM\SECTION_GHOSTS_final...\SECTION_GHOSTS\SECTION_GHOSTS_results.csv:80`; `...\sections\part_E_elliptic_audit.tex:86, 131, 2556-2573`;
`...\sections\part_E_embedding_gate.tex:465`.

**AG-097** — the degree-nine Fermat cubic cover and the cubic detector dessin. [scan]
"The cover for \(H_0\) is the degree-nine Fermat cubic ... Over \(k=\mathbb Q(\zeta_3)\) its boundary is rational"
(`LM\SECTION_GHOSTS_final...\sections\part_E_symmetry_audit.tex:202-204`); "\subsection{An explicit rational quotient of the cubic detector dessin}";
"The corresponding degree-nine rational Belyi map is"; "$\mathbb Q(\sqrt{-3})$ and has three ramification points"; "Michael Musty's BelyiDB"
(`RR\DELTA23_checkpoint_06_20261121T0329Z_unzipped\agents\characters\proofs\cubic_dessin_rational_quotient.tex:1-185`); "The cyclic3 symmetry of the
compact genus1" (`...\agents\characters\notes\APPROACHES.md:138`).

**AG-098** — the two CM frames as $E_3:y^2=x^3+1$ and $E_4:y^2=x^3-x$; Eisenstein and Gaussian algebras. [scan + read]
"For $E_3:y^2=x^3+1$ and $E_4:y^2=x^3-x$, choose CM-compatible" (`RR\DELTA23_checkpoint_06...\agents\characters\proofs\adelic_frames_draft.tex:22`);
"On $E_3:y^2=x^3+1$, the point ... satisfies $2P=(-1,0)$. The field $K$ contains $\zeta_3$; $P$ and its $\zeta_3$-multiple generate $E_3[4]$"; "For
$E_4:y^2=x^3-x$, its third-division polynomial is" (`LM\SECTION_GHOSTS_final...\sections\part_E_gt_scope_audit.tex:159-181`); "the quadratic twist by two of
\(E_4:Y^2=X^3-X\)" (`...\sections\part_E_arithmetic_cm_base.tex:142`); "Their natural adelic centralizer algebras are different quadratic algebras, the
Eisenstein and Gaussian algebras" (`LM\DELTA_ON_GT_checkpoint_05...\DELTA_ON_GT\sections\A.tex:931-935`).

**AG-099** — Atkin–Lehner defect at level 6 versus Δ (open). [scan]
"| A.86 | Open | Actual marked free-group Atkin-Lehner defect AL6,3 and comparison with Delta |"; "D23.F18 strengthens the level-six limitation: every gentle
H action is inner on the entire congruence completion, so all its congruence Atkin-Lehner defects vanish".
Locators: `RR\DELTA23_checkpoint_06...\LEDGER.md:12`; `...\IMPLICATIONS.md:117`; `...\QUESTIONS.tsv:20`.

**AG-100** — the Klein configuration of ten points and the involution $T(w)=2(w+6)/(w-2)$. [read]
"Let $H=\{1,a,b,ab\}$ act on $\mathbf P^1$ by $a(t)=-t$, $b(t)=1/t$, and let $Z=\mathbf P^1\setminus\{0,\infty,\pm1,\pm i\}$ ... ten labelled points";
"for the quartet $\{0,\infty\},\{t,1/t\}$ the coordinate is $w=t^2+t^{-2}$ ... a cusp at $w=\infty$ ... a cusp at $w=2$ ... and a point of order two at
$w=-2$"; "$r^2+r^{-2}=\frac{2(w+6)}{w-2}=:T(w)$. $T$ is an involution of $\mathcal R$ that fixes $w=-2$ and $w_0=6$ and exchanges the two cusps."
Locator: `R23\h17_note\h17_note_wb0007.tex:321-330, 375-394, 418-425`.

**AG-101** — the thrice-punctured line: Ihara's question at Vandiver primes. [read HEX]
H06b: "Ihara's kernel question: Vandiver implies a positive answer ... 'The question of Anderson and Ihara on the pro-p Galois action on the projective line
minus three points, at every prime satisfying Vandiver's conjecture'". Note: "by Brown's theorem, free on letters $s_m$ of odd weight $m\ge3$"
(`R23\h06b_note\h06b_note_wb0006.tex:139`). Locators: `HEX:23`; `R23\h06b_note\h06b_note_wb0006.tex`. Prompt 65: "the same class groups govern Ihara's question
on the Galois action on the fundamental group of the thrice-punctured line" (`PRO\_superseded_65_K_GROUPS_OF_Z_inside_sent_75\PROMPT.md:13`).

**AG-102** — dessins and Belyi maps in the topology/periods polish (Paper 6). [scan]
RESEARCH_SA09 B0.1: "Transitive monodromy permutations classify connected pre-clean Belyi pairs ... identify Belyi automorphisms with the simultaneous centralizer";
B2.2: "The three roots of that cubic give exactly three normalized sextic Belyi maps of the specified passport"; "any Belyi pair with passport[3,2,1;2,2,1,1;6] has
genus0 by Riemann–Hurwitz"; E.013: "Subdividing every oriented map edge by a white midpoint gives a clean dessin with the specified three permutations, and plane trees
are exactly connected genus-zero one-face cases". Locators: `RR\POLISH_TOPOLOGY_PERIODS_checkpoint_13...\notes\paper06_register_summaries.tsv:28, 33, 39`;
`...\notes\paper06_remaining_statement_first_derivations.md:25`; `...\notes\paper02_register_summaries.tsv:264`; prompt 91: "Paper 6. Grothendieck's tensor divided-power
categories (cote 137) and clean dessins (RESEARCH_SA09)" (`PRO\SENT\91_POLISH_TOPOLOGY_PERIODS\PROMPT.md:106-110`).

**AG-103** — the tame Belyi theorem in positive characteristic. [scan]
"prime-to-$p$ order. Thus the tame Belyi theorem does not provide"; "The general tame Belyi theorem"; "point-theoreticity for quasi-Belyi".
Locator: `RR\AN_GRH_final...\final\recovered\ANABELIAN_A1_cp03_text\ANABELIAN_A1\ANABELIAN_A1_paper.tex:5227, 7957, 8462`.

**AG-104** — the perfect $(2,3,7)$ partner branch, excluded (Hodge division). [scan]
"Exact imaginary-quadratic K models and the perfect(2,3,7)"; "a(2,3,7) partner quotient has actual pulled-back inertia orders2/3/7"; "## The whole large(2,3,7)
partner branch is excluded ... D-TD46 proved ... Q=imU-cover signature(2,3,7)". Locator: `RR\HODGE_DIVISION_checkpoint_34...\IMPLICATIONS.md:610, 620, 722-724`.

**AG-105** — the triple $(2,3,6)$ in the Weil-classes paper. [scan]
"(f, a, g) = (2, 2, 4), (2, 3, 6), (3, 2, 6)." Locator: `PAP\032_Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026.pdf`, text l.1049.

**AG-106** — Hecke computations over $\mathbf Q(\sqrt{-3})$ and the K-groups of Z. [scan]
"In (S8) take $K=\mathbb Q(\sqrt{-3})$, $N=2$"; "Both $7$ and $13$ split in $\mathbb Q(\sqrt{-3})$ and are regular"; "Put $E=\mathbf Q(\sqrt{-3})$, $e=6$, and $N=2$";
KTOWER: "$E^3$, where $E=\mathbf Q(\omega)$"; "and $p=7,13$. It expands the eta products by their logarithmic".
Locators: `RR\K17_checkpoint_08...\K17.tex:365, 1233, 2855`; `RR\KTOWER_checkpoint_11...\KTOWER.tex:267, 290, 774`; HEX H18 (Pintar, hexagon:2611.00829,
"Hecke calculations for the conditional vanishing of K_{4k}(Z) through degree 104", `R23\h18_note\GATE_PINTAR_20261123.md:7`).

**AG-107** — the Weil-projector certificate over $\mathbf Q(\omega)$ and $\mathbf Z[\omega]$ inside $\mathbf Q(\zeta_{24})$. [scan]
"\texttt{weil\_projector\_certificate.py} constructs the projector for \(K=\mathbb Q(\omega)\), \(\omega^2+\omega+1=0\), \(a=3+\omega\) (trace 5, norm 7), for \(n=2,3,4\)";
"The cyclotomic integral-basis theorem gives \(\mathcal O_E=\mathbf Z[t]\) and \(\mathcal O_F=\mathbf Z[\omega]\). Here \(i=t^6\), \(\omega=t^8\)".
Locator: `RR\DEG_L_checkpoint_06_20261121T0517Z_unzipped\DEG_L\DEG_L.tex:3091, 4035`.

**AG-108** — Eisenstein integers in the Fermat audit; cubic residue symbols. [scan]
"The Eisenstein integer ring is Euclidean"; "Writing the cubic residue symbol as \(13^{\lambda}\), the two"; "Chebotarev construction of E.114 controls cubic residue symbols".
Locators: `LM\SECTION_GHOSTS_final...\sections\part_E_fermat_audit.tex:52`; `...\part_E_two_inert_audit.tex:129`; `...\part_E_elliptic_audit.tex:858`.

## 6. Numerology: 24, 12, 691, 1728, 744, and the Monster primes

**AG-109** — 691 and weight 12: $T=\mathbf Z_{691}(12)$, $K_{22}(\mathbf Z)=\mathbf Z/691$. [scan]
"\label{coh:691} For $T=\mathbb Z_{691}(12)$, inflation identifies $H^2(G_{\mathbb Q,\{691,\infty\}},T)\simeq\mathbb Z/691$"; "The calculation $K_{22}(\mathbb Z)=\mathbb Z/691$";
"$(\mathbb Q_{691}/\mathbb Z_{691})(-11)^{G_{\mathbb Q_{691}}}$ ... since $690\nmid11$" (`LM\SECTION_GHOSTS_final...\sections\part_A_cohomology.tex:275-301`); "the weight-twelve/691
class" (`...\sections\part_P_literature.tex:348`); K17: "At691, Sharifi2007 and McCallum–Sharifi Theorem9.11 give a second explicit failure, now in weight12 with quotient Z/691"
(`RR\K17_checkpoint_08...\IMPLICATIONS.md:63`; `...\K17.tex:77`); h06b gate: "Ihara's relation in gr^{12} for p = 691" (`R23\h06b_note\GATE_H06b_ad855737_20261123.md:36`).

**AG-110** — $H^1(G_{\mathbf Q},\widehat{\mathbf Z}(2))=\mathbf Z/24$ and the fractions $n/24$. [scan]
"$H^1(G_{\mathbb Q},\widehat{\mathbb Z}(2))=\mathbb Z/24$, generated"; "$h+k\eta$, for one $k\in\mathbb Z/24$"; "The two congruences select exactly one $k\pmod{24}$"; "The term
$n_j/24$ retains the actual Ihara-action correction"; "$\eta(F_q)=(9-1)/24=1/3$ generates $\mathbb Z_2/8$. At $(q,\ell)=(2,3)$ the value $(4-1)/24=1/8$"; "order $5^2-1=24$ ...
$k\longmapsto k(5^2-1)/24=k$"; "of $1/24$ generates the invariants in each component".
Locators: `LM\SECTION_GHOSTS_final...\sections\part_B_arithmetic_generated.tex:26-81, 146`; `...\part_A_cohomology.tex:532-664`; `...\part_E_elliptic_audit.tex:2930-3033`.

**AG-111** — $K_3(\mathbf F_5)=\mathbf Z/24$. [scan]
"0 = K4 (F5 ) −→ K4 (ON ) −→ G −→ K3 (F5 ) = Z/24." Locator: `PAP\209_An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf`, text l.584.

**AG-112** — 24th roots: $\mathbf Q(\mu_{24},(-2)^{1/24})$, $3^{1/24}$, $(-2)^{1/24}$; $n_0=24$. [scan]
"$\mathbb Q\bigl(\mu_{24},(-2)^{1/24}\bigr)$"; "Let $u=3^{1/24}>0$"; "$R=F((-2)^{1/24},3^{1/3})$. It is abelian over $F$"; "exponents are $n_j=(j+4)!$, including $n_0=24$".
Locators: `LM\SECTION_GHOSTS_final...\sections\part_E_two_first_primes.tex:50, 111, 316`; `...\part_E_elliptic_audit.tex:76, 788`.

**AG-113** — 24 in the CUE collision scale. [scan]
"B_N=N^{1/24},\quad h_N=B_Ns_N." Locator: `RR\ZETA_HEAT_checkpoint_01_20261123T1654Z_unzipped\workbench\paper\sections\cue_collisions.tex:84`.

**AG-114** — 12 in the braid group: $\Omega=(abc)^4$ of degree 12; $B^{\mathrm{ab}}=\mathbf Z/6$. [read]
"So $\Pi$ is a power $\Omega^n$ of the central element $\Omega=(abc)^4$. But $\Pi$ lies in the closed commutator subgroup, and $\Omega$ has degree $12$ in $\Bh_4^{\ab}=\Zh$";
"$\Phi_F$ is the identity on $B^{\ab}=\Z/6$". Locator: `R23\h17_note\h17_note_wb0007.tex:286, 529-530`.

**AG-115** — rank 24 (theta quadrics) and "rank J = 24". [scan]
AG-047 (theta-rank); "\Theta\mathcal J=0,\qquad \operatorname{rank}\mathcal J=24" (`LM\SECTION_GHOSTS_final...\sections\part_E_compact_quaternion_homology.tex:125`).

**AG-116** — 1728 and 744 as integers in the runs. [scan]
"=\frac{96M+48G+1728}{744768}-76800\log_{863}a" (`RR\SIGN_NEXT_checkpoint_02...\SIGN_NEXT.tex:3906`); "including the nonzero minor $1728$" (AG-092); "Thus $|J|=32\cdot54=1728$"
(AG-055); "Per prime44 coassociativity,88 counit,88 antipode,18 orthogonality,7,744 module products" (`RR\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_20...\workbench\records\papers_2_3\SA17_REPORT_TABLE.md:59`).

**AG-117** — $2^{24}$ in a finite field; $d_3=24$, $d_5=168$. [scan]
"2^{24}=276,\quad56^{24}=978," (`LM\SECTION_GHOSTS_final...\sections\part_E_genus_two.tex:247`); "In particular \(d_3=24\) and \(d_5=168\)." (`...\part_E_fermat_audit.tex:192`).

**AG-118** — 23 and 47 (crosscap counts of cote 154). [read HEX]
"The genus of Grothendieck's relative-position surface (cote 154), with the 23 and 47 crosscap counts". Locator: `HEX:84` (row P91c). [mine] 23 and 47 are among Ogg's
supersingular primes (the primes dividing |M|); recorded as a coincidence of numbers only.

**AG-119** — Hermite/Riemann–Hurwitz constants with 12 and 24 in the lambency covers. (See AG-069/070: "$g_0=1+\mu/12-\dots$", "$\equiv0\pmod{24}$", "$\frac N{24}$".)

## 7. The user's vocabulary: ghosts, lambency, triality, Albert

**AG-120** — ghost (Hodge): the definition and the dichotomy. [read]
"A ghost is a class that passes every local test (here: algebraic modulo every good prime, by 032's Remark 8.5 and its CM transport) and whose global status is the question"
(`PRO\SENT\39_HODGE_GHOST_CLASSES_at_supersingular_and_ordinary_primes\PROMPT.md:36-37`); "A non-algebraic Hodge class is a ghost: finite complexity at every prime, tending to
∞ cofinitely (R3)" (`R20\hodge_bridge\HODGE_DIVISION_ATTACK_20261121.md:36`); "a counterexample would be a ghost" (prompt 46 v1, l.12); theorem "[Eventual minimum-degree
dichotomy]\label{thm:ghosts}" (`RR\HODGE_BOUNDED_CYCLES_final...\paper\main.tex:313-319`); GHOSTS run title "GHOSTS: bounded cycle complexity, CM transport, and an exact
Eisenstein Weil-class calculation" (`RR\GHOSTS_final_20261121T0256Z_unzipped\GHOSTS.tex:34`); "In the project's vocabulary it would be a ghost"
(`R20\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md:250`). Moonshine contact: the exact test of the ghost run is on $E^4$, $E:y^2+y=x^3$, $K=\Q(\omega)$ (AG-028).

**AG-121** — ghost (sections): the SECTION_GHOSTS run and the GT tower. [read]
"We have neither proved finite support for every ordinary pair surviving the full pronilpotent tower nor constructed one ordinary infinite-support pair with a compatible full-tower
section" (`LM\SECTION_GHOSTS_final...\SECTION_GHOSTS\README.md:28`); "The deeper ghosts take valuations divisible by `∏_{r ≤ R}(Q^r − 1)` (A.62, A.66)"; "No fixed finite level
separates a ghost from a point"; "an ordinary ghost that survives the whole pronilpotent tower has finite support, so by A.32 it is a rational point" (target)
(`<local>/Documents\pro_intake_20261116\EXPERT_GT_TOWER_AND_GHOSTS_20261116.md:46-99`). Moonshine contact: the same run proves the GT̂ chain E.176-E.191 (AG-078, the
elliptic points, the hexagonal curve).

**AG-122** — "the ghost as a sign". [scan]
"- **The ghost as a sign.** Root numbers ε = ±1; polarization signs; the parity ± in GCT VIII's ±(v − v⁻¹)^a f; the". Locator: `R23\NONSTANDARD_RH_SLICES_20261123.md:234`.

**AG-123** — lambency. (AG-069/070: EXIT_TOWER D.14-D.15, "The twenty-three lambencies, computed as covers"; the 14 Nov files named
`*_before_ghost_lambency_20261114.md` in `<local>/Documents\pro_intake_20261114\`.)

**AG-124** — triality: in the Kuga–Satake paper, the polish runs and the Hodge runs. [scan]
"a triality automorphism exchanging the vect[or]" (type D4; `PAP\032_Algebraic-Kuga-Satake...pdf`, text l.816); "triality-S3 counts in D4" (AG-065); "${}^3D_4(q)$" (AG-064);
"triality in rank four" (AG-062); "g2_triality_section" (AG-067); "the affine-plane triality" (AG-068); POLISH_CRISTAUX check events: "Full common Cartier incidence/triality/linear
symmetrizer/actual relative rank/birational proof independently rederived" (`RR\POLISH_CRISTAUX_checkpoint_18_20261123T1744Z_unzipped\CHECK_EVENTS.tsv:1765-1768`).

**AG-125** — "the September Albert representation". [scan]
"In the September Albert representation, two consecutive traces of a three-cycle vanish and its t[race ...]". Locator:
`R22\extended_grand_rh\research\MATHEMATICS_LOGBOOK.md:67`.

---

## 8. Searched, and what was set aside as a name collision

- **Searched (bounded, named folders only).** All PROMPT.md files and ORDER.md under `PRO\` (SENT 30-41, 62, 67, 67c, 70-70c, 90-92b, the unsent and superseded 46,
  63-73, 78, 93, 94); the returns listed in the header (latest checkpoint of each run; HODGE_DIVISION cp28 and cp34; text files only); `R23\` whole; the AG/Hodge parts
  of `R20\` and `R22\` (hodge_bridge, delta_sextic, deligne_sign_only_paper, split_zero, alpoge_rh, errata, IMPLICATIONS/NIGHT/SCRIBE/digest; hodge_reduction,
  MATHEMATICS_OF_THE_EVENING, paper_seeds, extended_grand_rh, gct_flip, second_pass_intake_audit, stalled_runs); `HEX`, `HEXAGON_BOARD.tsv`, `HEXAGON_CANDIDATES.md`;
  the intakes of these runs in `INT\`; the Longue Marche records the H17 note points to (SECTION_GHOSTS final, DELTA_ON_GT cp05, EXIT_TOWER cp28 sections D_lambencies and
  E_cm_parity_vanishing, `results_register\delta_referee_20261118`, the LM intake/expert files of 13-19 Nov); `PAP\` (the AG/Hodge PDFs, hodge_sources_20261121,
  successor_sources_20261121, Alpoge_Jacobian_Counterexample); `FM\algebraic_geometry.md`, `FM\hodge_theory.md`.
- **Not opened, by rule:** everything of prompt 74 (`74_*`, `74b_*`, `74c_SAT_WITNESS_EXTRACTION`, `reports_20261122\sat_kronecker_finite_fields`).
- **Not opened for lack of time:** LM7_PUSH (28,801 files) except through the H17 and DELTA_SEXTIC quotations of E.58, E.61, E.65; GT_TOWER_CHECK (A.C13-A.C17 only through
  the H17 crosswalk); the transcribed archive cotes (`MPL_*`), apart from the cote 63-64 pointer in ORDER.md; the moonshine dictionary of 14 Nov (other agents' sources).
- **Name collisions set aside (no entry):** "Ogg" = Néron–Ogg–Shafarevich / Grothendieck–Ogg–Shafarevich (POLISH_*, JAC1964, SIGN_NEXT, GRH_ALGORITHMS_FINISH, 001);
  "elliptic genus" = "hyperelliptic genus" / "nonhyperelliptic genus-three" (HECKE_DIV, JAC1964, HODGE_BOUNDED_CYCLES); `\sum_{j=0}` and similar indices; "cusp" of a
  punctured curve (h07) and the cusp singularity $t^2,t^3$ (s20) and the cuspidal line of p90a; `M_{11}, M_{12}, M_{21}, M_{22}` as matrix entries and equation labels
  (HODGE_SIGN, HODGE_BOUNDED_CYCLES, HODGE_FINISH, SECTION_GHOSTS E.208, DELTA_ON_GT (M11)); "M23" in prompt 68 (= statement label MT-M23); 196883, 196884, 744, 1728, 691,
  65520 occurring as digit strings inside long certificate integers or index lists (HODGE_FINISH gaussian_network and q32 certificates, ZETA_HEAT heat_trace_certificate);
  "691" as a page number in Masullo's text and in a bibliography (Drinfeld, J. Algebra 272, 643–691); "textheight=691.40198pt" (build logs); "Ghostscript"; the h15 table row
  $g=3$, exponent $1/12$; `\mathcal O_K=\mathbf Z[\omega]` of discriminant −23 at cote 15 (`RR\ARCH_ALG_final...\research\cote15\cote15_honda_check.tex:27`), where ω is not a
  cube root of unity.

## 9. The objects that recur most

1. **The hexagonal curve $E_0=\mathbf C/\mathbf Z[\omega]$ ($y^2=x^3+1$, $Y^2=Z^3+1$, $y^2+y=x^3$, the Fermat cubic; j = 0) with $\mu_6$ and $\mathbf Q(\omega)$:** AG-001,
   003, 017-018, 028, 080-098, 120 (Δ on GT̂, the (2,3,6) lattice, Alpöge's step 3 "C/Z[ω] as Weil5", HECKE_DIV's $E^8$, the Q(ω) Weil-class numbers, the Γ₁(3) forms of the K-tower).
2. **The Gaussian curve $y^2=x^3-x$ (j = 1728, $\mathbf Z[i]$, $\mu_4$):** AG-001, 002, 004, 015-016, 023, 034-035, 048, 098.
3. **$\mathrm{SL}_2(\mathbf Z)\cong$ the modular group $C_2*C_3$, the $(2,3,\infty)/(2,3,6)/(2,3,12)$ triangle groups and level 12 ($\mathrm{PSL}_2(\mathbf Z/12)$,
   the units {1, 5, 7, 11}, η and $\chi_{12}$):** AG-001, 005-009, 054-058, 078-086, 114.
4. **$E_8$ and even unimodular / Hermitian lattices ($W(E_8)$, the K3 lattice, $U\oplus U(3)\oplus E_8(-1)^2$, rank-24 theta quadrics):** AG-044-051, 062, 065-066.
5. **Hauptmoduln and η-products ($X_0(6)$; the 23 umbral covers with $T^X=q^{-1}-d^X+\dots$; $\eta(3\tau)^9/\eta(\tau)^3$, $\eta(\tau)^6\eta(3\tau)^6$):** AG-006, 017, 069-071.
6. **Theta lifts and theta series (Alpöge's chain; 032; the Weil representation):** AG-019-021, 031, 033.
7. **24 and 691 / weight 12:** AG-008-009, 069-070, 109-113.
