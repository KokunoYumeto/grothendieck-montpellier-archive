from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_046';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\mspage{42}',r'\mspage{\hand{42}}','The upper foliation42 is handwritten.','corrected-layer')
p.change(r'\mspage{46}',r'\margin{\hand{46}}','The lower-left46 is pencil archive foliation, separate from the manuscript number42.','corrected-layer')
for word in ['mais','des exemples','et en','cela implique','que des points','gé','faisceau']:
 p.change('\\unsure{'+word+'}',word,'The typewriter-cancelled letters of this occurrence are legible on enlargement.','doubt-resolved')
p.change(r'\in X(k)',r'\hand{\in} X(k)','Both membership signs are penned.','corrected-layer')
p.change(r'\geqslant',r'\hand{\geqslant}','Each greater-than-or-equal sign is handwritten.','corrected-layer')
p.change(r'\unsure{4}',r'\unsure{4|5}','The degree digit contains overlapping4/5-like strokes; the earlier layer is not securely distinguishable.','doubt-refined')
p.change(r'\unsure{X}',r'X','The handwritten note has a clear capital crossing X after the equals sign.','doubt-resolved')
p.change(r'8.\over{\unsure{10}}{11}',r'8.\over{\unsure{9|10}}{11}','The older numeral has a closed loop and descending9-like trace beneath the final strokes;9 is an additional supported older reading.','doubt-refined')
p.change("l'assertion a) signifie", "l'assertion a) siggifie",'The second g has a clear lower loop: the typescript reads siggifie. The normalized source word is corrected back to the image.','corrected-reading')
p.change(r'sertion b) signifie',r'sertion b) sig\unsure{g|n}ifie','The second middle letter is overprinted and retains both g-like and n-like outlines.','corrected-reading;doubt-added')
p.change(r"l\xout{\unsure{'annulation}}",r"l\unsure{'a|a}\xout{nnulation}",'The initial a lies outside the dense crosses; a faint apostrophe-like stroke above it remains unresolved. The cancelled nnulation is legible. This preserves the physical prefix without choosing a grammatical repair.','corrected-reading;doubt-refined')
p.change(r'\underline{\hand{\omega}}^{\otimes 2}_{X/\hand{k}}',r'\hand{\underline{\omega}}^{\otimes 2}_{X\hand{/}k}','Omega, its underline, and the long slash are penned; the k is a typed serif k. The tensor glyphs retain their typed layer.','corrected-layer')
p.note('12-25','overwritten references','overwritten references','doubt-retained','The final8,11 and12 readings are visible. The small older typed7 readings remain doubtful under the pen; they are not inferred from numbering continuity.')
p.note('10','full handwritten NB','full handwritten NB','confirmed','The entire interlinear note was read, including abbreviated pts, X, the quotation marks and the handwritten line-break hyphen in tangen-tes.')
p.note('18','sauf insertion','sauf insertion','confirmed','The entire sauf Y sing equals Y sup sing clause is penned and placed by a bracket before signifie.')
p.note('32-39','remark and formula','remark and formula','confirmed','Every word and symbol was compared, including the repeated géométriquement, source spaces s euls and f ait, handwritten essentiellement, exponent tensor2, Y^1, and typed tensor product.','full-line-check')
p.note('7-39','remaining complete lines','remaining complete lines','confirmed','Both halves were read through the final exceptionnelle. The additional typed en x after tangent, non si/singulière, two dots after8.12, and all characteristic-zero qualifications are preserved.','full-line-check')
s,d=p.finish()
ar.save(k,s,d,0,'Both full halves inspected; all cancelled words, degree overprint, handwritten NB, reference digits, two siggifie occurrences and full invertible-module formula enlarged.')
print('Saved46;',ar.aggregate(),'pages checked.')
