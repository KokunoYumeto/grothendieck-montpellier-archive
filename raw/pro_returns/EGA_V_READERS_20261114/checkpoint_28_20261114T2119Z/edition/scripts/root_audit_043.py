from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_043';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\mspage{\unsure{39}}',r'\mspage{\hand{39}}','The final handwritten second digit has a closed upper loop and a long descending9 stroke.','doubt-resolved;corrected-layer')
p.change(r'\longrightarrow',r'\hand{\longrightarrow}','The opening morphism arrow is penned.','corrected-layer')
p.change('\\deleted{non\nramifié}', '\\deleted{gon\nramifié}','The enlarged first letter of the second cancelled occurrence is a typed g with a descending loop. The source spelling gon is retained.','corrected-reading')
old=r'\margin{NB. L\'hyp. \unsure{(on fera ici en} \illegible{1} \unsure{lien de : non normalité)} ne sert que pour l\'équivalence avec (i ter). Énoncer 8.8. en conséquence\dots}'
# Use double quotes for apostrophes in the literal source.
old="\\margin{NB. L'hyp. \\unsure{(on fera ici en} \\illegible{1} \\unsure{lien de : non normalité)} ne sert que pour l'équivalence avec (i ter). Énoncer 8.8. en conséquence\\dots}"
new="\\margin{NB. L'hyp. f une \\uline{imm.} (au lieu de : non ramifié) ne sert que pour l'équivalence avec (i ter). Énoncer 8.8. en conséquence\\dots}"
p.change(old,new,'The rotated full note reads f une imm. (au lieu de: non ramifié). The abbreviation imm. is underlined and not expanded. An independent visual review confirmed these words.','doubt-resolved;recovered-margin')
p.change('(i ter) Le morphisme',r'(i ter) Le m\unsure{oo|or}phisme','The middle type positions show competing oo/or outlines; the apparent moophisme is retained beside morphisme.','doubt-added')
p.change(r'\inserted{H}',r'\inserted[typed]{H}','The inserted H has the typewriter serif form; its bracket is penned.','corrected-layer')
p.change(r'$x \in X(\bar{k})$',r'$x \hand{\in} X(\bar{k})$','The membership sign is handwritten.','corrected-layer')
p.change(r'\unsure{ou}',r'ou','The enlarged end of the handwritten insertion reads ou.','doubt-resolved')
p.change(r'\unsure{dodimension|codimension}',r'dodimension','The first two letters are clearly d and o; the original spelling is retained.','doubt-resolved')
p.change(r'\geqslant 2',r'\hand{\geqslant} 2','The inequality is penned.','corrected-layer')
p.change(r'\overset{\vee}{P}',r'\overset{\hand{\vee}}{P}','The last check over P is penned.','corrected-layer')
p.change(r'8.\unsure{7}.',r'8.\over{\unsure{5|6}}{7}.','The final handwritten7 is clear; an older rounded typed numeral beneath it remains5/6 doubtful.','doubt-refined;corrected-layer')
p.change(r'\unsure{iii}',r'\unsure{ii|iii}','The compact overprinted group has i-like stems sharing a baseline and dots; both ii and iii remain possible.','doubt-refined')
p.change(r'\margin{43}',r'\margin{\hand{43}}','The lower-left foliation is pencilled.','corrected-layer')
p.note('9-10','condition and precisely at right edge','condition and precisely at right edge','confirmed','The right edge clips the endings of condition and précisément; no invisible final letters are added. The (i)à(ii bis) insertion is typed and placed by its bracket.')
p.note('16','ibis overprint','ibis overprint','confirmed','The final label ibis remains legible, although b and the following i have dense overstrikes; no secure earlier label is supplied.')
p.note('23','sihg and dot','sihg and dot','confirmed','The exponent reads sihg. The small separate dot below the second underlined Y is visible but has no secure mathematical or editorial function; it is recorded as a doubtful physical mark.')
p.note('25','hyperplan initial h','hyperplan initial h','confirmed','The source h/h overwrite records the visible typed h with a larger looping pen h. The words en x and the ordinary-point terminology are retained.')
p.note('31','nonempty insertion and erased inequality','nonempty insertion and erased inequality','confirmed','The inserted relation is visibly not-equal to empty, followed by ou. The former less-than-or-equal is scratched out before the live equality to r-2. This mathematical tension is preserved for the guide.')
p.note('32-34','cancelled dimensional clause','cancelled dimensional clause','confirmed','The entire crossed clause is readable; its P has a pen check.')
p.note('42','last hypothesis and extra dot','last hypothesis and extra dot','doubt-retained','The hypothesis number remains ii/iii doubtful; the isolated dot below the opening parenthesis is retained as a physical mark in the NOTE.')
p.note('7-44','remaining lines','remaining lines','confirmed','Both halves were read completely, including images, muni, entenda, the immersion/unramified distinction stated in the margin, and every implication arrow.','full-line-check')
s,d=p.finish()
old=r'\underline{Y}^{\text{sihg}} \neq \underline{Y}^{\text{sup sing}}'
new=r'\underline{Y}^{\text{sihg}} \hand{\neq} \underset{\hand{\unsure{\cdot}}}{\underline{Y}}^{\text{sup sing}}'
assert old in s;s=s.replace(old,new)
d.append(dict(line='23',before=old,image=new,decision='corrected-layer;added-physical-mark',reason='The not-equal is penned. A separate dot is visible below the second Y underline; it is reproduced with uncertain function rather than treated as an established mathematical operator.',category='physical-mark'))
old=r'est de dimension r-1, i.e. de codimension 1 dans P}'
new=r'est de dimension r-1, i.e. de codimension 1 dans $\overset{\hand{\vee}}{P}$}'
assert old in s;s=s.replace(old,new)
d.append(dict(line='33',before=old,image=new,decision='added-handwriting',reason='A small check is visible above the P in the cancelled dimensional clause.',category='handwriting'))
s=s.replace(r'\scanpage{25/43}',r'\scanpage{25/43}'+'\n% NOTE: The dot below the second Y in(ii) has uncertain function. Another isolated dot lies below the opening parenthesis around the final hypothesis number; no additional character value is assigned.',1)
ar.save(k,s,d,0,'Both halves and rotated complete margin inspected; enlarged gon, initial h, typed H, nonempty clause, dodimension, overprinted reference and hypothesis number compared.')
print('Saved43;',ar.aggregate(),'pages checked.')
