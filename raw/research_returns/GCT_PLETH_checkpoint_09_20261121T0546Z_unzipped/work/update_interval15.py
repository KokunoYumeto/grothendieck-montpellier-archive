from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/theta/unstable_hook/first_unstable_hook_report.md'" not in s
s=s.replace("'work/root/stable_hook_report.md'","'work/root/stable_hook_report.md','work/theta/unstable_hook/first_unstable_hook_report.md'")
s=s.replace("      ('Q-STABLE-HOOKS'","      ('Q-FIRST-UNSTABLE-HOOKS','T-061 UH1–10; G-037 HK1–19; G-015','Evaluate every valid first unstable hook tail in varying outer degree','proved in the stated explicit encoding','For m≥4,a≥2,0≤r≤m−2,t≥0 with (m−2)a≥m+r, inner n=a+t−1 and λ=((m−1)a+t−m−r,a+t,(t+1)^r,t^(m−2−r)), the coefficient is the G037 stable hook value minus one on at most three specified induced hook labels. Actual equivariant evaluation splittings prove the kernel comparison. At a2 the exact single-Specht endpoint is proved. At a≥3 a specified G037 lattice point is deleted by at most2(m²+3m−4) disjoint bounded polytopes of at most m²+3m−4 variables. Binary-degree evaluation and support are polynomial in m and the binary parameters, retaining the t0 compressed-encoding caveat.'),\n      ('Q-STABLE-HOOKS'")
p.write_text(s)
note=r'''## First unstable hook order

T061 completes all valid first-order unstable hook tails in varying outer degree: \(n=a+t-1\), \(\lambda=((m-1)a+t-m-r,a+t,(t+1)^r,t^{m-2-r})\), \(m\ge4\), \(a\ge2\), and \((m-2)a\ge m+r\). The exact point evaluation has an explicit equivariant right inverse, including the smallest degree through its frame adjoint. The target consists of at most three indicated Specht labels, each once. The coefficient is the stable G037 value with one removed on those labels. An explicit tableau/subset/coin point and the first-different-coordinate partition realize this as at most \(2(m^2+3m-4)\) disjoint positive polytopes. Degree two has the stated single-Specht value. Author and root whole-proof readings pass; the separate independent archive review remains in progress. The author computation records9336 cycle-character comparisons,3162 removed-point validations, and129 literal polytope cases with3012 cells and212 original witnesses, of which161 remain. This is a completed formula for ideal order one; higher hook ideal orders remain active.
'''
for name in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(name);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in name else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text().replace('and for unstable hook charts.','and for hook charts of ideal order at least two. T061 completes every valid first unstable hook order with actual evaluation splittings and a positive deleted-point formula; its degree-two endpoint and full varying-degree encoding scope are proved.');p.write_text(s)
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writerow(dict(statement_id='T-061',date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type='targeted proof check',outcome='Read complete UH1–10, all six sections and the entire executable. Checked exact flag pushforward, all a≥3 interpolation maps, a2 frame-adjoint injection and Gram splitting, induced three-label decomposition, degree-two complement, every explicit tableau/subset point including22, binary coin construction and disjoint first-difference lattice bijection. Corrected rendering typo was confirmed. PASS. Computation remains attributed to author; archive review is in progress.'))
print(stamp,'integrated T061 after author/root full checks')
