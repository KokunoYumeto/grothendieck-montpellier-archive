# Statements for an independent re-proof (ZH3 note, 24 Nov 2026)

Extracted by the main session 329fb1e6 (Claude Opus 5.5 at effort max) from zh3_note.tex, lines 60-119: the setup and the statements of Theorems 1 and 2, nothing of their proofs. Suzuki's paper (arXiv:2610.32704) is the LaTeX file reports_20261122/extended_grand_rh/workshop_inputs/cp24_followup/Suzuki_number_field/screwzzwolf_6.tex (under <local>/Documents).

```latex
\cite{alpoge,lean} gives the Riemann hypothesis: every zero of $\Xi$ is real. Let $\Gamma\subset\R$ be the set of
distinct zeros of $\Xi$ and $m_\gamma$ the multiplicity of $\gamma\in\Gamma$. Since $\Xi$ is even and
$\Xi(0)=\xi(1/2)\ne0$, $\Gamma=-\Gamma$, $m_{-\gamma}=m_\gamma$, $0\notin\Gamma$, and, because $\Xi$ has order one,
$\sigma:=\sum_{\gamma\in\Gamma}m_\gamma\gamma^{-2}<\infty$ \cite[(2.2)]{suzuki}. Whether every $m_\gamma$ equals
one is the simplicity question for the Riemann zeros. It is open. Write
\[
 E(T)=\sum_{0<\gamma\le T}(m_\gamma-1),\qquad
 n(T)=\sum_{0<\gamma\le T}m_\gamma,\qquad
 \gamma_*=\min\{\gamma>0:m_\gamma\ge2\}\in(0,\infty],
\]
the multiplicity excess up to height $T$, the counted number of zeros up to $T$, and the first multiple ordinate
($\gamma_*=\infty$ if there is none).

\paragraph{Suzuki's compressions.}
Weil's quadratic form, $Q(u,v)=\sum_{\gamma\in\Gamma}m_\gamma\widehat u(\gamma)\overline{\widehat v(\gamma)}$ with
$\widehat u(t)=\int u(x)e^{itx}\,dx$, is positive, and its completion is realized by the sampling map
$u\mapsto(\widehat u(\gamma))_{\gamma\in\Gamma}$ in $\Hs=\ell^2(\Gamma,m)$, with norm
$\|c\|^2=\sum_\gamma m_\gamma|c_\gamma|^2$. On $\Hs$, let $C$ be multiplication by $1/\gamma$. Suzuki
\cite[§2.3 and (4.1)]{suzuki} shows that $C$ is a Hilbert--Schmidt operator with one eigenvector for each distinct
ordinate, and that its compressions to the subspaces of test functions supported in $[-a,a]$ converge to $C$ in
Hilbert--Schmidt norm; their positive eigenvalues decrease to $1/\gamma_1>1/\gamma_2>\cdots$ over the distinct
ordinates \cite[Theorem~1.1]{suzuki}. He notes that ``the multiplicities of the zeros are not recovered''
\cite[§1, after Theorem~1.2]{suzuki}.

We use finite-dimensional windows. For $N\ge1$, let $h=2^{-N}$ and let $V_N$ be the space of continuous functions on
$\R$, linear on each interval $[jh,(j+1)h]$, vanishing outside $(-N,N)$, with $\int f=0$. It has dimension
$d_N=2N2^N-2$. Let $P_N$ be the orthogonal projection of $\Hs$ onto the image of $V_N$ under the sampling map, and
$C_N=P_NCP_N$. For $k\ge1$ put
\[
 S_k=-2k\,[z^{2k}]\log\frac{\Xi(z)}{\Xi(0)}=2\sum_{\gamma>0}\frac{m_\gamma}{\gamma^{2k}},\qquad
 D_{N,k}=S_k-\tr C_N^{2k},\qquad H_{N,k}=\Bigl(\frac2{D_{N,k}}\Bigr)^{1/(2k)} .
\]
The middle equality is the Hadamard product (Section~\ref{sec:proof1}). Both terms of $D_{N,k}$ are computable from
arithmetic data: $S_k$ from the Taylor series of $\xi$ at $1/2$, and $\tr C_N^{2k}$ from two $d_N\times d_N$
matrices whose entries are given by the explicit formula with the prime powers below $e^{2N}$
(Section~\ref{sec:arith}).

\begin{theorem}\label{thm:main}
Assume the Riemann hypothesis (a theorem, \cite{alpoge}). For all $N,k\ge1$ and $T>0$,
\[
 D_{N,k}>2\sum_{\gamma>0}\frac{m_\gamma-1}{\gamma^{2k}}\ \ge\ \frac{2E(T)}{T^{2k}} .
\]
For fixed $k$, $D_{N,k}$ decreases in $N$ to $2\sum_{\gamma>0}(m_\gamma-1)\gamma^{-2k}$, and
\[
 \sup_{N,k\ge1}H_{N,k}=\gamma_* .
\]
Consequently, for each $T>0$, every zero with $0<\Im\rho\le T$ is simple if and only if $D_{N,k}<2/T^{2k}$ for some
$N,k\ge1$; and every nontrivial zero of $\zeta$ is simple if and only if $\sup_{N,k}H_{N,k}=\infty$.
\end{theorem}

The test has an integer form. Let $b_j=t_j-t_0$ ($0<|j|<N2^N$), where $t_j$ is the hat function of height one centred
at $jh$ with support $[(j-1)h,(j+1)h]$; these $b_j$ form a basis of $V_N$. Let $G_N$ and $H_N$ be the Hermitian
matrices $(G_N)_{ij}=Q(b_j,b_i)$ and $(H_N)_{ij}=\langle C\,\widehat b_j,\widehat b_i\rangle_{\Hs}$, where
$\widehat b$ denotes the sampling vector, and let $\ind_+$ denote the number of positive eigenvalues.

\begin{theorem}\label{thm:integer}
Assume the Riemann hypothesis. Let $T>0$ with $\Xi(T)\ne0$, and $\iota_N(T)=\ind_+(TH_N-G_N)$. Then $\iota_N(T)$ is
nondecreasing in $N$, at most the number of distinct ordinates in $(0,T]$, and equal to it for all large $N$. Hence
the zeros with $0<\Im\rho\le T$ are all simple if and only if $\iota_N(T)\ge n(T)$ for some $N$.
\end{theorem}
```
