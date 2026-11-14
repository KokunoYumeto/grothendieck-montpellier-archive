from pathlib import Path
import sys,json,os
sys.path.insert(0,str(Path('edition/scripts').resolve()))
import audit_record
key='ega25_25_107'
p=Path('edition/review_work')/(key+'.json')
r=json.loads(p.read_text());old_end=r['end_time']
assert len(r['decisions'])==50
cp=Path('edition/checked_pages')/(key+'.tex');s=cp.read_text()
assert s.count('le S-préschéma somme')==1
assert s.count('localement libres sur S')==1
s=s.replace('le S-préschéma somme',r'le S-prés\unsure{c|b}héma somme').replace('localement libres sur S',r'localement libres \unsure{s|d}ur S')
d=[{k:v for k,v in x.items() if k!='id'} for x in r['decisions']]
def add(line,before,image,reason,change=False):
 d.append(dict(line=line,before=before,image=image,decision='Amend checked text with localized uncertainty' if change else 'Retain checked reading after focused scan follow-up',reason=reason,category='reading_change' if change else 'documentary_followup'))
add(17,'NOTES item4: des after Div exponent/argument','des, with crowded typewriter overprinting at d/e','Focused follow-up reopened both scan parts and enlarged the proposition line. The surviving d stem/bowl, e bar and terminal s support des; no separate extra letter or cancellation is securely distinguishable. Existing Div n/m and P/E/R doubts are unchanged.')
add(10,'NOTES item6: tout','tout at pour tout n and avec tout changement','The upper and lower occurrences were inspected separately at enlargement. Their t-o-u-t sequence remains readable despite the displaced overprint in the lower initial t.')
add(16,'NOTES item6: Proposition','Underlined Proposition with a crowded o region','The heading enlargement preserves the complete P-r-o-p-o-s-i-t-i-o-n sequence; the doubled impression near the final o does not establish a separate character.')
add(19,'NOTES item6: Sym','Sym in the two upper displays and lower repeated formulas','The S-y-m glyphs remain identifiable at each occurrence, including the heavy overprint of the upper second y. Existing underlines, superscripts and dual accents are retained exactly; no formula is regularized.')
add(21,'NOTES item6: canoniquement','canoniquement at the proposition and both corollary occurrences','The word was compared in the upper/lower overlap and in both lower occurrences. The repeated q and neighboring letter impressions remain crowded, but the full recorded word is readable; no additional letter is securely separate.')
add(32,'S-préschéma',r'S-prés\unsure{c|b}héma','The enlarged lower line shows a tall ascender and closed lower bowl at the c position, compatible with an overprinted b, while c remains possible beneath the merged impression. Preserve c/b locally instead of selecting the ordinary spelling.',True)
add(34,'localement libres sur S',r'localement libres \unsure{s|d}ur S','The lower-line enlargement shows a merged initial with s-like curves and a d-like upper stem/bowl. The following u and r are clear. Preserve s/d only at the overwritten initial.',True)
notes=r['visual_notes']+' Focused documentary follow-up reopened both scan parts and enlarged the NOTES4/6 ordinary words; D0051–D0057 record their individual outcomes. Two newly localized c/b and s/d uncertainties are added; the earlier complete-page inspection remains the basis of the full-review attestation.'
new=audit_record.save(key,s,d,r['lines_read'],notes)
new['end_time']=old_end
new['followups']=r.get('followups',[])+[dict(time=audit_record.now(),scope='Focused NOTES4/6 documentary follow-up only',decision_ids=[x['id'] for x in new['decisions'][50:]],prior_complete_review_end_time=old_end)]
tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n');os.replace(tmp,p)
print(key,'saved',len(new['decisions']),'decisions; prior full-review endpoint preserved')
