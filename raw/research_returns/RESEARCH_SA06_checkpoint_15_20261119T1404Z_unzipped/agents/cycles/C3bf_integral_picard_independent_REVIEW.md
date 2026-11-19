# Independent audit of C.3bf

Reviewer: `/root/cycles`, GPT-6 Astra Pro, same research run; this is an independent agent/proof check, not an independent-model check.

Full typed proof read at13:47–13:48UTC on2026-11-19: `agents/real_weil/C3_integral_picard_kernel_draft.tex`,10731bytes at the time of reading. Outcome: **PASS** for the stated characteristic-five integral kernel. No rational failure follows.

## Complete mathematical check

1. I reread the entire certified C.3m before reading this draft. Its algebraic contraction, normalization, unique vertex, regular neighbourhood, ideal identity m_R O_Z=I_V, and split strict transform are unchanged after reduction to characteristic5: the only relevant denominator in the Fermat normal/Jacobian calculation is4. The divisor H0 is the projective bundle of the kernel of O_C^(m+1)→K_C, so its regularity is actual, not generic.

2. The coherent cohomology gives H¹(V,L)=k^(m+1), H²(V,L)=0, and H¹/H²(V,L^n)=0 for n≥2. The square-zero Picard kernel is the full additive vector group because constants lift. Higher Picard groups stabilize, and the stated unit surjectivity removes the inverse-limit ambiguity. The construction of a local-Picard morphism uses formal existence and the already proved functor-level Elkik comparison from C.3p/z. It does not replace this by a bijection of points. On smooth parameter spaces Cartier closure and the nonzero relative degree of L identify the normalized identity component and exclude exceptional-line-bundle ambiguity.

3. The target is genuinely split. From the exact sequence O_V→L→L_H one obtains the quotient H¹(V,L)/U. Serre duality identifies U with span{x0,x1,x2}, of dimension3. Higher H¹(H0,L_H^n) vanish for n≥2. Higher H² vanish as well, either by the same exact sequence and Kunneth or by the projective-bundle-over-a-curve calculation. I requested that this last easy vanishing be written explicitly where formal existence is invoked; it is a clarification, not a missing mathematical hypothesis.

4. The Picard extension class is the mixed Poincare Atiyah obstruction. I checked its orientation: the tensor in H¹(V,L)⊗H¹(J,O_J) is equivalently the displayed map H⁰(C,K_C)→H¹(V,L). The three degree-five Fermat Jacobian monomials form a basis in characteristic5. Thus its image is exactly U and its three components in Ext¹(J,Ga) are independent.

5. I independently computed the Hasse–Witt coefficient rule. For the three positive triples of sum4, off-diagonal exponents are not all divisible by4; diagonal exponent triples are permutations of(8,4,4). Their coefficient in F^4 is12=2 mod5. The Jacobian is ordinary, and ker(Verschiebung) is the etale group(Z/5)^3. Pullback of H¹(O) by Verschiebung is zero because Frobenius pullback is bijective and their composite is[5]^*=0.

6. The Hom–Ext sequence gives Hom(kerV,Ga)≅Ext¹(J,Ga). The rank-three extension therefore embeds kerV into U, and the splitting of the pulled-back extension embeds J^(5) itself as a proper abelian subgroup B. Its map to the split target is(V,0), so its exact kernel is the indicated etale subgroup. No assumption that a finite-valued homomorphism must vanish is used.

7. The certified actual-family realization C.3w/z applies to this explicitly algebraizable normal strict-local example. Amplitude/relative degree excludes every nonzero exceptional class from G. Thus the finite subgroup is nonzero in actual Pic(X), ordinarily algebraically trivial, and trivial after restriction to Y. This is an integral degree-one result only.

## Direct actual-family variant proposed by the parent

