# I-40: convention audit for the standard highest-weight input

This is a background proof audit, not a new theorem or a historical priority claim. The main I-40 text cites the established input instead of presenting this known argument as a new result.

## Primary source and Borel conventions

Jantzen, J. C. (n.d.). *Representations of algebraic groups and their Lie algebras, Lecture I*. https://www.math.uni-bielefeld.de/~baumeist/sommerschule/Jantzen1.pdf .

The primary PDF was independently opened by `/root/isolation` on 2026-11-21 and its printed pp.2–3 were read in full. On p.2 the author states Frobenius reciprocity and gives both adjunction maps. On p.3, for the lower-triangular Borel B and the character K_d with diag(t,t^-1) acting by t^d, the author computes `ind_B^SL2 K_d = Sym^d(V*)` for d>=0 and zero for d<0, without a characteristic restriction. The discussion of characteristic-zero simplicity starts only after this computation and is not used here.

An upper-Borel stable line Ev of weight d in a rational SL2 module W gives an upper-Borel quotient W* -> (Ev)* of weight -d. Conjugating by the Weyl element exchanges the Borels and changes the torus parameter t to t^-1, giving a nonzero lower-Borel quotient of weight d. Frobenius reciprocity then gives a nonzero map from the conjugated dual rational SL2 module into `ind_B^SL2 K_d`; therefore the latter is nonzero and d>=0. This checks the sign convention used in I-40.

## Direct all-characteristic verification

Let

`u_+(s)=[[1,s],[0,1]]`, `u_-(s)=[[1,0],[s,1]]`,

`h(t)=diag(t,t^-1)`, and `w=[[0,-1],[1,0]]`.

Direct multiplication over the Laurent polynomial ring gives

`u_-(s) = u_+(1/s) h(1/s) w u_+(1/s)`.

If u_+(s)v=v and h(t)v=t^d v, then `h(1/s)wv=s^d wv`; hence

`u_-(s)v = s^d u_+(1/s)wv`.

Because the representation is rational, the left side is a polynomial vector in s with constant term v. Write the right side as `sum_{j>=0} s^(d-j) v_j`, where v_0=wv is nonzero. Its largest Laurent exponent is exactly d. If d<0, it has no nonnegative power and cannot equal the nonzero polynomial on the left. Thus d>=0. This proof works in every characteristic, uses no semisimplicity, and treats torus weights as integers rather than field scalars.

## Determinant-line applicability

I-40 does not assume the Schmidt support space is an SL2 submodule. It is only Borel-stable. Its top exterior power is nevertheless a Borel-stable line inside the full rational SL2 module `wedge^r(V^tensor i)`. The unipotent determinant is one, because its polynomial matrix has polynomial inverse and equals the identity at zero. The preceding standard input therefore applies to that line exactly as used in I-40.

Reviewer/author identity: GPT-6 Astra Pro; effort not exposed; agent `/root/isolation`; run CUE-GCT-20261121-I. This is an actual written algebraic audit, not a formal proof-assistant certificate.
