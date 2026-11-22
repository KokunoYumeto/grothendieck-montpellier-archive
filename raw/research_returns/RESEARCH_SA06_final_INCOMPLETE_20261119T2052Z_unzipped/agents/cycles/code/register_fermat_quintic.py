"""Register actual C.3au proof/source/build checks after independent review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

start = time.perf_counter()
b = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
certificate = json.loads((b/'output/check_fermat_quintic_top.json').read_text())
build = json.loads((b/'output/compile_fermat_quintic_top.json').read_text())
assert not build['diagnostics'] and all(x['returncode'] == 0 for x in build['runs'])
assert (b/'fermat_quintic_top.tex').exists()
row = [
    'C.3au',
    'For the specified complex Fermat quintic surface cone, B^2(Z)_Q=Q by exceptional degree and B^2(X)_Q=0',
    'Proved in the stated restricted scope',
    'fermat_quintic_top.tex, C.3au',
    'C3ab/ad finite detection and Adams-weight-two calculation; C3ar coefficient-one normalization; actual Pic first jets; El Zein supported trace',
    '14:108-109',
    'Actual fixed proper-curve families; specified degree-five blown-up product cover; no integral, arbitrary-quintic, or arbitrary-isolated-singularity claim. Restricted result, no main-gate reset.'
]
with (b/'fermat_quintic_results.csv').open('w', newline='') as f:
    w=csv.writer(f); w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']); w.writerow(row)
checks = [
    ('targeted proof check','Verified fixed-level relative Adams group and its first-neighbourhood concentration; the absolute coefficient differential group is retained, not declared zero.'),
    ('targeted proof check','Verified the explicit degree-five cover, all25 reduced base points, both blow-up charts and the nonample source pullback line bundle.'),
    ('targeted proof check','Constructed an actual line bundle with any prescribed first Picard jet by formal existence, Popescu descent and henselian smooth lifting; no arbitrary formal K0 algebraization.'),
    ('targeted proof check','Verified finite-fibre differential evaluation and scalar absorption into the actual Picard parameter; all products arise from one fixed proper parameter curve.'),
    ('targeted proof check','Verified the first-conormal trace through -iota_theta, the global meromorphic eta/t, supported residue duality and exact branch multiplicities; no ramification is discarded.'),
    ('targeted proof check','Verified the Tor-independent Cartier square, finite first-jet elimination, exceptional degree quotient and localization.'),
    ('primary-source verification','Opened and read full El Zein1974/1978 primary scans, exact1974Prop2.1.2pp15-16 and1978supported duality/residuepp31-33,Prop2p41; visually inspected originalpp15,31,32,33,41. Source audit records p32 printed subsection-number anomaly.'),
    ('primary-source verification','Opened/read Stacks07GC,09RF,0H74 with proofs for actual Picard finite-jet approximation; reread Braunling Section4 residue normalization. Earlier exact BEK/CHW/Loday inputs retain their audited scope.'),
    ('finite exact computation',f"Certificate completed {certificate['utc']}; runtime {certificate['runtime_seconds']} seconds; exact defining/blow-up/inverse/evaluation/first-jet identities only. Full code,JSON and stdout retained."),
    ('independent full proof and source audit','Root full PASS certified2026-11-19T11:27:59.592062UTC, notes/ROOT_C3au_FERMAT_AUDIT.md. Complete revised proof, contraction sign, primary pages and finite certificate reviewed. No additional independent-model audit claimed.'),
    ('typesetting verification',f"Final renamed four-pass wrapper completed {build['utc']} in {build['runtime_seconds']} seconds; every command succeeded and diagnostic list empty. PDF and each stdout retained.")
]
with (b/'fermat_quintic_CHECK_EVENTS.tsv').open('w', newline='') as f:
    w=csv.writer(f, delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
    for typ, outcome in checks:
        w.writerow(['C.3au',stamp,'GPT-6 Astra (OpenAI); inherited reasoning effort; /root/cycles',typ,outcome])
report={'utc':stamp,'rows':1,'events':len(checks),'runtime_seconds':time.perf_counter()-start}
(b/'output/register_fermat_quintic.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
