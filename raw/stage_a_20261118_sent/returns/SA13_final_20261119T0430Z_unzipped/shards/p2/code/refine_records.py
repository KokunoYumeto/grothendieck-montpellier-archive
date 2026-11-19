#!/usr/bin/env python3
"""Human-authored exact excerpt and source-collation corrections; no verdict inference."""
import json,re
from pathlib import Path
O=Path(__file__).resolve().parents[1]
R=Path(__file__).resolve().parents[4]
A=json.loads((O/'items.json').read_text()); C=json.loads((O/'claims.json').read_text())
q={
102:r'iso si $\unsure{\underline{D}|D}_Y(G_\bullet)$ à ch.\ const.',
103:"montrer que c'est un isomorphisme",106:'la résolution des singularités à la Hironaka est possible',
111:r'il faut accoupler les deuxièmes mb.',113:r'u_*u^!(\mathrm{pr}_2^!(G))',117:'Consulter notes de Verdier',120:'Dualité analytique',
123:r'F_\bullet\in\operatorname{Ob}D^b(X)',125:"Pour l'implication inverse, utiliser la bidualité",126:r'\exists N\text{ tel que }',
129:r'\operatorname{Ext}^i(F,\unsure{G|C})=0',130:'se ramène par passage à la limite',131:'Attention, est-il vrai que',
134:r'\operatorname{Ext}^{2d}(F,\unsure{C|G})',135:r'\operatorname{Supp}\operatorname{Ext}^{-q}(\unsure{C|G},A_X)',136:'parfaite ??',
137:r'F\longrightarrow DDF',138:r'\text{loc.Inj-dim}^{*}\ D(F)\text{ comprise par }[-2n+N,M]',
140:r'Généralités, \inserted{le} th. de monodromie par voie arithmétique.',141:r'est un module de t.f. sur $\mathbb Z_\ell$',
143:r'H^1(X_{\bar K},\mathbb Z_\ell(1))',144:'nous verrons que la connaissance',146:r'une surface de degré $\geq4$',
147:r'\operatorname{Pic}(\mathbb P^3)\xrightarrow{\sim}\operatorname{Pic}(X_0)',148:'foncteurs fibre',149:r'Sa puiss. tensorielle',
150:r"l'étude des représentations $\ell$-adiques du groupe d'inertie",151:r'\deleted{toute} \inserted{parfois}',
152:r'I_t\simeq\prod_{\ell\ne p}\mathbb Z_\ell(1)',153:r'\uline{modérément ramifiée}',154:r'\operatorname{Gal}((\varinjlim_n K_n)/K)',
156:r"\operatorname{Gal}(\bar K'/K)=\pi'",157:r"\lambda^n=u'",158:r'multiplication par $e$',159:r'et $V$ excellent',160:r'ext. finie sép. $K_1/K$',
162:r"Il s'impose \unsure{de} vérifier",163:r'facteur inséparable $p^s$',165:r'une extension \uline{centrale}',
167:r'Généralités, \inserted{le} th. de monodromie par voie arithmétique.',169:r'F\inserted{\longrightarrow}i_{X\inserted{*}}i_X^{\inserted{*}}F',
170:r'qui sera démontré dans le \S\ 3',171:r'aurait la cohomologie nulle en dimension $\inserted{>}0$',174:r"s'assurer qu'on a bien mis",175:r'la conjecture de la l.\ 9 est fausse',
176:r'en utilisant un sous-espace partout dense bien choisi de $H$',178:r"l'application $(x,y)\mapsto x+y$ de $C\times C$ dans $F$ est propre",179:"vérifier qu'on ne s'en sert pas",
180:r'séparante en $F$',182:r'Si les $G_i$ sont fermés',184:r'$M^qR=\bar M^q$',185:r'any completion of $\bar R$ is also a completion of $R$',
186:r'F\deleted{f}ollows from Lemmas 9 and 10 by induction',188:r'is an epimorphism whose kernel is $\mathcal{F}$',190:r'$KJ=Kf$',
193:r'il faut pouvoir dire que $E$ est la limite inductive des $E_n$',195:r'le topos associé ) est beaucoup plus intrinsèque',196:'Sujets de recherches',
198:'Verdier',200:"montrer que c'est un isomorphisme",201:r"Il s'impose \unsure{de} vérifier",202:'On pourra aussi regarder',203:r'qui sera démontré dans le \S\ 3',
204:'Lemme fondamental de Verdier',205:r'\ell\neq\operatorname{car}k',206:r'la conjecture de la l.\ 9 est fausse',207:'JAN-ERIK ROOS'
}
for x in A:
 n=int(x['id'].split('-')[-1])
 if n in q:x['his_words']=q[n]
