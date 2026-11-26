# Deposit sheet — not filed

**Title:** Deterministic finite-field constructions after Alpöge, Lenstra, Mumford, and Pila.

**Author line:** Intentionally empty.

**Subject:** Computational algebra and analytic number theory; deterministic finite-field construction and factorization; exact Riemann-hypothesis inputs.

**Keywords:** Dirichlet GRH; Dedekind zeta; Kummer extensions; Teichmüller subgroup; deterministic factorization; finite-field presentations; effective Chebotarev; Frobenius; cubic residue characters; average algorithms.

## Exact manuscript abstract (LaTeX)

```latex
Pila used Frobenius polynomials of abelian varieties to find roots of
unity of fixed prime order in prime fields. Starting from that method
and Mumford's theta equations, and granting Alp\"oge's Dirichlet GRH,
we construct a cubic extension of \(\mathbb F_p\) deterministically
in time polynomial in \(\log p\) whenever \(v_3(p+1)=2\).
More generally, for \(p\equiv-1\pmod9\) we construct an element
of order nine in any presented quadratic extension. Exact CM height
bounds, algebraic recognition, marked good reduction and arithmetic
over the full residue algebra make the construction uniform in \(p\).
The construction extends to every fixed three-adic valuation;
uniformity in that valuation and in general prime degree remains open. We also identify the exact Riemann hypotheses in
eighteen classical algorithmic statements, prove the pure-field
zeta equivalence and Lenstra's prime-degree Teichm\"uller reduction,
and distinguish Tang's polynomial-time interfaces and their separate
zero-free inputs. Montgomery's character-product method and
Cilleruelo's quadratic-value estimates give short auxiliary searches
outside \(O(\sqrt P\log\log P)\) primes in a dyadic interval at
fixed degree. The mathematics and text were produced by GPT-6 Astra
in ChatGPT Pro mode; the ninth-root construction, principal reductions and average theorems received
statement-alone re-proofs by the same model, earlier proofs received
targeted checks by Claude Opus 5.5 at effort high, and no human has
checked this paper.
```

## Main statements in Section 1 (exact LaTeX)

