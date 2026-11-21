# Consequences and criteria under the adopted RH and Dirichlet GRH

Research module `consequences_criteria`. Author/checker: GPT-6 Astra Pro; effort setting not exposed. Date: 20 November 2026 UTC. The mathematical input is the RH and Dirichlet-GRH return adopted by the task. This module does not claim an independent proof or a kernel check of that return. Known conditional results are used with their actual hypotheses; an implication asserted here is relative to the adopted input, and hence has no remaining RH condition within the task's adopted theory.

The propositions labelled CC-F are deductions and counterexamples established in this run; no claim of historical priority or exhaustive novelty is made.

The main distinction is between **theorems whose hypotheses are now discharged**, **equivalent criteria whose asserted positivity or approximation now follows**, and **additional geometric or statistical structures that an equivalence does not supply**. An input-scope obstruction does not establish logical independence: it identifies the extra hypothesis in the available theorem and prevents an unjustified application of that theorem.

## 1. Highest-priority outcomes

| ID | Outcome | Exact operative source | What is discharged or remains |
|---|---|---|---|
| CC-F01 | Every smooth proper Borger \(\Lambda\)-scheme over \(\mathbb Z[1/M]\) has cohomological Dirichlet-completed factors satisfying RH on their weight-shifted lines | Borger (2009), Theorem 0.1, p. 3; Theorem 5.3, p. 17; Corollary 6.2 and (6.2.1), p. 20 | Dirichlet GRH suffices. This is a statement about realizations and their \(L\)-data; no Chow-motive decomposition or cycle-surjectivity assertion is inferred |
| CC-F01b | The rational compactly supported cohomology of every separated finite-type \(\Lambda\)-scheme over \(\mathbb Z\) actually splits into finite abelian characters and Tate twists | Borger (2009), §6 setup and Corollary 6.2, equation (6.2.1), followed by the weight-space descent proved here | No torsion-freeness hypothesis or semisimplification is inserted. Dirichlet GRH supplies the resulting primitive factors; bad-fiber model zeta functions require separate treatment |
| CC-C01 | Effective Chebotarev with the Lagarias–Odlyzko error term for \(L/K\) whenever the top field \(L/\mathbb Q\) is abelian | Lagarias–Odlyzko (1977), Theorem 1.1, equation (1.3) | Their exact analytic hypothesis is RH for \(\zeta_L\), discharged by Dirichlet factorization. Merely assuming \(L/K\) abelian does not do this |
| CC-C02 | A prime in every reduced class \(a\pmod q\), \(q>3\), below \((\varphi(q)\log q)^2\) | Lamzouri–Li–Soundararajan (LLS), corrected arXiv v3 (2016), Corollary 1.2, p. 3 | Dirichlet GRH suffices; a representative for every class supports finite character tests, including higher-rank semisimple representations |
| CC-F02 | Siegel's lower bound for primitive real Dirichlet \(L(1,\chi)\) has a computable constant for every positive rational exponent | LLS, Theorem 1.5, pp. 3–4, plus the full effective deduction below | Dirichlet GRH suffices. This is the analytic Siegel theorem; it is not an asserted effective integral-point theorem |
| CC-F03 | The Hilbert-class-field hypothesis is a real scope boundary even for an imaginary quadratic base | Explicit splitting field of \(x^3-x-1\), proved below | The required ideal-class-character \(L\)-function can be an irreducible degree-two Artin \(L\)-function over \(\mathbb Q\), outside Dirichlet factorization |
| CC-P01–CC-P04 | Weil positivity, Li positivity, the strong Nyman–Beurling approximation, and the bare spectral realization all hold in their precise senses | Exact locators in §4 | Stronger constructions, support ranges, approximation asymptotics, and geometric functoriality are separate questions |
| CC-P07 | The concrete de Branges sufficient positivity conditions analyzed by Conrey–Li are false and remain false | Conrey–Li (2000), §§3.1–3.2 and §4 Remark | A sufficient condition is not automatically an equivalent criterion. RH does not imply these conditions |

## 2. The Borger bridge, with a full proof

### CC-F01. Smooth proper \(\Lambda\)-cohomology satisfies its shifted analytic RH

**Statement.** Let \(X\) be smooth and proper over \(\mathbb Z[1/M]\), of finite type, and equipped with a \(\Lambda\)-structure in Borger's sense. Fix a prime \(\ell\), an algebraic closure \(\overline{\mathbb Q}_\ell\), and an identification of the algebraic roots of unity in it with complex roots of unity. Put
\[
 V^j=H^j_{\mathrm{\acute et}}(X_{\overline{\mathbb Q}},\mathbb Q_\ell).
\]
Then \(V^{2m+1}=0\), and there is a finite family of primitive Dirichlet characters, counted with nonnegative integer multiplicities \(r_{m,\chi}\), such that
\[
 V^{2m}\otimes\overline{\mathbb Q}_\ell
 \simeq\bigoplus_\chi(\chi_\ell\otimes\overline{\mathbb Q}_\ell(-m))^{\oplus r_{m,\chi}}.
 \tag{CC-F01.1}
\]
The convention for \(\chi_\ell\) is that its value on geometric Frobenius at an unramified prime \(p\) is \(\chi(p)\). Define the primitive Dirichlet completion of the cohomological factor by
\[
 L^{\mathrm{Dir}}_{2m}(X,s)=\prod_\chi L(s-m,\chi)^{r_{m,\chi}}.
 \tag{CC-F01.2}
\]
Every nontrivial zero of this factor lies on \(\Re s=m+\tfrac12\). The product has a pole at \(s=m+1\) of order precisely \(r_{m,1}\) and has no other poles. The corresponding completed factors have the usual gamma and conductor factors of these primitive Dirichlet characters. At all sufficiently good primes, (CC-F01.2) has exactly the cohomological Euler factor of \(X\).

If \(S\) contains \(\ell\), the bad primes of \(X\), and every character conductor prime, then the incomplete factor satisfies the exact identity
\[
 L^S_{2m}(X,s)
 =L^{\mathrm{Dir}}_{2m}(X,s)
   \prod_{p\in S}\prod_\chi
       (1-\chi(p)p^{m-s})^{r_{m,\chi}},
 \tag{CC-F01.3}
\]
where a primitive character is assigned value zero at a prime dividing its conductor. The explicitly deleted Euler factors can introduce zeros on \(\Re s=m\). They are excluded from the nontrivial-zero assertion. It would be incorrect to assert that every zero of an incomplete Euler product lies on the shifted critical line.

**Proof.** Borger's Theorem 0.1(c) says that the Hodge decomposition of \(H^j(X(\mathbb C),\mathbb C)\) has no components of type \((a,b)\) with \(a\ne b\). Smoothness and properness give purity of this Hodge structure of weight \(j\); its nonzero components therefore satisfy \(a+b=j\). Consequently odd cohomology vanishes. Comparison with étale cohomology proves \(V^{2m+1}=0\).

