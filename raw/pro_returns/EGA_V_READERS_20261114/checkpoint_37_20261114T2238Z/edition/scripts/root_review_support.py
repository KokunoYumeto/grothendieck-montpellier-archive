"""Record helpers used only after an actual complete visual comparison."""
import re

def decision(line,before,image,outcome,reason,category='visual'):
 return dict(line=str(line),before=before,image=image,decision=outcome,reason=reason,category=category)

def macros(text):
 pattern=re.compile(r'\\(hand|over|inserted|margin|deleted|xout|uline|uuline|unsure|illegible)\b')
 for m in pattern.finditer(text):
  pos=m.end(); narg=2 if m[1]=='over' else 1
  if pos<len(text) and text[pos]=='[':
   q=text.find(']',pos);pos=q+1
  ok=True
  for _ in range(narg):
   while pos<len(text) and text[pos].isspace():pos+=1
   if pos>=len(text) or text[pos]!='{':ok=False;break
   depth=1;pos+=1
   while pos<len(text) and depth:
    if text[pos]=='\\' and pos+1<len(text) and text[pos+1] in '{}%':pos+=2;continue
    if text[pos]=='{':depth+=1
    elif text[pos]=='}':depth-=1
    pos+=1
  if ok:yield (m.start(),pos,m[1],text[m.start():pos],text.count('\n',0,m.start())+1)

def retained_mark_decisions(text, changed_ranges=()):
 """No check is performed here: the caller must have read all these occurrences."""
 rows=[]
 for start,end,kind,raw,line in macros(text):
  if any(start<b and end>a for a,b in changed_ranges):continue
  doubt=kind in ('unsure','illegible') or '\\unsure' in raw or '\\illegible' in raw
  if kind=='unsure': outcome='doubt-retained';reason='The visible traces do not securely choose among the recorded reading(s); uncertainty retained after inspection.'
  elif kind=='illegible':outcome='unresolved';reason='The underlying word or character remains unreadable in the supplied images; no conjectural restoration made.'
  elif doubt:outcome='layer-confirmed;reading-unresolved';reason='The indicated physical layer or cancellation is visible; the nested doubtful or illegible reading remains unresolved.'
  else:outcome='confirmed';reason='This exact occurrence, its lettering, and its indicated physical layer were compared with the page image and retained.'
  rows.append(decision(line,raw,raw,outcome,reason,kind))
 return rows

class ReviewedPage:
 def __init__(self,text):self.original=text;self.text=text;self.decisions=[];self.changed_lines=set();self.changed_ranges=[];self.replacements=[]
 def change(self,before,after,reason,outcome='corrected-reading',count=None):
  occurrences=list(re.finditer(re.escape(before),self.text))
  if not occurrences:raise ValueError('Missing: '+before)
  if count is not None and len(occurrences)!=count:raise ValueError((before,len(occurrences),count))
  original_occ=list(re.finditer(re.escape(before),self.original))
  if not original_occ:
   mapped=before
   for old,new in reversed(self.replacements):mapped=mapped.replace(new,old)
   original_occ=list(re.finditer(re.escape(mapped),self.original))
  for m in original_occ:
   line=self.original.count('\n',0,m.start())+1
   self.changed_lines.add(line)
   self.changed_ranges.append((m.start(),m.end()))
   self.decisions.append(decision(line,before,after,outcome,reason,'reading-change'))
  if not original_occ:
   self.decisions.append(decision('revised passage',before,after,outcome,reason,'reading-change'))
  self.text=self.text.replace(before,after)
  self.replacements.append((before,after))
 def note(self,line,before,image,outcome,reason,category='NOTES'):
  self.decisions.append(decision(line,before,image,outcome,reason,category))
 def finish(self):
  # Mark confirmations for unchanged original lines only; transformed lines have explicit decisions.
  self.decisions+=retained_mark_decisions(self.original,self.changed_ranges)
  return self.text,self.decisions