```latex
\begin{theorem}[A cubic construction after Mumford and Pila]\label{thm:dirichlet-ninth-root-cubic}
Assume \(\mathrm A\), rational Dirichlet GRH. There is a uniform
deterministic algorithm which, on input a prime
\(p\equiv-1\pmod9\), computes:
\begin{enumerate}
\item a root \(u\in\mathbb F_p\) of
\(f(X)=X^3-3X+1\);
\item an element \(z\) of exact order \(9\) in
\(\mathbb F_p[W]/(W^2+3)\), or in any given presentation of
\(\mathbb F_{p^2}\).
\end{enumerate}
Its deterministic bit cost is \(O((1+\log p)^{C_*})\), for an
absolute effectively computable constant \(C_*\), independent of
\(p\). If \(v_3(p+1)=2\), it also outputs the explicit monic
irreducible polynomial
\[
                 H(Y)=Y^3-3Y-u\in\mathbb F_p[Y],
\]
and hence a presentation of \(\mathbb F_{p^3}\), within the same
bound. The only zero hypotheses used are for Dirichlet \(L\)-functions.
The auxiliary-prime step uses conductors dividing \(4p\). One may
use the sharper CM-height bound with conductors at most \(9q\),
where \(q=O((1+\log p)^2)\), or the unconditional polynomial
height bound of Proposition~\ref{prop:unconditional-cm-recognition}.
\end{theorem}

\begin{theorem}[Every fixed three-power stratum]\label{thm:kummer-fixed-three-power-stratum}
Fix \(b\ge2\). Under rational Dirichlet GRH, there is an
effective deterministic algorithm which, given a prime
\(p\equiv-1\pmod{3^b}\), constructs an element of exact order
\(3^b\) in any presented quadratic extension of
\(\mathbb F_p\), in bit time
\[
 O_b\bigl((1+\log p)^{C_b}\bigr).
\]
Here \(C_b\) is an effective constant depending on \(b\).
If \(v_3(p+1)=b\), the algorithm also constructs an irreducible
cubic over \(\mathbb F_p\). No uniform bound on \(C_b\)
as \(b\) varies is asserted.
\end{theorem}

\begin{theorem}[The pure-field hypothesis for the classical construction]
\label{thm:kummer}
Let $p$ and $r$ be distinct primes, with $r$ odd, and put
$F=\Q(p^{1/r})$, $K=\Q(\zeta_r)$, and $E=K(p^{1/r})$.
Under $A$, $\RH(\zeta_F)$ and $\RH(\zeta_E)$ are equivalent.
Either assertion implies a prime $\ell\ne p,r$ such that
\[
 \ell\equiv1\pmod r,\qquad p^{(\ell-1)/r}\not\equiv1\pmod\ell,
\]
with $\ell\ll r^2\log^2(rp)$. A completely explicit, less sharp
bound is
\begin{equation}\label{eq:bound}
 \ell\le \left(4r(2r-3)\log r+4(r-1)^2\log p
             +\frac52r(r-1)+5\right)^2.
\end{equation}
Given such a prime, one can construct $\F_{p^r}$ in deterministic time
polynomial in $\ell$ and $\log p$.  Thus the displayed analytic assumption
gives time polynomial in $r$ and $\log p$.
\end{theorem}

\begin{theorem}[Lenstra's Teichm\"uller construction, in prime degree]
\label{thm:teich}
Let $p\ne r$ be primes, with $r$ odd, and set
\[
 s=\ord_r(p),\quad a=v_r(p^s-1),\quad R=r^a,
 \quad D=\F_p[T]/\Phi_r(T),\quad \zeta=T\bmod\Phi_r.
\]
For $b\in\F_r^\times$, let $\rho_b$ be the automorphism
$\rho_b(\zeta)=\zeta^b$, and let $\omega_a(b)$ denote the unique
lift of $b$ modulo $r^a$ whose order divides $r-1$.
The following two inputs are interconvertible, without an analytic
assumption, in deterministic time polynomial in $r$ and $\log p$:
\begin{enumerate}
\item a presentation of $\F_{p^r}$;
\item an element $\eta\in D^\times$ of order $R$ such that
$\rho_b(\eta)=\eta^{\omega_a(b)}$ for every $b\in\F_r^\times$.
\end{enumerate}
If a presentation of $\F_{p^m}$ is given and $r\mid m$, it also
determines such an $\eta$ in time polynomial in $m$ and $\log p$.
\end{theorem}

\begin{theorem}[Nonresidues in a presented extension]
\label{thm:nonresidue}
Let $p$ be prime, let $r$ be a prime divisor of $p-1$, and let a
presentation of $\F_{p^m}$ be given.  Under $A$, an $r$th nonresidue
can be found deterministically in time polynomial in $m$ and $\log p$.
For $r=2$ and even $m$ no analytic assumption is needed.
\end{theorem}

\begin{theorem}[The two polynomial-time interfaces after Tang]
\label{thm:tangfront}
Assume the algebraic prime-field theorem and bit bound of OpenAI
\citep[Theorem~1.2, p.~3; Proposition~10.1, pp.~41--44]{OpenAI2026},
and the uniform Dedekind zero-free theorem of Cureton and Thorner
\citep[Theorem~1.1, p.~3]{CT2026}.
There are deterministic algorithms of polynomial bit complexity for
both of the following tasks:
\begin{enumerate}
\item completely factor a nonzero dense polynomial over a presented
finite field, including its multiplicities;
\item from a binary integer $q>1$ promised to be a prime power,
construct a power-basis presentation of the field of order $q$.
\end{enumerate}
The first interface reduces a degree-$n$ polynomial to at most
$\max(0,n-1)$ split squarefree prime-field queries of degree at most $n$.
For $q=p^m$, the second uses $O(m^2(1+\log_2p))$ prime-field
queries of degree at most $m$ and polynomial additional bit cost.
\end{theorem}

\begin{theorem}[A finite family for quasipolynomial factorization]
\label{thm:quasipoly}
Let a field $\F_{p^m}$ be presented, and let
$0\ne f\in\F_{p^m}[X]$ have degree $d\geq2$.
If $p\leq d$, its complete factorization can be
computed deterministically in polynomial time in
$d$ and $\log(p^m)$.  If $p>d$, put
\[
 \mathcal B=\{r\leq d: r\text{ prime},\quad
 r\nmid(p-1)m,\quad v_r(p^{\ord_r(p)}-1)>1\}.
\]
Under $A$ and RH for $\zeta_{\Q(p^{1/r})}$ for
$r\in\mathcal B$, complete factorization has
deterministic bit complexity
$(d^{\log d}\log(p^m))^{O(1)}$.
Only primes encountered by the algorithm need their
additional zeta hypothesis.  If every prime $r\leq d$
either divides $m$ or satisfies
$v_r(p^{\ord_r(p)}-1)=1$, the latter bound holds
without an analytic assumption.
\end{theorem}

\begin{theorem}[Short auxiliary primes for almost all inputs]\label{thm:fixed-r-almost-all-auxiliary}
Assume A and fix an odd prime $r$.  Let
\[
 C_r>\frac{r-1}{2\log r},\qquad
 B=C_r\log P\log\log P.
\]
For all sufficiently large $P$, depending on $r$ and $C_r$, all but
\[
 O_{r,C_r}\!\left(\sqrt P\log\log P\right)
\]
primes $p\in(P/2,P]$ admit a prime $\ell\le B$, with $\ell\ne p,r$, such that $\ell\equiv1\pmod r$ and $p^{(\ell-1)/r}\not\equiv1\pmod\ell$.
In particular this bounds the exceptions among inputs with $r\nmid p-1$ and $r^2\mid p^{\operatorname{ord}_r(p)}-1$.
For $r=3$ one may take $C_3=1$; the assertion remains asymptotic,
and no explicit numerical threshold for $P$ is asserted here.

On the successful inputs, deterministic enumeration and certification
of such an $\ell$, followed by the established auxiliary-prime
reduction, constructs $\mathbb F_{p^r}$ in time polynomial in
$\log p$ for the fixed $r$ and $C_r$.  An algorithm stopping at the displayed bound
can report failure on the exceptional inputs; the theorem is not an
all-input construction.
\end{theorem}

\begin{theorem}[A logarithmic cubic search for almost all inputs]
\label{thm:almost-all-small-tate}
Assume A.  Fix $C>1/\log3$ and, for sufficiently large $P$, put
\[
 K=\left\lfloor C\log P\right\rfloor.
\]
All but $O_C(\sqrt P\log\log P)$ primes $p\in(P/2,P]$
admit an integer $1\le k\le K$, $k\not\equiv3\pmod p$,
for which
\[
 Y^3-(k+3)Y^2+kY+1
\]
is irreducible over $\mathbb F_p$.  In particular, the same
exception bound holds among the hard cubic inputs
$p\equiv-1\pmod9$.

Testing these $O_C(\log p)$ cubics deterministically constructs
$\mathbb F_{p^3}$ in time polynomial in $\log p$ on the
successful inputs.  The search can report failure on the
exceptional inputs; the assertion is not an all-input parameter
bound.
\end{theorem}

\begin{theorem}[A simultaneous auxiliary table for almost all characteristics]\label{thm:aa-12r}
Assume \(A\), and fix \(a_0>0\). There is an absolute constant \(C_0\)
such that the following holds for all sufficiently large \(P\)
(the threshold may depend on \(a_0\)).
Let \(1\leq D\leq(\log P)^{a_0}\) be an integer.
Except for
\begin{equation}\label{eq:aa-12r-exceptions}
 O\!\left(
       \frac{\sqrt P\,D^3\log^2(PD)}{\log P}
    \right)
\end{equation}
primes \(p\in(P/2,P]\), every prime \(r\leq D\) simultaneously has
a rational prime \(\ell\) satisfying
\begin{equation}\label{eq:aa-12r-aux}
 \ell\leq C_0r^2\log^2(Pr),\qquad
 \ell\equiv1\pmod{12r},\qquad
 p^{(\ell-1)/r}\not\equiv1\pmod\ell.
\end{equation}
All such primes automatically satisfy
\(\ell\notin\{2,3,p,r\}\).
The constants in the \(O\)-bound are absolute; only the lower
threshold for \(P\) depends on \(a_0\).
\end{theorem}

\begin{corollary}[Average polynomial-time interfaces after Tang]\label{cor:aa-finite-field-algorithms}
Assume \(A\) and the purely algebraic auxiliary-prime algorithm
of \citet[Theorem~1.2, p.~3; Proposition~10.1, pp.~41--44]{OpenAI2026}.
For every prime outside the exceptional set in
Theorem~\ref{thm:aa-12r}, a single uniform deterministic procedure
has the following guarantees.
\begin{enumerate}
 \item Over any explicitly presented finite extension of characteristic
 \(p\), it completely factors every nonzero dense polynomial of degree
 \(n\leq D\), with leading coefficient and multiplicities, in time
 polynomial in \(n+1\) and the bit length of the field order.
 \item Given an integer promised to equal \(q=p^m\), with
 \(1\leq m\leq D\), it constructs a presentation of the field of order
 \(q\) in time polynomial in \(\log q\).
\end{enumerate}
The polynomial exponents are absolute and the algorithms do not
receive \(P\) or \(D\) as input. Their running time uses the input degree, not the global degree cutoff.
\end{corollary}
```

