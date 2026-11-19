from pathlib import Path
p=Path('SA08_work/sections/C_part.tex')
s=p.read_text()
start=s.index('\\begin{theorem}[C07:')
end=s.index('This counterexample does not refute',start)
s=s[:start]+r'''\begin{theorem}[C07: \status{Refuted}; strict equalization, scan~121(b)]\label{sa08:C07}
For every nonzero commutative ring $k$, the claim that every parallel
pair between admissible generalized PD de Rham theories can be
equalized by an admissible common source is false. It fails even
when both theories are special and tensor-universally flasque.
\end{theorem}
\begin{proof}
Let $S=k\{T\}$ and $F=\mathrm{DR}(\Phi,T)$ be the standard theory,
where $\Phi_n=k^{n+1}$. Put
\[
 W=\Phi\amalg_k\Phi,\qquad V=\Phi\otimes_k W,
 \qquad B=\mathrm{DR}(V,T\otimes T).
\]
The map $j:W\to V$, $w\mapsto T\otimes w$, is split in each
simplicial degree, using evaluation at any chosen vertex in the first
factor. All its terms and cokernels are free. The module $V$ is
acyclic: the first factor $\Phi$ is contractible and flat, so
Eilenberg--Zilber, or the tensor of its simplicial contraction with
the constant identity homotopy of $W$, proves the claim. Also
$V/k(T\otimes T)$ is flat, since the marked vector is unimodular
in every degree. Statement~\ref{sa08:C05} and the relative
Poincare argument in Statement~\ref{sa08:C06} show that $B$ is
special and tensor-universally flasque.

The map $j$ induces a monomorphism
\[
 F\otimes_S F=\mathrm{DR}(W,T)\lhook\joinrel\longrightarrow B.
\]
To verify injectivity over arbitrary $k$, split $j$ degreewise and
split off its common marked line. Divided powers and exterior
powers of the resulting inclusions into direct sums are injective,
by their direct-sum decompositions. Let $i_1,i_2:F\to B$ be the
two inclusions through $F\otimes_S F$.

In each simplicial degree, $F_n$ is free over $S$ on divided-power
and exterior monomials, including $1$. Comparison of the tensor
basis proves that $a\otimes1=1\otimes a$ holds exactly for $a\in S$.
The injection above therefore implies
\[
 \operatorname{Eq}(i_1,i_2)=S
\]
in simplicial bigraded differential algebras. If $h:H\to F$ from
an admissible theory equalized the pair, it would factor through the
constant coefficient algebra $S$. Its map on positive exterior-degree
cohomology after sections over any $X$ would consequently be zero.
But a morphism of admissible theories preserves the augmentation
and the two comparison arrows of scans~113--115, and hence induces
the ordinary-cohomology isomorphism after the shadow functor.
Taking $X=\Delta[1]/\partial\Delta[1]$, whose degree-one cohomology
is $k\ne0$, gives a contradiction.
\end{proof}

'''+s[end:]
p.write_text(s)
p=Path('SA08_work/notes/C_findings.md')
s=p.read_text()
start=s.index('## C07.')
end=s.index('## C08.',start)
s=s[:start]+'''## C07. Strict equalization conjecture121(b): false over every nonzero ring

This strengthens the initially discovered rational example. Let k be any nonzero commutative ring, S=k{T}, and F=DR(Phi,T) the standard theory. Set W=Phi amalg_k Phi, V=Phi tensor_k W, and B=DR(V,T tensor T). The natural map j:W->V sends w to T tensor w and is split in each simplicial degree (evaluate the first factor at a vertex). All terms and cokernels are free. V is simplicially acyclic because Phi is contractible and flat; its quotient by the marked line is flat. Thus B is special and tensor-universally flasque by C05 and the relative PD Poincare argument.

The induced map DR(W,T)=F tensor_S F -> B is injective: split the underlying module inclusion and its marked line degreewise; divided and exterior powers of an inclusion into a direct sum are injective. Therefore the two inclusions i1,i2:F->B have equalizer S. The latter assertion follows by writing F_n as a free S-module on divided-power/exterior monomials including1 and comparing the basis a tensor1 versus1 tensor a.

Any admissible H->F equalizing the two maps would factor through constant S. On sections over X=Delta[1]/boundary, that factorization kills degree-one cohomology. But every morphism between admissible theories induces the canonical ordinary-cohomology isomorphism in the shadow category, by the augmentation comparison diagram. H^1(X;k)=k is nonzero. Contradiction.

Thus121(b) is false in every nonzero coefficient ring, even in the special universally flasque category whose localization is a point by C06. This explicitly shows that strict common-source equalization is not equivalent to localization being connected and simply connected.

The earlier rational construction used B0=F tensor_S F directly. Its admissibility over Q was checked via Gamma^r(W) acyclic for r>=2, since N(W) is an identity disk plus k[1]. The new embedding B0->DR(Phi tensor W) removes the rational hypothesis and strengthens the counterexample. The earlier method is retained here only as a documented successful intermediate approach.

'''+s[end:]
p.write_text(s)
print('Strengthened C07 to all rings')
