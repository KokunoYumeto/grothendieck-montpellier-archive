# AM-K029 — a degree-seven repair of the literal unramified etaT character

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

The root-unit obstruction of AM-K028 can be repaired on an explicit larger field while keeping the ordinary primitive-J Hodge type. The following construction proves the full character interface, including the base-field restriction `ResEta`; it does not merely remove one necessary unit test.

Write
\[
 E_0=\mathbb Q(\zeta_{28}),\quad F_0=E_0^+,
 \quad\Phi_0=\{1,3,9,15,17,23\},
\]
and let B be the unique degree-seven subfield of \(\mathbb Q(\zeta_{29})\). Put
\[
                         K=E_0B,\qquad F=F_0B.
\tag{ER1}
\]
Give K the induced CM type \(\Psi\), containing all seven lifts of each member of \(\Phi_0\).

### Theorem ER2

The extension K/F is CM and unramified at every finite place, \([K:\mathbb Q]=84\), and \([F:\mathbb Q]=42\). There exists a continuous unitary Hecke character
\[
                   \eta:\mathbb A_K^\times/K^\times\longrightarrow S^1
\]
that is unramified at every finite place, has infinity component
\[
        \eta_\infty(z)=\prod_{\tau\in\Psi}\frac{z_\tau}{|z_\tau|},
\tag{ER2}
\]
and restricts to the quadratic character \(\eta_{K/F}\) on \(\mathbb A_F^\times\). Thus it satisfies the literal `IsEtaT` convention checked in AM-K028. Its normalized finite values
\[
                 \eta(\varpi_P)\,(NP)^{-1/2}
\tag{ER3}
\]
all lie in a single finite algebraic coefficient field, which may be enlarged to contain its complex conjugates. Therefore the separate `etaVal` field can also be supplied after that coefficient-field enlargement.

No class-number calculation for the degree-84 or degree-42 fields is needed for this existence proof. No bound on the degree, discriminant, or heights of the auxiliary coefficient field is asserted. The full polarized host, original `IsTen`, all source size predicates, and later selected-image bounds are separate conditions.

## 1. The field and its roots of unity

The group \((\mathbb Z/29\mathbb Z)^\times\) is cyclic of order 28. Its subgroup of order four contains complex conjugation and fixes B; thus B is totally real, cyclic of degree seven, and ramified only at 29, with ramification index seven there. The fields E₀ and B have coprime degrees 12 and 7, so are linearly disjoint. Hence K has degree 84, and its conjugation fixes exactly F, of degree 42.

Accepted DP57 proves that E₀/F₀ is unramified at every finite place. This property is preserved by base change. More concretely, locally a finite étale extension of a DVR stays étale after base change, and its finite field components give the completions of K/F. Hence K/F is everywhere finite-unramified.

The rational ramification indices in K are
\[
                     e_2=2,\qquad e_7=6,\qquad e_{29}=7,
\tag{ER4}
\]
and all other finite rational primes are unramified. These follow from the standard cyclotomic indices in \(\mathbb Q(\zeta_{28})\), the totally ramified degree-seven extension at 29, and their disjoint ramification sets.

It follows that
\[
                                  \mu(K)=\mu_{28}.
\tag{ER5}
\]
Indeed a primitive \(\ell^a\)-th root in K would force the cyclotomic ramification index \(\varphi(\ell^a)\) to divide the corresponding index in (ER4). No odd prime other than 7 can occur: at 29 the required index 28 does not divide 7, and all remaining odd primes are unramified. A 49th root would require index 42 at 7, and an eighth root would require index four at 2. Thus the root order divides 28; E₀ already contains all these roots. The same argument gives \(\mu(E_0)=\mu_{28}\).

For a CM field L and a unit u, \(u/\bar u\) is a root of unity. Here is the elementary fact used: all conjugates of this algebraic integer unit have absolute value one. The characteristic polynomials of its positive powers have bounded integer coefficients, so only finitely many such powers can occur; two powers are equal, proving finite order. This also gives the usual CM-unit index bound below without a unit-group classification theorem.

## 2. The entire unit phase image in E₀

