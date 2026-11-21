#!/usr/bin/env python3
"""Literal-safe, reproducible conversion of the two complete proof drafts.

Every source paragraph is retained.  Display formulae are transcribed below;
unrecognised prose is escaped, never reinterpreted as Markdown emphasis.
Only explicit **...** and `...` markup is interpreted.  No Pandoc dependency.
"""
from pathlib import Path
import re
import hashlib
import json

ROOT = Path(__file__).resolve().parent

SR = [
r'\#\bigl(D\cap J[r]\bigr)\leq 108r^4.\tag{SR1.1}',
r'D\cdot([r]^*3\Theta)^2=(2\Theta)\cdot(3r^2\Theta)^2=18r^4\Theta^3=108r^4.',
r'P=2^{2048},\quad L=\operatorname{lcm}(1,2,\ldots,P),\quad N=4L^2+1,\quad d=N-1=4L^2.\tag{SR1.2}',
r'H\cap(C-C)=\{0\}.\tag{SR1.3}',
r'J_6(q)=q^6\prod_{p\mid q}(1-p^{-6})>\frac{q^6}{2}.',
r'\begin{aligned}\Pr\bigl(\langle v\rangle\cap(D\setminus\{0\})\ne\varnothing\bigr)&\leq216\sum_{\substack{q\mid N\\q>1}}\frac{\varphi(q)}{q^2}\\&\leq216\left[\exp\left(\sum_{p\mid N}\frac1p\right)-1\right].\end{aligned}\tag{SR1.4}',
r'\sum_{q\mid N}\frac{\varphi(q)}{q^2}=\prod_{p^a\parallel N}\left(1+\frac{1-p^{-a}}p\right)\leq\prod_{p\mid N}\left(1+\frac1p\right).',
r'\log L<P\log4.',
r'\sum_{p\mid N}\frac1p\leq\frac{\log N}{(P+1)\log(P+1)}<\frac1{500}.',
r'\operatorname{ch}(F)=1-\frac N2\theta^2+\frac N3\theta^3,\qquad\Delta:=\int_Z\frac{\theta^3}{6}=\frac1N.\tag{SR1.5}',
r'\bigl(\dim\operatorname{Ext}^j(F,F)\bigr)_{j=0}^3=(1,6,6,1).\tag{SR2.1}',
r'0\longrightarrow T_C\longrightarrow\mathcal O_C^3\longrightarrow N_{C/J}\longrightarrow0.',
r'0\longrightarrow H^0(N_{\bar C/Z})\longrightarrow\operatorname{Ext}^1(F,F)\longrightarrow\operatorname{Ext}^1(F,\mathcal O_Z).',
r'\operatorname{Ext}^1(F,F)=H^1(\mathcal O_Z)\oplus H^0(N_{\bar C/Z}).\tag{SR2.2}',
r'H^1(\mathcal O_Z)\oplus H^0(T_Z)\longrightarrow\operatorname{Ext}^1(F,F).',
r'H^2(\mathcal O_Z)\oplus H^1(T_Z)\subset\operatorname{HH}^2(Z).',
r'\begin{aligned}&\operatorname{Ext}^2(F,F)\otimes\operatorname{Ext}^0(F^\vee,F^\vee)\\{}\oplus{}&\operatorname{Ext}^1(F,F)\otimes\operatorname{Ext}^1(F^\vee,F^\vee)\\{}\oplus{}&\operatorname{Ext}^0(F,F)\otimes\operatorname{Ext}^2(F^\vee,F^\vee).\end{aligned}',
r'H=N\theta_x+\widehat\theta+\gamma.\tag{SR3.1}',
r'\Phi=(\operatorname{id}_Z\boxtimes\operatorname{FM}_{\mathcal P^{-1}})\circ\mu^*,\qquad E=\Phi(F\boxtimes F^\vee).\tag{SR3.2}',
r'\exp(-\gamma/2)\operatorname{ch}(E)=t+2H-\frac{H^3}{12d}+\frac{H^5}{960d^2}.\tag{SR3.3}',
r'a=\frac{1+1/u}{2},\qquad\bar a=\frac{1-1/u}{2}.',
r'\operatorname{ch}(F)=a\exp(s\theta)+\bar a\exp(\bar s\theta).\tag{SR3.4}',
r'\begin{aligned}&\int_{c_i,d_i}\exp\bigl(s(a_i+c_i)(b_i+d_i)-t c_i d_i-(c_i v_i-d_i u_i)\bigr)\\&\quad=(s-t)-st a_i b_i-s b_i u_i-u_i v_i+s a_i v_i-s a_i b_i u_i v_i.\end{aligned}\tag{SR3.5}',
r'-\exp\bigl((a_i v_i-b_i u_i)/2\bigr)(s a_i-u_i)(s b_i-v_i).',
r't=-\Delta\bigl(a^2Q_s+\bar a^2Q_{\bar s}\bigr).\tag{SR3.6}',
r'\alpha\exp(\gamma_i/2-H_i/\alpha),\qquad H_i=N a_i b_i+u_i v_i+a_i v_i-b_i u_i.',
r'\Delta a\bar a\alpha^3\bigl[\exp(-H/\alpha)-\exp(H/\alpha)\bigr].',
r'T=\begin{pmatrix}-2&-1\\N&0\end{pmatrix}.',
r'N\theta_1+\theta_2+(m^*\theta-\theta_1-\theta_2)=(N-1)\theta_1+m^*\theta,',
r'j:E_i^3\longrightarrow J.',
r'j^*\Theta=2\theta_{E_i^3},\qquad\deg j=8.',
r'R=\begin{pmatrix}1&1\\\bar s&s\end{pmatrix},\quad k=\operatorname{diag}(h,\phi_\theta h),\quad f=NkR:E_i^6\longrightarrow A.\tag{SR4.1}',
r'R^\dagger\begin{pmatrix}N&1\\1&1\end{pmatrix}R=2dI,\qquad f^*H=4dN^2\theta_{\rm prod},\qquad\deg f=4096d^3N^{12}.\tag{SR4.2}',
r'\operatorname{Ext}^2(E_0,E_0)^G=\operatorname{Ext}^2(E,E).',
r'f_*\mathcal O_{E_i^6}=\bigoplus_{\alpha\in\ker\widehat f}\alpha,',
r'\operatorname{Ext}^j(E_0,E_0)=\bigoplus_\alpha\operatorname{Ext}^j(E,E\otimes\alpha).',
r'\Phi^{-1}(E\otimes\alpha)=(t_x^*F\otimes L_1)\boxtimes(t_y^*F^\vee\otimes L_2).',
r'\exp(B_0)\operatorname{ch}(E_0)=t_0+2H_0-\frac{H_0^3}{12d}+\frac{H_0^5}{960d^2}.',
r'\begin{gathered}P_m=2^{2048+\lceil\log_2(m+1)\rceil},\qquad L_m=\operatorname{lcm}(1,\ldots,P_m),\\N_m=4mL_m^2+1,\qquad d_m=4mL_m^2.\end{gathered}',
r'\sum_{p\mid N_m}\frac1p<\frac{\log(4m+1)+4P_m\log2}{P_m\log P_m}<\frac1{500}.',
r'\begin{gathered}R^\dagger C_2R=2\begin{pmatrix}-1&s\\\bar s&-1\end{pmatrix},\quad f^*\gamma=4N^2\begin{pmatrix}-1&s\\\bar s&-1\end{pmatrix}\otimes I_3,\\B_0=2N^2\begin{pmatrix}1&-s\\-\bar s&1\end{pmatrix}\otimes I_3.\end{gathered}\tag{SR6.1}',
r'\operatorname{ch}(E_0^{\prime})=t_0+2c\theta_{\rm prod}-\frac{16}{3}d^2N^6\theta_{\rm prod}^3+\frac{16}{15}d^3N^{10}\theta_{\rm prod}^5.\tag{SR6.2}',
r'\begin{gathered}t_0=\frac{c_3(E_0^{\prime})}{2}+\left[\frac{16}{3}d^2N^6(1-8d)\right]\theta_{\rm prod}^3,\\\delta=2,\qquad T_0:=-\int_{E_i^6}t_0^2=32768d^4N^{12}.\end{gathered}\tag{SR6.3}',
r'\begin{gathered}\int_A t^2=2\Delta^2(a\bar a)^2(s-\bar s)^6=-8d,\\-\int_{E_i^6}(f^*t)^2=8d\deg f=32768d^4N^{12}.\end{gathered}\tag{SR6.4}',
r'\deg f_m=64M^{12},\qquad f_m^*H=2M^2\Theta_S,\qquad B_m=-\tfrac12f_m^*\gamma=-M^2C_2\otimes I_3.\tag{SR6.5}',
r'\begin{gathered}t_m=\frac{c_3}{2}+\left[\frac{128}{3}d^5N^6(1-8d)\right]\Theta_S^3,\\\delta_m=2,\qquad T_m:=-\int_{E_i^6}t_m^2=512dM^{12}=2^{21}d^{13}N^{12}.\end{gathered}\tag{SR6.6}',
]

