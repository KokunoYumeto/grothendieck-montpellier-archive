import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_138'
r=[(r'\unsure{sur un}','sur un','The short cancelled phrase sur un is legible beneath the x strokes.'),(r'\margin{138}',r'\mspage{\hand{138}}','The lower pencil number138 is the archive foliation.')]
d={5:'The upper page number41 is handwritten.',8:'The replacement phrase is typed above the cancelled original. Most of the original can be followed but the heavy x strokes warrant retaining its existing doubt.',9:'The short cancelled sur un is legible and its doubt is removed.',12:'The lower number138 is pencil foliation.'}
n=['The long cancelled phrase retains doubt; the shorter sur un is legible. The replacement is typed above the line.','Both page numbers are handwritten; the lower one is now marked as foliation.','The remainder of both image parts is blank apart from paper texture and small non-textual specks.','The four text lines, their insertions and cancellations, and both image parts were inspected.']
x=complete(k,r,d,n);print(k,len(x['decisions']))
