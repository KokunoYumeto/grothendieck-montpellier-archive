# Builds version 2 of the HNAM note from the posted version-1 source (../hnam_note.tex).
import io, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "hnam_note.tex"
OUT = HERE / "nullstellensatz_am_half_plane.tex"
t = io.open(SRC, encoding="utf-8").read().replace("\r\n", "\n")

def rep(old, new, count=1):
    global t
    n = t.count(old)
    if n != count:
        raise SystemExit("expected %d occurrence(s), found %d: %r" % (count, n, old[:70]))
    t = t.replace(old, new)

# date
rep(r"\date{24 November 2026}", r"\date{25 November 2026}")

# abstract: the half-plane sentence now carries the two credits
rep(r"Any zero-free half-plane $\Re s>\theta$ with $\theta<1$, common to all Dedekind zeta functions, suffices, for instance $\Re s>31/32$ of Cureton and Thorner; that general statement is Proposition~17.2 of our earlier paper hexagon:2611.00987.",
    r"Any zero-free half-plane $\Re s>\theta$, $\theta<1$, common to all Dedekind zeta functions suffices, for instance $\Re s>31/32$ of Cureton and Thorner: the estimate is then Frei, Sofos and Widmer's effective Chebotarev theorem, as Baldwin and Sivek used it for one polynomial in work on 3-manifold recognition, and the step to $\AM$ is Proposition~17.2 of our paper hexagon:2611.00987.")
rep(r"So HN is in $\AM$ with no hypothesis beyond these theorems. Both are unrefereed preprints",
    r"So HN is in $\AM$ granted Hu's theorem or that of Cureton and Thorner. Both are unrefereed preprints")

# 1.4: who did what
rep(r"""\emph{A fixed half-plane suffices.} That $\Zh\theta$ for one fixed $\theta<1$ gives $\HN\in\AM$, and that the theorem of Cureton and Thorner provides such a $\theta$, is Proposition~17.2 of our paper \cite[p.~59 and Table~1]{N}, which writes out the transfer and an explicit two-message protocol. Theorems~\ref{thmA} and~\ref{thmB}(b) together restate it, with the threshold made explicit.

\emph{New here.} The derivation from Hu's Corollary~9.6, which gives Koiran's estimate itself with exponent $7/8+\varepsilon$ (Propositions~\ref{prop:PIT}(a) and~\ref{prop:K9}); the explicit threshold $x_0$; and Corollary~\ref{corD}, with the place where each source uses GRH. The reductions in Corollary~\ref{corD} belong to their authors.""",
    r"""\emph{The estimates from a half-plane.} Frei, Sofos and Widmer proved in October 2026 that the effective Chebotarev theorem of Lagarias and Odlyzko holds with error term $x^{1-\delta}$ when the Dedekind zeta function concerned has no zero with $\Re s>1-\delta$ \cite[Theorem~1.1, p.~2]{FSW}. Theorem~\ref{thmB}(b) is the case of a trivial extension. From that theorem Baldwin and Sivek proved, in November 2026, that under a zero-free half-plane common to all Dedekind zeta functions an irreducible $f\in\Z[x]$ of degree $d$ has a root modulo a prime of size polynomial in $d$ and $\log\|f\|$ \cite[Theorem~2.1, p.~4]{BS}. This is the estimate that Koiran's proof draws from GRH, for one polynomial. So they replaced GRH by a half-plane in it before our paper \cite{N}, and for another purpose, recognition problems for $3$-manifolds (Section~\ref{sec:context}); they report that Agol was aware of the same \cite[p.~3]{BS}. Nothing in their paper concerns $\HN$ or the class $\AM$.

\emph{From the estimate to $\AM$.} That $\Zh\theta$ for one fixed $\theta<1$ gives $\HN\in\AM$, and that the theorem of Cureton and Thorner provides such a $\theta$, is Proposition~17.2 of our paper \cite[p.~59 and Table~1]{N}, which writes out the transfer and an explicit two-message protocol; its proof derives the estimate it needs from the half-plane directly. Theorem~\ref{thmA} restates it with the threshold made explicit.

\emph{New here.} The explicit threshold $x_0$ in the step from the count of primes to $\HN\in\AM$ (Theorems~\ref{thmA} and~\ref{thm:K8}); the derivation through Hu's Corollary~9.6, which gives Koiran's estimate with exponent $7/8+\varepsilon$ (Propositions~\ref{prop:PIT}(a) and~\ref{prop:K9}); and Corollary~\ref{corD}, with the place where each source uses GRH. The reductions in Corollary~\ref{corD} belong to their authors.""")