IM = [
r'Y=C/L,\qquad X=C/H,',
r'u^*(\theta_C|_B)=|L|\,\theta_Y|_P.',
r'\operatorname{Ind}_H^G\chi\longrightarrow K^m,\qquad g\otimes v\longmapsto vge_1.',
r'\operatorname{Hom}_G(\rho,H^1(C,K))=H^1(Y,K)_\chi,',
r'f=\frac1{|H|}\sum_{h\in H}\bigl(\chi(h)^{-1}+\bar\chi(h)^{-1}\bigr)h\in\mathbb Q[G].',
r'A=\sum_{b,c}(\ell_c-1),\qquad R=\#\{(b,c):a_c\ne0\},\qquad S=\sum_{\substack{b,c\\a_c\ne0}}\frac{a_c}{d}.',
r'A+R=2m+2n,\qquad S=R/2.',
r'R=2(n-h+1),\qquad\sum a_c=dR/2.',
r'\sum_b\operatorname{age}(g_b)=A/2+S,\qquad\sum_b\operatorname{age}(g_b^{-1})=A/2+R-S.',
r'-m+A/2+S,\qquad-m+A/2+R-S.',
r'\operatorname{rank}(d\mathcal P)\leq\dim(\operatorname{im}\mathcal P)\leq\min(r-3,h+2n-1)\leq3n.',
r'\sum_jr_j\left(\frac1{x-a_j}-\frac{\zeta}{x-b_j}\right)dx,',
r'p_j(\zeta)=\frac D{x-a_j}-\frac{\zeta D}{x-b_j}-\frac D{x-a_6}+\frac{\zeta D}{x-b_6}.',
r'a_j=(2j)(2j+1)^d,\qquad b_j=2j,\qquad j=1,\ldots,5,',
r'q_j=\frac{\zeta_d}{(2j+1)^e},',
r'\eta^d=\mathcal O_{X_0}\bigl(e[0]+(d-e)[\infty]\bigr).',
r'q_j^{\prime}=\frac{b_j/a_j}{q_j}.',
r'F_j=\left(\frac1{x-a_j}-\frac{q_j}{x-b_j}\right)dx,\qquad j=1,\ldots,5,',
r'\left(\frac D{x-a_i}-\frac{q_iD}{x-b_i}\right)\left(\frac D{x-a_j}-\frac{q_j^{\prime}D}{x-b_j}\right),',
r'H^0(\omega\otimes\eta)\otimes H^0\bigl(\omega\otimes\eta^{-1}(B)\bigr)\longrightarrow H^0\bigl(\omega^2(B)\bigr),',
r'(g_1,g_2,g_3,g_4)=(a,a^{-1},b,b^{-1}).',
r'\begin{aligned}e=d:\quad c^6&=\operatorname{diag}(\zeta^6,1,1,1,1,1,\underbrace{\zeta^{-1},\ldots,\zeta^{-1}}_{6}),\\e<d:\quad c^7&=\operatorname{diag}(\zeta^7,\zeta^{-7},1,1,1,\underbrace{\zeta^{-e},\ldots,\zeta^{-e}}_{7}).\end{aligned}',
r'\begin{gathered}(\dim\operatorname{Fix}(a),\dim\operatorname{Fix}(b))=\begin{cases}(1,6)&e=d,\\(0,7)&e<d,\end{cases}\\n=-12+\operatorname{codim}\operatorname{Fix}(a)+\operatorname{codim}\operatorname{Fix}(b)=5.\end{gathered}',
r'0\longrightarrow H_1(\Gamma,\mathbb Q)\longrightarrow\mathbb Q[G]\longrightarrow\mathbb Q[G/\langle a\rangle]\oplus\mathbb Q[G/\langle b\rangle]\longrightarrow\mathbb Q\longrightarrow0.',
]

