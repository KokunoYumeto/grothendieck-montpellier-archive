"""Update the current gate summary and recovery provenance without changing old checkpoints."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time

start=time.perf_counter();base=Path(__file__).resolve().parents[1]
status=base/'STATUS.md';lines=status.read_text().splitlines()
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
header=('Checkpoint state: '+stamp+', reconstructed through C.3aq after scratch loss. '
 'The complete universal ordinary complex local restriction table is proved, integrally and rationally, '
 'with specified infinite-order kernels in every negative injectivity dimension and specified cokernels '
 'in every negative surjectivity dimension. The original full audits and fresh reconstruction checks '
 'are recorded separately; lost computations and builds are rerun with new timings. C.3an/aq refute '
 'integral top-quotient finiteness in dimension three in all positive characteristics. '
 'AI-produced by GPT-6 Astra (OpenAI), child task /root/cycles; no person credited, no priority claimed, '
 'and no independent-model verification claimed. Root, frobenius and real_weil supplied independent '
 'targeted checks within the same model/run.')
row=('| C.3 | INCOMPLETE as a full task; global universal surjectivity and the entire ordinary complex '
 'local restriction table are settled, as are all nonzero ordinary-J/Chow local-finiteness refutations '
 '| C.3a–aq and C.1f: the prior results; C.3z gives the ordinary degree-one positive-characteristic scope; '
 'C.3aa refutes finite B^r in every non-top degree; C.3ab/ad prove restricted top-cone theorems; '
 'C.3ac settles the Fpbar abelian branch with its2026-qualified strengthening separate; '
 'C.3an/aq give exponent-p integral top quotients in dimension three; C.3ao covers all r>=2,N>=2r+1 '
 'ordinary kernels; C.3ap completes the integral and rational complex table: r>=2 injection iffN<=r, '
 'surjection iffN<=r+1,isomorphism iffN<=r, with the separate degree-one table proved '
 '| Universal higher smooth-projective Griffiths/Beauville/J injectivity over C; exact individual-variety '
 'higher kernels and cokernels; rational top local B^(N−1) for N>=3 including the complex case; '
 'higher-degree positive-characteristic restriction. Universal ordinary complex local restriction is no longer a gate |')
for i,line in enumerate(lines):
 if line.startswith('Checkpoint state:'):lines[i]=header
 if line.startswith('| C.3 |'):lines[i]=row
text='\n'.join(lines)+'\n'
text=text.replace('Higher local restriction injectivity and higher-degree positive-characteristic questions remain separate.',
 'The injectivity question was subsequently completed by C.3al/am/ao and synthesized in C.3ap; higher-degree positive-characteristic questions remain separate.')
marker='\n## Recovered ordinary complex restriction classification\n'
if marker in text:text=text.split(marker)[0]
am=json.loads((base/'output/critical_injectivity.json').read_text())
ao=json.loads((base/'output/absolute_picard_kernel.json').read_text())
fetch=json.loads((base/'output/fetch_injectivity_sources.json').read_text())
build=json.loads((base/'output/compile_recovered_injectivity.json').read_text())
clean=all(all(c['returncode']==0 for c in item['runs']) and not item['diagnostics'] for item in build['wrappers'])
text+=marker+f'''
C.3al turns the actual nonzero Gysin classes of C.3t into integral closed-restriction kernels by principal self-intersection. C.3am covers the critical N=2r case using an elliptic family on an odd Fermat cubic whose coordinate section factors through the rational Fermat cubic surface. The full source nonvanishing is the previously audited C.3r calculation; the target equality is integral.

C.3ao supplies all r>=2,N>=2r+1. A homogeneous formal-Pic class algebraizes to an actual line bundle on the strict cone resolution. Its restriction to the principal puncture is trivial at every order, hence actually trivial by Elkik. Multiplying it by specified Pic0 divisor classes gives an actual ordinary family. Absolute Milnor-dlog cohomology, the residue −p*omega, and independent field differentials detect non-torsion; an integral projective-bundle coefficient recursion excludes exceptional boundary classes. This does not use a relative-complex Chern detector or a Chow Lefschetz conjecture.

C.3ap consequently proves, for r>=2, universal injection exactly for N<=r, surjection exactly for N<=r+1, and isomorphism exactly for N<=r. For r=1, injection holds exactly for N=1 or N>=3, surjection exactly for N<=2, and isomorphism exactly for N=1. Integral ordinary and rational tables agree. These are universal dimension statements in the specified complex coefficient-field scope; different pairs may witness the two negative columns.

The original root certification of ao/ap was2026-11-19T10:01:26.541461Z. After the scratch loss, root reread all reconstructed ao lines and renewed proof/fidelity PASS; real_weil reread am, ao and ap and passed them after two literal wording/spacing repairs. The checkpoint09 al proof survived unchanged. Fresh computation records: am runtime{am['runtime_seconds']} seconds, ao runtime{ao['runtime_seconds']} seconds; both pass all checks. The five recovered primary PDFs match their original SHA256 hashes, with fresh total retrieval runtime{fetch['runtime_seconds']} seconds. The restored registers contain four rows and32 events in the three named files; historical audit receipts are distinguished from recovery checks.

Fresh wrapper compilation state: {'all four wrappers clean' if clean else 'not yet all clean; retained logs identify the current format/font or layout failures'}. Total most recent wrapper runtime{build['runtime_seconds']} seconds. Failed recovery attempts remain in timestamped logs and are not described as successful builds.

C.3an/aq, owned by real_weil, give specified additive top quotients in local dimension three in every positive characteristic. Those exponent-p quotients do not decide the rational or complex top question. Current main C.3 gates are global smooth-projective injectivity, rational top local ordinary quotients, and higher-degree characteristic-p restriction. The proposed C.3ar product-of-curves cone theorem remains a separate draft until its full proof and exact source compatibility are audited; no gate closure is inferred from it.
'''
status.write_text(text)
for name,body in {
 'principal_gysin_REPORT.md':'C.3al proves the integral principal self-intersection inclusion and applies the exact C3t family in r+1<=N<=2r−1. Its proof survived checkpoint09. Original full root/frobenius/real_weil audits are recorded with their actual earlier times; the fresh wrapper is reported in the recovered build JSON.',
 'critical_injectivity_REPORT.md':'C.3am gives the critical N=2r kernels. The same elliptic class as C3r survives modulo H on the source. The coordinate hyperplane cuts its planes to the incidence over the Fermat cubic surface, whose explicit residual conic pencil and rational section prove CH0=Z integrally. The reconstructed proof removes the fixed Cartier line before the pencil, and both root historical audit and real_weil fresh fidelity check are recorded. The exact certificate and fresh timings are in output/critical_injectivity.json.',
 'absolute_picard_REPORT.md':'C.3ao supplies every remaining higher-dimensional ordinary kernel; C.3ap is the complete ordinary complex local restriction table. The proof separates actual formal-Pic algebraization, the ordinary divisor family, absolute Milnor-dlog detection over k0, and the integral exceptional-boundary recursion. Root certified the original at10:01:26.541461UTC and fully reread the reconstructed proof; real_weil independently passed both. Fresh certificate, source hashes, failed and successful wrapper logs, and event registers are retained. No global smooth-projective, rational-top, or positive-characteristic higher restriction claim is inferred.'
}.items():
 (base/name).write_text('# '+name.removesuffix('_REPORT.md').replace('_',' ')+'\n\n'+body+'\n\nReconstruction timestamp: '+stamp+'. Original lost computation outputs are not represented as retained; fresh reruns carry their own UTC and runtime_seconds fields.\n')
record={'utc':datetime.now(timezone.utc).isoformat(),'all_wrappers_clean':clean,
        'runtime_seconds':time.perf_counter()-start}
(base/'output/update_status_recovery.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
