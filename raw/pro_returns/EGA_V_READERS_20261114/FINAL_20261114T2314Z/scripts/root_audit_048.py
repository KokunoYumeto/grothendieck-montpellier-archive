from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_048';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\mspage{\unsure{45|46}}',r'\mspage{\hand{\unsure{44|45}}}','The retraced final digit supports4/5; the direction of any overwrite is unresolved. Independent visual inspection agrees and finds no secure6.','doubt-refined;corrected-layer')
p.change(r'\zeta',r'\xi','The repeated penned glyph is the curled xi form. Each occurrence was checked, including subscripts and the last membership clause.','corrected-reading')
p.change(r'\over{B}{P}our',r'Bour','The first type position has the serif spine and two bowls of B. No separate pen P is securely visible, so the unsupported overwrite is removed and the printed spelling retained.','corrected-reading;corrected-layer')
p.change(r'\deleted{\unsure{et $X\'$',r'\deleted{\hand{\unsure{de|et} $X\'$', 'The first word of the crossed handwritten insertion remains de/et doubtful.','doubt-refined') if False else None
p.change(r'\deleted{\unsure{et $X\'\!$}}',r'', 'unused') if False else None
old="\\deleted{\\unsure{et $X'$ qui est non réglée rel. à $f$}}"
new="\\deleted{\\hand{\\unsure{de|et} $X'$ qui est non réglée rel. à $f$}}"
p.change(old,new,'The crossed insertion is handwritten. Its initial word remains de/et doubtful, while the following phrase is legible.','doubt-refined;corrected-layer')
p.change(r'\unsure{qui est non réglée rel. à $f$}',r'qui est non réglée rel. à $f$','The crossed handwritten clause is legible.','doubt-resolved')
p.change(r'\unsure{i.e. toute composante irréductible $X\'$',r'', 'unused') if False else None
p.change(r'\margin{\unsure{lieu non-ordin. géométrique}}',r'\margin{lieu singulier géométrique}','The margin reads lieu singulier géométrique; the descending g and ending of singulier are visible. Independent comparison supports the same reading.','doubt-resolved')
p.change(r'\xout{xxxxxxxxxxxxxx(pt}',r'\xout{\unsure{est} \illegible{2} (pt}','The cancelled group begins with est-like surviving letters and ends (pt; the intervening crossed groups remain unreadable.','recovered-reading;doubt-added')
p.change(r'\over{,}{.}',r',','The mark after isolés is a typed comma with a descending tail. No separate pen full stop is visible in its enlargement.','removed-spurious-overwrite')
p.change('est inoffensif, car',r'est inoffens\unsure{i|f}f, car','The penultimate type position has competing i/f traces; the first inoffensif earlier in the proof remains distinct and unchanged.','doubt-added')
p.change('cela conduit à',r'cela condu\unsure{i|t}t à','The overwritten type position supports i/t; the final t is clear.','doubt-added')
p.change("d'un ensemble de codimension",r"d'un ensemble de \unsure{codimension}",'The middle letters have dense typewriter overprints. The lexical reading is retained as doubtful rather than silently normalized.','doubt-added')
p.change('plus satis-%',r'plus sat\unsure{is|in}-%','The last two type positions before the clipped line end are overprinted; is/in remain possible.','doubt-added')
p.change(r'\margin{\unsure{n}}',r'\margin{n}','The faint lower-left mark is a serif typed n.','doubt-resolved')
p.change(r'\unsure{isolé}',r'isolé','The crossed handwritten word isolé is legible.','doubt-resolved')
p.change("qu\\deleted{'il", "qu'\\deleted{il",'The apostrophe after qu precedes the deletion boundary; the cancelled passage starts with il.','corrected-deletion-boundary')
p.change('de $x$ tel que','de $X$ tel que','The X in the cancelled lower clause is uppercase.','corrected-reading')
p.change(r'\geq',r'\hand{\geq}','The greater-than-or-equal signs in the typed lines are penned.','corrected-layer')
p.change(r'\check{P}',r'\overset{\hand{\vee}}{P}','The otherwise typed P in condition b has a pen check; the top note is wholly handwritten.','corrected-layer')
p.change(r'\rightarrow',r'\hand{\rightarrow}','The arrow in the final corollary heading is penned.','corrected-layer')
p.change(r'\mspage{48}',r'\margin{\hand{48}}','The lower48 is pencil archive foliation, not another manuscript page number.','corrected-layer')
p.note('7-8','top handwritten note','top handwritten note','confirmed','The first mathematical letter favors the crossing-stroke X prime of the supplied reading; it is preserved. Sing is raised. The repeated rho-like reference mark joins this note to the later codimension2 sentence, and is not a variable.')
p.note('10-27','all formula letters','all formula letters','confirmed','The phi-like printed signs are typewriter characters, while their xi subscripts are penned. All indices, k/k-1 bounds and the deleted f et groups were compared separately.')
p.note('14-27','upper revisions','upper revisions','confirmed','The a insertion is placed after toute composante irréductible by its hook. In b the large box and diagonal crossings cancel the inner i.e. reformulation as well as the typed material. The lower soit contenue/dans X prime is outside the clear diagonals; its relation to the cancelled reformulation remains unsettled and it stays marked as an insertion.')
p.note('35-43','infimum and reference marks','infimum and reference marks','confirmed','The typed l inf de insertion belongs after égale à. The slash before the parenthetical proof is an insertion hook; the loop-headed mark after2 matches the top note. Neither is promoted to a mathematical symbol.')
p.note('46-49','cancelled final remark','cancelled final remark','confirmed','The entire boxed A vrai dire paragraph is crossed. The k, resp. dim and k+1 text are retained without supplying absent inequality signs.')
p.note('55-61','lower deletion','lower deletion','confirmed','The large enclosure and diagonals cross the typed clause and the handwritten continuation, including the isolated-point and component alternatives. The crossed E remains unreadable; the entire source cancellation is retained.')
p.note('10-61','complete page','complete page','confirmed','Both halves were read in full, including all interlinear and marginal material, the formula scopes, source singular singulier, cut right edges and the spelling inoffensif/conduit overprints.','full-line-check')
s,d=p.finish()
# Rejoin the top note at its matching reference mark.
old=r"\inserted{grâce au fait que $\underline{X'}$ sing est de dim $r-1$, où $r=\dim \overset{\hand{\vee}}{P}$ !}"
assert old in s;s=s.replace(old,'')
marker=r'\hand{\unsure{$\xi$}$\}$}'
new=r"\inserted{grâce au fait que $\underline{X'}^{\text{sing}}$ est de dim $r-1$, où $r=\dim \check{P}$ !}"
assert marker in s;s=s.replace(marker,new)
d.append(dict(line='8,43',before=old+' / '+marker,image=new,decision='corrected-placement;corrected-physical-mark',reason='The loop-headed reference mark at the top note repeats immediately after codimension2. The complete note is placed there; the link mark is not xi or a closing brace. Sing is visibly raised after X prime.',category='insertion-placement'))
# Hook of a: the added component description follows its typed noun phrase.
old=r"\inserted{$X'_i$ de $X'$ de dim $\leq k$ soit \uline{réglée} pour $f$.}"
assert old in s;s=s.replace(old,'')
anchor=r'toute composante irréductible \deleted{de $X_i$'
new= r'toute composante irréductible '+old+r' \deleted{de $X_i$'
assert anchor in s;s=s.replace(anchor,new,1)
d.append(dict(line='15-16',before=old+' before toute composante irréductible',image=new,decision='corrected-placement',reason='The insertion enclosure points to the end of the typed phrase toute composante irréductible, before the deleted continuation.',category='insertion-placement'))
# The inner b reformulation is within the diagonally cancelled block.
old=r"\inserted{\unsure{i.e. toute composante irréductible $X'_i$ de $X'$ de}}"
new=r"\deleted{\inserted{i.e. toute composante irréductible $X'_i$ de $X'$ de}}"
assert old in s;s=s.replace(old,new)
d.append(dict(line='24',before=old,image=new,decision='corrected-deletion;doubt-resolved',reason='This handwritten line is legible and lies inside the box crossed by several diagonals; it is cancelled with the typed block.',category='deletion'))
old=r"\inserted{\unsure{de dim $\leq k+1$ est, \deleted{\unsure{soit}} réglée rel. à $f$, \deleted{\unsure{soit}} telle que $X'_i = X_i$.}}"
new=r"\deleted{\inserted{dim $\leq k+1$ est, \deleted{soit} \uline{réglée} rel. à $f$, \deleted{soit} telle que $X'_i = X_i$.}}"
assert old in s;s=s.replace(old,new)
d.append(dict(line='26',before=old,image=new,decision='corrected-deletion;corrected-reading',reason='The lower handwritten line starts dim, without another de. It is crossed by the box cancellation; both inner soit cancellations and underlined réglée are visible. The letter/index string is retained.',category='deletion'))
old=r"\inserted{\unsure{soit contenue} \unsure{dans $X'$}}"
new=r"\inserted{soit contenue dans $X'$}"
assert old in s;s=s.replace(old,new)
d.append(dict(line='27',before=old,image=new,decision='doubt-resolved;attachment-unsettled',reason='The lower words soit contenue and dans X prime are legible. They lie below the principal crossed box; their exact attachment and the force of the small surrounding stroke remain unsettled, recorded in the NOTE.',category='insertion'))
old=r"\inserted[typed]{l'inf de}\n".replace('\\n','\n')
# The original contains a source newline after this insertion.
assert old in s;s=s.replace(old,'')
anchor=r'est égale à \hand{(}codim'
new=r"est égale à \inserted[typed]{l'inf de} codim"
assert anchor in s;s=s.replace(anchor,new)
d.append(dict(line='36-38',before=old+' / '+anchor,image=new,decision='corrected-placement;removed-noncontent',reason='The typewriter insertion is bracketed immediately before codim after égale à; the curved hook is not an extra mathematical parenthesis.',category='insertion-placement'))
s=s.replace(r'\hand{/}(ce qui',r'(ce qui',1)
d.append(dict(line='41',before=r'\hand{/}(ce qui',image='(ce qui',decision='moved-physical-mark-to-note',reason='The sloping stroke is the end of the insertion bracket, not a manuscript slash in the sentence.',category='physical-mark'))
s=s.replace(r'\hand{/}, on trouve',r', on trouve',1)
d.append(dict(line='51',before=r'\hand{/}, on trouve',image=', on trouve',decision='moved-physical-mark-to-note',reason='The sloping stroke belongs to the typed et8.6 insertion hook; it does not add a slash to the running sentence.',category='physical-mark'))
s=s.replace(r'\scanpage{25/48}',r'\scanpage{25/48}'+'\n% NOTE: Matching loop-headed reference marks carry the top grâce note to the proof after codimension2. Insertion hooks are not mathematical parentheses or slashes. The lower soit contenue dans X prime is legible but its attachment and the force of its small enclosure remain unsettled.\n',1)
ar.save(k,s,d,0,'Both full halves and all dense corrections enlarged; cancellation bounds, matching reference marks, typed infimum placement, manuscript foliation and three overprinted words inspected; independent margin/top/folio comparison.')
print('Saved48;',ar.aggregate(),'pages checked.')
