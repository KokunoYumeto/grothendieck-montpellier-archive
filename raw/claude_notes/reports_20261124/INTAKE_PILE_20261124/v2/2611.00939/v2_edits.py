# Version 2 edits of the note hexagon:2611.00939 (24 Nov 2026).
# Reads h06b_note_v1_posted.tex (the posted source), writes h06b_note_v2.tex.
# Every replacement must match exactly once; otherwise nothing is written.
import io, sys

SRC = "h06b_note_v1_posted.tex"
DST = "h06b_note_v2.tex"

R = []

# --- header comment, date, remark environment -------------------------------------------------
R.append((r"""% Hexagon note H06b, 23 Nov 2026. CC0 1.0.""",
r"""% hexagon:2611.00939, version 2, 24 Nov 2026 (version 1: 23 Nov 2026). CC0 1.0."""))

R.append((r"""\newtheorem{definition}[theorem]{Definition}""",
r"""\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}"""))

R.append((r"""\date{23 November 2026 \quad CC0 1.0}""",
r"""\date{Version 2, 24 November 2026 \quad CC0 1.0}"""))

# --- Section 1, Credit: Sharifi's theorem in the numbering of arXiv v2 --------------------------
R.append((r"""\cite[Theorem 1.1, p.~2]{Sharifi2002},""",
r"""\cite[Theorem~1, p.~2]{Sharifi2002},"""))

# --- Section 1, Context: Ishii's locators; the sentence of Sharifi 2019 in full, p. 221 ----------
R.append((r"""the present theorem makes no integral statement of that kind. Ishii recalls the regular case and proves the
analogue of Sharifi's theorem for once-punctured elliptic curves with complex multiplication, under an analogue of
the Deligne--Ihara conjecture \cite[Theorem 1.1 and Remark 1.1.1, p.~2]{IshiiKernel2026}. In 2019 Sharifi
described the irregular case as ``a very interesting open question of Anderson and Ihara''
\cite[\S1, p.~222]{Sharifi2019}. We have found no earlier statement of the equality at an irregular prime; searches of the literature and of Hexagon on 23 November 2026
returned none.""",
r"""the present theorem makes no integral statement of that kind. Ishii recalls the regular case
\cite[Theorem 1.1 and Remark 1.1.1, p.~2]{IshiiKernel2026} and proves an analogue of Sharifi's theorem for
once-punctured elliptic curves with complex multiplication, under an analogue of the Deligne--Ihara conjecture
\cite[Theorem~A, p.~2]{IshiiKernel2026}; his statement is recalled in Remark~\ref{rem:ishii}. In 2019 Sharifi
recalled that for regular $p$ the outer action is known to be injective on
$\operatorname{Gal}(\Omega_p/F_\infty)$, which is the equality $\Omega_p^*=\Omega_p$, and described the irregular
case as ``a very interesting open question of Anderson and Ihara'' \cite[\S1, p.~221]{Sharifi2019}. We have found
no earlier statement of the equality at an irregular prime; searches of the literature and of Hexagon on 23
November 2026 returned none."""))

# --- Section 6: label; Sharifi's theorem and lemma in the numbering of arXiv v2 -----------------
R.append((r"""\section{The arithmetic consequence of Greenberg's hypothesis}""",
r"""\section{The arithmetic consequence of Greenberg's hypothesis}\label{sec:arith}"""))

R.append((r"""At $p=3$, Sharifi's Theorem 1.1 and Brown's theorem apply, since $3$ is regular. Hence""",
r"""At $p=3$, Sharifi's theorem \cite[Theorem~1, p.~2]{Sharifi2002} and Brown's theorem apply, since $3$ is
regular. Hence"""))

R.append((r"""is \cite[Lemma~4, p.~3 of arXiv:math/0104116v2]{Sharifi2002}; performing it inside""",
r"""is \cite[Lemma~4, p.~3]{Sharifi2002}; performing it inside"""))

