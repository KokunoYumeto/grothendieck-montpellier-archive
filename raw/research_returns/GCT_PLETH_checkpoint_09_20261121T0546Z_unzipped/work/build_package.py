from pathlib import Path
import csv, json, re, subprocess, hashlib, zipfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'deliverables'
OUT.mkdir(exist_ok=True)
RUN=json.loads((ROOT/'work/run_start.json').read_text())

REPORTS=[
 ('Checked theta and positive formulas',[
 'work/theta/theta_report.md','work/root/root_report.md',
 'work/root/degree_three_report.md','work/root/invariant_polytope_report.md',
 'work/root/general_polytope_extensions.md','work/root/rank_three_presentation.md',
 'work/theta/few_columns_report.md','work/theta/width7/width7_report.md','work/theta/outer4/outer4_report.md','work/theta/end_node/end_node_report.md','work/theta/end_node/end_node_schur_report.md','work/theta/end_node/normalization_obstruction.md','work/theta/outer4/paired_rows_report.md','work/theta/outer4/proper_faces_report.md','work/theta/general_chart_report.md','work/theta/outer4/chamber_report.md','work/theta/outer4/four_fibers_report.md','work/theta/outer4/full_outer4_report.md','work/root/general_fiber_model.md',
 'work/theta/outer5/five_point_resolution_report.md','work/theta/outer5/five_point_family_report.md',
 'work/root/five_point_q_module_report.md','work/root/five_point_wedge2_report.md','work/root/five_point_symmetric_quotient_report.md',
 'work/theta/outer5/q_plus_report.md','work/theta/outer5/five_point_hook_report.md',
 'work/theta/outer5/q_plus_symmetric_report.md','work/theta/outer5/hook_all_powers_report.md',
 'work/theta/outer5/two_row_ray_report.md','work/theta/outer5/two_row_below_ray_report.md','work/theta/outer5/two_row_line_correction_report.md','work/theta/outer5/stable_defect_cohomology_report.md','work/theta/outer5/three_defect_positive_report.md',
 'work/root/five_point_three_parameter_report.md','work/root/five_point_two_row_report.md',
 'work/root/staircase_uniform_report.md','work/root/staircase_five_report.md','work/root/even_increment_transport.md','work/root/five_row_interior_nonvanishing.md','work/root/fat_linear_arrangement_model.md','work/theta/fat_arrangement_product_report.md','work/root/first_power_zero_twist_report.md','work/root/five_row_strict_nonvanishing.md','work/root/end_wall_support_report.md','work/theta/outer5/two_below_all_powers_report.md','work/theta/outer5/three_below_all_powers_report.md','work/root/second_power_zero_twist_report.md','work/root/third_power_fixed_twist_report.md','work/theta/outer5/variable_wall/variable_wall_report.md','work/root/all_order_zero_twist_report.md','work/theta/outer5/variable_wall/one_twist_report.md','work/theta/outer5/variable_wall/one_twist_strip_report.md','work/root/all_order_one_twist_report.md','work/theta/outer5/variable_wall/rank_three_trace_review.md','work/theta/outer5/variable_wall/generic_twist_upper_report.md','work/root/normalized_below_report.md','work/theta/outer5/variable_wall/generic_high_twist_report.md','work/root/complete_outer_five_report.md','work/root/all_five_row_support_report.md','work/theta/oscillator_charge_report.md','work/theta/charged_incidence_rees_report.md','work/theta/varying_hook/first_hook_report.md','work/root/stable_hook_report.md','work/theta/unstable_hook/first_unstable_hook_report.md','work/root/stable_second_row_report.md','work/root/stable_third_row_report.md','work/root/fixed_second_part_report.md','work/theta/unstable_hook/higher_hook_jets_report.md','work/theta/unstable_hook/fixed_order_hook_report.md','work/theta/unstable_hook/hook_endpoint_report.md','work/theta/unstable_hook/pair_boundary_hook_report.md','work/theta/unstable_hook/all_fixed_order_hook_report.md']),
 ('Checked canonical-map and rectangular results',[
 'work/rectangular/rectangular_report.md','work/rectangular/boundary_and_prime_blocks.md','work/rectangular/polarization_boundary_report.md','work/rectangular/polarization_r4_boundary_and_geometry.md','work/theta/endpoint_check.md',
 'work/root/prime_semigroup_report.md','work/root/chow_first_row_report.md','work/rectangular/rectangular_end_lower_bound.md','work/rectangular/polarization_r6_boundary_report.md','work/rectangular/three_boundary_kernels.md','work/rectangular/boundary_truncation_model.md','work/rectangular/polarization_second_row_range.md','work/rectangular/polarization_first_row_band.md','work/rectangular/canonical_boundary_ranges.md','work/rectangular/recursive_canonical_range.md','work/rectangular/polarization_next_row_families.md','work/rectangular/canonical_below_square_families.md','work/rectangular/canonical_next_row_below_square.md','work/rectangular/canonical_cofactor_endpoint_strip.md','work/rectangular/canonical_second_cofactor_endpoint.md','work/rectangular/canonical_second_cofactor_strip.md','work/rectangular/outer_five_canonical_rank_law.md','work/rectangular/finite_base_canonical_ranges.md','work/rectangular/two_column_tail_unit_family.md','work/rectangular/linear_second_row_canonical_ranges.md','work/rectangular/second_row_two_canonical_rank_law.md','work/rectangular/second_row_three_canonical_rank_law.md','work/rectangular/even_tail_canonical_preimages.md','work/rectangular/fourth_moment_canonical_block.md','work/rectangular/four_one_tail_canonical_rank_law.md','work/rectangular/four_three_one_tail_canonical_rank_law.md','work/rectangular/four_even_tail_canonical_block.md','work/rectangular/four_even_tail_small_inner_degrees.md','work/rectangular/four_three_even_tail_canonical_block.md','work/rectangular/single_four_tail_canonical_band.md','work/rectangular/double_four_tail_canonical_block.md','work/rectangular/tail_moment_canonical_range.md','work/rectangular/repeated_four_mixed_tail_profile.md','work/rectangular/one_row_improved_canonical_range.md','work/rectangular/odd_part_occupancy_canonical_range.md','work/rectangular/hook_tail_canonical_isomorphism.md','work/root/current_ranges.md']),
 ('Checked archive findings and integral identities',[
 'work/archive/archive_report.md','work/archive/TENSOR_POWER_INTEGRAL.md','work/archive/STUDY_ADDITIONS.md','work/archive/PRIMARY_SCAN_FOLLOWUP.md','work/archive/ITERATE_COUNTEREXAMPLE.md','work/archive/LEFSCHETZ_FRAGMENT.md','work/archive/SCALAR_TRIANGULATIONS.md','work/archive/WITT_UNIQUENESS.md','work/archive/FIELD_CANCELLATION.md','work/archive/MIXED_CHAR_LATTICES.md','work/archive/HYPERBOLIC_CLASSES.md','work/archive/LOCAL_RING_COUNTEREXAMPLE.md','work/archive/FIVE_POINT_COX_MAP.md','work/archive/FIVE_POINT_POWERS.md','work/archive/ALL_HOOK_CYCLE_MODULES.md']),
 ('Algebraic-geometric restatements and proof dictionaries',['work/root/geometric_dictionary.md']),
 ('Source register and verification',['work/archive/SOURCE_NOTES.md','work/root/background_register.md','work/archive/OUTER4_FREE_MODULE_REVIEW.md','work/archive/GENERAL_FIBER_REVIEW.md','work/archive/OUTER5_PROOF_REVIEW.md','work/archive/FIVE_POINT_JET_REVIEW.md','work/archive/HOOK_BUNDLE_REVIEW.md','work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md','work/archive/TWO_ROW_POSITIVE_REVIEW.md','work/archive/STAIRCASE_PROOF_REVIEW.md','work/archive/HIGHER_IDEAL_POWERS_REVIEW.md','work/archive/EVEN_INCREMENT_AND_INTERIOR_REVIEW.md','work/archive/STABLE_DEFECT_REVIEW.md','work/archive/THREE_DEFECT_REVIEW.md','work/archive/FAT_ARRANGEMENT_REVIEW.md','work/archive/STRICT_CHAMBER_REVIEW.md','work/archive/OUTER_FIVE_CANONICAL_REVIEW.md','work/archive/TWO_BELOW_ALL_POWERS_REVIEW.md','work/archive/END_WALL_SUPPORT_REVIEW.md','work/archive/THREE_BELOW_ALL_POWERS_REVIEW.md','work/archive/FINITE_BASE_CANONICAL_REVIEW.md','work/archive/SECOND_POWER_ZERO_TWIST_REVIEW.md','work/archive/ALL_WALL_SUPPORT_REVIEW.md','work/archive/OSCILLATOR_PRIMARY_NOTES.md','work/archive/OSCILLATOR_CHARGE_REVIEW.md','work/archive/CHARGED_INCIDENCE_REVIEW.md','work/archive/LINEAR_CANONICAL_RANGES_REVIEW.md','work/archive/TWO_COLUMN_UNIT_FAMILY_REVIEW.md','work/archive/SECOND_ROW_TWO_RANK_REVIEW.md','work/archive/SECOND_ROW_THREE_RANK_REVIEW.md','work/archive/THIRD_POWER_FIXED_TWIST_REVIEW.md','work/archive/VARIABLE_WALL_REVIEW.md','work/archive/FOURTH_MOMENT_BLOCK_REVIEW.md','work/archive/ZERO_WALL_COMPLETE_REVIEW.md','work/archive/FOUR_ONE_TAIL_RANK_REVIEW.md','work/archive/ONE_TWIST_CHAMBER_REVIEW.md','work/archive/ONE_TWIST_STRIP_REVIEW.md','work/archive/ONE_WALL_COMPLETE_REVIEW.md','work/archive/FOUR_THREE_ONE_TAIL_RANK_REVIEW.md','work/theta/outer5/variable_wall/G033_REVIEW.md','work/archive/FOUR_EVEN_TAIL_BLOCK_REVIEW.md','work/archive/GENERIC_SINGLETON_REVIEW.md','work/archive/GENERIC_UPPER_CHAMBER_REVIEW.md','work/theta/outer5/variable_wall/G035_REVIEW.md','work/theta/outer5/variable_wall/G036_REVIEW.md','work/archive/NORMALIZED_BELOW_REVIEW.md','work/archive/GENERIC_HIGH_TWIST_REVIEW.md','work/archive/COMPLETE_OUTER_FIVE_REVIEW.md','work/archive/FOUR_EVEN_TAIL_SMALL_DEGREE_REVIEW.md','work/archive/FOUR_THREE_EVEN_TAIL_BLOCK_REVIEW.md','work/archive/SINGLE_FOUR_TAIL_BAND_REVIEW.md','work/archive/DOUBLE_FOUR_TAIL_BLOCK_REVIEW.md','work/theta/varying_hook/G037_REVIEW.md','work/archive/STABLE_HOOK_UNIFORM_REVIEW.md','work/archive/FIRST_HOOK_KERNEL_REVIEW.md','work/archive/TAIL_MOMENT_CANONICAL_RANGE_REVIEW.md','work/archive/FIRST_UNSTABLE_HOOK_REVIEW.md','work/archive/REPEATED_FOUR_MIXED_PROFILE_REVIEW.md','work/archive/STABLE_SECOND_ROW_REVIEW.md','work/archive/HIGHER_HOOK_JETS_REVIEW.md','work/archive/ONE_ROW_IMPROVED_RANGE_REVIEW.md','work/archive/STABLE_THIRD_ROW_REVIEW.md','work/archive/FIXED_ORDER_HOOK_REVIEW.md','work/archive/FIXED_SECOND_PART_REVIEW.md','work/archive/HOOK_ENDPOINT_REVIEW.md','work/archive/ODD_PART_OCCUPANCY_REVIEW.md','work/archive/PAIR_BOUNDARY_HOOK_REVIEW.md','work/archive/HOOK_TAIL_CANONICAL_REVIEW.md','work/rectangular/sixth_power_source_scope_audit.md']),
 ('Unresolved questions and exact remaining gates',['work/root/remaining_gates.md']),
]

