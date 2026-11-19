"""Update the Part C result ledger after coefficient-dimension reduction."""
from pathlib import Path
import csv
import json
import time

start = time.perf_counter()
root = Path(__file__).resolve().parents[2]
path = root / 'part_c/results.csv'
with path.open(newline='') as handle:
    rows = list(csv.DictReader(handle))
fields = list(rows[0])
entry = ['c:broader-coefficients', 'General polygon and manuscript margin bound for strictly special coefficients of arbitrary presenting relative dimension', 'Proved in the stated finite-type setting', 'sections/part_c.tex, Proposition label c:broader-coefficients', 'Relative Bertini; hard Lefschetz pairing; purity and support induction; etale Cech descent Stacks072G', '12:111-120; C.4', 'General level min(i,2n-i)+j and margin level min(i,n-1)+j. Stronger reflected margin polygon retains the normalized presentation in this proof.']
if not any(row['id']==entry[0] for row in rows):
    rows.append(dict(zip(fields, entry)))
for row in rows:
    if row['id']=='c:level-optimality':
        row['notes']='For j>0 weight envelope is attained in interior degrees. Top endpoint improved to2n+j; lower endpoint has exact local-invariant-cycle gate.'
with path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields)
    writer.writeheader()
    writer.writerows(rows)
events = root / 'part_c/CHECK_EVENTS.tsv'
prior = events.read_text()
records = [
    ['c:broader-coefficients','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Dense-open generic Bertini, regular-stratum purity, and codimension inequalities prove the full epsilon0 polygon; etale Cech descent proves the requested margin bound.'],
    ['c:broader-coefficients','2026-11-19','GPT-6 Astra (OpenAI), /root/part_b','independent re-proof','Passed nested-support triangles, regular immersion purity and inherited dimension drop; dense generic normalization may use finite etale cover with trace. Passed etale Cech monotone argument; stronger margin reflection not inferred.'],
    ['c:top-direct-image','2026-11-19','GPT-6 Astra (OpenAI), /root/part_b','independent re-proof','Passed Gabber support bound including c>=1, even-q improvement, absence of new vertical maximal components, and top-cohomology Poincare duality.'],
]
with events.open('a', newline='') as handle:
    writer=csv.writer(handle, delimiter='\t')
    for row in records:
        if row[-1] not in prior: writer.writerow(row)
sources=root/'part_c/sources.tsv'
if 'stacksdescent\t' not in sources.read_text():
    with sources.open('a') as handle:
        handle.write('stacksdescent\topened exact statements and proofs\thttps://stacks.math.columbia.edu/tag/072G\tProposition96.21.1;Theorem59.19.2 Tag03OW; l-adic passage independently supplied\n')
notes=root/'part_c/part_c_notes.md'
prior=notes.read_text()
header='## Broader coefficient convention resolved for the requested bounds\n'
if header not in prior:
    notes.write_text(prior.replace('# Part C research ledger\n','# Part C research ledger\n\n'+header+'\nThe presenting smooth projective family may now have arbitrary relative dimension. Generic Bertini normalizes it over a dense open; a regular-stratum filtration of local cohomology and absolute purity supply the full general simultaneous polygon by dimension induction. The original margin bound follows from normalization on a surjective etale cover and Cech descent. Part B independently checked both arguments. Hence the former coefficient-dimension ambiguity is no longer an unresolved gate for the bounds actually requested. The still stronger reflected margin polygon proved for normalized coefficients remains restricted to that convention in our current proof.\n'))
checks=0
for n in range(1,31):
    for c in range(1,n+1):
        for np in range(0,n-c+1):
            for i in range(2*c,2*n+5):
                m=i-2*c
                lower=c+max(0,m-np)
                upper=c+min(m,np)
                assert lower>=max(0,i-n)
                assert upper<=min(i,n)
                checks+=1
output={'result_rows':len(rows),'events':sum(1 for _ in events.open())-1,'stratum_shift_checks':checks,'input_n_range':[1,30],'runtime_seconds':time.perf_counter()-start}
(root/'code/part_c/update_broader_records_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
