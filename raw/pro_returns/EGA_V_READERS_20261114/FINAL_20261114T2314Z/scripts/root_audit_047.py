from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_047';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\mspage{48}',r'\mspage{\hand{43}}','The circled upper foliation has the open double-curved3, not8.','corrected-reading;corrected-layer')
p.change(r'\unsure{\hand{(}}En',r'En','The stroke touching E belongs to the outline and hook of the top inserted note; it is not a separate manuscript parenthesis.','removed-noncontent')
p.change('justitffier','justitffer','The image has two fs followed directly by er; no i follows the second f.','corrected-reading')
p.change('avec dim P',r'avec di\unsure{m|p} P','The last letter is overtyped and shows an m top with a p-like descender.','doubt-added')
p.change(r'\xout{xxxdisant}',r'\xout{\illegible{1} disant}','Disant is legible, but the preceding crossed group does not yield a secure word. Literal placeholders are replaced by an explicit illegibility mark.','corrected-uncertainty-encoding')
p.change(r'\xout{xxxxx}',r'\xout{\illegible{1}}','The crossed group before the following number abbreviation remains unreadable; it is encoded as an illegible word.','corrected-uncertainty-encoding')
p.change(r'\margin{\unsure{$\|$}}','% NOTE: Two long parallel pencil sidestrokes mark the following paragraph.\n','The parallel pencil marks are marginal emphasis strokes, not a textual norm/double-bar symbol.','moved-description-to-note')
p.change(r'\unsure{dus|des}',r'dus','The middle letter has the open-bottom u form; the source spelling dus is retained.','doubt-resolved')
p.change(r'\unsure{\geq}',r'\geq','The marginal inequality is legible.','doubt-resolved')
p.change('``réglé\'\' pour f si',r"``\uline{réglé}'' pour f si",'Réglé is underlined in the marginal note.','added-underlining')
p.change(r'\to',r'\hand{\to}','The opening morphism arrow is handwritten; the arrow in the wholly handwritten marginal note remains a pen mark.','corrected-layer')
p.change(r'\xout{xxensemble}',r'\xout{ensemble}','The crossed word ensemble is readable; the initial literal xs were cancellation strokes.','recovered-reading')
p.change(r'\xout{auxxconditionsxéquivalentes}',r'\xout{aux conditions équivalentes}','The cancelled phrase is readable; interposed typewriter crosses are represented by the xout macro.','recovered-reading')
p.change(r"\xout{dex8x8xxx(disonsxdoncxsimplementxX'xestxnonxx}",r"\xout{de 8.8. (disons donc simplement X' est non}",'The cancelled reference and following words are readable across this line.','recovered-reading')
p.change(r'\xout{\illegible{12}}',r'\xout{que toute composante irréductible \illegible{3} de dimension \illegible{3}}','Independent enlargement identifies these two secure fragments. Intervening crossed groups stay unreadable; the word counts in the gaps are estimates, not reconstructed words.','recovered-reading;unresolved-gaps')
p.change(r'\xout{\illegible{10}}',r'\xout{\illegible{2} tels que \illegible{1} soit \illegible{1} régulier et que \illegible{1} satisfasse}','Independent enlargement identifies these surviving words. No intervening formula or index is reconstructed; gap word counts remain estimates.','recovered-reading;unresolved-gaps')
p.change(r'\mathrm{\unsure{sup\,sing}}',r'\mathrm{\unsure{supging|sup\,sing}}','The overtyped exponent contains a g-like outline where sing would begin; both visible candidates remain.','doubt-refined')
p.change(r'\hand{$\check{P}$}',r'$\overset{\hand{\vee}}{P}$','At these occurrences P is typed and its check is handwritten.','corrected-layer')
p.change(r'\xout{fermédesxxxxxx}',r'\xout{fermée des \illegible{1} tels}','The crossed group has readable fermée des and final tels, with the intervening group unresolved.','recovered-reading;doubt-added')
p.change(r'\margin{47}',r'\margin{\hand{47}}','The lower foliation is pencilled.','corrected-layer')
p.note('5-11','top note and end marker','top note and end marker','confirmed','The repeated rho/P-like marks link the lower insertion to its continuation along the top margin. They are editorial reference marks, not additional mathematical variables.')
p.note('21-23','marginal NB','marginal NB','confirmed','The complete note was read across the two halves and rotated. It states the codimension criterion, with réglé underlined and greater-than-or-equal2 legible. Its two arrows point to réglée and the later exceptional-case sentence.')
p.note('25','overwritten8.6','overwritten8.6','doubt-retained','The final6 is visible, but the preceding typed numeral is irrecoverable under the black strokes.')
p.note('31-40','cancelled proposition draft','cancelled proposition draft','confirmed','The boxed paragraphs and the handwritten corrections inside them are crossed by several unambiguous pen diagonals. The superscript remains overprinted; blank space between X prime and P is retained without inventing an arrow.')
p.note('33','k relation0','k relation0','doubt-retained','The relation between k and0 is not securely legible through the cancellation; the recorded greater-than-or-equal candidate stays doubtful.')
p.note('34-38','nested typewriter strikeouts','nested typewriter strikeouts','unresolved','Each full cancelled line was enlarged. Some fragments are recovered separately, while the dense two longer overwritten lines retain explicit illegibility marks.')
p.note('7-42','complete page','complete page','confirmed','Both halves were read line by line, including the ruled terminology, taupe, positive-characteristic example request, section-reorganization remark, doubled de de and final Z sub k clause.','full-line-check')
s,d=p.finish()
old=r'\margin{(\unsure{$\uparrow$|?} la variété \unsure{lin} L de codim 2 des hyperplans tangents à X en x, donc par raisons de dim. on a T = L, donc $X \subset L^{\circ}$ = polaire de L, qui est une droite, donc X est un \unsure{\uline{ouvert}} d\'une droite.)}'
# Apostrophes are literal manuscript characters.
old="\\margin{(\\unsure{$\\uparrow$|?} la variété \\unsure{lin} L de codim 2 des hyperplans tangents à X en x, donc par raisons de dim. on a T = L, donc $X \\subset L^{\\circ}$ = polaire de L, qui est une droite, donc X est un \\unsure{\\uline{ouvert}} d'une droite.)}"
assert old in s;s=s.replace(old,'')
old2=r'\inserted{Par exemple, si dim $X=1$, cela implique que X est une droite, car si $x \in X(k)$, alors T contient \unsure{$\uparrow$|P}}'
new="\\inserted{Par exemple, si dim $X=1$, cela implique que X est une droite, car si $x \\in X(k)$, alors T contient la variété lin L de codim 2 des hyperplans tangents à X en x, donc par raisons de dim. on a \\unsure{-|:} T = L, donc $X \\subset L^{\\circ}$ = polaire de L, qui est une droite, donc X est un \\uline{ouvert} d'une droite.}"
assert old2 in s;s=s.replace(old2,new)
d.append(dict(line='5,11',before=old+' / '+old2,image=new,decision='corrected-placement;doubt-resolved',reason='The identical end/start hook marks join the entire top note to the insertion after contient. Lin and underlined ouvert are readable. A short sign after on a remains dash/colon doubtful. The surrounding outline is recorded as an editorial enclosure, not manuscript parentheses.',category='insertion-placement'))
old=r"\hand{$\xi$}$\in$$\overset{\hand{\vee}}{P}$"
new=r"\hand{$\xi$}$\hand{\in} P$"
assert old in s;s=s.replace(old,new)
d.append(dict(line='42',before=old,image=new,decision='corrected-layer;removed-spurious-check',reason='At the final xi membership clause P is visibly typed with no check; the membership sign is handwritten. The earlier P on this line does have a pen check.',category='physical-mark'))
s=s.replace(r'\scanpage{25/47}',r'\scanpage{25/47}'+'\n% NOTE: The top note is enclosed and linked to the insertion after contient by matching rho/P-like reference marks; they carry no independent mathematical letter value.\n',1)
ar.save(k,s,d,0,'Both halves fully read, long top insertion traced and rejoined, rotated NB inspected, all cancelled lines enlarged; upper foliation43 and final unchecked typed P resolved.')
print('Saved47;',ar.aggregate(),'pages checked.')
