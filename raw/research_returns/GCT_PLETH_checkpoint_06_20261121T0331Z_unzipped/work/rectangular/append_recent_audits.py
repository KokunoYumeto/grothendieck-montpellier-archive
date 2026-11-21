"""Append separately scoped completed checks; preserve the six audit categories."""
from pathlib import Path
from datetime import datetime,timezone
import csv

HERE=Path(__file__).resolve().parent
PROOF='targeted proof check'
COMP='computation or formal certificate'
SOURCE='used and rechecked in this run'
WHO='GPT-6 Astra Pro; effort not exposed; /root/rectangular_cases'
EVENTS=[
('R-032',PROOF,'complete finite-base annihilator and Pieri proof','passed',
 'Checked FK.1-FK.12 in full: exact successive derivative and common-polarization maps, all intermediate degrees and scalar factors, full-multiplicity injection, complete finite base kernels, minimal tail antichains, first-row containment, every endpoint and the positive interlacing-strip codomain bound. Root and archive independently completed whole-proof readings.',
 'finite_base_canonical_ranges.md'),
('R-032',COMP,'complete base-tail enumeration','passed28 base rows and251 tails',
 'Executed verify_finite_base_tail_ranges.py. Extracted the exact previously independently verified low-degree canonical kernels, included the two relevant degree-five CIM summands, checked all28 rows and their five minimal antichains, and compared the stated inequalities against every251 sorted bounded four-tail. This computation did not independently recompute the original source map ranks.',
 'FINITE_BASE_KERNELS.tsv; FINITE_BASE_TAIL_CHECK.tsv'),
('R-032-draft-padding',"refuted, with the refined statement's id",'Pieri-codomain row padding','repaired in R-032',
 'Archive identified that the codomain chain bound can be positive at length(lambda)>a even though the actual target is zero. Changed the chain padding to max(a,length(lambda)); checked the example a6,t2,b7, mu=(2,2,2,2,2), strips25 and7, output(30,2,2,2,2,2,2). No canonical-image assertion changes.',
 'finite_base_canonical_ranges.md; work/archive/FINITE_BASE_CANONICAL_REVIEW.md'),
('R-033',PROOF,'complete unit-family exact tensor proof','passed',
 'Checked UT.1-UT.19: exact exterior transfer and GL2 scalar, all small dimensions, normalized hook polytabloid map, invariant self-dualities, Gram coevaluation, projected perfect-matching j! factor, dense balanced flag map and inverse, every parameter endpoint, canonical image corollaries and the precise finite IP padding/determinant/stability chain. Root completed a separate whole-proof reading.',
 'two_column_tail_unit_family.md'),
('R-033',COMP,'literal exterior matching maps and actual plethysm','passed28 maps and45 coefficients',
 'Executed verify_two_column_tail_unit_family.py. For all a2..8 and j1..a-1, exact rational Gram coevaluation lies in the literal exterior-transfer kernel and the projected matching sum equals j! times that vector (28 cases). Literal cycle-index/MN independently gives one in all45 cases a2..6,n2..4,j1..a-1.',
 'TWO_COLUMN_TAIL_EXTERIOR_CHECK.tsv; TWO_COLUMN_TAIL_UNIT_MN_CHECK.tsv'),
('R-034',PROOF,'complete arbitrary-power derivative-band proof','passed',
 'Read and rederived LP.1-LP.22: exact Cauchy kernel of D and its spectator tensor products, arbitrary L>=min(r,t), every polynomial diagonal and derivative factorial, whole-isotypic lower-kernel membership, exact common-polarization inverse from reread R018, b-L>=t>=1, degree-two and complete degree-five bases, both iterations and closed capped sums. Checked the literal nonzero kernel example outside b-L>=t. Root whole-proof reading passed.',
 'linear_second_row_canonical_ranges.md; polarization_second_row_range.md'),
('R-035',PROOF,'complete determinant-square canonical scalar and full band','passed',
 'Checked SR.1-SR.17: actual normalized grid evaluation, all pure and repeated-coordinate tensor factors, two-permutation determinant expansion, exact covariance denominator and sign, dense polynomial extension, both nonzero and length-zero endpoints, scalar-one rank transposition, and the actual skew-Cauchy embedding excluding every one-box tail. Root separately read the full proof and passed it.',
 'second_row_two_canonical_rank_law.md'),
('R-035',COMP,'literal canonical polynomial pairings','passed40 exact scalar cases',
 'Executed verify_second_row_two_rank_law.py. Expanded the determinants and product linear form directly, paired each monomial by its exact multinomial denominator, and compared with the scalar times the literal target polynomial. All40 cases a2..5,n2..5,j1..a-1 pass, using nonunit first coordinates and including every sampled j>=n zero endpoint.',
 'SECOND_ROW_TWO_CANONICAL_SCALAR_CHECK.tsv'),
('R-035',COMP,'independent complete small second-row band','passed165 target and60 source coefficients',
 'The same script uses literal cycle-index/MN for every second-row<=2 target shape at a2..6,n2..4 (165 values), and every pure-tail source shape including the top row (60 values). All target vanishing/unit claims and source length cutoffs agree. Actual ranks are proved by the explicit map, not inferred from these multiplicities.',
 'SECOND_ROW_TWO_BAND_MN_CHECK.tsv'),
('T-050',PROOF,'independent whole-proof reading','passed',
 'Read all ER.1-ER.15. Checked exact G027 normal truncations, global generation and scalar-jet surjection, pair degree forcing, multiplication and determinant intertwiner, third-and-higher-term degree vanishing, actual H1 cokernel map, endpoint branches, residue-polynomial ranges and finite-difference/polytope bijection. The1,520,400 constants were not independently replayed in this event; the separate791 actual-MN comparison is already logged.',
 'work/theta/outer5/two_below_all_powers_report.md'),
('T-051',PROOF,'independent whole-proof reading','passed',
 'Read all ET.1-ET.13. Checked actual jet/cokernel sequence, both pair degrees including the rational b0 dual-Pieri summand, every third-term degree exclusion, three explicit triple modules and orientation/complement signs, quotient maps, all21 endpoint branches, residue degree bounds, support deduction and polytope transport. Archive independently reconstructed the3,049,200 constants; this event does not claim that reconstruction as my computation.',
 'work/theta/outer5/three_below_all_powers_report.md'),
('T-051',COMP,'independent all-endpoint actual plethysm comparison','passed1561 coefficients including84 triple-sector cases',
 'Executed verify_outer5_three_below_endpoints.py for every valid k2..7,n<=7 and all seven outer labels. Literal cycle-index/MN agrees with the independently reconstructed Euler and pair traces minus induction summed over actual cycle-stable three-subsets. Restricted S3 standard/sign and S2 signs were computed directly, without calling the proposed triple trace table or positive evaluator.',
 'OUTER5_THREE_BELOW_ENDPOINTS_CHECK.tsv'),
('G-030',PROOF,'independent whole-proof reading','passed',
 'Read ZS.1-ZS.11 and the full evaluator. Checked exact rank-two chart and arrangement maps, both Weyl shifts in skew extraction, all seven normal Schur products, orientation signs, bulk and five boundary polynomial ranges, every initial negative-index convention, all Newton/polytope bijections and parity shifts, support deduction, and exact first-two-order/complement coverage. No new literal matrix/witness run is claimed here; archive supplied that separate check.',
 'work/root/second_power_zero_twist_report.md; work/root/second_power_zero_twist_positive.py'),
('G-030',COMP,'independent complete unbounded-integer fixed certificate','passed512400 constants',
 'Executed verify_second_power_zero_twist_certificate.py. Rebuilt cycle-subset normal products and their two Weyl shifts, and used literal MN outer character rows. All trace and difference arithmetic used Python unbounded integers. All504000 bulk and8400 boundary constants, seven bulk and35 boundary SHA256 streams, extrema and zero sets agree. Every active positive order is positive and all inactive orders vanish. Conversion to signed64 occurred only after each final bound check for hash bytes.',
 'SECOND_POWER_ZERO_TWIST_CERTIFICATE_INDEPENDENT_CHECK.txt'),
('G-030',COMP,'independent actual plethysm and evaluator comparison','passed210 coefficients',
 'Executed verify_second_power_zero_twist.py for every valid n<=6 and every outer label. Literal cycle-index/MN equals independently rebuilt arrangement traces and the positive evaluator in all210 cases. Both determinant parities and every available finite boundary are included.',
 'SECOND_POWER_ZERO_TWIST_MN_CHECK.tsv'),
('T-049',PROOF,'targeted complete quotient and saturation argument','passed',
 'Read DP.1-DP.10 and the complete all-degree saturation argument used by T052. Checked the actual diagonal substitution, signed monomial-simplex contraction, every bounded-bicomplex total-degree position and Tor vanishing, exact module quotient, graded Nakayama regularity, block Cech/Kunneth depth, regular-linear quotient bound, local product/intersection comparison and k0 endpoint. No full review of the later Rees section is claimed by this event.',
 'work/theta/fat_arrangement_product_report.md'),
('T-052',PROOF,'independent whole-proof reading','passed',
 'Read all OC.1-OC.31. Checked parameter and first-row reduction, Weyl brackets and center/adjoint shifts, real symplectic centralizers and vacuum-cover untwists, charge homogenization/inverse and d_i-k lowering scalar, rational characteristic-polynomial Fischer projector, ordinary harmonic highest-vector embeddings, complete determinant/complement and finite-group dual maps, L_k irreducibility and actual Schur-functor theta branching. No rerun of the proposed finite nullspace computation is claimed.',
 'work/theta/oscillator_charge_report.md'),
('T-052',SOURCE,'primary oscillator and traceless-tensor passages read','passed',
 'Independently opened arXiv2006.07102v2 and read the complete relevant section5.2 equations5.21-5.30 on printedpp29-31 and AppendixA equationsA.25-A.28 on pp76-77. Checked source parameters M+=r,M-=1,N=m, all half shifts, contraction equations, ordinary compact highest weights and the complementary-column tensor map. This verifies the established source input used by OC.20 and OC.31.',
 'https://arxiv.org/pdf/2006.07102; work/theta/oscillator_charge_report.md'),
]


def main():
    path=HERE/'CHECK_EVENTS.tsv'
    with path.open() as f:
        reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
    keys={(r['statement_id'],r['detail_type']) for r in rows}
    now=datetime.now(timezone.utc).isoformat(timespec='seconds')
    added=0
    for statement,kind,detail,outcome,how,source in EVENTS:
        if (statement,detail) in keys:continue
        rows.append(dict(statement_id=statement,date=now,who=WHO,type=kind,
                         detail_type=detail,outcome=outcome,how=how,source=source))
        added+=1
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('added',added,'events; total',len(rows))


if __name__=='__main__':main()
