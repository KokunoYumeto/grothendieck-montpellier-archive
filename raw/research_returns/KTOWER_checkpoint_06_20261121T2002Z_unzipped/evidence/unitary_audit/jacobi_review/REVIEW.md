# Independent review: Jacobi two-unit auxiliary fields

Recorded: 2026-11-21 19:49:05 UTC. Reviewer: /root/unitary_audit, GPT-6 Astra Pro. Reasoning effort is not exposed. This is a mathematical and primary-source scope review, not a Lean kernel build.

## Result

**PASS** for the complete main_gate/jacobi_two_unit_fields.tex. Initial whole-proof review:
8a0008048ae4528a0eacf437e0216dedc047cf961d6288675aa5167b235724ed.
The final version was subsequently read in full again, including the restored display closings, exact preprint locator, and added source-scope paragraph. Its final reviewed SHA-256 is
a03b614b8101e3696ad3e6cceef0f0b216af728cf14f9a2e5c742ee5fc3977a1.
These final changes do not alter the mathematics.

I read the entire proof, including both corollaries, and independently checked the mathematical steps below. I also read the exact primary statements and proof passages listed in the source table. The proof gives two auxiliary units in the same odd imaginary quadratic field under its stated rational Bernoulli unit hypothesis. Its displayed infinite residue families remove that extra hypothesis by an ordinary Kummer congruence.

The TypeII corollary really applies to the actual source, through the previously proved KT-AUXILIARY-UNIT-NO-TYPEII. No simultaneous third unit, absence of genuinely rank-three sources, or original strict Selmer vanishing is a conclusion of this review.

## Mathematical checks

### Class-number estimate

The norm form of an integral ideal has integral coefficients and discriminant \(D\). Its oriented isometry up to scale recovers the ideal class: an orientation-preserving similarity of the complex ideal lattices is multiplication by an element of the quadratic field. Thus counting proper form classes bounds the ideal class number in the asserted direction.

Choosing a shortest primitive vector and reducing the cross coefficient gives \(|b|\le a\le c\), hence \(3a^2\le |D|\). For each \(a\), there are at most \(a+1\) odd cross coefficients and at most one corresponding \(c\). This proves
\[
h(D)\le R(R+3)/2\le |D|/6+\sqrt{3|D|}/2.
\]
For \(|D|<4p\) the bound is strictly below \(p\) when \(p>27\). Boundary cases and strict inequalities are correct.

### Half-period specialization

I recomputed the transformation of \(g(\tau,z)=\Phi(\tau,z+1/2)\). For \(\gamma\in\Gamma_0(4)\), combining the modular transformation with the integral elliptic shift \((c/2,(d-1)/2)\) gives precisely
\[
g|_{K,1}\gamma=e(c(d-2)/4)g=g.
\]
The full integral elliptic transformation law is unchanged because its extra factor is \(e(-\lambda)=1\). Rational elliptic translates are holomorphic at the cusps: the transformed indices satisfy
\[
n'=n+r\lambda+\lambda^2,\qquad r'=r+2\lambda,\qquad
4n'-(r')^2=4n-r^2\ge0.
\]
In particular the exponent estimate in the draft supplies the required nonnegative Fourier exponents.

For the matrix \(S\), the direct formula is
\[
g|_{K,1}S=q^{1/4}\zeta\,\Phi(\tau,z+\tau/2).
\]
If all odd-\(r\) coefficients vanished modulo \(p\), the two summands of \(F|S\) would have disjoint \(\zeta\)-parities. Schwagenscheidt's theorem applies with \(N=2,m=1\) and \(p\nmid 2mN\), and therefore forces both summands to vanish, contradicting \(\Phi\not\equiv0\).

The scalar specialization
\[
(\Phi(\tau,0)-\Phi(\tau,1/2))/2=h_1(\tau)\vartheta_1(\tau,0)
\]
has trivial character on \(\Gamma_0(4)\). Its product cannot vanish modulo \(p\): the theta factor starts with \(2q^{1/4}\), which is a unit leading coefficient. The elliptic Sturm bound is \(K\cdot6/12=K/2\). Its constant term vanishes by the Jacobi support condition. Thus the asserted odd-\(r\) unit coefficient exists in the stated range.

### Integral Eisenstein series and heat lift

The scanned Eichler–Zagier definition of \(L_D(s)\) and Theorem 2.1 give exactly the multiplier in (JF.8), with exponents \(b-1\) and \(2b-1\) after substituting \(s=1-b\). The zero-discriminant coefficient of the normalized series is exactly \(\zeta(1-2b)=-B_{2b}/(2b)\).

The elementary Bernoulli-polynomial argument handles the possible \(p\)-factor of a quadratic conductor without an unspoken restriction on \(D\). All \(B_j\), \(j\le b\le p-2\), are \(p\)-integral by the recurrence. If \(p\mid f\), only the \(j=0\) term could have a denominator \(p\). Chinese remaindering makes its numerator divisible by \(p\), unless \(f=p\) and \(b=(p-1)/2\). This is exactly the excluded case. Hence all coefficients of the normalized Jacobi Eisenstein series are \(p\)-integral.

