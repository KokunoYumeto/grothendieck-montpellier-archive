"""Replay the five fully viewed reviews preserved in the conversation after checkpoint60.

The source images were inspected before the execution environment refresh; the
restored input manifests were verified before this replay. Existing reviews are
never replaced by this recovery script.
"""
import json,re,subprocess,sys,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
os.chdir(ROOT)
reviews=[]
def start(site,general,diffs,unsure,notes,illegible=None,**options):
 global r,s
 key=f'ps_134-6_{site:03d}';s=Path(f'inputs/text/transcription/ps_pages/{key}.tex').read_text()
 r=dict(key=key,both_halves_viewed=True,general=general,diffs=diffs,unsure=unsure,illegible=illegible or [],notes=notes,changes=[],**options)
def c(a,b,why):
 global s
 assert s.count(a)==1,(r['key'],a,s.count(a));r['changes'].append([a,b,why]);s=s.replace(a,b,1)
def finish():reviews.append(r)

start(61,'Both original halves and enlarged canceled parentheses, the overprinted b, these, where, edge g, isomorphism, diagram hat and The were inspected. The pen replacement over with clearly reads where. Enough of the cut final g survives to identify it. The canceled opening and closing characters are too obscured to confirm parentheses, so those readings are now qualified. The b in Ab is typed over an unidentified earlier round impression; these has e typed over i. Isomorphism has i typed over a, not a separate canceled a before the word. The upper-left diagram hat sits over an unreadable earlier typewriter impression. All six diagram arrows, the other body arrows and the two later Hom underlines are pen; the first Homadd underline is a regular thin typed rule. The stepped pen mark before The is a paragraph locator, with horizontal strokes beneath like and without any; the lower h under The is a separate typewriter impression. The literal other functor, Addinf, no tilde on the pair L and no comma after Here are retained.',
 [[8137,'The source has and that accordingly, with a clear that.'],[8143,'The second category name visibly reads Addinf(B), including inf.'],[8147,'The L in the displayed pair has its lower dot and no upper tilde.'],[8149,'No comma follows Here; the canceled run begins immediately after the word space.']],
 [['The penned h, e, r and final e can be distinguished over the old ith.','here'],['The surviving left bowl and lower return identify the clipped final g.','g']],
 ['The two canceled bracket-like characters cannot be confirmed and are qualified. The b is a typed overprint on an earlier unreadable round character.','The first e of these is typed over i; the old i dot survives above it.','The arrow has an uneven pen shaft and head.','The pen correction reads where.','The final g is clipped but its upper and lower left contours remain identifiable.','The initial i is typed over a at the same position.','The diagram hat has an unreadable earlier impression below it; all six arrows are drawn in pen, with typed category names.','The long stepped mark is a paragraph locator, not an underline of the phrase; the extra lower h under The is typed.','The 61 is handwritten archive foliation.'],hand_tokens=[r'\longrightarrow'],hand_underlines=['Hom','exact','abelianizator','for','simultaneous'])
