# F.3.29: single-line obstruction and genus-three recognition

F.3.29 is integrated into `output/RESEARCH_SA07/sections/F_audit.tex`. It proves that the actual genus-three universal degree-six quotient vanishes on every derivation tangent to one specified nonzero homology line. The original once-punctured genus-three curve therefore satisfies the arithmetic normalizer recognition assertion at every prime and after every finite arithmetic base change, with no condition on its Jacobian.

The proof uses the additional map R from the opened original Morita–Sakasai–Suzuki preprint, arXiv:2608.17673v1, Proposition 4.1, p.11. Its exact geometric vanishing is explicitly a primary-source dependency. The final program uses only the scalar coefficient of c in R([D,delta_abc]), together with all mixed ES7 equations. It does not impose an unprojected S equation. Actual mapping-class extension and contraction naturality transfer R-vanishing from stable genus to genus three.

The complete single-line space has dimension180. The integer mixed matrix has size7977×180, exact rational rank48, and132 independent integer kernel vectors. Every one of their105 complete contractions is an exact rational combination of two literal geometric degree-six Johnson brackets. The determinant used to clear these identities is−10752. Every coefficient identity is checked over the integers. The largest kernel coefficient is247830.

The final certificate also reconstructs, for each of the180 basis derivations, a polynomial B with D(b)=[B,b], then checks the degree-six Dynkin identity placing B in the free Lie algebra. Together with cyclic reconstruction when the constrained handle occurs once, this proves balanced single-line-to-paired tangency in every genus. This separate lemma does not prove the all-genus q6 conclusion.

Final production files are `code/check_genus_three_single_line.py` and `.output.txt`. Agent final run:50.942884514seconds. Independent elliptic final run:42.928949937seconds external,41.742954870seconds internal. The root checked the proof and core certificate independently, then the added conjugator and stabilization checks. The production registry ran only new program41:exit0,45.512690seconds; all40 previous records were preserved.

The after10b files contain12 canonical check events,3 exact source-check rows, and the bibliography key `AuditMoritaSakasaiSuzuki2026v1`. The source audit records the two narrow arithmetic slips in the preprint's proofs on pp.22 and25 and the verified final identities. They are not treated as theorem refutations, and neither slipped scalar expansion is imported by F.3.29.

The307-assertion inventory retains all statuses:195 PROVED,44 REFUTED,28 OPEN,30 READING,9 DOCUMENTARY-GAP,1 NAMED-CONJECTURE-IMPLICATION. Only `I.B05.01`, `I.B05.02`, and `II.MB15.02` receive the new dependency and a more precise retained obligation. The arbitrary detecting curve in the full LM6 A.22 assertion may have higher genus; an all-genus mixed-normalizer/contraction proof is still required.

## Work-only continuation

The proposed genus-uniform reduction uses the invariant projector for Sp(W)×Gm, where V is the direct sum of the constrained paired handle and W. This projector preserves the actual universal image, the tangent subspace, and q6. For positive constrained multiplicity, cyclic reconstruction reduces input parameters to Dynkin images of215 decorated degree-six tensors; the pure-W part has five invariant basis vectors once the complement genus is at least three. The exact mixed equations must still be formed and solved with their genus-dependent contractions. No universal vanishing has been inferred from the support bound or from a projection to a smaller surface.

## F.3.30 reduction integrated at10:46UTC

Root and generation independently approved the complete exact reduction LI.1–LI.6. It is now integrated as F.3.30 at precisely that scope: actual Levi projector,215 constrained Dynkin input span plus five pure-complement inputs, coupled scalar-polynomial mixed equations, and the five-detector map into the actual kernel of q6. The full mixed matrix remains uncomputed. The after10b ledger now contains16 events, the same3 source-check rows, and canonical result IDs F.3.29 and F.3.30. All307 assertion statuses are unchanged.

A work-only input program has separately constructed the formal positive-block equations. Their constrained dimensions are3,3,1,0 and the pure block has dimension5, giving12 formal input vectors. The specialization of its chosen pure block at complement genus3 still requires an exact detector injectivity check before that particular basis is used uniformly. This finite input calculation has not been promoted to a mixed-matrix or arithmetic conclusion.
