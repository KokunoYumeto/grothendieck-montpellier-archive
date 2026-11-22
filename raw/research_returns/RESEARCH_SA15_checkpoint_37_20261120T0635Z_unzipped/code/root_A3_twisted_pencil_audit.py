"""Record the complete auxiliary twisted-pencil proof audit; no rank inference."""
from pathlib import Path
import datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP27_twisted_pencil_lift_candidate.tex'
out=w/'outputs/root_A3_twisted_pencil_audit.json'
assert not out.exists()
snapshot=w/'notes/root_A3_twisted_pencil_audited_candidate.tex'
assert not snapshot.exists();shutil.copy2(p,snapshot)
record={'status':'FULL INDEPENDENT SYMBOLIC PROOF PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'labels':['lem:DE-A3-twisted-pencil-lift','rem:DE-A3-twisted-pencil-lift-scope'],
 'checks':[
  'Complete candidate and canonical residual-boundary kernel proof read, together with the actual DE-RB1 sheaf quotient and exact Cartier-divisor resolution. Restriction of the line-by-line extension stays exact because its quotient is locally free, and the actual quotient G|D to R remains surjective by right exactness.',
  'If the subline restriction P|D to R vanished, the quotient would factor through the second invertible line P|D and be a surjection of invertible sheaves, hence an isomorphism even on a nonreduced Cartier divisor. Degree0 versus b>0 excludes this. Thus the intrinsically defined sigma_G is nonzero, with no identification with the earlier norm section required.',
  'Applying Hom_D(-,R) gives the Yoneda obstruction gamma|D cup sigma_G, which is zero because the actual quotient extends sigma_G. Projective Gorenstein duality and P squared trivial transpose the two cup maps between AP and RP; the characteristic-two sign does not change the kernel.',
  'The hypothesis chi(AP)=0 gives equal dimensions m=h0(AP)=h0(RP). The nonzero dual kernel implies rank at mostm-1 for the original square m-by-m cup map. The exact initial cohomology sequence gives h0(AG)=m+nullity, hence at leastm+1>=2, exactly2 whenm=1, and2m in the split case.',
  'The resulting larger compulsory domain is not its image in H1(Sym squared G), and neither the residual-product intersection nor the actual Delta_s restriction is determined. No generic-rank result or main-gate movement is inferred.'
 ],
 'computation_scope':'No numerical program run for this symbolic proof audit.',
 'source_scope':'Fresh complete internal residual-boundary and boundary-kernel dependencies reread. No new external original-source read claimed.'}
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