Borger's Corollary 6.2, equation (6.2.1), supplies a cyclotomic field \(F=\mathbb Q(\zeta_N)\) over which the representation is a sum of Tate twists, with multiplicities the diagonal Hodge numbers. In degree \(2m\) the only possible Hodge type is \((m,m)\). Therefore
\[
 V^{2m}|_{G_F}\simeq\mathbb Q_\ell(-m)^{b_{2m}}.
\]
The twist \(W_m=V^{2m}(m)\) is thus trivial on \(G_F\) and factors through the finite abelian group \(\mathrm{Gal}(F/\mathbb Q)\). Characteristic-zero representations of a finite group are semisimple, by averaging a projection over the group. Every irreducible representation of a finite abelian group over an algebraically closed field is one-dimensional: a common eigenspace of the commuting operators is invariant, and irreducibility forces it to be the whole space. It follows that \(W_m\) splits into finite-order characters. Characters of \(\mathrm{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)\) are Dirichlet characters; replacing an imprimitive character by its primitive character changes the modulus description, not the Galois character. This proves (CC-F01.1).

On \(\mathbb Q_\ell(-m)\), geometric Frobenius has eigenvalue \(p^m\). Hence the good-prime determinant is
\[
 \det(1-\mathrm{Frob}_p p^{-s}\mid V^{2m})
   =\prod_\chi(1-\chi(p)p^{m-s})^{r_{m,\chi}}.
\]
Its inverse is the Euler factor of (CC-F01.2). Euler products agree in a right half-plane of absolute convergence, and their analytic continuations consequently agree wherever defined. Removing the finitely many factors in \(S\) gives (CC-F01.3).

By the adopted Dirichlet GRH, every nontrivial zero of \(L(s-m,\chi)\) has real part \(m+1/2\). A finite product with nonnegative multiplicities has no other nontrivial zeros. Only the primitive trivial character contributes a pole, and it contributes \(\zeta(s-m)\). At \(s=m+1\), all nonprincipal Dirichlet factors are nonzero by the classical nonvanishing of \(L(1,\chi)\); thus the pole order is exactly \(r_{m,1}\). Finally, if \(\chi(p)\ne0\), it is a root of unity, so \(1-\chi(p)p^{m-s}=0\) implies \(p^{m-\Re s}=1\), or \(\Re s=m\). If \(\chi(p)=0\), the factor is identically one. This proves every assertion. \(\square\)

**Scope and significance.** This supplies analytic RH to an entire geometric class identified inside the supplied \(\mathbf F_1\) literature. The argument proves a decomposition of realizations and their Dirichlet-completed \(L\)-functions. It does not identify a Chow motive with a direct sum of Artin–Tate Chow motives, prove a Hodge or Tate cycle map surjective, or construct the infinite-dimensional cohomology envisaged in Borger's introduction, p. 3. Borger's Theorem 6.1 applies much more generally to separated finite-type \(\Lambda\)-schemes; Corollary 6.2 gives their rational compactly supported cohomology after cyclotomic restriction. For arbitrary mixed objects one must separately control the actual extensions and bad-prime inertia. CC-F01b proves that Borger’s particular rational cohomology class actually splits, so no such extension is being silently discarded there; its asserted arithmetic-model comparison is restricted to good-prime data.

### CC-F01b. Actual rational splitting for every separated finite-type \(\Lambda\)-scheme

**Statement.** Let \(X\) be a separated \(\Lambda\)-scheme of finite type over \(\mathbb Z\), let \(n\ge0\), and let \(\ell\) be prime. For
\[
 V=H^n_{\mathrm{\acute et},c}(X_{\overline{\mathbb Q}},\mathbb Q_\ell),
\]
there is an actual isomorphism, after extension of coefficient field,
\[
 V\otimes\overline{\mathbb Q}_\ell
 \simeq\bigoplus_{m,\chi}
 (\chi_\ell\otimes\overline{\mathbb Q}_\ell(-m))^{\oplus r_{m,n,\chi}}.
 \tag{CC-F01b.1}
\]
The characters have finite abelian image, the multiplicities are nonnegative integers, and only finitely many occur. In particular this rational representation is semisimple. This assertion is about cohomology with \(\mathbb Q_\ell\) coefficients: it does not assume that integral or finite-coefficient cohomology is torsion-free, and asserts neither integral splitting nor absence of torsion. The primitive completion of its good-prime \(L\)-data is
\[
 L_n^{\mathrm{Dir}}(X,s)=\prod_{m,\chi}L(s-m,\chi)^{r_{m,n,\chi}},
 \tag{CC-F01b.2}
\]
whose nontrivial zeros lie on the lines \(\Re s=m+1/2\) for the weights present. Deleted Euler factors are explicit finite products and can add zeros on \(\Re s=m\). For a nonproper or singular model, no equality with the zeta function of its bad fibers is asserted.

**Proof.** In the setup of Borger §6, \(X\) is exactly a separated finite-type \(\Lambda\)-scheme over \(\mathbb Z\). Corollary 6.2, p. 20, equation (6.2.1), gives an isomorphism of the actual representation
\[
 V|_H\simeq\bigoplus_m\mathbb Q_\ell(-m)^{r_{m,n}},
 \qquad H=G_{\mathbb Q(\zeta_N)}.
\]
The source does not insert a semisimplification superscript here. Let \(\epsilon_\ell:G_\mathbb Q\to\mathbb Z_\ell^\times\) be the arithmetic cyclotomic character, so that \(\mathbb Q_\ell(-m)\) carries \(\epsilon_\ell^{-m}\). Its restriction to \(H\) has infinite image: \(H\) has finite index in \(G_\mathbb Q\), while the image of the full cyclotomic character is infinite, and the image of a finite-index subgroup has finite index in that image. The powers \(\epsilon_\ell^{-m}|_H\) are distinct for distinct integers \(m\), since the torsion subgroup of \(\mathbb Z_\ell^\times\) is finite.

Define the corresponding isotypic subspace
\[
 V_m=\{v\in V:\rho(h)v=\epsilon_\ell(h)^{-m}v\text{ for every }h\in H\}.
\]
The given direct-sum decomposition gives \(V=\bigoplus_m V_m\). Since \(H\) is normal and \(\epsilon_\ell\) is a character of the whole group, for \(g\in G_\mathbb Q\), \(h\in H\), and \(v\in V_m\),
\[
 \rho(h)\rho(g)v
 =\rho(g)\rho(g^{-1}hg)v
 =\epsilon_\ell(g^{-1}hg)^{-m}\rho(g)v
 =\epsilon_\ell(h)^{-m}\rho(g)v.
\]
Thus every \(V_m\) is \(G_\mathbb Q\)-stable. The twist \(V_m(m)\) is trivial on \(H\), hence factors through the finite abelian quotient \(G_\mathbb Q/H\). By characteristic-zero semisimplicity and the character decomposition of a finite abelian group, it splits over \(\overline{\mathbb Q}_\ell\) into one-dimensional finite-order characters. Undoing the twists proves (CC-F01b.1). The determinant computation and primitive-character identification in CC-F01 apply to every summand and give (CC-F01b.2) at good primes. The adopted Dirichlet GRH and the same elementary computation of zeros of deleted Euler factors prove the analytic assertions. No passage through a nonsplit extension or an exactness claim for inertia invariants occurs. \(\square\)

The nontrivial zero contributions in (CC-F01b.2) cannot be canceled by poles of other factors: their real parts are half-integers, whereas the only possible poles occur at the integers \(m+1\). Trivial zeros and possible cancellation among trivial zeros and poles are separate from this assertion. The importance of this refinement is that Borger's actual rational splitting eliminates an extension obstruction inside this specific geometric class. General mixed Artin–Tate objects outside this class can still have nontrivial extensions. Borger's Remark 6.3 explicitly cautions against an integral-coefficient analogue.

