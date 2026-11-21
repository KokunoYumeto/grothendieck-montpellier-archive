# Quarantined source audit: binary degree twelve

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Status: **unresolved and unused as a theorem**. Root explicitly instructed that the asserted degree-ten necessity must not be promoted until the issue below is resolved. No contribution to the main paper relies on it.

## Candidate and the part that was checked

Brouwer's author-maintained Poincaré-series page gives a positive rational form for binary order twelve with denominator weights `(2,4,5,5,6,6,7,8,9,11)`, then says that every homogeneous system of parameters must contain a degree divisible by ten, so that form cannot come from a parameter system. Source: <https://aeb.win.tue.nl/math/poincare.html>, Note paragraph, own refs `turn709571862view1` and fresh `turn705885009view1`, lines47–51.

The positive numerator has degree fifty. Its coefficients from degree zero through twenty-five are

`1,0,0,1,1,0,3,5,7,11,21,25,40,55,75,96,130,156,194,228,267,294,330,345,364,365`,

and the remaining coefficients are obtained by palindrome symmetry. An exact integer Cayley–Sylvester dynamic-programming calculation earlier in this run computed invariant dimensions through ordinary degree62. Multiplication by the displayed denominator reproduced precisely those numerator coefficients and zero coefficients in degrees51–62 (tool chunk `b3f0df`). That calculation was a finite arithmetic check of the displayed Hilbert expression, not a proof of the asserted h.s.o.p. obstruction.

The standard rational denominator in BDP Proposition4.1/Dixmier's formula for order12 differs from the displayed denominator by the factor `Phi_6`; its degree is61, whereas the displayed product has degree63. A global-quasipolynomial properness argument can therefore turn the finite coefficient verification into the rational identity. None of this supplies the missing parameter-degree necessity.

## Precise issue in the proposed necessity proof

BDP, *The degrees of a system of parameters of the ring of invariants of a binary form*, Transformation Groups20(2015),953–967, Theorem3.4(ii), printed p955, states for every integer `t>1` that at least `floor((n−1)/t)` h.s.o.p. degrees are divisible by `t` when the binary order `n` is even. The statement at `(n,t)=(12,10)` would give the claimed degree-ten necessity. Exact primary PDF: <https://pure.tue.nl/ws/files/17749340/Degrees2015.pdf>. Own refs `turn438638339view0`, image check `turn135559743view0`, and fresh full relevant passage `turn705885009view0`.

The preceding Lemma3.3(ii) instead chooses the least `j` with `gcd(n/2−j,t)=1` and gives `floor((n−j)/t)`. At `(12,10)`, this least `j` is3, and the lemma only yields zero. In the printed attempt to improve the bound, one writes `n=a*t+b` and replaces the condition on `gcd(n−2*i,2*t)` by a condition on `gcd(b−2*i,2*t)`. Subtracting `a*t` is not valid modulo `2*t` when `a` is odd. The concrete values `a=1,b=2,i=0` give

`gcd(n−2*i,2*t)=gcd(12,20)=4`,

but

`gcd(b−2*i,2*t)=gcd(2,20)=2`.

Thus that inference does not establish the theorem at the needed input. I verified the printed statement visually as well as through text extraction: there is no printed prime-power restriction on `t` that would remove this example. This identifies a gap in the cited argument, **not a proved counterexample to the theorem itself**.

Root also observed that the simplest semistable binary12 eigenform argument does not force primitive order ten: pairs of supported exponents at distance ten are `(0,10),(1,11),(2,12)`, and their relevant scalar orders are5,2,5. Derksen's universal denominator has no primitive-tenth factor. However, absence of that universal factor is not on its own a proof that an h.s.o.p. avoiding multiples of ten exists: the universal-denominator gcd characterization allows finite generating collections for Noether subalgebras, not necessarily a minimal parameter collection. This distinction is preserved.

## Consequence for the project

The binary12 example was withdrawn from the proposed positive-Hilbert-form-versus-canonical-parameter argument pending a sound necessity proof or a documented correction. It is neither cited as established nor announced as a refuted published theorem. The independently checked BDP Proposition4.2 coefficient-zero classification used in P-F25 has its own proof and does not depend on this necessity argument. The project's actual transfer counterexamples P-F21/P-F22 and the connected-semisimple example in P-F20 do not depend on this source issue.


## Resolution after the quarantined stage: P-F43

The earlier statements above describe the evidence available at that stage and are preserved as history. P-F43 now supplies a complete counterexample to the literal degree-ten necessity, including the explicit ten-entry degree sequence and four whole-proof readings. B12-Q1 is therefore refuted. The small sequence on Brouwer's page remains unproved here. No inference from universal-denominator absence was used.
