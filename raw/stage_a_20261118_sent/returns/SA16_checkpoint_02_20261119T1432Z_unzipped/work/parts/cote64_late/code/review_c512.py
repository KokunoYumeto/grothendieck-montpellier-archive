"""Incorporate the independently read early64 quadratic-gerbe proof.

This is an explicit scholarly revision after a cross-agent proof review, not an
inference from a label or search result.
"""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
claims=json.loads((B/'claims.json').read_text())
for c in claims:
    if c['id']=='C-SA16-512':
        c['statement']='Over a scheme S with 2 invertible, fix a cubic étale label scheme J and a section t of its projective branch line disjoint from J. The groupoid of elliptic double covers with these branch data is equivalent to the groupoid of lines T equipped with T⊗2≅T_(Σ_J,t), using the fixed norm convention. Locally both are μ2 twist groupoids; the deck involution acts by −1 on T. This geometric equivalence is separate from the exact symmetric μ4 pinning normalization in C-SA16-505.'
        c['class']='E'
        c['fate']='The geometric quadratic-cover/root-line equivalence follows from classical descent. The team proof in early64 §9 was read and checked: local Legendre models, matching μ2 automorphism sheaves and effective descent prove the arbitrary-J statement. The symmetric distinguished μ4 normalization remains separate. LG-PIN.'
        c['present_status']='The geometric groupoid equivalence is proved under the stated hypotheses and norm convention. It does not itself identify the coordinate scale or the distinguished symmetric pinning functor.'
        c['refs']=sorted(set(c['refs']+['SGA1']))
        c['cross_review']='Early64 proof_supplement.md §9, independently read and checked by the late64 agent on 2026-11-19; summarized in this part’s proof_notes.md §1.'
(B/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
problems=json.loads((B/'problems.json').read_text())
for p in problems:
    if p['id']=='MP-SA16-161':
        p['state_of_art']='The geometric double-cover/tangent-root groupoid equivalence is proved in the team’s early64 §9 and rechecked here by matching the local Legendre μ2 twist groupoids and their automorphism sheaves, with the norm sign fixed. AntieauMeier2020 Definition4.4, Proposition4.5 and Lemma4.7 supply the labeled atlas and twisted descent comparison; SGA1 VIII supplies descent. The exact symmetric μ4 distinguished normalization is still not identified with the ordinary Legendre rigidification of ConradLevel.'
        p['closure_status']='Geometric groupoid reconstruction proved by the team; the manuscript’s exact symmetric distinguished pinning normalization remains a comparison task, not an established modern open conjecture.'
        p['refs']=sorted(set(p['refs']+['SGA1']))
    if p['id']=='MP-SA16-172':
        p['plausible_today']='Let P=εqQ be a squarefree element of Z[T], with positive content q and primitive Q, defining a genuine quadratic field. Prove that its normalization over Z[T] is generically étale over every integer fibre exactly when q=1 and P=r²+4h. Show that the full normalized order is Z[T,u]/(u²−ru−h), u=(S+r)/2.'
(B/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
items=json.loads((B/'items.json').read_text())
for i in items:
    if i['id']=='SA16-513':
        i['reconstruction']='The torsor equivalence is proved here. The full geometric elliptic/root-line equivalence is now also proved by the team and rechecked in this run using local Legendre models and matching μ2 automorphism sheaves. The distinguished symmetric μ4 normalization is a separate comparison, not a consequence of the abstract torsor assertion alone.'
(B/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
p=B/'proof_notes.md';s=p.read_text()
needle='The example Q0 with s⁴=−4'
extra='''A further team proof now closes the geometric elliptic/root-line equivalence (C-SA16-512), separately from the symmetric pinning normalization. It was read and checked in early64 `proof_supplement.md`, §9. Send a four-branch elliptic double cover to its tangent at the distinguished ramification section, with the norm-induced square isomorphism and the explicitly fixed norm/jet sign. Étale locally order J and choose a Legendre model. The double covers with fixed branch data are then its μ2 twists; the tangent-square roots are twists by the same μ2. The nontrivial deck transformation acts as −1 on the tangent, so the induced map on automorphism sheaves is an isomorphism. Hence the functor is locally essentially surjective and fully faithful. Both sides satisfy descent, so it is an equivalence over arbitrary S and cubic étale J. This does not choose or compare the distinguished symmetric μ4 pinning scale of equations73 and83c.

'''
if extra not in s:s=s.replace(needle,extra+needle)
p.write_text(s)
p=B/'literature_notes.md';s=p.read_text().replace('Class C for seven pinning claims','Class C for six pinning claims');p.write_text(s)
p=B/'dossier_notes.md';s=p.read_text()
s=s.replace('The full equivalence with the manuscript’s elliptic objects, including its particular tangent-square identification and `Q0` twist, requires an additional comparison.',
 'The team’s early64 proof, independently read and checked here, also establishes the geometric elliptic/branch-data to tangent-square-root equivalence: locally both sides are the same μ2 twist groupoid, their automorphism sheaves match, and the equivalence descends. The particular symmetric `Q0`-twisted pinning normalization remains a separate comparison.')
s=s.replace('| Claims class E / C / F | 55 / 7 / 4 |','| Claims class E / C / F | 56 / 6 / 4 |')
s=s.replace('| Check events | 339 |','| Check events | 340 |')
p.write_text(s)
print('C-SA16-512 geometric equivalence updated C→E after reading and checking the team proof; exact symmetric normalization unchanged.')
