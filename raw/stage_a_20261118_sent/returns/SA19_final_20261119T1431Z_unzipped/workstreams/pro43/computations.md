# Pro cote 43: proofs, computations and explicit limits of the checks

Run: GPT-6 Astra Pro, November 19, 2026. Source: cote 43, scans 94–142, aggregate transcription lines 1–1871. This file distinguishes an independent proof from a finite computational illustration. The program `scripts/calculations.py` and its complete output `outputs/calculations.txt` contain every finite calculation reported here. Source-download and OCR programs are separately retained under `scripts/` with their outputs. None of the algebraic examples below is represented as additional manuscript text.

The notation `CL-n` below abbreviates `CL-SA19-nnn`. Citations use the keys in `references.bib`; they identify the precise primary result used, not a claim to have checked every proof in the work. A sheaf Ext, a global Ext, Yoneda Ext among algebraic groups, and Ext in a perfected group category are different objects throughout.

## 1. Derived sections, injectives and the conditional spectral sequences

**Claims:** CL-002, 003, 009–012, 025, 057–058. **Source:** 43/94, 97–98, 109, 128.

Let \(\mathcal T\) be a topos and let \(\mathbf Z_{\mathcal T}\) be the free abelian sheaf on its terminal object. For every abelian sheaf \(F\), a morphism \(\mathbf Z_{\mathcal T}\to F\) is uniquely specified by the image of 1; hence
\[
\Gamma(\mathcal T,F)=\operatorname{Hom}_{\mathcal T}(\mathbf Z_{\mathcal T},F).
\]
Taking an injective resolution gives \(H^i(\mathcal T,F)=\operatorname{Ext}^i(\mathbf Z_{\mathcal T},F)\). This proves the formal identity, after specifying an actual topos. It does not prove that the candidate category on scan 94 is a site with all the properties subsequently used.

If \(L\dashv R\) are functors between abelian categories and \(L\) is exact, then \(R\) preserves injectives: for a monomorphism \(M\hookrightarrow N\), exactness of \(L\) and injectivity of \(I\) make
\(\operatorname{Hom}(LN,I)\to\operatorname{Hom}(LM,I)\) surjective; adjunction identifies this with the extension property for \(RI\). Thus direct image for an ordinary morphism of topoi preserves injectives, since its inverse image is exact. This argument does **not** automatically apply to a premorphism of sites or to the proposed Néron realization.

For left exact \(R\) and \(\Gamma\), the composite-functor spectral sequence exists if \(R\) takes injectives to \(\Gamma\)-acyclic objects. Preservation of injectives suffices, but is stronger than necessary. Grothendieck (1957, Theorem 2.4.1, printed p. 148; `Grothendieck1957`) supplies this precise conditional statement. The downloaded Tôhoku extract ends at p. 184; its §4.2 was **not** directly read and is not an independent verification here. Modern realization-specific acyclicity is instead checked in Suzuki (2020, §§2.4 and 3.4; `Suzuki2014`).

For local-to-global Ext, the usual spectral sequence has \(E_2^{p,q}=H^p(\underline{\operatorname{Ext}}^q(F,G))\). Collapse to a single row is legitimate only after proving the internal Ext vanishings and the required acyclicity. This is exactly what fails to follow merely from the scratch table on scans 119–120.

## 2. Why infinite Witt coordinates obstruct naive filtered continuity

**Claims:** CL-007–008. **Source:** 43/96–97. **Attribution:** independent countermodel for the author's explicit withdrawal; not an identification of the uncertain \(V\).

Fix a prime \(p\). Put \(k_m=\mathbf F_p(x_1,\ldots,x_m)^{\mathrm{perf}}\), with compatible inclusions, and \(k=\bigcup_m k_m\). The underlying set of the infinite Witt functor is \(W(k)=k^{\mathbf N}\). The Witt vector with coordinates \((x_1,x_2,\ldots)\) belongs to \(W(k)\) but to no \(W(k_m)\): its \((m+1)\)-st coordinate is transcendental over \(k_m\). Consequently \(\varinjlim_m W(k_m)\to W(k)\) is not surjective.

In contrast, a length-\(n\) Witt vector has only finitely many coordinates. Every such vector over a filtered union occurs at a common stage, and equality of two vectors occurs at a later common stage. The polynomial coordinate laws then give \(W_n(\varinjlim k_m)=\varinjlim W_n(k_m)\). The program records finite coordinate bounds only. The infinite non-surjectivity follows from the preceding argument, not from checking finitely many lengths.

Suzuki's rational/ind-rational constructions (`Suzuki2013`, §2.1; `Suzuki2014`, §§2–3) supply carefully defined alternatives. They are not evidence that the withdrawn continuity on the manuscript holds after all.

## 3. Field coefficient rows: Kummer, Artin–Schreier and Frobenius

**Claims:** CL-019, 023, 029–032. **Source:** 43/104, 109, 112.

For a characteristic-\(p\) field \(K\), the exact fppf sequences
\[
0\to\mu_p\to\mathbf G_m\xrightarrow{p}\mathbf G_m\to0,
\qquad
0\to\alpha_p\to\mathbf G_a\xrightarrow{F}\mathbf G_a\to0
\]
and vanishing of \(H^1(K,\mathbf G_m)\) and positive-degree quasi-coherent cohomology yield
\[
H^1(K,\mu_p)=K^\times/K^{\times p},\qquad
H^1(K,\alpha_p)=K/K^p.
\]
The first quotient is multiplicative, the second additive. Both group schemes have only their identity as a \(K\)-point; this does not make them zero fppf sheaves. The Artin–Schreier exact sequence, already étale,
\[
0\to\mathbf Z/p\to\mathbf G_a\xrightarrow{F-1}\mathbf G_a\to0
\]
gives \(H^1(K,\mathbf Z/p)=K/(F-1)K\). See `Stacks03PK`, `Stacks0A3J`, and Milne (2006, III §§5–6; `Milne2006`).