def merge_events():
    fields=['statement_id','date','who_model_effort_run','type','detail_type','outcome','how','source']
    rows=[]
    for p in [ROOT/'work/root/CHECK_EVENTS.tsv',ROOT/'work/theta/CHECK_EVENTS.tsv',ROOT/'work/rectangular/CHECK_EVENTS.tsv',ROOT/'work/archive/CHECK_EVENTS.tsv']:
        if not p.exists(): continue
        for r in csv.DictReader(p.open(newline=''),delimiter='\t'):
            rr={k:r.get(k,'') for k in fields}
            rr['who_model_effort_run']=r.get('who_model_effort_run',r.get('who',''))
            rr['source']=r.get('source','') or str(p.relative_to(ROOT))
            rows.append(rr)
    with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    return rows

def questions():
    fields=['id','source_and_locator','question','state','finding_ids_or_current_gate']
    rows=[]
    for part,files in REPORTS[:3]:
        for name in files:
            p=ROOT/name
            if not p.exists(): continue
            for line in p.read_text().splitlines():
                m=re.match(r'#+\s+([AGRTM]-\d{3})[.:]\s*(.*)',line)
                if m:
                    sid,title=m.groups()
                    state='proved in stated scope'
                    if sid in ['A-001','A-002','A-003','A-005','G-001','T-009','R-003','R-010','A-015','A-016','A-023','T-057']:
                        state='specified assertion refuted; exact replacement proved'
                    if sid.startswith('M-'): state='source audit and exact morphisms checked; open ranges retained'
                    rows.append(dict(zip(fields,[sid,name+'; '+sid,title,state,sid])))
    # Some finite-certificate reports declare their ID in a statement paragraph.
    known={r['id'] for r in rows}
    for _,files in REPORTS[:3]:
        for name in files:
            p=ROOT/name
            if not p.exists(): continue
            for sid in re.findall(r'Statement \*\*([AGRTM]-\d{3})\*\*',p.read_text()):
                if sid not in known:
                    title=next((x.lstrip('# ').strip() for x in p.read_text().splitlines() if x.startswith('# ')),sid)
                    rows.append(dict(zip(fields,[sid,name+'; '+sid,title,'proved in stated scope',sid])))
                    known.add(sid)
    aq=ROOT/'work/archive/ARCHIVE_QUESTIONS.tsv'
    if aq.exists():
        for r in csv.DictReader(aq.open(newline=''),delimiter='\t'):
            if 'question_id' in r:
                rows.append(dict(zip(fields,[r['question_id'],r.get('source_file','')+'; cote '+r.get('cote','')+'/scan '+r.get('scan',''),r.get('assertion',''),r.get('status',''),r.get('proof_id','')+'; '+r.get('result_or_exact_gate','')+'; '+r.get('scan_verification','')])))
            else:
                rows.append({k:r.get(k,'') for k in fields})
    openq=[
      ('Q-ARCH-CONTEXT','Archive 4/007; 12/041; 16/038; 79/051; 119/217','Complete the unidentified or context-dependent assertions','precise mathematical and target-definition gates','Original contexts are recovered. Remaining inputs include crystalline Lefschetz/freeness, the stated motivic self-duality map, and reconstruction from one unlabeled triangulation; see assertion-level archive rows.'),
      ('Q-EFFICIENT','Mulmuley GCT VII Problem 1.1','Uniform positive #P formula of polynomial description size','open','G009–G011 give terminating positive formulas. Complete outer degrees3–5, stable hooks G037, stable two-row tails with every fixed second part G040 (small closed formulas G038–G039), and fixed-order hook charts a≥2k T064–T065 have explicit proved bounds. The remaining general varying-shape Hilbert bases, invariant lists and elimination data have no unrestricted polynomial input-size bound proved here.'),
      ('Q-STABLE-FIXED-SECOND-PART', 'G-040 FS1–18; A097 independent review', 'Give a positive polynomial construction for every fixed second part of a stable two-row tail', 'proved for every fixed b with the stated encoding', 'For every b≥2, all m≥3,a≥b,t≥0,n≥a+t and every outer label, the positive bounded-polytopes construction has at most3m+2b variables and construction/value/support complexity f(b)(m+binary input lengths+1)^g(b). The actual transfer has a finite cokernel in degrees b−1 through2b−2; all invariants e_i with i≥b kill it, leaving at most b−2 low variables. Actual minimal-cover cancellations, the high-variable multidegree inverse, fixed-variable Gröbner bounds and triangular monomial lifts prove the formula. The general finite algorithm is fully specified and checked; executable closed formulas and computation receipts currently cover b2/3. No polynomial complexity is claimed for unrestricted varying b.'),
      ('Q-STABLE-SECOND-PART2', 'G-038 SR2.1–17; T032 C4–8', 'Give a positive formula for every stable tail (a,2) with varying outer degree', 'proved in the stated explicit encoding', 'For m≥3,a≥2,t≥0,n≥a+t and every outer label, the actual quadratic transfer kernel yields at most binom(m,2)+4 bounded polytopes with at most3m−3 variables. Exact coefficient and support algorithms have polynomial bit complexity in m and the binary parameters. Actual free cover cancellation and the two explicit Koszul exceptions prove positivity; all source comparisons and executed receipts are retained.'),
      ('Q-STABLE-SECOND-PART3', 'G-039 SR3.1–23; T032 C4–8', 'Give a positive formula for every stable tail (a,3) with varying outer degree', 'proved in the stated explicit encoding', 'For m≥3,a≥3,t≥0,n≥a+t and every outer label, the cubic transfer kernel yields at most binom(m,2)+7 bounded polytopes with at most3m−1 variables. The actual curvature quotient and Ricci splitting identify the finite invariant-base cokernel, whose minimal covers give a nonnegative free remainder and explicit ordinary/modified Koszul cycles. Degree evaluation and support are polynomial in m and binary parameter lengths.'),
      ('Q-HOOK-JET-RIGHT-INVERSE', 'T-062 HJ1–10; T-065 HE4–7', 'Construct actual higher-order hook jet splittings', 'proved', 'The explicit quadratic frame jets and horizontal contraction construct an equivariant right inverse for all a≥2k+1. The verified Segre regularity bound and rational Gram right inverse close every valid endpoint a=2k, with m4 and k1 handled by their exact direct maps. The flag ideal kernel and determinant twist give the identical plethysm multiplicity.'),
      ('Q-ALL-FIXED-ORDER-HOOKS', 'T-067 AF1–21; G027 FA4/6; T049; G037', 'Evaluate every valid hook tail at every fixed positive ideal order', 'proved with explicit order and encoding bounds', 'For m≥4,k≥1,a≥1,t≥0,0≤r≤m−2 and (m−2)a≥mk+r, all outer labels have the positive formula AF20 with at most1+D_k(2(m²+3m−4)−1) disjoint bounded polytopes of at most m²+3m−4 variables. The exact complex has q≤k selected terms; complementary hook pairing gives residual Sym^A h_(m−q)⊗Λ^(r−s)h_(m−q), A≤k−q. The normal representation has rank and degree bounded by k, all subsequent LR additions have at most k cells, and every sign is specified. The signed correction is the actual jet-image multiplicity, between0 and D_k, giving complete point deletion. Values and support take f(k)poly(m+binary lengths); matrix construction has f(k)(m+k+1)^(2k+O(1)) times polynomial bit length. Together G037 and T067 cover all stable and unstable hook charts; unrestricted polynomial dependence on k remains open.'),
      ('Q-HOOK-PAIR-BOUNDARY', 'T-066 PB1–15; G027 FA4/6/8–9; T049 DP1–10', 'Evaluate every valid hook boundary a=2k−1', 'proved with the stated fixed-order and encoding bounds', 'For k≥2 and every physical m,r,t, the exact restriction complex has only ambient, singleton-jet and pair terms. The pair module is Ind_(S2×S_(m−2))^(Sm)(1⊗Λ^(r−1)h_(m−2)), zero at r0, with the proved orientation and determinant signs. Its multiplicity is the horizontal-two-strip indicator. The coefficient is stable hook minus jet plus pair; the net deleted-point correction is nonnegative and at most D_k. All explicit matrices and fixed-order bounds are retained. Together T064–T066 cover every valid a≥2k−1; the missing k1,a1 endpoint has no physical input.'),
      ('Q-FIXED-ORDER-HOOKS', 'T-063 HJ11–16; T-064 FK1–15; T-065 HE1–7', 'Evaluate all valid hook parameters with a≥2k by positive polytopes', 'proved with the stated fixed-order and encoding bounds', 'For every k≥1,m≥4,a≥2k,t≥0,0≤r≤m−2 with (m−2)a≥mk+r, the stated unstable hook coefficient equals the stable G037 value minus the explicit nonnegative jet correction. D_k=Σ_p S(k−1,p)2^p(p+1)! bounds the correction. At most1+D_k(2(m²+3m−4)−1) disjoint bounded polytopes suffice, with m²+3m−4 variables each. Construction is f(k)(m+k+1)^(2k+O(1)) times a polynomial in binary lengths; coefficient and support evaluation have the stronger f(k)poly(m+binary lengths) bound. No unrestricted polynomial bound in varying k is asserted. T067 completes the entire remaining physical hook range at every fixed k. Its explicit dependence on k and encoding scope are retained.'),
      ('Q-MAP-REPEATED4-MIXED', 'R-047 RF1–20', 'Determine finite multiplicities and actual ranks for tails (4^h,3,2^j,1)', 'proved in the stated ranges', 'For h≥1,j≥0 put K=2h+j+3 and r_s=min(h,max(0,s−h−j−3)). Target multiplicity is r_a for a≥2,n≥4. For a,n≥4 with max(a,n)≥K, actual image multiplicity is min(r_a,r_n); n≥K gives the full target for every a≥2. Complementary-column and faithful moment maps supply each finite comparison.'),
      ('Q-MAP-ALL-HOOK-TAILS', 'R-050 HM1–27; R046 TM14–17; Solomon §3; Langley–Remmel Thm3.1', 'Determine every actual canonical rank on a hook tail', 'proved', 'For all a,n≥1 and every valid λ=(an−t−r,t,1^r),t≥1,r≥0, the two actual normalized canonical maps are isomorphisms on the entire λ-isotypic component. The finite power-sum map from moments of degrees2..s is onto and faithful on all hook types by the exact hook specialization and invariant Koszul basis. The actual bounded-row input at row degree n maps injectively into moments2..n, so the exact canonical factorization applies even when n<t. The unit family λ=(an−D,T,1^(m−2)),T=binom(m,2)+1,D=binom(m+1,2)−1,a,n≥m has coefficient1 and the full nonzero scalar C_m(a,n) in HM24, including every square m.'),
      ('Q-MAP-ODD-OCCUPANCY', 'R-048 OI1–21; R-049 OO1–25', 'Sharpen full canonical surjectivity using the tail odd-part count', 'proved', 'For a,n≥2 and a valid nonempty tail ν of size D and width t≥2, let o be its number of odd parts, ε=t mod2, q=ceil((o−ε)/3), and M=floor((D+t−q)/2). The actual h_(n,a) reaches its entire target isotypic component at n≥M; both directions are isomorphisms at a,n≥M. The averaged extra-row morphism is literally id⊗q in the centered splitting, giving the exact kernel injection. Alternating highest weights, the finite-row character, faithful evaluation and normalized polarization prove the rank. The Euler-form hook family gives positive examples with unbounded improvement in the row threshold.'),
      ('Q-FIRST-UNSTABLE-HOOKS','T-061 UH1–10; G-037 HK1–19; G-015','Evaluate every valid first unstable hook tail in varying outer degree','proved in the stated explicit encoding','For m≥4,a≥2,0≤r≤m−2,t≥0 with (m−2)a≥m+r, inner n=a+t−1 and λ=((m−1)a+t−m−r,a+t,(t+1)^r,t^(m−2−r)), the coefficient is the G037 stable hook value minus one on at most three specified induced hook labels. Actual equivariant evaluation splittings prove the kernel comparison. At a2 the exact single-Specht endpoint is proved. At a≥3 a specified G037 lattice point is deleted by at most2(m²+3m−4) disjoint bounded polytopes of at most m²+3m−4 variables. Binary-degree evaluation and support are polynomial in m and the binary parameters, retaining the t0 compressed-encoding caveat.'),
      ('Q-STABLE-HOOKS','G-037 HK1–19; T-060 FH1–18; T-032 C4–8','Give a uniform positive formula and support for stable hook tails with varying outer degree and hook length','proved in the stated explicit encoding','Every λ=(mn−a−(m−1)t−r,a+t,(t+1)^r,t^(m−2−r)),m≥3,a≥1,0≤r≤m−2,t≥0,n≥a+t has one explicit bounded polytope with at most m²+3m−4 variables, a complete support test and polynomial-bit exact evaluation in m and the binary parameters. For t≥1 the ordinary binary-part list has m positive entries, giving a genuine polynomial-size #P verifier in that encoding. The exact Koszul differential, super-principal cell cancellation and invariant-form monomial basis supply the comparisons. The t0 compressed-encoding caveat is retained.'),
      ('Q-OUTER4','G-015 flag model at m4; T-037','Evaluate every outer-degree-four Schur coefficient by a fixed small positive formula','proved','T-037 gives at most108 fixed polytopes, at most5 variables, a fixed arithmetic evaluator and exact support for every output shape.'),
      ('Q-OUTER5','G-036 CF1–10; G-035 NB1–15; T-058 GU1–14; T-059 HT1–12; G-021','Evaluate every outer-degree-five Schur plethysm coefficient by a fixed positive formula','proved','G036 covers every n≥0, every outer label μ⊢5 and every output partition λ⊢5n. The exact stable first-row and perfect complementary-column maps give one normalized input with b+c≥2k. G021 covers c≥2k, T059 covers k≤c<2k, and G035 covers every c<k, including all lower cones, strips and small-order endpoints. The complete formula uses at most152 selected bounded polytopes in at most11 variables and a fixed arithmetic/binomial evaluator of polynomial bit complexity. G031 separately determines all support. Every map, determinant sign, rational phase certificate and provider route is explicit and checked.'),
      ('Q-EXACT-FLAG','G-027 FA1–17; T-049 DP1–12','Replace all unspecified flag-ideal cohomology ranks by explicit algebraic maps and known finite character terms','proved','G027 gives the exact normal-order map, signed restriction complex and full stabilizer model in every outer degree. T049 gives the actual diagonal quotient, all-degree saturated product equality and factored character; in outer degree five its character is48 fully specified signed bounded-table counts per cycle class.'),
      ('Q-NONVANISH5','G-024,G-028,G-031 NW1–8; complete344-node catalog','Classify nonvanishing for all outer-degree-five Schur labels','proved','G031 completes every proper nonempty gap support:172 seeds,344 deficient nodes,1896 point transitions and2084 bounded ray checks exhaust158 isolated points and196 stable ray bases. Its fixed normalization/table decision, together with G028 strict support and the determinant line, decides every coefficient in polynomial bit complexity. All maps, signs and interacting-ray endpoints are proved and independently checked.'),
      ('Q-CHARGED-REES','T-053 IR1–14','Identify the exact charged incidence algebra, its frame Rees algebra and positive torus-weight count','proved','The explicit algebra map preserves all k,l products, and the invariant-ring morphism gives the actual affine quotient. A terminating diagonal rewrite gives a flat family and2^r bounded polytopes for each row/charge weight. Every individual plethysm factor in that weighted sum has the explicit padded-rank label. The degree-two orbit proof excludes only a monomial initial ideal stable under this literal S_m action in these coordinates.'),
      ('Q-THETA-CHARGE','T-052 OC1–31','Identify the exact frame quotient with a charged oscillator and actual theta branching multiplicity','proved','The block homogenization maps the regular diagonal quotient to positive-charge coinvariants of U(m−2,1)×U(m). A finite rational Fischer projector gives harmonics; complementary-column and Gram pairings give the exact balanced module, all determinant/vacuum shifts, and the stated Schur functor of an irreducible one-column oscillator.'),
      ('Q-ADJACENT-WALLS','G-034 OW1–14; T-055 OT1–12; T-056 OS1–6','Evaluate both entire central-gap-one walls in every outer-five degree','proved','The c1 wall has a complete disjoint route through low orders, exact complementary defects0..3, the T055 chamber, T056 strip and two lower cones. A full rank-three triple identity computes the actual oriented quotient character. Stable-first-row multiplication and the perfect complementary-column pairing cover every original partition and both wall gaps, retaining outer-label signs.'),
      ('Q-CENTRAL-WALLS','G-033 ZW1–10;T-054 VW1–15;complementary-column pairing','Evaluate both entire central equal-row walls in every outer-five degree','proved','The c0 wall has a complete disjoint positive-formula route: low orders, exact complement defects0..3, T054 upper chamber and two triple-defect cones. The stable-first-row map covers λ2<n. The perfect exterior pairing transports λ3=λ4 to λ2=λ3. All maps, signs, fixed polytopes and support are explicit.'),
      ('Q-IDEAL-ORDER3','G-032 FT1–10;T-051,T-050,T-045,G-021','Evaluate every outer-five coefficient of ideal order at most three','proved','The three new low-twist slices and previously proved high twists exhaust k3. The finite rank-three restriction character yields17 selected positive polytopes in at most8 variables, with24 boundary branches and1552320 certified constants. The exact determinant/complement maps cover λ2≤n+3 orλ4≥n−3.'),
      ('Q-MAP-TAIL-MOMENTS','R-046 TM1–22; Sarkar Theorem D/6.4 for the coefficient threshold','Prove actual canonical surjectivity at the tail moment threshold','proved','For a,n≥2 and λ⊢an, put ν=(λ2,...),D=|ν|,t=ν1. The actual h_(n,a) is surjective on the full λ-isotypic component for D+t≤2n+1. Independent-row polarization, triangular Möbius moment substitution and finite centered evaluation factor the actual transpose with scalar1. This proves every even-tail component in full multiplicity at n≥|ρ|+ρ1 and every λ2≤b band at n≥floor(ab/2).'),
      ('Q-MAP-SINGLE4','R-044 SF1–14; R-039–R-043','Determine the actual map on every component with λ2≤4 and λ3≤3 in the ordered range n≥a≥2','proved','The actual four-column invariant-algebra surjection exhausts the four allowed single-four tail families. The explicit unit scalars and two- and three-dimensional moment matrices, with all finite-row relations and n2/n3 endpoints, give surjectivity on the entire isotypic component. The normalized grid map and rational preimages are retained.'),
      ('Q-MAP-SECOND3','R-036 CT1–20','Determine every actual canonical rank in the complete second-row-at-most-three band','proved','The actual signed exterior-invariant algebra excludes all tails except2^j and3,2^j. The latter unit target exists for n≥3 and j≤a−3 and has image1 exactly for j≤n−3. The cubic-minor scalar, n2 extension failure and complete band cokernel are proved. Every n≥a reaches the full band.'),
      ('Q-IDEAL-ORDER2','G-030 ZS1–11;T-045,T-050,T-051,G-021','Evaluate every outer-five flag family of ideal order at most two','proved','The disjoint twist families exhaust k=1,2, and the stable k=0 chart is explicit. Every shape with λ2≤n+2 orλ4≥n−2 has a fixed positive coefficient formula, exact support and specified complementary-column map.'),
      ('Q-MAP-SECOND2','R-035 SR1–17','Determine every actual canonical rank in the complete second-row-at-most-two band','proved','For a,n≥2 the only nonzero targets are the top row and (an−2j,2^j),1≤j≤a−1, each once. The latter image has rank1 exactly for j<n. The exact determinant-square scalar and all vanishing tails are proved. Degree-one maps are identities; natural dimension zeros are retained.'),
      ('Q-MAP-OUTER5','R-031 OF1–11; Jacob Def1.1.11,§4.2,Table4.4; CIM Theorem1.1','Determine every canonical rank with target outer degree five','proved','The actual rank is the source multiplicity for n≤4, the target multiplicity minus the eight published kernel copies for n=5, and the full target for n≥6; scalar-one adjunction and exact fourth-square normalization are proved. All313 small-degree shapes were independently evaluated.'),
      ('Q-IDEAL-ORDER1','G-026;T-045;G-021, exact c=λ2−λ3 dictionary','Evaluate every outer-five flag family of ideal order one','proved','G026 covers c=0, T045 covers c=1, and G021 covers every c≥2, including all support and determinant parity.'),
      ('Q-MAP','Sra III Theorem 1.3; boundary b=(a-1)^2-1','Full canonical-map rank in remaining parameter families','open with reduced component and finite boundary gates','G-011 counts ranks effectively; G-013 gives prime-adjacent semigroup preimages; G-014 lifts every tail of size at most the coordinate degree; R-011--R-015 certify specified common-polarization boundaries. R-019--R-023 remove the full first-row boundary band and the rectangular prolongation; R-024 gives recursive second-row ranges from actual degree-five and square bases; R025--R030 remove explicit multiplicity-one cofactor families and both complete endpoint strips throughout their below-square intervals, including the second-cofactor critical component, R031 determines the entire actual canonical rank law with target outer degree five, in every inner degree. R032 adds five preceding-degree families; R034 proves the arbitrary-power band injection and the exact capped linear thresholds B_t+Σ_(r=5)^(a−1)min(r,t), as well as b≥t(a−1). R033 gives the entire unit-multiplicity two-column-tail family and rectangular-Kronecker consequences. R035 determines the entire second-row≤2 canonical rank law: its nonzero unit target components (an−2j,2^j) have actual image1 exactly for j<n, with the top-row image1 and all one-box tails zero; every n≥a reaches the full band. R036 computes the entire second-row≤3 rank law and exact cokernel, through the signed invariant-algebra map and normalized cubic-minor scalar. R037 constructs explicit nonzero preimages for every even tail2ρ at n≥|ρ|+ρ1. R039 determines the whole unit component(an−2m−1,4,2^(m−2),1): target1 for a≥m+1,n≥3 and actual image1 exactly n≥m+1. R040 adds the complete unit family(an−2m−2,4,3,2^(m−3),1), with target1 for a≥m+2,n≥3 and image1 exactly n≥m+2; its weighted-minor scalar and inverse include all finite-row zero endpoints. R041 determines the whole higher-row block(an−2m−2,4,2^(m−1)) for m≥2,a≥m+1,n≥4: target min(3,a−m), image min(3,a−m,max(0,n−m)), with full three-by-three matrix, all finite-row relations and endpoint ranks. R042 completes the inner-degree-two and three endpoints of R041 by the exact row-degree-four functional and cubic moment matrix. R043 gives the full mixed block with tails(4,3,2^(m−2)), its two-dimensional matrix and all cubic endpoints. R044 exhausts every single-four tail via the actual invariant-algebra surjection and proves full isotypic surjectivity for λ2≤4,λ3≤3,n≥a≥2. R045 determines the repeated-four block(an−8,4,4), including its four-by-four normalized matrix, rank min(4,a−2,n−2) for a≥3,n≥4, exact finite relations and all cubic/quadratic endpoints. R046 proves full isotypic surjectivity for tail size D and width t with D+t≤2n+1, through an injective exact moment factorization; the remaining gate excludes this entire range. R047 gives the finite repeated-four mixed profile and exact ranks with one dimension at its threshold. R048 and R049 replace the uniform tail threshold by M=floor((D+t−ceil((o−(t mod2))/3))/2), using the actual averaged row map, and give explicit positive ranks with unbounded row improvement. R050 then proves the actual canonical isomorphism on every hook tail (t,1^r), including all unstable inner degrees, with explicit nonzero unit scalars in every outer rank. The remaining map gate excludes all of these full-isotypic ranges and all hook tails. R038 refines the already known binary isomorphism with its explicit quartic matrix/inverse and is not counted as a newly removed rank gate. The remaining critical annihilator injects into N_r tensor Sym^(r²-1), where N_r has first row at least r²+1 and second row at least r(r-1).'),
      ('Q-W7','Width-seven orbit calculation T-020','Small direct formula for all remaining valuation-filtered G2 invariant spaces','open','T-018 evaluates the end-node sector; G-010 gives a general finite count; evaluate the remaining boundary valuation filtration.'),
      ('Q-ALPOGE','Alpoge Remark p.4 steps 7--8; named Lean files absent','Identify the period/theta-lift object with the normalizer projector or grid-map image','input and explicit-morphism gate','No such comparison map is specified in the four-page note; T-001--T-003 construct the exact compact realization used here.'),
      ('Q-MASULLO','Prompt requested locator; no supplied work','Determine the intended Masullo theorem and map','input gate','No Masullo source or statement identifier in the 25 supplied files.'),
    ]
    rows.extend(dict(zip(fields,r)) for r in openq)
    with (OUT/'QUESTIONS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    return rows

def build_tex():
    intro=(ROOT/'work/root/paper_front.md').read_text()
    chunks=[intro]
    for part,files in REPORTS:
        chunks.append('\\part{'+part+'}\n')
        for name in files:
            p=ROOT/name
            if p.exists(): chunks.append(p.read_text())
    md='\n\n'.join(chunks)
    (ROOT/'work/paper.md').write_text(md)
    cmd=['pandoc',str(ROOT/'work/paper.md'),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+autolink_bare_uris',
      '-t','latex','-s','--toc','--number-sections','--top-level-division=section',
      '-V','documentclass=article','-V','fontsize=10pt','-V','geometry=margin=25mm',
      '-V','mainfont=DejaVu Serif','-V','monofont=DejaVu Sans Mono',
      '-V','mathfont=Latin Modern Math',
      '-V','colorlinks=true','--include-in-header='+str(ROOT/'work/preamble.tex'),
      '--lua-filter='+str(ROOT/'work/wrap_code.lua'),'-o',str(OUT/'GCT_PLETH.tex')]
    subprocess.run(cmd,check=True,capture_output=True,text=True)

def external_snapshot_paths():
    paths={
      'work/theta/unstable_hook/nagel_trok_2020.pdf',
      'work/theta/unstable_hook/nagel_trok_2020.txt',
      'work/theta/outer4/jacobians.pdf',
      'work/theta/outer4/jacobians.txt',
      'work/theta/sarkar_source.tar',
      'work/theta/sarkar/main.tex',
      'work/theta/sarkar/00README.json',
    }
    fetch=ROOT/'work/rectangular/sixth_source_audit/PRIMARY_FETCH.json'
    if fetch.exists():
        for r in json.loads(fetch.read_text()):
            paths.add('work/rectangular/sixth_source_audit/'+r['path'])
    return paths

def manifest():
    rows=[]
    snapshots=external_snapshot_paths()
    for p in sorted((ROOT/'work').rglob('*')):
        if not p.is_file() or '__pycache__' in str(p):continue
        if str(p.relative_to(ROOT)) in snapshots or (p.suffix in ['.pdf','.txt','.html','.tar','.tex','.mw'] and ('external' in p.parts or 'archive' in p.parts or 'width7' in p.parts or 'end_node' in p.parts)):
            rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'work/consulted_source_manifest.json').write_text(json.dumps(rows,indent=2))

