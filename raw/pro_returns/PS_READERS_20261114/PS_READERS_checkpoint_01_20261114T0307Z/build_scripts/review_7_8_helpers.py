"""Explicit observations supplied by the cote 134-7/134-8 visual reviewer."""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('review',ROOT/'build_scripts/review.py'); review=importlib.util.module_from_spec(spec);spec.loader.exec_module(review)
def save(key,notes,known,diffs,doubts,changes=(),extras=()):
    required={r['row_id']:r for r in review.DIFFS if r['page_key']==key and r['kind'] not in review.AUTO_KINDS}
    dm={r['id']:r for r in review.marks(review.source(key).read_text())}
    assert set(required)==set(diffs),(set(required)-set(diffs),set(diffs)-set(required))
    assert set(dm)==set(doubts),(set(dm)-set(doubts),set(doubts)-set(dm))
    dr=[]
    for id,value in diffs.items():
        if isinstance(value,str):
            image_reading=required[id]['page_reading'] or '(no corresponding text on scan)';decision='transcription confirmed';reason=value
        else: image_reading,decision,reason=value
        dr.append(dict(id=id,image_reading=image_reading,decision=decision,reason=reason))
    ur=[]
    for id,value in doubts.items():
        if isinstance(value,str): image_reading=dm[id]['reading'];decision='doubt retained';reason=value
        else: image_reading,decision,reason=value
        ur.append(dict(id=id,image_reading=image_reading,decision=decision,reason=reason))
    cs=[dict(old=a,new=b,reason=c) for a,b,c in changes]
    record=dict(key=key,viewed_halves=['a','b'],review_status='complete',notes_review=notes,known_error_review=known,diff_decisions=dr,doubt_decisions=ur,changes=cs,additional_decisions=list(extras))
    (ROOT/'review'/(key+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    review.commit(key)
