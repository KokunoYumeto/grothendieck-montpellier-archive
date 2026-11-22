"""Record an actual complete proof audit; this is not a mathematical computation."""
from pathlib import Path
import hashlib,json,datetime,csv,shutil
w=Path(__file__).resolve().parents[1]
source=w/'agents/obstructions_crystals/post_CP28_product_Frobenius_interpolation_obstruction_candidate.tex'
dest=w/'outputs/root_product_Frobenius_interpolation_audit.json'
assert not dest.exists()
snapshot=w/'notes/root_product_Frobenius_interpolation_audited_candidate.tex'
assert not snapshot.exists();shutil.copy2(source,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r={'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'source':str(source.relative_to(w)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'labels':['lem:DE-A4-product-Frobenius-interpolation','rem:DE-A4-product-Frobenius-interpolation-scope'],
 'checks':[
 'Relative Frobenius on a smooth elliptic curve has length-two geometric fibre 2p; finite flat base change and the product decomposition give precisely the typed rank-two and rank-four fibre evaluations.',
 'The degree-one and degree-three line-bundle cohomology assertions follow from Serre duality and Riemann--Roch. Each factor evaluation is onto with one-dimensional kernel.',
 'Two distinct Frobenius fibres cannot have the same kernel line: its nonzero section would vanish on a degree-four divisor despite the line bundle having degree three.',
 'Two dual two-planes in dimension three therefore meet in a line. Adapted-basis tensor intersections give total ranks seven when both coordinates differ and six when exactly one agrees.',
 'The proposed critical two-point surjectivity condition is false in this actual geometric example. The induced form from two point evaluations factors through a space of dimension at most seven, so alternation forces rank at most six.',
 'This does not refute maximal generic rank for arbitrary functionals, or establish any mixed-surface or general A.4 rank formula.'
 ],
 'scope':'Entire lemma and scope remark read and checked. No numerical program, finite extrapolation, fresh original-source theorem or main-gate advance is asserted.'}
dest.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in r['labels']:
  writer.writerow([label,now,r['reviewer'],'targeted proof check','PASS: complete restriction-sequence, tensor-intersection and alternating-rank proof audit; exact scope outputs/root_product_Frobenius_interpolation_audit.json.'])
print(json.dumps(r,indent=2))