# --- Section 7: the remark on K_{4k}(Z); Section 8: label ---------------------------------------
R.append((r"""corollary. No assertion about an unverified prime is needed for that
finite range.


\section{What remains open}
""",
r"""corollary. No assertion about an unverified prime is needed for that
finite range.

\begin{remark}[The groups $K_{4k}(\mathbb Z)$]\label{rem:ktheory}
Vandiver's conjecture at $p$ can be read in the algebraic $K$-theory of $\mathbb Z$. Let $\omega$ be the
Teichm\"uller character of $\operatorname{Gal}(F_1/\mathbb Q)$. For an odd prime $p$ and an integer $k\ge1$,
\begin{equation}\label{eq:kurihara}
 K_{4k}(\mathbb Z)/p\;\cong\;H^2_{\mathrm{\acute et}}\bigl(\mathbb Z[1/p],\mu_p^{\otimes(2k+1)}\bigr)
 \;\cong\;\bigl(\operatorname{Cl}(F_1)/p\bigr)(\omega^{-2k}),
\end{equation}
where the last group is the part of $\operatorname{Cl}(F_1)/p$ on which $\operatorname{Gal}(F_1/\mathbb Q)$ acts
through $\omega^{-2k}$. The first isomorphism is \cite[Chapter~VI, Corollary~8.3]{WeibelKbook}, which rests on
the norm residue isomorphism theorem. The second is Kummer theory over $\mathbb Z[\mu_p,1/p]$, where the prime
above $p$ is principal and the Brauer group contributes nothing, as in Section~\ref{sec:arith}. Since
$K_{4k}(\mathbb Z)$ is finite, it has no $p$-torsion if and only if the $\omega^{-2k}$-part of
$\operatorname{Cl}(F_1)\{p\}$ vanishes. The characters $\omega^{-2k}$ with $1\le k\le(p-3)/2$ are the nontrivial
even characters, and the part of $\operatorname{Cl}(F_1)\{p\}$ for the trivial character is zero, because the
class group of $\mathbb Q$ is trivial. Vandiver's conjecture at $p$ is the vanishing of the even parts, by the
identification made before this remark. It is therefore equivalent to the absence of $p$-torsion in
$K_{4k}(\mathbb Z)$ for $1\le k\le(p-3)/2$. This is Kurihara's theorem \cite{Kurihara1992}, in the form of
\cite[Chapter~VI, Theorem~10.9]{WeibelKbook}.

Mok and Zheng state that $K_{4m}(\mathbb Z)=0$ for every integer $1\le m\le30$
\cite[Theorem~1]{MokZheng2026}. The cases $m=1$ and $m=2$ are theorems of Rognes and of Dutour Sikiri\'c,
Elbaz-Vincent, Kupers and Martinet. For $3\le m\le30$ their argument uses the computation of Hart, Harvey and Ong
at the odd primes below $2^{31}$ and, at the larger primes, a bound for a Selmer group taken from the Lean files that
accompany Alp\"oge's announcement of November 2026, together with exact computations of Hecke determinants. Their
text was posted on 24 November 2026 and has not been refereed. We have read its statement, its introduction and
its second section, and we have not checked its proof. If their theorem holds, then by \eqref{eq:kurihara} the
$\omega^{-2m}$-part of $\operatorname{Cl}(F_1)\{p\}$ vanishes for $1\le m\le30$ at every odd prime $p$. For
$p\le61$ these are all the parts that Vandiver's conjecture concerns, and the conjecture was already known
there; for larger $p$ they are $30$ of the $(p-3)/2$ such parts. Theorem~\ref{thm:greenberg-kernel} needs the
whole of $X_p^+$ to be finite, so their theorem adds no prime to it, and nothing in this note depends on it.
\end{remark}


\section{What remains open}\label{sec:open}
"""))

# --- Section 8: the remark on Ishii's theorem ----------------------------------------------------
R.append((r"""free integral generators to the filtered group and graded Lie algebra
explicitly in \cite[Sections 1 and 4]{Sharifi2002}.

\section*{Provenance and checks}
""",
r"""free integral generators to the filtered group and graded Lie algebra
explicitly in \cite[Sections 1 and 4]{Sharifi2002}.

\begin{remark}[Elliptic curves with complex multiplication]\label{rem:ishii}
Ishii proves an analogue of Sharifi's theorem for a once-punctured elliptic curve
\cite[Theorem~A, p.~2, which is Theorem~2.14, p.~11]{IshiiKernel2026}. Let $K$ be an imaginary quadratic field
of class number one, $E$ an elliptic curve over $K$ with complex multiplication by the ring of integers of $K$,
with origin $O$, and $X=E\setminus\{O\}$. For $n\ge0$ let $K(p^n)$ be the ray class field of $K$ of conductor
$p^n$. Let $p\ge5$ be a prime that splits in $K$, and assume that
\begin{itemize}
\item[\textup{(1)}] $p$ does not divide the class number of $K(p)$;
\item[\textup{(2)}] exactly two primes of $K(p^2)$ lie above $p$;
\item[\textup{(3)}] his analogue of the Deligne--Ihara conjecture holds
\cite[Conjecture~2.3, p.~6]{IshiiKernel2026}: a graded Lie algebra over $\mathbb Q_p$ attached to the pro-$p$
outer Galois action on the fundamental group of $X$ is freely generated by one element in each degree of an
explicit set of pairs of positive integers.
\end{itemize}
Then the fixed field of the kernel of the pro-$p$ outer Galois representation of $X$ is the compositum of
$K(E[p])$ and the maximal pro-$p$ extension of $K(p)$ unramified outside $p$. Ishii notes that assumption (1)
implies that $p$ is regular \cite[Remark~1.1.2\,(3), p.~3]{IshiiKernel2026}. His theorem is thus the analogue of
the regular case, and its assumption (3) is a conjecture, whereas for the line minus three points the
corresponding statement is Brown's theorem. We have read the introduction of the preprint and the statements of
its second section, and we have not checked its proofs. The present note removes the regularity hypothesis for
the line minus three points by means of theorems on Sharifi's conjecture for the cyclotomic tower. Whether
assumptions (1) and (2) can be weakened in a similar way for $X=E\setminus\{O\}$ is a question that this note
does not examine.
\end{remark}

\section*{Provenance and checks}
"""))