### CC-F01a. The hexagonal CM curve does not itself furnish Borger's finite-type descent

Borger (2009), §2.9, pp. 10–11, proves that a connected smooth proper curve of genus at least one over \(\mathbb Q\), with a smooth proper model over some \(\mathbb Z[1/M]\), has no \(\Lambda\)-structure. In particular the genus-one CM curve with hexagonal period lattice in the adopted note cannot be identified with a smooth proper \(\Lambda\)-scheme over \(\mathbb Z[1/M]\). CM endomorphisms at split primes do not supply the commuting Frobenius lifts at all good primes required in Borger's definition. This refutes that particular identification; it does not refute the note's use of a CM curve or its separate reference to \(\mathbf F_1\).

## 3. Classical consequences and exact hypothesis map

### CC-C01. Lagarias–Odlyzko for abelian top fields

For a finite Galois extension \(L/K\), let \(G=\mathrm{Gal}(L/K)\), let \(C\) be a conjugacy class, let \(\pi_C(x,L/K)\) count unramified prime ideals of \(K\) of norm at most \(x\) with Frobenius in \(C\), and let \(n_L=[L:\mathbb Q]\), \(\Delta_L=|\mathrm{disc}(L)|\). Lagarias and Odlyzko (1977), Theorem 1.1, equation (1.3), require **RH for \(\zeta_L\)** and conclude, for \(x>2\),
\[
 \left|\pi_C(x,L/K)-\frac{|C|}{|G|}\operatorname{Li}(x)\right|
 \le c_1\left\{\frac{|C|}{|G|}\sqrt{x}\log(\Delta_Lx^{n_L})+\log\Delta_L\right\},
\]
with an absolute effectively computable \(c_1\). The inspected witness is the full retypeset primary text, Theorem 1.1 on its p. 4; the original article occupies pp. 409–464. Their Corollary 1.2 gives an effective least-prime norm bound \(c_2(\log\Delta_L)^2(\log\log\Delta_L)^4\); later sharpenings should not be silently substituted for this displayed corollary.

If \(L/\mathbb Q\) is abelian, its Dedekind zeta function is a product of primitive Dirichlet \(L\)-functions, including \(\zeta\); the adopted statements therefore discharge the analytic hypothesis. Any intermediate \(K\) is allowed. If only \(L/K\) is abelian, this factorization into Dirichlet \(L\)-functions over \(\mathbb Q\) is unavailable in general. For unrestricted \(L\), the missing input is RH for that top-field Dedekind zeta function, not Artin holomorphy as an additional hypothesis of Theorem 1.1.

### CC-C02. Least primes and finite character tests

LLS, corrected arXiv v3 (2016), Corollary 1.2, p. 3, gives
\[
 P(a,q)\le (\varphi(q)\log q)^2\qquad(q>3,\ (a,q)=1)
\]
under Dirichlet GRH. The small moduli are finite explicit cases. Theorem 1.1 gives stronger subgroup-escape bounds for \(q\ge3000\); Corollary 1.1 gives least quadratic nonresidue \(<(\log q)^2\) for prime \(q\ge5\). These need only Dirichlet GRH. The corrected v3 constants must be used: Theorem 1.2 has \(\alpha(2)=0.8\), \(\alpha(3)=0.7\), and \(\alpha(h)=0.66\) for \(h>3\). Earlier-version constants are not interchangeable.

For a rank-one character, its values on group generators determine it. For an arbitrary representation, the trace at the chosen generators need not determine the character. The safe finite certificate tests every residue class (or every class of the actual quotient), as in the separate archive module.

The earlier explicit bound is also now checked against its original source: Bach and Sorenson (1996), Theorem 5.3 (ERH), printed p. 1731, gives \(P(a,q)<2(q\log q)^2\) for positive moduli \(q\ge2\) and \((a,q)=1\). Their §2, p. 1720, specifies RH for \(\zeta_E\) and \(\zeta_{\mathbb Q}\); in this application \(E=\mathbb Q(\zeta_q)\), so the adopted input suffices. Their Corollary 3.5, pp. 1722–1723, concerns a prime in every ideal class of a quadratic field and explicitly sets \(E\) equal to its Hilbert class field. That application has the wider top-field hypothesis discussed in CC-F03, even though its base is quadratic. The stronger LLS bound is the one used for the finite certificate.

### CC-C03. Miller's deterministic algorithm

Miller (1976), Theorem 2, p. 301, proves under his ERH a deterministic primality algorithm taking \(O(b^4\log\log b)\) Turing-machine steps for an integer of binary length \(b\). His Appendix, pp. 316–317, formulates the relevant ERH for Dirichlet \(L\)-functions. The adopted Dirichlet GRH therefore discharges it. This validates that algorithm and its complexity analysis; deterministic primality testing was already unconditional by other algorithms, so one must not describe the consequence as the first proof that primality belongs to P. The exact bound on p. 301 was inspected visually as well as in extracted text.

### CC-C04. Bach's explicit witnesses and the class-group boundary

Bach (1990), *Explicit bounds for primality testing and related problems*, has distinct applications. Its abstract gives a Miller or Solovay–Strassen compositeness witness at most \(2(\log n)^2\), under the relevant ERH. LLS §1.1, p. 1, attributes to Bach a prime outside a proper subgroup below \(2(\log q)^2\), but that prime is allowed to divide \(q\); imposing \(p\nmid q\) changes that cited bound to \(3(\log q)^2\). This distinction must be preserved when applying a generator theorem.

Belabas, Diaz y Diaz, and Friedman (2008), *Small generators of the ideal class group*, introduction pp. 2–3 of the inspected author preprint, explicitly distinguish the two zero sums used by Bach: one for a nontrivial class character and one for the Dedekind zeta function. Their own Theorem 1.1, preprint p. 3, assumes RH for every nontrivial ideal-class-character \(L\)-function. This supplies a directly inspected primary locator for the hypothesis boundary.

The commonly cited class-group corollary is generation by prime ideals of norm at most \(12(\log|\Delta_K|)^2\), under GRH for the relevant ideal-class-character Hecke \(L\)-functions. This is identified as a consequence of Bach's Theorem 4, p. 376, by subsequent primary algorithmic literature. **Access/check status:** the original AMS article was not successfully retrieved in this run (HTTP 403); its theorem number is not represented here as directly checked against the original. Its exact original wording is a bibliographical gate, while the stronger operative LLS bounds and the mathematical hypothesis boundary are directly checked. The following explicit example explains why “\(K/\mathbb Q\) abelian” does not by itself discharge the class-character hypothesis.

### CC-F03. An abelian base with a non-Dirichlet class-character factor

**Statement.** Put \(K=\mathbb Q(\sqrt{-23})\), and let \(H\) be the splitting field of \(f(x)=x^3-x-1\). Then \(H/K\) is a nontrivial unramified cyclic cubic extension. A nontrivial character of \(\mathrm{Gal}(H/K)\) is an unramified class character of \(K\), but its induction to \(G_\mathbb Q\) is an irreducible two-dimensional representation. It is not a direct sum, or a virtual integer combination, of abelian one-dimensional representations. Thus its Hecke \(L\)-function is not supplied by an abelian-Artin factorization into Dirichlet \(L\)-functions.

