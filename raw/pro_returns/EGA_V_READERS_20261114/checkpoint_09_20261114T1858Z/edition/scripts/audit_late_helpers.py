"""Record explicitly reviewed passages; this module never supplies visual conclusions."""
from pathlib import Path
import re,csv,sys
from audit_record import begin,save,source_path
MACROS=re.compile(r'\\(unsure|illegible|hand|over|inserted|margin|deleted|xout)\b')
def group(s,i):
    while i<len(s) and s[i].isspace():i+=1
    if i<len(s) and s[i]=='[':
        i=s.index(']',i)+1
        while i<len(s) and s[i].isspace():i+=1
    if i>=len(s) or s[i]!='{': return i
    d=1;j=i+1
    while j<len(s) and d:
        if s[j]=='\\':j+=2;continue
        if s[j]=='{':d+=1
        elif s[j]=='}':d-=1
        j+=1
    return j

def complete(key, replacements, reviewed_lines, notes_reasons, extra=()):
    s=source_path(key).read_text();original=s
    decisions=[]
    for old,new,why in replacements:
        if old not in s:raise ValueError((key,'missing replacement',old))
        for match in re.finditer(re.escape(old),s):
            line=s[:match.start()].count('\n')+1
            decisions.append(dict(line=line,before=old,image=new,decision='corrected',reason=why,category='scan-reading'))
        s=s.replace(old,new)
    for m in MACROS.finditer(original):
        line=original[:m.start()].count('\n')+1
        j=group(original,m.end())
        if m.group(1)=='over':j=group(original,j)
        before=original[m.start():j]
        if line not in reviewed_lines:raise ValueError((key,'unrecorded macro line',line,before))
        desc=reviewed_lines[line]
        decisions.append(dict(line=line,before=before,image=desc,decision='reviewed',reason=desc,category=m.group(1)))
    note=next(r['notes'] for r in csv.DictReader(open('source/transcription/ega_v_cote25/NOTES.tsv'),delimiter='\t') if r['key']==key)
    items=note.split(' | ')
    if len(items)!=len(notes_reasons):raise ValueError((key,'notes count',len(items),len(notes_reasons),items))
    for i,(item,why) in enumerate(zip(items,notes_reasons),1):
        decisions.append(dict(line=f'NOTES {i}',before=item,image=why,decision='reviewed',reason=why,category='source-note'))
    decisions.extend(extra)
    lines=sum(bool(x.strip()) and not x.startswith('%') and not x.startswith('\\scanpage') for x in original.splitlines())
    return save(key,s,decisions,lines,'Both supplied image parts inspected; each nonempty content source line compared with its scan, including all margins, formulas, and handwritten material.')