# --- Provenance: who wrote what; the checks without "earlier versions" --------------------------
R.append((r"""The mathematics, and the text of Sections 3 to 8, are the work of GPT-6 Astra (ChatGPT Pro mode), in research
runs of November 2026;""",
r"""The mathematics, and the text of Sections 3 to 8 apart from Remarks \ref{rem:ktheory} and \ref{rem:ishii}, are
the work of GPT-6 Astra (ChatGPT Pro mode), in research runs of November 2026;"""))

R.append((r"""Claude Opus 5.5 at effort high checked every step of Lemma~\ref{lem:persistence} and of the deduction of
$X_p^+=0$ from it in the present text (23 November). In earlier versions of the argument it checked the
separation lemma and the deduction of the theorem at primes satisfying Vandiver's conjecture (21 and 22
November). On 23 November it then checked the present text of Sections 4 to 6 step by step, with""",
r"""Claude Opus 5.5 at effort high checked every step of Lemma~\ref{lem:persistence} and of the deduction of
$X_p^+=0$ from it (23 November). On 21 and 22 November, before this note was written, it had checked the
separation lemma (Lemma~\ref{lem:rational-magnus}) and the deduction of the theorem at primes satisfying
Vandiver's conjecture, in the text that the research run had written by then. On 23 November it then checked
Sections 4 to 6 step by step, in the text of version 1 of this note, with"""))

R.append((r"""own. For this note the editor read the abstracts of \cite{Sharifi2002} and \cite{IshiiKernel2026}; the literature""",
r"""own. For version 1 of this note the editor read the abstracts of \cite{Sharifi2002} and \cite{IshiiKernel2026}; the literature"""))

R.append((r"""\cite[p.~1]{Sharifi2002}, and the sentences on the programme are the editor's summary.

The records of the checks are at the permanent page of this work, WB-0006:
""",
r"""\cite[p.~1]{Sharifi2002}, and the sentences on the programme are the editor's summary.

\paragraph{Version 2 (24 November 2026).}
No statement and no proof of version 1 (23 November 2026) is changed, and the checks described above are checks
of that text. In Sections 3 to 7 the changes are two locators in Section~\ref{sec:arith} and the new
Remark~\ref{rem:ktheory}. All the changes are these.
\begin{itemize}
\item[\textup{(i)}] Sharifi's paper \cite{Sharifi2002} is cited throughout in the numbering of
arXiv:math/0104116v2. Version 1 cited his theorem by its number in the author's version, Theorem~1.1, and his
lemma by its number in the arXiv version.
\item[\textup{(ii)}] The sentence of \cite{Sharifi2019} cited in Section 1 is on p.~221, and the article
occupies pp.~220--227. Version 1 gave p.~222 and pp.~221--228. The quoted words were compared with the source and
are exact.
\item[\textup{(iii)}] The account of the checks no longer speaks of earlier versions of the argument; it says
which text each check read.
\item[\textup{(iv)}] Remarks \ref{rem:ktheory} and \ref{rem:ishii} are new, and the locators for
\cite{IshiiKernel2026} are more precise.
\end{itemize}
Points (i) to (iii) were raised in the review of 23 November and again in a reading of 24 November, both by
Claude Opus 5.5 at effort high. The connection of Vandiver's conjecture with the groups $K_{4k}(\mathbb Z)$ and with
\cite{MokZheng2026} was pointed out by Claude Opus 5.5 at effort max. The editor, Claude Fable 5.2 at effort max,
made the changes and wrote the two remarks with the sources open: \cite{Sharifi2002}, in the arXiv version and in
the author's version, at the theorem and the lemma; \cite{Sharifi2019} at the page; \cite{IshiiKernel2026} at the
statements cited; \cite{MokZheng2026} at its Theorem~1, its introduction and its second section; and
\cite{WeibelKbook} at Theorem~8.2, Corollary~8.3 and Theorem~10.9 of Chapter~VI. The page numbers in (ii) are
the editor's correction.
\cite{Kurihara1992} was not opened. The two remarks report results of others and have had no second reader. No
human has checked version 2.

The records of the checks are at the permanent page of this work, WB-0006:
"""))

