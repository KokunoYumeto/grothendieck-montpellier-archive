import importlib.util,json
from pathlib import Path
s=importlib.util.spec_from_file_location('r',Path(__file__).with_name('review_134_7_8.py'));r=importlib.util.module_from_spec(s);s.loader.exec_module(r)
circ_b=r'\margin{\tikz[baseline=(bi.base)]{\node[inner sep=3pt] (bi) {\ensuremath{b_i^{\prime}}};\draw[color=blue] (bi.center) ellipse (1.6em and 1.4em);}}'
circ_note=r'\margin{\tikz[baseline=(cn.base)]{\node[inner sep=3pt] (cn) {\shortstack{Centrer\\et déployer}};\draw[color=blue] (cn.center) ellipse (4.4em and 2.5em);}}'
outer=r'''\draw[color=blue,line width=.35pt] (2.3,.55)--(2.3,.40) .. controls (1.8,.50) and (-.65,.62) .. (-.65,-.20) .. controls (-.8,-1.1) and (-.6,-2.15) .. (-.15,-2.28) .. controls (.8,-2.55) and (1.75,-2.5) .. (2.0,-2.75)--(2.0,-3.25);
\draw[color=blue,->,line width=.35pt] (1.95,.43)--(2.22,.44);
\draw[color=blue,->,line width=.35pt] (1.45,-2.58)--(1.75,-2.65);'''
picture=r'''\hand{(6)} \diagram{
% Hand-drawn arrows are marked blue; typed objects remain plain.
\begin{tikzpicture}[x=1.35cm,y=1.05cm,baseline=(bp.base)]
\node (bp) at (0,0) {\ensuremath{B'}};
\node (b) at (0,-1) {\ensuremath{B}};
\node (ap) at (1.65,0) {\ensuremath{\mathrm{Add}(B')}};
\node (a) at (1.65,-1) {\ensuremath{\mathrm{Add}(B)}};
\node (ip) at (3.85,0) {\ensuremath{\mathrm{Addinf}(B')}};
\node (i) at (3.85,-1) {\ensuremath{\mathrm{Addinf}(B)}};
\node (up) at (6,0) {\ensuremath{B'^{\hand{\wedge}}_{ab}}};
\node (u) at (6,-1) {\ensuremath{B^{\hand{\wedge}}_{ab}}};
\node (sp) at (3,-2.65) {\ensuremath{B'^{\hand{\wedge}}}};
\node (ss) at (3,-3.6) {\ensuremath{B^{\hand{\wedge}}}};
\foreach \s/\t in {bp/ap,ap/ip,ip/up,b/a,a/i,i/u}{
 \draw[color=blue,->] ([xshift=2pt,yshift=3pt]\s.east) .. controls ([xshift=-2pt,yshift=1pt]\s.east) and ([xshift=-1pt,yshift=-1pt]\s.east) .. ([xshift=5pt,yshift=-1pt]\s.east) -- (\t.west);
}
\draw[color=blue,->] (bp.south)--node[left]{\ensuremath{\hand{f}}}(b.north);
\draw[color=blue,->] (ap.south)--node[left]{\ensuremath{\hand{\mathrm{Add}(f)}}}(a.north);
\draw[color=blue,->] (ip.south)--node[left]{\ensuremath{\hand{\mathrm{Addinf}(f)}}}(i.north);
\draw[color=blue,->] (up.south)--node[right]{\ensuremath{\hand{f_!^{ab}}}}(u.north);
\draw[color=blue] ([xshift=4pt]bp.south) .. controls ([xshift=-5pt,yshift=-1pt]bp.south) and ([xshift=1pt,yshift=-3pt]bp.south) .. (1.0,-.73);
\draw[color=blue,->] (1.7,-1.35)--(sp.north west);
\draw[color=blue,->] ([xshift=3pt]b.south) .. controls ([xshift=-7pt,yshift=-1pt]b.south) and ([xshift=1pt,yshift=-5pt]b.south) .. (ss.north west);
\draw[color=blue,->] (sp.south)--node[right]{\ensuremath{\hand{f!}}}(ss.north);
\draw[color=blue] (sp.north east)--(4.4,-1.45);
\draw[color=blue,->] (4.9,-.80)--(up.south west);
\node at (4.0,-1.72) {\ensuremath{\hand{\mathrm{Wh}_{B'}}}};
\draw[color=blue,->] (ss.east)--node[right]{\ensuremath{\hand{\mathrm{Wh}_{B}}}}(u.south);
OUTER
\node at (6.9,-3.75) {.};
\end{tikzpicture}}'''.replace('OUTER',outer)
raw=r.read('ps_134-6_057');start=raw.index(r'\hand{(6)} \diagram{');end=raw.index(r'\end{tikzcd}}',start)+len(r'\end{tikzcd}}');oldpic=raw[start:end]
a={'key':'ps_134-6_057','both_halves_viewed':True,'summary':'Both full halves inspected. The older vertical remains partly covered by horizontal; the are correction covers only ar, with the final typed e outside it. Both a-to-A corrections are retained. The circled margin b-prime with lower i is legible and rendered with its oval. The cancelled formula before the sum remains doubtful under both typed and pen cancellation. In the sums, the i and I are typed while the sum and membership signs are pen. The extra p in envelopes is legible. Into has pen t and pen o over typed o; a is added in pen. Beautiful has a cancelled baseline a and an interlinear pen au. Both diagrams are checked; all arrows, including the six horizontal hooks of(6), are hand-drawn. The lower B diagonal targets the bottom B-hat. The B-prime diagonal and Wh-B-prime diagonal are interrupted at the intervening row. The unattached outer pencil enclosure is preserved separately, with its two arrowheads and bent ends; independent inspection confirms that neither end meets a named object. The margin instruction is circled. The empty-hat constructs and nested dollars are repaired without changing the source notation.',
'edits':[
 {'old':r'\over{\unsure{are}}{ar}e','new':r'\over{\unsure{ar}}{ar}e','reason':'The pen ar covers two typed cells; the final typed e is separate and untouched. Narrow the uncertain old span so the old final e is not duplicated.'},
 {'old':r"\margin{\unsure{$b'_i$}}",'new':circ_b,'reason':'The handwritten b, raised prime and dotted lower i are identifiable inside a continuous oval, which is now rendered.'},
 {'old':r"\deleted{\xout{\unsure{$f_!^{ab}(L')$}}}",'new':r"\deleted{\xout{\unsure{f_!^{ab}(L')}}}",'reason':'The old expression remains doubtful under both layers of cancellation. Remove only the redundant dollar delimiters inside the surrounding display.'},
 {'old':r'\hand{\bigoplus_{i\in I}}','new':r'\hand{\bigoplus}_{i\hand{\in} I}','count':2,'reason':'The i and I are regular typed characters; only the circled plus and membership sign are hand-drawn.'},
 {'old':r'envelop\xout{\unsure{p}}es','new':r'envelop\xout{p}es','reason':'The extra p has a legible lower descender and bowl beneath the x cancellation.'},
 {'old':r'in\unsure{to} \hand{a}','new':r'in\hand{t}\over{o}{o} \hand{a}','reason':'The t has a free pen stem/crossbar; no separate older t is certified. The following pen o retraces a visible typed o, and a is pen.'},
 {'old':r'be\over{a}{au}tiful','new':r'be\deleted{a}\inserted{au}tiful','reason':'The old baseline a is crossed out, while the new pen au is above the line. Preserve that placement rather than depicting a same-cell overwrite.'},
 {'old':r'\margin{Centrer et déployer}','new':circ_note,'reason':'The handwritten French instruction is enclosed by a pencil oval; both the two-line text and the oval are now represented.'},
 {'old':oldpic,'new':picture,'reason':'Reconstruct the checked source diagram with hand-drawn horizontal hooks, four vertical functors, the correctly targeted B-to-B-hat diagonal, both interrupted diagonals, their handwritten labels, the lower-right period, and the separate unattached pencil enclosure. The old dddrr route targeted a nonexistent grid row.'},
 {'old':r"% NOTE: the rows B' -> Add(B') -> Addinf(B') -> B'^_ab and B -> Add(B) -> Addinf(B) -> B^_ab with their hook arrows are typed; all vertical and diagonal arrows and their labels are drawn by hand. The hooked arrow from B' to B'^ is drawn interrupted (behind Add(B)); a further hand-drawn curved line with arrowheads runs from above the top row round the left of the diagram to the bottom, towards B'^.",'new':'% Reviewed diagram(6): all arrows are hand-drawn; object names are typed. The two interrupted diagonals and the unattached outer pencil enclosure are preserved as drawn.','reason':'Correct the nonprinting draft description after the source shows six hand-drawn horizontal hooks, not typed arrows.'}],
'diff':{'8088':{'reading':circ_b,'reason':'The circled b-prime with lower dotted i is clearly visible and retained.'},'8091':'The source reads accordingly if F is an object, without an extra and or of.','8097':'The source has canonical isomorphisms in the plural.','8099':{'reading':'separate outer pencil enclosure with two arrowheads','decision':'our transcription corrected','reason':'The outer curve has two bent unattached ends and two arrowheads along it. It is restored as a graphic rather than invented as a functor between nodes; independent inspection agrees.'},'8100':{'reading':circ_note,'reason':'The margin instruction Centrer et déployer and its surrounding oval are visible pencil strokes.'}},
'unsure':{'1':{'decision':'doubt retained','reason':'The older vertical-like word is partly obscured by the longer pen horizontal. The image does not expose every old character sufficiently to remove the existing doubt.'},'2':{'reading':r'\over{\unsure{ar}}{ar}e','decision':'doubt retained','reason':'Only the old ar cells are covered; the last typed e is clear and retained outside the overwrite.'},'3':{'reading':circ_b,'reason':'The b, raised prime and lower dotted i are identifiable within the circle.'},'4':{'reading':r"\deleted{\xout{\unsure{f_!^{ab}(L')}}}",'decision':'doubt retained','reason':'The general shape matches the proposed expression, but the heavily crossed first symbol and indices remain too obscured for certainty.'},'5':{'reading':'p','reason':'The extra p is legible through the typed x.'},'6':{'reading':r'\hand{t}\over{o}{o}','reason':'The live t and o are pen; the old o is visible, but no independent old t is supplied.'}},
'notes':{'1':'Horizontal is clear pen, while the older vertical remains partly covered. The corrected ar span is narrowed to two cells, excluding the untouched final e.','2':'The cancelled formula remains uncertain; both pen and typewriter cancellation are preserved and nested math delimiters removed.','3':'The circled b-prime with lower i is legible and now rendered with its oval.','4':'The t is pen, o is pen over typed o, and the following a is pen.','5':'The old extra p is legible below the x lattice.','6':'The reconstructed diagram preserves both interrupted diagonals. All six horizontal hooks are pen. The outer pencil enclosure is independent of the named objects; neither end is attached, as confirmed by a second reading.','7':'The lower-left57 is handwritten archive foliation.','8':'The page has handwriting throughout its corrections, labels and diagram arrows; the original trailing long-handwriting note adds no further undeciphered lexical passage.'}}
# Apply caret placement repairs after replacing diagram(6), then mark the remaining confirmed symbols.
t=raw
for e in a['edits']:t=t.replace(e['old'],e['new'],e.get('count',1))
for old,new in [(r"B'\hat{}",r"B'^{\hand{\wedge}}"),(r'B\hat{}',r'B^{\hand{\wedge}}'),(r'D^-',r'D^{\hand{-}}')]:
 n=t.count(old)
 if n:a['edits'].append({'old':old,'new':new,'count':n,'reason':'Place the visibly handwritten caret or minus on its actual typed base, repairing the empty-accent source construct where present.'});t=t.replace(old,new)
for old,new in [(r'\ar[r,',r'\ar[color=blue,r,'),(r'\ar[d,',r'\ar[color=blue,d,')]:
 n=t.count(old)
 if n:a['edits'].append({'old':old,'new':new,'count':n,'reason':'The arrows of diagram(5) are continuous pen strokes; mark their handwriting without changing directions or labels.'});t=t.replace(old,new)
r.annotate_hand_tokens(a,[r'\simeq',r'\to'])
r.commit(a)
p=Path('PS_READERS_WORK/records/MASTER_VARIANTS_134_7_8.json');vs=json.loads(p.read_text());v={'key':a['key'],'before':picture,'after':picture.replace(outer,''),'in_math':False,'kind':'unattached placement graphic','reason':'The outer pencil enclosure has no endpoint on a named object. Preserve it in the diplomatic diagram and apparatus without adding a functor to the reading diagram. All mathematical arrows and labels are unchanged.','source_id':'GRAPH:'+a['key']+':outer'};assert not any(x['source_id']==v['source_id'] for x in vs);vs.append(v);p.write_text(json.dumps(vs,ensure_ascii=False,indent=2)+'\n')