At13:48UTC I also checked the proposed direct construction, which can replace reliance on the whole local-Picard identification for ordinary equivalence. Choose a smooth proper curve C′ in B through0 and a chosen kernel point. The Pic(V2)-gerbe can be split on C′: its global-unit band is an extension of Gm by an additive vector group; Br(C′)=0 and H²(C′,O)=0 handle both parts. For n≥2, Kunneth gives H²(V×C′,L^n)=0, so a chosen first-order family lifts through all stages. H¹ of the product need not vanish, but existence is enough: each endpoint has a unique higher Picard class. Proper GAGA produces a completed family. Popescu descent to a smooth R-algebra followed by henselian lifting with prescribed reduction modulo m² gives an actual family on Z×C′ with the exact V2 data. Since mO_Z=I_V, matching modulo m² is precisely the required first-neighbourhood matching. Endpoint Picard stabilization and completion injectivity then preserve source nonzero and target zero. I sent these checks and the unit-band clarification to both parent and author. A final changed proof should retain those details.

## Source and computation scope

This review freshly read the entire C.3m antecedent and the relevant Step5 of C.3z, and reused their previously audited Illusie/formal-GAGA/Elkik/actual-family inputs. It does not claim a new full rereading of all those primary works. The Hasse–Witt and Jacobian-ring computations above were independently checked symbolically by hand; the author's forthcoming retained program is a separate certificate. No new runtime is fabricated for this manual proof check.

### Final replacement read at13:49:28UTC

I read the entire newly written replacement Step5, not only the proposed outline. It includes the full Gm×Ga gerbe band, both vanishing obstructions, compatible but not uniquely chosen proper-curve families, uniquely determined endpoint classes, precise modulo-m² Popescu descent, and separate actual source/target completion detection. The tensor-difference argument makes the finite-group assignment well defined and injective. **Final typed replacement PASS; no remaining correction.**

### Source-minimal replacement read at13:53:54UTC

The author has now replaced the gerbe paragraph by a direct Poincare-bundle obstruction calculation. I read the complete revised Step5. **PASS.** The normalized Poincare bundle pulled back from C×J has the relevant mixed Atiyah component in H⁰(C,Ω¹_C)⊗H¹(J,O_J); normalization and degree zero remove the pure components relevant here. Its obstruction on V₂×P is the contraction with κ in H¹(V,L)⊗H¹(P,O_P). Pullback through Verschiebung kills the H¹(J,O_J) factor, so the previously certified transition-unit/Illusie obstruction formula gives an actual line bundle Q₂. Its morphism P→G and the prescribed b|P have the same projection to J. Their difference is therefore a morphism from a proper connected curve to the affine vector group U₀, hence constant. Tensoring with the inverse fibre at0 removes precisely that constant. This produces the exact prescribed first-order family with no separate gerbe neutralization theorem and no new global local-Picard representability claim. The rest of the already checked higher lifting, GAGA, prescribed mod-m² Popescu descent, endpoint uniqueness, and puncture detection is unchanged.

For source transparency, during the review I also opened the following exact inputs for the superseded gerbe route: Stacks Theorem59.68.5, Tag03RM (H² of Gm on a smooth curve over an algebraically closed field vanishes); Proposition35.9.3, Tag03DW (quasicoherent cohomology agrees in the Zariski, etale, and fppf topologies); and Lemma21.14.5, Tag0732 (Leray). The Colliot-Thélène–Skorobogatov author book dated31October2019, §2.2.3(3), printedp55, equation(2.8), explicitly gives smooth-commutative-group etale/fppf comparison, citing MilneIII.3.9. These inputs would support a Leray formulation of the original lifting step, but the current proof does not need them. I explicitly did not treat Stacks Lemma21.11.1 as an unconditional gerbe theorem: it has an additional cover hypothesis. I also did not use Stacks59.100.8 to identify the big Gm sheaf with an inverse-image small-etale sheaf.

### Retained finite-certificate audit

I read the complete `real_weil/code/check_C3bf_integral_picard.py`, its retained JSON, and stdout. All41 recorded checks pass. The retained run began2026-11-19T13:51:48.836254+00:00 and took0.07533210799738299seconds. The calculation verifies the smooth quartic gradient, the Hasse–Witt matrix2I₃ with determinant3 mod5, the three independent Jacobian monomials, the universal Segre polynomial identity, the split strict-transform substitution, and the stated finite linear/degree/group checks. The script correctly disclaims a computational proof of the Picard, formal-existence, Popescu, Elkik, or ordinary-equivalence arguments. I inspected the program and every retained output; I did not rerun it or substitute its finite samples for the all-dimension proof.