For \(K=\mathbf F_p(t)\), the valuation at \(t=0\) of a nonzero \(p\)-th power is divisible by \(p\), while \(v_t(t)=1\). Thus \(t\) gives nonzero classes in both relevant \(p\)-power quotients. After passing to \(K^{\mathrm{perf}}\), those classes vanish. Perfectness of a residue field therefore does not justify replacing an imperfect fraction field by its perfection in flat cohomology.

For a complete discrete valuation field with algebraically closed residue field \(k\), and \(n\) prime to \(\operatorname{char}k\), every unit is an \(n\)-th power. First choose a root of its residue in \(k\); then Hensel's lemma lifts that root because the derivative \(nX^{n-1}\) is invertible at the root. The valuation therefore induces \(K^\times/K^{\times n}\cong\mathbf Z/n\), and all \(n\)-th roots of unity lift from \(k\). Without the algebraically closed residue-field hypothesis, the unit quotient and residue Galois terms need not disappear.

## 4. The finite prime-to-characteristic multiplicative Ext calculation

**Claims:** CL-024–028. **Source:** 43/109.

Work over an algebraically closed field of characteristic \(p\), in the category for which the proalgebraic/perfected Ext comparison has been established. Suzuki (`Suzuki2014`, §2.4) identifies the relevant \(\operatorname{Ext}^1(G,\mathbf Q/\mathbf Z)\) with continuous torsion characters of the étale Tate module. For \(G=\mathbf G_m\) and \((n,p)=1\),
\[
\operatorname{Hom}_{\mathrm{cont}}(T\mathbf G_m,\mu_n)
=\operatorname{Hom}(\mu_n,\mu_n)=\mathbf Z/n,
\]
where the maps are powers; and
\[
\operatorname{Hom}_{\mathrm{cont}}(T\mathbf G_m,\mathbf Z/n)
=\operatorname{Hom}(\mu_n,\mathbf Z/n)=\mu_n^\vee.
\]
Over a general base field these expressions carry the indicated Galois action. Choosing a primitive root trivializes a twist, but does not give a canonical trivialization. The Kummer extension represents the power-map generator in the first calculation. In a perfected category \(\mu_p\) disappears; the displayed argument consequently proves no corresponding all-\(n\) internal fppf Ext table. The character group of the abstract group \(k^\times\) is another object again.

## 5. Normal closures of decomposition and inertia subgroups

**Claims:** CL-034–035. **Source:** cancelled 43/113.

Let \(L/K\) be a Galois extension, possibly infinite, with profinite group \(G\). Choose places and their decomposition subgroups \(D_v\). Put \(H=\overline{\langle gD_vg^{-1}:g\in G,v\rangle}\). For an intermediate Galois extension \(E=L^N\), the decomposition group of a selected place in \(E/K\) is the image of \(D_v\) in \(G/N\). It is trivial exactly when \(D_v\subset N\). Since \(N\) is closed and normal, this holds for every selected place exactly when \(H\subset N\), or equivalently \(E\subset L^H\). Thus \(L^H\) is the largest intermediate Galois extension in which these places split completely.

The same argument with inertia groups \(I_v\) gives the largest intermediate Galois extension unramified at the selected places. It assumes the places and their subgroups are already specified. It proves no recovery of inertia from an abstract group. This distinction separates the valid elementary reconstruction from the earlier run's external-project leads.

## 6. The rank \(2a+t\) and its excluded \(p\)-adic reading

**Claim:** CL-041. **Source:** 43/117.

Let \(0\to T\to G\to B\to0\) be a semiabelian variety over an algebraically closed field, with \(\dim B=a\) and \(T\cong\mathbf G_m^t\). For \(\ell\ne p\), multiplication by \(\ell^n\) is surjective on \(T\); the snake lemma gives
\(0\to T[\ell^n]\to G[\ell^n]\to B[\ell^n]\to0\).
The transition maps are surjective, so inverse limits preserve exactness. The outer Tate modules are free of ranks \(t\) and \(2a\), giving \(\operatorname{rank}_{\mathbf Z_\ell}T_\ell G=2a+t\).

In characteristic \(p\), the étale \(p\)-Tate module of the torus is zero, and that of \(B\) has rank its \(p\)-rank, which can be less than \(2a\). A full \(p\)-divisible group is a different object. The page's \(\mu\) therefore needs an explicit prime-to-\(p\) interpretation before the arithmetic is valid. The finite isogeny and \(p\)-divisible distinctions are recorded in Oda (1969, §1; `Oda1969`).

## 7. What the abelian-variety Kummer–Ext calculation actually proves

**Claims:** CL-042–045. **Source:** 43/119–120.

Let \(A/S\) be an abelian scheme and \(B=A^\vee\). In the category of fppf abelian sheaves, Barsotti–Weil gives \(\underline{\operatorname{Ext}}^1(A,\mathbf G_m)=B\), while \(\underline{\operatorname{Hom}}(A,\mathbf G_m)=0\). Ribeiro and Rosengarten (first circulated 2025; revised 2026, Theorem 4.3; `RibeiroRosengarten2025`) prove \(\underline{\operatorname{Ext}}^2(A,\mathbf G_m)=0\) over an arbitrary base.

Apply derived Hom to the fppf Kummer sequence. Its low-degree segment is
\[
0\to\underline{\operatorname{Ext}}^1(A,\mu_n)\to B
\xrightarrow{n}B\to\underline{\operatorname{Ext}}^2(A,\mu_n)\to0.
\]
Multiplication by \(n\) on an abelian scheme is an fppf epimorphism. Therefore
\[
\underline{\operatorname{Hom}}(A,\mu_n)=0,\quad
\underline{\operatorname{Ext}}^1(A,\mu_n)=B[n],\quad
\underline{\operatorname{Ext}}^2(A,\mu_n)=0.
\]
The next segment identifies \(\underline{\operatorname{Ext}}^3(A,\mu_n)\) with the kernel of \(n\) on \(\underline{\operatorname{Ext}}^3(A,\mathbf G_m)\). It supplies no general zero. The same source explicitly notes higher Ext nonvanishing in characteristic 2. Breen's older characteristic-dependent ranges (`Breen1975`) cannot be replaced by unlimited vanishing.