def package(name):
    target=ROOT/name
    if target.exists(): raise FileExistsError(target)
    snapshots=external_snapshot_paths()
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for p in sorted(ROOT.rglob('*')):
            if not p.is_file():continue
            rel=p.relative_to(ROOT)
            if str(rel) in snapshots:continue
            if rel.parts[0] not in ['deliverables','work','sources','upload']:continue
            if p.suffix=='.zip' or '__pycache__' in rel.parts:continue
            if 'library_helpers' in rel.parts or p.suffix in ['.o','.pyc']:continue
            if p.suffix=='' and p.open('rb').read(4)==b'\x7fELF':continue
            if p.suffix=='' and p.name.startswith(('check_polarization','recheck_polarization','character_')):continue
            if 'texfmt' in rel.parts:continue
            if 'public_scans' in rel.parts and 'ranges' in rel.parts:continue
            if any(part.startswith('polarization_') and part.endswith('_parts') for part in rel.parts):continue
            if p.suffix=='.input' and p.stat().st_size>20_000_000:continue
            if p.suffix in ['.aux','.log','.toc','.out','.fls','.fdb_latexmk','.xdv']:continue
            # User-provided sources remain present. External papers are cited and hashed,
            # not redistributed; all current proofs, code and certificates are included.
            if rel.parts[0]=='work' and p.suffix in ['.pdf','.txt','.html','.tar','.tex','.mw','.png']:
                if 'external' in rel.parts or ('archive' in rel.parts and not any(token in p.name for token in ['CERTIFICATE','CHECK','RECEIPT','RESULT'])) or 'braun' in rel.parts or 'series' in rel.parts:
                    continue
                if 'width7' in rel.parts and p.name not in ['METRIC_PATH_CHECK.txt']:continue
                if 'end_node' in rel.parts and p.suffix=='.pdf':continue
            if rel.parts[0]=='deliverables': arc=str(Path(name[:-4])/Path(*rel.parts[1:]))
            else:arc=str(Path(name[:-4])/rel)
            z.write(p,arc)
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        names=z.namelist()
        for n in ['GCT_PLETH.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md']:
            assert name[:-4]+'/'+n in names,n
        assert not any(n.endswith('.zip') for n in names)
    return target

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--package');args=a.parse_args()
    es=merge_events();qs=questions();manifest();build_tex()
    print(json.dumps({'events':len(es),'questions':len(qs),'tex_bytes':(OUT/'GCT_PLETH.tex').stat().st_size}))
    if args.package:print(package(args.package))