# Longest literal match wins.  These substitutions only typeset the notation;
# they do not delete, combine, or reword any source sentence.
MATH = {
'K=Q(zeta_d)':r'K=\mathbb Q(\zeta_d)', 'K=Q(sqrt(-d))':r'K=\mathbb Q(\sqrt{-d})',
'Q(sqrt(-m))':r'\mathbb Q(\sqrt{-m})', 'Q(sqrt(-d))':r'\mathbb Q(\sqrt{-d})',
'Q(zeta_d)':r'\mathbb Q(\zeta_d)', 'Q(i)':r'\mathbb Q(i)',
'G(d,e,m)':r'G(d,e,m)', 'G(d,d,m)':r'G(d,d,m)',
'G(d,e,m)/G(d,d,m)':r'G(d,e,m)/G(d,d,m)',
'rho=Ind_H^G chi':r'\rho=\operatorname{Ind}_H^G\chi',
'Ind_H^G chi=rho':r'\operatorname{Ind}_H^G\chi=\rho',
'chi:H->mu_d':r'\chi:H\to\mu_d', 'L=ker(chi)':r'L=\ker\chi',
'L=ker chi':r'L=\ker\chi', 'chi-bar':r'\bar\chi', 'rho-bar':r'\bar\rho',
'theta_C':r'\theta_C', 'theta_Y':r'\theta_Y', 'theta_prod':r'\theta_{\rm prod}',
'theta_0':r'\theta_0', 'theta_hat':r'\widehat\theta', 'phi_theta':r'\phi_\theta',
'phi_(Ntheta)':r'\phi_{N\theta}', 'Nphi_theta=phi_(Ntheta)':r'N\phi_\theta=\phi_{N\theta}',
'q^*theta=Theta':r'q^*\theta=\Theta', 'q^*q_*Theta=N Theta':r'q^*q_*\Theta=N\Theta',
'[C]*[-C]=2Theta':r'[C]*[-C]=2\Theta', '[C]-2[pt]':r'[C]-2[\mathrm{pt}]',
'ch(O_C)=[C]-2[pt]':r'\operatorname{ch}(\mathcal O_C)=[C]-2[\mathrm{pt}]',
'1-NTheta^2/2+2N[pt]':r'1-N\Theta^2/2+2N[\mathrm{pt}]',
'NS(Z)_Q':r'\operatorname{NS}(Z)_{\mathbb Q}', 'q:J->Z=J/H':r'q:J\to Z=J/H',
'q|C':r'q|_C', 'Cbar':r'\bar C', 'F=I_Cbar':r'F=\mathcal I_{\bar C}',
'Ext^1(F,F)':r'\operatorname{Ext}^1(F,F)', 'Ext^2(F,F)':r'\operatorname{Ext}^2(F,F)',
'Ext^1(F,O_Z)':r'\operatorname{Ext}^1(F,\mathcal O_Z)',
'Hom(F,O_Z)':r'\operatorname{Hom}(F,\mathcal O_Z)',
'Hom(F,O_Cbar)':r'\operatorname{Hom}(F,\mathcal O_{\bar C})',
'Ext^j(E_0,E_0)=0':r'\operatorname{Ext}^j(E_0,E_0)=0',
'H^1(O_Z)->H^1(O_Cbar)':r'H^1(\mathcal O_Z)\to H^1(\mathcal O_{\bar C})',
'H^2(F)=H^2(O_Z)':r'H^2(F)=H^2(\mathcal O_Z)',
'H^2(F)^*':r'H^2(F)^*', 'H^2(F)':r'H^2(F)',
'H^0(N_(Cbar/Z))':r'H^0(N_{\bar C/Z})',
'N_(C/J)':r'N_{C/J}', 'N_(Cbar/Z)':r'N_{\bar C/Z}',
'H^1(T_C)->H^1(O_C)^3':r'H^1(T_C)\to H^1(\mathcal O_C)^3',
'H^0(K_C) tensor H^0(K_C)->H^0(K_C^2)':r'H^0(K_C)\otimes H^0(K_C)\to H^0(K_C^2)',
'K_C=O_C(1)':r'K_C=\mathcal O_C(1)', 'H^0(C,O_C(2))':r'H^0(C,\mathcal O_C(2))',
'H^0(T_Z)':r'H^0(T_Z)', 'H^1(T_Z)':r'H^1(T_Z)', 'H^1(O_Z)':r'H^1(\mathcal O_Z)',
'H^2(O_Z)':r'H^2(\mathcal O_Z)', 'H^2(Omega_Z^1)':r'H^2(\Omega_Z^1)',
'H^3(Omega_Z^1)':r'H^3(\Omega_Z^1)', 'H^0(N)':r'H^0(N)',
'h^0(N)=3':r'h^0(N)=3', 'h^1(N)=3':r'h^1(N)=3',
'sigma_F^j:Ext^j(F,F)->HH_(-j)(Z)':r'\sigma_F^j:\operatorname{Ext}^j(F,F)\to\operatorname{HH}_{-j}(Z)',
'sigma_F^j(x)=tr(exp(at(F))x)':r'\sigma_F^j(x)=\operatorname{tr}(\exp(\operatorname{at}(F))x)',
'sigma_F^1':r'\sigma_F^1', 'sigma_F^2':r'\sigma_F^2',
'sigma_(F^vee)^j':r'\sigma_{F^\vee}^j',
'F external_tensor F^vee':r'F\boxtimes F^\vee', 'F^vee':r'F^\vee',
'ch(F^vee)=1-(N/2)theta^2-(N/3)theta^3':r'\operatorname{ch}(F^\vee)=1-(N/2)\theta^2-(N/3)\theta^3',
'End(F)=C':r'\operatorname{End}(F)=\mathbb C', 'omega_Z=O_Z':r'\omega_Z=\mathcal O_Z',
'td(J)=1':r'\operatorname{td}(J)=1', 'c_1(F)=0':r'c_1(F)=0', 'rank(F)=1':r'\operatorname{rank}(F)=1',
'-(N/2)theta^2':r'-(N/2)\theta^2', 'ch(F)':r'\operatorname{ch}(F)',
'HH_-2 tensor HH_0':r'\operatorname{HH}_{-2}\otimes\operatorname{HH}_0',
'HH_-1 tensor HH_-1':r'\operatorname{HH}_{-1}\otimes\operatorname{HH}_{-1}',
'HH_0 tensor HH_-2':r'\operatorname{HH}_0\otimes\operatorname{HH}_{-2}',
'HH_-2':r'\operatorname{HH}_{-2}', 'HH^2(Z)':r'\operatorname{HH}^2(Z)',
'A=Z times Zhat':r'A=Z\times\widehat Z', 'Z times Zhat':r'Z\times\widehat Z',
'Z times Z':r'Z\times Z', 'C times C':r'C\times C',
'gamma=c_1(Poincare)':r'\gamma=c_1(\mathcal P)', 'phi_theta^*theta_hat=theta':r'\phi_\theta^*\widehat\theta=\theta',
'mu:Z times Z->Z times Z':r'\mu:Z\times Z\to Z\times Z',
'mu(x,y)=(x+y,y)':r'\mu(x,y)=(x+y,y)', 'u=sqrt(-d)':r'u=\sqrt{-d}',
'bar_s':r'\bar s', 'bar_a':r'\bar a', 'Q_bar_s':r'Q_{\bar s}', 'Q_s':r'Q_s',
'u^2=-d':r'u^2=-d', 'N=d+1':r'N=d+1', 'alpha^2=-4d':r'\alpha^2=-4d',
'alpha=s-bar_s=2u':r'\alpha=s-\bar s=2u', 'a bar_a=N/(4d)':r'a\bar a=N/(4d)',
'st=N':r'st=N', 's+t=-2':r's+t=-2', 'H^7=0':r'H^7=0',
'T^2+2T+N=0':r'T^2+2T+N=0', 'T+1':r'T+1', 'sqrt(-d)':r'\sqrt{-d}',
'S=[[N,1],[1,1]]':r'S=\bigl(\begin{smallmatrix}N&1\\1&1\end{smallmatrix}\bigr)',
'S(T+1)=[[0,-d],[d,0]]':r'S(T+1)=\bigl(\begin{smallmatrix}0&-d\\d&0\end{smallmatrix}\bigr)',
'E_i=C/(Z+iZ)':r'E_i=\mathbb C/(\mathbb Z+i\mathbb Z)',
'x^4+y^4+z^4=0':r'x^4+y^4+z^4=0', 'E_i^6':r'E_i^6', 'E_i^3':r'E_i^3',
'h=qj:E_i^3->Z':r'h=qj:E_i^3\to Z', 'r=2L':r'r=2L', 'd=r^2':r'd=r^2',
's=-1+ri':r's=-1+ri', 'diag(i,i,i,-i,-i,-i)':r'\operatorname{diag}(i,i,i,-i,-i,-i)',
'deg(h)=8N':r'\deg h=8N', 'deg(k)=64':r'\deg k=64',
'deg(phi_theta)=Delta^2=N^(-2)':r'\deg\phi_\theta=\Delta^2=N^{-2}',
'deg(R)=Norm(2ri)^3=(4d)^3':r'\deg R=\operatorname{Norm}(2ri)^3=(4d)^3',
'G=ker(f)':r'G=\ker f', 'E_0=f^*E':r'E_0=f^*E',
'f^*:HH_-2(A)->HH_-2(E_i^6)':r'f^*:\operatorname{HH}_{-2}(A)\to\operatorname{HH}_{-2}(E_i^6)',
'Pic^0(Z times Z)=Pic^0(Z) times Pic^0(Z)':r'\operatorname{Pic}^0(Z\times Z)=\operatorname{Pic}^0(Z)\times\operatorname{Pic}^0(Z)',
'B_0=-f^*gamma/2':r'B_0=-f^*\gamma/2', 't_0=f^*t':r't_0=f^*t',
'H_0=f^*H':r'H_0=f^*H', 'H_0=4dN^2 theta_prod':r'H_0=4dN^2\theta_{\rm prod}',
'theta_0=3theta_prod':r'\theta_0=3\theta_{\rm prod}',
'H_0=(4dN^2/3)theta_0':r'H_0=(4dN^2/3)\theta_0',
'H_1(Z,Q)':r'H_1(Z,\mathbb Q)', 'q_H(x,y)=E_H(x,Jy)':r'q_H(x,y)=E_H(x,Jy)',
'q_H(v,v)=c h(v,v)':r'q_H(v,v)=c h(v,v)', 'q_H':r'q_H', 'E_theta':r'E_\theta',
'[[0,-d],[d,0]] tensor E_theta':r'\bigl(\begin{smallmatrix}0&-d\\d&0\end{smallmatrix}\bigr)\otimes E_\theta',
'(-1)^3':r'(-1)^3', '[-1]':r'[-1]',
'3Theta':r'3\Theta', '2Theta':r'2\Theta', 'theta^2':r'\theta^2', 'theta^3':r'\theta^3',
'mu_{d/e}':r'\mu_{d/e}', 'mu_d':r'\mu_d', 'mu_e':r'\mu_e',
'Mat_m(K)':r'\operatorname{Mat}_m(K)', 'K[G]':r'K[G]', 'Q[G]':r'\mathbb Q[G]',
'H^1(C,K)':r'H^1(C,K)', 'H^1(C,K)^L':r'H^1(C,K)^L', 'H^1(Y,K)':r'H^1(Y,K)',
'p:C->Y':r'p:C\to Y', 'p_* p^*=|L|':r'p_*p^*=|L|', 'p_*p^*=[|L|]':r'p_*p^*=[|L|]',
'u:P->B':r'u:P\to B', '|L|^(4n)':r'|L|^{4n}', '|L|^(2 dim P)':r'|L|^{2\dim P}',
'dim P=2n':r'\dim P=2n', 'P[|L|]':r'P[|L|]', 'p^*P':r'p^*P',
'h^dagger=h^(-1)':r'h^\dagger=h^{-1}',
'A+R=2m+2n':r'A+R=2m+2n', 'S=R/2':r'S=R/2',
'h=1-m+A/2':r'h=1-m+A/2', 'R=2(n-h+1)':r'R=2(n-h+1)',
'2h-2=-2m+A':r'2h-2=-2m+A', '2n=2(h-1)+R':r'2n=2(h-1)+R',
'3h-3+R=h+2n-1':r'3h-3+R=h+2n-1', '3h-3+R':r'3h-3+R',
'H^0(omega tensor eta) tensor H^0(omega tensor eta^(-1))->H^0(omega^2)':r'H^0(\omega\otimes\eta)\otimes H^0(\omega\otimes\eta^{-1})\to H^0(\omega^2)',
'H^0(omega tensor eta^(+/-1))':r'H^0(\omega\otimes\eta^{\pm1})',
'H^0(omega^2)':r'H^0(\omega^2)', 'H^0(omega^2(B))':r'H^0(\omega^2(B))',
'H^0(X_0,omega_(X_0)^2)':r'H^0(X_0,\omega_{X_0}^2)',
'H^1(omega^2)=0':r'H^1(\omega^2)=0',
'H^1(omega tensor eta)=H^0(eta^(-1))^*=0':r'H^1(\omega\otimes\eta)=H^0(\eta^{-1})^*=0',
'omega tensor eta':r'\omega\otimes\eta', 'omega tensor M':r'\omega\otimes M',
'omega^2(B)':r'\omega^2(B)', 'eta^(-1)(B)':r'\eta^{-1}(B)',
'O(infinity)':r'\mathcal O(\infty)', 'x^(-1)eta^(-1)':r'x^{-1}\eta^{-1}',
'B=[0]+[infinity]':r'B=[0]+[\infty]', 'M=eta^(-1)(B)':r'M=\eta^{-1}(B)',
'q_j^d=(b_j/a_j)^e':r'q_j^d=(b_j/a_j)^e', 'q_j q\'_j=b_j/a_j':r'q_jq_j^{\prime}=b_j/a_j',
'w^d=x^e':r'w^d=x^e', 'w^(d/e)/x':r'w^{d/e}/x',
'zeta_d^(d/e)':r'\zeta_d^{d/e}', 'q_j^d (a_j/b_j)^e=1':r'q_j^d(a_j/b_j)^e=1',
'H^1(X,T_X(-B))':r'H^1(X,T_X(-B))', 'H^0(X,omega_X^2(B))':r'H^0(X,\omega_X^2(B))',
'x=t^(d/e)':r'x=t^{d/e}', 'H^1(X,Z/d)':r'H^1(X,\mathbb Z/d)',
'Sp_(2h)(Z)':r'\operatorname{Sp}_{2h}(\mathbb Z)', '(Z/d)^(2h)':r'(\mathbb Z/d)^{2h}',
'e(Z/d)^(2h)':r'e(\mathbb Z/d)^{2h}',
'gcd(d,e,v_1,...,v_(2h))=gcd(e,v_1,...,v_(2h))':r'\gcd(d,e,v_1,\ldots,v_{2h})=\gcd(e,v_1,\ldots,v_{2h})',
'f:X->P^1':r'f:X\to\mathbb P^1', 'X->P^1':r'X\to\mathbb P^1',
'Y->X->P^1':r'Y\to X\to\mathbb P^1', 'Y->X':r'Y\to X', 'P^1':r'\mathbb P^1',
'H^1(X,f^*T_(P^1))':r'H^1(X,f^*T_{\mathbb P^1})',
'deg f^*T_(P^1)=2m>2h-2':r'\deg f^*T_{\mathbb P^1}=2m>2h-2',
'f^*T_(P^1)':r'f^*T_{\mathbb P^1}', 'f^*':r'f^*',
'delta_W':r'\delta_W', 'c_t':r'c_t', '[rho]=Ind[chi]':r'[\rho]=\operatorname{Ind}[\chi]',
'Hom_G':r'\operatorname{Hom}_G', 'h^1':r'h^1',
'E\'_0':r'E_0^{\prime}', 'E\'_0=E_0 tensor L_B':r'E_0^{\prime}=E_0\otimes L_B',
'B\'_0=0':r'B_0^{\prime}=0', 'B_0':r'B_0', 'L_B':r'L_B', 'C_2':r'C_2',
'C_2=[[0,1],[1,0]]':r'C_2=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)',
'c=4dN^2':r'c=4dN^2', 'H_0=c theta_prod':r'H_0=c\theta_{\rm prod}',
'h^*theta=2theta_(E_i^3)':r'h^*\theta=2\theta_{E_i^3}',
'ch_1=2H_0':r'\operatorname{ch}_1=2H_0', 'ch_2=0':r'\operatorname{ch}_2=0',
'c_1=2H_0':r'c_1=2H_0', 'c_2=2H_0^2':r'c_2=2H_0^2',
'ch_3=-(2/3)H_0^3+c_3/2':r'\operatorname{ch}_3=-(2/3)H_0^3+c_3/2',
't_0':r't_0', 'H_0':r'H_0', 'T_0':r'T_0', 'Theta_S':r'\Theta_S',
'f_m=Mk:E_i^6->A':r'f_m=Mk:E_i^6\to A', 'M=2dN':r'M=2dN',
't_m=f_m^*t':r't_m=f_m^*t', 'H_m=2M^2 Theta_S':r'H_m=2M^2\Theta_S',
'E_K^6':r'E_K^6', 'B_m':r'B_m', 'f_m':r'f_m', 't_m':r't_m',
'h(x,y)=q_H(x,y)+u E_H(x,y)':r'h(x,y)=q_H(x,y)+uE_H(x,y)',
'h(x,Jy)=u h(x,y)':r'h(x,Jy)=u h(x,y)', 'h(Jx,y)=-u h(x,y)':r'h(Jx,y)=-u h(x,y)',
'h(v,v)=q_H(v,v)':r'h(v,v)=q_H(v,v)', 'J^2=-d':r'J^2=-d',
'V=H_1(Z,Q)':r'V=H_1(Z,\mathbb Q)', 'H_1(A,Q)=V direct_sum V':r'H_1(A,\mathbb Q)=V\oplus V',
'I=L direct_sum L':r'I=L\oplus L', 'S tensor E_theta':r'S\otimes E_\theta',
}