The local-to-global spectral sequence now gives the **global degrees 1 and 2**:
\[
\operatorname{Ext}^1(A,\mu_n)=H^0(S,B[n]),\qquad
\operatorname{Ext}^2(A,\mu_n)=H^1(S,B[n]).
\]
For total degree 3, an additional \(E_2^{0,3}\) term can occur, together with subsequent differentials. Consequently the all-degree formula \(\operatorname{Ext}^i=H^{i-1}(B[n])\) is not proved. Passing from \(\mu_n\) to \(\mu_\infty\) also requires a continuity theorem; the finite calculation alone supplies none.

## 8. Kummer limits, torsion of torsors and geometric divisibility

**Claims:** CL-047, 050. **Source:** 43/119–120.

For an abelian variety \(B/K\), finite Kummer gives
\[
0\to B(K)/nB(K)\to H^1(K,B[n])\to H^1(K,B)[n]\to0.
\]
For \(n\mid mn\), the map on the first term is multiplication by \(m\), on the middle term the inclusion \(B[n]\hookrightarrow B[mn]\), and on the last term the natural inclusion of torsion subgroups. To see the first map, an \(n\)-division point of \(b\) is also an \(mn\)-division point of \(mb\), with the same cocycle.

Every class of \(H^1(K,B)\) is torsion. A torsor under the smooth group \(B\) has a closed point separable over \(K\) after choosing a point in its nonempty smooth locus, so it becomes trivial over a finite separable extension. Restriction followed by corestriction multiplies its class by that extension's degree. Equivalently one may use the usual finite-extension transfer for the abelian Galois cohomology of \(B(K^{\mathrm s})\). Taking filtered colimits, which are exact for abelian groups, yields
\[
0\to B(K)\otimes\mathbf Q/\mathbf Z\to H^1(K,B_{\mathrm{tors}})
\to H^1(K,B)\to0.
\]
Continuity of degree-one cohomology here can also be read on continuous cocycles: their compact-domain image in a discrete torsion union is finite, hence occurs at a finite stage. For the full flat torsion system this is the usual finite-presentation/flat Kummer formulation. No canonical homomorphism from \(B(K)\) itself to the first term is asserted; an embedding into \(\mathbf Q/\mathbf Z\) is not specified by the integer 1.

For the **geometrized local** groups, Suzuki (`Suzuki2014`, Proposition 3.4.3(b,d)) gives \(\mathbf H^2(K,A[n])=0\). The realized Kummer long exact sequence therefore makes \(n:\mathbf H^1(K,A)\to\mathbf H^1(K,A)\) an epimorphism. Any component quotient inherits divisibility. This is not a statement about units of an arithmetic ring, and not an assertion about arbitrary ordinary \(H^2\) over an unrelated field.

## 9. Divisibility and torsion-free character duals

**Claim:** CL-051. **Source:** 43/120.

For an abelian group \(D\), let \(D^*=\operatorname{Hom}(D,\mathbf Q/\mathbf Z)\). Its \(n\)-torsion is canonically
\[
D^*[n]=\operatorname{Hom}(D/nD,\mathbf Q/\mathbf Z).
\]
If \(nD=D\), this vanishes. Conversely, \(\mathbf Q/\mathbf Z\) is an injective cogenerator: every nonzero cyclic subgroup of a nonzero group maps nontrivially to \(\mathbf Q/\mathbf Z\), and injectivity extends that map. Thus vanishing forces \(D/nD=0\). Applying this for every \(n\) proves that \(D\) is divisible if and only if \(D^*\) is torsion-free. In the discrete torsion case, this is compatible with the compact Pontryagin topology. Serre duality of proalgebraic groups needs its own categorical version; it cannot simply be identified with abstract Hom without a comparison.

## 10. The complete DVR calculation and the finiteness obstruction

**Claims:** CL-053–056. **Source:** 43/123, 125. **Attribution:** the DVR model is an earlier-run suggestion independently verified here.

Put \(R=k[[t]]\), \(K=k((t))\), \(M_n=R/t^nR\). The resolution
\(0\to R\xrightarrow{t^n}R\to M_n\to0\)
gives \(\operatorname{Hom}_R(M_n,R)=0\), \(\operatorname{Ext}^1_R(M_n,R)=R/t^nR\), and higher Ext zero. The surjection \(M_{n+1}\to M_n\) lifts to the identity in degree 0 and multiplication by \(t\) in degree 1. Since Ext is contravariant in its first argument, the induced direct-system map is
\[
R/t^n\xrightarrow{\,t\,}R/t^{n+1}.
\]
The compatible map \(a\bmod t^n\mapsto a/t^n\bmod R\) identifies its colimit with \(K/R\).

Any \(R\)-linear endomorphism of \(K/R\) preserves its \(t^n\)-annihilator \(t^{-n}R/R\). The latter is cyclic, so the restriction is multiplication by an element \(a_n\in R/t^n\). Compatibility means \(a_{n+1}\equiv a_n\pmod {t^n}\). Conversely every compatible family acts on the union. Hence
\(\operatorname{End}_R(K/R)=\varprojlim R/t^n=R\).
This agrees with Matlis (1958, Theorem 3.7, pp. 522–523; `Matlis1958`); completeness is visible in the final equality. The program checks the finite transition matrices commute with multiplication by \(t\), are injective, and that the endomorphism algebra of the length-\(n\) Jordan module has dimension \(n\), for \(1\le n\le8\). The infinite statements follow from the explicit formulas, not those tests.

