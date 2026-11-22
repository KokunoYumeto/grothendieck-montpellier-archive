# Independent proof audit: A2Y

20 November 2026. GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run;
effort inherited and not exposed. No priority claim.

**PASS for smooth projective integral X over an algebraically closed field
of characteristic p>0, dimension n>=3, and a smooth very ample divisor Y.**

The finite-p-group reduction and A2V were independently audited earlier.
Together they give a nonzero Frobenius-killed class alpha in
H1(Y,L^-a), where L=O_Y(Y) and a>=1, from any nonzero point kernel.

1. Since dim Y>=2 and L^a is very ample, Bertini supplies a smooth
   connected effective divisor E. Projectivity and connectedness identify
   H0(O_Y) and H0(O_E) with k, and restriction is the identity on scalars.
   The exact sequence for E therefore injects H1(L^-a) into H1(O_Y).
2. The Frobenius square uses multiplication by s on the left and by s^p
   on the right. It commutes on Cech representatives. The right vertical
   map need not be injective. Injectivity of Frobenius on H1(O_Y) and of
   the left vertical map suffices to contradict the nonzero alpha.
3. I independently opened Adrian Langer, On the S-fundamental group
   scheme, Ann. Inst. Fourier 61 (2011), 2077-2119, published PDF
   https://www.numdam.org/item/10.5802/aif.2667.pdf, Section 11 and
   Corollary 11.2, p.2116. The section assumes a smooth W2(k) lifting of
   the variety. The corollary gives H^j(E(-D) tensor Omega^i)=0 for ample
   D, numerically flat E, and i+j<min(p,dim). Set variety=Y, E=O_Y,
   D=aL, i=0, j=1. Every p>=2 and dim Y>=2 satisfies this inequality.
   No lifting of the ample bundle, no lifting of X, and no dim Y<p
   assumption occurs. The source proof iterates its truncated
   Deligne--Illusie inequality to Serre vanishing.

Thus either target hypothesis excludes a point kernel. The remaining
universal A2 gate is strictly smaller: a counterexample requires
noninjective Frobenius on H1(O_Y) and no smooth W2 lifting of Y, in
addition to A2V/A2W. This gives no existence construction.