Define
\[
 a_0(x)=\prod_{\phi\in\Phi_0}\frac{\phi(x)}{|\phi(x)|}
                       \quad(x\in E_0^\times).
\tag{ER6}
\]
We prove the exact identity
\[
                             a_0(\mathcal O_{E_0}^\times)=\mu_7.
\tag{ER7}
\]

First every real unit \(\varepsilon\in\mathcal O_{F_0}^\times\) has phase one. The canonical quadratic Artin character of the known extension E₀/F₀ is unramified at every finite place and has local sign at every real place. On a principal real unit, its finite value is one, so global reciprocity gives
\(\operatorname{sgn}N_{F_0/\mathbb Q}\varepsilon=1\). This sign is exactly \(a_0(\varepsilon)\). This uses the quadratic character on **F₀**, which exists by class field theory; it does not presume the obstructed `etaT` character on E₀.

Next put \(u_0=1-\zeta_{28}\). It is a unit because
\[
 \Phi_{28}(X)=X^{12}-X^{10}+X^8-X^6+X^4-X^2+1,
                      \qquad \Phi_{28}(1)=1.
\]
Its conjugation quotient is
\[
                       \frac{u_0}{\bar u_0}=-\zeta_{28}=\zeta_{28}^{15}.
\tag{ER8}
\]
For an arbitrary unit u, write \(u/\bar u=\zeta_{28}^a\). Choose \(\epsilon\in\{0,1\}\) with \(a-15\epsilon\) even and choose j with \(2j\equiv a-15\epsilon\pmod{28}\). Then
\(u/(\zeta_{28}^j u_0^\epsilon)\) is fixed by conjugation and is an integral unit. Thus
\[
 \mathcal O_{E_0}^\times
   =\mu_{28}\,\mathcal O_{F_0}^\times\,\{1,u_0\}.
\tag{ER9}
\]
This proves exactly the needed Hasse-index-two description; no missing generator is assumed.

On \(\mu_{28}\), the phase is \(a_0(\zeta_{28}^j)=\zeta_{28}^{68j}\), whose image has order seven. For \(0<a<28\),
\[
 \frac{1-e^{2\pi ia/28}}{|1-e^{2\pi ia/28}|}
                             =-i e^{\pi ia/28}.
\]
Using the six integers in \(\Phi_0\), this gives
\[
                    a_0(u_0)=(-i)^6\zeta_{56}^{68}=\zeta_7^5.
\tag{ER10}
\]
Equations (ER9)–(ER10), and the real-unit result, prove (ER7).

## 3. All new units of K satisfy the required phase condition

Let
\[
 a(x)=\prod_{\tau\in\Psi}\frac{\tau(x)}{|\tau(x)|}
                   =a_0(N_{K/E_0}x).
\tag{ER11}
\]
The equality follows by multiplying over all lifts of each embedding; the absolute values multiply in the same way.

For a unit U of K, put \(v=N_{K/E_0}U\), an E₀-unit. By (ER5), write \(U/\bar U=\zeta\in\mu_{28}\). Since this root lies in E₀,
\[
                       \frac v{\bar v}=\zeta^7.
\]
Consequently
\[
 a(U)^2=a_0(v)^2
       =\prod_{\phi\in\Phi_0}\phi(v/\bar v)
       =a_0(\zeta^7)=1.
\tag{ER12}
\]
On the other hand, (ER7) gives \(a(U)=a_0(v)\in\mu_7\). The only element common to \(\mu_2\) and \(\mu_7\) is one. Therefore
\[
                            a(\mathcal O_K^\times)=\{1\}.
\tag{ER13}
\]
This treats every new unit in the degree-seven extension, not only the roots inherited from E₀.

## 4. Extending a unit-compatible angular type to an unramified character

We use the following elementary ideal construction. Let L be a CM field, let b be a unitary angular character of \((L\otimes\mathbb R)^\times\), and suppose \(b(\mathcal O_L^\times)=1\). On the principal fractional ideals define
\[
                         c((x))=b(x)^{-1}.
\tag{ER14}
\]
It is well-defined by the unit condition. It extends to a homomorphism \(c:I_L\to S^1\) on all fractional ideals. To see this without an abstract extension theorem, write the finite class group as a direct sum of cyclic groups, choose representative ideals \(\mathfrak a_j\) of their generators and relations \(\mathfrak a_j^{h_j}=(x_j)\), and choose roots \(c(\mathfrak a_j)^{h_j}=b(x_j)^{-1}\) in \(S^1\). Every ideal has a principal remainder after choosing the canonical ranges of the generator exponents. The displayed root equations make its value independent of carries and make multiplication exact.

