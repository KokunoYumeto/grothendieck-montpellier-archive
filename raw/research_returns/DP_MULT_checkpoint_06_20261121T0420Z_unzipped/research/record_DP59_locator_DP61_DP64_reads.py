#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
r=Path(__file__).resolve().parent; now=datetime.now(timezone.utc).isoformat()
repls=[('`IsTwistPull`,76–84','`IsTwistPull`,73–81'),('`IsActOf`,86–87','`IsActOf`,83–84'),('\\texttt{IsTwistPull},76--84','\\texttt{IsTwistPull},73--81'),('\\texttt{IsActOf},86--87','\\texttt{IsActOf},83--84')]
changes=[]
for p in [r/'theta_translate_span_DP59.md',r/'DP59_integrated_fragment.tex',r.parent/'DP_MULT.tex']:
 before=p.read_text();after=before
 for old,new in repls:after=after.replace(old,new)
 assert after!=before,p
 p.write_text(after)
 changes.append({'path':str(p.relative_to(r.parent)),'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest()})
d={'recorded_utc':now,'statement':'DP59','who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','scope':'Archive reviewer caught two imprecise declaration line ranges after the earlier pass. Root directly read numbered original ThetaPt.lean36-92, confirming SymLift44-51, IsTwistPull73-81, IsActOf83-84 and IsGenSec86-87. Replaced only the two mistaken locator ranges in memo, intended fragment and main. The mathematical proof is unchanged.','outcome':'PASS corrected exact locators; previous review hashes are retained as historical events, not rewritten.','changes':changes}
(r/'DP59_locator_correction_metadata.json').write_text(json.dumps(d,indent=2)+'\n')
for n,fn,scope in [
 (61,'selected_row_degree_gate_DP61.md','Read COMPLETE saved memo sections1-7, all statements and all proofs. Checked P/Q/nV indexing, reversed negative partition, every positivity/dominance subtraction, exact first-row exclusion scope, all contraction and row-addition cases for disjoint determinant completion, coefficient-one primitivity, axes-zero column factorization, and each finite-window inequality. Source theorems are accepted with the exact independently read source ranges recorded by the author and reviewer; no source execution is claimed.'),
 (64,'cyclotomic_type_prime_budget_DP64.md','Read COMPLETE saved memo sections1-7 and challenged all new arguments. Checked restriction-fibre and embedding cardinalities, uniformity over types and fields in a fixed cyclotomic field, exact first-order coefficient mean, summable tails, full floor rounding and saturation at n, n=0/1 boundary cases, entropy bound for unequal order distributions, finite mod7 adaptive-selector table, and every geometric/source/variable-conductor limitation. Reopened and read Rudnick primary printed p2 equation1 and preceding fixed-modulus statement before this proof read.')]:
  p=r/fn
  d={'statement':f'DP{n}','recorded_utc':now,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','scope':scope,'outcome':'PASS complete saved proof; mathematical reading, not machine formalization.','file':fn,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  (r/f'DP{n}_root_whole_review_metadata.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'recorded_utc':now,'reads':[61,64],'locator_corrected':59,'changes':changes}))
