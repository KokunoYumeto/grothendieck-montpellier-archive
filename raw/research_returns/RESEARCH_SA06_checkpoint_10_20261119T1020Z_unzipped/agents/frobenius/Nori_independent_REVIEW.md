# Independent audit of C.1i: explicit counterexamples in every non-top range

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/frobenius`.
Date: 2026-11-19.
Reviewed file: `research/agents/cycles/nori_counterexamples.tex`.
Conclusion: **the proof and its numerical hypotheses are valid as written**. No change to the statement or degree choice is required. We did not modify the cycles agent's files.

## Exact primary statements opened

1. Nagel (2002), *Effective bounds for Hodge-theoretic connectivity*, author PDF <https://nagel49.perso.math.cnrs.fr/connect.pdf>, Theorem 3.13, printed p.23. Opened full PDF (`turn683175876view0`), exact theorem (`turn191802653view3`), and independently inspected the rendered primary page `research/agents/cycles/output/nagel-theorem313.png`.
2. Nagel (2004), *Lectures on Nori's connectivity theorem*, author PDF <https://nagel49.perso.math.cnrs.fr/grenoble.pdf>, Theorem 5.11 and following bibliographical paragraph, printed p.35. Opened full PDF (`turn683175876view1`) and exact theorem (`turn546446229view0`). The paragraph explicitly says that the condition that the connectivity parameter be at most n should be added to the 2002 statement. Theorem 6.2 and its proof, printed pp.36–37, were also read (`turn546446229view2`).
3. Nagel (1998), *Effective bounds for Nori's connectivity theorem*, author PDF <https://nagel49.perso.math.cnrs.fr/Nori_CRAS.pdf>, printed p.3, immediately before Theorem 2, states that the regularity constant is one for every smooth quadric (`turn546446229view1`). The same fact is Exercise 5.8 in the 2004 author version, printed p.34 (`turn546446229view0`). The 1998 announcement's sharper condition (C) is not used. Nagel2002 Remark3.14(i), printed p.26, explicitly corrects it (`turn191802653view3`).

These are primary author versions. Their printed pagination is not silently identified with journal pagination. The 2002 theorem works over the smooth-fibre open U of the projectivization of the direct sum of section spaces, exactly the parameter space used in C.1i; it applies to every smooth morphism T→U, without a dimension restriction on T.

## Parameters and inequalities

To avoid the collision between the cycle codimension and Nagel's connectivity parameter, write c for the cycle codimension and b for the latter parameter. We have

- c<n<2c;
- dim Q=2c;
- s=2c−n is a positive integer;
- r=s−1=2c−n−1<n;
- b=n, so b≤n and μ=floor((n+b)/2)=n;
- every degree is D=4c+2;
- m_Q=1.

Nagel's condition (C) is

\[
\sum_{\nu=\min(b,r)}^r d_\nu\ge m_Q+\dim Q-1.
\]

Since r<b, its left side is exactly D and its right side is 2c. Each condition (C_i), for 0≤i≤min(b−1,r)=r, is

\[
\sum_{\nu=i}^rD+(\mu-b+i)D
 = (r-i+1)D+iD=sD
 \ge1+2c+n-i.
\]

The right side is at most 4c, since n≤2c−1. The left side is at least D=4c+2. Thus every inequality has positive margin, including the hypersurface case s=1. No asymptotic choice remains.

The conclusion is relative cohomology vanishing in every degree at most n+b=2n. In the algebraic-equivalence argument, injectivity in degree 2c uses H^{2c}(Q×T,X_T)=0, and surjectivity in degree 2c after base change to the curve family uses H^{2c+1}(Q×C,X_C)=0. Since c≤n−1, both degrees lie within the asserted range. The extra degree needed for surjectivity is present.

## Finite witness, field, and trace

A relation on the geometric generic fibre is finite algebraic data. In characteristic zero, a finite definition-field extension becomes finite étale over a nonempty open of the original smooth parameter space. After further shrinking, the curve family is smooth projective, its degree-zero divisor has degree zero on every connected fibre component, and the Chow equality and any rational-equivalence witnesses hold on total spaces. Both T and the total curve space C are therefore permitted smooth bases for Nagel's theorem.

The cohomological lifting and subsequent pushforward are precisely the mechanism in Nagel2004 Theorem6.2. Proper base change for the curve projection identifies its fibre restriction. The degree-zero divisor has zero class on each fibre curve, so the class of the original ambient cycle vanishes. This is a direct contradiction argument for finite data on the specified geometric generic fibre; no assertion about fields of definition of analytic exceptional loci is needed.

For the stronger Lefschetz-image obstruction, tracing a cycle over a finite extension to the rational function field is legitimate with rational coefficients. All conjugate algebraic-equivalence relations yield the trace relation. The universal common-zero incidence is the projectivization of the kernel of a surjective evaluation map over Q. Its projective-bundle hyperplane class is pulled back from the parameter projective space and becomes zero on the generic fibre. Thus the projective-bundle formula expresses the traced generic cycle as the restriction of an ambient cycle, with the asserted codimension. This step does not assume that an arbitrary geometric generic cycle descends before taking trace.

## Quadric and homological calculations

The two displayed maximal linear spaces meet in a projective (c−1)-plane and are the two components of the indicated linear section, so their sum is h^c. The normal sequence gives self-intersection (1+(-1)^c)/2. Hence, from Z=2[Π_+]−h^c, its square has degree 2(-1)^c. The equal degrees of the two planes imply h cl(Z)=0 because H^{2c+2}(Q) is one-dimensional. The primitive class is therefore nonzero and orthogonal to every h times an ambient codimension-(c−1) class.

On the complete intersection, weak Lefschetz applies in degree 2n−2c<n. The push-pull pairing contains h^s with s≥1 and hence annihilates cl(Z); Poincaré duality gives cl(z)=0. Together with the finite-witness injectivity, this proves the nonzero Griffiths class and the stronger exclusion from L A^{c−1}_{alg}(X).

The persistence assertions use only finite-type spreading and specialization over an algebraically closed base field. A hypothetical new relation after an algebraically closed extension would specialize to one over the original algebraically closed field. They therefore apply also after adjoining the generic hyperplane and under every embedding into C.

## Scope and status

The construction covers exactly every integer pair c<n<2c, beginning at (c,n)=(2,3). In the remaining nonzero high-codimension case c=n, cycles modulo algebraic equivalence are determined by degree on a connected smooth projective variety, and a point of the smooth hyperplane has degree one. Thus the universal dichotomy stated in C.1i follows. Groups with c>n vanish. This review does not claim a positive-characteristic version of Nori's connectivity theorem.