A useful cross-stream obstruction is the root agent's example with first argument \(K\). Every map \(K\to t^{-n}R/R\) is zero: for \(x\in K\), write \(x=t^ny\), then its image is \(t^n f(y)=0\). But \(K\to K/R\) is a nonzero quotient map. Thus Hom from this nonfinite module fails to commute with the displayed filtered colimit. This explains why the coherent first-argument hypothesis in SGA2 VI, Theorem 2.3 (recomposed pp. 59–60; `SGA2`) matters. Neither an unrestricted Hom-colimit interchange nor an underived inverse-limit duality follows from the page.

## 11. Curve Kummer rows and the Picard obstruction

**Claims:** CL-062–066. **Source:** 43/132–133.

Let \(C/k\) be a smooth proper geometrically connected curve over an algebraically closed field and \(J=\operatorname{Pic}^0(C)\). For \((n,p)=1\), Kummer and \(\operatorname{Br}(C)=0\) give
\[
H^0(C,\mu_n)=\mu_n(k),\quad H^1(C,\mu_n)=\operatorname{Pic}(C)[n]=J[n](k),
\quad H^2(C,\mu_n)=\operatorname{Pic}(C)/n=\mathbf Z/n.
\]
Indeed the degree quotient of Pic is \(\mathbf Z\), while multiplication by \(n\) on \(J(k)\) is surjective. Untwisting \(\mu_n\) gives the \(\mathbf Z/n\) row with \(\mu_n^\vee\) in degree 2 and \(J[n]\otimes\mu_n^\vee\) in degree 1. These are the exact arguments in `Stacks03RN`, Lemma 59.69.1, with Kummer exactness from `Stacks03PK`.

For the manuscript's **relative** notation, the same formal long exact sequence gives \(R^0f_*\mu_p=\mu_p\) and \(R^1f_*\mu_p=\operatorname{Pic}_{C/k}[p]=J[p]\), because multiplication by \(p\) on the relative \(\mathbf G_m\) is an fppf epimorphism. The degree term gives \(R^2f_*\mu_p=\mathbf Z/p\) when the chosen realization has the asserted vanishing of \(R^2f_*\mathbf G_m\). Suzuki (`Suzuki2018`, Proposition 3.1.1) proves the latter in his ind-rational realization; Artin–Milne (1976, §4; `ArtinMilne1976`) uses a perfect test-site. On that perfect test-site the infinitesimal sheaf \(\mu_p\), and the infinitesimal part of \(J[p]\), are invisible. These references must not be read as proving an identification of the full big-fppf group-scheme row with the perfected row. The full relative \(p\)-row is accordingly recorded as conditional on the specified relative realization, while its values on algebraically closed fields follow directly from flat Kummer.

For a general field \(k\), the Leray low-degree sequence contains
\[
0\to\operatorname{Pic}(C)\to\operatorname{Pic}_{C/k}(k)
\to\operatorname{Br}(k)\to\operatorname{Br}(C).
\]
The middle map is a descent obstruction. A \(k\)-point of \(C\) splits pullback \(\operatorname{Br}(k)\to\operatorname{Br}(C)\), so kills that obstruction; without such an argument the inclusion need not be equality. Full Pic, with its degree component, is required for the \(H^2\) calculation. Replacing it by \(\operatorname{Pic}^0\) destroys the \(\mathbf Z/n\) term.

## 12. The curve \(\mathbf Z/p\) and \(\alpha_p\) rows

**Claims:** CL-067–068. **Source:** 43/133.

Over an algebraically closed field, \(H^0(C,\mathcal O_C)=k\), \(H^2(C,\mathcal O_C)=0\), and both \(F:k\to k\) and \(F-1:k\to k\) are surjective. The respective long exact sequences therefore give
\[
H^1(C,\mathbf Z/p)=\ker(F-1:H^1(C,\mathcal O_C)\to H^1(C,\mathcal O_C)),
\]
\[
H^2(C,\mathbf Z/p)=\operatorname{coker}(F-1)=0,
\]
and
\[
H^1(C,\alpha_p)=\ker F,\qquad H^2(C,\alpha_p)=\operatorname{coker}F.
\]
The \(\alpha_p\) cohomology is fppf. In the relative formulation its degree-zero sheaf is \(\alpha_p\); on field points it is zero.

For completeness, write a Frobenius-semilinear operator on \(k^g\) as \(F(v)=Av^{[p]}\). The additive polynomial map \(v\mapsto F(v)-v\) has derivative \(-I\), so is étale and open. Its image on an algebraically closed field is a constructible subgroup containing a nonempty open subset; an open subgroup of the connected algebraic group \(\mathbf G_a^g\) is the whole group. This proves surjectivity. Its kernel is zero-dimensional and finite, since an étale finite-type fibre is a zero-dimensional finite-type scheme. This is the mechanism in `Stacks0A3L`; it does not say that \(F\) itself is surjective.

The program's rank-one examples \(F=1\) and \(F=0\) illustrate the ordinary and supersingular linear parts. Its \(F-1\) calculations over the **finite set** \(\mathbf F_3\) are expressly not a proof of algebraic-closure surjectivity: \(x^3-x\) vanishes on \(\mathbf F_3\) but is surjective on its algebraic closure.

## 13. The constant \(\mathbf Z\) row and the shift test

**Claims:** CL-069–070, 075. **Source:** 43/133.