# Exact anchor in the second supplied locus is retained with its correct page.
for x in A:
 if x['id']=='SA13-147' and not any(z['scan']==6 for z in x['lines']):x['lines'].append(dict(file='pro/MPL_33_147-181+34_002-017_transcription.tex',cote=34,scan=6,start=1112,end=1116));x['scans'].append('34:006')
 if x['id']=='SA13-148':x['his_words']='foncteurs'
 if x['id']=='SA13-204':x['his_words']='Verdier'
M={x['id']:x for x in A}; cm={int(x['id'].split('-')[-1]):x for x in C}
for x in C:
 if x['items'] and int(x['id'].split('-')[-1])<168:x['his_statement']=M[x['items'][0]]['his_words']
cm[105]['items']=['SA13-111'];cm[105]['lines']=M['SA13-111']['lines'];cm[105]['scans']=M['SA13-111']['scans']
cm[116].update(modern_statement='With ordinary algebraic codimension, the literal estimate codim Supp Ext^r(C,Λ_X)≥r is false: on a smooth curve X over an algebraically closed field, for i:{x}→X and invertible Λ=Z/ℓ, internal Ext²(i_*Λ,Λ_X)=i_*Λ(−1) has support of codimension1. Shifted dualizing or half-degree conventions give different estimates.', literature_fate='The purity test refutes the ordinary-codimension interpretation of the margin, not every possible normalization. Smooth purity is stated in Milne16.7; the doubtful codimension word and degree convention must be read on the scan.',reconstruction='The counterexample is X=A¹, Z={0}, ℓ prime to the characteristic. Ri!Λ=Λ(−1)[−2] gives the nonzero internal Ext². This is the earlier notes’ diagnostic, not an independent theorem attributed to Grothendieck.',authorship='Earlier-run diagnostic of Grothendieck margin, rechecked here')
cm[127].update(literature_fate='Ramis–Ruget1970, Théorème1, constructs analytic duality for coherent sheaves with the required separated topological quotients. This establishes a substantial branch of the programme; the short manuscript list does not specify one theorem exhausted by this result.',references=['RamisRuget1970:Théorème1,printedp81'],confidence='medium')
cm[130].update(modern_statement='For X a scheme, the draft asserts that the least full U-topos of presheaves on Sch/X satisfying (A) invariance under affine morphisms inducing underlying homeomorphisms and (B) filtered affine inverse-limit continuity, and containing all representables satisfying both, is Sh(X_Zar). It reduces this to the deferred lemma: a representable Y/X satisfies(A),(B) iff Y→X is a local isomorphism.',classification='C',literature_fate='SGA4VII introduction identifies the Roos oral source family; VII4.1 proves the analogous small/big étale comparison. The exact stronger minimum-topos/representable criterion in this Roos typescript was not collated with a published theorem. Its completed étalé-space construction and its deferred representability lemma remain separate.',references=['SGA4VII:introduction,4.1; exact draft criterion not collated'],confidence='medium')
cm[149].update(modern_statement='For an open normal subgroup I′ of inertia I, let P′=ker(I′→I′_t). Then P′ is characteristic in I′, and 1→I′_t→I/P′→I/I′→1 is a central extension. This asserts centrality inside inertia, not centrality under all of G_K.',literature_fate='The canonical tame character is equivariant; inertia has trivial cyclotomic action, so conjugation by I on I′_t is trivial. This gives the manuscript corollary. Centrality does not imply splitting: for K=C((t)) and I′=mI, the resulting extension of Z/m by mZhat has no group section.',reconstruction='Pass to the strictly henselian trait to treat I as its absolute Galois group, then use the canonical Tate-twist identification for I′. In the example a section would produce a nonzero finite-order element of torsion-free Zhat.')
cm[161]['his_statement']=r'evaluating these integrals (see [18a])'
cm[161]['lines']=[dict(file='pro/MPL_33_147-181+34_002-017_transcription.tex',cote=33,scan=177,start=851,end=858)];cm[161]['scans']=['33:177']
qc={174:r'E^U=E^{G^\circ}',175:r'\text{pour }i\geq0',179:r'G\simeq G^\circ\times\Gamma',191:r'Comme $f_\alpha$ est propre',215:'Le cas de la car résiduelle',219:r'H_{\deleted{\unsure{1}}}^1',226:r'\pi_1(\mathbb F_p)\simeq\widehat{\mathbb Z}',230:r'\uline{il est} plausible'}
for n,v in qc.items():cm[n]['his_statement']=v
for n in [203,204,209,210,229]:
 x=cm[n]
 x['references']=[v.replace('DeligneWeilII:3.4.1','DeligneWeilII:3.4.1(iii),3.4.12–13') for v in x['references']]
 x['literature_fate']=x['literature_fate'].replace('WeilII3.4.1 (1980','WeilII Corollary3.4.13, printedp210 (1980')
