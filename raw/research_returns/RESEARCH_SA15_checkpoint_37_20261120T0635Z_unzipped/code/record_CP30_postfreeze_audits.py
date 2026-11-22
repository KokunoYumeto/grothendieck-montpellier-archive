"""Record actual post-freeze audits without editing the frozen CP30 paper."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/CP30_postfreeze_audits_report_record.json'
assert not dest.exists()
root85=json.loads((w/'outputs/root_B85_audit.json').read_text())
root86=json.loads((w/'outputs/root_B86_audit.json').read_text())
oc85=json.loads((w/'agents/obstructions_crystals/B85_independent_audit.json').read_text())
oc86=json.loads((w/'agents/obstructions_crystals/B86_independent_audit.json').read_text())
for r in [root85,root86,oc85,oc86]:assert 'PASS' in r.get('status',r.get('result',''))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
paragraph='''
### Actual audits completed after the checkpoint30 paper freeze

The complete B85 and B86 candidates remain separate from the frozen numbered paper. Both now have full root and companion proof/code audits. B85 uses an actual degree-p second-level point field to exclude either vanishing first-layer diagonal projection. Its inverse valuations are prime to p; the same lower break would obey two incompatible equalities, with positive gap (p+1)(p²+1). For p congruent to1 modulo4 this gives at least six wild matrix dimensions in the tame reducible sector. B86 excludes the remaining pair of three-dimensional traceless layers: the nonzero last cyclotomic character factors through the genuine degree-p² point field, whose every lift has lower break strictly below the cyclotomic quotient's actual break N². The exact norm-polynomial quotient formula then contradicts that break. Combined, the two audited candidates give at least seven wild matrix dimensions only in the tame reducible sector. Atp5,e20, only wild orders5^7 and5^8 could remain in that sector, with the already proved necessary parameter pair{25,75}; no such example is constructed, and other residual sectors are unchanged. No promotion or canonical paper edit occurred before checkpoint30.

B85 author/root/companion exact run times were0.3171308919991134,0.3250291720032692 and0.315905258001294 seconds. B86 times were0.4382091660081642,0.4253982070076745 and0.4311180119984783 seconds. Each unchanged isolated rerun agrees in all mathematical fields with its preserved author output; no execution failed. Complete root source snapshots, programs, stdout/stderr, hashes, inputs, counts and proof audits are retained in outputs/root_B85_audit.json and outputs/root_B86_audit.json and the paths they name. The companion records are agents/obstructions_crystals/B85_independent_audit.json and B86_independent_audit.json. Root and companion freshly opened the specified original Cohen structure theorem and Colmez tame-uniformizer and quotient-ramification proofs, with exact source scopes recorded; those reads are also listed in notes/ROOT_SEARCH_LOG_30.md.

The separate root theta-torsion avoidance candidate also passed both complete independent written-proof audits: agents/monodromy/outputs/independent_theta_torsion_avoidance_audit.json and agents/obstructions_crystals/root_theta_torsion_avoidance_independent_audit.json. It remains auxiliary. Its Cartier coefficient identification, the direction needed for a fixed target surface, and any triple-free theta-image assertion are still unproved. The norm17 search produced exact triple- or five-point packets for two more selected maps on the remaining exceptional model, so neither map proves the uniform17 case. The separate Moore one-zero-chart calculation classifies precisely that chart; it neither classifies all singular matrices nor identifies the actual Cartier parameter. All such exploratory code and output are retained without promoting their stronger targets.
'''
for path in [w/'notes/checkpoint30_changes.md',w/'RESEARCH_SA15_report.md']:
 s=path.read_text()
 s=s.replace('Cartesian/Cartier coefficient bridge','Cartier coefficient bridge')
 path.write_text(s+paragraph)
record={'status':'RECORDED_WITHOUT_CANONICAL_PROMOTION','actual_utc':now,
 'audits':['outputs/root_B85_audit.json','outputs/root_B86_audit.json','agents/obstructions_crystals/B85_independent_audit.json','agents/obstructions_crystals/B86_independent_audit.json'],
 'scope':'Report-only post-freeze record; frozen paper and bibliography unchanged; candidate audit facts are not silently turned into numbered statements.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
