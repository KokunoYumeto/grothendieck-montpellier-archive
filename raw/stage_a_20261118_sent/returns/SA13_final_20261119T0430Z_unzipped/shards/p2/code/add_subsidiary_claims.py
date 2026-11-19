#!/usr/bin/env python3
"""Additional literal subsidiary EVT statements, individually reviewed rather than inferred from headings."""
import json,copy
from pathlib import Path
O=Path(__file__).resolve().parents[1]
C=[x for x in json.loads((O/'claims.json').read_text()) if not 231 <= int(x['id'].split('-')[-1]) <= 240]; cm={int(x['id'].split('-')[-1]):x for x in C}
F='pro/MPL_33_147-181+34_002-017_transcription.tex'
def add(n,title,scan,a,b,quote,st,status,cl,proof):
 x=copy.deepcopy(cm[150]);x.update(id=f'C-SA13-{n}',title=title,items=[],cote=[33],scans=[f'33:{scan:03d}'],lines=[dict(file=F,cote=33,scan=scan,start=a,end=b)],his_statement=quote,modern_statement=st,page_status=status,classification=cl,reconstruction=proof,literature_fate='Standard convexity/topological-vector-space mathematics in the reconstructed scope; exact reused source/edition remains uncollated after the EVT/Bourbaki searches. '+('No complete original theorem is identifiable from the cropped text.' if cl=='F' else 'The mathematical argument is independently checked in this review.'),computations=[],authorship='Reused EVT editorial typescript; individual author and edition unresolved')
 for k,v in [('statement','modern_statement'),('status_on_pages','page_status'),('class','classification'),('fate','literature_fate'),('present_status','literature_fate'),('computation','computations')]:x[k]=x[v]
 C.append(x)
# Refine the location of the already recorded extreme-fibre lemma.
cm[150]['lines']=[dict(file=F,cote=33,scan=155,start=235,end=235)]
cm[150]['his_statement']=r'alors $y$ est extrémal dans $C$'
add(231,'Separation determines a closed convex set',155,245,245,r'Donc $B=A$',
'If A and B are closed convex subsets of a Hausdorff locally convex space and every continuous affine functional nonnegative onB is nonnegative onA, thenA⊂B. Equality also needsB⊂A, supplied by the missing old theorem context.',
'proof sketched','F','If a∈A\\B, Hahn–Banach separation supplies a continuous affine functional nonnegative onB and negative ata. The claimed equality cannot be obtained from this direction alone without the other inclusion.')
add(232,'Extreme points and removal from a convex set',157,310,316,r'$A-\{x\}$ convexe',
'For a convex setA andx∈A, x is an extreme point iffA\\{x} is convex.',
'stated without proof','E','If a nontrivial segment between two points other thanx containsx, removal is not convex; conversely failure of convexity ofA\\{x} forces precisely such a segment.')
add(233,'Slices and a compact generating subset',155,247,249,r'\overline{\Gamma(K)}\neq A',
'For compact convexA in a Hausdorff locally convex space, slices containing an extreme pointx form a neighbourhood basis atx. Thus if compactK⊂A omitsx, its closed convex hull omits a slice nearx and is not allA.',
'proof sketched','E','For a neighbourhoodU ofx, cover compactA\\U by finitely many separating halfspaces avoidingx; the compact convex hull of the resulting excluded compact pieces does not contain extreme x. Separate that hull fromx. Compactness ofK is essential: a dense nonclosedK may omitx while generatingA.')
add(234,'Extreme rays characterized by decompositions',155,253,257,r'ceci caractérise les génératrices extrémales',
'For a pointed convex coneC and rayD⊂C, D is an extreme ray iff every decompositionx=y+z ofx∈D withy,z∈C hasy,z∈D.',
'stated without proof','E','Scale any convex decomposition of a nonzero ray point to a sum; conversely divide a sum by2. Pointedness excludes an entire line masquerading as an extreme ray.')
add(235,'Locally compact union of compact sets',157,301,301,r'Donc $C$ est fermé et localement compact',
'LetC=∪C_n⊂E, eachC_n compact, E Hausdorff topological vector space. If a fixed closed zero-neighbourhoodV satisfies(x+V)∩C⊂C_n for some n depending on everyx∈E, thenC is closed, locally compact and complete.',
'proof sketched','E','Near each ambientx, C lies in a compact closedC_n, soC is closed and locally compact. A Cauchy filter has a member contained inx+V for somex∈C; its tail lies in compactC_n and converges. The proof does not assume an arbitrary Cauchy net has bounded range.')
add(236,'Lower-semicontinuity and a closed set',168,607,607,r'$A$ est fermé parce que $f$ est sci',
'For a lower semicontinuous real extended-valued functionf, every sublevel set{f≤a} and the epigraph are closed in the appropriate topology. The fragment does not defineA, so its exact closed-set claim is conditional on that identification.',
'stated without proof','F','A sublevel is the complement of the open superlevel{f>a}; the generalA in the old example cannot be recovered.')
add(237,'Continuous dual separates a Hausdorff locally convex space',168,625,625,r'cette dualité est séparante en $E$',
'The evaluation pairingE×E′ is always separating onE′; ifE is Hausdorff locally convex overR orC it is also separating onE, by Hahn–Banach.',
'stated without proof','E','For nonzero x choose a continuous seminormp withp(x)>0 and extend the functional onspan{x} by Hahn–Banach. Nonzero f∈E′ is nonzero on some vector by definition.')
add(238,'Inductive limit as quotient of a locally convex sum',171,698,702,r'Une limite inductive est quotient',
'A locally convex inductive limit is the quotient of the locally convex direct sum of its objects by the subspace generated by the transition relations; in the Hausdorff category take the closure of that subspace.',
'stated without proof','E','Linear maps from this quotient correspond exactly to compatible families of continuous maps from the system objects. This universal property gives the stated inductive limit; quotient may be non-Hausdorff unless separated.')
add(239,'Direct-sum product map and closed coordinate subspaces',171,702,710,r"L'injection canonique de $E$ dans $\prod E_i$ est continue",
'The canonical map⊕E_i→∏E_i is continuous and for finiteI is a topological isomorphism. For closedG_i⊂E_i, ⊕G_i is closed in⊕E_i.',
'proved there','E','Each projection is continuous by the sum universal property; finite sums and products have the same topology. The subspace⊕G_i equals∩p_i^{-1}(G_i).')
add(240,'Countable box-neighbourhood construction fragment',168,599,599,r'On construit par récurrence des intervalles',
'The fragment constructs compact intervals[a_n,b_n] with finite products insideU∩R^n. The assumptions onU and compatibility of embeddings are missing, so no general final-topology theorem is asserted.',
'proof sketched','F','Finite-stage compactness can justify extension to the next coordinate whenU is suitably open along the existing compact box, but the complete source hypotheses are unavailable.')
for x in C:
 x['refs']=list(dict.fromkeys(s.split(':')[0] for s in x['references']))
(O/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(C),'claims; added C-SA13-231..240 and corrected C-SA13-150 locator.')
