# FIND_s6: every appearance of moonshine structure in the S6 work

Dossier of the S6 domain for the moonshine swarm of 23 Nov 2026. Compiled by Claude Opus 5.5 at effort max (one agent
of the swarm). Running notes: `<local>/Documents\agent_notes\moonshine_find_s6_NOTES.md`.

**What this is.** One numbered entry per appearance (S6-001, ...). Each entry gives the objects, the statement or
formula as written in the source (TeX lightly flattened; constants, signs and labels unchanged), the exact locator,
and what the source uses it for. No entry was dropped for seeming peripheral, and no entry judges relevance. Where I
add a fact of my own (an identification or an exact equality between two entries), it is marked **[finder's note]**
and was checked (computation named) or is a standard fact stated as such. Source status words ("proved", "refuted",
"recalled, not checked", "hunch") are the sources' own and are kept.

**Provenance of the sources (for the reader of the conference).** The S6 papers and returns are AI-produced (GPT-6
Astra in ChatGPT Pro mode, GPT-5.6 Sol / GPT-6 Astra in Codex at reasoning effort ultra for the workbench, with intakes
by Claude Fable 5.2 at effort high and at effort max and Claude Opus 5.5 at effort max, as Paper I L6095-6097 records); no human has checked the mathematics (Paper I, L6083-6116). The workbench lattice lane (Aug-Sep 2026) takes
its mod-840 lattice from the user's Erdős–Straus corpus (S6-061).

## Locator aliases

| Alias | Path |
|---|---|
| [I] | `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z_unzipped\S6_SERIES_PUBLISH_I.tex` (Paper I, version of 21-22 Nov) |
| [II] | `...\returns\S6_SERIES_PUBLISH_checkpoint_52_20261123T1647Z_unzipped\S6_SERIES_PUBLISH_II.tex` (Paper II, newest, 23 Nov 16:47Z) |
| [III], [IV], [V] | `...\returns\S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z_unzipped\S6_SERIES_PUBLISH_{III,IV,V}.tex` |
| [S605] | `...\returns\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC\` (return of 15 Nov) |
| [S605P] | `...\s6_pro_prompts_20261112_work\sent_20261115\S6_05_ARITHMETIC\PROMPT_as_sent_20261115.md` |
| [PUSH] | `...\returns\S6_02_PUSH_final_20261115T2217Z_unzipped\S6_02_PUSH\S6_02_PUSH_report.md` |
| [CN] | `...\s6_pro_prompts_20261112_work\S6_08_PAPERS\stage\3_reviews_notes\notes\CLAUDE_NOTES_S6_20261115-16.md` (Claude Opus 5.5 at effort max, 15-16 Nov; its §38 lists corrections by Claude Fable 5.2 at effort high) |
| [LZQ], [LZC] | `...\s6_pro_prompts_20261112_work\reviews\LEECH_Z24_QUESTION_20261113.md`, `...\LEECH_Z24_CONSULT_20261113.md` |
| [ROUTES] | `...\s6_pro_prompts_20261112_work\reviews\S6_ROUTES_FABLE_MAX\NOTES.md` |
| [WB] | `<local>/Documents\s6_workbench_repo_20261112\codex_workspace\canonical_S6_snapshot\supporting_materials\workbench\research\` (identical copies under `s6_pro_prompts_20261112_work\S6_08_PAPERS\stage\4_background\workbench\`) |
| [WBE] | `<local>/Documents\s6_workbench_repo_20261112\codex_workspace\canonical_S6_snapshot\supporting_materials\workbench\` |
| [KA] | `<local>/Documents\s6_workbench_repo_20261112\yang_mills_repository_s6\27_s6_key_advances_frozen_2026-09-06.tex` |
| [D1] | `<local>/Documents\s6_workbench_repo_20261112\survey_20261112\work\D1_notes.md` (survey reader D1, Claude Fable 5.2 at effort high, 12 Nov) |
| [CG] | `<local>/Documents\s6_workbench_repo_20261112\codex_workspace\courses\CG-S6\src\` |
| [TRI] | `[WBE]\evidence\quaternionic_4441_audit_20260904\source\Triality_4-4-4-1_Dynamic_Completion_20260904\triality_dynamic_completion.tex` |
| [HEX] | `<local>/Documents\field_experts\hexagon\HEXAGON_STATUS.md` |

Line numbers (L...) refer to those exact files. Labels (`fam:src:F.1.1`, ...) are the sources' own.

---

## 1. The j-invariant and modular functions

**S6-001** · j-line base, `t = j/1728`, E4, E6, Δ, η, Weierstrass model
- Statement: `N(z,\tau)=|\vartheta_1(z,\tau)/\eta(\tau)| e^{-\pi(\Im z)^2/\Im\tau}`, `\Delta_0=q\prod_{n\ge1}(1-q^n)^{24}`, `t=j(\tau)/1728`. "Then `t=E_4^3/(1728\Delta_0)` and `t-1=E_6^2/(1728\Delta_0)`." Arithmetic model `E_t: Y^2=X^3-\tfrac34t^3(t-1)X+\tfrac14t^4(t-1)^2`, `P_t=(0,t^2(t-1)/2)`, `\Delta_E=27t^8(t-1)^3`; `g_2^3-27g_3^2=(2\pi)^{12}\eta(\tau)^{24}`; archimedean local height `-\log N`.
- Locator: [I] L6382-6416, definition `I:def:theta-height`.
- Context: the conventions of Paper I for periods, the norm N and heights of the section P.

**S6-002** · the source rational elliptic surface with `j = 1728t`; the base IS the j-line
- Statement: "`y^2=x^3-3t^3(t-1)x+2t^4(t-1)^2`. It has `j=1728t` and singular fibres of types `IV^*`, `III`, and `I_1` at `p_1,p_2,p_0`" ([E26] §2). Homology monodromies `C_1=(\begin{smallmatrix}-1&-1\\1&0\end{smallmatrix})`, `C_2=(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix})`, `C_0=(C_1C_2)^{-1}=(\begin{smallmatrix}1&1\\0&1\end{smallmatrix})`. [CN] §6: "The degree of J is the sum of n over the `I_n` fibres, which is 1. So `J: P^1 -> P^1_j` is an isomorphism sending 0 to 0 (j = 0), 1 to 1728 and inf to inf. The base of the S6 construction is the j-line tripod, and the `I_1` fibre is its cusp."
- Locator: [V] L10755-10784 (definition before `maps:src:E.1.2`); [CN] L5-10; also [S605P] L17.
- Context: the elliptic surface from which every complex six-sphere `X_c` of [AC26]/[E26] is built; Paper V forms its fibre product with X.

**S6-003** · the lift τ of the (3,4,∞) orbifold through j; cusp expansion `q = w/1728`
- Statement: "Theorem 1.1. There is a holomorphic function `\tau:\mathfrak h_z\to\mathfrak h` with `j(\tau(z))=1728t(z)`, `\tau(g_1z)=(\tau(z)-1)/\tau(z)`, `\tau(g_2z)=-1/\tau(z)`, `\tau(g_0z)=\tau(z)-1`. It has `\tau(z_1)=\rho,\tau(z_2)=i`; ... orders of `\tau-\rho,\tau-i` are 1,2. In the specific cusp coordinate `w=1/t`, `e^{2\pi i\tau}=w/1728+O(w^2)`." Modular facts used: `E_4=1+240\sum\sigma_3(n)q^n`, `E_6=1-504\sum\sigma_5(n)q^n`, `\Delta_{\rm mod}=(E_4^3-E_6^2)/1728=q\prod(1-q^n)^{24}`, `j=E_4^3/\Delta_{\rm mod}`, `j-1728=E_6^2/\Delta_{\rm mod}`. Workbench form: `J_B=1728(t\circ\pi)`, "`j:\mathfrak h_\tau^\dagger\to\mathbb C\setminus\{0,1728\}` is an unramified covering with deck group `PSL_2(\mathbb Z)`"; at a translate of `z_1`, `J_B` has local degree three over 0, at `z_2` local degree four over 1728. Further cubic data: `c_4=144t^3(t-1)`, `c_6=-1728t^4(t-1)^2`, `\Delta_{\rm cub}=1728t^8(t-1)^3`, `\Delta_\infty=1728v(1-v)^3`.
- Locator: [CG]`global-periods-and-line-bundle-quotients.md` L49-110 (Thm 1.1, eqs. 1.4-1.9) and L558-567; [WB]`candidate_geometry.tex` L150-175, L604-607 (`q=(1728R)^{-1}(1+O(R^{-1}))`).
- Context: construction of the period map of the (3,4,∞) family (course CG-S6 lesson 4; original candidate geometry of the workbench).

**S6-004** · `J(q)=q^{-1}+744+196884q+...` and the natural boundary of the family
- Statement: "For every `w_0` with `|w_0|=216` ... there is no flat proper holomorphic map ... whose fibre at each `w\in U\cap\{0<|w|<216\}` is biholomorphic to `X_w`. The intrinsic divisor `2S_2` and its Albanese nome `iw/216` retain the invariant `J(iw/216)`, where `J(q)=q^{-1}+744+196884q+\cdots` has the unit circle as a natural boundary." Proposition: "For `0<|w|<216`, the reduced multiplicity-four surface has `j(\operatorname{Alb}S_2(w))=J(iw/216)`, `J(q)=q^{-1}+744+196884q+\cdots`. This holomorphic function has no meromorphic continuation through any point of `|w|=216`."
- Locator: [I] L5703-5713 (Theorem G, `series:I:G`), L6030-6034 (step G-1); [I] L15610-15620 (`push:src:D.1.1`); Known/new table L6079 ("the map `w\mapsto iw/216` supplies the modular boundary").
- Context: the outer boundary of the parameter disc is the natural boundary of Klein's J; it obstructs continuing the family of complex six-spheres.

**S6-005** · Albanese curves of the multiple fibres and their j-invariants
- Statement: "`\operatorname{Alb}(S_1)=\mathbb C/(\mathbb Z+\kappa_1(c)\mathbb Z)`, `\operatorname{Alb}(S_2)=\mathbb C/(\mathbb Z+\tfrac12\kappa_2(c)\mathbb Z)`. Writing `J(q)=q^{-1}+744+196884q+\cdots`, their invariants are `j_1(w)=J(e^{-2\pi i\kappa_1^{\rm part}}w^2)`, `j_2(w)=J(e^{-\pi i\kappa_2^{\rm part}}w)`." Outside a countable exceptional set, equality of both Albanese invariants forces `c'-c\in2\mathbb Z`.
- Locator: [I] L8768-8782 (`fam:src:A.4.1`).
- Context: the Albanese j-invariants recover the family parameter modulo its period subgroup.

**S6-006** · exact nomes `q_1=-w^2/48^3`, `q_2=iw/216`, `q_1=(27/64)q_2^2`
- Statement: "`\kappa_1=c+\tfrac12-\frac{3i}{2\pi}\log48`, `q_1=-w^2/48^3`, `\kappa_2=c+\tfrac32-\frac{3i}{\pi}\log6`, `q_2=iw/216`, `q_1=(27/64)q_2^2`. The family is parameterized by `0<|q_2|<1` and exists precisely in that domain. ... `j(\operatorname{Alb}S_1)=J(-w^2/48^3)`. This function is holomorphic on `0<|w|<48^{3/2}`, has a pole of order two at zero, and has a natural boundary at `|w|=48^{3/2}`. In particular it continues holomorphically through every point of the family boundary `|w|=216`." Theorem B: "the reduced finite fibres have Albanese nomes `q_2=iw/216`, `q_1=-w^2/48^3=(27/64)q_2^2`."
- Locator: [I] L15073-15092 (`ari:C.2.1`), L5382-5385 (Theorem B); prompt version [S605P] L68 (Lead 8).
- Context: identifies the isomorphism classes of the family with the punctured unit disc in the nome of `Alb S_2`.

**S6-007** · the constants 216 and `48^3` as 1728 divided by norms of ramified primes; Siegel values
- Statement: "`|q1|=|w|^2N(z1)^{12}/1728^2` and `|q2|=|w|N(z2)^6/1728` ... `N(z1)^4=\mathrm{Norm}(1+\rho)=3` and `N(z2)^2=\mathrm{Norm}(1+i)=2`, so `48^3=1728^2/3^3` and `216=1728/2^3`. The points `(2-\rho)/3` and `(1-i)/2` generate the kernels of the ramified primes (`\sqrt{-3}`) of `Z[\zeta_3]` and `(1+i)` of `Z[i]`." §33: "For `a=(2/3,1/3)` and every τ: `g_a(\tau)^{12}=\Delta(\tau)/\wp'(z_a)^4` ... `g_a(\rho)^{12}=-27` ... For `b=(1/2,1/2)`, `g_b(\tau)=-e^{-\pi i/4}f(\tau)^2` (Weber), `f(i)^{12}=8`, `g_b(i)=-1+i`." "`q1=c1 r^{12}` with `c1=-2^{-12}3^{-3}=g_a(\rho)^{12}/1728^2`; `q2=c2 r^6` with `c2=i/216=g_b(i)^6/1728`" (`1728^{1/6}=2\sqrt3`); "`c2^{1/6}=e^{\pi i/12}/\sqrt6` lies in `Q^{ab}`; `c1^{1/12}=e^{\pi i/12}3^{-1/4}/2` does not. It generates `Q^{ab}(3^{1/4})`". Correction §38: the canonical datum is the ratio `q(Alb S_1)/q(Alb S_2)^2=27/64`, whose class in `Q^{ab*}` modulo twelfth powers has order exactly two; no Galois group acts on anything in S6.
- Locator: [CN] L110-119 (§23), L335-366 (§33), L469-475 (§38).
- Context: Claude's notes explain the family's constants through the Néron/Siegel side (second Kronecker limit formula) at the two CM fibres.

**S6-008** · the theta formula for the missing period; exact domain `0<|w|<216`
- Statement: "`\beta_{\rm part}=\frac{6i}{\pi}\Log\frac{\vartheta_1(\mu,\tau)}{2\sqrt3\,\eta_D(\tau)}`, `N(P)=|\vartheta_1(\mu,\tau)/\eta_D(\tau)|e^{-\pi(\Im\mu)^2/\Im\tau}`" ... "`D_{\rm part}=\frac6\pi\log\frac{N}{2\sqrt3}`, `\max N=\sqrt2` (t=1), `\max D_{\rm part}=-\frac3\pi\log6`. All ordinary fibres and both normalized finite root fibres are compact complex tori exactly on `\Im c<H_*:=\frac3\pi\log6`, `0<|w|<216`." "`t=0` is a noncritical `C^1` point with `L_t(0)=7/384`"; levels below the maximum are Jordan curves star-shaped about 1; possible `C^1` point on the level `L=\tfrac14\log3`. Special values: `\mu_0=\frac12-\frac{i\log a}{2\pi}`, `\mu(z_1)=\frac{2-\rho}{3}`, `\mu(z_2)=\frac{1-i}{2}`, `\beta^{\rm part}(z_2)=i(\frac32-\frac3\pi\log6)`, `\Re\beta^{\rm part}(z_1)=-\frac12`, `e^{2\pi i\mu_0}=-a`, `a=5+2\sqrt6`.
- Locator: [I] L5246-5281 (Theorem A), L6692-6712 (`fam:src:C.1.1`), L6793-6809 (`fam:src:C.2.1`: norm invariant under `[v]\mapsto[v/(c\tau+d)]`, `\tau\mapsto(a\tau+b)/(c\tau+d)` in `SL_2(\mathbb Z)`).
- Context: the period of the AC26 complex structure in closed form; the domain of existence.

**S6-009** · theta/eta values at ρ and i
- Statement: "`\vartheta_1((2-\rho)/3,\rho)/\eta(\rho)=e^{\pi i/12}\,3^{1/4}e^{\pi/(6\sqrt3)}`, `\vartheta_1((1-i)/2,i)/\eta(i)=\sqrt2\,e^{\pi/4}`, `\beta^{\rm part}(z_1)=-\frac12+i(\frac1{\sqrt3}-\frac3{2\pi}\log48)`, `\beta^{\rm part}(z_2)=i(\frac32-\frac3\pi\log6)`. Consequently `N(z_1)=3^{1/4}`, `N(z_2)=\sqrt2`, `D_{\rm part}(z_1)=-3\log48/(2\pi)`, `D_{\rm part}(z_2)=-3\log6/\pi`."
- Locator: [I] L6936-6953 (`ari:C.1.2`); request: [S605P] L67 (Lead 7).
- Context: values at the two CM fibres (equianharmonic and square lattices).

**S6-010** · Dedekind η and the odd Jacobi theta function
- Statement: "`\vartheta_1(v,\tau)=2\sum_{n\geq0}(-1)^n e^{\pi i\tau(n+1/2)^2}\sin((2n+1)\pi v)`, `\eta_D(\tau)=\eta(\tau)=e^{\pi i\tau/12}\prod_{n\geq1}(1-e^{2\pi in\tau})`. Choose the cusp lift reached from `\tau=iT`, `T>1`, on which `\mu=1/2-iy(T)` ... Put `a=5+2\sqrt6` and `\rho=e^{\pi i/3}`."
- Locator: [I] L6675-6690 (`I:theta-series-cusp-branch`); L6832-6846 (`I:logarithmic-lattice-norm`, `\rho=(1+i\sqrt3)/2`).
- Context: normalizations underlying every theta/eta formula of the series.

**S6-011** · Siegel functions and modular units of level n
- Statement: "`g_a(\tau)=-e^{\pi ia_2(a_1-1)}q^{B_2(a_1)/2}(1-e^{2\pi iv})\prod_{r\ge1}(1-q^re^{2\pi iv})(1-q^re^{-2\pi iv})`, `B_2(x)=x^2-x+\tfrac16`. Then `g_a(\tau)=i e^{\pi ia_1v}\vartheta_1(v,\tau)/\eta(\tau)`, `N(v,\tau)=|g_a(\tau)|`. When `a\in n^{-1}\mathbb Z^2\setminus\mathbb Z^2`, `n\ge2`, `g_a^{12n}` is a modular unit for `\Gamma(n)` with Fourier coefficients in `\mathbb Q(\zeta_n)` ... `\lambda_\infty(Q)=-\log N(Q)`. Thus `D_{\rm part}=-(6/\pi)(\lambda_\infty(P)+\log(2\sqrt3))`."
- Locator: [I] L7038-7063 (`ari:C.4.1`, cited); request [S605P] L70 (Lead 10).
- Context: identifies the period norm with a Siegel function and the archimedean Néron height.

**S6-012** · division-polynomial norm law and the five torsion values
- Statement: "`N(P)^{m^2}=\frac{N(mP)|\Delta_E|^{(m^2-1)/12}}{|\psi_m(P)|}`. For torsion P of order n and `m\equiv\pm1\pmod n`, `N(P)^{12}=|\Delta_E|/|\psi_m(P)|^{12/(m^2-1)}`." Table t / ord(P) / `N(P)^{12}`: 0/3/27; 1/2/64; 32/5/4/10; `64(47-27\sqrt3)/11`/6/`17+10\sqrt3`; `64(47+27\sqrt3)/11`/6/`10\sqrt3-17`. `F_4=5t-32`, `F_5=89t^2+4736t-4096`, `F_6=11t^2-6016t+8192`, `F_7=881t^4+4745344t^3-12079104t^2+24641536t-16777216`, `F_8=49t^4-2614336t^3-7864320t^2+19398656t-8388608`; for `r=N^{12}`: n=4: `r=64/|t|`; 5: `r^5=432^5/((1-t)(5t-32)^4)`; 6: `r^2=1728^2/F_5(t)`; 7: `r^{35}=2^{192}3^{81}/(|t|^8|t-1|^3|F_6(t)|^{12})`; 8: `r^4=1728^4/|F_7(t)|`.
- Locator: [I] L5283-5301 (Theorem A); L7221-7265 (`ari:C.4.4`); L7286-7291 (`F_5(t)(17\pm10\sqrt3)^2=1728^2`).
- Context: exact torsion values of the period norm (powers of 1728, 432, 27, 64 appear as the cusp constants).

