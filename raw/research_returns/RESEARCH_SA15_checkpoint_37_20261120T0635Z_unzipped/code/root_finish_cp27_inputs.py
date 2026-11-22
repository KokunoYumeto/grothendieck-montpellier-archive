"""Preserve and finish the last independently audited CP27 inputs."""
from pathlib import Path
import datetime, json, re, shutil
w=Path(__file__).resolve().parents[1]
out=w/'outputs/checkpoint27_root_final_inputs'
assert not out.exists();out.mkdir()
for rel in ['code/update_current27.py','notes/checkpoint27_changes.md',
            'notes/root_references.bib','RESEARCH_SA15_references.bib']:
    shutil.copy2(w/rel,out/Path(rel).name)
p=w/'code/update_current27.py';s=p.read_text()
s=s.replace("rows=json.loads((w/'notes/item_status.json').read_text())",
"uniform=proved('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex')\n"
"b74=proved('agents/reduction_descent/B_iterated_high_quotient.tex')\n"
"rows=json.loads((w/'notes/item_status.json').read_text())")
anchor=" if row['item']=='B.4' and b72:"
assert anchor in s
s=s.replace(anchor,""" if row['item']=='A.4' and uniform:
  row['status']=('OPEN generally; every fixed f0 principal surface in all even '
                 'degrees and odd degrees divisible by3,5or7; every fixed f1 '
                 'surface in odd degrees divisible by3 and even degrees0or4mod6, plus2')
  row['where']+=('; lem:cubic-component-clean-node-product-candidate; '
                 'prop:cubic-component-weighted-graph-gluing-candidate; '
                 'thm:cubic-component-arbitrary-odd-norm-transfer-candidate; '
                 'cor:f0-odd-multiples-three-five-seven-candidate')
  row['gate']+=(' The complete uniform e-component transfer now works for every '
       'odd source degree e>=3 with known full image, through any odd polarized '
       'isogeny of multiplier n with indecomposable nonordinary source. Its '
       'e movable cubic components give18e² nodes per type and a vertex star '
       'with36(e-1) ones and18e²-36(e-1) zeros. Exact pure graph lifts and '
       'the finite-Lang extension argument give the full targetGL_(9e²n²-1). '
       'Applying the uniform source degrees3,5,7 and the incoming-neighbour '
       'theorem proves every fixed-f0 odd degree divisible by at least one '
       'of3,5,7. The least remaining fixed-f0 odd degree is11. The source '
       'degree1 case and fixed-f1degree5/even8 are not proved.')
"""+anchor)
anchor=" if row['item']=='A.3' and unipotent and boundary:"
assert anchor in s
s=s.replace(anchor,""" if row['item']=='B.4' and b74:
  row['status']=('OPEN generally; exact height-two index2 iff p<e<p³ and '
                 'exact index3 on p³<e<p⁴, with proved larger-index bounds '
                 'for p>=5, p not dividing e, mu_p in K')
  row['where']+=('; lem:B-RD74-actual-levels; prop:B-RD74-formal; '
                 'thm:B-RD74-upper; cor:B-RD74-third-index')
  row['gate']=row['gate'].replace(
       'at e128 the least index is at least3. Its exact value, the '
       'five-divisible index20, arbitrary higher indices and higher '
       'heights remain open at this stage.',
       'at e128 the least index is exactly3 by the later B74 induction. '
       'The five-divisible index20 and higher heights remain open.')
  row['gate']+=(' The full actual-quotient induction proves nu_min<=n-1 '
       'whenever e<p^n and n>=3 under the same prime-to-p height-two '
       'hypotheses. The jth quotient retains actual p^(n-j)-torsion, '
       'so high-line alignment uses a real available second level and the '
       'last comparison only p-torsion. With p^k<e<p^(k+1), e>p, '
       'floor((k+3)/2)<=nu_min<=max(2,k). In particular nu_min=3 '
       'throughout p³<e<p⁴. For p5 this settles all prime-to5 multiples '
       'of4 from128 through624. At the next permitted e628 only3<=nu<=4 '
       'is proved here. This interval is not claimed to classify every '
       'instance of index3, and no p-divisible or higher-height case is inferred.')
"""+anchor)
s=s.replace("'arbitrary_odd_neighbors':neighbors}","'arbitrary_odd_neighbors':neighbors,'uniform_cubic_transfer':uniform,'iterated_high_quotients':b74}")
p.write_text(s)
p=w/'notes/checkpoint27_changes.md';s=p.read_text()
old='The uniform larger-source norm transfer and an iterated higher-level quotient bound are separate candidates under independent audit. Neither contributes a main theorem or gate reduction until promotion. The complete four-squares source read and the norm-eleven exploratory computations remain retained, with their precise scope and any failures.'
assert old in s
s=s.replace(old,'The uniform larger-source norm transfer and iterated higher-level quotient bound completed their independent audits and were promoted before this freeze; their exact scopes and audit records are given below. The complete four-squares source read and the norm-eleven exploratory computations remain retained, with their precise scope and any failures. Later unpromoted investigations remain outside the proved outcome table.')
s+='''

## Uniform cubic-component transfer and all odd multiples of three, five, or seven

The five-assertion proof `agents/monodromy/nonordinary_cubic_component_norm_transfer.tex` was promoted at 22:48:03.970684 UTC, canonical SHA256 ce972fef0cf0d0295d2620592e14359fe5969d15ddf836c5fb36101465afe9c9. The exact final candidate SHA256 fc7cfba6ce2075e9b6fef1ce2dde893b4f40a1c53a72cb18d4e594852a8b89cf remains preserved. Root's complete symbolic proof audit passed at 22:46:04.664366 UTC; OC's independent complete audit passed at 22:47:46.739141 UTC. No new numerical computation is claimed. Records are `outputs/root_cubic_component_transfer_audit.json`, `agents/obstructions_crystals/cubic_component_norm_transfer_independent_audit.json`, and `agents/monodromy/outputs/cubic_component_norm_transfer_promotion.json`.

For every odd source degree e >= 3 whose full monodromy is already known, the proof transfers through an arbitrary odd polarized isogeny with indecomposable nonordinary source. It uses e general cubic components, all Picard twists included. The graph has 9ke²−9e edges, where k is the order of the odd translation kernel; the extra-node module has dimension 9e²(k−1), with 18e² labels per type. A selected eighteen-label tangency supplies an exact pure graph pair. The resulting vertex star has 36(e−1) ones and 18e²−36(e−1) zeros in every type. The common-kernel and translation-heart arguments, Goursat separation, Lang extension over the full normal base, and normal-transvection dimension inequality are proved uniformly. The special stable rank drop (e−1)(2−f) is retained explicitly.

The full target group is GL_(9e²n²−1), where n is the polarized multiplier. Combining the previously uniform source degrees 3, 5, and 7 with the incoming-neighbour theorem proves every odd degree divisible by at least one of 3, 5, or 7 on every fixed p-rank-zero principal surface. Together with the earlier even result, only the other odd degrees remain in that case; the smallest is 11. The e=1 source case is not asserted. For p-rank one the known uniform source e=3 gives the already stated odd multiples of three; degrees 5 and 8 remain open.

## Actual quotient induction and the exact third-index interval

The five-assertion proof `agents/reduction_descent/B_iterated_high_quotient.tex` was promoted at 22:50:15.749863 UTC, canonical SHA256 16ab6c8fcc024402a4e38f09f57976d4948b19e48f66f13a49501159e4639502. Its final candidate SHA256 30538d9b2588452cd20be474b5e9860994d37b91ba7cf257b8a2b389dfa32990 remains preserved. Root's full proof/code audit passed at 22:46:56.468649 UTC with an isolated unchanged-program runtime of 0.8197192030056613 s. OC's complete independent proof/code audit passed at 22:48:42.726134 UTC with runtime 0.8659103850077372 s. Both author-preserving reruns reproduce every mathematical output field. Records are `outputs/root_B74_audit.json`, `agents/obstructions_crystals/B74_independent_audit.json`, and `agents/reduction_descent/outputs/B74_promotion.json`.

In the same full height-two, perfect-residue, p >= 5, μp subset K, p not dividing e setting, actual p^n-torsion determines the required character whenever e < p^n and n >= 3. Thus the manuscript least index satisfies νmin <= n−1. After j high-subgroup quotients the proof retains actual p^(n−j)-torsion, with the total rank-p^j kernel killed by p^j. Every alignment is performed while a second torsion level is available; the terminal comparison uses only the remaining first level. A mixed crossing is excluded by tame/wild opposition, both large parameters are recovered from first-level breaks, and an entirely small sequence ends with parameters between 1 and p−1, where the common norm character is injective. The existing mixed filtered threshold is incompatible with this range.

Together with the actual lower examples, this gives floor((k+3)/2) <= νmin <= max(2,k) when p^k < e < p^(k+1) and e > p. In particular **νmin = 3 throughout p³ < e < p⁴**. For p=5 all prime-to-five multiples of four from 128 through 624 are now determined. The next permitted e=628 is bounded only by 3 <= νmin <= 4 here. The theorem does not claim that its interval exhausts all instances of index three; ramification divisible by p and higher heights remain open.

The author's final exact supplement ran at 22:44:19.389842 UTC in 0.863016332994448 s. It checks four actual module quotients, 20,400 subgroup points and 81,600 induced matrix-point identities; 196 complete sectors with 88,870 parameter pairs; and 406 explicitly sampled deeper sectors with 161,887 pairs. It retains 683,813 aligned stages, 433,056 marked stages and 16,832 final-first-level stops, plus 11,880 character-orbit checks and 100 complete sectors in the exact third-index interval. The earlier successful version and output are preserved; its division inequality was replaced by exact integer cross-multiplication without changing the counts. No failed run is invented and no existence theorem is inferred from the finite enumeration.
'''
p.write_text(s)
root=w/'notes/root_references.bib';rb=root.read_text()
aggregate=(w/'RESEARCH_SA15_references.bib').read_text()
def entry(text,key):
    start=re.search(r'(?m)^@[^\n{]+\{'+re.escape(key)+',',text)
    assert start,key
    nxt=re.search(r'(?m)^@',text[start.end():])
    return text[start.start():start.end()+nxt.start() if nxt else len(text)].strip()