**Proof.** A reducible monic cubic in \(\mathbb Z[x]\) has an integer root dividing its constant term. Neither \(1\) nor \(-1\) is a root of \(f\), so \(f\) is irreducible. Its discriminant is \(-4(-1)^3-27(-1)^2=-23\), a nonsquare. A transitive subgroup of \(S_3\) is \(A_3\) or \(S_3\); the discriminant being a nonsquare forces \(\mathrm{Gal}(H/\mathbb Q)=S_3\). The fixed field of \(A_3\) is \(K\), since the product of the root differences squares to \(-23\). Consequently \(\mathrm{Gal}(H/K)=A_3\cong C_3\).

For \(p\ne23\), the polynomial has separable reduction. Its roots lie in an unramified extension of \(\mathbb Q_p\): choose a finite residue extension splitting the reduction, lift it to the corresponding unramified local extension, and lift each simple root by Hensel's lemma. Hence the splitting field is unramified at all such primes.

At \(p=23\), direct multiplication gives
\[
 x^3-x-1\equiv(x-10)^2(x-3)\pmod{23}.
\]
The simple root \(3\) lifts to a root \(a\in\mathbb Z_{23}\), and polynomial division writes \(f=(x-a)g\) with \(g\) monic quadratic over \(\mathbb Z_{23}\). The resultant of \(x-a\) and \(g\) is a unit, because \(3\) differs from \(10\) modulo 23. The discriminant product formula
\(\mathrm{disc}(f)=\mathrm{disc}(g)\mathrm{Res}(x-a,g)^2\)
therefore gives valuation one for \(\mathrm{disc}(g)\). The splitting field of \(g\) is a ramified quadratic extension of \(\mathbb Q_{23}\); the linear factor adds nothing. Its inertia group acts as a transposition on the three roots. The relative inertia group for \(H/K\) is its intersection with \(A_3\), which is trivial. Thus \(H/K\) is unramified also above 23. There are no real places of \(K\), so there is no archimedean ramification. Global class field theory identifies this cyclic unramified extension with a quotient of the ideal class group.

Let \(\eta\) be a nontrivial complex character of \(A_3\). Its conjugate by a transposition is \(\eta^{-1}\ne\eta\). The induced representation has character values \(2,0,-1\) on the identity, a transposition, and a three-cycle, respectively. Its character norm is \((4+3\cdot0+2\cdot1)/6=1\), so it is irreducible. Every one-dimensional character of \(S_3\) kills \(A_3=[S_3,S_3]\), and every virtual combination of them has equal character values on the identity and on a three-cycle. The induced character does not. More generally, every abelian character of \(G_\mathbb Q\) is trivial on its commutator subgroup; the image of this commutator subgroup in the quotient \(S_3\) is \(A_3\). A virtual combination of abelian \(G_\mathbb Q\)-characters likewise cannot equal this induced character. Artin induction of \(L\)-functions identifies \(L_K(s,\eta)\) with the degree-two induced Artin \(L\)-function, so the claimed abelian factorization is unavailable. \(\square\)

This is a counterexample to the proposed *factorization route*, not a proof that Dirichlet GRH could never imply this Hecke GRH by a different theorem. In this example the missing hypothesis is the zero-line theorem for that class-character factor, or sufficiently strong Dedekind GRH for the corresponding Hilbert class extension. One need not identify \(H\) with the entire Hilbert class field for this obstruction.

### CC-F03b. A sufficient condition that does discharge the class-character hypothesis

**Statement.** Let \(K/\mathbb Q\) be a number field whose Hilbert class field \(H_K\) is abelian over \(\mathbb Q\). Then every ideal-class-character Hecke \(L\)-function of \(K\) is a product of primitive Dirichlet \(L\)-functions, and its GRH follows from the adopted input. In particular this applies when \(K\) is imaginary quadratic and its ideal class group has exponent dividing two.

**Proof.** Write \(G=\mathrm{Gal}(H_K/\mathbb Q)\), \(U=\mathrm{Gal}(H_K/K)\), and let \(\eta\) be a character of \(U\). The Hilbert class field correspondence identifies \(\eta\) with the chosen ideal-class character. Because \(G\) is finite abelian, \(\mathrm{Ind}_U^G\eta\) is a direct sum of one-dimensional characters of \(G\). Induction compatibility of Artin \(L\)-functions therefore writes \(L_K(s,\eta)\) as the product of the corresponding finite abelian \(L\)-functions over \(\mathbb Q\), which are primitive Dirichlet factors. This proves the first claim.

For imaginary quadratic \(K\), its Hilbert class field is stable under complex conjugation, and conjugation acts on the class group by inversion: an ideal \(\mathfrak a\) satisfies \([\overline{\mathfrak a}]=[\mathfrak a]^{-1}\), since \(\mathfrak a\overline{\mathfrak a}\) is generated by the ideal norm. The exact sequence for \(\mathrm{Gal}(H_K/\mathbb Q)\) splits by complex conjugation, which has order two and restricts nontrivially to \(K\). Thus this group is the semidirect product of the class group by the inversion action. If the class group has exponent dividing two, inversion is trivial and the semidirect product is abelian. The first part applies. \(\square\)

### CC-C05. Littlewood's consequences

Titchmarsh, revised by Heath-Brown (1986), Theorem 14.2 and equations (14.2.5)–(14.2.6), pp. 336–337, gives the Littlewood bounds leading from RH to the Lindelöf hypothesis. Theorem 14.25(A)–(C), pp. 369–370, gives convergence of \(\sum\mu(n)n^{-s}=1/\zeta(s)\) for \(\Re s>1/2\), and the equivalence
\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 M(x)=O_\varepsilon(x^{1/2+\varepsilon})
 \quad\text{for every }\varepsilon>0.
\]
These are now available with the RH hypothesis discharged. This does not yield the much stronger inequality \(|M(x)|\le\sqrt{x}\).

For the edge of the Dirichlet critical strip, the exact effective form used here is LLS Theorem 1.5. Write
\[
 B_1(q)=\log\log q-\log2+\tfrac12+\frac1{\log\log q}
       +\frac{14\log\log q}{\log q}.
\]
For a primitive character of conductor \(q\ge10^{10}\),
\[
 |L(1,\chi)|\ge\frac{\pi^2}{12e^\gamma B_1(q)}.
\]
LLS Corollary 1.3 then gives, for negative fundamental discriminant \(-q\),
\[
 h(-q)\ge\frac{\pi}{12e^\gamma}\frac{\sqrt q}{B_1(q)}.
\]
These require only Dirichlet GRH. Bounds for Hecke or higher-rank automorphic \(L\)-functions require their corresponding analytic hypotheses.

### CC-F02. A fully effective analytic Siegel bound

**Statement.** For every positive rational \(\varepsilon\), there is an algorithm producing a positive rational \(c_\varepsilon\) such that every primitive real nonprincipal Dirichlet character \(\chi\) of conductor \(q\) satisfies
\[
 L(1,\chi)\ge c_\varepsilon q^{-\varepsilon}.
\]