In the ordinary geometric étale setting where rational constant cohomology is acyclic in positive degrees, \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\) gives \(H^1(C,\mathbf Z)=0\) and
\[
H^i(C,\mathbf Z)=H^{i-1}(C,\mathbf Q/\mathbf Z),\qquad i\ge2.
\]
The prime-to-\(p\) part of \(H^2(C,\mathbf Q/\mathbf Z)\) is the colimit of \(\mu_n^\vee\), and the \(p\)-part is zero. For the last assertion, use the \(\mathbf Z/p\) calculation of §12 and successive exact sequences for \(\mathbf Z/p^r\), then the usual étale filtered-cohomology continuity. A change to an exotic site requires its own rational acyclicity and continuity theorem; these are hypotheses, not purely formal consequences of the short exact sequence.

The Abel–Jacobi identification of \(\pi_1(C)^{\mathrm{ab}}\) with \(\pi_1(J)\) is proved by the symmetric-power/projective-bundle argument in SGA1 IX, Remark 5.8, final paragraph (recomposed p. 194; original pp. 252–253; `SGA1`). Therefore \(H^1(C,\mathbf Q/\mathbf Z)\) consists of continuous characters of the **étale** Tate module of \(J\). This does not identify the full finite flat group \(J[p]\).

Our cohomological convention is \(H^i(K[1])=H^{i+1}(K)\). Thus a complex concentrated in degrees 0 and 1 becomes concentrated in degrees \(-1,0\) after \([1]\), and in degrees \(1,2\) after \([-1]\). The opposite shifts written on scan 133 cannot yield the same unshifted degree table under a single fixed convention. This is a mathematical alarm; it does not decide the ink.

## 14. A complete counterexample to the full-group-scheme reading of \(\pi_1/p=J[p]\)

**Claim:** CL-071; refined statement CL-070. **Source:** 43/133, lines 1580–1583. **Attribution:** current independent reconstruction, not a counterexample written by him.

Let \(k=\overline{\mathbf F}_3\) and let \(E\) be the projective cubic
\[
Y^2Z-X^3+XZ^2=0.
\]
Its partial derivatives in characteristic 3 are \(Z^2,2YZ,Y^2+2XZ\). If all vanish, then \(Z=0\), then \(Y=0\), and the equation forces \(X=0\), impossible in projective space. Thus \(E\) is smooth over the algebraic closure, not just smooth at its rational points. It is proper; a smooth projective plane cubic with the point \([0:1:0]\) is a geometrically connected genus-one curve and its own Jacobian.

On \(y^2=x^3-x\), the regular differential \(\omega=dx/y\) spans \(H^0(E,\Omega^1)\). Since \(1/y=(x^3-x)/y^3\),
\[
\omega=y^{-3}(x^3-x)\,dx.
\]
Cartier satisfies \(C(f^3\eta)=fC(\eta)\); on the separating coordinate \(x\), only exponents congruent to 2 modulo 3 survive in \(C(x^i dx)\). The exponents here are 3 and 1, so \(C(\omega)=0\). Serre duality identifies Frobenius on \(H^1(E,\mathcal O_E)\) with the transpose of Cartier; hence that Frobenius is zero. These are the same differential/Dieudonné conventions used in Oda (1969, §5, especially the Cartier discussion and Corollary 5.11; `Oda1969`). The program independently checks the partial derivatives and the missing \(x^2\) coefficient.

By §12, \(H^1_{\mathrm{et}}(E,\mathbf Z/3)=\ker(-1)=0\), so the maximal elementary abelian étale 3-quotient is trivial. On the other hand \(E[3]\) is finite flat of rank \(3^{2\dim E}=9\). A trivial étale quotient cannot be this nontrivial finite group scheme. Every smoothness/properness/connectedness hypothesis of the reconstructed curve claim is met. The correction is to take the appropriate étale realization and dual; the missing marker on the manuscript remains undecided.

## 15. Cartier annihilators, Frobenius twists and the \(\alpha_p\) assertion

**Claims:** CL-072–073. **Source:** 43/133; companions cote 54/3–7 and cote 44/8–9 read separately.

For a perfect pairing of finite commutative group schemes \(G\times G^D\to\mathbf G_m\), Cartier duality is an exact contravariant anti-equivalence. If \(f:H\to G\), dualize its image/kernel factorization. The resulting exact sequences give
\[
(\operatorname{im}f)^\perp=\ker D(f),\qquad
(\ker f)^\perp=\operatorname{im}D(f)
\]
in their respective ambient duals. These universal identities are safer than changing a printed \(F\) to \(V\) by intuition.

For an abelian variety \(A\), relative Frobenius is \(F_A:A\to A^{(p)}\); its dual is \(V_{A^\vee}:(A^\vee)^{(p)}\to A^\vee\). Conversely \(D(V_A)=F_{A^\vee}\), with the twists retained. If restricting the \(p\)-Weil pairing on \(A[p]\times A^\vee[p]\), the annihilator of \(\ker F_A\) in \(A^\vee[p]\) is the kernel of the resulting map to \((\ker F_A)^D\), which identifies with \(\ker F_{A^\vee}\) after the factorization through \(\ker V_{A^\vee}\). This is compatible with \((\ker F_A)^D\cong\ker V_{A^\vee}\); the two sentences refer to a quotient and an annihilator, respectively. They must not be conflated.

Oda (1969, Definition 3.5, p. 82) writes the dual Dieudonné module as \(DM=\operatorname{Hom}_W(M,\operatorname{Frac}W/W)\), with
\[
(Fa)(x)=\sigma(a(Vx)),\qquad (Va)(x)=\sigma^{-1}(a(Fx)).
\]
Proposition 3.13 (p. 86) identifies \(M(G^{(p)})=(W,\sigma)\otimes_WM(G)\) and spells out the maps. Corollary 3.16 and Theorem 3.19 (pp. 88–89) identify the anti-equivalence and Cartier duality. These are exact primary conventions, rather than a linear algebra substitution without twists.

