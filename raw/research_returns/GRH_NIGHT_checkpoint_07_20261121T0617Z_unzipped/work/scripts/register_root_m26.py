from pathlib import Path
from datetime import datetime,timezone
import json,csv
base=Path(__file__).resolve().parents[2];root=base/'work/root'
now=datetime.now(timezone.utc).isoformat()
rows=json.loads((root/'rows.json').read_text())
assert not any(x['id']=='MT-M26' for x in rows)
with (root/'section.tex').open('a') as f:f.write('\n'+(root/'masullo_strip_trace.tex').read_text())
rows.append(dict(id='MT-M26',statement='The literal fixed-character Masullo strip Hilbert quotient retains every zero jet when its strip contains all zero real parts in its interior; its smooth quotient map is faithful with proper dense image. Every exponential-Schwartz convolution is trace class with traceΣmρ Mg(ρ−a), uniformly on bounded test sets. A strip containing[0,1] works unconditionally; under M_H any positive-width strip centered at1/2 works.',input='neither for the containing-strip theorem and GRH/trace-positivity equivalence on a wide strip; Masullo (conditional) for arbitrary positive-width centered strips; fixed character throughout',status='proved here with actual Hilbert closed-kernel equality, bounded block maps, trace-norm convergence and dense-extension argument; no positive-operator or varying-character uniformity assertion',where_the_proof_is='GRH_NIGHT.tex MT-M26; work/root/masullo_strip_trace.tex; literal source9.2.2.31p416,Definition10.1.1.1p434,(10.4.1.3)p456',where_it_lives='MasulloCh10 actual Hilbert trace route; Q-MAS-INFINITE-BASIS and Q-MAS-STRIP-TRACE; cote1/SA23 geo-H-lidskii/geo-H-genus'))
(root/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (root/'events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['MT-M26',now,'/root','GPT-6 Astra Pro','not exposed','GRH_NIGHT_20261121','targeted proof check','Read entire proof and both concluding deductions. Checked adapted rectangle minimum modulus with positive vertical zero distance, uniform Hilbert restrictions, polynomial lifts, finite-rank trace-norm bound, identity on dense smooth image before injectivity, approximate-identity kernel argument, proper density, involution pairing and GRH equivalence. Independently read originalPDF416 norm and434 closure; actual max-weight formula matches. No gap found.'])
with (base/'work/checks/source_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['M-SOURCE',now,'/root','GPT-6 Astra Pro','not exposed','GRH_NIGHT_20261121','used and rechecked in this run','Fresh originalPDF text-layer read of entirep416 andp434 confirms literal norm9.2.2.31 and closureDefinition10.1.1.1 used in MT-M26. No use of the draft theorem claiming trace class; M_H remains conditional.'])
qp=root/'questions.tsv'
with qp.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;qs=list(reader)
for q in qs:
    if q['id']=='Q-MAS-INFINITE-BASIS':q['state']+=' MT-M26 proves actual fixed-character strip-Hilbert trace class and faithful completion whenever its interior contains all zero real parts; global varying-character uniformity remains separate.'
qs.append(dict(id='Q-MAS-STRIP-TRACE',source_and_locator='Masullo9.2.2.31p416;10.1.1.1p434;10.4.1.3p456;MT-M24',question='Does the actual strip Hilbert quotient retain the full zero divisor and have trace-class convolution?',state='proved MT-M26 for each fixed character with an interior containing strip: exact closed kernel, faithful proper dense smooth image and traceΣmρ Mg(ρ−a). Unconditional strip contains[0,1]; under M any positive-width strip centered at1/2 suffices. All-character trace requires separate uniform estimates.'))
with qp.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(qs)
with (root/'implications.md').open('a') as f:
    f.write('\n## Trace class on the draft’s actual strip Hilbert quotient\n\nMT-M26 proves the exact closed kernel and trace-class convolution on the literal fixed-character Hilbert quotient of Masullo(10.4.1.3). A strip containing[0,1] in its interior suffices unconditionally; M_H narrows it to every positive-width strip centered at1/2. The smooth full-jet quotient has proper dense image, so its stronger topology is not confused with this norm. The remaining all-character passage is explicitly a uniform-estimate question, while scalar trace positivity remains equivalent to GRH on a wide strip.\n')
with (root/'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — literal strip Hilbert trace proved\n\nMT-M26 closes the fixed-character trace-class and exact-kernel gate for the actual Masullo strip Hilbert quotient. It has complete author and root readings, with source norm and closure checked directly. No independent positivity argument or global varying-character summation is claimed.\n')
print(json.dumps(dict(date=now,root_rows=len(rows),new='MT-M26')))
