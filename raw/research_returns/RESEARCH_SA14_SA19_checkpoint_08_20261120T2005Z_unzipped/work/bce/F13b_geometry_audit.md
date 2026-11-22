# Targeted audit of F13b

GPT-6 Astra (OpenAI), delegated `/root/bce`, 20 November 2026.
**PASS**, limited to the geometry and intersection calculation in F13b of
`work/fhi/F_metabelian_log_conductor.tex`. This is not an audit of its
modular representation lemma or the complete new conductor/Betti programme.

Let X0 be the fixed regular resolution over the complete excellent normal
local domain A0, with algebraically closed residue field k. If X1->X0 is
connected finite etale, X1 is regular and connected, hence integral.
Its restriction U1 is a dense connected open. The Stein ring is the
normalization A1 of A0 in the finite extension of fraction fields:
regularity gives normality, and proper birational pushforward to the
normalization identifies the global functions. A1 is finite by excellence.
A finite algebra over a complete local ring is a product of complete local
rings; since A1 is a domain, it is local. Its residue field is finite over k,
hence k. The proper birational map X1->Spec A1 is an isomorphism off the
closed point, and the inverse image D1 of D0 is its reduced SNC exceptional
divisor. Etale pullback preserves regularity, reducedness and the SNC
condition. Thus the negative-definite resolution intersection argument
used in F10 applies on X1 too.

For a component C'_a over C_i, the finite map of smooth proper curves is
etale of degree d_a. Riemann-Hurwitz gives
2g(C'_a)-2=d_a(2g(C_i)-2). Every crossing on C_i is k-rational and has
exactly d_a preimages on C'_a. Distinct components above the same C_i
are disjoint, and each preimage is one crossing with a component above
a different C_j. Hence nu'_a=d_a nu_i, with no omitted ramification or
self-intersection term. It follows that k'_a=d_a k_i.

Etale pullback gives coefficient one along each C'_a. Projection formula
therefore reads (B' f* v)_a=d_a(Bv)_i. Taking v=(-B)^(-1)k yields
(-B') f*v=k', so uniqueness gives (-B')^(-1)k'=f*v. Combining the
already-audited F10 inequality with the nonnegative inverse matrix
therefore bounds the new Swan coefficient by the original t_i.
There is no factor deg(f), and no hypothesis that deg(f) be prime to p.