# --- Bibliography ---------------------------------------------------------------------------------
R.append((r"""\bibitem{IshiiKernel2026}S.~Ishii, \emph{On the kernels of the pro-$p$ outer Galois representations
associated to once-punctured CM elliptic curves},
arXiv:2312.04196v3, 6 January 2026.
\url{https://arxiv.org/pdf/2312.04196}.
""",
r"""\bibitem{IshiiKernel2026}S.~Ishii, \emph{On the kernels of the pro-$p$ outer Galois representations
associated to once-punctured CM elliptic curves},
arXiv:2312.04196v3, 6 January 2026, 30 pages.
\url{https://arxiv.org/abs/2312.04196v3}.
Locators in that version: Theorem~1.1, Remark~1.1.1 and Theorem~A, p.~2; Remark~1.1.2, p.~3;
Conjecture~2.3, p.~6; Theorem~2.14, p.~11.
"""))

R.append((r"""\url{https://www.jstage.jst.go.jp/article/tmj1949/33/2/33_2_263/_pdf/-char/en}.
""",
r"""\url{https://www.jstage.jst.go.jp/article/tmj1949/33/2/33_2_263/_pdf/-char/en}.

\bibitem{Kurihara1992}M.~Kurihara, \emph{Some remarks on conjectures about cyclotomic fields and
$K$-groups of $\mathbb Z$}, Compositio Math. \textbf{81} (1992), 223--236.
Cited through \cite[Chapter~VI, Theorem~10.9]{WeibelKbook}.
"""))

R.append((r"""Theorem~14.9, Remark~14.10, Example~14.11 and Proposition~14.13,
printed pp.~96--98.
""",
r"""Theorem~14.9, Remark~14.10, Example~14.11 and Proposition~14.13,
printed pp.~96--98.

\bibitem{MokZheng2026}C.~P.~Mok and H.~Zheng, \emph{Vanishing of $K_{4m}(\mathbb Z)$ through degree $120$},
Hexagon 2611.00998, version~1, dated 23 November 2026 and posted 24 November 2026, 12 pages.
\url{https://hexagonmath.org/2611.00998}.
Theorem~1, p.~2; Section~2, pp.~2--3.
"""))

R.append((r"""Proc. Sympos. Pure Math. \textbf{70} (2002), 275--284.
Author's 13-page version: \url{https://www.math.ucla.edu/~sharifi/publ/galstr.pdf};
arXiv:math/0104116v2.
""",
r"""Proc. Sympos. Pure Math. \textbf{70} (2002), 275--284.
arXiv:math/0104116v2, 3 October 2001, 12 pages: \url{https://arxiv.org/abs/math/0104116v2}.
Locators in this note are to that version: Ihara's inclusion, p.~1; Theorem~1, p.~2; Lemma~4, p.~3.
In the author's 13-page version, \url{https://www.math.ucla.edu/~sharifi/publ/galstr.pdf},
the theorem is Theorem~1.1, p.~2, and the lemma is Lemma~2.1, p.~4.
"""))

R.append((r"""\textbf{2120} (2019), 221--228.""",
r"""\textbf{2120} (2019), 220--227."""))

R.append((r"""Theorem~8.2.3, pp.~50--51.
\end{thebibliography}""",
r"""Theorem~8.2.3, pp.~50--51.

\bibitem{WeibelKbook}C.~A.~Weibel, \emph{The $K$-book: an introduction to algebraic $K$-theory},
Graduate Studies in Mathematics \textbf{145}, American Mathematical Society, 2013.
Chapter~VI, Theorem~8.2, Corollary~8.3 and Theorem~10.9, read in the author's online version of that chapter,
pp.~47--48 and 65: \url{https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf}.
\end{thebibliography}"""))

def main():
    s = io.open(SRC, encoding="utf-8", newline="").read()
    crlf = "\r\n" in s
    if crlf:
        s = s.replace("\r\n", "\n")
    bad = 0
    for i, (old, new) in enumerate(R, 1):
        c = s.count(old)
        if c != 1:
            print("replacement %d: found %d times: %r" % (i, c, old[:70]))
            bad += 1
    if bad:
        print("NOTHING WRITTEN")
        return 1
    for old, new in R:
        s = s.replace(old, new)
    if crlf:
        s = s.replace("\n", "\r\n")
    io.open(DST, "w", encoding="utf-8", newline="").write(s)
    print("applied %d replacements; wrote %s (%d bytes)" % (len(R), DST, len(s.encode("utf-8"))))
    return 0

if __name__ == "__main__":
    sys.exit(main())
