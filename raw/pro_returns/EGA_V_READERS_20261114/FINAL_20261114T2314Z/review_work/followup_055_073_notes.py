from pathlib import Path
import csv, json, os, sys
sys.path.insert(0, str(Path('edition/scripts').resolve()))
import audit_record

updates = {
    'ega25_25_055': dict(
        expected=67, line=27,
        before=r'NOTES item6: handwritten dual accent above P in P(n)',
        image=r'\overset{\hand{$\vee$}}{P}(n)',
        reason='Focused inspection of the lower original scan shows a small pen vee immediately above the typed P, before the separately typed parenthesized n. Its descending left stroke and rising right stroke are visible. Retain the existing accent placement. This local record supersedes the unrelated target-capital wording repeated in D0039; it makes no change to the distinct P/R/X doubt on line17.',
        scope='Focused NOTES6 check of the P(n) dual accent in the lower scan only',
        concern=6, ids=[11,68,17,19,23],
        mapping='D0011 records the pen accent above the doubtful target capital; D0068 precisely records the separate pen vee above P in P(n), superseding the unrelated rationale repeated in D0039. D0017/D0019/D0023 preserve the hooked point-symbol xi/zeta uncertainty in its three occurrences.'),
    'ega25_25_073': dict(
        expected=26, line=13,
        before='NOTES item9: clipped les at the right edge of the Grass-arrow line',
        image='les, with the rightward extent of the terminal s cut by the scan edge',
        reason='Focused inspection of the upper original scan shows a full l and e after the comma following V-double-prime. The surviving upper and lower curved portions of the final glyph support s, while its extreme right edge is clipped. Retain the already encoded les; no additional ending or subsequent word is supplied. This explicitly documents the fifth edge word omitted from the enumeration in D0026.',
        scope='Focused NOTES9 check of the right-edge les in the upper scan only',
        concern=9, ids=[26,27],
        mapping='D0026 explicitly records the clipped utilisant/dans/des/une group. The focused D0027 separately records the visible l/e and surviving s curves of les at the Grass-arrow line edge, retaining the existing word without supplying anything beyond the clipped glyph.')
}

crosswalk = Path('edition/records/NOTES_CROSSWALK_middle.tsv')
rows = list(csv.DictReader(crosswalk.open(), delimiter='\t'))
replay_path = Path('edition/review_work/middle_notes_crosswalk.py')
replay = replay_path.read_text()
old_entries = {
 'ega25_25_055': "(6,[11,39,17,19,23],'The decisions record the pen dual accents and the three hooked point-symbol occurrences, retaining xi/zeta uncertainty. D0039 is attached to the P(n) accent line but repeats the other target-capital rationale; only its local hand-accent identification is used here, not that unrelated capital discussion.'),",
 'ega25_25_073': "(9,[26,12,13],'D0026 explicitly records the clipped utilisant/dans/des/une group and its unchanged visible portions. The concern’s additional les is on the already checked Grass-arrow line13, documented by D0012–D0013 and the complete-page reading record; it is not separately named in the edge-word list.'),"
}

for key, u in updates.items():
    p = Path('edition/review_work') / (key + '.json')
    r = json.loads(p.read_text())
    assert len(r['decisions']) == u['expected'], key
    assert old_entries[key] in replay, key
    decisions = [{k:v for k,v in d.items() if k!='id'} for d in r['decisions']]
    decisions.append(dict(line=u['line'], before=u['before'], image=u['image'],
                          decision='Retain checked reading after focused scan follow-up',
                          reason=u['reason'], category='documentary_followup'))
    checked = (Path('edition/checked_pages') / (key + '.tex')).read_text()
    old_end = r['end_time']
    notes = r['visual_notes'] + ' ' + u['scope'] + '; the new decision closes the documentary enumeration gap without changing the checked text. The original complete-page inspection remains the basis of the full-review attestation.'
    new = audit_record.save(key, checked, decisions, r['lines_read'], notes)
    new['end_time'] = old_end
    new['followups'] = r.get('followups',[]) + [dict(time=audit_record.now(), scope=u['scope'], decision_ids=[new['decisions'][-1]['id']], prior_complete_review_end_time=old_end)]
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
    os.replace(tmp,p)
    cid = f"{key}-N{u['concern']:03}"
    matches = [row for row in rows if row['concern_id']==cid]
    assert len(matches)==1
    matches[0]['decision_ids'] = ' '.join(f'{key}-D{d:04}' for d in u['ids'])
    matches[0]['reason'] = u['mapping']
    new_entry = f"({u['concern']},{u['ids']!r},{u['mapping']!r}),"
    replay = replay.replace(old_entries[key],new_entry)
    print(key, new['decisions'][-1]['id'], 'saved; checked text unchanged')

tmp = crosswalk.with_suffix('.tmp')
with tmp.open('w') as f:
    w=csv.DictWriter(f,fieldnames=['concern_id','decision_ids','reason'],delimiter='\t')
    w.writeheader(); w.writerows(rows)
os.replace(tmp,crosswalk)
tmp = replay_path.with_suffix('.tmp')
tmp.write_text(replay)
os.replace(tmp,replay_path)