```latex
\begin{theorem}[Lenstra's Teichm\"uller construction, in prime degree]
\label{thm:teich}
Let $p\ne r$ be primes, with $r$ odd, and set
\[
 s=\ord_r(p),\quad a=v_r(p^s-1),\quad R=r^a,
 \quad D=\F_p[T]/\Phi_r(T),\quad \zeta=T\bmod\Phi_r.
\]
For $b\in\F_r^\times$, let $\rho_b$ be the automorphism
$\rho_b(\zeta)=\zeta^b$, and let $\omega_a(b)$ denote the unique
lift of $b$ modulo $r^a$ whose order divides $r-1$.
The following two inputs are interconvertible, without an analytic
assumption, in deterministic time polynomial in $r$ and $\log p$:
\begin{enumerate}
\item a presentation of $\F_{p^r}$;
\item an element $\eta\in D^\times$ of order $R$ such that
$\rho_b(\eta)=\eta^{\omega_a(b)}$ for every $b\in\F_r^\times$.
\end{enumerate}
If a presentation of $\F_{p^m}$ is given and $r\mid m$, it also
determines such an $\eta$ in time polynomial in $m$ and $\log p$.
\end{theorem}
```

```latex
\begin{theorem}[Nonresidues in a presented extension]
\label{thm:nonresidue}
Let $p$ be prime, let $r$ be a prime divisor of $p-1$, and let a
presentation of $\F_{p^m}$ be given.  Under $A$, an $r$th nonresidue
can be found deterministically in time polynomial in $m$ and $\log p$.
For $r=2$ and even $m$ no analytic assumption is needed.
\end{theorem}
```

