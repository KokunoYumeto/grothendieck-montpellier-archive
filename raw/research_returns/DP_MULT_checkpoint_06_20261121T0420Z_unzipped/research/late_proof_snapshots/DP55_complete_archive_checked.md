# DP55 — Actual endpoint detection and nonzero periods at a principal auxiliary level

**Author/checker:** GPT-6 Astra Pro. **Reasoning effort:** not exposed. **Date:** 2026-11-21 UTC. This continues DP52 at the actual endpoint interface. It does not audit the accepted global theorems. Source reading, original-archive byte recovery and whole-proof checks are separate; no Lean execution is claimed.

## 1. Precise result

Retain the weak conjugation assumptions, dominant coefficient weights and endpoint level of DP52(c). Let \(S\) be the source's point datum \(\mathrm{ptGSD}\), \(S'\) its row datum \(\mathrm{rowGSD}\), and \(\mathcal E\) its endpoint evaluation object \(\mathrm{ptEv}\). Write
\[
 \mathcal F=\operatorname{span}_{\mathbf C}
       \{\,\mathcal E.\operatorname{emb}(\phi):
                  \phi\in S.\operatorname{EqFun}\,\}.       \tag{ED1}
\]
This is exactly the source's \(\mathcal E.\mathrm{Fi}\), not the entire ambient function space.