**Proof.** For \(q\ge10^{10}\), put \(t=\log q\) and \(u=\log t\). Then \(t>23\) and \(u>3\). Since \(-\log2+1/2<0\), \(1/u<1/3\), and \(14/t<1\),
\[
 B_1(q)\le2u+\tfrac13<3u.
\]
The displayed LLS bound yields
\[
 L(1,\chi)\ge \frac{\pi^2}{36e^\gamma\log\log q}.
\]
The value is positive: the real Euler product is positive on \(s>1\), continuity and nonvanishing at \(s=1\) give positivity at 1. Choose a computable integer \(Q\ge10^{10}\) with
\(\log Q\ge\max(2,2/\varepsilon^2)\). For \(q\ge Q\), the elementary estimate \(e^v\ge v^2/2\) gives
\[
 q^\varepsilon=e^{\varepsilon t}
 \ge\frac{\varepsilon^2t^2}{2}\ge t\ge\log t=\log\log q.
\]
Consequently \(q^\varepsilon L(1,\chi)\ge\pi^2/(36e^\gamma)\) throughout that range.

Only finitely many conductors remain. Primitive real characters of conductor below \(Q\) can be enumerated by finite arithmetic. For each such nonprincipal \(\chi\), periodicity and zero sum on a period imply
\(A(x)=\sum_{n\le x}\chi(n)\) has \(|A(x)|\le q\). Abel summation gives the certified tail estimate
\[
 \left|L(1,\chi)-\sum_{n\le N}\frac{\chi(n)}n\right|
 \le \frac{2q}{N}.
\]
Increase \(N\) until the rational number
\(b_\chi=\sum_{n\le N}\chi(n)/n-2q/N\)
is positive. This terminates because the partial sums converge to the positive number \(L(1,\chi)\). Since \(q^\varepsilon\ge1\), one may choose a positive rational \(c_\varepsilon\) below both \(\pi^2/(36e^\gamma)\) and every resulting \(b_\chi\). The finite minimum and the computable constant permit such a choice. For \(q<Q\), \(L(1,\chi)\ge b_\chi\ge c_\varepsilon\ge c_\varepsilon q^{-\varepsilon}\); for \(q\ge Q\), the preceding tail-range estimate applies. This algorithm establishes effectivity, without claiming practical efficiency. \(\square\)

### CC-C06. Cramér's RH theorem, as distinct from his stronger conjecture

Cramér's classical RH consequence is \(p_{n+1}-p_n=O(\sqrt{p_n}\log p_n)\). An inspected primary modern source is Dudek (2014), *On the Riemann hypothesis and the difference between primes*, arXiv:1402.6417v2: Theorem 1, p. 2, states Cramér's result; Theorem 2, p. 2, proves the explicit version
\[
 (x-\tfrac4\pi\sqrt x\log x,x]\quad\text{contains a prime for every }x\ge2;
\]
Theorem 3 replaces \(4/\pi\) by \(1+\varepsilon\) for sufficiently large \(x\). RH is the sole unproved analytic hypothesis. Cramér's conjectural \(O((\log p_n)^2)\) gap bound is not the theorem being discharged. The original 1920 theorem number was not directly inspected; the exact operative locators here are Dudek's numbered statements, with the original work retained in the bibliography.

### CC-C07. Selberg's mean square for short intervals

The usable RH consequence is
\[
 \int_1^X|\psi(t+h)-\psi(t)-h|^2\,dt
 \ll Xh(\log X)^2\qquad(1\le h\le X).
\]
An inspected modern primary statement is Bhowmik–Schlage-Puchta, *Mean representation number of integers as the sum of primes*, Lemma 1, which explicitly attributes the input to Selberg (1943), equation (13). The original Selberg article is *On the normal density of primes in small intervals, and the difference between consecutive primes*, pp. 87–105; it is paper 12 in *Collected papers*, vol. I. The original equation was not directly inspected in this run, so that locator is marked as transmitted by the later primary paper.

The elementary consequence needed here requires no further zero hypothesis. Apply the mean square with upper endpoint \(2X\). For fixed \(\delta>0\), the measure of \(t\in[X,2X]\) for which \(|\psi(t+h)-\psi(t)-h|>\delta h\) is at most \(O(X(\log X)^2/(\delta^2h))\), by integrating over that set. Thus if \(h/(\log X)^2\to\infty\), the relative exceptional measure tends to zero. This is an almost-all-interval statement, not a bound in every interval and not the Selberg eigenvalue conjecture.

### CC-C08. Montgomery's restricted pair correlation

