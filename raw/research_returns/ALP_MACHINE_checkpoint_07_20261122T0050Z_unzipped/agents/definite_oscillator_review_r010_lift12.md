# Independent whole-proof reviews: AM-R-010 and ALP-LIFT-12

Reviewer: `/root/definite_oscillator`, GPT-6 Astra Pro,
ALP_MACHINE; inherited reasoning effort not separately exposed.
Completed 21 November 2026, 22:10 UTC.

## AM-R-010: pass for the common-host permitted first-image family

I read the complete `work/research/permitted_family_unramified_host.md`.
The proof passes in its stated first-image scope, with the exact torus
input cost and all other arithmetic costs retained separately.

The source compact-vacuum proof extends from rank-two target to every
even target by an orthogonal sum of integral hyperbolic planes at odd
unramified places. Pan's §6.2 scalar is one for each plane because the
opposite source-action character is trivial. The split comparison,
including the dyadic places, has the same value. The odd source rank
and its other splitting character do not enter this source action.

The original \(\alpha\)-half-orbit remains in one isotropic factor
at each place over 29 after extension to \(E'\). Its denominator
is at most \(29^e\), and a principal congruence of exponent \(e\)
changes it by an integral vector in that same factor. Both relevant
alternating pairings vanish; the trace-one character is trivial at
this odd place. This proves simultaneous fixation of the actual
finite Schwartz span, including the specified theta-group signs.

There are six relative split places over 29. The compact index is
\((28\,29^{e-1})^6\), and the rational subgroup \(\mu_{28}\)
injects modulo 29. The class number-one torus decomposition from
the corrected R009 therefore gives
\[
             h'_M=28^5\,29^{6(e-1)}.
\]
The displayed prime contents \(v_2=10,v_7=5\), and
\(v_{29}=6(e-1)\) are exact. In particular this denominator is
an 11-adic unit.

The finite component supporting the input has no rational root
stabilizer, so every actual infinity weight is permitted. Probability
measure gives that component mass \(1/h'_M\). Character orthogonality
then gives the exact realization and norm formulas for one weight
and for their finite direct sum. The supremum is attained at the real
identity. Stars-and-bars in six total CM degrees gives precisely
\(\binom{D+6}{6}\) for degrees at most \(D\), independently of the
number of target entries. The coordinate substitution has only dyadic
denominators and decomposes into orthogonal isotypic components. It
does not alter the norm of the original Fock vector.

The actual multiplication/translation identity and the factor
\(M^{-d}\) transport the permitted jets with the unchanged period
\(C^{2n}\). The gauge input is correctly restricted to ordinary
products of \(J\); the added \(i\)-action has not changed them
into conjugated-action products. The result does not assert that a
weight summand individually has the combined sharp valuation. It
also keeps the source-input norm distinct from the archimedean norm,
target mass, later Schwartz input, or DP44 determinant gain.

## ALP-LIFT-12: pass for an unrestricted actual second Schwartz input

I read the complete `work/agents/second_definite_lift_nonvanishing.md`.
I also checked the primary source passages listed below. The result
passes in its stated classical theta-lift category, including the
assertion for each particular nonzero first vector. It supplies no
arithmetic bound for the second Schwartz vector or its output.

### First-image temperedness

Gan–Ichino Theorem 4.4(i)(a) and (ii)(b), printed p.14, explicitly
give the almost equal rank parameter
\((\phi_T\chi_V^{-1}\chi_W)\oplus\chi_W\) in every nonzero
case. For the unitary torus input and unitary splitting characters
its Weil image is bounded. Theorem 4.4(iii) gives the irreducibility
of the nonzero big theta lift in this tempered case. Their §2
states the bounded-parameter criterion. At split places, Mínguez
Theorem 1(2), printed p.718, gives the parameter
\(\phi_T^\vee\oplus1\) for \(\mathrm{GL}_1\to\mathrm{GL}_2\);
the additional block has dimension one, so no nonunitary exponents
are introduced. This specific dimension matters. The determinant
twist and contragredient preserve temperedness.

### Finite local occurrence

The target \(I_4\) is hyperbolic at nonsplit unramified finite
places. At the original ramified place, the displayed vectors
\((1,2,b,0)\) and \((0,-b,2,1)\), with \(b^2=-5\), have
both norms and mutual inner product zero and are independent.
The Hensel lift exists with \(b\equiv3\pmod7\). This proves
the hyperbolicity needed for the polarization.

In its Schrödinger model, the identity orbit is the closed set
\(g^*Jg=J\) in \(M_2(L)\). The extension argument for compact
locally constant functions on this closed orbit is valid: compact
open pieces extend to compact open ambient sets, and a finite
disjointification extends any such function. The map to the right
regular representation is therefore a quotient of the whole
oscillator, not merely of an open-orbit submodule. The map (S11)
is right-equivariant by the substitution \(u=gh\), and its image
contains the chosen smooth vector by a compact-open idempotent.
Irreducibility gives a quotient onto every desired representation.

At split places, Mínguez Theorem 1(2) supplies nonzero occurrence
directly for \(n=2\le m=4\), in every residue characteristic.
The proof correctly does not apply the closed-unitary-orbit argument
to an open general-linear orbit.

### Real normalized zeta factor and global formula

I inspected the rendered GQT pages 52 and 54. The theta integral
has \(\overline f\); the doubled Schwartz evaluation is
\(\delta(\phi_1\otimes\overline{\phi_2})(0)
=\langle\phi_1,\phi_2\rangle\); and the local zeta integral
has the complex conjugate of the representation matrix coefficient.
The displayed second splitting character is trivial, so its extra
determinant twist is absent here. The type match from the corrected
DO023 and amended LIFT11 consequently gives
\[
 Z_\infty(1)=\int_{U(2)}
       |\langle\pi(g)a,a\rangle|^2dg
               =\operatorname{vol}(U(2))/(d+1)>0.
\]
This explicit compact calculation avoids the unrestricted real-place
converse that GQT do not claim. Division by the nonzero local
tempered factor retains nonvanishing.

Every unramified finite Satake eigenvalue has absolute value one,
so the standard Euler product at \(3/2\) is absolutely convergent
and nonzero. The finite number of remaining local factors is
nonzero and regular there; the alternative argument using GQT
Theorem 11.4(ii)'s holomorphy and absence of zeros in local factors
is also adequate. This is not a central-value assertion.

The source's dimension is 2, the target's is 4, and the global
Witt index of the positive target is zero. Hence
\(d(n)=2,s_{m,n}=1,r=0\); the lower-tower hypothesis is empty.
GQT Proposition 11.6(i) applies to the finite places, and the
explicit real calculation supplies the other local factors.
Theorem 11.4(ii) gives nonzero global lift for each actual irreducible
cuspidal embedding, with the stated factor 2 and the published
measure normalization. No probability-volume or finite-test-function
cost is suppressed.

### Particular vectors and multiplicity spaces

The common kernel over all actual second Schwartz inputs is closed
and invariant: each scalar theta pairing is continuous on the compact
source quotient, and right translation moves to the Schwartz factor.
A nonzero such kernel in the discrete anisotropic automorphic spectrum
contains an irreducible copy, including a possible copy inside a
multiplicity space. Applying the preceding Rallis formula to that
actual embedding contradicts the definition of the common kernel.
Thus every particular nonzero repaired first vector has a surviving
second input. This argument does not assume multiplicity one.

The transfer to \(E'=\mathbf Q(\zeta_{28})\) is justified by the
separately checked R009/R010 inputs and DO022 finite hyperbolicity;
it does not identify the two original fields. The resulting second
Schwartz function is allowed to be arbitrary. The selected finite
moved family, its integral content and norm, and the literal source
row and terminal identities remain outside this result.

## Primary passages directly checked

- Gan, W. T., & Ichino, A. (2015). *The Gross–Prasad conjecture
  and local theta correspondence*. arXiv:1409.6824. §2.2–2.3,
  boundedness/temperedness; Theorem 4.4(i)–(iii), printed p.14;
  §6.7, printed p.27, the invoked tempered local-factor statement.
- Mínguez, A. (2008). Correspondance de Howe explicite: Paires
  duales de type II. *Annales scientifiques de l'École Normale
  Supérieure, 41*(5), 717–741. Theorem 1, printed p.718, including
  its general-linear parameter paragraph and all-residue-characteristic
  scope. https://www.numdam.org/item/ASENS_2008_4_41_5_717_0.pdf
- Gan, W. T., Qiu, Y., & Takeda, S. (2014). *The regularized
  Siegel–Weil formula (the second term identity) and the Rallis
  inner product formula*. arXiv:1207.4709v3. §11.2–11.3, printed
  p.52; §11.6 and Theorem 11.4, p.54; Proposition 11.6, p.55;
  Theorem 11.7's additional real-place conditions, pp.56–57.
  https://arxiv.org/pdf/1207.4709v3

The review uses these published theorems rather than claiming new
proofs of local Langlands, Howe duality, or the Rallis formula.
No Lean execution or formal verification is claimed.
