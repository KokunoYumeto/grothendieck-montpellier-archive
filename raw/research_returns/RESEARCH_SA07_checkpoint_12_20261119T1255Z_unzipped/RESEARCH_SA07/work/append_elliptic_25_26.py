from pathlib import Path
p=Path('output/RESEARCH_SA07/sections/A_elliptic.tex')
s=r'''

\begin{result}{A.4.25}{The exact defect between the complex and ordinary differential operators}{Proved}
On a fine modular curve, work locally with an algebraic symplectic frame $(\omega,\xi)$ of the universal elliptic de Rham bundle, with $\omega$ spanning the Hodge line and $\langle\omega,\xi\rangle=1$. Write
\[
 \nabla\omega=\omega\otimes A+\xi\otimes B,
 \qquad \operatorname{KS}(\omega^{\otimes2})=B.
\]
Here $B$ is a local generator of the cotangent bundle. Projection along the complement $L_a=\langle\xi+a\omega\rangle$, followed by Kodaira--Spencer, defines the weight-raising operator
\[
 D_a(f\omega^{\otimes k})
 =\left(\frac{df}{B}+k\left(\frac AB-a\right)f\right)
   \omega^{\otimes(k+2)}.
\]
For any two complements,
\[
 (D_a-D_b)(f\omega^{\otimes k})
   =k(b-a)f\omega^{\otimes(k+2)}.
\]
At a good ordinary point, let $L_{u_p}$ be the unit-root complement. For a specified embedding into $\C_p$ of a number field containing an algebraic $h$, agreement of the two operators on one section of nonzero weight and nonzero value is exactly
$\iota_p(h)=u_p$.
\end{result}
\begin{proof}
The symplectic definition of Kodaira--Spencer gives
$\langle\omega,\nabla\omega\rangle=B$, fixing its sign. Projection along $L_a$ sends $\omega$ to itself and $\xi$ to $-a\omega$. The Leibniz rule on $\omega^{\otimes k}$ therefore gives
\[
 \operatorname{pr}_a\nabla(f\omega^{\otimes k})
 =\bigl(df+kf(A-aB)\bigr)\omega^{\otimes k}.
\]
Applying the inverse Kodaira--Spencer identification proves the first formula. Subtraction proves the second. At the stated point, $k$ and $f$ are nonzero in characteristic zero; equality of the values is consequently equivalent to equality of the two complement parameters. A nonzero local section of the Hodge line supplies such a test section, so no global nonvanishing assumption on a particular Eisenstein series is needed.
\end{proof}

Mori's corrected final article \cite[Sections 3.3--3.5, pp.56--57]{EllMori1994} uses exactly Gauss--Manin, Kodaira--Spencer, and projection to construct these operators. Its Theorems~1 and~10 retain a CM elliptic curve with ordinary good reduction. Section~3.5 obtains equality of the complex and $p$-adic operators from the CM endomorphism decomposition. A.4.25 computes the equality required to apply that comparison in the present question. It has not been proved for a putative non-CM algebraic $h$. Section~0.4, p.47, explicitly corrects a constant in the 1990 and 1991 announcements; none of those uncorrected numerical expressions is used here.

\begin{result}{A.4.26}{The reduced theta coefficient field and its torsion translations}{Proved}
Let $k=\Q(g_2,g_3)$ for the fixed short Weierstrass equation, let $\sigma(u)$ be normalized by $\sigma'(0)=1$, and let $h$ be the actual Hodge splitting coefficient. The normalized reduced theta function and the associated Kronecker theta function are
\[
 \theta_h(u)=e^{-hu^2/2}\sigma(u),\qquad
 \Theta_h(u,v)=e^{-huv}\frac{\sigma(u+v)}{\sigma(u)\sigma(v)}.
\]
Their Taylor or Laurent coefficient fields over $k$ are exactly $k(h)$. Under the principal polarization, $\Theta_h$ represents the canonical meromorphic section of
\[
 m^*\mathcal O_E([0])\otimes
 p_1^*\mathcal O_E([0])^{-1}\otimes
 p_2^*\mathcal O_E([0])^{-1}
 \quad\hbox{on }E\times E.
\]
For every nonzero torsion point represented by $u_0\in\Lambda\otimes\Q$, the reduced translation
\[
 T_{u_0}(u)=
 e^{-c\bar u_0(u+u_0/2)}\theta_h(u+u_0),
 \qquad c=\frac{\pi}{\operatorname{Area}(\Lambda)},
\]
has coefficient field over $\Qb$ exactly $\Qb(h)$.
\end{result}
\begin{proof}
The formal equations $\wp'^2=4\wp^3-g_2\wp-g_3$, $\zeta'=-\wp$, and $\sigma'/\sigma=\zeta$, with their normalized leading terms, give
\[
 \sigma(u)=u-\frac{g_2}{240}u^5-\frac{g_3}{840}u^7+\cdots\in k[[u]].
\]
All subsequent coefficients are obtained by rational recursion. The coefficient of $u^3$ in $\theta_h$ is $-h/2$, and all coefficients lie in $k(h)$. This proves its exact field. Moreover,
\[
 \Theta_h(u,v)=\frac1u+\frac1v-h(u+v)
       +\text{terms of total degree at least three}.
\]
The same reasoning proves the exact Laurent coefficient field.

For $\lambda\in\Lambda$, the sigma transformation law and
$\eta_\lambda=h\lambda+c\bar\lambda$ give
\[
 \theta_h(u+\lambda)
 =\epsilon(\lambda)
   e^{c\bar\lambda(u+\lambda/2)}\theta_h(u).
\]
Together with $\theta_h'(0)=1$, this is the normalized reduced theta function of Bannai--Kobayashi \cite[Example 1.9, pp.10--11]{EllBannaiKobayashi2010}. Their area variable is $\operatorname{Area}(\Lambda)/\pi$, so its inverse is exactly our $c$. Taking the quotient under the addition map $m$ gives the stated section and line bundle, with residue one along $u=0$ \cite[Example 1.10, pp.11--12]{EllBannaiKobayashi2010}.

Extend $\lambda\mapsto\eta_\lambda$ $\Q$-linearly to $\Lambda\otimes\Q$. Direct multiplication gives
\[
 T_{u_0}(u)=e^{-hu^2/2}\,S_{u_0}(u),\qquad
 S_{u_0}(u)=e^{-\eta_{u_0}(u+u_0/2)}\sigma(u+u_0).
\]
Theorem~2.12, pp.26--27, of the same source applies to every algebraic elliptic curve, including those without CM, and gives algebraic coefficients for $S_{u_0}$. Its constant coefficient is nonzero because the torsion point is nonzero. If $s_j=[u^j]S_{u_0}$ and $t_j=[u^j]T_{u_0}$, then
$t_0=s_0\ne0$ and $t_2=s_2-hs_0/2$. Thus all $t_j$ lie in $\Qb(h)$ and $h=2(s_2-t_2)/s_0$, proving equality of fields.
\end{proof}

Bannai--Kobayashi's Proposition~2.14, pp.28--29, proves ordinary integrality by choosing an actual CM multiplication whose two eigenvalues have different $p$-adic valuations. Proposition~2.1 and Corollary~2.2, pp.20--21, likewise retain CM in their origin-algebraicity proof. The torsion-translation theorem used in A.4.26 has the broader hypothesis explicitly stated there; its exact Gaussian factor shows what it transfers. The theorem has not supplied ordinary bounded denominators from $h\in\Qb$, and H1 remains unchanged.
'''
with p.open('a') as f:f.write(s)
with Path('work/elliptic_references.bib').open('a') as f:f.write(r'''
@article{EllMori1994,
 author={Andrea Mori},title={A characterization of integral elliptic automorphic forms},
 journal={Annali della Scuola Normale Superiore di Pisa, Classe di Scienze},series={4},volume={21},number={1},pages={45--62},year={1994},
 url={https://www.numdam.org/item/ASNSP_1994_4_21_1_45_0.pdf},
 note={Opened and downloaded complete final primary scan. Theorem 1, pp.45--46; correction to constants in the 1990/1991 announcements, Section 0.4, p.47; Theorem 10, p.54; geometric differential operators in Sections 3.3--3.5, pp.56--57. All cited integrality comparisons retain the stated CM and ordinary hypotheses.}
}
@article{EllBannaiKobayashi2010,
 author={Kenichi Bannai and Shinichi Kobayashi},title={Algebraic theta functions and the $p$-adic interpolation of {Eisenstein--Kronecker} numbers},
 journal={Duke Mathematical Journal},volume={153},number={2},pages={229--295},year={2010},
 url={https://arxiv.org/pdf/math/0610163},
 note={Opened and downloaded complete 55-page primary arXiv version 4, dated 11 December 2007. All page locators refer to that opened version: Examples 1.9--1.10, pp.10--12; Proposition 2.1 and Corollary 2.2, pp.20--21; Theorem 2.12, pp.26--27, explicitly valid with or without CM; Proposition 2.14, pp.28--29, retains CM and ordinary hypotheses. Their area parameter equals area divided by pi.}
}
''')
with Path('work/agent_elliptic.md').open('a') as f:f.write(r'''

## 26. Corrected Mori operators and the exact theta morphism

**A.4.25 (proved).** In an algebraic symplectic frame with ∇ω=ωA+ξB and KS(ω²)=B, projection along ξ+aω gives D_a(fω^k)=(df/B+k(A/B−a)f)ω^(k+2). Therefore D_a−D_b=k(b−a) on every nonzero weight section. At an ordinary algebraic point, the equality between the complex Hodge operator transported through a specified p-adic embedding and the unit-root operator is exactly ι_p(h)=u_p. Proof is the displayed Leibniz/projection calculation in the TeX result. Mori1994 final primary PDF https://www.numdam.org/item/ASNSP_1994_4_21_1_45_0.pdf opened/downloaded complete. Theorem1 pp45–46, Theorem10p54, Sections3.3–3.5 pp56–57 retain CM and ordinary hypotheses. Section0.4p47 explicitly corrects a constant in the 1990/1991 announcements; the older numerical expressions are not used. The original 1990 download timed out/returned503 and is not claimed as fully read.

**A.4.26 (proved).** The exact normalized theta function is θ_h(u)=exp(−hu²/2)σ(u), with σ′(0)=1. The sigma coefficients lie in k=Q(g2,g3), and [u³]θ_h=−h/2; thus its coefficient field is k(h). The Kronecker theta function Θ_h=e^(−huv)σ(u+v)/(σ(u)σ(v)) begins 1/u+1/v−h(u+v)+terms of degree≥3, hence has the same exact coefficient field. Its actual line bundle is m*O([0])⊗p1*O([0])^-1⊗p2*O([0])^-1 on E×E, under the principal polarization. The sigma quasiperiod law and ηλ=hλ+c barλ prove reduced automorphy, including the area normalization c=π/area.

For every nonzero torsion class u0, define T_u0(u)=exp[−c bar(u0)(u+u0/2)]θ_h(u+u0). Direct multiplication gives T_u0=exp(−hu²/2)S_u0, with S_u0=exp[−η(u0)(u+u0/2)]σ(u+u0). Bannai–Kobayashi Theorem2.12 applies with or without CM and gives algebraic coefficients s_j of S_u0. Since s0≠0, t2=s2−hs0/2 recovers h, so Qbar(coefficients T_u0)=Qbar(h). Thus the exact torsion translation transfers the same coefficient-field condition, without introducing a new independent algebraicity input.

Primary source: https://arxiv.org/pdf/math/0610163, complete55-page version4 dated11December2007, opened/downloaded/text read. Examples1.9–1.10pp10–12; Proposition2.1/Corollary2.2pp20–21; Theorem2.12pp26–27; Proposition2.14pp28–29. Final DukeMathJ153(2010)229–295 metadata separately retrieved. The area variable in this source equals area/π. Proposition2.14's ordinary integrality proof chooses a CM multiplication whose two eigenvalues have different p-adic valuations; the proof was read and that hypothesis is retained. No ordinary integrality conclusion from coefficient algebraicity alone has been established. These are exact map/source checks; the H1 gate is unchanged.
''')
with Path('work/agent_elliptic_check_events.tsv').open('a') as f:
    for row in [
      ('A.4.25','independent re-proof','Exact Gauss-Manin projection and Kodaira-Spencer sign give D_a-D_b=k(b-a), so complex/unit-root comparison on a nonzero section is exactly h=u_p.'),
      ('A.4.25','used and rechecked in this run','Mori1994 final primary scan read: Theorem1 pp45-46, correction0.4p47, Theorem10p54, Sections3.3-3.5pp56-57; CM/ordinary hypotheses retained.'),
      ('A.4.26','targeted proof check','Sigma normalization, reduced automorphy, coefficient extraction and torsion Gaussian identity prove exact coefficient fields k(h) and Qbar(h).'),
      ('A.4.26','used and rechecked in this run','BannaiKobayashi2007v4 complete primary PDF read at Examples1.9-1.10pp10-12, Prop2.1/Cor2.2pp20-21, Thm2.12pp26-27, Prop2.14pp28-29; distinct CM hypotheses explicitly checked.')]:
        f.write('\t'.join((row[0],'2026-11-19','OpenAI GPT-6 Astra; effort inherited; elliptic_splitting',row[1],row[2]))+'\n')
print('Appended A.4.25-26 with bib and check events')
