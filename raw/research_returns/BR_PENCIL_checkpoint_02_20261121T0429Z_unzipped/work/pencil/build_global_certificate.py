#!/usr/bin/env python3
"""Package the already independently verified j=3,4,5 integer minors."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'


def main():
    audit=json.loads((HERE/'root_certificate_audit.json').read_text())
    audit={d['j']:d for d in audit}
    audit[5]=next(d for d in json.loads((HERE/'root_certificate_audit_strengthened.json').read_text()) if d['j']==5)
    replacement=json.loads((HERE/'det5_characteristic3_certificate.json').read_text())
    output=[]
    for j,target in [(3,8),(4,9),(5,11)]:
        original=json.loads((ROOT/f'j{j}.json').read_text())
        records=[]
        for item in original['records']:
            if item['support_bound']>=target:continue
            entry={k:item[k] for k in ['subset','support','support_bound','orbit_size']}
            entry['families']={}
            for family in ['det','per']:
                proof=next(x for x in audit[j]['minors'] if x['family']==family and x['subset']==item['subset'])
                if 'external_certificate' in proof:
                    entry['families'][family]={'lower_bound':11,'certificate':'R-04: unit-minor prolongation obstruction'}
                    continue
                cert=next(x for x in item['families'][family]['koszul']
                          if x['p']==proof['p'] and x['rank_mod_p']==proof['minor_order'])
                c={'p':cert['p'],'pure_cost':cert['pure_cost'],
                   'minor_order':proof['minor_order'],'rows':cert['rows'],'cols':cert['cols'],
                   'determinant_Z':proof['determinant_Z'],'lower_bound':proof['bound']}
                if j==5 and family=='det' and item['subset']==replacement['subset']:
                    c={'p':replacement['p'],'pure_cost':replacement['cost'],
                       'minor_order':len(replacement['rows']),
                       'rows':replacement['rows'],'cols':replacement['cols'],
                       'determinant_Z':replacement['determinant_Z'],
                       'lower_bound':replacement['threshold_bound']}
                entry['families'][family]=c
            records.append(entry)
        output.append({'j':j,'uniform_residual_lower_bound':target,
                       'all_subsets':original['number_of_subsets'],
                       'all_orbits':original['number_of_orbits'],
                       'low_support_orbits':len(records),'records':records})
    (HERE/'global_j345_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    # The main paper's full 26-row table.
    lines=[]
    for rec in output[-1]['records']:
        sub=','.join(map(str,rec['subset']))
        vals=[]
        for family in ['det','per']:
            c=rec['families'][family]
            if 'p' not in c:vals.append(r'\text{R-04}')
            else:vals.append(f"{c['p']};{c['minor_order']};{c['determinant_Z']}")
        lines.append(r'\(\{'+sub+r'\}\) & \('+vals[0]+r'\) & \('+vals[1]+r'\) \\')
    (HERE/'j5_table.tex').write_text('\n'.join(lines)+'\n')
    print(json.dumps([{k:v for k,v in item.items() if k!='records'} for item in output],indent=2))


if __name__=='__main__':main()
