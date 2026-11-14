import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_135'
r=[(r'\mspage{38}',r'\mspage{\hand{38}}','The upper folio number is handwritten.'),(r'\mspage{135}',r'\mspage{\hand{135}}','The lower archive number is handwritten.'),(r'\hand{\unsure{?}} ','','There is no distinct front-side question-mark glyph before the comparison sign; the crossing stroke belongs to the cancellation of the paragraph.')]
d={13:'One long diagonal hand stroke cancels the whole paragraph from Pour par.20 through revient !.',14:'Both typewriter-cancelled fragments remain uncertain; both lambda subscripts are handwritten.',15:'The comparison sign is handwritten. A separate question mark is unsupported by the visible front-side ink and has been removed.',19:'The final lambda is handwritten inside the cancelled paragraph.',22:'The signature A Grothendieck is handwritten and legible.'}
n=['The whole paragraph is crossed by the long diagonal pen stroke and stays deleted.','Both cancelled fragments remain uncertain.','All three lambdas are handwritten.','The handwritten comparison sign remains; the additional alleged question mark is not separately visible in the front-side ink.','Both page numbers are now marked as handwriting.','The reverse-side text in the lower half is show-through and is not repeated.','The entire front-side letter and all marks were read in both supplied images.']
x=complete(k,r,d,n);print(k,len(x['decisions']))