Montgomery (1973), §1, unnumbered Theorem, p. 181, equations (1)–(2), defines
\[
 F(\alpha,T)=\left(\frac{T}{2\pi}\log T\right)^{-1}
 \sum_{0<\gamma,\gamma'\le T}
 T^{i\alpha(\gamma-\gamma')}
 \frac4{4+(\gamma-\gamma')^2}.
\]
Under RH,
\[
 F(\alpha,T)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1)
\]
uniformly on \(0\le\alpha\le1-\varepsilon\), for each fixed \(\varepsilon>0\). RH suffices for this theorem. The unrestricted pair-correlation prediction, discussed separately in the same paper at equations (11)–(12), is not obtained by dropping a hypothesis from the displayed theorem: its Fourier-support obstruction remains. RH determines the horizontal locations, not all vertical correlations or simplicity.

## 4. Criteria and programmes

| ID | Precise conclusion now available | Exact locator | Remaining mathematical task |
|---|---|---|---|
| CC-P01 | The global Weil quadratic form is nonnegative on its specified test-function space | Connes–Consani, supplied source, Appendix C, Proposition C.1, p. 51; explicit formula Appendix B | The local archimedean or semilocal comparison with a particular cutoff/Sonin projection is an additional identity or inequality, not an automatic termwise consequence of the global sum |
| CC-P02 | Every classical Li coefficient is nonnegative; indeed CC-F04 proves strict positivity for the nonzero Dirichlet systems | Li (1997), Theorem 1, p. 325; generalized criterion Lagarias (2007), Theorem 2.4, p. 1702 (preprint Theorem 2.2, p. 11) | Higher-rank automorphic positivity requires RH for the corresponding \(L\)-function |
| CC-P03 | \(\mathbf1_{(0,1]}\) belongs to the closed span of \(x\mapsto\{1/(nx)\}\), \(n\ge1\), in \(L^2(0,\infty)\) | Báez-Duarte (2002), Theorem 1.1, p. 1 | Convergence of a particular proposed coefficient sequence or optimal distance asymptotics needs its own theorem; the ordinary Möbius truncations diverge, as discussed at (1.1), p. 2 |
| CC-P04 | There is an abstract self-adjoint operator whose spectral ordinates are the zeros, counting multiplicity | Elementary construction CC-F05 below | Arithmetic origin, a prescribed trace formula, canonical domain, and geometric functoriality do not follow from the diagonal construction |
| CC-P05 | Connes's RH-equivalent trace assertion for the \(\mathbb Q\) version has its zero hypothesis discharged | Connes (1999), §VIII, Theorem 5 in positive characteristic, and the explicit \(\mathbb Q\) analogue on preprint pp. 44–47 | The literally numbered theorem concerns positive characteristic. General number-field Hecke \(L\)-functions exceed the adopted Dirichlet statement |
| CC-P06 | Deninger's proposed eigenvalue location is correct for the adopted abelian Artin–Tate factors | Deninger, *The Hilbert–Pólya strategy and height pairings*, §2, Conjectures 1–2, pp. 2–5 | The functorial cohomology, determinant formula, Hodge star, and positive height pairing remain construction/positivity questions; CC-F06 refutes a general converse from eigenvalue location to the adjoint identity |
| CC-P07 | The specific sufficient de Branges conditions tested by Conrey–Li remain refuted | Conrey–Li (2000), Theorems 1–2; §§3.1–3.2, equations (3.1)–(3.4); §4 Remark | Any successful revised Hilbert-space construction must avoid those disproved positivity assumptions |
| CC-P08 | The \(\Lambda\)-geometric class in CC-F01 has its analytic RH | Borger Theorem 0.1 and Corollary 6.2 | Infinite-dimensional \(\mathbf F_1\) cohomology, an archimedean theory, and a geometric proof of RH are separate parts of the programme |
| CC-P09 | The already proved restricted Katz–Sarnak density results can now be interpreted with real ordinates in the Dirichlet families | Rubinstein (2001), Theorem 3.1, pp. 150–151 | Full support and higher-rank families do not follow. Theorem 3.1 itself was already unconditional, allowing complex ordinates |

### CC-P01. Exact global positivity and the archimedean boundary

For \(g\in C_c^\infty(\mathbb R_{>0})\), use \(\widetilde g(s)=\int_0^\infty g(x)x^{s-1}dx\) and impose \(\widetilde g(0)=\widetilde g(1)=0\). On RH the zero-side form is
\[
 Q(g)=\sum_\rho\widetilde g(\rho)
       \overline{\widetilde g(1-\overline\rho)}
     =\sum_\rho|\widetilde g(\rho)|^2\ge0.
\]
The sums converge because the Mellin transform decays rapidly on a vertical strip and the zero count is \(O(T\log T)\). Proposition C.1 of the supplied Connes–Consani paper expresses the equivalent prime-and-archimedean inequality with their sign convention as \(\sum_v W_v(g*\overline g^{\sharp})\le0\); it allows finitely many additional Mellin vanishing conditions as well. The global inequality is now a theorem in the adopted theory. Their Theorem 1 and Theorem 6.11 concern a more specific comparison of the archimedean term with a Sonin-space trace, with support and vanishing restrictions. Those results remain their existing proved theorems; RH alone does not justify enlarging their support class or declaring each separate local term positive.

### CC-F04. Strict real-part positivity of Dirichlet Li coefficients

**Statement.** For the zeros of \(\zeta\), or of any primitive Dirichlet \(L\)-function after the usual completion and removal of the trivial-character poles, define the Li coefficients by the standard symmetrically ordered zero sum
\[
 \lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right],\qquad n\ge1.
\]
Under the adopted statements, \(\Re\lambda_n>0\) for every \(n\ge1\). For a real character, or for \(\zeta\), \(\lambda_n\) itself is real and strictly positive. The criterion is the known theorem of Li and its generalized form; the short proof here records the strictness and the treatment of complex characters.

**Proof.** Every zero has the form \(\rho=1/2+i\gamma\), and
\[
 z_\rho=1-\frac1\rho=\frac{-1/2+i\gamma}{1/2+i\gamma}
\]
has modulus one. Write \(z_\rho=e^{i\theta_\rho}\). Each real-part summand is \(1-\cos(n\theta_\rho)\ge0\). For \(|\gamma|\to\infty\), \(\theta_\rho=O(1/|\gamma|)\); hence these real parts are \(O_n(1/\gamma^2)\). The usual zero count \(O(T\log(q(T+2)))\), with \(q\) fixed, makes the real-part series absolutely convergent, so taking real parts of the prescribed symmetric limit gives the sum of these nonnegative terms.

There are infinitely many zeros with arbitrarily large \(|\gamma|\). For finite \(\gamma\), \(z_\rho\ne1\), while \(z_\rho\to1\) as \(|\gamma|\to\infty\). For a fixed \(n\), choose a sufficiently large zero so that the nonzero principal argument satisfies \(0<|\theta_\rho|<2\pi/n\). Then \(1-\cos(n\theta_\rho)>0\), so the entire sum is strictly positive. In the real-character and zeta cases, conjugate zeros occur with equal multiplicities; their contributions are conjugates, making the standard sum real. \(\square\)

No assertion of reality is made for the coefficient attached to a complex Dirichlet character. The generalized Li criterion uses its real part (Lagarias, published Theorem 2.4; preprint Theorem 2.2).

### CC-F05. The bare Hilbert–Pólya existence statement

**Statement and proof.** List the nontrivial zeros of \(\zeta\), with multiplicity, as \(1/2+i\gamma_j\), and choose an enumeration with \(|\gamma_j|\to\infty\). On \(\mathcal H=\ell^2(\mathbb N)\), put
\[
 D(a_j)=(\gamma_j a_j),\qquad
 \operatorname{Dom}(D)=\{a\in\ell^2:\sum_j\gamma_j^2|a_j|^2<\infty\}.
\]
Finite sequences give a dense domain. Since the \(\gamma_j\) are real, \(D\) is symmetric. If \(b\in\operatorname{Dom}(D^*)\), testing the adjoint relation against the coordinate vectors forces \((D^*b)_j=\gamma_jb_j\); membership of \(D^*b\) in \(\ell^2\) then forces \(b\in\operatorname{Dom}(D)\). Conversely every such \(b\) satisfies the adjoint relation by Cauchy–Schwarz. Thus \(D^*=D\). The resolvent \((D-i)^{-1}\) is diagonal with entries \((\gamma_j-i)^{-1}\to0\), and its truncations are finite-rank operators converging in operator norm. Therefore it is compact. Each coordinate vector is an eigenvector with the prescribed ordinate, with multiplicities retained. If a complex number \(z\) is not an ordinate, discreteness and escape to infinity give \(\inf_j|\gamma_j-z|>0\), so the diagonal operator \(R_z\) with entries \((\gamma_j-z)^{-1}\) is bounded. The coordinate identity \(DR_z=I+zR_z\) shows that its range is in \(\operatorname{Dom}(D)\), bounded in the graph norm; also \((D-z)R_z=I\) and \(R_z(D-z)=I\) on their respective domains. Hence there is no additional spectrum. This proves the abstract existence statement. \(\square\)

This construction uses the zeros themselves as input. It supplies none of the independent arithmetic explanation sought in a stronger Hilbert–Pólya programme. The same construction works for each primitive Dirichlet function. No zero-simplicity assumption is required.

### CC-P05. Connes: exact theorem scope

Connes's *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* has several assertions that should not be merged. Its §III Theorem 1, preprint p. 13, gives a spectral realization of critical zeros (with the multiplicity cutoff stated there), with noncritical zeros entering a resonance description. The adopted RH removes the noncritical alternatives for \(\zeta\) and the relevant Dirichlet twists. In §VIII, Theorem 5 is explicitly formulated for global fields of positive characteristic. The text then constructs and discusses the corresponding \(\mathbb Q\) cutoff using the real place and prolate spaces on preprint pp. 44–47, ending with the stated analogues of Lemma 1, Theorem 5 and Lemma 3. For \(\mathbb Q\), unitary Hecke characters are Dirichlet characters times imaginary norm powers; these shift ordinates without changing the real zero line. Thus the analytic hypothesis in that \(\mathbb Q\) criterion is covered. The statement for general number-field Hecke characters requires additional GRH outside the adopted family. A proof of an equivalent trace assertion does not, by itself, provide a new geometric derivation of its required cutoff limit.

### CC-F06. Eigenvalue purity does not imply Deninger's positive adjoint structure

**Statement.** For every real \(w\), there is a complex linear endomorphism with spectrum on \(\Re s=w/2\) that admits no positive-definite Hermitian form for which \(A+A^*=wI\).

**Proof.** On \(\mathbb C^2\), put \(A=(w/2)I+N\), where \(Ne_2=e_1\) and \(Ne_1=0\). Its only eigenvalue is \(w/2\), and \(N^2=0\ne N\). If a positive Hermitian form made \(A+A^*=wI\), then \(N^*=-N\). Taking \(x=e_2\) gives
\[
 \|Nx\|^2=\langle x,N^*Nx\rangle
          =-\langle x,N^2x\rangle=0,
\]
contradicting positive definiteness and \(Nx=e_1\ne0\). \(\square\)

Deninger's proposed identity in §2, pp. 4–5, is \(\nu(f,f')=(\theta f,f')+(f,\theta f')\), obtained from a trace, cup product and Hodge star. It implies the desired line. The example proves that a general converse from line location to that positive adjoint identity is false. It does not refute the existence of the particular geometric objects Deninger conjectures. Semisimplicity, a pairing and the functorial geometry are additional content.

### CC-P07. What the de Branges counterexamples settle

Conrey and Li's Theorems 1–2 formulate sufficient positivity conditions in de Branges spaces. In §3.1 they show that the proposed conditions fail for \(E(z)=\xi(1-iz)\), and in §3.2 they give analogous failures for the character modulo 4. Their §4 Remark attributes to Sarnak a nonnumerical proof of failure of the kernel-shift condition (3.3), via the value distribution of \(\log\zeta\), with a Dirichlet analogue for (3.8). The derivative-test counterexamples to (3.1) in §3 are cited as the published numerical results, not as computations independently certified in this run. The nonnumerical kernel-shift refutation already suffices to disprove the blanket assertion that every proposed sufficient positivity condition follows from RH. The accurate outcome is a refutation of those particular sufficient conditions. It would be a logical error to deduce them from RH.

### CC-P09. Katz–Sarnak and the restriction that survives

Rubinstein's Theorem 3.1, pp. 150–151, treats primitive quadratic characters \(\chi_d\), averaged over fundamental discriminants with \(X/2\le|d|<X\). For product Schwartz tests \(f(x_1,\ldots,x_n)=\prod_i f_i(x_i)\), each \(f_i\) even, with Fourier support \(\sum_i|u_i|<1\), the normalized \(n\)-level density is the symplectic determinant with kernel
\[
 K_{-1}(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)}
            -\frac{\sin\pi(x+y)}{\pi(x+y)}.
\]
The sentence immediately preceding the theorem explicitly allows complex ordinates and says RH is not assumed. Thus the theorem itself was already unconditional. Dirichlet GRH now supplies real ordinates but does not remove its Fourier-support restriction. Full number-field family statistics, and analogues involving higher-rank \(L\)-functions, are not consequences of just the adopted zero-line statements. The finite-field monodromy and equidistribution part of Katz–Sarnak likewise was not waiting for number-field RH.

