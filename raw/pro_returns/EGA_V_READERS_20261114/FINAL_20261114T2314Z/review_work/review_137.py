import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_137'
d={5:'Handwritten page number40 at upper right.',10:'The typed lesxf fragment is x-cancelled before un.',13:'Relatifs is typewritten above the line and placed after diviseurs.',23:'De façon essentielle is typewriter-cancelled; the printed desur is retained.',36:'The clipped fibr fragment at line end is cancelled.',37:'The following typewriter-cancelled phrase remains partly obscured; fibrés principaux homogènes remains a tentative reading.',41:'Handwritten archive number137 at lower left.'}
n=['Both page numbers are handwritten as transcribed.','The v in diviseurs is overtyped but legible.','Relatifs is a typed insertion after diviseurs; the overtyped item number is legible as2.','The three low x characters are typed and retained in their positions.','There is no visible hyphen after inver at the clipped right edge; none supplied.','The x-cancelled phrase remains partly obstructed and stays doubtful.','The printed desur is retained exactly.','All typed lines and margins in both images were inspected.']
x=complete(k,[],d,n);print(k,len(x['decisions']))
