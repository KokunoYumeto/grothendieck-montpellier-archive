"""Record manually supplied decisions for the late Blass page range."""
from pathlib import Path
import csv, re
from audit_record import begin, save, source_path
from audit_late_helpers import MACROS, group

def complete(key, replacements, reviewed_lines, notes_reasons, extra=(), visual_notes=None):
    original=source_path(key).read_text()
    s=original
    decisions=[]
    for old,new,why in replacements:
        if old not in s:
            raise ValueError((key,'missing replacement',old))
        for match in re.finditer(re.escape(old),s):
            line=s[:match.start()].count('\n')+1
            decisions.append(dict(line=line,before=old,image=new,decision='corrected',reason=why,category='scan-reading'))
        s=s.replace(old,new)
    for m in MACROS.finditer(original):
        line=original[:m.start()].count('\n')+1
        j=group(original,m.end())
        if m.group(1)=='over':
            j=group(original,j)
        before=original[m.start():j]
        if line not in reviewed_lines:
            raise ValueError((key,'unrecorded macro line',line,before))
        desc=reviewed_lines[line]
        decisions.append(dict(line=line,before=before,image=desc,decision='reviewed',reason=desc,category=m.group(1)))
    with open('source/transcription/ega_v_cote24_blass/NOTES.tsv') as f:
        note=next(r['notes'] for r in csv.DictReader(f,delimiter='\t') if r['key']==key)
    items=note.split(' | ')
    if len(items)!=len(notes_reasons):
        raise ValueError((key,'notes count',len(items),len(notes_reasons),items))
    for i,(item,why) in enumerate(zip(items,notes_reasons),1):
        decisions.append(dict(line=f'NOTES {i}',before=item,image=why,decision='reviewed',reason=why,category='source-note'))
    decisions.extend(extra)
    s=s.replace('not yet checked by eye.','checked against both supplied scan parts; see CHECK_DECISIONS.tsv.')
    if visual_notes is None:
        raise ValueError('Supply the page-specific description of the completed visual reading.')
    return save(key,s,decisions,0,visual_notes)