c(r'\xout{(}(',r'\xout{\unsure{(}}(','The canceled initial character is obscured by the overstrike; qualify the parenthesis reading instead of treating it as certain.')
c(r'(Sets))\xout{)}',r'(Sets))\xout{\unsure{)}}','The canceled closing character is similarly obscured; retain the proposed parenthesis with doubt.')
c(r'with (Ab)  being',r'with (A\over[typed]{\illegible{1}}{b})  being','The b is typed over an earlier round character whose exact identity is no longer recoverable; record that one-character overprint.')
c('these niceties',r'th\over[typed]{i}{e}se niceties','The old i dot remains above the typed replacement e.')
c(r'\over{ith}{\unsure{here}}',r'\over{ith}{here}','The pen replacement clearly supplies here after the retained w.')
c(r'correspondin\unsure{g}','corresponding','The cut final g is identified by its surviving upper and lower left contours.')
c(r'in\inserted{section} 93',r'in \inserted{section} 93','Restore the visible space before the separately inserted word section.')
c(r'\xout{a}isomorphism',r'\over[typed]{a}{i}somorphism','The i is typed over a in the same position; this is an overprint rather than a separate deletion before an intact i.')
c(r'\begin{tikzcd}',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\begin{tikzcd}','Document the mixed typed and handwritten provenance of the diagram.')
c(r'A^{\wedge} \arrow[r]',r'A^{\over[typed]{\illegible{1}}{\wedge}} \arrow[r]','The upper-left hat overlays an unreadable earlier typewriter impression; retain the single unknown old character.')
for n in range(6):
 m=next(m for m in re.finditer(r'\\arrow\[([^]]*)\]',s) if 'color=blue' not in m.group(1));a=s.rfind('\n',0,m.start())+1;b=s.find('\n',m.end());old=s[a:b]
 c(old,s[a:m.start()]+r'\arrow[color=blue,'+m.group(1)+']'+s[m.end():b],'Restore handwritten provenance for diagram arrow '+str(n+1)+' from the visibly uneven pen shaft and head; its endpoints, direction and typed objects are unchanged.')
marker=r'\hand{\tikz[x=.4em,y=.4em,baseline=0]{\draw (-2,0)--(0,0)--(0,1.3)--(2,1.3);\draw (.15,0)--(.15,1.3);}}'
c(r'\hand{$\rfloor\!\lceil$}',marker+'\n'+r'% The stepped paragraph locator runs below like, then rises to a stroke below without any.','Replace the corner-glyph approximation with the visible stepped paragraph locator, including its second upright; no lexical content is added.')
c(r'The point\inserted{of (8)}',r'T\(\underset{\text{h}}{\text{h}}\)e point \inserted{of (8)}','Retain the extra lower typed h beneath the baseline h, and the word boundary before the inserted phrase.')
finish()

start(62,"Both original halves and four detailed panels covering all listed overprints and insertion locators were inspected. The first correction in variable is i typed over y, not a deleted j before i. Which has reciprocal pen corrections of the typed c and i. The first abelian has a typed over e, and relevant has e typed over i. The extra h below The is retained spatially. The final y of canonically lies over an a-like impression whose identity remains doubtful; integrators has reciprocal typed e/t corrections and a pen g over an obscured character. Wh is retraced in pen and its X has two typed impressions. Inserted X, e, even an isomorphism, chain and the later quasi-special words are typed; their locators are pen, and the quasi-special parentheses are handwritten. The three long insertion hooks cross nearby letters without canceling them. The canceled name of is legible, while the initial abbreviation and clipped final x remain uncertain. The final closing-quote-like mark after nicety is canceled; its cancellation was previously unmarked. The brace and both arrows in the correspondence are pen. Underline extents have been restricted to the words actually marked; author spellings and the literal A instead of the witness B are retained.",
 [[8164,'The page explicitly says abelianizators followed by the inserted pair and for A; the locator crosses but does not delete for A.'],[8177,'The word upon is fully visible between forces and us.'],[8179,'The article a is visible in make a sense.']],
 [['The initial abbreviation is overprinted; the scan does not securely settle its first-letter case or the underlying letter, so the reading remains qualified.'],['The scan cuts the final letter of complex at the right boundary; retain the x doubt.'],['The canceled n,a,m,e and o,f remain legible beneath the typewriter x strikes.','name of']],
 ['The first correction is a typewriter i over y at one position, not an independent struck j.','The enlarged panels identify the reciprocal c/i pen correction, a-over-e and e-over-i typing, the lower extra h, the partly obscured final y correction, the t/e overprints and pen g, the retraced initial a in the diagram and the pen ld correction in should; unresolved old impressions are qualified.','The first letter of i.e. has overlapping capital-like and lowercase-like strokes; retain doubt.','The last letter of complex remains clipped by the scan boundary.','The pen arc is the insertion locator for the pair; for A remains live.','The arc over the is the locator for still, without canceling the word.','The arc across ho locates the typed word chain; homotopism remains live.','The canceled wording reads name of beneath the typed x strikes.','The 62 is handwritten archive foliation.'],hand_tokens=[r'\longrightarrow'],hand_underlines=['integra-','tor','we get an existence and unicity statement','abelianizator for A','will be no more no less than',r'just a\xout{n}','inte-','grator for B','a projective resolution of','whose components satisfy a mild extra assumption besides being projective','any'])
c(r'var\xout{j}iable',r'var\over[typed]{y}{i}able','The old y fork and descender survive under a regular typed i; retain the one-position overprint.')
c(r'\inserted{$X$}',r'\inserted[typed]{$X$}','The inserted X is a regular typewriter impression; the pen supplies its locator.')
c(r'\mathrm{Wh}_A(X)',r'\over{\mathrm{Wh}}{\mathrm{Wh}}_A(\over[typed]{\unsure{X}}{X})','The Wh has additional pen strokes; X is a typed overprint on an earlier X-like impression whose identity remains qualified.')
c('which should make',r'wh\over{c}{i}\over{i}{c}h should make','The typed c and i are corrected reciprocally by pen strokes; preserve both overwritten positions.')
c('an arbitrary abelian presheaf',r'an arbitrary \over[typed]{e}{a}belian presheaf','The initial a is typed over a visible earlier e.')
c('The main fact',r'T\(\underset{\text{h}}{\text{h}}\)e main fact','The lower h is a displaced extra typewriter impression beneath the intact baseline h.')
c('canonically defined',r'canonicall\over[typed]{\unsure{a}}{y} defined','The final y has an earlier a-like impression beneath it; qualify that underlying reading.')
c(r'proc\inserted{e}eding',r'proc\inserted[typed]{e}eding','The interlinear e is typed, with a pen locator.')
c('quasi-special integrators for B',r'quasi-special in\over[typed]{e}{t}\over[typed]{t}{e}\over{\illegible{1}}{g}rators for B','The t and e are reciprocal typewriter overprints, while g is drawn over an obscured one-letter fragment.')
c(r'\inserted{(even an isomorphism !)}',r'\inserted[typed]{(even an isomorphism !)}','The inserted parenthesis and words are regular typewriter impressions; the surrounding pen hook is their locator.')
c('the relevant categories',r'the rel\over[typed]{i}{e}vant categories','The old i dot remains above the replacement typed e.')
c(r'\inserted{chain}',r'\inserted[typed]{chain}','The word chain is typed above the baseline, with a pen locator passing across ho.')
c(r'\uline{an abelianizator for A will be no more no less than just a\xout{n}}',r'an \uline{abelianizator for A} \uline{will be no more no less than} \uline{just a\xout{n}}','The visible underline begins at abelianizator, not an, and has breaks after A and than; preserve those extents.')
c(r'\inserted{(quasi-special)}',r'\inserted[typed]{\hand{(}quasi-special\hand{)}}','The later quasi-special words are typed above the line; the visible parentheses are pen strokes.')
c(r'\uline{a projective resolution of $\underline{Z}_B$ in $B^\wedge_{ab}$}',r'\uline{a projective resolution of} $\underline{Z}_B$ in $B^\wedge_{ab}$','The pen underline ends beneath of, before the coefficient and category formulas; preserve the actual extent.')
c(r'\text{abelianizators for A}',r'\text{\over{\unsure{A}}{a}belianizators for A}','The first a is retraced in pen over an A-like earlier impression; retain doubt about that old letter.')
for line in list(s.splitlines()):
 if r'\hand{$^{s}$}' in line:c(line,line.replace(r'\hand{$^{s}$}',r'\hand{\ensuremath{{}^{s}}}'),'Give each isolated handwritten superscript s an explicit empty base inside the text labels; its position and content are unchanged.')
c(r'\left\{',r'\hand{\left\{\textcolor{black}{','The brace is handwritten while the correspondence labels are typed; begin a balanced colored brace group with plain label content.')
c(r'\right.',r'}\right.}','Close the balanced handwritten-brace group without changing the correspondence.')
c(r'\xout{\unsure{name of}}',r'\xout{name of}','The canceled name of is legible beneath the typewriter strikes.')
c("\\hand{''}for", "\\hand{''} for",'Restore the visible word space after the handwritten closing quotation marks.')
c('should be in Addinf',r'shou\over{d}{l}\over{d}{d} be in Addinf','The pen l replaces a typed d and the following d is retraced at its own position.')
c('irrelevant nicety" for',r'irrelevant nicety\xout{\unsure{"}} for','Restore the canceled raised closing-quote-like mark after nicety; its exact underlying form remains doubtful.')
finish()

start(63,'Both halves and enlarged to-f, If, Ch, Addinf punctuation, canceled Hom, the two-line cancellation, formula13 hat and lower B, respect, ultimately, standard, abelianizators and formula15 comparison were inspected. Pen strokes reinforce f in If and C in Ch; the latter retains its literal C reading. The opening parenthesis before B replaces a typed f, whereas the dense following exclamation-like mark remains doubtful. The old Hom expression and the two overstruck lines remain unresolved. Formula13 has a pen hat over a typed small a and a repeated typed B beneath lim. Respect contains reciprocal typed p/s corrections; ultimately has m over p, and standard and abelianizators have n over m. The three interlinear additions are typed with pen locators. All display arrows and comparison signs match the existing pen attribution; the final comparison has one wave and one lower stroke. The long underlines are pen. The literal this category and absence of comma after Now are retained.',
 [[8191,'There is a normal space after Now with no comma.'],[8199,'The demonstrative is this, clearly including the initial th.']],
 [['The dense stroke after the inner closing parenthesis has several crossbars and an extended lower tip; its exact exclamation-like reading and operation remain uncertain.'],['The canceled expression shows an initial H and round/parenthesis forms, but the overlapping strokes do not settle the full Hom(Ab) reading.']],
 ['The canceled f after to has additional pen strokes. The f in If has a pen retracing rather than an ordinary added typed bar.','The C has a narrow pen curve through the older C, with tips above and below it; record the retracing without changing the literal C.','The opener before B is drawn over a typed f; the later dense punctuation remains doubtful.','The canceled Hom expression stays doubtful. The pen hat covers a typed small a, and the lower B has a repeated typewriter impression.','The two overstruck lines remain unreadable as a complete fragment; retain the original one-group illegible marker.','Enlarged regular serif impressions show reciprocal p/s in respect, m over p in ultimately, and n over m in standard and abelianizators.','The drawn arrow shafts and comparison strokes are visible in every display; the final comparison remains simeq.','The 63 is handwritten archive foliation.'],
 [['Two overlapping lines of typewriter x strikes cover this fragment; some isolated letter stems survive but no complete reading is secure.']],hand_underlines=['exact','arbitrary','functor','commuting to small sums','abelianizators for','turn out to be no more,','no less than just','a projective resolution,','in the category','of functors from','to','commuting with small direct limits,','of the most interesting object','in this category,','namely the functor'])
c(r'to\xout{f}',r'to\deleted{\xout{f}}','The canceled f has additional irregular pen strokes over the typewriter cancellation.')
c('If so',r'I\over{f}{f} so','The f is retraced in pen, with irregular strokes through its earlier typed form.')
c(r'\text{Ch.}',r'\text{\over{C}{C}h.}','The C has an additional narrow pen curve with projecting tips; preserve it as a retracing of C.')
c(r'Addinf(B)\unsure',r'Addinf\over{f}{(}B)\unsure','The visible opening parenthesis replaces a typed f whose crossbar survives underneath.')
for body in ['abelian','(projective)','(abelian)']:c(r'\inserted{'+body+'}',r'\inserted[typed]{'+body+'}','The interlinear addition has regular typewriter letterforms and a pen insertion locator.')
c('c ategory (12)','category (12)','The scan has ordinary letter spacing within category; remove an extra transcription space.')
old=next(l for l in s.splitlines() if l.startswith('(13)'))
c(old,old.replace(r'\underset{B}',r'\underset{\over[typed]{B}{B}}',1).replace(r'A^{\wedge}',r'A^{\over{a}{\wedge}}',1),'In formula13 the lower B is a repeated typewriter impression, and the pen hat is written over a typed small a; the category base A remains unchanged.')
c(r'\xout{\illegible{1}}'+'\n',r'\xout{\illegible{1}}'+'\n'+r'% This unresolved fragment occupies two overlapping lines of typewriter x strikes.'+'\n','Document the visible two-line extent of the canceled fragment without inventing its unreadable contents or changing the existing group count.')
c('with respect to',r'with re\over[typed]{p}{s}\over[typed]{s}{p}ect to','The typed p and s are reciprocally overprinted at their two positions.')
c('Thus, ultimately,',r'Thus, ulti\over[typed]{p}{m}ately,','The earlier p descender remains under the typed m.')
c('``standard',r'``sta\over[typed]{m}{n}dard','The n is typed over a visible earlier m.')
c("abelianizators''",r"abelia\over[typed]{m}{n}izators''",'The n in this occurrence is typed over m.')
finish()

start(64,"Both original halves and five detail panels covering the locators, clipped endings, canceled clauses, formulas and bold letter positions were inspected. Around has a typed interlinear r with a pen locator passing beside the intact o. Small is also typed above the line. The final s of friends and rs plus raised closing quote of integrators are handwritten; an additional black canceled fragment at the right edge of the latter is now retained as unreadable. The mark after coefficients is x-shaped and below the baseline, but its purpose and underlying character remain uncertain. Was has a typed a over q. The canceled sheaf pre and B above can be read; the latter is replaced by the typed C upstairs. The displayed pen C covers a typed B, and its upper star overlays a typed x. Both Gammas are typed I completed by a pen upper bar. The margin VII has both upper and lower rules. Enlarged letters distinguish typed overprints in wandering, cowered and order from pen retracings in vine, unpremeditatedly and out; ordinary ink variation in surroundings does not establish another correction. The literal cowered, breethe, hav'nt and part VI remain, together with the separate margin VII.",
 [[8204,'The source has the time, not this time.'],[8213,'The preposition is in, with its n visible.'],[8216,'The equality sign is plainly present before the handwritten Delta.'],[8222,'The image retains the raised star; its underlying typed x and the B under the new C are now recoverable.',r'R\over{I}{\Gamma}(\over{B}{C}^{\over{\mathrm{x}}{*}},F)'],[8225,'The margin has VII between upper and lower rules, beside the still-typed part VI.',r'\margin{\(\overline{\underline{\mathrm{VII}}}\)} smoothly in part VI']],
 [['The low mark has the shape and serifs of an x-like overstrike; its purpose and any underlying punctuation remain uncertain.',r'\unsure{${}_{\mathrm{x}}$}','reading refined; residual doubt retained'],['The canceled letters spell sheaf pre beneath the typed x strikes.','sheaf pre']],
 ['The r is a regular typewriter impression above the intact o; the crossing stroke is its pen locator.','The mark is x-shaped and below the baseline; uncertainty about its function is retained.','The a is typed over a q whose descender remains.','The canceled strings can be read as sheaf pre and B above.','C upstairs is typed above the canceled baseline wording.','The old character beneath C is B; the upper star is drawn over a typed x.','The rs and raised closing double quote survive at the edge. A dense canceled fragment below that quote remains unreadable and is retained.','The 64 is handwritten archive foliation.','The enlarged positions show regular typed i-over-r and the order corrections, while the very dark n, e and t have irregular pen retracings. Other apparent boldness alone does not establish an extra character.'],
 [['The canceled text reads B above, with the final comma remaining outside the cancellation.','B above'],['The pale vertical stem and two bowl remnants identify B beneath the pen C.','B']],hand_tokens=[r'\simeq'],unnest_display_hand_math=True)
c(r'a\inserted{r}ound',r'a\inserted[typed]{r}ound','The interlinear r is typed; its pen locator passes beside the intact o and does not replace it.')
c(r'\xout{glad}',r'\deleted{\xout{glad}}','The canceled glad has additional thick pen strokes through the typewriter strikeout.')
c('wandering in the',r'wander\over[typed]{r}{i}ng in the','The i is typed over r; the old hook survives below the new dot.')
c('vine-%',r'vi\over{n}{n}e-%','The n is reinforced by irregular heavy pen strokes over the typed n.')
c('cowered with',r'c\over[typed]{o}{o}wered with','Two distinct offset typewriter o impressions are visible; retain the literal w and spelling cowered.')
c('in order to get',r'in or\over[typed]{e}{d}\over[typed]{\illegible{1}}{e}r to get','The d is typed over e; the following e has another underlying impression that cannot be identified securely.')
c('unpremeditatedly',r'unprem\over{e}{e}ditatedly','The second e is retraced with irregular thick pen strokes.')
c('turns out to be',r'turns ou\over{t}{t} to be','The t has a pen retracing with a long uneven upright and crossbar.')
c("\\hand{rs''}","\\hand{rs}\\deleted{\\illegible{1}}\\hand{''}"+'\n'+r'% The closing quotation mark is raised above the dense canceled fragment at the cut right edge.','Retain the additional unreadable canceled fragment beneath the raised closing quote at the right edge; the visible rs remains unchanged.')
c(r'a\inserted{small}',r'a \inserted[typed]{small}','Small is typed above the line with a pen locator; preserve its separate word boundary.')
c(r'\unsure{$_{*}$}',r'\unsure{${}_{\mathrm{x}}$}','The low mark is x-shaped rather than a star; retain doubt about its function and underlying character, with an explicit empty base for the isolated subscript.')
c('The idea was',r'The idea w\over[typed]{q}{a}s','The old q descender is visible beneath the typed a.')
c(r'\xout{\unsure{sheaf pre}}',r'\xout{sheaf pre}','The canceled sheaf pre is legible beneath the typewriter strikes.')
c(r'\xout{\illegible{1}}\inserted[typed]{C upstairs}',r'\xout{B above}\inserted[typed]{C upstairs}','Recover B above beneath the typed cancellation; the replacement C upstairs is already correctly attributed as typed.')
c(r'\over{\illegible{1}}{C}^{\hand{$*$}}',r'\over{B}{C}^{\over{\mathrm{x}}{*}}','The C is written over a typed B; the handwritten upper star covers a typed x whose lower legs remain visible.')
for line in list(s.splitlines()):
 if r'R\Gamma' in line:c(line,line.replace(r'R\Gamma',r'R\over{I}{\Gamma}'),'Each visible Gamma is a typed I completed with a pen upper bar; preserve that mixed provenance.')
c(r'\margin{\uline{VII}}',r'\margin{\(\overline{\underline{\mathrm{VII}}}\)}','The handwritten margin VII has both an upper and a lower rule; retain the still-typed VI in the body.')
c(r'after\inserted{now}',r'after \inserted{now}','Restore the visible word boundary before the separately inserted now.')
for line in list(s.splitlines()):
 if '\\[' not in line:
  new=line.replace(r'\hand{$\bullet$}',r'\hand{\bullet}').replace(r'\hand{$\Delta$}',r'\hand{\Delta}').replace(r'\hand{$\backslash$}',r'\hand{\backslash}').replace(r'\hand{$\xleftarrow{\ \sim\ }$}',r'\hand{\xleftarrow{\ \sim\ }}')
  if new!=line:c(line,new,'Remove nested dollar delimiters inside already open inline math; symbols, positions and handwriting are unchanged.')
finish()

start(65,"Both halves and enlarged computational, synonym, we've, the first constant Z, broader, integration, Moreover, simultaneous, an, there and the final integrators were inspected. The canceled letter after computational remains uncertain, while the preceding l is a typed correction over o. The final e-like blot after synonym remains doubtful and is a pen cancellation. The v of we've is drawn over an ascender-bearing b, and the first Z is typed over B. Broader has r over o; the lower loop of the first integration g and the initial M of Moreover are pen retracings. Simultaneous has a pen t over a, a typed a over e and an extra canceled fragment before o. The deleted an has pen cancellation, th in there is retraced, and the later integrators has reciprocal typed r/g corrections. Both Gamma signs are typed I completed by pen bars. The two for A additions are typed with pen locators and the first following comma is pen. The long terminology underlines are pen. The literal abelianizator for B together with X in A-hat and Wh-A is retained as an unresolved mathematical index discrepancy for the guide.",
 [[8229,'No comma follows Therefore.'],[8230,'The final letter of embodied is d.'],[8238,'No comma follows Therefore across its source line break.'],[8239,'Cointegrator has a visible pen underline.'],[8247,'No comma follows Thus.'],[8249,'The handwritten archive number65 is present at the lower left.']],
 [['The extra canceled character after computational is covered by thick crossing strokes; neither l nor y can be confirmed.'],['The dense final mark has an e-like upper contour, but its inner strokes are filled and the letter remains doubtful.']],
 ['The live l is typed over o, followed by a separate canceled uncertain letter with additional pen strokes.','The final e-like character is canceled by a dense pen blot; no regular typewriter x is distinguishable.','Both for A phrases are typed above the line; their hooks and the comma after the first are handwritten.','The 65 is handwritten archive foliation.'],hand_underlines=['co','cointegrator','integration','integrator','for'])
c("we've come",r"we'\over{b}{v}e come",'The pen v covers a typed b whose upper ascender remains visible.')
c(r'the constant abelian presheaf $\underline{Z}_A$',r'the constant abelian presheaf $\underline{\over[typed]{B}{Z}}_A$','The first constant-presheaf Z is typed over a visible B; its underline and lower A are unchanged.')
c('a broader use',r'a b\over[typed]{o}{r}oader use','The r is typed over an earlier o.')
c('``integra-%',r'``inte\over{g}{g}ra-%','The lower loop of the first integration g is reinforced with pen strokes.')
c('Moreover, it turns',r'\over{M}{M}oreover, it turns','The initial M is retraced in pen over its typed form.')
c(r'computational\xout{\unsure{l}}',r'computationa\over[typed]{o}{l}\deleted{\xout{\unsure{l}}}','The live l is typed over o and the following uncertain canceled character has additional pen strokes.')
c(r'synonym\xout{\unsure{e}}',r'synonym\deleted{\unsure{e}}','The final e-like character is covered by a pen blot rather than a discernible typewriter x strike; retain the letter doubt.')
c('simultaneous computation',r'simul\over{a}{t}\over[typed]{e}{a}ne\deleted{\xout{\illegible{1}}}ous computation','The t is pen over a, the following a is typed over e, and an extra canceled fragment occurs before o; preserve all three visible operations.')
c(r'by \xout{an}',r'by \deleted{\xout{an}}','The canceled an has additional irregular pen strokes.')
c("there does'nt",r"\over{th}{th}ere does'nt",'The t and h are retraced with heavy pen strokes.')
c('come from integra-%',r'come from inte\over[typed]{r}{g}\over[typed]{g}{r}a-%','The g and r are reciprocal typewriter overprints; the old g descender survives below the replacement r.')
c("integrator''\\inserted[typed]{(for A)}", "integrator'' \\inserted[typed]{(for A)}",'Retain the visible separation before the inserted parenthetical for A.')
for line in list(s.splitlines()):
 if r'R\Gamma' in line:c(line,line.replace(r'R\Gamma',r'R\over{I}{\Gamma}'),'Restore the typed I and handwritten upper bar that together form Gamma in this occurrence.')
finish()

ledger=ROOT/'PS_READERS_WORK/review_notes/134_5_6.jsonl'
existing={json.loads(x)['key'] for x in ledger.read_text().splitlines()}
temp=ROOT/'tmp/collation_134_5_6';temp.mkdir(parents=True,exist_ok=True)
for review in reviews:
 if review['key'] in existing:continue
 q=temp/(review['key']+'_recovered.json');q.write_text(json.dumps(review))
 subprocess.run([sys.executable,'PS_READERS_WORK/scripts/record_review_134_5_6.py',str(q.relative_to(ROOT))],check=True)
subprocess.run([sys.executable,'PS_READERS_WORK/scripts/collation_134_5_6.py'],check=True)
