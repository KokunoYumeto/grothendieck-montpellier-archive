"""Curatorial corrections following reread; sanitize retrieval logs.

No note verdict is inferred by parsing. Replacements are explicit human-readable
decisions following the mathematical and source checks recorded in this run.
"""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1]
p=W/'code/make_items.py'
s=p.read_text()
changes={
'For p≠2,3 the potentially good elliptic inertia image is expected among orders2,4,6.':'For p≠2,3 the geometric special-fiber automorphism group is cyclic of order2,4,or6; inertia is a subgroup, so orders1 and3 are also possible.',
'The marginal denial has no unambiguous attachment or example. The rank':'The marginal denial has no unambiguous attachment or example. An independent p=5 counterexample is proved in proofs.md; it is not attributed to Tate. Its characters are those of finite potentially-good monodromy, equivalently ℓ-adic inertia for ℓ≠5, not literal full5-adic Tate-module inertia. The rank',
"['1000–1048;1089–1102;1152–1159']":"['1000–1048;1089–1102;1113–1119;1154–1156']",
"['1061–1064;1089–1181']":"['1061–1064;1089–1145']",
"['1159–1167']":"['1120–1124']",
"['1182–1193']":"['1147–1152']",
"['1194–1236']":"['1158–1169;1185–1214']",
"['1206–1217']":"['1173–1183']",
'Koblitz’s later asymptotic Hasse–Witt estimates are relevant and must be matched with the critical vanishing quotient.':'The exact positivity assertion is later proved in SGA7II, XXI, Theorem1.4 for projective equidimensional Cohen–Macaulay X and all sufficiently large d. Its motivic equivalence remains a separate question.',
"['1219–1233']":"['1222–1230']",
"['1234–1236;1237–1279']":"['1232–1248;1271–1277']",
"['1219–1236;1237–1279']":"['1216–1221;1250–1271']",
'The μp⊂K, potentially good elliptic test remains separate from the withdrawn general claim.':'The μp⊂K elliptic test is a separate live question on the page; this run gives an independent counterexample, not a historical attribution.',
'Automorphism/inertia orders require geometric special fiber and p≠2,3; general trace should have rank2g.':'Geometric automorphism orders are2,4,6 for p≠2,3; inertia can also have order1or3. General trace should have rank2g.',
'Absent section7 cannot certify the claimed internal result; positivity is matched separately with later Hasse–Witt estimates.':'Absent section7 cannot certify an internal proof; the exact eventual generic positivity statement appears in SGA7IIXXITheorem1.4.'
}
for a,b in changes.items():
    assert a in s,a
    s=s.replace(a,b)
p.write_text(s)
sessions=[]
for p in sorted((W/'outputs').glob('web_*.json')):
    data=json.loads(p.read_text())
    txt='\n'.join(x.get('text','') for x in data['result'].get('content',[]) if x.get('type')=='text')
    idx=[]
    for m in re.finditer(r'([^\n]+)\n【([^】]+)】([^\n]*)',txt):
        tail=m.group(3)
        idx.append({'header':m.group(1),'ref':m.group(2),'error':tail if any(x in tail.lower() for x in ['error','failed','403','forbidden']) else None})
    sessions.append({'search_id':'P894-S'+p.stem.split('_')[1],'request':data['request'],'result_index':idx})
(W/'outputs/search_sessions_001_012.json').write_text(json.dumps(sessions,ensure_ascii=False,indent=2)+'\n')
# Remove full third-party excerpts; queries, locators, titles, own summaries remain.
for p in (W/'outputs').glob('web_*.json'):p.unlink()
print('Applied',len(changes),'explicit corrections; sanitized',len(sessions),'retrieval sessions.')