```latex
\begin{theorem}[The two polynomial-time interfaces after Tang]
\label{thm:tangfront}
Assume the algebraic prime-field theorem and bit bound of OpenAI
\citep[Theorem~1.2, p.~3; Proposition~10.1, pp.~41--44]{OpenAI2026},
and the uniform Dedekind zero-free theorem of Cureton and Thorner
\citep[Theorem~1.1, p.~3]{CT2026}.
There are deterministic algorithms of polynomial bit complexity for
both of the following tasks:
\begin{enumerate}
\item completely factor a nonzero dense polynomial over a presented
finite field, including its multiplicities;
\item from a binary integer $q>1$ promised to be a prime power,
construct a power-basis presentation of the field of order $q$.
\end{enumerate}
The first interface reduces a degree-$n$ polynomial to at most
$\max(0,n-1)$ split squarefree prime-field queries of degree at most $n$.
For $q=p^m$, the second uses $O(m^2(1+\log_2p))$ prime-field
queries of degree at most $m$ and polynomial additional bit cost.
\end{theorem}
```

```latex
\begin{theorem}[A finite family for quasipolynomial factorization]
\label{thm:quasipoly}
Let a field $\F_{p^m}$ be presented, and let
$0\ne f\in\F_{p^m}[X]$ have degree $d\geq2$.
If $p\leq d$, its complete factorization can be
computed deterministically in polynomial time in
$d$ and $\log(p^m)$.  If $p>d$, put
\[
 \mathcal B=\{r\leq d: r\text{ prime},\quad
 r\nmid(p-1)m,\quad v_r(p^{\ord_r(p)}-1)>1\}.
\]
Under $A$ and RH for $\zeta_{\Q(p^{1/r})}$ for
$r\in\mathcal B$, complete factorization has
deterministic bit complexity
$(d^{\log d}\log(p^m))^{O(1)}$.
Only primes encountered by the algorithm need their
additional zeta hypothesis.  If every prime $r\leq d$
either divides $m$ or satisfies
$v_r(p^{\ord_r(p)}-1)=1$, the latter bound holds
without an analytic assumption.
\end{theorem}
```