The full subcategory killed by both \(F\) and \(V\) consists of \(\alpha_p\)-power groups. Under exact duality, the largest subgroup in this subcategory becomes the largest quotient in the dual subcategory: any competing quotient dualizes to a subgroup and factors through the maximal one. A chosen self-duality identifies the two ambient groups; tangent spaces of \(\alpha_p^r\) are ordinary dual vector spaces. This proves the maximal-subgroup/maximal-quotient assertion, but implies neither a positivity theorem nor integral descent of a polarization to an arbitrary quotient.

## 16. Localization and the missing quotient in local support cohomology

**Claims:** CL-076–082. **Source:** 43/135–138.

For an ordinary étale topos, an open immersion \(j:U\hookrightarrow X\) and closed complement \(i:Y\hookrightarrow X\) give
\(0\to j_!j^*F\to F\to i_*i^*F\to0\).
At a geometric point of \(U\), this is \(0\to F_{\bar x}\to F_{\bar x}\to0\); at one of \(Y\), it is \(0\to0\to F_{\bar x}\to F_{\bar x}\to0\). Geometric stalks detect exactness. Since \(j_!\) is exact and left adjoint to restriction, derived adjunction gives the corresponding Ext comparison. This proof uses an ordinary topos, not an undefined realization functor.

The support triangle is
\[
R\Gamma_Y(X,F)\to R\Gamma(X,F)\to R\Gamma(U,F)\to R\Gamma_Y(X,F)[1].
\]
If \(H^m(X,F)=H^{m+1}(X,F)=0\), it yields
\(H^m(U,F)\cong H^{m+1}_Y(X,F)\).
There is a shift, and two neighboring vanishings are needed. For a valuation ring and its fraction field the degree-two support term in the finite-flat realization is
\[
\mathbf H^2_x(\mathcal O_K,N)
=\operatorname{coker}\bigl(\mathbf H^1(\mathcal O_K,N)\to\mathbf H^1(K,N)\bigr)
\]
under the remaining vanishings proved in Suzuki (`Suzuki2014`, Proposition 3.4.6). It equals the whole field \(\mathbf H^1\) only with an additional zero-image assertion. Henselian/completion comparison is supplied for smooth and finite-flat coefficients by `Suzuki2018`, Proposition 2.6.2; Remark 2.7.9 explicitly rules out unrestricted extension to every fppf sheaf.

Prime-to-\(p\) codimension-one purity gives the two-degree shift and Tate twist, as recorded in SGA2 XIV §2.3. Wild flat coefficients require the additional flat-duality theory; the source itself narrows the easy coefficient range on scan 135.

## 17. Counterexample to the unshifted boxed support/open comparison

**Claim:** CL-083; refined statement CL-082. **Source:** 43/140. **Attribution:** current independent test of a literal ordinary interpretation.

Let \(k\) be algebraically closed, \(\ell\ne\operatorname{char}k\), \(X=\mathbf P^1_k\), \(U=\mathbf A^1_k\), \(Y=\{\infty\}\), and \(G=\mathbf Z/\ell\) on \(U\). These are a smooth proper geometrically connected curve, an open complement of one closed point, and a finite étale coefficient. Every stalk of \(j_!G\) on \(Y\) is zero. A global section supported on \(Y\) therefore has zero stalk everywhere and is zero; hence
\[
H^0_Y(X,j_!G)=0.
\]
But \(U\) is connected, so \(H^0(U,G)=\mathbf Z/\ell\ne0\). Thus the boxed unshifted comparison is false already in degree zero in ordinary étale cohomology. This does not decide the unspecified underlined relative notation or change the transcription. The valid conditional shifted statement is §16.

## 18. Atiyah's connectivity inequality

**Claims:** CL-085–089. **Source:** reused typescript 43/103, 101; published match `Atiyah1961`, Theorems 6.2 and 6.5 and Lemmas 6.3–6.4, p. 308.

Starting with \(r=d(n-k+1)-2\),
\[
2r\ge dn-2
\iff 2dn-2dk+2d-4\ge dn-2
\iff n\ge2(k-1)+2/d.
\]
For \(d=1,2,4\), the integer thresholds are respectively \(2k\), \(2k-1\), and \(2k-1\). The program verifies this equivalence for all \(1\le k\le20\), \(k\le n<80\); the displayed rearrangement proves it for all integers. The source's final theorem imposes its own real range \(n\ge2k\), and uses earlier divisibility information for the other cases. No finite enumeration proves those homotopy-theoretic lemmas or the order of a \(J\)-group element.

The explicit numerical cross-section programme has later primary solutions: the accessible Adams–Walker (1965) publisher extract states the complex sufficiency theorem, and Sigrist–Suter (1973, main theorem pp. 247–248, Theorem 2.6 p. 253) gives the quaternionic criterion. Their conclusions do not prove equality of Atiyah's particular intrinsic-join dual map and diagonal Thom map on p. 309. That separate question remains an identified question whose ultimate resolution was not located.

## 19. The multiplicity counterexample and the different associated-prime question

**Claims:** CL-091–094. **Source:** 43/110. **Published comparison:** EGA IV3, 12.2.1(xi), 12.2.1.4, 12.2.2(iii), and 12.2.3(vi), pp. 179–183.

Take \(R=k[[t]]\), \(X=Y=\operatorname{Spec}R\), \(f=\mathrm{id}\), and \(\mathcal F\) associated to \(R\oplus k\). The identity is proper, finite type and universally open. The sheaf is coherent and has full support. The sole component of \(X\) dominates \(Y\). Both fibres are zero-dimensional; every finite module over a field satisfies \(S_1\), so the special-fibre hypothesis holds. Its generic length is 1 and special length is 2. Thus the inequality \(\ell(\mathcal F_s)\ge\ell(\mathcal F_\eta)\) holds, while multiplication by \(t\) has kernel \(k\). The module is not flat; explicitly \(\operatorname{Tor}_1^R(k,R\oplus k)=k\). This refutes only the literal sentence “inequality implies flatness.” Replacing “inequality” by “equality” is a reading proposal requiring the image, not a correction made here.

