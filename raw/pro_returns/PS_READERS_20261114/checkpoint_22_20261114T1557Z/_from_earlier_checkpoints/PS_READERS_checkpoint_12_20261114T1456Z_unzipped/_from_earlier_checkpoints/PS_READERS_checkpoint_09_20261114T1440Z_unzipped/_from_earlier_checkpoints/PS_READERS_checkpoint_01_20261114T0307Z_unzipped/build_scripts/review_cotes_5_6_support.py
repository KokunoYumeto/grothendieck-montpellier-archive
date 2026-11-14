"""Serialize manually supplied scan decisions for the 134-5/134-6 review."""
import json
import review

def record(key,notes,known,diff_findings,doubt_findings,edits=(),extra=()):
    required=[r for r in review.DIFFS if r['page_key']==key and r['kind'] not in review.AUTO_KINDS]
    doubts=review.marks(review.source(key).read_text())
    assert len(diff_findings)==len(required),(key,len(diff_findings),len(required))
    assert len(doubt_findings)==len(doubts),(key,len(doubt_findings),len(doubts))
    d=[]
    for row,f in zip(required,diff_findings):
        if isinstance(f,str): image=row['page_reading']; decision='the typescript reads as our transcription';reason=f
        else: image,decision,reason=f
        d.append({'id':row['row_id'],'image_reading':image,'decision':decision,'reason':reason})
    u=[]
    for row,f in zip(doubts,doubt_findings):
        if isinstance(f,str): image=row['reading'];decision='retained';reason=f
        else: image,decision,reason=f
        u.append({'id':row['id'],'image_reading':image,'decision':decision,'reason':reason})
    r={'key':key,'viewed_halves':['a','b'],'review_status':'complete','notes_review':notes,'known_error_review':known,'diff_decisions':d,'doubt_decisions':u,'changes':[{'old':a,'new':b,'reason':c} for a,b,c in edits],'additional_decisions':list(extra)}
    (review.ROOT/'review'/(key+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    review.commit(key)