cm[210]['reconstruction']='The original Numdam PDF was opened and downloaded; its printedpp207–210 were read. Theorem3.4.1(iii) is the finite-field pure-lisse statement; Corollary3.4.13 is the exact smooth-proper, normal-connected geometric-base conclusion.'
cm[207]['references']=[v.replace('6.13–6.14','6.13,7.12') for v in cm[207]['references']]
cm[214].update(reconstruction='A concrete trait counterexample is R=W(overline F_5), K=Frac(R). Choose an ordinary elliptic curve over overline F_5 and its Serre–Tate lift with parameter q=1+5. Katz2.1 gives the connected–étale p-divisible extension. Its rational Tate extension 0→Q5(1)→V5(E)→Q5→0 is the nonzero Kummer class of q. The 5-adic logarithm has valuation1, so q cannot become infinitely5-divisible in K; no power of its Kummer class vanishes. Since the residue field is algebraically closed, G_K=I. Thus the good-reduction representation is not semisimple on inertia. Passage from compatible Artin lifts to the elliptic scheme uses the usual algebraization of polarized abelian deformations.',references=['Katz1981:Theorem2.1 and extension construction,printedpp148–153','BrinonConrad2009:8.3.6–8.3.7; compatible nonsplit crystalline examples'],confidence='high')
cm[195]['lines']+= [dict(file='codex/K34-03_transcription.tex',cote=34,scan=50,start=2,end=33)]
cm[195]['scans'].append('34:050')
# Theorem1.1 was not separately opened; abstract comparison only.
cm[141]['references']=['Ji2024:opened abstract; no exact-text theorem collation']
for x in C:
 x['statement']=x['modern_statement'];x['status_on_pages']=x['page_status'];x['class']=x['classification'];x['fate']=x['literature_fate'];x['present_status']=x['literature_fate'];x['refs']=list(dict.fromkeys(s.split(':')[0] for s in x['references']));x['computation']=x['computations']
(O/'items.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
(O/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
norm=lambda s:re.sub(r'\s+',' ',s).strip()
bad=[]
for coll,field in [(A,'his_words'),(C,'his_statement')]:
 for x in coll:
  if not x[field]:continue
  txt='\n'.join('\n'.join((R/'sources/texts'/z['file']).read_text().splitlines()[z['start']-1:z['end']]) for z in x['lines'])
  if norm(x[field]) not in norm(txt):bad.append((x['id'],x[field]))
print('Exact-excerpt mismatches remaining:',bad)
print('Saved primary-collation and mathematical corrections, without changing source transcriptions.')
