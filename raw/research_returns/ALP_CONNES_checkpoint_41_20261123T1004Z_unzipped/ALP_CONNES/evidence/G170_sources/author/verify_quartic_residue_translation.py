"""Exact translation only; the reflection/strict theorem is separate."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

BASE = Path(__file__).resolve().parent
P = 269
input_path = BASE/'quartic_odd_annihilator_table.json'
table = json.loads(input_path.read_text())
lookup = {(r['sigma'],r['a'],r['b'],r['k']): r for r in table['rows']}
assert len(lookup) == 1072
families = []
for sigma in (1,-1):
    for a in (0,1):
        rows = []
        for r in range(268):
            extensions = []
            for b in (0,1):
                exponent = (-r) % 268
                odd = (exponent+a+b) % 2 == 0
                source = (sigma,a,b,exponent) if odd else (-sigma,a,b,(1-exponent)%268)
                witness = lookup[source]
                extensions.append({'b':b,'class_character_exponent':exponent,
                                   'odd_source':list(source),'method':'direct' if odd else 'reflection',
                                   'operator_witness':witness['nonzero_witness'],
                                   'operator_value':witness['witness_value']})
            rows.append({'residue':r,'two_extensions':extensions,
                         'both_supported':all(x['operator_witness'] is not None for x in extensions)})
        excluded = [x['residue'] for x in rows if not x['both_supported']]
        expected = {(1,0):[243,248],(-1,0):[19,24],(1,1):[11,60,229],(-1,1):[38,207,256]}
        assert excluded == expected[(sigma,a)]
        # At the rational prime269, phi(269)=phi(13)=i;
        # chi_-4(269)=1.  K_p has residue degree2.
        rational_frob = pow(82,sigma,P)
        assert rational_frob*rational_frob % P == P-1
        assert rows[0]['both_supported']
        families.append({'sigma':sigma,'a':a,'excluded':excluded,
                         'supported_count':268-len(excluded),'rational_frob_269':rational_frob,
                         'K_local_frob':P-1,'rows':rows})
assert sum(f['supported_count'] for f in families) == 1062
assert pow(P,4,48)==1 and pow(P,2,48)!=1
result={'utc':datetime.now(timezone.utc).isoformat(),
        'status':'FINITE_TRANSLATION_ONLY_FULL_ARITHMETIC_PROOF_PENDING',
        'annihilator_input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'families':families,'total_supported':1062,'total_uncovered':10,
        'local_auxiliary_field':'H48 p-local e268,f4; adjoiningmu_p² requiresseparateramificationargument',
        'scope':'Exact odd/reflectedcharacter dictionary andoperatorwitnesses; no class/reflection/strict/window conclusion fromthisfile alone.'}
(BASE/'quartic_residue_translation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'utc':result['utc'],'families':[{k:v for k,v in f.items() if k!='rows'} for f in families],
                  'supported':1062,'uncovered':10},indent=2))