# 1.5: label, and the paragraph on 3-manifolds
rep(r"\subsection{Context}", r"\subsection{Context}\label{sec:context}")
rep(r"""We have not examined whether a fixed half-plane implies them; the substitution is made in Koiran's proof directly.
""",
    r"""We have not examined whether a fixed half-plane implies them; the substitution is made in Koiran's proof directly.

\emph{Three-manifold topology.} Kuperberg's proof that knottedness is in $\cl{NP}$ under GRH \cite[Theorem~1.1]{Kup}, and the $\cl{coNP}$ results built on it, among them Zentner's for the recognition of the $3$-sphere \cite[Theorem~11.2]{Zen}, use GRH only to find a prime of polynomial bit length modulo which an irreducible integer polynomial has a root \cite[Theorem~3.2]{Kup}; it is the estimate that Koiran obtains under GRH \cite[p.~2]{BS}. Baldwin and Sivek observed that a zero-free half-plane common to all Dedekind zeta functions is enough for it \cite[Theorem~2.1]{BS}. They concluded that the recognition of the unknot, of the $3$-sphere, of torus knots and of hyperbolic knots, and the hyperbolicity of cusped $3$-manifolds, are in $\cl{coNP}$ modulo such a half-plane \cite[Theorems~1.1 and~1.3]{BS}. They note that the Lean-formalized proof of Cureton and Thorner would make these results unconditional, and they keep them conditional \cite[pp.~2--3]{BS}. They also record that unknot recognition was already in $\cl{coNP}$ with no hypothesis by Lackenby \cite{Lac}, and hyperbolic knot recognition by Haraway and Hoffman \cite[Remark~1.4]{BS}. These results are theirs. Theorem~\ref{thmA}(2) gives such a prime for a whole system, and we claim nothing in topology.
""")

# 1.6: scope
rep(r"Proved here outright: Theorem~\ref{thmB}, where part~(b) rests on the explicit formula and zero count of Lagarias and Odlyzko as quoted in Section~\ref{sec:count}.",
    r"Theorem~\ref{thmB}(a) is a two-line consequence of Hu's corollary, and Theorem~\ref{thmB}(b) is a case of the theorem of Frei, Sofos and Widmer.")

# Proposition 3.1: statement of (b) and its proof now cite Frei-Sofos-Widmer
pat = re.compile(r"In \{\\rm\(b\)\}, for every number field \$K\$ and every \$x\\ge3\$,.*?\\end\{proposition\}", re.S)
new_stmt = r"""In {\rm(b)}, for every number field $K$ and every $x>2$,
\begin{equation}\label{eq:PITtheta}
 \bigl|\pi_K(x)-\Li(x)\bigr|\le c_1\,x^{\theta}\Bigl(\frac{\log d_K}{1-\theta}+n_K\log x\Bigr),
\end{equation}
with the absolute constant $c_1$ of \cite[Theorem~1.1]{FSW}.
\end{proposition}"""
if len(pat.findall(t)) != 1:
    raise SystemExit("statement of Proposition 3.1(b) not found once")
t = pat.sub(lambda m: new_stmt, t)

pat = re.compile(r"\(b\) Write \$n=n_K\$, \$d=d_K\$.*?A second proof of the consequence of \(b\) needed below, by a contour shift for a weighted prime ideal sum, is in \\cite\[proof of Proposition~17\.2\]\{N\}\.", re.S)
new_proof = r"""(b) This is the theorem of Frei, Sofos and Widmer \cite[Theorem~1.1, p.~2]{FSW}. It reads: let $L/K$ be a Galois extension of number fields with group $G$, let $C$ be a conjugacy class of $G$ and $0<\delta\le1/2$, and suppose that $\zeta_L$ has no zero with $\Re s>1-\delta$. Then for $x>2$ the number $\pi_C(x,L/K)$ of prime ideals of $K$ unramified in $L$, of norm at most $x$ and with Frobenius class $C$, satisfies
\[
 \Bigl|\pi_C(x,L/K)-\frac{|C|}{|G|}\Li(x)\Bigr|\le c_1\,\frac{|C|}{|G|}\,x^{1-\delta}\log\bigl(d_L^{1/\delta}x^{n_L}\bigr),
\]
with an effective absolute constant $c_1$. They obtain it by modifying the proof of Lagarias and Odlyzko \cite{LO}, which is the case $\delta=1/2$. Take $L=K$, $C=\{1\}$ and $\delta=1-\theta$; this is \eqref{eq:PITtheta}. For $x>2$ and $\theta<\eta<1$ the bracket in \eqref{eq:PITtheta} is at most $(\log d_K+n_K)\log x/((1-\theta)\log2)$, and $x^\theta\log x\le x^\eta/(e(\eta-\theta))$; at $x=2$ trivially $|\pi_K(2)-\Li(2)|\le n_K$. This is $\Ph\eta$.
\end{proof}

A proof of the consequence of (b) needed below that does not pass through \cite{FSW}, by a contour shift for a weighted prime ideal sum, is in \cite[proof of Proposition~17.2]{N}."""
if len(pat.findall(t)) != 1:
    raise SystemExit("proof of Proposition 3.1(b) not found once")
t = pat.sub(lambda m: new_proof, t)