## 5. Explicit boundary catalogue

| Proposed extension | Status and actual additional gate |
|---|---|
| General effective Chebotarev from Dirichlet GRH | Theorem 1.1 of Lagarias–Odlyzko needs RH for \(\zeta_L\). It is discharged when \(L/\mathbb Q\) is abelian; arbitrary top fields need more |
| Bach class-group generators for every abelian \(K/\mathbb Q\) | The class-character Hecke \(L\)-functions need their own zero theorem, or a suitable Hilbert-class-extension Dedekind GRH; CC-F03 shows why abelian base is insufficient for the offered factorization argument |
| Full generalized Li positivity | Lagarias Theorem 2.4 (preprint 2.2) is family by family. General unitary cuspidal \(GL_N\) functions require their own RH; Dirichlet GRH covers the finite-order \(GL_1/\mathbb Q\) family and its norm shifts |
| Full GUE / Katz–Sarnak statistics / simplicity of all zeros | The cited restricted statistics keep their test-function restrictions. No theorem here upgrades zero location to arbitrary correlations or simplicity |
| Cramér's logarithmic-square gap conjecture | Distinct from Cramér's RH-conditional square-root-times-log theorem |
| Universal local positivity in an explicit formula | Positivity of a sum of local terms does not imply positivity of each summand. Connes–Consani's extra local comparison has its own hypotheses |
| Deninger's positive cohomology or a canonical Hilbert–Pólya operator | The analytic target is supplied for the adopted factors; functorial spaces, adjoints, pairings and trace compatibility remain. CC-F06 disproves an unrestricted linear-algebra converse |
| A \(\Lambda\)-structure on the hexagonal elliptic curve | Refuted by Borger §2.9; split-prime CM Frobenius lifts are weaker data |
| A Chow-motive Artin–Tate decomposition from the cohomological \(L\)-factorization | Not proved by the factorization; a realization is not automatically fully faithful or conservative in the required motivic sense |
| Effective integral points merely from the phrase “effective Siegel” | No such implication is asserted. CC-F02 proves only the analytic lower bound for real Dirichlet \(L(1,\chi)\) and its class-number consequences |

## 6. Source register and exact-reading status

The following are primary works or mirrors of primary texts. Web references in the companion TSV are provenance aids; the paper should cite authors, dates and the locators above. No original statement number is guessed when an original was not inspected.