for term, tex in {
'rho':r'\rho','chi':r'\chi','zeta_d':r'\zeta_d','zeta':r'\zeta',
'Theta':r'\Theta','theta':r'\theta','gamma':r'\gamma','eta':r'\eta',
'omega':r'\omega','Delta':r'\Delta','alpha':r'\alpha','Phi':r'\Phi',
'mu':r'\mu','kappa':r'\kappa','infinity':r'\infty','X_0':r'X_0',
'P_m':r'P_m','L_m':r'L_m','N_m':r'N_m','d_m':r'd_m',
}.items(): MATH[term]=tex
for name in 'BCDEFGHJKLMNPRSTVXYZdefghmnpqrstuvxyz':
    MATH.setdefault(name,name)

MATH.update({
'J=J(C)':r'J=J(C)', 'D=C-C':r'D=C-C', 'Cbar=q(C)':r'\bar C=q(C)',
"p-q=p'-q'":r'p-q=p^{\prime}-q^{\prime}',
'J[N]=(Z/N)^6':r'J[N]=(\mathbb Z/N)^6', 'J[N]':r'J[N]', 'J[r]':r'J[r]',
'product(1-a_i)>=1-sum a_i':r'\prod_i(1-a_i)\geq1-\sum_i a_i',
'sum_(n>=2)n^(-6)<1/2':r'\sum_{n\geq2}n^{-6}<1/2',
'phi(q)':r'\varphi(q)', 'q|N':r'q\mid N', '(N/q)v':r'(N/q)v',
'psi(x)=log lcm(1,...,floor(x))':r'\psi(x)=\log\operatorname{lcm}(1,\ldots,\lfloor x\rfloor)',
'psi(2r)-psi(r)<=log binom(2r,r)<=2r log2':r'\psi(2r)-\psi(r)\leq\log\binom{2r}{r}\leq2r\log2',
'log N<=log5+2logL<log5+4Plog2':r'\log N\leq\log5+2\log L<\log5+4P\log2',
'logP=2048log2':r'\log P=2048\log2', 'exp(x)-1<=x/(1-x)':r'\exp(x)-1\leq x/(1-x)',
'N=4mL^2+1':r'N=4mL^2+1', 'd=4mL^2':r'd=4mL^2', 'd=4L^2':r'd=4L^2',
'P=2^2048':r'P=2^{2048}', 'sum_(p|N)1/p<1/500':r'\sum_{p\mid N}1/p<1/500',
'Ext^1(F,F)<=3+3=6':r'\operatorname{Ext}^1(F,F)\leq3+3=6',
'Ext^1(F,O_Z)=H^2(F)^*':r'\operatorname{Ext}^1(F,\mathcal O_Z)=H^2(F)^*',
'0->F->O_Z->O_Cbar->0':r'0\to F\to\mathcal O_Z\to\mathcal O_{\bar C}\to0',
'F->O_Z':r'F\to\mathcal O_Z', 'Ext^2':r'\operatorname{Ext}^2',
'at(F)':r'\operatorname{at}(F)', 'at(F^vee)':r'\operatorname{at}(F^\vee)',
'HH_-1':r'\operatorname{HH}_{-1}', 'HH_0':r'\operatorname{HH}_0',
'H^1(Z)':r'H^1(Z)', 'H^1(Y)':r'H^1(Y)', 'H^1':r'H^1',
'N^12':r'N^{12}', 'Pic^0(Z)':r'\operatorname{Pic}^0(Z)',
'phi_theta:Z->Zhat':r'\phi_\theta:Z\to\widehat Z',
'Q_s=product_(i=1)^3(s a_i-u_i)(s b_i-v_i)':r'Q_s=\prod_{i=1}^3(s a_i-u_i)(s b_i-v_i)',
'theta=sum alpha_i beta_i':r'\theta=\sum_i\alpha_i\beta_i',
'theta_x=sum a_i b_i':r'\theta_x=\sum_i a_i b_i',
'theta_y=sum c_i d_i':r'\theta_y=\sum_i c_i d_i',
'theta_hat=sum u_i v_i':r'\widehat\theta=\sum_i u_i v_i',
'gamma=sum(a_i v_i-b_i u_i)':r'\gamma=\sum_i(a_i v_i-b_i u_i)',
'sum(c_i v_i-d_i u_i)':r'\sum_i(c_i v_i-d_i u_i)',
'theta^3/6=1/N':r'\theta^3/6=1/N',
'f_*/deg(f)':r'f_*/\deg f', 'q_*Theta':r'q_*\Theta',
't_0+P(theta_0)':r't_0+P(\theta_0)', 't_m+2H_m-H_m^3/(12d)+H_m^5/(960d^2)':r't_m+2H_m-H_m^3/(12d)+H_m^5/(960d^2)',
't_g^*(-)':r't_g^*(-)', 't_g^*L_B^(-1)':r't_g^*L_B^{-1}',
't_g':r't_g', 'f_m^*E':r'f_m^*E', '(s-bar_s)^6':r'(s-\bar s)^6',
'2t_0':r'2t_0', '2C_2':r'2C_2', 'I_3':r'I_3', 'E_0':r'E_0', 'E_i':r'E_i',
'E_H(x,y)':r'E_H(x,y)', 'E_H':r'E_H',
'k=diag(h,phi_theta h)':r'k=\operatorname{diag}(h,\phi_\theta h)',
'L_m<P_m':r'L_m<P_m', 'm<P_m':r'm<P_m', 'P_m>=2048log2':r'P_m\geq2048\log2',
'P_m>=2^2048':r'P_m\geq2^{2048}', '2/P_m':r'2/P_m',
'a_i':r'a_i', 'b_i':r'b_i', 'c_i':r'c_i', 'd_i':r'd_i', 'u_i':r'u_i', 'v_i':r'v_i',
'alpha_i':r'\alpha_i', 'beta_i':r'\beta_i',
'(p^*)^*theta_C=|L|theta_Y':r'(p^*)^*\theta_C=|L|\theta_Y',
'Hom_G(rho,V)':r'\operatorname{Hom}_G(\rho,V)',
'diag(zeta_d,zeta_d^(-1),1,...,1)':r'\operatorname{diag}(\zeta_d,\zeta_d^{-1},1,\ldots,1)',
'u=diag(zeta_d^e,1,...,1)':r'u=\operatorname{diag}(\zeta_d^e,1,\ldots,1)',
'p^*p_*=sum_{l in L} l^*':r'p^*p_*=\sum_{l\in L}l^*',
'S_m':r'S_m', 's_i':r's_i', 's_1':r's_1', 's_(m-1)':r's_{m-1}',
'e_1':r'e_1', 'e_j':r'e_j', 'ell_c':r'\ell_c', 'a_c':r'a_c',
'g_b^ell':r'g_b^\ell', 'g_b':r'g_b', 'g_1':r'g_1', 'g_r':r'g_r',
't^ell-zeta_d^a':r't^\ell-\zeta_d^a', 'zeta_d^a':r'\zeta_d^a',
'n^2>3n':r'n^2>3n', 'r-3>=n^2':r'r-3\geq n^2', 'n^2':r'n^2',
'zeta=zeta_d':r'\zeta=\zeta_d', 'zeta^(-1)':r'\zeta^{-1}',
'zeta_d^(-1)':r'\zeta_d^{-1}', 'zeta_3->374':r'\zeta_3\mapsto374',
'zeta_4->469':r'\zeta_4\mapsto469', 'zeta_6->375':r'\zeta_6\mapsto375',
'sum_j(1-zeta)r_j=0':r'\sum_j(1-\zeta)r_j=0',
'D(x)=product_j(x-a_j)(x-b_j)':r'D(x)=\prod_j(x-a_j)(x-b_j)',
'p_i(zeta)p_j(zeta^(-1))':r'p_i(\zeta)p_j(\zeta^{-1})',
'omega_(X_0)':r'\omega_{X_0}', 'F_j-F_6':r'F_j-F_6',
'F_i':r'F_i', 'F_j':r'F_j', "F'_j":r'F_j^{\prime}', "q'_j":r'q_j^{\prime}',
'a_j':r'a_j', 'b_j':r'b_j', 'q_j':r'q_j', 'q_j^d':r'q_j^d',
'F_1009':r'\mathbb F_{1009}', 'x^(-e)':r'x^{-e}',
'X=C/H->P^1':r'X=C/H\to\mathbb P^1',
'p^*':r'p^*', 'p_*':r'p_*', 'D^2':r'D^2', 'xD^2':r'xD^2',
'n^2-dimensional':r'n^2\text{-dimensional}', 'u^(-1)':r'u^{-1}',
'wedge^2<span beta_i>':r'\bigwedge^2\langle\beta_i\rangle',
'span(alpha_i) tensor wedge^3<span beta_i>':r'\langle\alpha_i\rangle\otimes\bigwedge^3\langle\beta_i\rangle',
'G(d,e,12)':r'G(d,e,12)', 'G(d,d,12)':r'G(d,d,12)', 'S_12':r'S_{12}', 'A_12':r'A_{12}', 'A_3':r'A_3',
'a_0':r'a_0','b_0':r'b_0','c=a^(-1)b':r'c=a^{-1}b','c^6':r'c^6','c^7':r'c^7',
'b_0^(-1)a_0b_0a_0^(-1)':r'b_0^{-1}a_0b_0a_0^{-1}', 'a^(-1)':r'a^{-1}', 'b^(-1)':r'b^{-1}',
'D_0':r'D_0', 'mu_(d/e)':r'\mu_{d/e}', 'M_(0,4)':r'M_{0,4}',
'delta_f':r'\delta_f','delta_f^t':r'\delta_f^t', 'zeta^(c_j)':r'\zeta^{c_j}', 'e_(pi(j))':r'e_{\pi(j)}',
'12-dim Fix(a)-dim Fix(b)=5':r'12-\dim\operatorname{Fix}(a)-\dim\operatorname{Fix}(b)=5',
})

