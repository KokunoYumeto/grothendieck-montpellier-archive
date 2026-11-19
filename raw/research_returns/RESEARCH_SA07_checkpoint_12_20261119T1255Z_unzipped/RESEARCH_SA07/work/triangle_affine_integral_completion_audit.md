# Independent audit of the actual affine-integral automorphism completion

19 November 2026. Independently read the entire `work/agent_affine_integral_automorphism_completion.md`, with particular attention to AF7 and the global conjugator. **PASS at its stated scope.** No edit was made to that file.

## AF1 and the actual embedded completion

For finite-index K_N in F, the discrete extension Gamma_N is residually finite by the finite quotients Gamma_N/mA_N. The normality of mA_N follows from the integral Q_N action, and its index is finite. Thus an element of F outside [K_N,K_N] survives a finite quotient killing that commutator, proving the claimed intersection with its profinite closure. The finite-quotient universal property gives the specified completion P_N, not merely an abstract isomorphic virtually abelian group.

The subgroup A_N has the full profinite topology induced from Gamma_N because every mA_N is normal and of finite index. Consequently its completion is exactly the kernel N/D_N, and Gamma_N intersects that kernel in A_N. Density of K_N in N and continuity of the commutator give D_N equal to the closed commutator of N.

For M contained in N, both transition maps really are quotient maps of the same F or G. They send Gamma_M onto Gamma_N. Compatible coordinates in P_N give compatible compact cosets in the actual G. Their intersection is one point because D_N is contained in N and the open N separate points. Restricting to coordinates in Gamma_N yields the displayed H. The specified characteristic chain is finite at each level and cofinal, so it is legitimate throughout.

## AF2: original lattices and inner automorphisms

The choice of normal N inside the core of U makes D_N lie in the closed commutator of U. Thus the chosen representative f has the same actual abelian class as z and belongs to F intersect U. This proves the nontrivial inclusion in AF.6. The reverse inclusion uses F contained in H and is exact.

For an arbitrary g in G, the open coset gU contains f in the dense F. Writing g=f u with u in U makes its conjugation on U_ab equal to the actual discrete basepoint-change map ad(f); ad(u) is trivial there. This proves integral-lattice transport between the precise corresponding subgroups, even though the chosen f may depend on U. No common discrete representative of g is asserted.

## AF3--AF4: local conjugators and their actual normalizer

The integral subgroup A_N is normal in P_N because it is stable under Q_N and commutes with the abelian kernel. Therefore P_N/A_N is a valid abstract quotient. The group V_N=Ahat_N/A_N is uniquely divisible: surjectivity of multiplication by m uses an integral representative modulo m, and injectivity uses A_N intersect mAhat_N=mA_N. Hence it is a Q-vector space.

The two discrete subgroups induce actual complements to V_N in the quotient. For their difference cocycle c, the stated averaging vector v has c(q)=v-qv. Conjugation by a lift of -v therefore carries the second complement to the first with the displayed sign. Since both original subgroups contain A_N, equality of quotient images is equality of the original subgroups after conjugation. The solution set is a left coset of the actual normalizer; no compactness of this nonclosed set is used.

The formula B_N=Gamma_N Z_N passes. Reducing a prospective normalizer by a Gamma_N element leaves a in Ahat_N. It normalizes precisely when every (q-1)a is integral. Stack these conditions in one integer matrix. Smith normal form turns a profinite solution of the integral linear system into an integral solution with the same image: divisibility by an integer in every Z_p is ordinary integer divisibility. Their difference is Q_N-invariant. These invariants are central in P_N, so the reverse containment also holds.

## AF5--AF6: compatibility of the local conjugators

The covering graph has no two-cells. A Q_N-invariant edge chain has constant coefficient on every edge with a given free-generator label. Each such sum has boundary zero. This identifies the full invariant cycle lattice and its completion with the r displayed sums e_j^N. The same argument in completed permutation coordinates avoids any unjustified exchange of invariants and completion.

The actual covering map sends e_j^M to [N:M]e_j^N. This map on central invariant modules need not be onto, but the proof does not assume it is. For z in Z_N choose an integral invariant z0 representing its coordinates modulo [N:M]. Lift z0 through the surjection Gamma_M->Gamma_N, and lift z-z0 through Z_M. Together with the lift of the Gamma_N factor, this produces an actual element of B_M mapping to the prescribed element of B_N. This is the crucial exact surjectivity step; the lift of z0 need not be central in the source, since it already belongs to Gamma_M and the remaining source factor is central.

For solutions s_N and a chosen t_M, the element s_N t_N^{-1} belongs to B_N with the correct left-coset orientation. A lift b_M gives b_M t_M mapping exactly to s_N. Therefore the transition maps of solution sets are surjective. A compatible sequence along the characteristic chain exists, and the actual isomorphism G=lim P_N supplies one h in G. Compactness is invoked only for its closed D_N-cosets, not for the nonclosed conjugator solution sets. The resulting beta normalizes every Gamma_N and thus H. Conversely, H-preservation and AF.6 give every original affine-cover lattice; inner conjugation preserves them by AF2. The stated equality of subgroups inside Aut_cont(G) follows.

## AF7: finite-generator characterization

This step passes without needing an assumption about the inverse generator images. For each characteristic N, the actual images of the specified generators lying in H imply alpha_N(Gamma_N) contained in Gamma_N, since Gamma_N is the discrete group generated by those images. Alpha also preserves Ahat_N, because it preserves N and D_N. Intersecting therefore gives alpha_N(A_N) contained in A_N.

The restriction is an integer matrix. Its completion is precisely the continuous automorphism induced by alpha on Ahat_N: the two maps agree on the dense A_N. Its determinant is consequently a unit in every Z_p. An integer with this property is +1 or -1, so the restriction maps A_N onto itself. Finally alpha induces an automorphism of Q_N. A subgroup of Gamma_N containing A_N and surjecting onto Q_N is the whole Gamma_N. Hence alpha_N(Gamma_N)=Gamma_N for every N, and the actual inverse-limit equality proves alpha(H)=H.

This characterization is explicitly inside actual continuous automorphisms of G. It supplies no assertion that an arbitrary tuple of elements of H generates G or defines an automorphism.

## AF8 and the remaining scope

The boundary lattice sequence is the actual integral homology sequence of the compactification pair and splits as abelian groups because the proper homology is free. Given the two integral diagonal blocks, changing integral splittings changes the off-diagonal block by P f-f' S, an integral homomorphism. Thus its residue class modulo the integral Hom group is an intrinsic obstruction to affine integrality. The proof correctly leaves its vanishing for the actual Galois transporter unproved.

Even after that vanishing, AF.16 only gives H-preservation up to the one proven inner conjugator. It supplies no discrete representative preserving F, and it does not invoke an endomorphism theorem whose source is F without constructing that source map. These remaining obligations are stated accurately.

No proof gap was found in AF1--AF7 or in the stated AF8 obstruction. The result is an exact characterization of actual profinite automorphisms preserving all affine integral-cover lattices, with the proper-boundary and discrete-representative steps retained at their precise scope.
