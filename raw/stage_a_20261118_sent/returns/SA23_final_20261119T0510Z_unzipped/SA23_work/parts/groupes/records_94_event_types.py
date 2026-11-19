"""Match event labels to the actual verification performed."""
for e in events:
    if e[3]=='recomputed with code':e[3]='computation or formal certificate'
    if e[3]=='manual consolidation with linked proof checks':e[3]='used and rechecked in this run'
    if e[0] in [f'C-SA23-groupes-{n:03d}' for n in [20,22,27,41,67,72,73,74,82,88,91,99,104,108,111]] and e[3] in ['independent re-proof','carried as background without fault found']:
        e[3]='used and rechecked in this run'
    if e[0] in [f'C-SA23-groupes-{n:03d}' for n in [29,81,86,98]] and e[3]=='independent re-proof':
        e[3]='targeted proof check'
for c in claims:
    if c['id']=='C-SA23-groupes-017':
        old='The actual Barsotti–Tate comparison under a complete discretely valued field with perfect residue field'
        new='The actual Barsotti–Tate comparison under Liu’s finite totally ramified extension K/K0, with K0 the fraction field of the Witt vectors of a perfect residue field'
        for k in ['proof_or_check']:
            c['computation'][k]=c['computation'][k].replace(old,new)
        c['present_status']=c['present_status'].replace(old,new)
        for e in events:
            if e[0]==c['id']:e[4]=e[4].replace(old,new)
