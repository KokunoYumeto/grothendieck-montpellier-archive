"""Record the actually completed root proof and certificate audits after CP10."""
from pathlib import Path
import csv, datetime
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[]
for label in ['lem:DE-A3-theta-pfaffian','prop:DE-A3-ppav-degree-one',
              'lem:DE-A3-ppav-odd-norm','lem:DE-A3-ppav-even-bound','thm:DE-A3-ppav-ranks']:
    events.append((label,'independent re-proof',
      'PASS: complete universal ppav rank proof read and rederived. Checked invariant-cubic Pfaffian formula, all exceptional tensors and Fourier projectors, global descent against Oda simplicity, typed relative determinant, every odd maximal-isotropic norm and exceptional jet incidence, exact symmetric norm class, connected Prym and even 2-torsion bound. Debarre original Section3 equations3.2-3.3 pp346-347 opened/read with arbitrary-characteristic scope.'))
for label in ['thm:ss-product-degree-two-full-group','thm:ss-product-degree-three-full-group']:
    events.append((label,'independent re-proof',
      'PASS: full proof read; checked coherent/Cartier transpose and Lang inverse, maximal-rank stable bundle at possibly singular coefficient points, actual geometric GL8 block, primitive-prime normal-transvection closure and Clifford multiplicities. Degree2 additionally checked self-normalizing complement and the literal fixed-lift obstruction. Exact independent verifiers read and rerun.'))
events.append(('prop:B-RD33','independent re-proof',
      'PASS: full graph proof; integral perfect pairings and inverse via Tate full-BT faithfulness, maximal-isotropic flat closure, tame idempotent decomposition, unique 1-dimensional formal subgroups, all quotient Q_r and generic-isomorphism/special-zero maps. Original Tate Theorem4 and Corollaries1-2 with proof/Proposition12 pp181-182; Sections1.2-1.3 pp159-160 read. No new numerical upper bound claimed from this equality alone.'))
for label in ['lem:linear-covectors-any-nil-length','lem:surface-frobenius-distributions','thm:nonordinary-ppav-all-covectors']:
    events.append((label,'targeted proof check',
      'Root complete proof written and checked; independent monodromy and obstruction/crystal full proof/source/code audits PASS. Arbitrary nil-length root extension, pole removal and exponent induction force linear lifts; torsor adjunction identifies End(F_*O) with distributions. Restricted-Lie rational normal forms give every exact operator and arithmetic descent. Even invariant dimensions 1 for two-rank0, 2 for two-rank1; odd0. Scope complete systems all degrees, ambient systems at stated regularity bound.'))
for label,program,seconds,out in [
 ('CP11-SS2-CODE','verify_supersingular_degree_two_group.py',0.08990957599962712,'outputs/root_verify_supersingular_degree_two_group.json'),
 ('CP11-SS3-CODE','verify_supersingular_degree_three_group.py',0.4399738840002101,'outputs/root_verify_supersingular_degree_three_group.json'),
 ('CP11-PPAV-RANK-CODE','A3_ppav_rank_checks.py',0.29324621799969464,'outputs/root_A3_ppav_rank_checks.json'),
 ('CP11-PPAV-COVECTOR-CODE','ppav_nonordinary_covector_checks.py',0.09968187000049511,'outputs/root_ppav_nonordinary_covector_checks.json')]:
    events.append((label,'computation or formal certificate',
       f'PASS: complete program {program} read and run; runtime {seconds} seconds; full output {out}. Author outputs preserved. Finite or symbolic scope stated in each program and proof; no extrapolation from sampled degrees.'))
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,kind,outcome in events: writer.writerow([label,now,who,kind,outcome])
print(f'Recorded {len(events)} actual root audit events at {now}.')