For a finite module over a DVR, let \(N\) be its \(t\)-power torsion and \(G=F/N\). The quotient is torsion-free, hence flat over the DVR. Tensoring \(0\to N\to F\to G\to0\) with \(R/t\) gives
\(0\to N/tN\to F/tF\to G/tG\to0\), because \(\operatorname{Tor}_1^R(R/t,G)=0\). This is a valid step in the draft. It does not automatically transfer absence of embedded associated points from \(F/tF\) to \(G/tG\).

EGA IV3 12.2.3(vi) explicitly asks whether the flatness hypothesis in the multiplicity theorem can be replaced by full support and universal openness under the stated fibre condition. It connects this to a noetherian-local question about a finite full-support module \(M\), a one-dimensional minimal component, and \(t\) avoiding **minimal** primes. This is different from the version in which \(t\) avoids **all associated** primes. Under the latter, \(t\) is \(M\)-regular. For a minimal prime \(\mathfrak p\in\operatorname{Ass}M\) with \(\dim A/\mathfrak p=1\), the standard associated-prime depth inequality gives \(\operatorname{depth}M\le1\); regularity gives \(\operatorname{depth}M\ge1\). Thus \(\operatorname{depth}(M/tM)=0\) and \(\mathfrak m\in\operatorname{Ass}(M/tM)\). This proves the stronger-hypothesis reading only. The exact later fate of the minimal-prime version was searched but not located; no claim of current openness follows from that bounded search.

## 20. Euler characteristic and the zero-sheaf test

**Claims:** CL-098–099. **Source:** 43/121; EGA III1, OIII 11.10.2 p. 49 and III 2.5.2–2.5.3 pp. 109–110.

For a bounded complex \(L^\bullet\) of finite-length modules, put \(Z^i=\ker d^i\), \(B^i=\operatorname{im}d^{i-1}\). The two exact sequences give
\[
\ell(L^i)=\ell(Z^i)+\ell(B^{i+1})
=\ell(H^i)+\ell(B^i)+\ell(B^{i+1}).
\]
Multiplying by \((-1)^i\) and summing cancels every boundary term, proving \(\chi(L^\bullet)=\chi(H^\bullet)\). Boundedness and finite lengths make the summation legitimate. A long exact cohomology sequence then proves additivity for coherent-sheaf Euler characteristics whenever the required lengths are finite.

The program uses a concrete complex \(\mathbf Q^2\to\mathbf Q^3\to\mathbf Q^2\), with differential ranks 1 and 1, composition zero, and cohomology dimensions \(1,1,1\). Both alternating sums are 1. This checks the finite example; the two exact sequences prove the general statement.

EGA's projective Hilbert–Euler theorem gives a polynomial for **all integer** twists; only the equality with \(\ell H^0\) requires \(n\gg0\). On projective space, \(\chi(\mathbf P^d,\mathcal O(n))=\prod_{i=1}^d(n+i)/d!\), including negative \(n\). The program prints these polynomials' values for \(0\le d\le3\), \(-4\le n\le4\). The zero sheaf has zero polynomial, so an unconditional strict-positive leading coefficient cannot replace the source's nonnegative assertion. For a nonzero coherent sheaf, the usual degree convention supplies its own positive leading term; that qualifier must be stated.

## 21. Soft rings, fine sheaves and the tensor embedding

**Claims:** CL-105–110. **Source:** reused typescripts 43/124, 126, 141, 139, in that logical order.

For the constant sheaf with at least two values on \([0,1]\), prescribe different values at 0 and 1. A global section is locally constant and hence constant on the connected interval, so cannot extend this closed-subset section. This directly checks the source's obstruction to softness.

For a soft sheaf of unital rings on a paracompact Hausdorff space, take a locally finite open refinement \((U_i)\) of the given cover and two shrinkings so that closed \(F_i\) cover \(X\), \(F_i\subset V_i\subset\overline V_i\subset U_i\). Softness extends the section equal to 1 near \(F_i\) and 0 near \(X\setminus V_i\), giving \(a_i\) with support in \(U_i\). Well-order the index set and put
\[
e_i=\left(\prod_{j<i}(1-a_j)\right)a_i.
\]
These products are locally finite: near any point only finitely many \(a_j\) are nonzero. The ordered telescoping identity gives \(\sum e_i=1-\prod(1-a_i)=1\), because some \(a_i\) equals 1 near every point. Supports remain in \(U_i\). This argument even works for noncommutative rings with the indicated order; the program checks the finite identity on noncommuting 2×2 integer matrices. The original typescript instead begins a maximal-family argument whose continuation is absent. The proof here is expressly a reconstruction.

Let \(\mathcal I\) be the sheaf of all integer-valued functions. At a point \(x\), evaluation \(\mathcal I_x\to\mathbf Z\) is well defined on germs and sends the constant germ 1 to 1. Hence
\[
\mathcal F_x\to\mathcal F_x\otimes\mathcal I_x,qquad v\mapsto v\otimes1
\]
has a left inverse \(1\otimes\operatorname{ev}_x\), proving the sheaf injection without requiring a global evaluation map. Cartan (1951, Exposé XV §5 Proposition 1 and §6; Exposé XVI p. 4) proves fineness of this ring and the resulting tensor embedding (`Cartan1951XV`, `Cartan1951XVI`).

The typed algebraic lemma also holds. If \(H\) is torsion-free and \(a\ne0\) is indivisible, every finitely generated subgroup containing \(a\) is free and \(a\) is primitive in it; therefore \(a\) extends to a basis. The tensor map is injective at every such finite stage. If an element becomes zero in the filtered colimit tensor, it becomes zero at a later finite stage containing \(a\), so was zero already. Indivisibility is essential: \(H=\mathbf Z\), \(a=2\), \(G=\mathbf Z/2\) would fail.