# Common simple formulas are safe to typeset automatically, without parsing
# arbitrary prose as mathematics.
for a in ['d','e','h','m','n','r','R','N','P','j','q','t','s','u']:
    for op,top in [('>=',r'\geq'),('<=',r'\leq'),('!=',r'\ne'),('=', '='),('>', '>'),('<', '<')]:
        for b in ['0','1','2','3','4','5','6','9','14','15','163','d','n','n+1','h-1']:
            MATH.setdefault(a+op+b,a+top+' '+b)

keys=sorted(MATH,key=len,reverse=True)
pat=re.compile(r"(?<![A-Za-z0-9_'’-])(?:"+'|'.join(map(re.escape,keys))+r")(?![A-Za-z0-9_'’^-])")
escapes={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','$':r'\$','%':r'\%','&':r'\&','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','<':r'\textless{}','>':r'\textgreater{}'}
def esc(t):
    return ''.join(escapes.get(c,c) for c in t)

def simple_inline(t):
    out=[];pos=0
    for hit in pat.finditer(t):
        out.append(esc(t[pos:hit.start()]));out.append(r'\('+MATH[hit.group()]+r'\)');pos=hit.end()
    out.append(esc(t[pos:]));return ''.join(out)

def inline(t):
    # Only explicit source markup is interpreted.  Single underscores and
    # asterisks in mathematical notation are never Markdown delimiters.
    out=[];pos=0
    for hit in re.finditer(r'`([^`]+)`|\*\*([^*]+)\*\*',t):
        out.append(simple_inline(t[pos:hit.start()]))
        if hit.group(1) is not None: out.append(r'\texttt{'+esc(hit.group(1))+'}')
        else: out.append(r'\textbf{'+inline(hit.group(2))+'}')
        pos=hit.end()
    out.append(simple_inline(t[pos:]));return ''.join(out)

def convert(source, target, displays):
    raw=(ROOT/source).read_text(); lines=raw.splitlines(); out=[]; blocks=[];i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip(): out.append('');i+=1;continue
        if line.startswith('    '):
            b=[]
            while i<len(lines) and lines[i].startswith('    '):b.append(lines[i][4:]);i+=1
            idx=len(blocks);blocks.append('\n'.join(b));assert idx<len(displays)
            out.extend([r'\[',displays[idx],r'\]']);continue
        if line.startswith('#'):
            level=len(line)-len(line.lstrip('#'));title=line[level:].strip()
            cmd={1:'section',2:'subsection',3:'subsubsection'}.get(level,'paragraph')
            out.append('\\'+cmd+'{'+esc(title)+'}')
            m=re.match(r'(D-(?:IM|SR)-[0-9]+G?)\.',title)
            if m:out.append(r'\label{'+m.group(1)+'}')
            i+=1;continue
        if line.startswith('|'):
            table=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',c) for c in cells):table.append(cells)
                i+=1
            out.extend([r'\begin{center}',r'\begin{tabular}{'+('l'+'r'*(len(table[0])-1))+'}',r'\hline'])
            for j,row in enumerate(table):
                out.append(' & '.join(inline(c) for c in row)+r' \\')
                if j==0:out.append(r'\hline')
            out.extend([r'\hline',r'\end{tabular}',r'\end{center}']);continue
        # Preserve each ordinary paragraph, with source line breaks merely
        # converted to spaces (the standard prose meaning of Markdown).
        p=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('    ','#','|')):
            p.append(lines[i]);i+=1
        paragraph=' '.join(p)
        rendered=inline(paragraph)
        citations=[]
        for needle,key in [('Published convention references:','IM-LehrerTaylor,IM-LewisWang'),
                           ('Lange--Ortega','IM-LangeOrtega'),
                           ('Farb--Margalit','IM-FarbMargalit'),
                           ('Write sigma_F^j','SR-BuchweitzFlenner2003,SR-BuchweitzFlenner2008'),
                           ('Beauville,','SR-Beauville2014'),
                           ('Conjugating tensorization','SR-Mukai1981'),
                           ('Perry','SR-Perry2026'),
                           ('Poincare formula','SR-BirkenhakeLange'),
                           ('To prove this, embed J by 3Theta','SR-BauerSzemberg')]:
            if needle in paragraph:citations.append(key)
        if citations:rendered+=r' \cite{'+','.join(citations)+'}'
        out.append(rendered)
    assert len(blocks)==len(displays),(source,len(blocks),len(displays))
    header='% Generated by build_tex_sections.py; full proof text, no abridgement.\n% Requires amsmath, amssymb, and UTF-8 support.\n'
    tex=header+'\n'.join(out)+'\n'
    (ROOT/target).write_text(tex)
    return {'source':source,'target':target,'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'target_sha256':hashlib.sha256(tex.encode()).hexdigest(),'display_count':len(blocks),'source_lines':len(lines),'source_words':len(raw.split()),'output_lines':len(tex.splitlines())}

if __name__=='__main__':
    result=[convert('IMPRIMITIVE_PROOFS.md','imprimitive_section.tex',IM),convert('SEMIREGULAR_CM_PROOFS.md','semiregular_section.tex',SR)]
    (ROOT/'tex_conversion_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