for key in ['Tian2009HWCyclic']:
    rb=rb.replace(entry(rb,key),entry(aggregate,key))
assert 'HardyWright1960FourSquares' not in rb
rb+='\n\n'+entry(aggregate,'HardyWright1960FourSquares')+'\n'
assert 'Hattori2008TameCharacters' not in rb
rb+='\n'+(w/'agents/reduction_descent/B73_literature_references.bib').read_text()
old=entry(rb,'Hoshi2009TameBlind')
new=old.replace('no universal improvement is asserted.',
 'no universal improvement is asserted. During the targeted B73 search, reduction_descent freshly read the introduction pp23--28, Theorem0.1, Corollary0.2 and the epsilon_Fon definition, and the full Corollary3.5 statement and one-line proof pp50--51. This limited fresh reread does not claim a new full audit of Theorem3.4; no theorem is imported into B73.')
assert new!=old;rb=rb.replace(old,new);root.write_text(rb)
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'prior_inputs':str(out.relative_to(w)),
        'updates':['B74 and uniform cubic transfer canonical gates',
                   'full promotion and audit scopes in checkpoint27 changes',
                   'persist Hardy/Wright and Tian actual reads in consolidation source',
                   'merge two Hattori comparison entries and Hoshi limited fresh read']}
(out/'record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