If \(\mathcal G\) is fine, its support-controlled endomorphisms \(\theta_i\) induce \(1\otimes\theta_i\) on \(\mathcal F\otimes\mathcal G\); their locally finite identity sum and support conditions persist. For extension by zero from an open or closed subspace \(Y\), first shrink a locally finite cover of \(X\) so its closures lie in the original cover, restrict it to \(Y\), and choose fine endomorphisms there. Extend these by the functor \(j_!\) or \(i_*\). Their supports in \(X\) lie in the closures of the shrunken members and hence in the original members; the family is locally finite on \(X\), and the identity sum holds on every stalk, including zero stalks outside \(Y\). This supplies the boundary support control that a bare assertion “extend the endomorphism” would omit.

## 22. The earlier run's arithmetic-unit examples

**Items:** SA19-3, 5 and the associated external-project leads. **Attribution:** these arithmetic examples are not claims on the Jacobian pages.

Unique prime factorization gives
\(\mathbf Q^\times\cong\{\pm1\}\oplus\bigoplus_q\mathbf Z\),
with the \(q\)-coordinate the valuation \(v_q\). It is not finitely generated, since a finite list of rationals involves only finitely many primes. Its infinitely divisible subgroup is trivial: divisibility by every \(n\) forces every integer valuation to be divisible by every \(n\), hence zero, and being a square forces the remaining sign positive. Likewise \(\mathbf Z[1/6]^\times=\{\pm2^a3^b:a,b\in\mathbf Z\}\), whose infinitely divisible subgroup is trivial.

The finite valuation matrix printed by the program illustrates independence of five prime coordinates; the factorization argument proves the infinite assertions. None of this challenges the separate geometric divisibility theorem in §8. No external-project source file was supplied, so the specific earlier run's theorem or lemma cannot be verified merely by these elementary models.

## 23. Polynomial dimension, depth and coprofondness

**Claims:** CL-100–103. **Source:** cancelled 43/129.

For \(A\) noetherian local, \(B=A[t_1,\ldots,t_n]_{\mathfrak P}\) with \(\mathfrak P\cap A=\mathfrak m\), the map \(A\to B\) is flat local. The flat local dimension theorem (`Stacks00OG`, Lemma 10.112.7) gives
\[
\dim B=\dim A+\dim\bigl(\kappa(\mathfrak m)[t_1,\ldots,t_n]_{\overline{\mathfrak P}}\bigr).
\]
The fibre dimension is \(\nu=n-\operatorname{trdeg}_{\kappa(\mathfrak m)}\kappa(\mathfrak P)\). When \(\mathfrak P\) is maximal over \(\mathfrak m\), Zariski's lemma makes that transcendence degree zero. Thus a draft moving between “maximal” and “prime” must not quietly keep a nonzero transcendence term in the former setting.

Polynomial rings over **every** field are regular. The exact primary proof read is `Stacks00OO`, Lemma 10.114.1 and Proposition 10.114.2: successive minimal polynomials of residue coordinates provide the needed regular local analysis. It does not assume that a residue-field extension is separable or that arbitrary inseparable base change preserves regularity. This avoids an unjustified repair of the compressed draft proof.

The closed fibre above is regular of dimension \(\nu\), hence has depth \(\nu\). The flat local depth formula (`Stacks0338`, Lemma 10.163.1, which cites EGA IV2 Corollary 6.3.1) gives \(\operatorname{depth}B=\operatorname{depth}A+\nu\). Subtraction yields
\[
\dim B-\operatorname{depth}B=\dim A-\operatorname{depth}A.
\]
This verifies the coprofondness arithmetic with the noetherian/flat hypotheses. The difference between variables \(t_0,\ldots,t_n\) and \(t_1,\ldots,t_n\) changes the count by one. The final blank list of properties \(P\) is not filled by this argument.

## 24. Faithful flatness, pure unit maps and the quotient \(B/A\)

**Claims:** CL-104, 111. **Source:** reused typescript 43/137.

Let \(A\to B\) be flat. If it is faithfully flat, the unit \(u_M:M\to B\otimes_A M\) is injective for every module \(M\). Indeed, after tensoring with \(B\), the resulting map has a left inverse induced by multiplication \(B\otimes_A B\to B\). Its kernel therefore becomes zero after faithfully flat tensoring, and was zero. Applying this to \(M=A/I\) gives \(IB\cap A=I\).

Conversely, if every proper ideal remains proper after extension, then for every maximal \(\mathfrak m\), \(B/\mathfrak mB\ne0\); the nonzero-fibre criterion makes the flat map faithfully flat (`Stacks00HP`, Lemma 10.39.15). Surjectivity on spectra is equivalent to these fibres being nonempty. If all unit maps are injective, then \(B\otimes M=0\) implies \(M=0\), another direct proof of faithfulness. Flatness remains part of these equivalences.

For the less commonly stated formulation, suppose first \(A\hookrightarrow B\) and put \(Q=B/A\). The Tor sequence, using flatness of \(B\), gives
\[
0\to\operatorname{Tor}_1^A(Q,M)\to M\xrightarrow{u_M}B\otimes_A M.
\]
Thus \(Q\) is flat exactly when every unit map is injective. Faithful flatness also implies \(A\to B\) injective by the case \(M=A\). Consequently, **for a flat ring map**, faithful flatness is equivalent to injectivity together with flatness of \(B/A\). This checks the quotient reading of the typed formula; juxtaposition \(Bh(A)\) cannot play the same role.

## Verification boundary

All 24 sections have been checked as written. Exact finite outputs are retained. Neither finite matrix tests nor a matching theorem title certify a full higher-Ext table, a whole category equivalence, a missing handwritten hypothesis, or a negative literature conclusion. The surviving uncertainties are explicitly indexed in `claims.json`, `problems.json` and `readings.tsv`; no transcription was changed.
