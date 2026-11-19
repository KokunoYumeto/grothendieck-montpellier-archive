from pathlib import Path
p=Path('output/RESEARCH_SA07/sections/F_audit.tex')
s=p.read_text()
assert '\\begin{result}{F.3.15}' not in s

a=Path('work/LM6_A20_primary_reproof.tex').read_text()
a_body=a[a.index('\\paragraph{1. Actual finite-cover'):a.index('\\paragraph{Boundary of this audit.}')]
a_body=a_body.replace("Nakamura's (4.3)--(4.4) gives", "Nakamura's (4.3)--(4.4) gives\\cite[p.~214]{AuditNakamura1995}")
a_body=a_body.replace("It is surjective by Lemma4.10 for odd $\\ell$.", "It is surjective by Lemma4.10 for odd $\\ell$\\cite[p.~217]{AuditNakamura1995}.")
a_body=a_body.replace("Ishii's Corollary4.10 gives a nonzero character", "Ishii's Corollary4.10 gives a nonzero character\\cite[p.~21]{AuditIshii2024v2}")
a_body=a_body.replace("multiplied by the nonzero factor $(1-\\ell^2)^{-1}$.", "multiplied by the nonzero factor $(1-\\ell^2)^{-1}$\\cite[Theorem1.3,p.~3]{AuditIshii2024v2}.")
a_body=a_body.replace("Nakamura1994, Theorem2.1.1, applied", "Nakamura's Theorem2.1.1\\cite[p.~94]{AuditNakamura1994}, applied")
a_result=r'''\begin{result}{F.3.15}{CM pro-prime normalizers: an independent primary-source proof}{Proved; the separate integral lifting claim is not used}
Let $K=\Q(i)$, $E_0:y^2=x^3-x$, $U=E_0\setminus\{O\}$, and
\[
 F=\pi_1(U_{\overline K}),\qquad P_\ell=F^{(\ell)},\qquad
 E_\ell=\pi_1(U)/\ker(F\to P_\ell).
\]
For every prime $\ell$, a nontrivial closed procyclic subgroup $A\subset P_\ell$ whose normalizer in $E_\ell$ has open image in $G_K$ is contained in an actual cusp inertia subgroup of $P_\ell$.
\end{result}
\begin{proof}
This independently re-proves the recognition assertion of LM6 A.20. The arithmetic nonvanishing input is Ishii's author version arXiv:2312.04175v2, with its exact standing hypotheses checked below; the final journal full text was not obtained. The distinct integral class-four lifting claim at $\ell=5$ in the prior return is not an input or a conclusion here.

'''+a_body+r'''\end{proof}

\paragraph{Verification boundary.}
The displayed proof also supplies the two steps previously left implicit: the ordinary-reduction condition in Ishii's input, and the removal of a lower inner conjugator when the original abelian image of $u$ is not primitive. It uses no chosen splitting of the arithmetic normalizer. The exact numerical normalization $\kappa/48$ and the integral class-four lift at5 remain outside this re-proof's scope. The full profinite common-kernel subgroup in LM6 A.22 remains to be constructed or excluded.

'''

b=Path('work/LM6_A22_CM_Prym_cover.tex').read_text()
b_body=b[b.index('Take the smooth plane quartic'):b.index('\\subsection*{Exact reach of the cover tower')]
b_body=b_body.replace('\\subsection*{The actual punctured maps also eliminate this cover\'s proper homology alternative}',"\\paragraph{The actual punctured maps eliminate this cover's proper homology alternative.}")
b_body=b_body.replace('There is a stronger scoped consequence, using the pro-prime recognition theorem already proved in LM6 A.20 for $E_0$.', 'We now apply the independently proved recognition theorem F.3.15 to $E_0$.')
b_body=b_body.replace('LM6 A.20 makes it cuspidal', 'F.3.15 makes it cuspidal')
b_body=b_body.replace("Nakamura's full profinite recognition theorem then", "Nakamura's full profinite recognition theorem\\cite[Theorem2.1.1,p.~94]{AuditNakamura1994} then")
b_body=b_body.replace('and the cusp centralizer statement places all of $A$ there.', 'and the cusp centralizer statement places all of $A$ there\\cite[Lemma2.1.2,p.~95]{AuditNakamura1994}. Here $Y$ has28 punctures, so each peripheral generator belongs to a free generating system and the cited primitive-generator lemma applies directly.')
b_result=r'''\begin{result}{F.3.16}{A finite-cover CM Prym and its actual punctured quotient maps}{Proved; a precise special case of the residual homology test}
For $U=(y^2=x^3-x)\setminus\{O\}$ over $K=\Q(i)$, there is a degree-$32$ finite etale cover $Y\to U$ whose smooth compactification has genus3 and whose proper Prym contains an elliptic curve isogenous to $E_0:y^2=x^3-x$. Thus a general assertion that these Pryms have no CM weight-one characters is false.

For this same cover, every closed procyclic subgroup of $\pi_1(Y_{\overline K})$ with open arithmetic normalizer image has zero image in the proper homology $H_1(\overline Y,\Z_\ell)$ for every $\ell$. Whenever it has nonzero image in $H_1(Y_{\overline K},\Z_\ell)$ for some $\ell$, it is contained in one cusp inertia group. These assertions use the explicit maps on the same punctured curve constructed below.
\end{result}
\begin{proof}
'''+b_body+r'''\end{proof}

'''

c=b[b.index('\\subsection*{Exact reach of the cover tower'):]
c_body=c[c.index('The subgroup $H='):]
c_result=r'''\begin{result}{F.3.17}{The precise reach and limitation of this cover tower}{Proved; no arithmetic normalizer is asserted for the invisible elements}
Let $F=\pi_1(U_{\overline K})$, $P_p=F^{(p)}$,
\[
 R=\bigcap_p\ker(F\to P_p),\qquad S=R_{\rm nil}(F').
\]
The cover of F.3.16 and the Fermat power tower below have geometric covering subgroups containing $\ker(F\to P_2)$ and hence $R$. There are actual nontrivial closed procyclic subgroups of $S$ whose images in the first homology of every member of this tower vanish. More generally this holds for every family of open subgroups of $F$ containing $R$. The exhibited subgroups are not asserted to have open arithmetic normalizer image, so this conclusion does not decide LM6 A.22.
\end{result}
\begin{proof}
'''+c_body+r'''\end{proof}

'''

marker='\\paragraph{Unresolved obligations retained.}'
assert marker in s
s=s.replace(marker,a_result+b_result+c_result+marker)
old='The incomplete LM6 A.22/A.50 summaries do not supply the missing character premise; their complete statements and that proof remain a source obligation.'
new='The full LM6 source has now been obtained and the exact A.50 enlargement is checked in F.3.10. Its residual weight-one character still does not supply the cyclotomic-action premise needed to close A.22. F.3.15 independently re-proves the pro-prime recognition result; F.3.16--F.3.17 give actual additional cover maps and their precise remaining visibility limit.'
assert old in s
s=s.replace(old,new)
p.write_text(s)
print('Integrated F.3.15--F.3.17; result environments:',s.count('\\begin{result}'),'; source lines:',len(s.splitlines()))