For a finite idele \(z_f\), let \(I(z_f)=\prod_PP^{v_P(z_P)}\). Then
\[
                         \chi(z)=b(z_\infty)c(I(z_f))
\tag{ER15}
\]
is continuous, unitary, unramified at all finite places, and trivial on L× by (ER14). The ideal-valued map is locally constant, and b is continuous, so continuity has not been omitted. A character with trivial infinity component and unramified finite components similarly factors through the ordinary finite ideal class group.

By (ER7), this constructs an unramified unitary character \(\chi_7\) on E₀ with angular type \(a_0^7\). By (ER13), it constructs a character \(\chi_0\) on K with angular type a. The latter already has all desired clauses except the exact restriction to F.

## 5. Repairing the restriction without a large class-number calculation

The only numerical class-number input is
\[
                                  h(F_0)=1.
\tag{ER16}
\]
This is explicitly tabulated in Masley (1978), Table 3, printed p.316: conductor 28, degree 6, class number 1. I inspected that primary table image. The field is the maximal real subfield of E₀, whose Galois group is cyclic of order six. No conjectural class-number bound is used.

Let \(\eta_0=\eta_{E_0/F_0}\). The restriction of \(\chi_7\) to F₀ has sign at each real place, since seven is odd, and is unramified at all finite places. Hence \((\chi_7|_{\mathbb A_{F_0}^\times})/\eta_0\) has trivial infinity component and factors through \(\mathrm{Cl}(F_0)\). By (ER16),
\[
                        \chi_7|_{\mathbb A_{F_0}^\times}=\eta_0.
\tag{ER17}
\]

Put \(\eta_1=\eta_{K/F}\) and
\[
 \beta=\chi_7\circ N_{K/E_0},\qquad
 \delta=\chi_0^7\beta^{-1},\qquad
 \tau=(\chi_0|_{\mathbb A_F^\times})\eta_1^{-1}.
\tag{ER18}
\]
The norm pulls local units to local units. Thus β is unramified everywhere finite and its infinity component is \(a^7\). It follows that δ is an ordinary class character of K. Likewise τ is an ordinary class character of F, because the infinity component of \(\chi_0|_F\) is the product of signs, exactly that of \(\eta_1\).

The quadratic base-change identity gives
\[
                \beta|_{\mathbb A_F^\times}
             =\eta_0\circ N_{F/F_0}=\eta_1.
\tag{ER19}
\]
It can also be checked locally here. At a finite prime of F₀ where E₀ splits, both sides are trivial. At an inert finite prime E₀/F₀ is unramified quadratic; after a residue extension of degree f it splits precisely when f is even. The unramified value of \(\eta_0\) on the norm of a uniformizer is \((-1)^f\), the same as the new quadratic character. Both sides are trivial on units. At infinity the norm and sign give the same product of local signs. This proves (ER19), including primes where F/F₀ itself is ramified.

Let \(j:\mathrm{Cl}(F)\to\mathrm{Cl}(K)\) be extension of ideals. From (ER18)–(ER19),
\[
                                  \delta\circ j=\tau^7.
\tag{ER20}
\]
The kernel of j has exponent dividing two: applying the ideal norm to an extended ideal gives its square. If x lies in this kernel, then (ER20) gives \(\tau(x)^7=1\), while \(x^2=1\) gives \(\tau(x)^2=1\). Therefore \(\tau(x)=1\). Thus \(\tau^{-1}\) is a well-defined character on \(\operatorname{im}j\).

Every character of a subgroup of a finite abelian group extends to the whole group: adjoining one generator at a time, choose a root of the specified value of its least positive power lying in the previous subgroup. All these values remain roots of unity. Apply this to obtain a class character \(\lambda\) of K with
\[
                                   \lambda\circ j=\tau^{-1}.
\tag{ER21}
\]
Finally set
\[
                                      \eta=\chi_0\lambda.
\tag{ER22}
\]
It is unitary, unramified at every finite place, has infinity component a, and its restriction to F is \(\tau\eta_1\tau^{-1}=\eta_1\). This proves all four literal `IsEtaT` clauses. The argument has handled the capitulation compatibility explicitly; it has not inferred `ResEta` merely from the unit condition.