```latex
\begin{theorem}[Short auxiliary primes for almost all inputs]\label{thm:fixed-r-almost-all-auxiliary}
Assume A and fix an odd prime $r$.  Let
\[
 C_r>\frac{r-1}{2\log r},\qquad
 B=C_r\log P\log\log P.
\]
For all sufficiently large $P$, depending on $r$ and $C_r$, all but
\[
 O_{r,C_r}\!\left(\sqrt P\log\log P\right)
\]
primes $p\in(P/2,P]$ admit a prime $\ell\le B$, with $\ell\ne p,r$, such that $\ell\equiv1\pmod r$ and $p^{(\ell-1)/r}\not\equiv1\pmod\ell$.
In particular this bounds the exceptions among inputs with $r\nmid p-1$ and $r^2\mid p^{\operatorname{ord}_r(p)}-1$.
For $r=3$ one may take $C_3=1$; the assertion remains asymptotic,
and no explicit numerical threshold for $P$ is asserted here.

On the successful inputs, deterministic enumeration and certification
of such an $\ell$, followed by the established auxiliary-prime
reduction, constructs $\mathbb F_{p^r}$ in time polynomial in
$\log p$ for the fixed $r$ and $C_r$.  An algorithm stopping at the displayed bound
can report failure on the exceptional inputs; the theorem is not an
all-input construction.
\end{theorem}
```

```latex
\begin{theorem}[A logarithmic cubic search for almost all inputs]
\label{thm:almost-all-small-tate}
Assume A.  Fix $C>1/\log3$ and, for sufficiently large $P$, put
\[
 K=\left\lfloor C\log P\right\rfloor.
\]
All but $O_C(\sqrt P\log\log P)$ primes $p\in(P/2,P]$
admit an integer $1\le k\le K$, $k\not\equiv3\pmod p$,
for which
\[
 Y^3-(k+3)Y^2+kY+1
\]
is irreducible over $\mathbb F_p$.  In particular, the same
exception bound holds among the hard cubic inputs
$p\equiv-1\pmod9$.

Testing these $O_C(\log p)$ cubics deterministically constructs
$\mathbb F_{p^3}$ in time polynomial in $\log p$ on the
successful inputs.  The search can report failure on the
exceptional inputs; the assertion is not an all-input parameter
bound.
\end{theorem}
```

```latex
\begin{theorem}[A simultaneous auxiliary table for almost all characteristics]\label{thm:aa-12r}
Assume \(A\), and fix \(a_0>0\). There is an absolute constant \(C_0\)
such that the following holds for all sufficiently large \(P\)
(the threshold may depend on \(a_0\)).
Let \(1\leq D\leq(\log P)^{a_0}\) be an integer.
Except for
\begin{equation}\label{eq:aa-12r-exceptions}
 O\!\left(
       \frac{\sqrt P\,D^3\log^2(PD)}{\log P}
    \right)
\end{equation}
primes \(p\in(P/2,P]\), every prime \(r\leq D\) simultaneously has
a rational prime \(\ell\) satisfying
\begin{equation}\label{eq:aa-12r-aux}
 \ell\leq C_0r^2\log^2(Pr),\qquad
 \ell\equiv1\pmod{12r},\qquad
 p^{(\ell-1)/r}\not\equiv1\pmod\ell.
\end{equation}
All such primes automatically satisfy
\(\ell\notin\{2,3,p,r\}\).
The constants in the \(O\)-bound are absolute; only the lower
threshold for \(P\) depends on \(a_0\).
\end{theorem}
```

## The eight opening requirements