1. **Borger, J. (2009).** *\(\Lambda\)-rings and the field with one element* (arXiv:0906.3146v1). Theorems 0.1, 5.3, 6.1; Corollary 6.2, equation (6.2.1); Corollaries 6.5–6.6; §2.9. https://arxiv.org/pdf/0906.3146 . Supplied TeX and external PDF both inspected. The PDF's regenerated date is not used as the publication date.
2. **Lamzouri, Y., Li, X., & Soundararajan, K. (2015; corrected preprint 2016).** Conditional bounds for the least quadratic non-residue and related problems. *Mathematics of Computation, 84*(295), 2391–2412. https://doi.org/10.1090/S0025-5718-2015-02925-1 . Operative corrected text: https://arxiv.org/pdf/1309.3595 , v3, 8 December 2016, internal date 12 December 2016. Theorems 1.1, 1.4, 1.5; Corollaries 1.1–1.3. PDF and extracted text inspected.
3. **Lagarias, J. C., & Odlyzko, A. M. (1977).** Effective versions of the Chebotarev density theorem. In A. Fröhlich (Ed.), *Algebraic number fields: L-functions and Galois properties* (pp. 409–464). Academic Press. Theorem 1.1, equation (1.3); Corollary 1.2. Inspected retypeset primary text: https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf .
4. **Miller, G. L. (1976).** Riemann's hypothesis and tests for primality. *Journal of Computer and System Sciences, 13*(3), 300–317. Theorem 2, p. 301; Appendix, pp. 316–317. https://www.cs.cmu.edu/~glmiller/Publications/Papers/Mi76.pdf . Original PDF inspected, including rendered p. 301.
5. **Bach, E. (1990).** Explicit bounds for primality testing and related problems. *Mathematics of Computation, 55*(191), 355–380. https://doi.org/10.1090/S0025-5718-1990-1023756-8 . Original PDF access failed; author abstract and LLS attribution inspected. Theorem 4 / p. 376 class-group locator remains to be directly checked.
6. **Titchmarsh, E. C. (1986).** *The theory of the Riemann zeta-function* (2nd ed., D. R. Heath-Brown, rev.). Oxford University Press. Theorems 14.2 and 14.25(A)–(C). Original book scan: https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf . Inspected extracted text; equations crosschecked against theorem context.
7. **Cramér, H. (1920).** Some theorems concerning prime numbers. *Arkiv för Matematik, Astronomi och Fysik, 15*(5), 1–33. Historical attribution; original statement number not inspected. Operative source follows.
8. **Dudek, A. W. (2014/2015).** On the Riemann hypothesis and the difference between primes. Preprint arXiv:1402.6417v2; published in *International Journal of Number Theory, 11*(3), 771–778. Theorems 1–3 in the inspected preprint (published numbering 1.1–1.3). https://arxiv.org/pdf/1402.6417 .
9. **Selberg, A. (1943).** On the normal density of primes in small intervals, and the difference between consecutive primes. *Archiv for Mathematik og Naturvidenskab, 47*(6), 87–105. Equation (13), as cited by the next primary work; original not directly inspected.
10. **Bhowmik, G., & Schlage-Puchta, J.-C. (2010).** Mean representation number of integers as the sum of primes. *Nagoya Mathematical Journal, 200*, 27–33. https://doi.org/10.1215/00277630-2010-010 . Lemma 1, p. 2 in arXiv v3, with explicit attribution to Selberg equation (13). Primary PDF inspected: https://arxiv.org/pdf/0806.3295 ; initial mirror: https://paperzz.com/doc/9064999/mean-representation-number-of-integers-as-the-sum .
11. **Montgomery, H. L. (1973).** The pair correlation of zeros of the zeta function. In *Analytic number theory* (Proceedings of Symposia in Pure Mathematics, Vol. 24, pp. 181–193). American Mathematical Society. https://doi.org/10.1090/pspum/024/9944 . §1 unnumbered Theorem, p. 181, equations (1)–(2); conjectural equations (11)–(12). Primary-text mirror inspected: https://studylib.net/doc/7952799/the-pair-correlation-of-zeros-of-the-zeta-function .
12. **Li, X.-J. (1997).** The positivity of a sequence of numbers and the Riemann hypothesis. *Journal of Number Theory, 65*(2), 325–333. https://doi.org/10.1006/jnth.1997.2137 . Theorem 1, p. 325; equation (1.4). Primary-text mirror: https://paperzz.com/doc/7086946/--science-direct .
13. **Lagarias, J. C. (2007).** Li coefficients for automorphic \(L\)-functions. *Annales de l'Institut Fourier, 57*(5), 1689–1740. https://doi.org/10.5802/aif.2311 . Published Theorem 2.4, p. 1702: https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf . In arXiv v4 (2005), https://arxiv.org/pdf/math/0404394 , the corresponding statement is Theorem 2.2, p. 11. Both primary statements inspected; their different numbering is retained.
14. **Báez-Duarte, L. (2002/2003).** A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis. *Rendiconti Lincei. Matematica e Applicazioni, 14*, 5–11. Theorem 1.1 in arXiv:math/0202141v2: https://arxiv.org/pdf/math/0202141 . PDF inspected. The quantitative continuation is arXiv:math/0205003; not used here without checking its exact numbered statement.
15. **Connes, A. (1999).** Trace formula in noncommutative geometry and the zeros of the Riemann zeta function. *Selecta Mathematica, 5*, 29–106. https://arxiv.org/pdf/math/9811068 . §VIII, Theorem 5, and preprint pp. 44–47. PDF inspected; characteristic scope checked against the theorem's opening words.
16. **Connes, A., & Consani, C. (2020).** Weil positivity and trace formula, the archimedean place. arXiv:2006.13771. https://arxiv.org/pdf/2006.13771 . Supplied TeX `weil-compo.tex`; Appendix C Proposition C.1; Theorem 1; Theorem 6.11; Appendix B. Supplied text and PDF locators inspected.
17. **Deninger, C. (2010).** The Hilbert–Pólya strategy and height pairings. In *Casimir force, Casimir operators and the Riemann hypothesis* (pp. 275–283). Walter de Gruyter. §2, Conjectures 1–2 and the adjoint calculation, preprint pp. 2–5. Author/institute PDF: https://www.uni-muenster.de/SFB878/publications/files/php7aMxKR3029.pdf ; arXiv: https://arxiv.org/pdf/1001.1621 . PDF inspected; publication metadata checked on the author’s publications page.
18. **Conrey, J. B., & Li, X.-J. (2000).** A note on some positivity conditions related to zeta- and \(L\)-functions. *International Mathematics Research Notices, 2000*(18), 929–940. https://arxiv.org/pdf/math/9812166 . Theorems 1–2; §§3.1–3.2; §4 Remark. Primary PDF inspected.
19. **Rubinstein, M. (2001).** Low-lying zeros of \(L\)-functions and random matrix theory. *Duke Mathematical Journal, 109*(1), 147–181. Theorem 3.1, pp. 150–151. https://web.williams.edu/Mathematics/sjmiller/public_html/ntprob17/handouts/Lfns/Rubinstein_ThesisPaper_Duke.pdf . Original PDF inspected. The theorem's explicit absence of an RH assumption was checked.

20. **Belabas, K., Diaz y Diaz, F., & Friedman, E. (2008).** Small generators of the ideal class group. *Mathematics of Computation, 77*(262), 1185–1197. https://doi.org/10.1090/S0025-5718-07-02003-0 . Inspected author preprint dated 5 December 2005: https://www.math.u-bordeaux.fr/~kbelabas/research/OnBach.pdf . Introduction pp. 2–3 and Theorem 1.1, p. 3.
21. **Bach, E., & Sorenson, J. (1996).** Explicit bounds for primes in residue classes. *Mathematics of Computation, 65*(216), 1717–1735. https://doi.org/10.1090/S0025-5718-96-00763-6 . Original author-hosted PDF inspected: https://www.researchgate.net/profile/Jonathan-Sorenson-2/publication/220576951_Explicit_bounds_for_primes_in_residue_classes/links/55100ea70cf2ac2905afbceb/Explicit-bounds-for-primes-in-residue-classes.pdf . Theorem 5.3, p. 1731; §2, p. 1720; Corollaries 3.4–3.5, pp. 1722–1723. The numerical computations reported by the authors were not rerun here.

## 7. Check record and unresolved bibliographical gates

Every new proof in this module must be read as a whole after composition. The companion `consequences_criteria_CHECK_EVENTS.tsv` records the actual completion of those reads and any correction; it does not call a same-author proof read an independent re-proof. The adopted Alpöge statements receive an event for their use, not for a claimed verification of the unseen full archive.

The unresolved bibliographical items are narrowly delimited: direct inspection of Bach's original Theorem 4 and the original Selberg equation (13). These are not presented as completed direct-source checks. The operative least-prime, cohomological, effective-Siegel and criterion results above have explicit inspected primary locators. No mathematical claim of global logical independence is made from a failure of the current factorization route.