## 6. A single finite coefficient field for etaVal

The finite values required in the source are normalized by \((NP)^{-1/2}\). Their common algebraicity can be built into the preceding construction.

Define the algebraic type norm
\[
                T(x)=\prod_{\phi\in\Phi_0}\phi(N_{K/E_0}x)\in E_0^\times.
\tag{ER23}
\]
Since E₀ is Galois, every factor and the product lie in E₀. For the chosen complex embedding,
\[
              a(x)=\frac{T(x)}{\sqrt{N_{K/\mathbb Q}x}},
\tag{ER24}
\]
where the norm is positive because K is CM. In particular \(T(U)=1\) on every unit by (ER13).

The principal-ideal rule \(\psi((x))=T(x)^{-1}\) is therefore well-defined. Extend it to all ideals by the cyclic-class construction of §4, choosing only the finitely many roots
\[
                         \psi(\mathfrak a_j)^{h_j}=T(x_j)^{-1}.
\tag{ER25}
\]
All ψ-values then lie in one finite extension of E₀. Every chosen root has complex absolute value \((N\mathfrak a_j)^{-1/2}\), since \(\mathfrak a_j^{h_j}=(x_j)\); the same absolute-value identity holds on all ideals. Thus
\(c(I)=\psi(I)\sqrt{NI}\) is the unitary ideal character used to construct \(\chi_0\).

The correcting class character λ has finite order. Adjoining its finitely many root-of-unity values, one obtains a fixed finite coefficient field containing
\[
                        \eta(\varpi_P)(NP)^{-1/2}
                                      =\psi(P)\lambda(P)
\tag{ER26}
\]
for every finite prime P. Closing that field under conjugation is still a finite extension. This supplies the existence part of the source `etaVal` condition, with its exact `valTw(1/2)` normalization. No bound for the necessary class orders or this coefficient field is part of the theorem.

## 7. Persistence under further real extensions and remaining host work

The repaired character persists under any further totally real extension \(F_1/F\). Put \(K_1=KF_1\), use the induced CM type, and pull η back by \(N_{K_1/K}\). Its infinity exponent remains one at every induced embedding, its finite components remain unramified, and the same local quadratic base-change check proves the exact restriction \(\eta_{K_1/F_1}\). Thus the character obstruction need not be solved again when a further real extension is required for other numerical host conditions.

This construction concerns the ordinary type of a possible \(J^{14}\) host. It proves the auxiliary character and its normalized value field, with no assertion here that the full integral polarized lattice is the standard product lattice or that all old source real, rank, tensor, and size records are instantiated. Those additional comparisons must retain their own finite and archimedean costs. The degree-seven step repairs one actual previously impossible field of the source adapter; it does not complete the GRH extension or the MainX window.

## 8. Primary references and precise use

- Masley, J. M. (1978). Class numbers of real cyclic number fields with small conductor. *Compositio Mathematica, 37*(3), 297–319. Table 3, printed p.316, conductor28/degree6 row: \(h(F_0)=1\). Primary PDF: https://numdam.org/item/CM_1978__37_3_297_0.pdf. The table image was inspected directly, rather than relying on search snippets or a secondary class-number list.
- Milne, J. S. (2020). *Class field theory* (Version4.03, 6 August 2020). Chapter V, Proposition4.12, pp.177; Proposition5.2 and Theorem5.3, pp.178–179: the quadratic Artin character, its local restrictions, principal-idele triviality, and norms. https://www.jmilne.org/math/CourseNotes/CFT.pdf. Only these standard class-field inputs are used; the unit generation, character-extension, and capitulation correction are proved above.
- Accepted DP57 and AM-DO-022: the original ordinary J² field/type and finite-unramified CM extension E₀/F₀. AM-K028: exact source `HasInf`, `UnrAt`, `ResEta`, `IsEtaT`, and `etaVal` conventions and their provenance.

The exact finite arithmetic checks are separate from the proof of character existence. No Lean compilation, new analytic L-function theorem, large-field class-number computation, or effective coefficient-height estimate is claimed.
