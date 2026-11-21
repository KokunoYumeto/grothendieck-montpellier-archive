# Independent audit of recovered ANABELIAN_A1 A.2–A.5

Date: 2026-11-21. Checker: GPT-6 Astra Pro, `/root/effective_galois`; effort setting not exposed by the runtime. Type: targeted proof check by reading each entire proof and following its dependency maps; not a formal verification or a claim of different-model verification.

Source read: `/workspace/scratch/63b175cc138c/recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`, statements A.2–A.5, lines126–411 in the recovered file. The whole text of all four proofs was read.

## Outcome

**No mathematical gap found in A.2–A.5 under their stated hypotheses.** This check concerns the relative configuration sequence and boundary transport only; it does not by itself check the later point-recognition or Kummer evaluation step of A.1.

## A.2: free fibre, pro-r monodromy

The characteristic iterated Frattini quotients are cofinal for a finitely generated free pro-r group. Their automorphism kernels above the Frattini quotient are r-groups. Thus the closure of the H-action is pro-r once the mod-r action is an r-group, and the universal property extends it to H^(r). The composite L^(r) → H^(r) → Aut(L^(r)) is the inner action. The given Magnus proof of trivial centre is valid in rank at least2: finite r-group augmentation ideals are nilpotent, their evaluations detect every nonidentity element, and a series commuting with two independent free variables is scalar. Compactness then gives domination of an arbitrary prescribed finite r-quotient by a finite quotient of H^(r).

No residual-r assumption on the original discrete H is silently needed. The proof establishes injectivity of its completed fibre by the action, not by an unsupported exactness assertion for completion.

## A.3: relative cusp exactness

Given F_cr → Q, its cusp image R is a normal finite r-group and A=Q/R is a finite pro-Sigma proper quotient. Pulling the configuration family to C'×C' labels all punctures. Monodromy fixes the puncture subspace and the compactified H1 quotient, because the compactified family is the product. Hence its mod-r action is in the additive r-group Hom(H1(C'),W), including when r divides |A|. A.2 applies.

The finite core J* is taken over Γ/H, with H normal and quotient A×A. Its kernel quotient H/J* embeds in a finite product of r-groups. Thus Γ/J* is a finite Sigma-group with normal r-kernel and prescribed proper quotient. The containment J*∩Λ⊂ker(q) follows since J*⊂H, so this intersection already lies in L. Passing to the joint finite image justifies the completed containment.

The quotient kills ker(K_E→K_E^(r)) because the image of K_E lies in the finite normal r-kernel. Conversely the fibre map kills ker(K_F→K_F^(r)). Detecting every finite quotient proves fibre injectivity. Right exactness of pro-Sigma completion is sufficient for the final surjectivity/exactness step; it is not being used as an unjustified left exactness theorem.

## A.4: specialization and arithmetic quotient

The curve and its marked point admit a smooth proper lift over a complete mixed-characteristic DVR; the required obstruction groups H2 vanish in dimension1. The product pair with diagonal and the curve pair with its point are smooth proper pairs with smooth relative boundary. Transversality has multiplicity1. Prime-to-p specialization applies functorially to these pairs and preserves inertia.

The required SGA statements were independently opened in the primary recomposed SGA1 PDF https://arxiv.org/pdf/math/0206203:

- Exp.III Theorem7.3 and Corollary7.4, recomposed p.70/PDF p.86: existence of a smooth proper curve lift. Retrieval `turn721533385view0`, lines3850–3858.
- Exp.XIII Corollary2.9, recomposed pp.288–289/PDF pp.304–305: smooth proper finite presentation, relative normal-crossings boundary, coefficients in primes different from all residue characteristics; local constancy and base-change through H1. Retrieval `turn838826874view0`, lines16956–16981.
- Exp.XIII §2.10 constructs specialization and states path ambiguity as inner conjugacy; Lemma2.11, recomposed p.290/PDF p.306, gives specialization of inertia. Retrieval `turn838826874view1`, lines17047–17130.

The specialisation passage does not alter G_k. After geometric relative exactness has been established, the arithmetic fibre map is an isomorphism by comparison of extensions with identical geometric kernels and the identity on G_k. This part of the proof does not need a section of the configuration fibration.

## A.5: boundary and transport

The root-stack argument uses only the tame-cover extension across a normal-crossings boundary after a Kummer chart. Exp.XIII Proposition5.2 (absolute Abhyankar lemma), recomposed pp.315–316/PDF pp.331–332, was checked in the primary SGA1 text: it gives the local unique étale extension on the entire Kummer chart and invokes purity. Retrieval `turn838826874view2`, lines19016–19091. The local extensions glue by uniqueness; this supplies the stated finite-cover interpretation of the root-stack tower.

For the boundary root gerbe, covers with trivial stabilizer action descend to D, so its fundamental-group map to pi1(D) is right exact with inertia image as kernel. No finite stabilizer injectivity is assumed. The diagonal image in the proper product ensures that any further kernel in the image boundary group is still inertia. Relative pro-r quotienting leaves a quotient of Z_r(1).

The explicit Heisenberg representation proves that this inertia is the full Z_r(1), including r=2: the boundary product of commutators maps to 1+e13 over Z_r, of infinite r-adic order. The ordinary pro-r quotient of the punctured curve factors through the relative cuspidally pro-r quotient, so this detector remains available there. Fibre injection and transverse intersection identify it with diagonal inertia.

The cusp subgroup comparison is a comparison of extensions with identical Z_r(1) inertia and G_k quotient. Finally, lift the proper conjugating element γ to a geometric d in the boundary group, then correct its first proper-coordinate inner action by a geometric element e in the target fibre over γ^(-1). Their composite is over the identity of Π_C and G_k and sends the cusp to a geometric conjugate. No point-separation conclusion is inserted into the construction.

## Exact scope

These four proofs establish the stated relative single-prime cuspidal configuration transport while retaining the full chosen pro-Sigma proper base. They do not claim unrestricted exactness for every pro-Sigma completion of every discrete extension. The passage to cofinal r-quotients is local to the labelled-puncture family, which is why the monodromy lemma applies.