**DP55(a).** The row representing map
\[
 J:\mathbf C^{\dim_K S'.\operatorname{EqFun}}
                 \longrightarrow\mathcal F                \tag{ED2}
\]
is conjugate-linear and surjective, without the original Fields.Ok.quad hypothesis. The weakened endpoint period of DP52 satisfies
\[
 \operatorname{per}(F,z)=\langle Jz,F\rangle_{\mathrm{cl}}.    \tag{ED3}
\]
The classwise hermitian form is positive definite on \(\mathcal F\). Consequently every nonzero \(F\in\mathcal F\) is detected by some row coordinates:
\[
 Jz=F,\qquad
 \operatorname{per}(F,z)=\langle F,F\rangle_{\mathrm{cl}}>0.   \tag{ED4}
\]
This holds at the originally specified endpoint level whenever such an \(F\) is given; freeness of the finite-class action is not required.

**DP55(b).** Enlarge a specified finite endpoint-level support by a place \(P\) above an odd rational prime \(\ell\) unramified in the CM field \(E\), and put the level subgroup at \(P\) equal to \(\{1\}\), with its trivial character. Retain the other endpoint-level data. Then the action on the source's decorated lattices is free. For every dominant endpoint coefficient weight, both the point and row spaces are nonzero and the actual weakened endpoint period has an explicit pair with value \(1\).

This works for the actual mixed type \(\{1,2,3\}\) of \(\mathbf Q(\zeta_7)\), at every admissible rebuilt even lift count. It changes an auxiliary endpoint level; no estimate for the cost of that change is asserted.

**DP55(c).** Membership \(F\in\mathcal F\) is equivalent to coefficient-valuedness and finite-stabilizer invariance at each class representative. The source proves the corresponding adelic realization under the named additional inputs DecoPtSurj and IsLevOf; that theorem does not assume Fields.Ok. Thus period detection reduces to supplying a nonzero endpoint vector in this exact subspace for the intended theta family and satisfying its adelic/kernel ties. Neither an arbitrary algebraic theta germ nor a local derivative bound supplies that identification by itself.

## 2. Exact source declarations

All paths in this section begin with Formalism/LocalToGlobal/Columns/.

- CoefModB.lean: the bilinear Fock pairing and pairBK, 18–68; the actual theorem pairingBInvariant_holds, 188–191; and the actual theorem pairingBNondegenerate_holds, 193–203. The proposition PairBNondeg at 88–90 is not being mistaken for its proof.
- TiedPer.lean: GSD.Dua, 79–87; the complete partner proof, 104–117; jOf, 121–122; ip_jOf, 127–131; jOf_mem_Fi, 133–148; jOf_partner, 150–162; additivity and conjugate scalar behavior, 164–170; jOf_onto, 172–189.
- The same file: per_pair_smul, 199–202; per_pair_repr, 204–214; per_pair_ext, 216–219; the actual perDua constructor, 232–239; per_jMCL_eq, 243–244; per_jMC_mem_Fi, 246–248; and per_jMC_onto, 250–252.
- RecordInst.lean: ptEv_gram_unit, 47–58. Its proof identifies the endpoint Gram matrix with the **positive definite** matrix supplied by roundPk_gram_pos, not merely an arbitrary nonsingular matrix. The endpoint period identity is at 60–64.
- Record.lean: perCl, 315–329; perCl_emb, 331–337; pairSemi, 1551–1554; and periodC, 1568–1571.
- TiedValFi.lean: InvAt, 16–18; the proof from Fi, 20–34; averaging and the bump construction, 43–89; the converse proof, 91–130; and mem_Fi_iff, 132–133. Its IsLevOf at 151–154, adOf_mem at 185–201, invAt_of_adForms at 209–237 and fi_iff_FiC at 239–255 supply the adelic comparison discussed in §5.
- StdLatUnimodular.lean: Deco, 68–76; Deco.Ok, 81–94; Deco.act, 108–111; the standard lattice and base decoration, 128–137; and DecoSet.base, 650.
- ColForms.lean: level subgroup and character, 16–21; family group and inverse character, 24–37; action and coefficient action, 46–59.
- GSetLemmas.lean: Free, 206; resFree, 221–225; free classwise pairing, 227–232.
- CoefColLemmas.lean: the extremal coefficient vector, membership and nonvanishing, 320–332; coefficient-module nontriviality, 334–342.

## 3. Perfect coefficient pairing and row partners

The point and row data have the same decorated-lattice set and naturally identical acting groups. Their representations are respectively round and square, and their finite-level characters are mutually inverse. The actual source pairing
\[
 B=\operatorname{pairBK}_\lambda:
      V_{\mathrm{pt}}\times V_{\mathrm{row}}\longrightarrow K          \tag{ED5}
\]
is nondegenerate and satisfies
\[
 B(\rho_{\mathrm{pt}}(g)x,\rho_{\mathrm{row}}(g)y)=B(x,y).              \tag{ED6}
\]
For precision, the polynomial pairing is the normalized bilinear Fock form
\[
 B_\lambda(f,g)=
 \frac{\sum_{\alpha} f_\alpha g_\alpha\,\alpha!}
      {\prod_\tau\sum_\alpha
       (\operatorname{extremal}_{\lambda_\tau})_\alpha^2\,\alpha!},
                                                                    \tag{ED7}
\]
restricted to the finite-dimensional coefficient module. The theorem pairingBNondegenerate_holds proves nondegeneracy by applying the established coefficient-pairing theorem with the trivial involution. The theorem pairingBInvariant_holds proves (ED6) for round/square actions. The inverse finite characters cancel, giving exactly perDua. Neither constructor nor pairing theorem assumes a common quadratic subfield.

Let \(H\) be the point coefficient hermitian form. For a point-equivariant \(\phi\), perfectness gives a unique row value \(\psi(d)\) at each decorated lattice \(d\) with
\[
             B(x,\psi(d))=H(\phi(d),x)
                   \quad\text{for every }x.                         \tag{ED8}
\]
It is row-equivariant: for \(g,x\), point equivariance, invariance of \(H\), and (ED6) give
\[
\begin{aligned}
 B(x,\psi(gd))
 &=H(\rho_{\mathrm{pt}}(g)\phi(d),x)\\
 &=H(\phi(d),\rho_{\mathrm{pt}}(g)^{-1}x)\\
 &=B(\rho_{\mathrm{pt}}(g)^{-1}x,\psi(d))\\
 &=B(x,\rho_{\mathrm{row}}(g)\psi(d)).
\end{aligned}
\]
Uniqueness gives \(\psi(gd)=\rho_{\mathrm{row}}(g)\psi(d)\). This is the full mathematical content of GSD.Dua.partner. It uses DP52's point-goodness invariance, rather than the false quadratic-field wrapper.

Choose a \(K\)-basis \((b_a)\) of the row equivariant space and write \(\psi=\sum_a c_ab_a\). The representing map is
\[
 (Jz)(c)=
 \sum_a\overline{z_a}\,
 \mathcal E.\operatorname{sharp}
  \left(x\longmapsto\sigma_0(B(x,b_a(d_c)))\right),                     \tag{ED9}
\]
where \(d_c\) is a point-class representative. The positive coefficient Gram matrix is invertible, and sharp represents the displayed functional in the first, conjugate-linear slot of the coefficient inner product. Taking \(z_a=\sigma_0(c_a)\), equations (ED8)–(ED9) give
\[
                   Jz=\mathcal E.\operatorname{emb}(\phi).           \tag{ED10}
\]
Indeed, pair each side with every evaluated coefficient vector. The pairings agree by (ED8); both sides lie in the evaluated coefficient span, whose Gram matrix is nonsingular, so the vectors agree.

Formula (ED9) makes \(J\) additive and conjugate-linear. An arbitrary \(F\in\mathcal F\) has a finite expression \(\sum_i t_i\mathcal E.\operatorname{emb}(\phi_i)\). If \(Jz_i=\mathcal E.\operatorname{emb}(\phi_i)\), then
\[
       J\left(\sum_i\overline{t_i}z_i\right)
                  =\sum_i t_i\mathcal E.\operatorname{emb}(\phi_i).
\]
This proves surjectivity. Conversely \(Jz\in\mathcal F\): each value lies in the coefficient span, and row equivariance with (ED6) makes it invariant under the point stabilizer. The averaging argument in §5 then applies. Thus (ED2) has exactly its stated codomain.

The source per_jMC_onto uses \(h_X:X.\mathrm{Ok}\) only in ptOk. Replacing it by DP52's point-goodness proof therefore gives the result with the same perDua, row basis and Gram theorem. No quadratic-type assumption is restored.

## 4. Positivity and detection

On \(\mathcal F\) the classwise form is
\[
 \langle F_1,F_2\rangle_{\mathrm{cl}}
 =\sum_c\frac{1}{|\operatorname{Stab}(d_c)|}
       \langle F_1(c),F_2(c)\rangle_{\mathrm{coef}}.                   \tag{ED11}
\]
Every stabilizer is finite and contains the identity, so its weight is strictly positive. Each \(F(c)\) lies in the coefficient-evaluation span, and its evaluated basis has the positive Gram matrix used in ptEv_gram_unit. Every summand of \(\langle F,F\rangle_{\mathrm{cl}}\) is therefore nonnegative, with at least one positive when \(F\ne0\). This proves positive definiteness.

The exact finite-sum identity of DP52 gives (ED3). Surjectivity gives \(z\) with \(Jz=F\), and (ED11) gives (ED4), proving DP55(a). The chosen row coordinates have no uniform denominator, norm or height bound in this argument. Such estimates remain quantitative global inputs.

## 5. Exact classwise and adelic membership conditions

InvAt says that each \(F(c)\) lies in the coefficient-evaluation span and is fixed by the finite stabilizer of \(d_c\). Every \(F\in\mathcal F\) has this property by equivariance.

Conversely suppose InvAt holds. Express each \(F(c)\) in the evaluated \(K\)-coefficient basis, with complex scalar coefficients. Average each \(K\)-basis vector separately over \(\operatorname{Stab}(d_c)\), dividing by its finite order, and retain those same complex scalar coefficients. Their evaluated combination is still \(F(c)\), because that value is stabilizer invariant. Each averaged basis vector remains in the \(K\)-coefficient module, is fixed by the stabilizer, and therefore extends equivariantly from \(d_c\) to its orbit; extend it by zero on the other orbits. Summing these finitely many \(K\)-valued orbit functions with their complex coefficients expresses \(F\) in (ED1). This proves mem_Fi_iff even when stabilizers are nontrivial.

The later theorem fi_iff_FiC identifies this same space with values of adelic automorphic coefficient functions under:

1. an actual CM datum \(hc\) for \(E/F\);
2. the point-goodness certificate already constructed;
3. DecoPtSurj \(hc,n,ST,SG\), identifying decorated lattices with the required adelic representatives; and
4. IsLevOf, identifying the level subgroup with levU and its character with levTyp.

Its statement has no Fields.Ok argument. One direction constructs an adelic function from an equivariant decorated-lattice function; the converse uses the level transformation law to prove InvAt and then the preceding averaging argument. These are exact remaining identification inputs. We do not infer DecoPtSurj, the intended level identities or membership of a particular iterated theta vector from its local formal-group height. This proves DP55(c) as the asserted source-interface reduction.

## 6. A principal auxiliary level makes the action free

### Lemma ED12

If \(R\) is the ring of integers of a finite unramified extension of \(\mathbf Q_\ell\) and \(\ell\) is odd, the group \(1+\ell M_n(R)\) has no nonidentity element of finite order.

**Proof.** A nonidentity finite-order element would have a power \(A\) of prime order \(q\), still in this subgroup. Write \(A=I+\ell^a C\), with \(a\ge1\) and some entry of \(C\) a unit.
If \(q\ne\ell\), then
\[
 A^q\equiv I+q\ell^a C
               \pmod{\ell^{a+1}M_n(R)},
\]
whose first-order term is nonzero. If \(q=\ell\), then
\[
 A^\ell\equiv I+\ell^{a+1}C
               \pmod{\ell^{a+2}M_n(R)}.
\]
For \(2\le j<\ell\), the \(j\)-th binomial term has valuation at least \(1+aj\ge a+2\); the last has \(a\ell\ge a+2\), since \(\ell\ge3\). Again the first displayed term cannot vanish. Both cases contradict prime order. \(\square\)

Choose an odd rational prime \(\ell\) unramified in \(E\) and outside the old finite level support, and a place \(P\mid\ell\). Put \(H_P=\{1\}\) and retain all other level subgroups and characters. Such an auxiliary prime exists because only finitely many primes are excluded.

Suppose \((g,h)\) stabilizes a source decorated lattice \(d\) with lattice \(N\). Then \(gN=N\). The hermitian form is positive at every complex embedding by DP52, so the lattice isometry \(g\) has finite order. For a direct proof, its rational trace norm is a positive definite quadratic form. Images of a \(\mathbf Z\)-basis of \(N\) lie among finitely many lattice points of the corresponding bounded norms. There are only finitely many possible isometries, proving finiteness of the lattice-isometry group.

The exact decoration action is
\[
       \operatorname{be}_P(x)\longmapsto
                    h_P\,\operatorname{be}_P(g^{-1}x).
\]
Since \(h_P=1\), stabilization says
\(\operatorname{be}_P(g^{-1}x)=\operatorname{be}_P(x)\).
For \(x\in N\), the be_add and be_ker fields then give
\[
                         (g^{-1}-1)N\subseteq PN.                    \tag{ED13}
\]
After completion at \(P\), the lattice is free over an unramified local ring \(R_P\), with \(P\) generated by \(\ell\). Thus the matrix of \(g^{-1}\) lies in \(1+\ell M_n(R_P)\). Lemma ED12 gives \(g=1\) locally and hence globally.

Now stabilization implies \(h_w\operatorname{be}_w(x)=\operatorname{be}_w(x)\) at every level place \(w\). The be_surj field makes each map surjective, so every \(h_w=1\). The full stabilizer is trivial. This proves freeness for both row and point actions, whose underlying actions coincide. It uses the exact Deco.Ok fields and action formula, with no quadratic-induced-type hypothesis.

## 7. Explicit nonzero endpoint period

The decorated-lattice set is nonempty: the standard lattice and its residue-coordinate decorations give DecoSet.base. The endpoint rank is positive in an admissible source record. The coefficient module is nonzero: it contains the tensor of highest-weight extremal polynomials, represented as the product of nonzero polynomials in disjoint variable blocks. This also explains the source proof extVV_ne_zero.

For a free action, a value assigned at each orbit representative extends uniquely by \(\phi(gd_c)=\rho(g)\phi(d_c)\). Therefore the equivariant space is precisely the space of arbitrary coefficient values on the finite class set; this is resFree.

Choose one class \(c_0\), a nonzero coefficient vector \(x\), and by perfectness a vector \(y\) with \(B(x,y)=1\). Construct a point function with value \(x\) at \(d_{c_0}\) and zero at every other representative. Construct a row function with value \(y\) at the same representative and zero at the others. Write that row function in the chosen row basis and apply \(\sigma_0\) to its coordinates to obtain \(z\).

The exact identity perCl_emb now has only \(c_0\) contributing. Its stabilizer has order one, so
\[
        \operatorname{per}(\mathcal E.\operatorname{emb}\phi,z)
                    =\sigma_0(B(x,y))=1.                             \tag{ED14}
\]
Thus both coefficient spaces and the actual endpoint period are nonzero. This proves DP55(b), rather than merely constructing some unrelated nonzero bilinear form.

For the actual type \(\{1,2,3\}\) of \(E=K=\mathbf Q(\zeta_7)\), all weak assumptions hold by DP52. Any odd auxiliary prime other than \(7\), outside the specified support, is unramified and can be used. The construction is uniform in the rebuilt even lift length, with its changed endpoint rank and weights.

## 8. Exact remaining scope

The actual period detects every nonzero vector of the exact source space Fi, at any endpoint level. After an auxiliary principal-level refinement, that space itself is nonzero and a period value \(1\) exists for every dominant coefficient weight.

This does not establish that the prescribed iterated theta kernel has a nonzero image in Fi. It does not identify a finite global theta-jet realization on a Jacobian with the particular adelic coefficient functions, weights, levels, translated family or local operators used in the multiplicity argument. The same-family identification, selected theta identities and net quantitative comparison remain necessary.

Even when a nonzero endpoint vector is already given, the detecting row vector has no proved global cost bound here. The auxiliary level refinement also changes level costs. Neither a shorter actual global lift chain nor minimality of the old chain is asserted.