**S6-013** · global height formula and the eleven rational CM fibres (class number one singular moduli)
- Statement: "`\sum_{\sigma}\log N(P_{\sigma(t)})=\sum_{v\nmid\infty}n_v\lambda_v(P_t)-[K:\Q]\widehat h_O(P_t)`" ... "At the eleven nonspecial rational CM parameters `t=j/1728` its values are" j / `A_t`: 8000/`\sqrt6`; 54000/`2^{2/3}3^{1/4}`; 287496/`2^{3/4}`; 16581375/2; −3375/2; −32768/`\sqrt3`; −884736/1; −12288000/`3^{5/12}`; −884736000/1; −147197952000/1; −262537412640768000/1. Proof: "The CM discriminants ... are −8,−12,−16,−28,−7,−11,−19,−27,−43,−67,−163. Enumeration of primitive reduced forms ... gives exactly one form of each discriminant ... the CM theorem ... makes the corresponding singular modulus an integer. The Fourier enclosures ... place it within 1/4 of the specified j." Minimal models: row 11 `j=-262537412640768000`, `[a_3,a_4,a_6]=[1,-75065352465446420,7916029533155605844266842]`, `y_P=-2813543945482`; local-height table with Kodaira types `III^*,I_n^*,III,IV` at p=2,3,7,11,19,23,31,43,67,127,163.
- Locator: [I] L5303-5326 (Theorem A), L26780-26855 (`ari:C.6.3`), L26995-27009 (discriminants); heights table L26893-26915 (`I:CM-height-sizes`); L26985-26992 (enclosures of radius `<10^{-236}`).
- Context: the norm at the CM fibres of the family; **[finder's note, standard]** the thirteen class-number-one j-values are 0, 1728 (the two orbifold points of the base) and these eleven.

**S6-014** · CM newform coefficients for s = 11, 43, 67, 163; ranks, L-derivatives, Heegner points, Sha
- Statement: "For `s=11,43,67,163`, let `E_s` be the respective rational elliptic curve `121b1`, `1849a1`, `4489a1`, or `26569a1`. The coefficients of its normalized newform are `b_n=\sum_{a^2=n,\ a>0}(\frac as)a+\sum_{u,v>0,\ u\equiv v\ (2),\ u^2+sv^2=4n}(\frac{(s+1)u/2}{s})u`." Ranks: "two for j=8000 and j=−12288000, and one for all nine other values"; `L'(E_i,1)/\Omega_i`: 0, 5.13439843, 2.13412085, 31.81013979, 1.86946271, 3.42887338, 0.36258335, 0, 9.62927392, 16.04238858, 1247.32180615; `L''(E_1,1)/\Omega_1=28.71408723...`, `L''(E_8,1)/\Omega_8=78.03222042...`. Analytic leading quotients: "`Q_i=1` for `i=2,3,4,5,6,7,9,10` and `Q_{11}=9`"; Kolyvagin's Heegner-point theorem and the Gross–Zagier Heegner height are used for rank one and finite Sha; open: "the analytic quotient of row eleven is exactly 9; its identification with `\#\operatorname{Sha}(E_{11}/\mathbb Q)` ... remains open".
- Locator: [I] L27151-27166 (`I:CM-coefficient-series`), L27090-27110 (`ari:C.6.R1`), L27219-27248 (`ari:C.6.R2`), L27450-27468 (Gross–Zagier–Kolyvagin), L27491-27505 (`I:analytic-leading-quotients`), L32175-32182 (open questions).
- Context: BSD-type arithmetic of the CM fibres of the S6 family.

**S6-015** · no CM torsion; the conjugate order-six fibres over `Q(\sqrt3)`
- Statement: "There is no `t\in\mathbb C\setminus\{0,1\}` for which `E_t` has complex multiplication and `P_t` is torsion. On the smooth models at t=0,1 after base change of orders 3,4 ... the limiting points have orders 3,2." "`t_\pm=(3008\pm1728s)/11`" (`s=\sqrt3`); `E_-: y^2=x^3-(18+10s)x+21+12s`, `P_-=(0,3+2s)`, discriminant `1032912+596352s`; bad primes `\mathfrak p_2` (IV*), `\mathfrak p_3` (III), `\mathfrak p_{11,-}` (`I_1`, `\lambda=\log11/12`).
- Locator: [I] L26616-26624 (`ari:C.5.1`), L28015-28063 (`ari:C.6.T2`).
- Context: torsion and CM loci on the family's elliptic section.

**S6-016** · Ramanujan's system, `g_2(i)=\Gamma(1/4)^8/(16\pi^2)`
- Statement: "Put `G=g_2(i)=\Gamma(1/4)^8/(16\pi^2)` ... in the notation `P=E_2`, `Q=E_4`, `R=E_6`: `xP_x=(P^2-Q)/12`, `xQ_x=(PQ-R)/3`, `xR_x=(PR-Q^2)/2` ... For `E=\pi^2E_2/3`, `g_2=4\pi^4E_4/3`, `g_3=8\pi^6E_6/27`: `E'=\frac{i}{2\pi}(E^2-g_2/12)`, `g_2'=\frac{i}{\pi}(2Eg_2-3g_3)`, `g_3'=\frac{i}{\pi}(3Eg_3-g_2^2/6)`." Ramanujan derivatives: `E_6'(i)=-\pi iE_4(i)^2`, `E_4'(\rho)=-(2\pi i/3)E_6(\rho)`; `E_6(\rho)=-27/(\pi^6F^6)` (L13680).
- Locator: [I] L7328-7357 (`I:local-expansion-conventions`), L11469-11471, L13678-13680; [II] L27500 (`E_2'=(\pi i/6)(E_2^2-E_4)`, Atkin–Garvan).
- Context: local expansions of the period near the elliptic points.

**S6-017** · the period scalar `C_4=4\sqrt\pi/(3^{3/4}\Gamma(1/4)^2)`
- Statement: "`\mu_s(0)=i\,C_4`, `C_4=\frac{\sqrt{2/3}}{\pi E_4(i)^{1/4}}=\frac{4\sqrt\pi}{3^{3/4}\Gamma(1/4)^2}>0`. For `r^3=t` ... set `\lambda=\frac{3e^{5\pi i/6}}{2\pi E_6(\rho)^{1/3}}`. Then `\tau=\rho+\lambda r+O(r^2)`, `K_r=-\frac{3i\lambda}{2\pi}r^2+O(r^3)`; `0.2366093140807852<C_4<0.2366093140807853`." Finite coordinate: "`\tau=i+\frac{i}{\pi\sqrt{E_4(i)}}s^2+O(s^4)`".
- Locator: [I] L11437-11464 (`inv:A2.2`), L11283-11297 (`I:def:finite-coordinates`); repository README `<local>/Documents\s6_workbench_repo_20261112\README.md` L127-128.
- Context: the residue connecting scalar that fixes the Hodge number `h^{1,2}=1` of the complex six-sphere.

**S6-018** · the period determinant as `E_4^2/E_6`
- Statement: "`6\mu_z^2-\tau_z\beta_z=\tau_z^2\frac{E_4(\tau)^2}{E_6(\tau)}`. The right side extends holomorphically through the apparent poles. Its exact orders are two at `z_1` and zero at `z_2` ... `\operatorname{divisor}(\det\kappa_0)=p_1+p_2`." Also [I] L12954.
- Locator: [I] L11354-11367 (`inv:A2.1`).
- Context: Kodaira–Spencer divisor of the family.

**S6-019** · local expansions of j at i and ρ
- Statement: "Using `j=1728E_4^3/(E_4^3-E_6^2)`, we obtain `j(\tau)-1728=-1728\pi^2E_4(i)(\tau-i)^2+O((\tau-i)^3)`. Since `j=1728(1+s^4)` ... `j(\tau)=-512i\pi^3E_6(\rho)(\tau-\rho)^3+\cdots`." "`j''(i)=-2\pi^2j(i)E_4(i)`: indeed `j'=-2\pi i jE_6/E_4` and `E_6'(i)=-\pi iE_4(i)^2`."
- Locator: [I] L11469-11484, L16236-16239, L16558-16565.
- Context: branch identification at the order-four and order-three points.

**S6-020** · the weight form Θ = `E_4^2 E_6^{1/2}/Δ` on the (3,4,∞) cover
- Statement: "`\Theta=\frac{(E_4\circ\tau)^2(E_6\circ\tau)^{1/2}}{\Delta_{\mathrm{mod}}\circ\tau}` has those exact factors [`-1/\tau`, `1/\tau`], orders two and one in `s_1,s_2`, and a simple pole in `t_c`." Workbench: "`h^2=E_6\circ\tau` ... `\Theta=(E_4\circ\tau)^2h/(\Delta_{\rm mod}\circ\tau)` ... `\Theta\circ g_1=-\Theta/\tau`, `\Theta\circ g_2=\Theta/\tau`."
- Locator: [I] L8640-8649; [WB]`candidate_geometry.tex` L399-432 (eq. 2.1e).
- Context: trivializes the line bundle L of the period construction.

**S6-021** · the cusp zero of ℘ as a q-series in `\Delta_0/E_6^{3/2}`
- Statement: "`\mu=\frac12-i\beta_{\rm cusp}-\frac{36i\sqrt6}{\pi}\sum_{n\ge1}\frac{a_nq^n}{n^2}`, `\beta_{\rm cusp}=\frac{\log(5+2\sqrt6)}{2\pi}`, `\sum a_nq^n=\frac{\Delta_0}{E_6^{3/2}}`, `\mu''=144\pi i\sqrt6\frac{\Delta_0}{E_6^{3/2}}`."
- Locator: [I] L28524-28540 (`I:cusp-zero-equation`).
- Context: critical-point analysis of the norm.

**S6-022** · radial derivative `(t-1)L_t=X(X-2)/24`; Green function
- Statement: "`X=3Wp/g_2`, `F=1-X`, `W=\vartheta_1'(\mu,\tau)/\vartheta_1(\mu,\tau)+2\pi i\Im\mu/\Im\tau`. These are single-valued modular invariants wherever `g_2\ne0`. ... `X(0)=1/4` and `X(1)=0`. ... `(t-1)L_t=\frac{X(X-2)}{24}`, `r\frac{d}{dr}L(1+re^{i\theta})=\frac{\Re(X(X-2))}{12}`, `F=\frac{6\pi ip}{g_2}R`." `\partial_\tau D_{\rm part}=\frac{iZ}{4\pi^2P}(3ZP-2g_2)`; "`D_{\rm part}(\tau)=-12G_\tau(\mu(\tau))-\frac6\pi\log(2\sqrt3)`" (Green function, Lin–Wang).
- Locator: [I] L28560-28583 (`ari:C.8.12`), L7361-7387 (`ari:C.8.11`), L16368-16383 (`push:src:D.4.4`), L16579-16603 (`push:src:D.4.6`), L5803-5809 (step A-5).
- Context: level curves of the period norm on the j-line.

**S6-023** · signed Gaussian identity; Betti measure of total mass 1/12
- Statement: "`\sqrt{2T}\,|\eta(\tau)|^2N(z,\tau)^2=\sum_{m\in\frac12\Lambda}\epsilon(m)e^{-2\pi|z-m|^2/T}`, where `\epsilon=-1` on Λ and +1 on the three other cosets." "`dd^cL=\frac1{12}\delta_\infty-m_P`, `\int_{\mathbb P^1}m_P=\frac1{12}`"; densities `|t|^{-2/3}/(64T_0|p|^{2/3})` (t→0) and `|t-1|^{-3/2}/(24\pi^2\sqrt{E_4(i)})` (t→1), `T_0=\sqrt3/2`.
- Locator: [I] L28268-28280 (`ari:C.8.8`), L28333-28363 (`ari:C.8.9`); [ROUTES] L50-51.
- Context: the norm as a Green current on the j-line; the mass 1/12 sits at the cusp.

**S6-024** · Mahler-measure identities and complex beta integrals at the two CM lattices
- Statement: "`6L=\int\log|\wp'(z)^2/\wp(z)^3|d\mu`, `N(v)^2=|\Delta(\Lambda)|^{1/6}\exp(-\int\log|\wp|d\mu)`" ... "`N(v)^6=4\exp(\int\log|C(u)|d\nu(u))`", `C(u)=1-(g_2/4)u^2-(g_3/4)u^3`; maximum theorem `\int\log|C|d\nu\leq\log2`, equality iff `g_3=0`. "For the square and equianharmonic lattices ... `\int\log|C|\,d\nu=\log2`, `\int\log|C|\,d\nu=\frac32\log3-2\log2`. They recover `N^2=2` and `N^4=3`." `B_{\mathbb C}(a,b)=\pi\frac{\Gamma(a)\Gamma(b)\Gamma(1-a-b)}{\Gamma(1-a)\Gamma(1-b)\Gamma(a+b)}`.
- Locator: [S605]`sections\C_integral.tex` L4-32 (C.8.6), L75-96 (C.8.7).
- Context: the maximum of the period norm as an inequality of logarithmic Mahler measures.

**S6-025** · theta determinant of the period map (`\eta'/\eta=\pi iE_2/12`)
- Statement: "`\det\frac{d\Omega}{d\tau}=-(\mu'-\frac{i}{2\pi}h)^2-\frac{\wp(\mu,\tau)}{4\pi^2}`. For the AC period branch `\wp(\mu,\tau)=0`, this becomes `\det\frac{d\Omega}{d\tau}=-\frac{g_2(\tau)^2}{36\pi^2g_3(\tau)}`." "`\eta'/\eta=\pi iE_2/12`", "`h(\mu)=1/\mu-\frac{\pi^2E_2}{3}\mu+O(\mu^3)`"; "The modular form `g_2` has a simple zero at ρ and `g_3` a simple zero at i, with no other zeros modulo the modular group." Index-six isogeny to the torus with period matrix `(I,\Omega)`.
- Locator: [II] L27431-27525 (`cdp:st:E8`; "E8" is the statement number E.8, not the lattice), L5442-5452 (in Theorem `series:II:E`); [ROUTES] L51-52, L65.
- Context: Kodaira–Spencer rank of the family (rank one at the order-three point).

**S6-026** · theta values at τ = i
- Statement: "`\frac{\vartheta_1(1/2,i)}{\eta(i)}=2e^{-\pi/6}\prod_{n\geq1}(1+e^{-2\pi n})^2>1`" ... lattice `\mathbb Z(1,0)+\mathbb Z(0,1)+\mathbb Z(\tau,1/2)+\mathbb Z(3,\beta(\tau))` ... "`\det\Omega'(i)=-\frac{\wp(1/2;i)}{4\pi^2}=-\frac{\vartheta_3(0,i)^4+\vartheta_4(0,i)^4}{12}\ne0`."
- Locator: [II] L30128-30225.
- Context: a comparison family with constant section μ = 1/2.

**S6-027** · `j=q^{-1}+744+O(q)` in three deformation arguments
- Statement: [II]: "Its elliptic modulus has nonzero λ-derivative when `|c(\mu)\lambda|` is sufficiently small, as follows from `j(q)=q^{-1}+744+O(q)`." [IV]: "For a small nonzero Tate coordinate we have `j(Q)=Q^{-1}+744+O(Q)` ... For any root of unity `\zeta\ne1`, `Q(j(Q)-j(\zeta Q))\to1-\zeta^{-1}\ne0`" (intrinsic obstruction to every smaller winding). [I]: "The convergent Fourier expansion `j=q^{-1}+744+O(q)`".
- Locator: [II] L29396-29409; [IV] L26739-26748; [I] L10690.
- Context: Tate-curve j-expansion used to detect windings and nonzero derivatives.

**S6-028** · `j_\Gamma/1728` as the period map's left inverse
- Statement: "`j(E)=1728\,4A^3/(4A^3+27B^2)` ... Its discriminant is `1728t^8(t-1)^3` ... `j(\tau)=1728t` (`t\in B^\circ`) ... derivative of the composite `j\circ\tau` equals 1728 ... `j_\Gamma/1728` is a holomorphic left inverse ... `j_\Gamma(p_c(t))=1728t\to\infty`." Step C-4: "The modular function `j/1728` is the period map's left inverse ... proves properness on the finite t-line."
- Locator: [I] L9808-9846, L9897; L5878-5882 (step C-4).
- Context: properness and injectivity of the period map into `\Gamma\backslash\mathcal O_+`.

**S6-029** · genus-zero modular covers of index 4 and 10 with their dessins (collision profiles 50/II, 56/II)
- Statement: "`G=\operatorname{PSL}_2(\mathbb Z)=\langle s,r\mid s^2=r^3=1\rangle`, `[T]=sr`." Coset actions: index 4: `s=(01)(23)`, `r=(023)(1)`, `sr=(012)(3)`; index 10: `s=(01)(24)(35)(69)(78)`, `r=(023)(1)(467)(589)`, `sr=(01265)(384)(79)`. "both curves have exactly one elliptic point of order 3 and none of order 2. Their cusp widths are (3,1) and (5,3,2). The map j to the j-line has respectively degree 4 and 10. Its ramification contributions over 0,1728,∞ are (2,2,2) and (6,5,7). ... Riemann–Hurwitz therefore gives genus zero." Dessin: "Put a black vertex at each r-orbit and a white vertex at each s-orbit ... This is the inverse image of an arc joining the elliptic values on the modular sphere." Words `H=SR^{-1}S^{-1}`, `V=R^{-1}TR`, `B=V^3`, `C=(RSR^{-1})T^2(RSR^{-1})^{-1}`; peripheral words `(T^3,V,H)`, `(T^5,B,C,H)`. Index-four model: "`c_4=t^2(t+27)(t+3)`, `c_6=t^3(t+27)(t^2+18t-27)`, `\Delta=t^7(t+27)^2`, `y^2=x^3-\frac{c_4}{48}x-\frac{c_6}{864}`. ... `c_4^3-c_6^2=1728\Delta`. ... `j(t)=\frac{(t+27)(t+3)^3}{t}`, `j(t)-1728=\frac{(t^2+18t-27)^2}{t}`." Index ten: "`\Delta` of `\mathcal O(12)` with divisor `5p_5+3p_3+2p_2+2a`. ... `c_4^3=j\Delta`, `c_6^2=(j-1728)\Delta`, `c_4^3-c_6^2=1728\Delta`." Rational elliptic surfaces with fibres `(II,I_3,I_1^*)` and `(I_2,II,I_5,I_3)`; Mordell–Weil heights 1/12 and 1/30.
- Locator: [III] L29903-30245 (theorem `mapsD:repair:collision-realization` L29934-29968, proof steps L29983-30207).
- Context: realizing two marked collision profiles used for the S6 maps (Miranda's list, Fukae Table 3 rows 50 and 56).
- **[finder's note]** The index-four passport (cusp widths 1 and 3, one elliptic point of order 3, none of order 2) is that of `\Gamma_0(3)`, and the displayed j-map is the classical `\Gamma_0(3)` relation: with `x=(\eta(\tau)/\eta(3\tau))^{12}` one has `j(3\tau)=(x+27)(x+3)^3/x` (checked by q-series through `q^{26}`: scratchpad `ms\check_x03.py`). So t is a Hauptmodul of level 3; `x+12` is the Monster McKay–Thompson series of class 3B (standard).

**S6-030** · OS49: `j/1728=4t(1-t)`, the index-two modular cover, central `Y^2=X^3+1`
- Statement: "`y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12)` has fibres `IV^*,II,I_2` at 0,1,∞, and primitive Mordell–Weil generator `G=(t^2,t^2)`." "`f^3-g^2=-\tfrac14t^8(t-1)^2`, `j/1728=4t(1-t)`." "The central good-reduction curve is `Y^2=X^3+1`, and G specializes to (0,1), a nonzero point of order three." Height "`2-\frac43-\frac12=\frac16`"; "The verified Oguiso–Shioda Main Theorem table ... has exactly one row with root lattice `E_6+A_1`, namely row49". "Its exact degree-two map `j/1728=4t(1-t)` has permutations `S=(12)` over one, `R=1` over zero, and cusp permutation (12). The associated index-two modular cover therefore has two order-three elliptic points and one cusp of width two." Marking `A=(\begin{smallmatrix}-2&-3\\1&1\end{smallmatrix})`, `B=(\begin{smallmatrix}1&1\\-1&0\end{smallmatrix})`, `C=(\begin{smallmatrix}1&2\\0&1\end{smallmatrix})`, `ABC=I`. "The central normalization is the standard hexagonal toric surface ... Its Euler number is two."
- Locator: [III] L23044-23096 (theorem `night:P3F.26` and proof); [IV] L5358-5375 (Theorem C, OS49 returns `-k(j-1)^2`, fan image `\gcd(k,28)\mathbb Z/28`).
- Context: a component-supported source giving the standard smooth `S^6`.

**S6-031** · OS47: a degree-nine genus-zero modular cover (Todd–Coxeter)
- Statement: "`f=1+8t+40t^2+48t^3`, `g=1+12t+84t^2+280t^3+504t^4` ... `g^2-f^3=-1728t^7(64t^2+13t+2)` gives `I_7` at zero, simple nodal fibres at `t_\pm=(-13\pm7i\sqrt7)/128`, and III at infinity." "`G=(1+4t,12\sqrt3\,t^2)`". Monodromy `A=(\begin{smallmatrix}-5&26\\-1&5\end{smallmatrix})`, `B=(\begin{smallmatrix}1&7\\0&1\end{smallmatrix})`, `C=(\begin{smallmatrix}1&0\\-1&1\end{smallmatrix})`, `D=(\begin{smallmatrix}-2&9\\-1&4\end{smallmatrix})`, `ABCD=I`, `A^2=-I`. "In `PSL_2(\mathbb Z)=\langle S,R\mid S^2=R^3=1\rangle` ... The subgroup generated by `T^5ST^{-5}`, `T^7`, `STS^{-1}`, `T^3STS^{-1}T^{-3}` has ... `S=(12)(34)(57)(6)(89)`, `R=(123)(456)(789)`. The product corresponding to T has cycles (1,3,5,8,7,6,4),(2),(9). ... It gives a degree-nine genus-zero modular cover, with ramification `3^3` over zero, `2^4 1` over one, and cusp widths 7,1,1." Page expression `(-72+168)/24=4`, physical class 4 in `\Theta_7`.
- Locator: [IV] L14540-14619.
- Context: the weighted OS47 source of Theorem IV.B.
- **[finder's note]** The cusp widths have lcm 7, while 9 does not divide `|PSL_2(\mathbb F_7)|=168`; by Wohlfahrt's level theorem this index-9 genus-zero subgroup is noncongruence.

**S6-032** · the Oguiso–Shioda rank-one rows and permutation (dessin) certificates for every j-map
- Statement: rows "43 `E_7` 1/2; 45 `A_7` 1/8; 46 `D_7` 1/4; 47 `A_6+A_1` 1/14; 49 `E_6+A_1` 1/6; 50 `D_5+A_2` 1/12; 55 `A_4+A_3` 1/20; 56 `A_4+A_2+A_1` 1/30" with Kodaira refinements. "Their Euler numbers must sum to 12 ... gives 24 candidates. ... For a candidate let `d=\deg j` ... use `j/1728` ... The minimal ramification profiles over 0 and 1 are `1^{a_0}2^{b_0}3^{(d-a_0-2b_0)/3}`, `1^{a_1}2^{(d-a_1)/2}` ... `x=2d-2-\sum(e-1)` is nonnegative ... Precisely three of the 24 candidates have x=−1: `I_8+II+II`, `I_7+III+II`, `I_5+IV+III`. They cannot occur. ... For each of them the program constructs four explicit permutations `\sigma_0\sigma_1\sigma_*\sigma_\infty=1` ... The verified Euler equation gives genus zero ... This is a j-map with the specified profiles."
- Locator: [IV] L13200-13262.
- Context: classical inputs (Oguiso–Shioda, Miranda) for the source catalogue of Paper IV.

**S6-033** · `I_9+3I_1`: degree-12 j-map and a unique trivalent modular graph
- Statement: "At a=0, b=1 the source has `I_9+3I_1`. Its j-map has degree twelve and ramification profiles `3^4`, `2^6`, and (9,1,1,1) over 0, 1728, ∞. Indeed `f=t(t^3+1)` has four simple roots, `g=t^6+\frac32t^3+\frac38` has six simple roots, and `g^2-f^3=(8t^3+9)/64` ... The associated trivalent modular graph is unique. It has four vertices and six edges, with three monogon faces."
- Locator: [IV] L86555-86570.
- Context: marked local system of an OS45-type source.
- **[finder's note]** `I_9+3I_1` with a degree-12 j-map is Beauville's semistable rational elliptic surface of `\Gamma_1(3)\cap\Gamma_0(9)` (index 12, cusp widths 9,1,1,1; standard list).

**S6-034** · Viaclovsky and Liu–Rollenske `III^*` sources; twelve `I_1`
- Statement: "Viaclovsky 2609.33785: `III^*,I_1,I_1,I_1`; `P=(0,1)` on `y^2=x^3+tx+1` ... degree four, base genus zero, twelve `I_1`. Liu–Rollenske 2609.33826: `III^*,II,I_1`; `P=(-t^2,it^3)` ... four II and four `I_1`." "Both primitive sections have height 1/2"; "`\chi(\mathcal O)=1`, `\sigma=-8`, `h(P)=2`". Elsewhere: "`\Delta=1728\lambda^3(1+\epsilon a^4)`. It has twelve simple zeroes on `C^\circ` ... precisely the twelve `I_1` fibres."
- Locator: [IV] L14170-14190, L8926-8934.
- Context: comparison sources from the literature on complex `S^6`.

**S6-035** · the E6-source j-function and the winding −6
- Statement: "`p=t-r^2/3`, `q=t^2-rt/3+2r^3/27`. The formula `1728\,4p^3/(4p^3+27q^2)` therefore gives `j_r(t)=-\frac{256(r^2-3t)^3}{t^2F_r(t)}`." "`j=1728f^3/(f^3-g^2)`, with `Qj(Q)` tending to one. The winding is therefore −6."
- Locator: [IV] L102705-102716, L109985-109990.
- Context: the E6 source `E_r: y^2=x^3+rx^2+tx+t^2` of Theorems IV.D-G.

**S6-036** · Hesse and Legendre coordinates; `j^{1/3}=E_4/\eta^8=\theta_{E_8}/\eta^8`
- Statement: "At the LG point `y=2\zeta t_H(1+O(t_H^3))` ... `j=27t_H^3(8-t_H^3)^3/(1+t_H^3)^3`: both are `\mu_3`-eigencoordinates of the same character (cube roots of j; `j^{1/3}=E4/\eta^8=\theta_{E8}/\eta^8`, Williams Thm 8.1). ... At j = 1728, `j-1728=256t_L^2(4t_L^2-9)^2/(4t_L^2-1)^2` in CHH's Legendre coordinate." Hesse model: "`j-1728=-27(t^2+2t-2)^2(t^4-2t^3+6t^2+4t+4)^2/((t+1)^3(t^2-t+1)^3)`"; "`t=j/1728=(1+8g)^3/(64g(1-g)^3)` with `g(\rho)=-1/8`; ρ is not elliptic for `\Gamma_0(3)`".
- Locator: [CN] L105-109 (§23), L140-141, L159-161 (§24).
- Context: comparison of S6's chart at the order-three point with CHH's Landau–Ginzburg/Hesse coordinate (§38: "says only that both are cube-root coordinates").

**S6-037** · the twelfth root `y=1728^{-1/12}E_4/(\eta^2\sqrt{E_6})` on the central 12-cycle
- Statement: "B.4.19 ... after `w=r^6` ... a 12-cycle, with relative component cover `y^{12}=K`, `K=t^4/(t-1)^3`, of cusp order −1." "`K=E4^{12}/(1728E6^6\Delta)`, so `y=K^{1/12}=1728^{-1/12}j^{1/3}(j-1728)^{-1/4}=1728^{-1/12}E4/(\eta^2\sqrt{E6})`. Orbifold divisor of y: `(1/3)[j=0]-(1/4)[j=1728]-(1/12)[cusp]`. Monodromy on the 12 components: +4 around j = 0, −3 around j = 1728, −1 around the cusp (+4 − 3 − 1 = 0)." "For general twists `K=t^{4l1}(t-1)^{3l2}=E4^{12l1}E6^{6l2}/(1728\Delta)^{4l1+3l2}` ... the S^6 condition says that power is ±1, i.e. y carries `\eta^{\mp2}`." Paper I: central fibre "a cycle of twelve ruled surfaces, with component cover `y^{12}=t^{4l_1}(t-1)^{3l_2}` and rotations `4l_1,3l_2,-b` modulo 12." "K(t) = t^4/(t − 1)^3 (B.4.19) is a Belyi map whose third critical point is t = 4, with K(4) = 256/27".
- Locator: [CN] L94-104 (§23), L437-438 (§34); [I] L5656-5661 (Theorem F).
- Context: the partial filling at w = 0; η² inside S6 ("eta^2 is inside S6", [CN] L238).

**S6-038** · `\exp(2\pi i\beta)\vartheta_1^{12}/\eta^{12}=12^6`; `N^4` via `|j-1728|^{1/4}`
- Statement: "Period point `\Omega=[[\tau,\mu],[\mu,\beta/6]]`; `\exp(2\pi i\beta)\theta_1(\mu,\tau)^{12}/\eta(\tau)^{12}=12^6`: the period curve lies over the universal elliptic curve." "`N(v)^4=6\sqrt6|\eta|^6N(2v)/|E6|^{1/2}=6\sqrt6N(2v)/|j-1728|^{1/4}=3^{3/4}N(2P)/|t-1|^{1/4}`." Also `(2\sqrt3)^6=1728` ([CN] L220).
- Locator: [ROUTES] L38-39, L54-56; [CN] L219-220.
- Context: routes note of Claude Fable 5.2 at effort max (13 Nov), described there as unverified.

**S6-039** · Theta-function and 12th-power coefficient cocycles
- Statement: "`\bar\partial G=\bar\partial Q=0`, `[G]=g_\gamma`, `i_b^*[Q]=\eta`, `\exp(12[G])=f^*\mathcal O_{\mathbb P^1}(1)`. ... `Q=\tfrac1{12}\bar\partial\sum w_nc_{a,n}`." "The theta factors with their original finite affine phases and the extending cusp Cartier units define the local twelfth-power lines on the four pieces."
- Locator: [I] L5548-5563 (Theorem D), L5921-5928 (step D-5).
- Context: global Dolbeault representatives on the complex six-sphere.

---

## 2. Lattices and codes

**S6-040** · `H_2(\Delta_{0,6})=\mathbb Z^{24}`: an even rootless rank-24 lattice with an `S_6` action
- Statement: "`\Delta_{0,6}` is the boundary complex of `\bar M_{0,6}`: the trees on 6 leaves. 25 vertices (15 splits 2|4, 10 splits 3|3), 105 edges, 105 triangles. Homotopy type: a wedge of 24 copies of `S^2` (Readdy 2005, Thm 4.7)." "`H_2=\ker d_2` inside `\mathbb Z^{105}` ... even, rank 24, no roots (a 2-cycle needs at least 14 triangles; the 60 associahedron spheres have norm 14); det `=5^8\cdot11^{10}\cdot13^5`; discriminant group `(\mathbb Z/11)^2\times(\mathbb Z/55)^3\times(\mathbb Z/715)^5`." "Values on `1^6, 2, 2^2, 2^3, 3, 3.2, 3^2, 4, 4.2, 5, 6`: 24, 0, 0, −8, 0, 0, 3, 0, 0, −1, 1. Decomposition: `V(4,1,1)+V(3,3)+V(2,2,1,1)` (dimensions 10+5+9) ... The 6-cycle is a Coxeter element of `W(A_5)` (h = 6); its trace is `\mu(6)=1`. ... The 24 is also `b_3(M_{0,6})`: `(1+2t)(1+3t)(1+4t)=1+9t+26t^2+24t^3`; these are the cell counts of the return's presentation of `\Gamma_{0,6}`: 9 generators, 26 relators, 24 identities."
- Locator: [LZQ] L1-37; program `<local>/Documents\s6_workbench_repo_20261112\tools\delta06_lattice_20261113.py`.
- Context: the user's question of 13 Nov whether this `Z^24` is related to the Leech and Niemeier lattices (route: Coxeter numbers, holy constructions).

**S6-041** · the consult on `\mathbb Z^{24}`: `A_4^6` under `PGL_2(5)`, Frame shapes, Leech exclusions
- Statement: "Restricted to the stabilizer `S_5` of a leaf, `L\otimes\mathbb Q` is isomorphic to `(A_4\otimes\mathbb Q)\otimes\mathbb Q[P^1(F_5)]=A_4^6\otimes\mathbb Q`, where `S_5` acts on each `A_4` as its Weyl group and permutes the six copies as `PGL_2(5)` acts on `P^1(F_5)`. ... `A_4^6` is the root system of the Niemeier lattice with Coxeter number 5, and `PGL_2(5)` is its glue group `G_2`." "No even unimodular lattice of rank 24 (Leech or any of the 23 with roots) admits `S_6` acting by isometries with character χ." "det L = 13 times a square, so `L\otimes\mathbb Q` is not similar to the rational space of any even unimodular lattice." "Frame shape `1\cdot2\cdot6^5/3^3`, characteristic polynomial `\Phi_1^4\Phi_2^6\Phi_3^2\Phi_6^5`"; Coxeter element of `N(A_5^4D_4)`: Frame `2\cdot6^5/(1^5\cdot3)`; of `N(D_4^6)`: `2^6\cdot6^6/(1^6\cdot3^6)`; "order-3 Frame shapes of `Co_0` from memory of Kondo's table: `3^{12}/1^{12}`, `1^63^6`, `3^9/1^3`, `3^8`, traces −12, 6, −3, 0." "the 24 of L is 6 * 4 = (number of Sylow 5-subgroups of `S_5`) * rank(`A_4`)". Tests: "The glue code of `N(A_4^6)` is generated by [1 (0 1 4 4 1)] and its cyclic shifts over Z/5 ... its group is `G_1.G_2=2.PGL_2(5)`"; T3: "`Co_0` has a subgroup `S_5` whose 5-elements have Frame shape `5^5/1`".
- Locator: [LZC] L11-152 (P1-P5, T1-T5, workbench quotations §4).
- Context: answer of the S6 survey agent (Claude Fable 5.2 at effort high), by hand, flagged as to be machine-checked.

**S6-042** · the mod-840 Niemeier lattice `N(A_5^4D_4)` (index-72 glue)
- Statement: "The lattice `R_{\mathrm{ES}}` is even integral of rank 24 and has Gram matrix `G_A^{\oplus4}\oplus G_D` ... determinants 6 and 4 ... `\det R_{\mathrm{ES}}=6^4\cdot4=5184`." "`D_{R_{\mathrm{ES}}}=(\mathbb Z/6)^4\oplus\mathbb F_2^2`, `q(x_1,..,x_4;y)=\frac56\sum x_i^2+\mathbf1_{y\ne0}\pmod{2\mathbb Z}`." Glue: "`E=\{u\in F_2^4:\sum u_i=0\}`, `\tau(u)=(u_2+u_4,u_3+u_4)`, `j(a,b)=(a+b,a+2b,a,b)`, `C_3=j(F_3^2)`, `H=\{(3u+2j(a,b);\tau(u))\}`, `N=\{x\in R^\vee:x+R\in H\}`. Thus `|H|=8\cdot9=72`." "The subgroup `\mathcal H` is isotropic of order 72. Its inverse image N is a positive-definite even unimodular lattice of rank 24, with `[N:R_{\mathrm{ES}}]=72`. Among the 71 nonzero glue classes, 46 have minimum squared norm 4 and 25 have minimum squared norm 6. The roots of N are exactly those of `R_{\mathrm{ES}}`, with root system `A_5^4D_4`: 30 roots in each A5 summand and 24 in D4." Glue generators "(3,3,3,3;00), (3,3,0,0;10), (3,0,3,0;01), (2,2,2,0;00), (2,4,0,2;00)".
- Locator: [WB]`es_niemeier_shared.tex` L154-193 (`esn:thm:root-discriminant`), L264-272 (`esn:thm:niemeier`); [WB]`niemeier_umbral_shadow.tex` L8-39; [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L8-21.
- Context: the lattice of the workbench's lattice lane, built from the Erdős–Straus residue datum (S6-061).

**S6-043** · the Leech neighbour of `N(A_5^4D_4)` along its Weyl vector (holy construction)
- Statement: "`\rho_A=(5,3,1,-1,-3,-5)/2`, `\rho_D=(3,2,1,0)` ... the exact glue class of ρ is (3,3,3,3;00) ... `\rho^2=4(35/2)+14=84=2\cdot6\cdot7`." "`K=\ker\ell_\rho`, `v=\rho/6-\alpha`, `\Lambda=K+\mathbb Zv` ... `v^2=84/36-2/6+2=4`." "`N\cap\Lambda=K`, `[\Lambda:K]=6`, `\det K=36`, `\det\Lambda=1`." "`\Lambda=\{x+k\rho/6: x\in N, k\in\mathbb Z, (\rho,x)+k\equiv0\pmod6\}`." "Theorem (The Leech neighbor in the retained coordinates). The lattice `\Lambda=K+\mathbb Z(\rho/6-\alpha)` is positive definite even unimodular of rank 24 and has minimum squared norm exactly four. It is the holy-construction Leech lattice of the retained `A_5^4D_4` glue". Shifted minima table: k=1: 35/72 (A), 7/18 (D); k=2: 11/18, 4/9 (A), 2/9, 5/9 (D); k=3: 3/8, 17/24 (A), 1/2 (D). Holy presentation: "`\Lambda=\{\sum a_ff+\sum b_ag_a: \sum a_f+\sum b_a=0\}`" with 29 vectors (negative simple roots and highest roots), `g_a^2=7/3`; "exactly the holy coefficient rules of Conway–Sloane [pp. 277-280]. Borcherds gives the uniform proof".
- Locator: [WB]`es_niemeier_leech.tex` L28-101 (theorem `esnl:thm:leech-neighbor` L94-101), L113-245 (minima and rootlessness), L247-328 (holy presentation NL8-NL11); summary [KA] L198-212.
- Context: the workbench's explicit Leech lattice; the d-neighbours of N along ρ are `A_2^{12}` (d=2), `A_1^{24}` (d=3), Leech (d=6) ([S605P] L66; [LZC] L138-139).

**S6-044** · the order-twelve quotient `\Lambda/R_0\cong\mathbb Z/12\oplus(\mathbb Z/6)^2`
- Statement: "`[K:R_0]=72`, `[N:R_0]=[\Lambda:R_0]=432`, `\det R_0=6^2\cdot5184=186624`." "Theorem (The exact order-twelve quotient generator). The quotient of Λ by the original height-zero root sublattice `R_0` is `\Lambda/R_0\cong\mathbb Z/12\oplus(\mathbb Z/6)^2`. The class of `v=\rho/6-\alpha` has exact order twelve." "This particular occurrence of twelve is proved from the Coxeter denominator six and the actual order-two Weyl-vector glue class." "`K^\vee/K=\langle[\alpha],[v]\rangle\cong(\mathbb Z/6)^2`", "`q_K(a[\alpha]+b[v])=ab/3\pmod{2\mathbb Z}`".
- Locator: [WB]`es_niemeier_leech.tex` L330-405 (`esnl:thm:cyclic-twelve` L348-381).
- Context: a lattice-theoretic 12 attached to the Coxeter number 6.

**S6-045** · Lorentzian presentation: `N\perp U`, isotropic `w=(\rho,6,7)`
- Statement: "The vectors `z=(0,0,1)` and `w=(\rho,6,7)` are primitive isotropic: `w^2=84-2\cdot6\cdot7=0` ... `z^\perp/\mathbb Zz\to N`, `w^\perp/\mathbb Zw\to\Lambda`, `[(x,m,n)]\mapsto x-m\rho/6`." Transport: "`T(\Lambda_\rho)=\Lambda_{T\rho}`" for every `T\in O(N)`.
- Locator: [WB]`es_niemeier_leech.tex` L407-450 (NL17, NL18).
- Context: both lattices as quotients of the even unimodular lattice `II_{25,1}`-type space `N\perp U`.

**S6-046** · the three Leech neighbours, their common intersection J (det 81) and the `\mathbb F_3^4` correspondence
- Statement: "`\Lambda_0\cap\Lambda_1=\Lambda_1\cap\Lambda_2=\Lambda_2\cap\Lambda_0=\bigcap_j\Lambda_j=J`, `[\Lambda_j:J]=9`." "`J^\vee=\Lambda_i+\Lambda_j` (i≠j), `J^\vee/J\cong\mathbb F_3^4`", "`q_J(a,b,c,d)=\frac23(2ad+bc+bd)\pmod{2\mathbb Z}`"; Leech planes "`P_0=\{(a,b,0,0)\}`, `P_1=\{(0,0,c,d)\}`, `P_2=\{(a,b,a-b,b)\}`"; residue action `\mathcal R` with `\mathcal R^3=I`, `\mathcal R^TB\mathcal R=B`, `\mathcal RP_j=P_{j+1}`. "The fourth plane (a,b,−a+b,−b) is r-invariant."
- Locator: [WB]`es_niemeier_residue_fixed_neighbor.tex` L313-325 (`esrf:thm:common-J`), L363-415 (`esrf:thm:discriminant-correspondence`); [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L68-82.
- Context: the order-three residue element r cycles three Leech lattices.

**S6-047** · the fixed fourth extension: the Niemeier lattice `A_2^{12}` with 72 roots
- Statement: "The plane `P_\infty` is isotropic and is fixed by the induced residue action. Its inverse image M is a positive definite even unimodular lattice with exactly 72 roots, of root system `A_2^{12}` and minimum squared norm two. ... It fixes four of these `A_2` components pointwise and acts as a coordinate three-cycle on each of the other eight." "`M\cap\Lambda_j=J`, `[M:J]=[\Lambda_j:J]=9`, `M\cap N=L_0`, `[M:L_0]=[N:L_0]=6`. `R_M\cong A_2^{\perp12}`, `\det R_M=3^{12}=531441`, `[M:R_M]=3^6=729`." "This new 72 is a root count, not the earlier index."
- Locator: [WB]`es_niemeier_residue_fixed_neighbor.tex` L546-572 (`esrf:thm:fourth-extension`); [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L82-86; [KA] L207-212.
- Context: the r-fixed even unimodular overlattice of J.

**S6-048** · J: exactly eight even unimodular overlattices (six Leech, two `A_2^{12}`)
- Statement: "B.1 (Proved) ... `rJ=J`, `[\Lambda_i:J]=9`, `\det J=81` ... `Q_J(a,b,c,d)=\frac{2ad+bc+bd}{3}\pmod{\mathbb Z}`. In particular this discriminant form is split and nondegenerate." "B.2 (Proved): There are exactly eight even unimodular lattices containing J in `J\otimes\mathbb Q`" (table: `M_0`=Λ_1, `M_5`=Λ_0, `M_7`=Λ_2, three further rootless, two with root system `A_2^{12}` (`M_2`=`N_2`, `M_6`)); "Moreover `N_3` has root system `A_1^{24}`. Thus Lead 6 holds".
- Locator: [S605]`sections\B.tex` L49-149; request [S605P] L15, L66 (Lead 6), L91 (B.2).
- Context: Pro return (GPT-6 Astra, ChatGPT Pro mode) on the workbench lattice.

**S6-049** · the full automorphism group of J and a ternary code
- Statement: "B.4 (Proved): `|\operatorname{Aut}J|=12597120=2\cdot3^7\cdot2880=2^73^95`. ... `\operatorname{Aut}J\cong C_2\times((\mathbb F_3)^7\rtimes\operatorname{Aut}_{\rm mon}(D))`, where D is the ternary code generated by [5×12 matrix] ... Its order is 2880. ... Its action on the eight extensions has order 36 and has two orbits, the six Leech extensions and the two rooted extensions."
- Locator: [S605]`sections\B.tex` L293-320.
- Context: identification of J requested in B.2.

**S6-050** · isotropic planes of `\Lambda/3\Lambda` under `Co_0`: 129 orbits
- Statement: "B.5 (Proved) ... The plane `P=3J^\vee/3\Lambda\subset\Lambda/3\Lambda` is totally isotropic ... Its full stabilizer in `Co_0=\operatorname{Aut}\Lambda` has order 2099520. Its `Co_0`-orbit consists of 3960692736000 isotropic planes." "B.9 (Proved): There are exactly 129 `Co_0`-orbits of totally isotropic planes in `\Lambda/3\Lambda`. Of these, 106 have a line whose 3-neighbour is `A_2^{12}`, another 20 have a line whose 3-neighbour is `A_1^{24}`, and the remaining three have eight Leech extensions. ... The sum of the 129 orbit lengths is exactly 61549107892647466000, `\sum_{[P]}1/|Co_{0,P}|=14703561369481/1986515435520`. ... rows 1 and 12 both have four Leech and four `A_2^{12}` extensions, but their stabilizers have orders 93312 and 103680."
- Locator: [S605]`sections\B.tex` L396-413, L467-493; data `[S605]records\B_all_129_plane_orbits.json`.
- Context: classification of the configuration "three Leech lattices and `A_2^{12}` over J" inside the Leech lattice.

**S6-051** · Weyl-vector d-neighbours of all 23 rooted Niemeier lattices (Coxeter-number rule refuted)
- Statement: "B.6 (Refuted ...) The proposed rule that the Weyl d-neighbour has Coxeter number h/d, for every d|h, is false. Of the 96 pairs ... exactly the following eleven violate the rule: `D_{12}^2` 22 2 `D_6^4` (10≠11); `D_8^3` 14 2 `D_4^6` (6≠7); `E_8^3` 30 2 `D_8^3` (14≠15); `E_8^3` 30 3 `A_8^3` (9≠10); `E_8^3` 30 5 `A_4^6` (5≠6); `D_6^4` 10 2 `A_3^8` (4≠5); `E_6^4` 12 3 `A_2^{12}` (3≠4); `D_4^6` 6 2 `A_1^{24}` (2≠3); `D_{10}E_7^2` 18 2 `A_7^2D_5^2` (8≠9); `D_{16}E_8` 30 2 `D_8^3` (14≠15); `D_{24}` 46 2 `D_{12}^2` (22≠23). ... Every d=h neighbour is Leech."
- Locator: [S605]`sections\B.tex` L880-905; request [S605P] L92 (B.3).
- Context: test of the holy-construction pattern across the Niemeier list.

**S6-052** · Wilson's octonionic `E_8` and Leech lattices; fixed lattice `3G_{E_8}`, coinvariant `A_2\otimes E_8`
- Statement: "The lattice `L_W` is even and unimodular, has minimum norm 2 ... `\det G_8=1`. Its norm-two vectors are precisely the 112 vectors `\pm e_i\pm e_j` ... and the 128 vectors `\frac12(\pm e_0\pm\cdots\pm e_7)` with an odd number of minus signs." "The explicitly generated lattice `\Lambda_W` ... is an even unimodular rank-24 lattice of minimum norm 4. ... This is the actual Wilson Leech construction". "`F=\{(n,n,n)\}`, `C=\{(m_1,m_2,-m_1-m_2)\}` ... `G_F=3G_8`, `G_C=(\begin{smallmatrix}2G_8&G_8\\G_8&2G_8\end{smallmatrix})` ... the fixed lattice has minimum norm 6 and determinant `3^8`. ... identifies its displayed Gram matrix with the usual `A_2\otimes E_8` Gram matrix." Quotient `\Lambda_{\rm cyc}/(\text{fixed}\oplus\text{complement})\cong(\mathbb Z/3)^8`; "The cycle (y,z,x) is `c^{-1}`".
- Locator: [WB]`es_niemeier_wilson_cyclic.tex` L93-117 (`wcl:lem:e8`), L246-252 (`wcl:thm:Leech`), L319-341 (`wcl:thm:fixed-coinvariant`); [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L88-96; primary input R. A. Wilson, J. Algebra 322 (2009) ([KA] L296-300).
- Context: comparison of Wilson's cyclic Leech construction with the marked Niemeier/Leech embeddings.

**S6-053** · the literal common lattice `\{\sqrt2(a,a,a):a\in D_4\}` and its cubic `2\sqrt2a_0(a_0^2-3(a_1^2+a_2^2+a_3^2))`
- Statement: "`\Lambda_{\rm cyc}\cap\mathcal L(N)=\Lambda_{\rm cyc}\cap\mathcal L(\Lambda)=\mathcal I:=\{\sqrt2(a,a,a):a\in D_4\subset U\}` ... rank four, minimum norm 12, Gram matrix `6G_{D_4}`, `\det=4\cdot6^4=5184`." "`\tau(\sqrt2(a,a,a))=2\sqrt2\,a_0(a_0^2-3(a_1^2+a_2^2+a_3^2))`. The generated group is `4\sqrt2\mathbb Z`, but `12\sqrt2` is not attained. Indeed `P(a)\equiv a_0^3\pmod3`, so `3\mid P(a)` forces `3\mid a_0`; substitution then gives `9\mid P(a)`."
- Locator: [WB]`es_niemeier_wilson_cyclic.tex` L688-719 (`wcl:thm:literal-intersection`); [KA] L265-293; [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L98-123.
- Context: the exact common sublattice of Wilson's and the workbench's Leech lattices in the triality space.

**S6-054** · the complete cubic image on `D_4`: `18\mathbb Z\cup(6\mathbb Z+2)\cup(6\mathbb Z-2)`
- Statement: "The original polynomial has the exact image `P(D_4)=18\mathbb Z\cup(6\mathbb Z+2)\cup(6\mathbb Z-2)=S`. Equivalently, `P(D_4)=\{n: n\bmod18\in\{0,2,4,8,10,14,16\}\}`." Section `\sigma(18h)=(-3h,h+1,h-1,h)`, `\sigma(2(3r+\varepsilon))=(-3r-\varepsilon,r,r,r+\varepsilon)`. Local images: "`P(D_{4,2})=2\mathbb Z_2`, `P(D_{4,3})=\mathbb Z_3^\times\cup9\mathbb Z_3`, `P(D_{4,p})=\mathbb Z_p` (`p\ge5`) ... An integer belongs to every local image if and only if `n\in S`". ES bridge header: "the full cubic image `2\sqrt2(18\mathbb Z\cup(6\mathbb Z+2)\cup(6\mathbb Z-2))` of the literal common Niemeier–Leech lattice".
- Locator: [WB]`common_d4_image.tex` L123-148 (`d4i:thm:complete-image`), L247-262 (`d4i:thm:local-images`); [WB]`erdos_straus_koide_s6_bridge.tex` L13-16.
- Context: the individual values of the Albert cubic on the common lattice (local-to-global holds).

**S6-055** · Albert-cubic value groups of N, J, M, Λ; quotient `\mathbb Z/12`
- Statement: "`F(X)=P_0(X)+\sqrt2P_2(X)+\sqrt3P_3(X)` ... `\det Q_{\mathbb O}(\lambda;\mathcal LX)=\lambda^3-\lambda(X,X)+2F(X)`." "exactly 4495 specified generators of `\mathcal V_F(N)`, and ... exactly 4960 ... of `\mathcal V_F(\Lambda)`". "`\mathcal V_F(N)=\frac1{27}\mathbb Z\oplus\frac{\sqrt2}{54}\mathbb Z\oplus\frac{\sqrt3}{18}\mathbb Z`, `\mathcal V_F(\Lambda)=\frac1{27}\mathbb Z\oplus\frac{\sqrt2}{216}\mathbb Z\oplus\frac{\sqrt3}{54}\mathbb Z` ... `\mathcal V_F(\Lambda)/\mathcal V_F(N)\cong\mathbb Z/4\oplus\mathbb Z/3\cong\mathbb Z/12`." "`\mathcal V_F(J)=\mathcal V_F(M)=\frac1{27}\mathbb Z\oplus\frac{\sqrt2}{216}\mathbb Z\oplus\frac{\sqrt3}{18}\mathbb Z`"; inclusions `\operatorname{diag}(1,4,1)`, `\operatorname{diag}(1,1,3)`; "explicit quotient coordinate `a/27+b\sqrt2/216+c\sqrt3/54\mapsto9b+4c\bmod12`." Reader D1-5 / prompt: "the workbench's cubic 'value groups' depend on a chosen isometry `N\otimes\mathbb R\to\mathbb O^3` and are not invariants".
- Locator: [WB]`es_niemeier_cubic_arithmetic.tex` L114-144, L251-268, L322-345 (`nca:thm:value-modules`); [WB]`es_niemeier_JM_cubic_extension.tex` L108-120 (`jmv:thm:JM-values`); [KA] L214-242; [WBE]`WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` L50-66, L125-149; [S605P] L15.
- Context: the arithmetic of the Albert cubic transported through the Niemeier–Leech neighbours.

**S6-056** · the Wilson cubic stabilizer (order 252) and an `E_8^3` embedding with integral 2F
- Statement: "B.7 (Proved): The full stabilizer of F in `\operatorname{Aut}\mathcal W` is `C_2^2\rtimes C_3\times(C_7\rtimes C_3)\cong A_4\times(C_7\rtimes C_3)`, of order 252. Generators are the even sign changes of the three octonion coordinates, their cyclic permutation, and the simultaneous Fano permutations `i_t\mapsto i_{t+1}` and `i_t\mapsto i_{2t}`." "B.8 (Proved): The Niemeier lattice `E_8^3` ... has the explicit isometric embedding `L^3\subset\mathbb O^3`, where `L=D_8+\mathbb Zs` ... Its cubic value group ... is `\langle F(L^3)\rangle_{\mathbb Z}=\tfrac12\mathbb Z`. In particular 2F is integer valued ... rotating ... gives ... `\tfrac12\mathbb Z+\tfrac{\sqrt2}4\mathbb Z`."
- Locator: [S605]`sections\B.tex` L995-1007, L1114-1129; request [S605P] L93 (B.4).
- Context: dependence of the cubic value groups on the embedding.

**S6-057** · K3 surfaces as cyclic symplectic torus quotients: exceptional rank + Euler number = 24 in every row
- Statement: "The K3 minimal birational classes occurring as normalization components of proper two-torus degenerations are exactly the minimal resolutions of cyclic quotients of complex two-tori by nontrivial symplectic automorphisms ... After a translation of the origin, the generator is linear of order 2,3,4, or 6." Table n / quotient singularities / exceptional curves / `e(A/\langle g\rangle)`: 2 / `16A_1` / 16 / 8; 3 / `9A_2` / 18 / 6; 4 / `4A_3+6A_1` / 18 / 6; 6 / `A_5+4A_2+5A_1` / 18 / 6. "The finite quotient Euler formula gives the last column; adding the exceptional ranks gives 24 in every row." Generalized Kummer classification (Roulleau); elliptic pencil via `H'=H+\sum_{i=1}^4\frac{H\cdot C_i}{2}C_i` and Lagrange's four-square theorem.
- Locator: [II] L41722-41768 (`cdp:st:C.2.UN.32`), L42097-42130.
- Context: which surfaces occur as components of degenerations of torus fibrations (Campana–Demailly–Peternell analysis).

**S6-058** · torus / bielliptic / K3 trichotomy; K3 Euler number 24, Enriques 12
- Statement: "`L=I`: a two-torus; `\dim\ker(L-I)=1`, G acts freely: a bielliptic surface; `\ker(L-I)=0`, `\det L=1`: a K3 surface; all other cases `P_m(Z)=0`. In particular an Enriques surface is not bimeromorphic to a cyclic quotient of a complex two-torus." "K3 and Enriques surfaces have Euler numbers 24 and 12, respectively."
- Locator: [II] L40631-40657 (`cdp:st:C.2.UN.23`), L7800-7808.
- Context: components of degenerations.

**S6-059** · ADE (`A_n`, `D_n`, `E_6`, `E_7`, `E_8`) plane germs and their cubic suspensions
- Statement: "Arnold's normal forms ... give `A_1,\ldots,A_{10}`, `D_4,\ldots,D_9`, and `E_6,E_7,E_8`. The only further form with nonzero cubic jet and `\mu\le10` is `J_{2,0}=x^3+ax^2y^2+y^6`." Table type / `r_0` / weights / δ: `A_n` `x^2+y^{n+1}` (1/2,1/(n+1)); `D_n` `x^2y+y^{n-1}`; `E_6` `x^3+y^4` (1/3,1/4) 3; `E_7` `x^3+xy^3` (1/3,2/9) 4; `E_8` `x^3+y^5` (1/3,1/5) 4. `p_g(X_r)=\#\{(i,j,k):(i+1)w_x+(j+1)w_y+(k+1)/3\le1\}`; `(p_g, b_1(\text{link}))`: `A_5` (1,2), `D_4` (1,2), `E_6,E_7,E_8` (1,0).
- Locator: [II] L47535-47600.
- Context: classification of singular fibre germs of bounded delta.

**S6-060** · `E_8` inside rational elliptic surfaces of the S6 sources
- Statement: [IV]: "the infinite fibre is the literal affine `E_8` plumbing with central multiplicity six and three arms (5,4,3,2,1), (3), (4,2). ... The compact source pencil therefore has `II^*+I_1+I_1`. Its integral intersection matrix, including the last section, is unimodular of signature −8; the executed certificate supplies the integral basis consisting of the fibre, section and the eight finite `E_8` roots." [IV]: "The signature form modulo its radical is rationally represented by `(\begin{smallmatrix}2&1\\1&6\end{smallmatrix})`. In particular the `E_8` summand of the rational elliptic surface does not give an `E_8` signature for this parameter filling." [I]: "In the unimodular `E_8` summand, the primitive rank-two lattice spanned by `m-F,v` has discriminant eleven ... the nonzero Smith factors are five ones and eleven."
- Locator: [IV] L21778-21794, L11022-11031; [I] L18377-18382.
- Context: topology of fillings (signatures, Smith factors) of the six-sphere families.

**S6-061** · origin of the lattice in the user's Erdős–Straus corpus; Fricke transport
- Statement: "Residual note. The Clankers, *Residual divisor shells, support-homogeneous signs, and the `A5^4D4` Niemeier refinement of the modulo-840 Erdos–Straus datum*, April 2026 ... Foundation transport theorem. The maintained Erdős–Straus Foundation manuscript, theorem `thm:exact-support-glue-Fricke-transport`." Earlier glue `h_1=(1,3,1,1;0,0)`, `h_2=(1,4,2,3;1,1)`, `h_3=(3,0,3,0;0,1)`, `C_3^{gl}=\operatorname{span}\{(1,1,1,0),(1,2,0,1)\}`, transporter `P(x_1,x_2,x_3,x_4;y)=(x_3,x_4,x_1,x_2;y)`. Reader D1: "N is not built from X. It is built from the Erdős–Straus residue datum modulo 840 = 24·5·7 ... the kernel `S_{840}=\{1,121,169,289,361,529\}=\langle289\rangle` is exactly Mordell's set of residue classes mod 840 not covered by the classical identities. Each fibre gives an `A_5` ... a `D_4` is added by hand, with its discriminant group `F_2^2` identified with the quotient `V_{840}/S_{840}`".
- Locator: [WB]`ES_NIEMEIER_PROVENANCE.md` L5-75; [D1] L10-27.
- Context: where the Niemeier lattice of the S6 workbench comes from.

**S6-062** · fifteen selector states at p = 1201 in `\mathrm{Herm}_3(\mathbb H)`
- Statement: "The 15 marked states `s=(\chi,R,h,r,t)` at `p_0=1201` map to rank-one matrices `h(r,t)^T(r,t)` in `\mathrm{Sym}_2(\mathbb R)\subset\mathrm{Herm}_3(\mathbb H)`; their span and Jordan closure are `\mathrm{Sym}_2(\mathbb R)`, of dimension 3. `\#(E\sqcup M)=15, 54, 36, 29` for p = 1201, 4561, 8761, 9601 (all ≡ 361 mod 840). The 15 states lie on a conic, so no three are collinear, which excludes an incidence identification with PG(3,2)."
- Locator: [D1] L341-350 (D1-12); source [WB]`p1201_selector_jordan_bridge.tex` (thm:fifteen-span L194-219).
- Context: test of the coincidence 15 = dim `Herm_3(H)` (rejected).

---

## 3. Groups

**S6-063** · the integral monodromy group: a congruence condition through `\alpha:SL_2(\mathbb Z)\to\mathbb Z/12`
- Statement: "Every element of `P_{e,\mathbb Z}` has a unique expression `g(B,x,t)=(\begin{smallmatrix}1&0&0\\6x&B&0\\t&-x^{\mathsf t}J_2B&1\end{smallmatrix})`, `B\in SL_2(\mathbb Z)`, `x\in\mathbb Z^2`, `t\in\mathbb Z` ... There is a homomorphism `\alpha:SL_2(\mathbb Z)\to\mathbb Z/12` determined by `\alpha(S)=9` and `\alpha(T)=1`; in particular `\alpha(a)=4` [`a=(\begin{smallmatrix}0&1\\-1&-1\end{smallmatrix})`]. With `Q(x)=x_1+x_2+x_1x_2`, the monodromy group is `\Gamma=\{g(B,x,t):t+6Q(x)-\alpha(B)=0` in `\mathbb Z/12\}`. Consequently `[P_{e,\mathbb Z}:\Gamma]=12` and `P_{\mathbb Z}=\{\pm I\}\times P_{e,\mathbb Z}`, so `[P_{\mathbb Z}:\Gamma]=24`. Its image in the Levi quotient is exactly `SL_2(\mathbb Z)`." Fundamental set: "the classical modular region for τ, the Iwasawa angle `0\le\theta<\pi`, `0\le x_1,x_2<1` and `0\le t<12`, with the modular lifts `g(S,0,9)`, `g(T,0,1)`, `g(-I,0,6)` and the Heisenberg face identifications `(x_1,x_2,t)\mapsto(x_1+1,x_2,t-6-6x_2)`, `(x_1,x_2,t)\mapsto(x_1,x_2+1,t-6+6x_1)`." Proof: "`A_1^3=A_2^4=I` ... `K=[A_1,A_2^2]=g(I,(0,-1)^{\mathsf t},6)`", "`\alpha(T^{72})=0\pmod{12}`".
- Locator: [I] L9390-9421 (`fam:src:F.1.1`), L5413-5440 (Theorem C), L9427-9482, L9613.
- Context: answers Engel's Remark 8.4 on the monodromy of the (3,4,∞) family.

**S6-064** · maximal domain of proper discontinuity in `Sp_4(\mathbb R)/U(1,1)`
- Statement: "On `\mathcal D=\operatorname{Sp}_4(\mathbb R)/\operatorname U(1,1)` put `q_d(J)=\psi(d,Jd)`. The largest Γ-invariant open domain of proper discontinuity is `\mathcal O=\{q_d\ne0\}` ... The null locus has a dense set of points with infinite monodromy stabilizer. ... `\mathcal O_+` has `\Im\tau>0`, `D_c<0` and `q_d=-6/D_c`. ... the period map ... extends to a proper holomorphic embedding `\mathbb C=B\setminus\{\infty\}\hookrightarrow\Gamma\backslash\mathcal O_+`." Invariant class: "`\eta=6\gamma\wedge\delta+u\wedge w` has square −12; a fibre with `\mathrm{NS}=\mathbb Z\eta` has no compact curves."
- Locator: [I] L5442-5456, L5487-5488 (Theorem C).
- Context: the period domain of the family of complex six-spheres.

**S6-065** · the peripheral character `\chi:SL_2(\mathbb Z)\to\mathbb Z/12` and the mod-24 boundary
- Statement: "There is a unique isomorphism `\bar\nu:SL_2(\mathbb Z)_{\rm ab}\to\mathbb Z/12` for which the marked character `\chi=\bar\nu\circ\operatorname{ab}` sends `C_0` to −1. Its values on the three peripheral matrices are `\chi(C_1)=4`, `\chi(C_2')=-3`, `\chi(C_0)=-1 \pmod{12}`. The residues 4 and −3=9 are complementary idempotents in `\mathbb Z/12`; additively they have exact orders 3 and 4. Let `j:\mathbb Z/12\hookrightarrow\mathbb Z/24`, `j(a)=2a`. Every group homomorphism `\psi:SL_2(\mathbb Z)\to\mathbb Z/24` has image in the even subgroup and factors uniquely through j. ... `(\chi_{24}(C_1),\chi_{24}(C_2'),\chi_{24}(C_0))=(8,-6,-2)\pmod{24}` ... Its image has order 12, not 24. ... there is no group homomorphism `\tilde\chi:SL_2(\mathbb Z)\to\mathbb Z/24` with `r\circ\tilde\chi=\chi`."
- Locator: [WB]`higher_rung_24d_continuation.tex` L3577-3637 (`h24:thm:peripheral-moduli`); D1's reading [D1] L37-43 ("Both are instances of `Hom(SL_2(Z),C^\times)\cong Z/12`: any character of `SL_2(Z)` is a power of the `\eta^2` multiplier").
- Context: "What the mod-12 and mod-24 arithmetic actually is" in the workbench's higher-rung continuation.

**S6-066** · the same Z/12 in the notes: local rotations 4, −3, −1 of the twelve-cycle
- Statement: "The coefficients 4, 3 and 12 are the images in `SL_2(Z)^{ab}=Z/12` of an order-3 element (`U^2\to4`), an order-4 element (`S\to3`) and the cusp (`T^{12}\to12=0`)." "Its local monodromies are 4, −3, −1 mod 12. These are the values of the abelianization `SL2(Z)\to Z/12` on the order-3 element, on S and on the cusp." "[hunch] ... Both should be computed by the Rademacher function: Meyer's signature cocycle and the eta multiplier, the Euler-number and signature-defect faces in Atiyah 1987."
- Locator: [CN] L36-52 (§15), L351-355 (§33); [CN] L401-402 (§34: "the three rotations 4, −3, −1 ... sum 0 mod 12, as `g_1g_2g_0=1`").
- Context: Claude's reading of the S^6 sphere condition as arithmetic of `SL_2(Z)^{ab}`.
- **[finder's note]** Exact equality across entries: Paper I's α (α(S)=9, α(T)=1, α(order-3 a)=4) and the umbral file's χ (χ(T)=−1, χ(S)=3; S6-081) satisfy `\alpha\equiv-\chi` on generators, and the higher-rung χ has `\chi(C_0)=-1` for `C_0=T` (Paper V L10783). All three are the unique-up-to-unit generator of `\operatorname{Hom}(SL_2(\mathbb Z),\mathbb Z/12)`.

**S6-067** · `(3,4,\infty)` peripheral matrices; finite-order affine lifts
- Statement: "`\widetilde A_1=A_1\oplus C_1`, `\widetilde A_2=A_2\oplus C_2'`, `\widetilde M_0=M_F^{\rm man}\oplus C_0`. Then `\widetilde A_1^3=I`, `\widetilde A_2^4=I`, `\widetilde A_1\widetilde A_2\widetilde M_0=I`." "`\widetilde g_j(x,y)=(A_jx+v_j/m_j,D_jy)`, `(m_1,m_2)=(3,4)`." Paper V: `A_1=(\begin{smallmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{smallmatrix})`, `A_2=(\begin{smallmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{smallmatrix})`, `A_0=(A_1A_2)^{-1}`; Paper I: "`A_1^3=A_2^4=A_1A_2M_0=I` and `A_jv_j=v_j`".
- Locator: [WB]`higher_rung_24d_continuation.tex` L726-748 (`h24:prop:finite-lift`); [V] L10768-10784; [I] L13983, L6213.
- Context: the integral homology monodromy of the family over the (3,4,∞) orbifold.

**S6-068** · the umbral group `GL_2(\mathbb F_3)=O(N)/W(R)`; `Q_8\rtimes S_3`
- Statement: "The original marked quotient is `G=O(N)/W(R)\cong GL_2(\mathbb F_3)`" with `\ell_1=(1,1)`, `\ell_2=(1,2)`, `\ell_3=(1,0)`, `\ell_4=(0,1)`. "Every isometry of N has a unique factorization `T=wL_g` ... `O(N)=W(R_{\mathrm{ES}})\rtimes L(G)`, `W(R_{\mathrm{ES}})\cong S_6^4\times W_D`, `|O(N)|=48\cdot(6!)^4\cdot(2^3\cdot4!)`." "There is a split exact sequence `1\to Q_8\to GL_2(\mathbb F_3)\to GL_2(\mathbb F_2)\to1`" with `I_q=(\begin{smallmatrix}0&1\\2&0\end{smallmatrix})`, `J_q=(\begin{smallmatrix}1&1\\1&2\end{smallmatrix})`, splitting `A_R=(\begin{smallmatrix}1&0\\0&2\end{smallmatrix})`, `A_H=(\begin{smallmatrix}1&2\\0&2\end{smallmatrix})`, "`GL_2(\mathbb F_3)` with `Q_8\rtimes S_3`". Provenance: "Cheng–Duncan–Harvey ... Table 3, page 21 records the `A5^4D4` row with lambency 6, group `GL2(3)`, and quotient `PGL2(3)`."
- Locator: [WB]`niemeier_umbral_shadow.tex` L417-435; [WB]`es_niemeier_shared.tex` L1616-1650 (`esn:fa:thm:full-quotient`), L756-778 (`esn:thm:triality-q8`), L855-882; [WB]`ES_NIEMEIER_PROVENANCE.md` L7.
- Context: the symmetry group of the marked Niemeier lattice = the umbral group of lambency 6+3.

**S6-069** · residue action inside the Weyl group
- Statement: "`\rho(289)` is the same six-cycle in each of the four A coordinate sets and is the identity on D ... `S_{840}\xrightarrow{\rho}O(N)\to O(N)/W(R)` is the trivial homomorphism." Reader D1: "`\rho(S_{840})\subset W`, commutes with L(G), `C_6\times GL_2(F_3)` of order 288". Correction: "the transported `GL2(F3)` complement, not the entire lattice isometry group, centralizes the stated residue action".
- Locator: [WB]`niemeier_umbral_shadow.tex` L403-415; [D1] L90; [WBE]`evidence\triality_leech_20260906\README.md` L23-27.
- Context: which part of the residue symmetry survives the Weyl quotient.

**S6-070** · `W(D_4)\subset W(F_4)` with quotient `S_3` (triality); `O(D_4)=W(F_4)`
- Statement: "`R_D=\operatorname{diag}(-1,1,1,1)`, `H_D=\frac12(\begin{smallmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{smallmatrix})` are the short-root reflections ... They induce (s c) and (v s) on the three nonzero discriminant classes. There is a split exact sequence `1\to W_D\to W_F\to S_3\to1` ... `|W_D|=192` and `|W_F|=1152`." "`O(D)=W_D\rtimes\delta(GL_2(\mathbb F_2))` ... `O(D)=W_F`." "The ordinary Coxeter number of the ambient root system `F_4` is `h(F_4)=12`. The restricted root system ... is `A_2`; its Weyl group is `S_3` and its Coxeter number is 3 ... `[W(F_4):W(D_4)]=1152/192=6`."
- Locator: [WB]`es_niemeier_shared.tex` L440-474 (`esn:thm:d4-f4-triality`), L1517-1533; [WB]`higher_rung_24d_continuation.tex` L1659-1677 (`h24:prop:two-Coxeter-systems`).
- Context: the triality symmetry of the `D_4` summand.

**S6-071** · the `F_4` Coxeter element of order 12 on the `D_4` summand
- Statement: "`C=s_{\beta_1}s_{\beta_2}s_{\beta_3}s_{\beta_4}` ... `C=\frac12(\begin{smallmatrix}1&1&1&1\\-1&1&1&-1\\1&1&-1&-1\\1&-1&1&-1\end{smallmatrix})`, `C^3=(\begin{smallmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{smallmatrix})`. It satisfies `C^4-C^2+I=0`, `C^6=-I` and has exact order twelve. Its marked discriminant action is `v_D+D\mapsto c_D+D\mapsto s_D+D\mapsto v_D+D`. ... `1\to\langle C^3\rangle\cong\mathbb Z/4\to\langle C\rangle\cong\mathbb Z/12\to\langle(v_D\,c_D\,s_D)\rangle\cong\mathbb Z/3\to1`, with `\langle C^3\rangle\subset W(D_4)`." "The Coxeter denominator six in (NL1), the cyclic order twelve in (NL14), and the `F_4` Coxeter twelve in (NL20) therefore have their stated, distinct domains".
- Locator: [WB]`es_niemeier_leech.tex` L452-532 (`esnl:thm:f4-coxeter-twelve`).
- Context: three occurrences of 12 in the lattice construction, kept apart.

**S6-072** · isometries of `A_5`: `O(A)=S_6\times\{\pm I\}`
- Statement: "Every element of O(A) has exactly one expression `\epsilon Q_\sigma|_{\mathbb RA}` ... `W(A)\cong S_6`. On the marked discriminant group `D_A=(\mathbb Z/6)\lambda` ... `k\lambda+A\mapsto\epsilon k\lambda+A`. The kernel of this discriminant action is exactly W(A)."
- Locator: [WB]`es_niemeier_shared.tex` L1402-1421 (`esn:fa:thm:a5-automorphisms`).
- Context: building block of O(N).

**S6-073** · `Spin(8)`, `F_4` and the octonionic flag `F_4/Spin(8)` (24-dimensional)
- Statement: "The diagonal `F_4`-action on `\operatorname{Fl}(\mathbb O)` is transitive, the stabilizer of `x_{\mathbb O,0}` is `\operatorname{Spin}(8)`, and hence `\operatorname{Fl}(\mathbb O)\cong F_4/\operatorname{Spin}(8)`." Cohomology: "`e_1=2\beta_1-\beta_2`, `e_2=-\beta_1+2\beta_2`, `e_3=e_1+e_2=\beta_1+\beta_2`, `H^*(\operatorname{Fl}(\mathbb O);\mathbb Z)\cong\mathbb Z[\beta_1,\beta_2]/(\beta_1^2-\beta_1\beta_2+\beta_2^2,\ \beta_1\beta_2(\beta_1-\beta_2\ldots))`." "its reduced Euler class `e_N=6u_{\mathbb O}\bmod N` ... has additive order `N/\gcd(N,6)`. In particular `e_{12}` has order two and `e_{24}` has order four." "`\rho:\operatorname{Sp}(1)\to\operatorname{Spin}(8)=\operatorname{RT}(\mathbb O)`, `\rho(u)=(B_u,A_u,D_u)`, `\operatorname{Re}(((B_ux)(A_uy))(D_uz))=\operatorname{Re}((xy)z)`." Spin(8) is the stabilizer of the Albert frame: "`H_\tau` is isomorphic to the compact simply connected `\operatorname{Spin}(8)`".
- Locator: [WB]`higher_rung_24d_continuation.tex` L1406-1503, L1545-1612, L3728-3753, L5343-5360, L2309-2324.
- Context: the "24-dimensional octonionic flag" of the higher-rung continuation (Mare–Willems).

**S6-074** · `Co_0` traces (from memory) used to exclude Leech
- Statement: "(123)(456) has trace 3, but elements of order 3 in `Co_0` have traces −12, 6, −3 or 0 (ATLAS 3A-3D; confirm)." "Check: GAP, `CharacterTable("2.Co1")`, the degree-24 character on the classes of element order 3."
- Locator: [LZQ] L24; [LZC] L52-55.
- Context: route (a) closing the Leech possibility for the `S_6`-lattice `H_2(\Delta_{0,6})`.

**S6-075** · `\mathbb Z/6` centre: `(U(1)\times SU(2)\times SU(3))/\mu_6\hookrightarrow U(6)`
- Statement: "`\iota:SU(2)\times SU(3)\hookrightarrow SU(6)`, `\iota(A,B)=A\otimes B`. Its restriction to the centres is the isomorphism `\mu_2\times\mu_3\to\mu_6=Z(SU(6))` ... real dimension 3+8=11." "`\delta(\xi)=(\xi,\xi^3I_2,\xi^2I_3)` ... `\ker\hat\iota=\delta(\mu_6)` ... `\det\hat\iota(z,A,B)=z^6`, `\operatorname{im}\hat\iota\cap SU(6)=\iota(SU(2)\times SU(3))`."
- Locator: [WB]`z6_defect_center_bridge.tex` L461-477 (`zdc:thm:tensor-centres`), L535-570 (`zdc:thm:common-centre`).
- Context: the cyclic-six centre of the workbench's physics lane.

**S6-076** · quaternion order of reduced discriminant 108; `SO(F,\mathbb Z)` from the quaternion algebra of discriminant 6
- Statement: "`K^2=-I^2J^2=108`" ... reduced norm "`x_0^2-18x_1^2+6x_2^2-108x_3^2`" ... "Thus the reduced discriminant of this order is 108, not 6." "`\iota_\gamma:\mathbb Z[\sqrt3]\hookrightarrow\mathcal O`, `\sqrt3\mapsto\gamma-2`"; "The norm-one units of `\mathbb Z[\sqrt3]` are `\{\pm(2+\sqrt3)^k\}`"; hyperbolic length `2\log(2+\sqrt3)`; constant "`C_0=\frac9{2\pi^2}\log(2+\sqrt3)`". Prompt: "For `F=s^2-3t^2-18z^2` and `\Gamma=SO(F,\mathbb Z)` (cocompact, arithmetic, from the quaternion algebra of discriminant 6) ... `C_0=\lambda_0\cdot c` with `c=(9/(2\pi^2))\cdot\log^2(2+\sqrt3)`". "`\zeta_K(s)=\zeta(s)L(s,\chi_{12})`".
- Locator: [WB]`koide_quaternion_bridge.tex` L5-61, L132-135, L368, L405-465, L735; [WB]`koide_exact_parametrization.tex` L143-144; [S605P] L60-64 (Leads 1-4).
- Context: the Koide counting problem of the S6_05 prompt (part A), a Fuchsian-group count with character `\chi_{12}`.

---

## 4. Moonshine proper (umbral shadow, eta quotients, Hauptmoduln, Fricke, lattice theta series, M24, Monster numbers)

**S6-077** · Cheng–Duncan–Harvey theta functions and the ADE coefficient matrix `\Omega^X=5I_{12}+J`
- Statement: "`\theta_{m,r}(\tau,z)=\sum_{k\equiv r\ (2m)}q^{k^2/(4m)}e(kz)`" ... "`\Omega_m(n)_{r,s}=1` if `r+s\equiv0\pmod{2n}`, `r-s\equiv0\pmod{2m/n}`, 0 otherwise" ... "`\Omega^{A_{m-1}}=\Omega_m(1)`, `\Omega^{D_{m/2+1}}=\Omega_m(1)+\Omega_m(m/2)`". "the original five components have Coxeter number h=m=6, and the primary theta prescription has precisely 2h=12 indices and denominator 4h=24 in its exponents. The root rank remains `4\cdot5+4=24`; the glue index remains 72." "Put `J=\Omega_6(3)` ... the single value `s\equiv5r\pmod{12}` ... `\Omega^X=5I_{12}+J`, `J_{r,s}=\mathbf1_{s\equiv5r\ (12)}`" (12×12 matrix displayed). D1: "`\Omega^X=4\Omega_6(1)+(\Omega_6(1)+\Omega_6(3))=5I_{12}+J`".
- Locator: [WB]`niemeier_umbral_shadow.tex` L41-122; [D1] L314-315.
- Context: specialization of the umbral moonshine prescription (arXiv:1307.5793, §§3-5) to the marked `A_5^4D_4` lattice ("lambency 6" in CDH Table 3).

**S6-078** · the umbral shadow `S^X=\Omega^XS_6` and its odd part
- Statement: "The unary series and the actual shadow are `S_{6,r}(\tau)=\frac1{2\pi i}\partial_z\theta_{6,r}|_{z=0}=\sum_{k\equiv r\ (12)}kq^{k^2/24}`, `S^X=\Omega^XS_6`." "`S_{6,-r}=-S_{6,r}`, so `S_{6,0}=S_{6,6}=0`." "`\Omega^X\mathcal A=\mathcal AM^X`, `M^X=(\begin{smallmatrix}5&0&0&0&1\\0&4&0&0&0\\0&0&6&0&0\\0&0&0&4&0\\1&0&0&0&5\end{smallmatrix})`." "The diagonal entries (5,4,6,4,5) are exactly the Coxeter exponent multiplicities: four copies of (1,2,3,4,5) and one copy of (1,3,3,5)." "the modular transformation shows the same cuspidal behavior at every cusp of the full modular group."
- Locator: [WB]`niemeier_umbral_shadow.tex` L124-149, L225-229; ES bridge header [WB]`erdos_straus_koide_s6_bridge.tex` L16-18 ("maps to the Cheng–Duncan–Harvey shadow `(5I_{12}+J)S_6`").
- Context: the weight-3/2 shadow attached to the Niemeier root system of the S6 workbench lattice.

**S6-079** · the Weil representation of `\mathbb Z/12` (`L=\mathbb Z\ell`, `(\ell,\ell)=12`)
- Statement: "`A_L=L^\vee/L=\mathbb Z/12`, `q_L(r)=r^2/12\pmod{2\mathbb Z}`, `Q_L(r)=q_L(r)/2=r^2/24\pmod{\mathbb Z}`." "`(F_\pm)_{r,s}=12^{-1/2}e(\pm rs/12)`, `R_{r,s}=\mathbf1_{s\equiv-r\ (12)}` ... `F_\pm^2=R`, `F_-=RF_+=F_+R`, `F_+F_-=I`." "`\theta_6(\tau+1,z)=D\theta_6(\tau,z)`" (`D_{r,s}=e(r^2/24)\delta_{r,s}`), "`\theta_6(-1/\tau,z/\tau)=\sqrt{-i\tau}\,e(6z^2/\tau)F_-\theta_6(\tau,z)`". "`U(T)=D`, `U(S)=e(-1/8)F_-`." "`S_6(-1/\tau)=\tau\sqrt{-i\tau}F_-S_6(\tau)`, `S_6(\tau+1)=DS_6(\tau)`. ... the unary series has weight 3/2 with the same finite multiplier; theta has weight 1/2." "`\Omega^X` commutes with both finite multiplier matrices" (`5^{-1}=5` mod 12).
- Locator: [WB]`niemeier_umbral_shadow.tex` L151-229.
- Context: the modular transformation law of the shadow.

**S6-080** · quadratic similitude `\mathbb Z/12\to\mathbb Z/6` with multiplier ten
- Statement: "`p:\mathbb Z/12\to\mathbb Z/6`, `p(r)=r\bmod6` has kernel {0,6} and satisfies `q_A(p(r))=\frac56r^2=10q_L(r)\pmod{2\mathbb Z}`. Thus it is a surjective quadratic similitude with precisely multiplier ten ... `\widetilde D=(\mathbb Z/12)^4\oplus\mathbb F_2^2\to D_R` ... its radical is `\{0,6\}^4\oplus0` ... The inverse image of the original H has order `16\cdot72=1152` and is isotropic for this pullback form."
- Locator: [WB]`niemeier_umbral_shadow.tex` L231-259.
- Context: relation of the twelve theta indices to the glue coordinates.

**S6-081** · the determinant of the 12-dimensional theta representation is the `\eta^2` character; `\chi(T)=-1`, `\chi(S)=3`
- Statement: "Let `\chi:SL_2(\mathbb Z)\to\mathbb Z/12` be the retained marking `\chi(T)=-1`, `\chi(S)=3`. These values respect the presentation `S^4=I`, `(ST)^3=S^2` ... `\det F_+=12^{-6}\prod_{0\le j<k\le11}(\zeta^k-\zeta^j)` ... `\sum_{j<k}(j+k)=11\cdot66=726` ... `\det F_+=-i`, `\det F_-=i`." "The sum of the squares of all twelve indices is `\sum_{r=0}^{11}r^2=\frac{11\cdot12\cdot23}{6}=506`. Consequently `\det U(T)=e(506/24)=e(1/12)`, `\det U(S)=e(-12/8)\det F_-=-i=e(-3/12)`." "`G=\sum_{r=0}^{11}e(r^2/24)=1+4e(1/24)+2e(1/6)+2e(3/8)+2e(2/3)+e(1/2)` ... `=\sqrt{12}\,e(1/8)`." "`(F_-D)^2=e(1/8)D^{-1}F_-`, `(F_-D)^3=e(1/8)R`", "`(U(S)U(T))^3=U(S)^2=-iR`, `U(S)^4=-I_{12}`." "`\det U(\gamma)=e(-\chi(\gamma)/12)`. The dual determinant ... `e(\chi(\gamma)/12)`, with the retained signs `T\mapsto e(-1/12)`, `S\mapsto i`." "`\eta(\tau+1)=e(1/24)\eta(\tau)`, `\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)` show that `\eta^2` has weight one and multiplier `\det U` ... `\eta^2(S\tau)=(-i)\tau\eta^2(\tau)`."
- Locator: [WB]`niemeier_umbral_shadow.tex` L261-367 (`nus:subsec:determinant`).
- Context: the order-twelve character of `SL_2(\mathbb Z)` realized as a determinant of the umbral theta representation (cross-reference S6-063, S6-065, S6-066).

**S6-082** · CDH twisted shadows and the class table of `GL_2(\mathbb F_3)` for `A_5^4D_4`
- Statement: class functions "`a_g=\#\{i:p(i)=i\}`, `b_g=\sum_{p(i)=i}\varepsilon_i`, `s_g=\operatorname{sgn}(B_p|_{\{v,s,c\}})`, `c_g=\#\operatorname{Fix}(B_p|_{\{v,s,c\}})-1` ... precisely CDH's `(\bar\chi^{X_A},\chi^{X_A},\chi^{X_D},\check\chi^{X_D})`." "`(\Omega_g^{X_A})_{r,s}=(b_g\mathbf1_{r\ \text{even}}+a_g\mathbf1_{r\ \text{odd}})\delta_{r,s}`"; for the exceptional m=6 `D_4` case `c_g\delta_{r,s}` (r≡0,3 mod 6), `\delta_{r,s}+s_gJ_{r,s}` (r≡1,5), `s_g\delta_{r,s}+s_gJ_{r,s}` (r≡2,4); "`M_g^X=(\begin{smallmatrix}a_g+1&0&0&0&s_g\\0&b_g&0&0&0\\0&0&a_g+c_g&0&0\\0&0&0&b_g&0\\s_g&0&0&0&a_g+1\end{smallmatrix})`". Table [g] / a b s c / size: 1A 4 4 1 2 /1; 2A 4 −4 1 2 /1; 2B 2 0 −1 0 /12; 4A 0 0 1 2 /6; 3A 1 1 1 −1 /8; 6A 1 −1 1 −1 /8; 8A,8B 0 0 −1 0 /12 ("CDH class names of their table `tab:chars:eul:6`"; obtained from all 48 matrices over `\mathbb F_3`). "The four-component signed action and the D4 triality quotient survive and enter the displayed matrix. The central element `-I\in GL_2(\mathbb F_3)` ... changes `b_g` from four to minus four".
- Locator: [WB]`niemeier_umbral_shadow.tex` L462-541.
- Context: the twisted (umbral McKay–Thompson-type) shadows `S_g^X=\Omega_g^XS_6` of the marked glue group.

**S6-083** · frame shape `-5[1]+[2]-[3]+5[6]`, the eta quotient `T_6` and `\Gamma_0(6)`
- Statement: "The Coxeter calculation above gives the original formal frame exponent `\pi_X=-5[1]+[2]-[3]+5[6]`. Let `\mathcal E(\sum a_d[d])=\prod_d\eta(d\tau)^{a_d}`. ... `T_6(\tau)=\mathcal E(-\pi_X)=\frac{\eta(\tau)^5\eta(3\tau)}{\eta(2\tau)\eta(6\tau)^5}`." "`\mathscr L(\Omega^X)(\tau)=1+\sum_{n\ge1}\alpha_{n\bmod6}\frac{nq^n}{1-q^n}`" with "`\alpha_{n\bmod6}=5-\mathbf1_{2\mid n}+\mathbf1_{3\mid n}-5\mathbf1_{6\mid n}`"; "`f^X:=\mathscr L(\Omega^X)=-q\frac{d}{dq}\log T_6=5\lambda_6+\lambda_2-\lambda_3`", "`\lambda_d=q\frac{d}{dq}\log\frac{\eta(d\tau)}{\eta(\tau)}=\frac{d-1}{24}+\sum_{n\ge1}\sigma_1(n)(q^n-dq^{dn})`". CDH §4.2: "`\sigma^X(\tau,z)=\sum_{r\ (12)}\overline{S_r^X(\tau)}\theta_{6,r}(\tau,z)`, `\mathscr S_{1,1}(\sigma^X)=f^X`". "The original modular subgroup here is `\Gamma_0(6)`, and `[SL_2(\mathbb Z):\Gamma_0(6)]=12`" (`SL_2(\mathbb Z/6)\cong SL_2(\mathbb F_2)\times SL_2(\mathbb F_3)` of order 144).
- Locator: [WB]`niemeier_umbral_shadow.tex` L555-635; ES bridge header [WB]`erdos_straus_koide_s6_bridge.tex` L19-22.
- Context: the weight-two "shadow-to-Fricke" map from the umbral shadow to an eta quotient. Reader D1: "Classical: `T_6` is a Hauptmodul of `\Gamma_0(6)` and `T+5+72/T` one for `\Gamma_0(6)+6`" ([D1] L317).

**S6-084** · Fricke involution with the scalar 72; `J_6=T_6+5+72/T_6`, `Y_6^2=(J_6-5)^2-288`
- Statement: "Under the exact Fricke transformation `W_6\tau=-1/(6\tau)` ... `\prod_{d\mid6}(6/d)^{a_d/2}=6^{5/2}3^{-1/2}2^{1/2}=72`. Consequently `T_6(W_6\tau)=72/T_6(\tau)`." "`f^X|_2W_6=-f^X`." "the primary Eichler–Zagier operator `\mathcal W_6(6)` acts on theta by `\Omega_6(6)=R` ... On the odd shadow and on the corresponding skew-Jacobi form its eigenvalue is minus one." "`J_6=T_6+5+72/T_6`, `Y_6=T_6-72/T_6`. ... `J_6(W_6\tau)=J_6(\tau)`, `Y_6(W_6\tau)=-Y_6(\tau)`, `Y_6^2=(J_6-5)^2-288`, `dJ_6=Y_6\,dT_6/T_6=-2\pi iY_6f^X\,d\tau`." "They do not construct a new graded moonshine module or a new moonshine theorem. The name 'umbral shadow' here refers to precisely the CDH prescription". Also: "`T_6(-1/(6\tau))=72/T_6(\tau)`" in the ES bridge header.
- Locator: [WB]`niemeier_umbral_shadow.tex` L637-697; [WB]`erdos_straus_koide_s6_bridge.tex` L21-22; check `[WBE]evidence\spectral_umbral_period_20260906\check_shadow.py` (exact arithmetic in `\mathbb Q[z]/(z^8-z^4+1)`, first 240 Lambert coefficients, `72^2`).
- Context: the scalar 72 of the user's Erdős–Straus [the user's words, omitted] theorem equals the glue index (S6-086).

**S6-085** · residue Fourier map and the composite `SL_2(\mathbb Z)\to\mathbb Z/12\to\mathbb Z/6\to S_{840}`
- Statement: "`\kappa(289^j)=j\pmod6`, with the full ordered residue list `(289^j)_{j=0}^5=(1,289,361,169,121,529)\pmod{840}`." "`E_2:\mathbb C[S_{840}]\to\mathbb C[\mathbb Z/12]`, `E_2(e_{289^j})=e_{2j}`" ... "`F_-E_2=BF_6^-`." "In particular `Q_L(6)=3/2=1/2\pmod{\mathbb Z}`, so the quotient `\mathbb Z/12\to\mathbb Z/6` does not carry `Q_L` itself". "The already marked composite `SL_2(\mathbb Z)\xrightarrow{\chi}\mathbb Z/12\to\mathbb Z/6\xrightarrow{j\mapsto289^j}S_{840}` is onto, has kernel `\chi^{-1}(\{0,6\})`, and sends T to `289^5=529`. Following it by the Weyl quotient kills it ... Following χ into the dual determinant multiplier retains its complete order twelve".
- Locator: [WB]`niemeier_umbral_shadow.tex` L369-415, L543-553; D1: "That last arrow is a chosen marking" ([D1] L42-44).
- Context: the bridge from the Erdős–Straus residues mod 840 to the modular character.

**S6-086** · for every Niemeier root system, Fricke constant of the CDH eta quotient = order of the glue code
- Statement: "for a Coxeter frame shape `\pi=\sum a_d[d]` of a root system R one has `\prod d^{a_d}=\det(1-C)=\det(R)`, `a_{h/d}=-a_d` and `\sum a_d=0`, so the eta quotient `T^X=\prod\eta(d\tau)^{-a_d}` satisfies `T^X(W_h\tau)\cdot T^X(\tau)=\prod d^{a_d/2}=\sqrt{\det R_X}=[N:R_X]`. So for every Niemeier root system the Fricke constant of the CDH eta quotient equals the order of the glue code (`2^{12}` for `A_1^{24}`, `3^6` for `A_2^{12}`, 72 here, ...; table computed in `es.py`). This is a two-line proof; I expect it is implicit in CDH and known, not searched." "72 = glue index = Fricke constant of the eta quotient `T_6` = root count of `A_2^{12}`. Of these coincidences only 'glue index = Fricke constant' is a theorem".
- Locator: [D1] L318, L52-56; script `<local>/Documents\s6_workbench_repo_20261112\survey_20261112\work\scratch\D1\es.py`.
- Context: survey reader's explanation of "the original scalar seventy-two".

**S6-087** · the theta series of J is a weight-12 modular form on `\Gamma_0(3)`
- Statement: "B.3 (Proved): The minimum of J is four, its kissing number is 23058, and its theta series is a modular form of weight 12 on `\Gamma_0(3)` with trivial character. ... `\Theta_J(\tau)=\frac{7381}{66430}E_4(\tau)^3+\frac{59049}{66430}E_4(3\tau)^3-\frac{531432}{6643}\Delta(\tau)-\frac{4251528}{6643}\Delta(3\tau)+\frac{88938}{73}\eta(\tau)^{12}\eta(3\tau)^{12}`. In particular its coefficients through `q^8` are `1+23058q^2+1849032q^3+44291124q^4+514246104q^5+3824355978q^6+20831769864q^7+90541677312q^8+O(q^9)`."
- Locator: [S605]`sections\B.tex` L207-227; request [S605P] L91 (B.2: "theta series (identified as a modular form of weight 12 on the group it belongs to").
- Context: identification of the common intersection of the three Leech neighbours.
- **[finder's note]** Same level as S6-029: both J's theta series and the index-four collision cover live on `\Gamma_0(3)`; `\eta(\tau)^{12}\eta(3\tau)^{12}` here and `(\eta(\tau)/\eta(3\tau))^{12}` there are the level-3 eta products.

**S6-088** · the Leech theta series as a section on `P(3,4)`: `\Theta_{\rm Leech}/\Delta=j-720`
- Statement: "Leech has no role at w -> 0. On P(3,4) (u = `E6^{1/2}`, v = E4), `\Theta_{Leech}=(7/12)v^3+(5/12)u^4`, a section of `J*\lambda^{12}` vanishing only at t = 5/12 (j = 720; `\Theta_{Leech}/\Delta=j-720`). The 12-cycle and the twelve `A_2` planes of N(12 `A_2`) share the number 12 and nothing shown." "'`\Theta_\Lambda/\Delta` parameterizes the base': true and empty (it is j − 720; any rank-24 even unimodular L gives j − 720 + 24 h(L))."
- Locator: [CN] L124-126 (§23), L156-158 (§24); also L262.
- Context: test of whether the Leech lattice enters the w → 0 degeneration.

**S6-089** · Leech shells 1, 4600, 47104, 93150 (196560); kissing shells spanning `\mathbb Z[\omega]`, `\mathbb Z[i]`
- Statement: "The Leech inner-product counts 1, 4600, 47104, 93150 (sum 196560)." "Kissing shells: ((4,2),(2,4)) and ((4,0),(0,4)) are imprimitive: the pairs span scaled copies of `Z[\omega]` and `Z[i]` (D = −3, −4, maximal orders), not the orders of discriminant −12 and −16. The `\langle x,y\rangle=\pm1` pairs span the non-principal class `2x^2+xy+2y^2` of D = −15 (scaled)."
- Locator: [CN] L142, L165-167 (§24).
- Context: audit of an answer on Leech and Heegner points that the user pasted on 16 Nov (the heading of §24 in the notes calls it [the user's words, omitted]).

**S6-090** · `\eta(\tau)\eta(23\tau)`: the M24 cycle shape 1.23 (recalled)
- Statement: "`\eta(\tau)\eta(23\tau)` and its expansion; Gal(H/Q) = `S_3` for D = −23." "`\eta(\tau)\eta(23\tau)`: a(p) = 0 marks p inert in `Q(\sqrt{-23})` (Frobenius a transposition; p splits 1 + 2 in the cubic field); a(p) = −1 marks p inert in the cubic field (3-cycles)." "[recalled, not checked] `\eta(\tau)\eta(23\tau)` is the eta product of the M24 cycle shape 1.23 (Mason 1985; Dummit–Kisilevsky–McKay 1985): the weight-one form of §4 is the M24 class-23 form." §25(d): "`\eta(\tau)\eta(23\tau)` as the M24 cycle shape 1.23 eta product (recalled; §24)."
- Locator: [CN] L143, L168-171, L269.
- Context: the "outside" programme item (Leech, Heegner, M24) of Claude's 16 Nov notes.

**S6-091** · Heegner j-values, a quartic, and the flat-coordinate expansion at ρ
- Statement: "The nine Heegner j-values, all cubes. The quartic `m u^4+24u^3-mu+3=0`, a square at m = 12. ... Flat-coordinate expansion at ρ: `13824w^3-39744w^6+(1920024/35)w^9-(1736613/35)w^{12}`." "(τ − 1)/τ fixes ρ and rotates the Cayley disc by `\omega^2`. ... A2 in 12A2 in N(12A2), 3-neighbour to Leech (h(A2) = 3)." "Heegner points other than D = −3, −4 are ordinary smooth fibres of S6: no role found."
- Locator: [CN] L138-144 (§24), L267-268 (§25(d)).
- Context: the points of that pasted answer which the notes checked and found correct.

**S6-092** · Humbert surfaces vs Heegner divisors (Borcherds products, `O(2,3)`)
- Statement: "Wang–Williams ... `H(D,\lambda)=\{Z\in H_2: Z\in\lambda^\perp\}` ... a locus of principally polarized abelian surfaces with REAL multiplication ... Poor–Shurman–Yuen (Thm on Borcherds products): `Hum(r^2-4nm,r)` ... (Gritsenko–Hulek)." "Humbert surfaces are the special (Heegner) divisors of the O(2,3) Shimura variety `A_2`; Heegner points are the special 0-cycles of O(2,1); both have modular generating series (weight 5/2, van der Geer; weight 3/2, Zagier's class numbers)." "d = b^2 − 4ac − 4de is 0 or 1 mod 4, so `H_3, H_7, H_{15}`, ... do not exist".
- Locator: [CN] L200-214 (§25(a)).
- Context: correction of the Humbert–Heegner map claimed in that pasted answer.

**S6-093** · Salié sums (half-integral weight Kloosterman sums): Biró's Conjecture 1 refuted by Louvel's first moment (Hexagon H10)
- Statement: "`T(m,n;c)=\sum_{x\in(\mathbb Z/c)^\times}(\frac xc)e(\frac{m\bar x+nx}c)`, `\epsilon_c=1` (c≡1 mod 4), i (c≡3 mod 4). ... In Biró's conjecture take L=4, K=1, m=4, n=1, B=1, α=0, r=1. ... `T(4,\bar4;c)=T(1,1;c)`. Thus his asserted estimate would give `\sum_{c\equiv1(4)}g(c/C)T(1,1;c)/\sqrt c=O_{g,\varepsilon}(C^{1/2+\varepsilon})`." Results row: "Biro2026 Conjecture1 is false as printed: the fixed family ... has normalized first moment `(4/\pi^2)\sqrt C\int g+O(C^{1/4+\eta})`, by Louvel2012 Theorem1." Related: "the theta-corrected half-integral Kloosterman-sum Conjecture 1.4 of Sun"; "a finite quadratic Fourier transform converts the Salié sums to `S(2-18h^2,-\bar4;q)` ... `S(2-18h^2,-\bar4;q)=-S(2-18h^2,-1;2q)`". Hexagon row: "H10 | S6 | Biró's Conjecture 1 contradicts Louvel's first moment of Salié sums | ... | S6_05 A.5.7".
- Locator: [S605]`sections\A_conjecture_audit.tex` L1-60 (Statement A.5.7); [S605]`S6_05_ARITHMETIC_results.csv` row A.5.7; [S605]`sections\A.tex` L2177-2223; [HEX] L114; Louvel source `...\reviews\S6_INTAKE_CHECKPOINTS_20261115\A57_sense_check\src_louvel_1107.5282\SalieSums.tex`.
- Context: square-root cancellation input for the Koide/geodesic-arc count of S6_05 part A.

---

## 5. Triangle groups, `\mathbb Z[\omega]`, `\mathbb Z[i]`, CM

**S6-094** · the (3,4,∞) triangle group `(\mathbb Z/3)*(\mathbb Z/4)`, the family's name
- Statement: "Let `\Delta\simeq(\mathbb Z/3)*(\mathbb Z/4)` be the orientation-preserving `(3,4,\infty)`-triangle group acting on a simply connected Riemann surface `\mathfrak h_z`, with elliptic generators `g_1,g_2` and `g_0=(g_1g_2)^{-1}`." Course: "Around the finite vertices there are exactly 6 and 8 triangles, so their lifted neighbourhoods are discs; at the ideal vertex the successive strips give a cusp." [AC26] title: "The (3,4,∞) modular family of 2-tori, completed at its three special points, is a complex structure on `S^6`"; Paper I: "The `(3,4,\infty)` family of complex six-spheres I. Periods, moduli and the two ends". Routes note: "`\Delta(3,4,\infty)` is not in Takeuchi's list of arithmetic triangle groups (from memory)."
- Locator: [WB]`candidate_geometry.tex` L8-22; [CG]`global-periods-and-line-bundle-quotients.md` L45-47; [I] L5172; [S605P] L112; [ROUTES] L58.
- Context: the base orbifold of every member of the S6 family (orders 3 and 4 at j = 0 and j = 1728, cusp at ∞).

**S6-095** · triangle groups in Paper V (spherical list, Euclidean/hyperbolic cases)
- Statement: "For three points of orders at least two it is a nontrivial triangle group. ... Take a geodesic triangle with angles `\pi/m_1,\pi/m_2,\pi/m_3` in the sphere, Euclidean plane or hyperbolic plane according as their sum is greater than, equal to or less than π. In the spherical case the possible orders are, after sorting, (2,2,n), (2,3,3), (2,3,4), (2,3,5)". "`\Gamma=\langle q_1,q_2,q_3\mid q_i^{m_i}=1,\ q_1q_2q_3=1\rangle`, `\epsilon=\sum_i1/m_i-1`. ... If `\epsilon\le0`, `1\to A\to\pi_1\to\Gamma\to1`. If `\epsilon>0`, Γ is the finite spherical triangle group."
- Locator: [V] L4860-4870, L8600-8616.
- Context: fundamental groups of the fibre-product fourfolds.

**S6-096** · `\mathbb Z[\rho]` and `\mathbb Z[i]` at the two multiple fibres; the twelve-cycle ends are the Albanese Tate curves
- Statement: "Their kernels are generated by `k_1=(2/3,\rho)`, `k_2=(1/2,i)`. The residual affine generators lift to `h_1(\xi,\eta)=(\xi+\kappa_1/3,(\rho-1)\eta)`, `h_2(\xi,\eta)=(\xi-\kappa_2/4,-i\eta)`. ... the lattice indices are three and two." Notes: "B.1.2: ... first factor `E_j=C/(Z+\kappa_jZ)` of A.1.2's cover `E_j\times F_j\to S_j` (`F_1` has CM by `Z[\rho]`, `F_2` by `Z[i]`). The deck lifts `\xi\to\xi+\kappa_1/3` and `\xi\to\xi-\kappa_2/4` are the component shifts +4 and −3". "At the order-3 end, the twelve-cycle is the `I_{12}` degeneration (in r) of `E_1`, and `E_1` IS Alb(`S_1`), with Tate parameter `q1=c1r^{12}` ... At the order-4 end ... `q2^2=c2^2r^{12}`, `c2^2=-6^{-6}` ... `d_*=-1+(3i/2\pi)\log(3/4)`. So `e^{-2\pi id_*}=27/64`".
- Locator: [I] L17222-17235 (eq. `pub:I:eq:E8`; the label is not the lattice); [CN] L392-419 (§34).
- Context: the CM elliptic curves `E_\rho`, `E_i` sit in the multiple fibres over j = 0 and j = 1728.

**S6-097** · Picard twists resonant at ρ and i
- Statement: "Put `\rho=e^{\pi i/3}`, `\beta_j=\beta_c(z_j)` at the specified order-three and order-four marked root centers. Define `\ell_1(z)=1+\epsilon_n` at `z=n+k(3\beta_1+4-2\rho)`, `k\ne0`, and zero elsewhere; define `\ell_2(z)=1` at `z=n+k(2\beta_2+3-3i)`, `k\ne0`, `n\equiv1,2\pmod4`" ... "`(h^0,h^1,h^2,h^3)(T_X\otimes M_z)=(0,J_z,1+J_z,0)`." Step E-3: "The joint order-three coefficient `123ik/(64\pi)` fixes the local normal form".
- Locator: [I] L5598-5616 (Theorem E), L5946-5951.
- Context: cohomology jumps of twisted tangent sheaves at the CM points.

**S6-098** · the Eisenstein norm `x^2+xy+y^2` governs the `\Theta_7` returns
- Statement: "For `P=(v\ w)\in GL_2(\mathbb Z)`, the periodic fan T(P) has triangles `\{z,z+v,z+w\}` and `\{z+v,z+w,z+v+w\}` ... `(x,y)^t=P^{-1}e_2`, `S(P)=x^2+xy+y^2`." Returns: "`A_6(P)=-4+\frac32(S(P)-1)-\frac{27}8(S(P)^2-1)`, `A_2(P)=-\frac38(S(P)-1)(S(P)-3)`. Each has the exact image {0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26} modulo 28." "`I_a(P)=1-a-3(a-1)(S(P)-1)-\frac{2a+1}4(S(P)-1)(S(P)-3)\pmod{28}`" with images {0,6,8,10,14,20,22,24} (a=1), {5,7,9,13,19,21,23,27} (a=2). "`[\frac23(\mathscr C(P)+1)-S(P)]_{28}` ... all fourteen odd residues". "Each preserves `x^2+xy+y^2` by direct expansion"; "vectors (1,0),(0,1),(1,1) all give `x^2+xy+y^2=1\pmod2`". Course: "`0=\operatorname{tr}(\widetilde S_1^{-1}\widetilde P^{-1})=1+k(p^2-pr+r^2)` ... The positive integer `p^2-pr+r^2` must be 1 ... solutions (1,0),(0,1),(1,1)." Flag cohomology relation `\beta_1^2-\beta_1\beta_2+\beta_2^2` (S6-073).
- Locator: [IV] L5200-5206, L5415-5422, L5483-5497, L5536-5544, L47881, L47927, L48204, L68870, L69711; [CG]`global-periods-and-line-bundle-quotients.md` L108-116.
- Context: smooth monodromy (exotic 7-sphere classes) of the six-sphere families on every periodic `A_2`-type fan.

**S6-099** · finite-order torus automorphisms: Gaussian and Eisenstein rings, `\zeta_8`, `\zeta_{12}`
- Statement: "After an integral choice of character basis, a generator acts by d / `M_d`: 1 `I_2`; 2 `-I_2`; 3 `(\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix})`; 4 `(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix})`; 6 `(\begin{smallmatrix}0&-1\\1&1\end{smallmatrix})`. For orders 3,4,6, the preserved rank-two lattice is a rank-one module over `\mathbb Z[\zeta_d]`. ... The Gaussian and Eisenstein rings are Euclidean for their norms, so this ideal is principal." "`A=E_i\times E_i`, `E_i=\mathbb C/(\mathbb Z+i\mathbb Z)`. The Gaussian-integer matrices `G_8=(\begin{smallmatrix}0&i\\1&0\end{smallmatrix})`, `G_{12}=(\begin{smallmatrix}0&1\\1&i\end{smallmatrix})` ... `G_8^2=iI`, and its holomorphic eigenvalues are `\zeta_8,\zeta_8^5`. The characteristic polynomial of `G_{12}` over C is `x^2-ix-1`, with roots `(i+\sqrt3)/2=\zeta_{12}` and `(i-\sqrt3)/2=\zeta_{12}^5`. ... the integral characteristic polynomials `\Phi_8` and `\Phi_{12}` ... This accounts for all nineteen rows with finite-order automorphisms g of projective two-tori A."
- Locator: [II] L53990-54037, L42810-42845.
- Context: components of degenerations as quotients of abelian surfaces.

**S6-100** · CM by `\mathbb Q(\sqrt{-19})`: multiplication law, compact slope, Gaussian eigencoordinate
- Statement: "Let `E/\bar{\mathbb Q}` have complex multiplication by an order `\mathcal O` ... `\eta(z)=s_2z+\frac{\pi}{A}\bar z`, `\theta(z)=\sigma(z)e^{-s_2z^2/2}` ... `\theta(\alpha z)^2=F_\alpha(\exp_Ez)\theta(z)^{2d}`, `\operatorname{div}(F_\alpha)=2[\alpha]^*(O)-2d(O)`." "For `E:y^2+y=x^3-38x+90`, `P=(0,9)`, `Q=2P=(4,-2)`, one has `N(Q)=19^{1/4}N(P)^4`." "There is an endomorphism B of `\mathcal G` inducing β on E and `(t_1,t_2)\mapsto(t_2^{-1},t_1^d)` on the torus. It satisfies `B^2=[-d]` ... `\operatorname{End}(\mathcal G)\otimes\mathbb Q=\mathbb Q(\beta)`" (β = `\sqrt{-19}`). "Put `\tau_0=(1+i\sqrt{19})/2` ... `\tau=\frac{1+i/\sqrt{19}}2`, `\omega_1=(g_2(\tau)/152)^{1/4}>0`. The logarithm u is selected by `0<u<\omega_1/2`, `\wp(u)=4`, `\wp'(u)=-3`." "`\mathcal F(z,w)=\sqrt{19}\,\theta(z)\theta(w)e^{-kzw}`" (`s_2=-2`). "`A_R^{n^2}=\delta^{n^2-m^2}|\psi_m(Q)|/|\psi_n(R)|`", `\delta=19^{1/4}`. Nonzero ordinary p-adic height for this curve at p = 5. The CM order "has discriminant −19 and is maximal".
- Locator: [I] L29493-29521 (`ari:C.7.6`), L29743-29758 (`ari:C.7.8`), L29775, L29813-29852 (`ari:C.7.9`), L29988-30056 (`ari:C.7.10`), L30277-30292, L30296-30360 (`ari:C.7.11`), L30525-30584 (`ari:C.7.12`).
- Context: transcendence questions for the period norm on CM curves.

**S6-101** · transcendence of the norm: 1-motives and the open questions at j = −3375
- Statement: "N(P) is algebraic if and only if the fibre of `G_P` above P contains an algebraic point of the maximal compact subgroup ... `N(P)^4=3^{3/4}(t-1)^{-1/4}|\vartheta_1(x,i/T)/\eta(i/T)|`." "Its dimension is 5 for CM and 7 without CM." "`N(P)=|\Delta|^{1/12}|\theta(u)|\exp(-\frac{\pi|u|^2}{2A})`." Open: "`E:y^2=x^3-140x+784`, `P=(0,28)`, `j=-3375`, `N(P)=2e^{-\widehat h_O(P)}` ... `\widehat h_O(P)=0.46736568\ldots`. The unresolved assertion is transcendence of `2e^{-\widehat h_O(P)}`. For the conductor-361 example `y^2+y=x^3-38x+90`, `P=(0,9)`, ... `N(P)=e^{-\widehat h_O(P)}=\exp(-\frac{L'(E,1)}{4\Omega_E})`." Relative Semi-abelian Conjecture (Bertolin) lower bound `\operatorname{trdeg}\ge2\dim B_Q+\dim Z(1)`.
- Locator: [I] L29262-29275 (`ari:C.7.2`), L29342-29375 (`ari:C.7.3`), L29659-29740 (`I:Gaussian-comparison`), L32149-32229 (open part).
- Context: the arithmetic nature of the S6 period norm at CM points (j = −3375 is the D = −7 singular modulus).

**S6-102** · `\mathbb Q(\zeta_{12})`: `\chi_{-3}`, `\chi_{-4}`, `\chi_{12}` and the sphere condition (with corrections)
- Statement: "A candidate for what it is all suggestive of: `Q(\zeta_{12})`. `(Z/12)^\times=Gal(Q(\zeta_{12})/Q)=Aut(\mu_3)\times Aut(\mu_4)` has three quadratic characters `\chi_{-3}`, `\chi_{-4}`, `\chi_{12}=\chi_{-3}\chi_{-4}`, cutting out `Q(\sqrt{-3})`, `Q(i)`, `Q(\sqrt3)`. The imaginary quadratic fields with units beyond ±1 are exactly the imaginary quadratic subfields of `Q(\zeta_{12})`; their CM points are the two orbifold points of the j-line and of S6's base. `12=lcm(6,4)=|\mu(Q(\zeta_{12}))|=|Pic(M_{1,1})|`." "`\eta=\sum\chi_{12}(n)q^{n^2/24}`: eta's character is that of `Q(\sqrt3)`." Correction §38: "The sphere condition is |p| = 1 as an integer. `\chi_{12}(p)=1` is necessary and not sufficient: p = 11 and p = 13 give Z/11 and Z/13. ... 'the sign at 3 is `\chi_{-3}`' is an analogy only." "t = −1 ± √3 at j = 1728 ... generates the ramified prime over 2, `(1+\sqrt3)^2=2(2+\sqrt3)`."
- Locator: [CN] L159-160, L172-194 (§24), L458-463 (§38); also [CN] L257-260 (Q(ζ_12) ramified vs inert primes; `Q(E3[4])=Q(i,(3/4)^{1/4})`).
- Context: Claude's arithmetic reading of the level 12 in S6 and in the Longue Marche Δ problem.

**S6-103** · the corner (j = 0, w = 0): Fermat cubic (Landau–Ginzburg point) × cusp, modulo `\mu_3`
- Statement: "over j = 0 the reduced fibre is `(E_\rho\times A1)/\mu_3`: the Fermat cubic curve (CHH's Landau–Ginzburg point, `Z[\zeta_3]`) times a curve A1 whose nome is `-w^2/48^3`. w -> 0 sends A1 to its cusp and leaves `E_\rho` fixed: the corner (j = 0, w = 0) is 'LG point x cusp, modulo `\mu_3`'. ... the base disc at j = 0 is the Cayley disc `s=(\tau-\rho)/(\tau-\bar\rho)` of CHH's expansion (`j\sim s^3`, `\mu_3` = rotation)". Correction §38: "The cover of `S_1` has group `C_3\times C_3` (degree 9), not `\mu_3`."
- Locator: [CN] L88-93 (§23), L455-458 (§38).
- Context: answer to the user's question [the user's words, omitted].

---

## 6. Numerology: 12, 24, 28, 72, 216, 840

**S6-104** · twelve throughout the twists, fillings and line bundles
- Statement: Theorem B: "`p=12l_0-4r_1-3r_2` ... complete invariants `(|p|,e^{-\pi i(c+k_2)})`, `|p|\ge1`, `\gcd(|p|,6)=1`." Theorem E: "`d(n)=\frac{n-4r_1(n)-3r_2(n)}{12}`". Theorem F: "After `w=r^6` ... the central fibre is a cycle of twelve ruled surfaces ... rotations `4l_1,3l_2,-b` modulo 12. On `q=Q^{12m}` and `r=R^n` ... deck differences `am\gamma-6am^2\delta`, `an\gamma-6an(n-1)\delta`"; "`N=12kl`" for `(3k,4l)`; step F-5: "Admissibility gives `\gcd(a,12)=1`"; step F-6: "`K_X^{-N}=f^*\mathcal O(4l+3k-kl)`". Paper V: "`L^3\cong\mathcal O_X(S_2)`, `L^4\cong\mathcal O_X(S_1)`, `L^6\cong\mathcal O_X(2S_2)`, `L^{12}\cong\mathcal O_X(W)`." "A nonzero r-component shift therefore forces a nonreduced q-fibre. In particular a shift −1 mod 12 in this class of constructions forces multiplicity at least twelve." Paper II: "`0\le r_2(n)<4`, `r_2(n)\equiv3n\pmod4`, `d(n)=\frac{n-4r_1(n)-3r_2(n)}{12}`".
- Locator: [I] L5339-5357, L5577-5597, L5648-5684, L6004-6014; [V] L10790-10797; [I] L19562-19582 (`push:src:B.3.3`); [II] L5388-5410 (`series:II:E`).
- Context: the integer 12 = lcm(3,4) of the (3,4,∞) orbifold in all discrete data of the six-sphere family.

**S6-105** · the sphere condition as a Seifert Euler number `e=\pm1/12`
- Statement: "Why no Tate-style filling: the vanishing circles over the base form the Seifert fibration of `S^3` over `S^2(3,4)`, with Euler number `p=12l_0-4l_1-3l_2=\pm1`, which is exactly the `S^6` condition." "[mine] p = 12 e, where `e=l_0-l_1/3-l_2/4` is the rational Euler number of a Seifert fibration with exceptional fibres of orders 3 (the `IV^*` fibre, j = 0) and 4 (the III fibre, j = 1728). p = ±1 means e = ±1/12: the (3,4)-torus-knot fibration of `S^3`." "p ≡ −`l_1` (mod 3) and p ≡ `l_2` (mod 4). So p = ±1 fixes the pair of local residues ... to (1, 1) or (2, 3), i.e. the units 1 or 11 of Z/12; with the other orientation of `l_1`, the units 5 or 7." "If `l1` is a unit mod 3 and `l2` a unit mod 4 ..., then p = 12 l0 − 4 l1 − 3 l2 is prime to 12".
- Locator: [CN] L32-43 (§15), L122-123 (§23).
- Context: why the corner (cusp, w = 0) cannot be filled (corrected in §38: the obstruction is the γ-winding of F, not |p| = 1).

**S6-106** · `\pi_6(S^3)=\mathbb Z/12`, the Lie-framed three-torus, e-invariant 1/2; `\pi_{12}(S^9)=\mathbb Z/24`
- Statement: "Agreement only on the exterior permits all twelve elements of `\pi_6(S^3)`, because the relative pinch of an interior six-ball adds any chosen element." "The marked quotient has `[e]=6\nu'=\eta_3\eta_4\eta_5`, the element of order two in `\pi_6(S^3)=\mathbb Z/12`. A regular inverse image is a three-torus; the monodromy calculation identifies its normal framing with its Lie framing, whose real e-invariant is 1/2. The holomorphic algebraic reduction `f:X\to\mathbb P^1` is null-homotopic. Its explicit factorization through the circle quotient contains the normalized power map of degree `3\cdot4=12` on `S^3`, which kills `\pi_6(S^3)`." Workbench: "`[g]=0\in\pi_6(S^3)\cong\mathbb Z/12`, `a=0\pmod{12}`, `[E^6g]=0\in\pi_{12}(S^9)\cong\mathbb Z/24`."
- Locator: [III] L5178-5215 (Theorems III.A, III.B); [III] L27864; [WB]`higher_rung_24d_continuation.tex` L4347-4357.
- Context: homotopy classes of the maps `X\to S^3` and `X\to\mathbb P^1` from the complex six-sphere.

**S6-107** · `\Theta_7=\mathbb Z/28` and the denominator 24 (Eells–Kuiper)
- Statement: "We identify `\Theta_7` with `\mathbb Z/28` by `[\Sigma]\mapsto28\mu(\Sigma)`". "`[\Phi]=A_M:=\frac{4k_M-\ell_M}{24}\pmod{28}`, `\mu(\Sigma_\Phi)=A_M/28`", "`(k,\ell)(a)=(1,4)` and `(k,\ell)(b)=(8,8)` give `\mu(\lambda(a))=0` and `\mu(\lambda(b))=1/28`", "`(k_M,\ell_M)=(3H,24\chi)`, `A_M=H/2-\chi`". Eells–Kuiper: "`\mu(M)=\frac{p_1(V)^2-4\sigma(V)}{896}\pmod{\mathbb Z}`"; "`\mu(M)=\frac{3\ell^2/k-8\ell-4k-12\operatorname{sign}(k)}{2688}`. Moreover `\ell=4k+24r` ... `\mu(M)=\frac{k-\operatorname{sign}(k)+32r+144r^2/k}{224}`"; "`\mu(-\lambda(f_0))=\frac{p_1^2-4\sigma(W)}{896}-\frac{z^2p_1}{192}+\frac{z^4}{384}=\frac{6p}{896}-\frac p{192}=\frac p{672}`. ... substitute `p=-24A(f)`: `\mu(\lambda(f))=A(f)/28`" (Milnor sphere `S_{2,-1}(\mathbb H)` has invariant +1/28). "the spin congruence `\ell\equiv4k\pmod{24}`". "`\mu_6(a)=6a` on `\mathbb Z/28`. Its kernel is {0,14} ... `\mu_6^{-1}(2r)=\{5r,5r+14\}`". Theorem G: "`A_j=8-\frac{j(j^2-9j+26)}3` ... twenty-eight actual witness words ... realize every element of `\Theta_7`".
- Locator: [IV] L5190-5258 (Theorem IV.A), L10536-10545, L11751-11762, L14795-14822, L12685-12692, L9993-10010 (`maps:src:B.6.1`), L5556-5598 (Theorem IV.G).
- Context: smooth monodromy of the six-sphere families in the group of exotic 7-spheres.

**S6-108** · Mordell–Weil heights `1/d`, physical pair `(3d,24)`
- Statement: "Take a marked primitive generator G on any of the following rational elliptic source profiles, with `d=1/h(G)`: 8: `I_8+4I_1`, `I_8+II+2I_1`; 14: `I_7+I_2+3I_1`, ...; 20: `I_5+I_4+3I_1`, ...; 30: `I_5+I_3+I_2+2I_1`, ... Their primitive positive scalar loops have physical pair (3d,24) and integer d/2−1, namely 3,6,9,14." "Its stated OS45 family has primitive class 3, invariant 3/28, and positive finite pullbacks realizing all twenty-eight classes. The weighted OS47 construction ... has class 4." "the four primitive groups give 21,14,7,14". Heights in S6-030 (1/6), S6-029 (1/12, 1/30), S6-032 (table).
- Locator: [IV] L5266-5310 (Theorem IV.B).
- Context: catalogue of rational elliptic sources and their exotic-sphere classes.

**S6-109** · `|G_2|=48`, `|G_3|=216`, `|G_4|=3072`
- Statement: "Exact enumeration gives `|G_2|=48`, `|G_3|=216`, `|G_4|=3072`; the accompanying program checks these finite examples, while the construction proves the statement for arbitrary N." `G_N=\langle(A_1,-1),(A_2,0)\rangle`.
- Locator: [III] L7422-7430, L7349.
- Context: degrees of local Kummer covers of the cusp.

**S6-110** · the Erdős–Straus residues mod 840: `V_{840}` (24 classes), `S_{840}=\langle289\rangle`
- Statement: "`V_{840}=\{r\in(\mathbb Z/840)^\times: r\equiv1\pmod{24}\}`, `\beta(r)=(\frac{1-(r/5)}2,\frac{1-(r/7)}2)\in\mathbb F_2^2`, `S_{840}=\ker\beta`." "The map β is an onto group homomorphism, each `F_\eta` has six elements, and `S_{840}=\{1,121,169,289,361,529\}=\langle289\rangle`, `(289^j)_{j=0}^5=(1,289,361,169,121,529)\pmod{840}`. ... `\kappa:S_{840}\to\mathbb Z/6`, `r=289^{\kappa(r)}`". "`289\equiv1\pmod{24}`, `289\equiv4\pmod5`, and `289\equiv2\pmod7`". Integral count map: "`Q_{R,P}=6W_{R,P}-M_{R,P}u\in A(S_{840})\subset N`", "`\rho(289)f_k=\zeta_6^{-k}f_k`".
- Locator: [WB]`es_niemeier_shared.tex` L45-106 (`esn:thm:cyclic-fibre`), L1298-1328 (`esn:thm:sample-fourier`).
- Context: the 24 free coordinates of the Niemeier lattice N are the 24 residues `\equiv1\bmod24` mod 840 (four fibres of six).

**S6-111** · the Erdős–Straus / S6 terminal-lattice bridge: `\lambda=12\ell_0-4\ell_1-3\ell_2` and the (3,4) central extension
- Statement: "Fix throughout a prime `p\equiv1\pmod{12}`, `h=\frac{p-1}{12}` ... `R_j=4j+3`, `a_j=3h+j+1=\frac{p+R_j}4` ... `\mathscr S(p)=\{(x,y,z): 4xyz=p(xy+xz+yz)\}`." "`\lambda(\ell_0,\ell_1,\ell_2)=12\ell_0-4\ell_1-3\ell_2`", "`G(\ell_0,\ell_1,\ell_2)=\langle c,x,y\mid c` central, `xy=c^{\ell_0}`, `x^3=c^{\ell_1}`, `y^4=c^{\ell_2}\rangle`", "`\mathsf R=(\begin{smallmatrix}3&-\ell_1\\4&\ell_2-4\ell_0\end{smallmatrix})`, `\det\mathsf R=-\lambda`". "Theorem (strong marked bridge theorem). ... `\Theta_{\varepsilon,p}:(j,u)\mapsto(j,\frac{T+1}4,u-jT)` is a bijection ... `\mathsf U_j\mathsf A_\varepsilon(p;j,u)=\mathsf R(\ell_0,\ell_1,1)` ... `\operatorname{Rel}(\mathsf A_\varepsilon)=\operatorname{Rel}(\mathsf R)`" ("they differ by a displayed element of `SL_2(\mathbb Z)`"). Scope: "not a geometric morphism from the reciprocal cubic to the complex threefold". D1: "the presentation that gives `\pi_1(X)=Z/|12l_0-4l_1-3l_2|` in [AC26]".
- Locator: [WB]`erdos_straus_koide_s6_bridge.tex` L25-122, L360-420 (`thm:esksb-bridge`), L987-1023; [WB]`erdos_straus_selector_crosswalk.tex` L191-212 (`thm:es-s6-selector-terminal-bijection`); [D1] L28-37.
- Context: the exact Erdős–Straus appearance in S6 — the same linear form `12\ell_0-4\ell_1-3\ell_2` as Paper I's `p=12l_0-4r_1-3r_2` (S6-104).

**S6-112** · the affine gate: an Erdős–Straus witness exactly when `p\equiv13\pmod{24}`; `A_3(2521)=0`, `A_3(3361)=6`
- Statement: "For prime `p=12m-11`, `m\ge2`, and `0\le j<3m-3`, `u_j\mid a_j^2\iff(j=0` and `2\mid m)` or `(j=2` and `8\mid m)`. Consequently the single unmarked point (6.2), with all markers restored, produces an Erdős–Straus witness if and only if `p\equiv13\pmod{24}`. In that case j=0, u=2, K=m gives `\frac4p=\frac1{3m-2}+\frac1{pm}+\frac1{pm(3m-2)/2}`. For `p\equiv1\pmod{24}`, this affine S6 point supplies no supported selector state". "`A_3(2521)=0` and `A_3(3361)=6` although both primes are 1 modulo 840". D1: "2521 has 12 selector states on other shells (my census: 6 E, 6 M, 9 unordered solutions)".
- Locator: [WB]`erdos_straus_koide_s6_bridge.tex` L775-834 (`thm:esksb-affine-gate`), L1025-1031; [D1] L333-338.
- Context: what the S6 presentation does and does not give for Erdős–Straus (the open half is `p\equiv1\pmod{24}`).

**S6-113** · the coincidences of small integers, as listed by the survey reader
- Statement: "3, 4 (orders of the two special fibres; entries of R(l)); 6 = `|S_{840}|` = Coxeter number of `A_5` and `D_4`; 12 = lcm(3,4) = `|SL_2(Z)^{ab}|` = 2h = number of theta indices = Coxeter number of `F_4`; 24 = rank = `|V_{840}|` = dim `O^3`; 72 = glue index = Fricke constant of the eta quotient `T_6` = root count of `A_2^{12}`." Higher-rung: "No arrow between these four lines is defined merely by equality of their integers" (as quoted by D1). Notes: "Numerology (no mechanism known): S6's `q1/q2^2=(3/4)^3` against R6's `(3/4)^{1/4}`; `\Omega^2=-12`; the 12-cycle and the twelve A2 planes; `\Theta_{Leech}` vanishing at t = 5/12".
- Locator: [D1] L52-56, L49-50; [WB]`higher_rung_24d_continuation.tex` L6139-6168 (`h24:thm:exact-numerical-boundary`); [CN] L261-264.
- Context: the sources' own inventory of shared numbers.

---

## 7. The user's own vocabulary (ghosts, octonions, triality, Albert, the Leech/Albert object, hexagons)

**S6-114** · ghosts in log geometry: the injective q-ghost map `\operatorname{diag}(12m,12m)`
- Statement: "## 2. A precise ghost-valuation lemma. On the underlying analytic site, KKN's definition gives the exact sequence `0\to Y\to T_{\log}^{(Y)}\to A\to0` ... evaluation of the characteristic monoid gives a homomorphism `\operatorname{ord}_Q:T_{\log}^{(Y)}\to i_*\mathbb Z^2`. The composite with Y is `u\mapsto(12,0)`, `\gamma\mapsto(0,12)`. In particular it is injective. ... Applying `\operatorname{ord}_Q` makes this cocycle a coboundary, the difference of the local integral ghost vectors. ... the induced map to `H^1(D_Q,\mathbb Z^2)` is multiplication by diag(12,12). ... The same calculation survives `q=Q^{12m}`, `r=R^n` with positive m,n. The r-loop class becomes nγ, while the Q-ghost map on Y is diag(12m,12m), still injective. Thus finite Kummer covers do not trivialize this particular torsor obstruction."
- Locator: [PUSH] L6580-6600; Paper I proposition "Obstruction in the fixed log-torus category" [I] L24270 (`push:src:B.4.24`) with "The ghost-valuation obstruction" L24415-24499 and L24798-24827; [CN] L13 ("the 'injective q-ghost map' of B.4.24").
- Context: the obstruction to filling the family at the corner survives every finite cover (cf. the user's concept: an object passing every finite-level test).

**S6-115** · H-ghosts in the Adams tower (course CG-S6)
- Statement: "Call a map with this vanishing property an H-ghost. The definition quantifies over every V, every j and every target map ... **Extension lemma.** If a target E has such a construction of length at most r, then any composite of r H-ghosts followed by any map to E is zero." "Each `t_s` is an H-ghost by (3.4)–(3.5)."
- Locator: [CG]`the-original-adams-tower-and-arithmetic-completion.md` L217-221, L267.
- Context: arithmetic completion of the stable homotopy computations for `S^6`.

**S6-116** · "ghosts turn spheres into lens spaces" (hunch, answered negatively); ghost classes 5, 7
- Statement: "If the central frame class acts on Λ/12 by the scalar a, a ghost (Δ = 1) carries the sphere's local twists (p = ±1 mod 12) to a lens class (±5): 'ghosts turn spheres into lens spaces' profinitely. Caveat: GT0 acts on the completed modular group `Z/2 * Z/3`, while S6's base group is `Z/3 * Z/4` (P(3,4) is the cover by `E6^{1/2}`)". "The ghost classes 5, 7: each local type is a CM type, but they differ by an automorphism moving √3." Later in §25: "every element of GT0 acts on S6's class p (mod 12, and the Euler class) by multiplication by lambda, whatever Delta is. 'Ghosts turn spheres into lens spaces' is false; F14 is answered in the negative."
- Locator: [CN] L249-256 (§25(c)), L181-182 (§24), L296-302 (end of §25).
- Context: bridge attempt between S6's Seifert class and the Longue Marche Δ on `\widehat{GT}`.

**S6-117** · the octonionic almost complex structure on `S^6`
- Statement: "# Almost complex structures, octonions, and integrability ... The standard octonion construction gives an endomorphism of the tangent bundle of the round six-sphere. To compare these objects, we need the exact map ..." (comparison with Baez, *The Octonions*, §2.2); "a real two-plane generated by independent U,V has zero octonionic associator with p exactly when it is the complex line generated by U"; Nijenhuis tensor vs associator. Survey: "'`J_X` is homotopic to the octonionic almost complex structure' (G2-8): immediate from `\pi_6(CP^3)=0`."
- Locator: [CG]`almost-complex-structures-and-integrability.md` L1-5, L106-194, L342, L402, L495; `<local>/Documents\s6_workbench_repo_20261112\survey_20261112\FINDINGS.md` L379.
- Context: comparison of the AC26 complex structure with the `G_2`/octonion almost complex structure.

**S6-118** · the Leech/Albert object: `N\otimes\mathbb R\cong\mathbb O^3`, cyclic triality, Albert determinant `\lambda^3-\lambda(X,X)+2F(X)`
- Statement: "Choose an ordered orthonormal octonion basis `(u_0,\ldots,u_7)` ... `\mathcal L:V_N\to\mathbb O^3`, `q_{j+1}=\sum_{i=1}^4\sum_{p=0}^1(t_{i,p,j}+\frac{b_{2(i-1)+p}}{\sqrt3})u_{2(i-1)+p}`." "Theorem (Actual rank-24 map, inverse, pairing, and residue action). The map `\mathcal L` is a real linear isometry onto `\mathbb O^3` ... If `r=\rho(289^2)=\rho(361)` ... and `c(q_1,q_2,q_3)=(q_3,q_1,q_2)`, then `\mathcal Lr=c\mathcal L`, `r^3=c^3=I`, `rN=N`." "`Q_{\mathbb O}(\lambda;q)=(\begin{smallmatrix}\lambda&q_3&\bar q_2\\\bar q_3&\lambda&q_1\\q_2&\bar q_1&\lambda\end{smallmatrix})\in\mathfrak h_3(\mathbb O)`" ... "`\det_{\mathbb O}(\lambda I+E(\mathcal LX))=\lambda^3-\lambda(X,X)+2\mathfrak t_N(X)`", "`\operatorname{tr}(E(\mathcal LX)\circ E(\mathcal LY))=2(X,Y)`", `\mathfrak t(q)=\operatorname{Re}((q_1q_2)q_3)`. Leech in the same coordinates: "`\varrho=\mathcal L\rho=(V+2U,V,V-2U)` ... `|\varrho|^2=84`, `|\delta|^2=2`, `\langle\varrho,\delta\rangle=1` ... `\Lambda_{\mathrm{Leech},\mathbb O}=K_{\mathbb O}+\mathbb Z(\varrho/6-\delta)`." D-summand: "`d\mapsto\frac1{\sqrt3}(z(d),z(d),z(d))` ... its 24 shortest nonzero dual vectors become 24 specified points". "The proved cyclic subgroup `\langle c\rangle` does preserve both the lattice and its Albert cubic."
- Locator: [WB]`es_niemeier_triality_bridge.tex` L5-321 (`n24:thm:full-isometry` L50-80, Albert L155-222, Leech L243-321); [WB]`es_niemeier_shared.tex` L14-18; [KA] L214-258.
- Context: the workbench's "24-dimensional / triality / mod 12" pattern made into explicit maps.

**S6-119** · which glue isometries preserve N; triality frame versus Albert frame (traces)
- Statement: "the necessary and sufficient condition for T(N)=N is `B\tau(u)=\tau(P_pu)`, `(\varepsilon_i\ell_{p(i)})=(\ell_iA)` for some `A\in GL_2(\mathbb F_3)`" ... "`O(N)=(S_6^4\times W(D_4))\rtimes L(G)`, `G\cong GL_2(\mathbb F_3)`" ... "`O(\Lambda_{\mathbb O})=\mathcal LO(N)\mathcal L^{-1}`". "On `V_N`, each of `\widehat R,\widehat H` has trace 5−5+2=2 ... Their three-cycle has trace 5+1=6. A geometric Albert-frame transposition ... trace is 1−7=−6. Its three-cycle has trace zero. ... `V_N|\cong7\mathbf1\oplus5\operatorname{sgn}\oplus6\operatorname{Std}`, `\mathbb O^3|_{S_3^{\rm frame}}\cong\mathbf1\oplus7\operatorname{sgn}\oplus8\operatorname{Std}`." "the connected group `\operatorname{Spin}(8)` acts on the ambient triality module, and its subgroup preserving `\Lambda_{\mathbb O}` ... is finite".
- Locator: [WB]`es_niemeier_triality_bridge.tex` L323-426.
- Context: limits of the triality identification.

**S6-120** · Peirce table and the Jordan determinant of the Albert algebra
- Statement: "`e_i\circ e_j=\delta_{ij}e_i`, `e_i\circ E_i(a)=0`, `e_j\circ E_i(a)=e_k\circ E_i(a)=\tfrac12E_i(a)`, `E_i(a)\circ E_i(b)=h(a,b)(e_j+e_k)`, `E_i(a)\circ E_j(b)=\tfrac12E_k(\overline{ab})`." "`d(X)=\xi_1\xi_2\xi_3-\sum_i\xi_iN(q_i)+2\operatorname{Re}((q_1q_2)q_3)`." "the octonionic flag ... `\mathbb{OP}^2=\{a\in\mathfrak h_3(\mathbb O):a^2=a,\operatorname{tr}a=1\}`, `\operatorname{Fl}(\mathbb O)=\{(a,b):\operatorname{Re}\operatorname{tr}(ab)=0\}`".
- Locator: [WB]`higher_rung_24d_continuation.tex` L2080-2092, L2192-2206, L1406-1432.
- Context: the exceptional Jordan algebra behind the 24-dimensional constructions.

**S6-121** · three 24-dimensional constructions: `F_4/\mathrm{Spin}(8)`, `X^{\wedge4}\cong S^{24}`, the determinant sphere `S^{24}`
- Statement: "The relative boundary of `\mathcal C(\mathbb O)` ... `(\mathcal C(\mathbb O)^+,(\partial\mathcal C(\mathbb O))^+)\cong(B^{25},S^{24})`. In particular `S^{24}_{\det,\mathbb O}:=(\partial\mathcal C(\mathbb O))^+\cong S^{24}` is an exact determinant-boundary sphere." "`\mathcal B:\mathbb O^3\to\partial\mathcal C(\mathbb O)`, `q\mapsto Q_{\mathbb O}(a(q);q)` is a proper homeomorphism ... It extends to a based homeomorphism `\mathcal B^+:(\mathbb O^3)^+\to S^{24}_{\det,\mathbb O}`." "(i) The octonionic flag is the homogeneous 24-manifold `F_4/\operatorname{Spin}(8)`, with `H^8\cong H^{16}\cong\mathbb Z^2` and χ = 6. (ii) After a based diffeomorphism `X\cong S^6`, the fourth smash power `X^{\wedge4}` is a based sphere `S^{24}_\wedge`". "The six Kuhn zero-strata and the six octonionic fixed flags have the marked `S_3`-equivariant finite-set bijection".
- Locator: [WB]`higher_rung_24d_continuation.tex` L1884-1905, L2739-2772, L3511-3540, L1740-1757, L6139-6168.
- Context: the higher-rung continuation of the S6 work (a 24-dimensional successor).

**S6-122** · the division-algebra boundary ladder `S^3, S^6, S^{12}, S^{24}`; the forced 4+4+4+1 cubic
- Statement: "On `\mathcal T_{13}`, the determinant is `\mathcal N_{13}(\lambda;q_1,q_2,q_3)=\lambda^3-\lambda(|q_1|^2+|q_2|^2+|q_3|^2)+2\Re(q_1q_2q_3)`. It is invariant under the cyclic permutation ... and under the vertex gauge action". "Theorem (Division-algebra boundary ladder). The real dimension of `\mathcal T(\mathbb A)` is 1+3d. ... `\mathcal C(\mathbb A)^+\cong B^{1+3d}`, `(\partial\mathcal C(\mathbb A))^+\cong S^{3d}`" — table R / 1 / 4 / `S^3`; C / 2 / 7 / `S^6`; H / 4 / 13 / `S^{12}`; O / 8 / 25 / `S^{24}`. "The complex rung supplies a canonical `S^6` as the compactified determinant boundary of a seven-dimensional real cone. The quaternionic and octonionic rungs explain the previously recurring dimensions `S^{12}` and `S^{24}`."
- Locator: [TRI] L118-135 (`thm:triality-cubic`), L200-246 (`thm:sphere-ladder`).
- Context: the workbench's triality dynamic completion (4 Sep 2026): `S^6` and `S^{24}` on one ladder.

**S6-123** · hexagons: the `dP_6` cusp fibre, the hexagonal toric surface, the `A_2` honeycomb
- Statement: [II]: "For every admissible member of the original (3,4) family, every member of the two-parameter family of [Viaclovsky] ... and every member of the Liu–Rollenske family ... there is a reduced full hexagonal fibre W with normalization `\eta:\mathrm dP_6\to W` such that `\eta^*L=\mathcal O_{\mathrm dP_6}` (`L\in\operatorname{Pic}(Y)`), `H^2(\mathrm dP_6,K_{\mathrm dP_6}\otimes\eta^*(K_Y^{-1}\otimes L))=\mathbb C`." [I]: "It preserves the inverse image of the singular locus, the hexagon on `\mathrm{dP}_6`. Its permutation of the six components preserves their cyclic incidence, hence lies in the order-twelve dihedral group." "`\partial S` is the hexagon. Here `h^1(\mathcal O_{\partial S})=1` ... The hexagon traversal maps to `e_1-e_2+e_3-e_1+e_2-e_3=0`." [III]: "The central normalization is the standard hexagonal toric surface ... Its Euler number is two"; "honeycomb dual to the `A_2` triangulation". [V]: "the normalized hexagon", "hexagonal toric boundary".
- Locator: [II] L27203-27222 (`cdp:st:C4g`); [I] L10745-10751, L31925-31940, L9148, L26003, L26201; [III] L23078, L6593; [V] L13449, L14864-14882, L15086.
- Context: the cusp fibre over j = ∞ of every complex six-sphere is a cycle of `dP_6` with hexagonal boundary (the periodic `A_2` fan).

**S6-124** · the higher-rung "ternary triality structure"
- Statement: "The higher target is a three-directional structure encoded by the ordered triality modules and their invariant trilinear tensor. The proofs retain the Peirce coefficient 1/2, determinant coefficient 2, spectral graph, flag-cell inverse and degree-+1 collapse ... The single shared source ... retains the original modulo-840 lattice, full Weyl quotient, exact index-six Leech neighbour and cyclic-triality isometry. ... whose inclusion has quotient `\mathbb Z/12`; the Albert determinant contains 2F, not F. It also gives the common Leech intersection J of determinant 81 and index 9, and its fixed fourth `A_2^{12}` extension with 72 roots. Wilson's construction supplies the cyclic fixed Gram matrix `3G_{E_8}`, the `A_2\otimes E_8` complement, the quotient `\mathbb F_3^8`". Attempts file: "'24-dimensional' refers to the rank of the Niemeier and Leech lattices; 'triality' refers to the three 8-dimensional octonionic summands, and 'mod 12' ...".
- Locator: [WB]`higher_rung_24d_continuation.tex` L4-28; `<local>/Documents\s6_workbench_repo_20261112\yang_mills_repository_s6\ATTEMPTS.md` L20-26, L97-125.
- Context: summary paragraph tying the lattice lane to the S6 higher rung.

**S6-125** · triality inside the umbral shadow
- Statement: "The distinguished residue action has quotient g=1 and therefore produces the untwisted shadow ... The four-component signed action and the D4 triality quotient survive and enter the displayed matrix." ([WB]`niemeier_umbral_shadow.tex`); "`H_D`, `R_D` ... induce (s c) and (v s)"; "`C v_D=c_D+(1,-1,0,0)`" (correction in the evidence README).
- Locator: [WB]`niemeier_umbral_shadow.tex` L535-541; [WBE]`evidence\triality_leech_20260906\README.md` L23-27.
- Context: the `D_4` triality acts on the umbral data through `s_g`, `c_g`.

---

## 8. Summary for the conference

**Entries:** 125 (S6-001 to S6-125): 39 on j and modular functions, 23 on lattices and codes, 14 on groups, 17 on
moonshine proper, 10 on triangle groups / `Z[ω]` / `Z[i]` / CM, 10 on numerology (12, 24, 28, 72, 216, 840), 12 on the
user's vocabulary.

**Central objects (the ones that recur most, with the entries where they occur).**
1. Klein's j with the base coordinate `t=j/1728`; the base of every complex six-sphere is the j-line, with the
   orbifold points j = 0 (order 3), j = 1728 (order 4) and the cusp; `J(q)=q^{-1}+744+196884q+\cdots` and its natural
   boundary bound the family (`0<|w|<216`). S6-001 to S6-007, S6-012, S6-013, S6-019, S6-027 to S6-037.
2. `SL_2(\mathbb Z)` / `PSL_2(\mathbb Z)` and the order-twelve character `SL_2(\mathbb Z)^{ab}\cong\mathbb Z/12` (the
   `\eta^2` multiplier): Paper I's α, the umbral determinant χ, the peripheral values 4, −3, −1. S6-063, S6-065,
   S6-066, S6-081, S6-085, S6-104, S6-105.
3. Dedekind η, Jacobi `\vartheta_1` and Siegel functions (the period norm `N=|\vartheta_1/\eta|e^{-\pi(\Im z)^2/\Im\tau}`;
   `\Delta=\eta^{24}`; `\eta^2` inside the central 12-cycle). S6-001, S6-008 to S6-012, S6-023, S6-025, S6-026,
   S6-037, S6-081, S6-083.
4. The Niemeier lattice `N(A_5^4D_4)` (built from the Erdős–Straus residues mod 840) with its Weyl-vector Leech
   neighbours, their intersection J (det 81), the `A_2^{12}` extension, the umbral group `GL_2(\mathbb F_3)` and the
   CDH shadow of lambency 6. S6-041 to S6-056, S6-061, S6-068 to S6-072, S6-077 to S6-087, S6-110 to S6-112.
5. `\mathbb Z[\omega]` and `\mathbb Z[i]` (the CM fibres at j = 0 and 1728, the norms 3 and 2 inside 216 and `48^3`,
   the Eisenstein norm `x^2+xy+y^2` of the `\Theta_7` returns, `\zeta_{12}`, `\mathbb Q(\zeta_{12})`). S6-007, S6-009,
   S6-089, S6-096 to S6-103.
6. The numbers 12, 24, 72: the twelve-cycle and mod-12 twists, `\Lambda/R_0\supset\mathbb Z/12`, the value-group
   quotient `\mathbb Z/12`, the `F_4` Coxeter number 12; rank 24, `|V_{840}|=24`, K3's 24, the denominator 24 of the
   exotic-sphere class; glue index 72 = Fricke constant of `T_6` = root count of `A_2^{12}`. S6-040, S6-044, S6-047,
   S6-055, S6-057, S6-071, S6-084, S6-086, S6-104 to S6-113.
7. Octonions, triality and the Albert algebra (the Leech/Albert object `N\otimes\mathbb R\cong\mathbb O^3`, the cubic
   `\operatorname{Re}((q_1q_2)q_3)`, `F_4/\mathrm{Spin}(8)`, the sphere ladder `S^6\to S^{24}`). S6-052 to S6-056,
   S6-070, S6-073, S6-117 to S6-125.
8. Level 3 and level 6: `\Gamma_0(3)` (the index-four collision cover, the theta series of J, the Hesse coordinate)
   and `\Gamma_0(6)` (`T_6`, Fricke `W_6`, `J_6`). S6-029, S6-036, S6-083, S6-084, S6-087.
9. Genus-zero modular covers and their dessins (index 2, 4, 9, 10, 12; Oguiso–Shioda rows with heights `1/d`).
   S6-029 to S6-034.
10. `E_8` (Wilson's octonionic `E_8`, `3G_{E_8}`, `A_2\otimes E_8`, the affine `E_8` plumbing, `j^{1/3}=E_4/\eta^8=\theta_{E_8}/\eta^8`).
    S6-036, S6-052, S6-056, S6-059, S6-060.

**Exact coincidences between entries (finder's notes; equalities of formulas, not interpretations).**
- `\alpha\equiv-\chi`: Paper I's monodromy character (α(S)=9, α(T)=1, α(order-3 a)=4) is the negative of the umbral
  determinant character (χ(T)=−1, χ(S)=3) and agrees with the higher-rung peripheral character up to the same sign
  convention (χ(C_1)=4, χ(C_2')=−3, χ(C_0)=−1). S6-063, S6-065, S6-066, S6-081.
- The linear form `12\ell_0-4\ell_1-3\ell_2`: Paper I's sphere integer p (S6-104), the Seifert Euler number 12e
  (S6-105) and the Erdős–Straus terminal value λ with its group `\langle c,x,y\mid xy=c^{\ell_0},x^3=c^{\ell_1},y^4=c^{\ell_2}\rangle`
  (S6-111) are the same expression.
- Level 3: the j-map `j=(t+27)(t+3)^3/t` of the index-four cover (S6-029, checked to be the classical
  `\Gamma_0(3)` relation) and the weight-12 theta series of J on `\Gamma_0(3)` (S6-087).
- 72: glue index of `N(A_5^4D_4)` (S6-042), Fricke constant of `T_6` (S6-084), root count of `A_2^{12}` (S6-047);
  the first two are equal by the theorem of S6-086.
- 1/12: total mass of the Betti current (S6-023), Seifert Euler number ±1/12 (S6-105), cusp coefficient −1/12 of the
  orbifold divisor of y (S6-037), Mordell–Weil height 1/12 of profile 50 (S6-029, S6-032).

**How the search was bounded.** Roots searched (and only these): `s6_pro_prompts_20261112`, `..._work` (history and
`_from_earlier_checkpoints` copies pruned), `..._sent`, `s6_workbench_repo_20261112`, `TO_SEND\PRO\9_S6_papers`
(incl. SENT), `S6_HEXAGON_DEPOSITS_20261120` (inside `..._work`), `task_notes\s6_*.md`, `agent_notes\s6_fork_NOTES.md`,
`field_experts\hexagon\HEXAGON_STATUS.md`. Keyword scans (scratchpad `ms\scan.py`, `ms\count.py`) located the files;
the mathematics was then read from the statements (`ms\stmts.py`) and contexts of the newest versions. No file named
`SAT_WITNESS_EXTRACTION*`, `74_*` or `SAT_KRONECKER*` was opened. Nothing was published.

**Read in full or at statement level:** Papers I-V of the series (results outlines in full; bodies through every
statement environment carrying a modular, lattice, group or numerology keyword; Paper IV, 130,000 lines, through its
outline and keyword-located passages); Paper VI of S6_10 (merged into Paper II; nothing additional); the S6_05
ARITHMETIC prompt and return (section B in full at statement level; sections A and C where they bear on the entries);
the S6_02_PUSH report (ghost lemma); the workbench lattice lane (`niemeier_umbral_shadow`, `es_niemeier_*`,
`common_d4_image`, `erdos_straus_*`, `higher_rung_24d_continuation` statements, `z6_defect_center_bridge`,
`koide_*` where modular, `candidate_geometry`), the frozen key advances, the Pro feedback of 6 Sep, the provenance
note, the survey reader D1's notes, the Leech `Z^24` question and consult, Claude's S6 notes of 15-16 Nov, the routes
notes, course CG-S6 lessons 4 and 11 and the Adams-tower lesson, HEXAGON_STATUS row H10.

**Earlier versions holding the same statements (not re-listed):** `S6_07_PAPER_paper.tex` (16 Nov),
`S6_09_PAPERS_{I,II,III}.tex` (17 Nov), `S6_10_PAPERS_{I..VI}.tex` (19 Nov), `S6_SERIES_GRIND_{I..V}.tex` (20 Nov),
the Hexagon deposit builds (`S6_HEXAGON_DEPOSITS_20261120\I`, `\V`), and the S6_01/S6_02/S6_03/S6_04/S6_06 returns
whose statements the series absorbed.

**Third-party literature that fed the S6 work (in the S6 folders; not extracted as entries):** Cheng–Duncan–Harvey,
Umbral moonshine and the Niemeier lattices (arXiv:1307.5793; cited, Table 3); Chenevier–Lannes (arXiv:1409.7616, in
`s6_pro_prompts_20261112_work\literature\arXiv_src\1409.7616`); Wilson, Octonions and the Leech lattice (2009);
Conway–Sloane ch. 16, 24; Borcherds 1985; Schütt–Shioda, Elliptic surfaces (arXiv:0907.0298, supersingular K3);
Gross–Siebert (math/0309070, the ghost sheaf); Louvel (arXiv:1107.5282, Salié sums); Oguiso–Shioda 1991; Miranda
1990; Fukae 2002; Mare–Willems 2013; Duke–Imamoglu on zeros of ℘ (`literature\Duke_Imamoglu_zeros_of_Weierstrass_p.pdf`).