Richter's weight congruence gives filtration \(k=b+1\). The possible weight-zero exception at \(k=p-1\) is excluded by the stated index-one free-module decomposition, which gives \(J_{0,1}=0\). Multiplication by a common denominator prime to \(p\) legitimately reduces the rational bounded-denominator case to the integral statements.

Richter's Proposition 2 then gives nonzero heat reduction of filtration \(K=k+p+1\), because \(2k-1=2b+1\) is not divisible by \(p\). The explicit form (JF.11) has the right weight and index and reduces to the heat series; its coefficients remain \(p\)-integral. The heat coefficient is exactly \((4n-r^2)c_\phi(n,r)\).

### Fundamental discriminant and unit extraction

An odd-\(r\) unit heat coefficient forces \(p\nmid 4n-r^2\) and a unit coefficient of \(\phi\). The support and unit condition give a negative odd discriminant \(D'=r^2-4n\) with
\[
0<|D'|\le2K-1\le4p-1.
\]
Writing \(D'=Du^2\), the fundamental discriminant \(D\) stays odd and prime to \(p\). The integer multiplier in (JF.8), together with the already proved \(p\)-integrality of \(B_{b,\chi_D}/b\), makes that Bernoulli value a unit. The class-number bound gives \(p\nmid h(D)\). The class number formula has only the harmless unit factor \(2/w(D)\) at \(p\ge29\).

The previously proved finite-character reduction (FV.2) then gives the Teichmüller-twisted \(B_1\) unit and transports the result to every positive odd weight in the same residue class. This does not require \(p\) to exceed the transported weight.

### Actual GD and the two automatic families

I checked the literal twelve fields of HeightAndVanishing/Counts.lean, lines 9–22. Odd fundamental \(D\), \(p\nmid D h(D)\), even positive \(e\), and the stated genericity condition give the required clauses at \(N=2,\psi=1\). For eta, an inertia element at a prime dividing \(D\) lies in the residual cyclotomic kernel but not in \(G_E\); such a prime exists and differs from \(p\). No splitting condition at \(p\) is needed.

For \(p\equiv3\pmod4\), the choice \(b=(p+3)/2\) meets all range and parity conditions. Ordinary Kummer gives
\[
B_{p+3}/(p+3)\equiv B_4/4=-1/120\pmod p.
\]
The orders of \(\omega^{1+e}\) and \(\omega^e\) in the first family are respectively \(p-1\) and \((p-1)/2\); the gcd calculations in the draft are correct.

For the TypeII family \(p\equiv7\pmod8\), \(e=(p+1)/4+(p-1)t\) is even, the representative of \(2e+1\) is the same \(b=(p+3)/2\), and \((p-1)\nmid2e\). The actual source exclusion consumes the unit with exponent \(2e\), which is exactly the unit this construction supplies. The proof correctly retains the absence of a claimed exponent-\(e\) unit in this same field.

## Primary-source scope actually checked

| Source | Exact passages read | Application and scope |
|---|---|---|
| Eichler–Zagier, MPIM preprint 1983(8), *On the theory of Jacobi forms I* | Scanned printed p.19a and p.20, PDF pages 24–25, directly viewed as images | Full definition of \(L_D(s)\), general nonfundamental multiplier, Theorem 2.1, convergence/holomorphy and zero-discriminant normalization. The complete 141-page preprint was not read. |
| Richter, Proc. AMS 137 (2009), 869–875 | Equation (3), p.869; index-one decomposition and theta setup, p.871; Proposition 1 and Definition 2, p.872; Proposition 2 and its complete proof, p.873 | Weight congruence, filtration, heat lift. The cited foundational results in Richter's proof are imported; no independent reconstruction of their proofs is claimed. |
| Schwagenscheidt, Research in Number Theory 2:4 (2016) | Theorem 1.2, p.2; normalized Eisenstein discussion, p.3; complete proof of Theorem 1.2, pp.11–12 | Integrality at transformed cusps for \(N=2,m=1\), and the bounded-denominator normalization. The almost-all-primes nonvanishing theorem is not used. |
| Choi–Choie–Kikuta, Acta Arith. 158.2 (2013), 129–139 | Opening elliptic Sturm statement, p.129 | The exact elliptic congruence subgroup/coefficient-field version, with index 6. The genus-two theorem is not used. Sturm's original proof is imported, not reconstructed. |
| Pinned HeightAndVanishing/Counts.lean | Full GD structure, lines 9–22 | Checks all twelve actual source fields, including odd discriminant through the \(N=2\) coprimality clause. |

The checked local source files and their hashes, plus the exact reviewed proof hash, are recorded in the adjacent manifest. The earlier finite-character reduction and actual TypeII exclusion are already checked results; this review verifies their exact hypotheses at the new inputs.

## Limits

There is no evaluated third twisted Bernoulli unit and no assertion that the same field works for both exponents \(e\) and \(2e\). The remaining genuinely rank-three source problem is unchanged. No numerical experiment is being substituted for the uniform proof.