| Requirement | Exact location |
|---|---|
| Title identifies the problem and whose work it follows | Title: Alpöge, Cilleruelo, Lenstra, Montgomery, Tang |
| Named starting work and check provenance | First and last sentences of the abstract |
| Full main theorems, hypotheses and inputs | Section1: pure-field zeta gate; Teichmüller equivalence; extension nonresidues; Tang interfaces; finite quasipolynomial family; fixed-r average; logarithmic cubic average; simultaneous auxiliary table and algorithm corollary |
| Why the conclusions matter | Section1 opening and explanatory paragraphs following the theorem statements; classical table |
| Exact division of credit | Theorem-adjacent paragraphs with source statements/pages; Cilleruelo product estimate and Montgomery character argument before the average theorems |
| Earlier and neighbouring work | Classical table, Tang/OpenAI/Cureton–Thorner comparison, source-specific elliptic and class-field comparisons |
| Scope and unresolved uniform implication | Section1 distinctions and each average theorem's explicit exception; final Questions section |
| Proof mechanism before formal proofs | Section1 concluding explanation; first paragraph of each body section |

## Exact closing note (LaTeX)

```latex
\paragraph{Method and records.}
The mathematics and text were produced by GPT-6 Astra in ChatGPT Pro mode.
Independent statement-alone re-proofs of the ninth-root construction, principal algebraic reductions and average theorems used the same model; the configured effort was not exposed
in their records. These were not different-model or formal checks.  Earlier project records describe targeted checks
by Claude Opus 5.5 at effort high; those checks concern the earlier
consequences, not Tang's later algorithm.  No human has checked this paper.
Our text is dedicated to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0~1.0}.
The accompanying programs and records are in the
\href{\workbenchurl}{zeta and $L$-functions workbench}; the permanent
record address is \url{\recordurl}.
```

## Authors and works carried

Alpöge supplies the granted rational Dirichlet GRH theorem. Adleman and Lenstra supply the classical Gaussian-period construction, and Lenstra the Teichmüller algorithms. Montgomery supplies the character-product mechanism; Cilleruelo supplies the quadratic-value product estimates used in the logarithmic cubic average. Bach and Sorenson, Murty, and Zaman supply classical prime-bound inputs. Bhargava, Ivanyos, Mittal and Saxena supply factor-count/nonresidue transfers; Ivanyos, Karpinski, Rónyai and Saxena supply the unconditional algebraic factoring interface. Tang supplies the polynomial-time interfaces, using OpenAI's prime-field algebraic theorem and Cureton–Thorner's fixed Dedekind strip. Kazhdan and Patterson supply the representation-theoretic facts used in the local repair. Cohen and Pazuki, Silverman, Hashimoto and Nuida, and the cited class-field authors carry the explicitly identified geometric inputs. Each of the eighteen classical table rows gives its own source and exact scope. This credit list does not authorize contact.

**Filing state:** No public deposit, push, assigned WB number, or author contact. The workbench is prepared for registration. The requested uniform A-only derivation remains open. Both complete reading passes cover the98-page version; the added components have full targeted proof readings. Final delta readings and all-page visual QA remain to be completed.

## Additional technical inputs

Sutherland’s general volcano structure, Bernard and Kučera’s composite-conductor Jacobi identity, Buchmann and Lenstra’s p-maximal-order algorithm, Pila’s fixed-shape Frobenius algorithm, the abelian Colmez formula, Pazuki’s theta-height comparison, the effective estimate of Wei, Kannan–Lenstra–Lovász recognition, A. K. Lenstra’s number-field factorization, and the Shimura–Taniyama formula as developed in Milne are used with exact local citations. Mumford’s fixed theta equations and the marked good-reduction proof now complete the finite-field CM model and addition interface. The growing-parameter complexity remains under investigation.

## CM construction credit and verification update

Pila supplies the fixed-shape Frobenius algorithm and prime-order root-of-unity precedent; Mumford supplies theta moduli, equations and the classical addition mechanism. The paper supplies the stated uniform composition for ninth roots, its explicit cubic endpoint, and the fixed-valuation extension, with exact scope. Serre–Tate, Milne, Colmez, Pazuki, Wei, von Känel–Kret, Kannan–Lenstra–Lovász and algebraic-number algorithms carry the cited interfaces. The ninth-root main theorem has a complete statement-only same-model reproof sealed before author exposure; the stronger fixed-parameter extension is still receiving its separate statement-only review.