# Remark 3.3: Baldwin-Sivek at Proposition 3.2
rep(r"The paper \cite[\S17]{N} makes the same point and avoids the term by passing to an integral primitive element.",
    r"The paper \cite[\S17]{N} makes the same point and avoids the term by passing to an integral primitive element. For a monic $f$, the prime ideal estimate under a half-plane, and from it a prime of size polynomial in the degree and in the logarithm of the coefficients modulo which $f$ has a root, were obtained before by Baldwin and Sivek \cite[Corollary~3.3 and Theorem~2.1]{BS}, who reduce a polynomial that is not monic to a monic one \cite[\S5]{BS}. For a single polynomial, Proposition~\ref{prop:K9} with the bound for the discriminant in the proof of Theorem~\ref{thm:K8} gives their Theorem~2.1 again.")

# note on method
old_m = re.compile(r"with two exceptions: \\cite\{LO\} is used as quoted in \\cite\{Roj\} and \\cite\{OAIF\}, and \\cite\{BHZ\} as quoted in \\cite\{PR25\}\. Claude Opus 5\.5 at effort high then checked this text, recomputing every constant of Sections~\\ref\{sec:count\} and~\\ref\{sec:proofA\} and reading the sources at the cited places, with the same two exceptions\.")
new_m = r"with these exceptions: \cite{LO}, \cite{BHZ} and \cite{Lac} were not opened and are cited as \cite{FSW}, \cite{PR25} and \cite{BS} describe them. Claude Opus 5.5 at effort high then checked the text, recomputing every constant of Sections~\ref{sec:count} and~\ref{sec:proofA} and reading the sources at the cited places, with the same exceptions; it also found the papers \cite{FSW} and \cite{BS}, which Claude Fable 5.2 at effort max then read at the cited statements."
if len(old_m.findall(t)) != 1:
    raise SystemExit("method sentence not found once")
t = old_m.sub(lambda m: new_m, t)

# bibliography
def bib_before(key, entry):
    global t
    marker = "\\bibitem{%s}" % key
    if t.count(marker) != 1:
        raise SystemExit("bibitem %s not found once" % key)
    t = t.replace(marker, entry + "\n" + marker)

bib_before("CT", r"\bibitem{BS} J.~A.~Baldwin and S.~Sivek, \emph{3-manifold decision problems and Riemann hypotheses}, arXiv:2611.06705v1 (4 November 2026), Theorem~1.1 (p.~1), Hypothesis~1.2 and Theorem~1.3 (p.~2), pp.~2--3, Remark~1.4 (p.~3), Theorem~2.1 (p.~4), Theorem~3.1 and Corollary~3.3 (p.~7), \S5.")
bib_before("Hu", r"\bibitem{FSW} C.~Frei, E.~Sofos and M.~Widmer, \emph{Some applications of the quasi-Riemann hypothesis to class groups and small generators of number fields}, arXiv:2610.18491v2 (14 October 2026; first version 13 October 2026), Theorem~1.1 (p.~2).")
bib_before("LO", r"\bibitem{Kup} G.~Kuperberg, \emph{Knottedness is in NP, modulo GRH}, Adv.\ Math.\ \textbf{256} (2014), 493--506; arXiv:1112.0845, Theorems~1.1 and~3.2." + "\n" +
           r"\bibitem{Lac} M.~Lackenby, \emph{The efficient certification of knottedness and Thurston norm}, Adv.\ Math.\ \textbf{387} (2021), Paper No.~107796; arXiv:1604.00290.")
# LO and Rojas: locators that are no longer used go
m = re.search(r"\\bibitem\{LO\}[^\n]*\n", t)
if not m or "409--464" not in m.group(0):
    raise SystemExit("LO entry not as expected")
t = t.replace(m.group(0), r"\bibitem{LO} J.~C.~Lagarias and A.~M.~Odlyzko, \emph{Effective versions of the Chebotarev density theorem}, in Algebraic Number Fields (Durham, 1975), Academic Press, 1977, 409--464." + "\n")
m = re.search(r"\\bibitem\{OAIF\}[^\n]*\n", t)
if not m:
    raise SystemExit("OAIF entry not found")
t = t.replace(m.group(0), "")
m = re.search(r"\\bibitem\{Roj\}[^\n]*\n", t)
if not m or "Theorem~5 (p.~7)" not in m.group(0):
    raise SystemExit("Rojas entry not as expected")
t = t.replace(m.group(0), m.group(0).replace(", Theorem~5 (p.~7)", ""))
t = t.replace(r"\end{thebibliography}", r"\bibitem{Zen} R.~Zentner, \emph{Integer homology $3$-spheres admit irreducible representations in $\mathrm{SL}(2,\mathbb C)$}, Duke Math.\ J.\ \textbf{167} (2018), no.~9, 1643--1712; arXiv:1605.08530v4, Theorem~11.2." + "\n" + r"\end{thebibliography}")

for bad in ("eq:LO", "eq:count", "OAIF"):
    if bad in t:
        raise SystemExit("left over: " + bad)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(t)
a = t.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0].strip()
print("written", OUT.name, "abstract chars:", len(a))
