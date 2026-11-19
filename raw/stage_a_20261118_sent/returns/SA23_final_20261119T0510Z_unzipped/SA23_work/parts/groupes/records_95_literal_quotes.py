"""Manually selected literal excerpts from the already fully read passages.

Line selections were made after inspecting their content, not by a heading or
keyword rule. This code only copies the selections and verifies provenance.
The previous English gloss remains separately available as source_paraphrase.
"""
import re

# Two citation ranges were too narrow for their explicitly discussed clauses.
for c in claims:
    if c['id']=='C-SA23-groupes-014':c['lines'].append(f'{source_file("1")}:558–575')
    if c['id']=='C-SA23-groupes-019':c['lines'].append(f'{source_file("1")}:704–707')
    if c['id']=='C-SA23-groupes-061':c['lines'].append(f'{source_file(4)}:104–117')
    if c['id']=='C-SA23-groupes-076':c['lines'].append(f'{source_file(5)}:15–39')
for p in problems:
    if p['id']=='MP-SA23-groupes-29':
        p['occurrences'].append(occurrence(4,[53],'104–117','module-property list, including the explicit injectivity question'))

# n: (source part, one or more inclusive physical-line intervals)
selections={
 1:('1',[(39,40)]),2:('1',[(43,43)]),3:('1',[(32,32)]),4:('1',[(69,69)]),
 5:('1',[(223,223)]),6:('1',[(256,256)]),7:('1',[(291,291)]),8:('1',[(355,355)]),
 9:('1',[(409,409)]),10:('1',[(423,423)]),11:('1',[(444,444)]),12:('1',[(506,506)]),
 13:('1',[(553,553)]),14:('1',[(568,568)]),15:('1',[(571,571)]),16:('1',[(609,609)]),
 17:('1',[(621,624)]),18:('1',[(660,660)]),19:('1',[(707,707)]),20:('1',[(716,716)]),21:('1',[(725,725)]),
 22:(1,[(13,16)]),23:(1,[(102,109)]),24:(1,[(327,327)]),25:(2,[(532,535)]),
 26:(2,[(61,61)]),27:(2,[(168,168)]),28:(2,[(73,73)]),29:(1,[(524,524)]),
 30:(2,[(224,224)]),31:(2,[(251,254)]),32:(2,[(268,271)]),33:(2,[(277,277)]),
 34:(2,[(153,153)]),35:(2,[(615,615)]),36:(2,[(743,743),(754,757)]),37:(2,[(778,780)]),
 38:(3,[(249,250)]),39:(3,[(34,34)]),40:(3,[(273,275)]),41:(3,[(255,255)]),
 42:(3,[(277,277)]),43:(3,[(334,335)]),44:(3,[(359,359)]),45:(3,[(371,371)]),
 46:(3,[(469,470)]),47:(3,[(466,468)]),48:(3,[(489,490)]),49:(3,[(600,600)]),
 50:(3,[(608,608)]),51:(3,[(753,753)]),52:(3,[(639,643)]),53:(3,[(678,682)]),
 54:(3,[(776,776)]),55:(3,[(817,819)]),56:(3,[(832,834)]),57:(4,[(10,10)]),
 58:(4,[(4,4)]),59:(4,[(19,19)]),60:(4,[(54,54)]),61:(4,[(114,114)]),62:(4,[(87,87)]),
 63:(4,[(96,96)]),64:(4,[(122,122)]),65:(4,[(139,143)]),66:(4,[(160,163)]),
 67:(4,[(172,172)]),68:(4,[(402,402)]),69:(4,[(433,433)]),70:(4,[(300,300)]),
 71:(4,[(353,353)]),72:(4,[(351,351)]),73:(4,[(180,184)]),74:(4,[(365,365)]),
 75:(5,[(11,13)]),76:(5,[(35,35)]),77:(5,[(58,58)]),78:(5,[(89,89)]),79:(5,[(114,114)]),
 80:(5,[(119,121)]),81:(5,[(132,132)]),82:(5,[(193,195)]),83:(5,[(308,308)]),
 84:(5,[(336,336)]),85:(5,[(339,339)]),86:(6,[(41,45)]),87:(6,[(51,51)]),
 88:(6,[(85,88)]),89:(6,[(138,138)]),90:(6,[(183,185)]),91:(6,[(310,314)]),
 92:(6,[(312,312)]),93:(6,[(337,337)]),94:(6,[(372,375)]),95:(6,[(395,399)]),
 96:(6,[(419,419)]),97:(6,[(426,428)]),98:(7,[(3,9)]),99:(6,[(471,472)]),
 100:(7,[(13,15)]),101:(7,[(309,315)]),102:(7,[(355,358)]),103:(7,[(360,365)]),
 104:(7,[(576,585),(593,595)]),105:(7,[(613,618)]),106:(7,[(678,684)]),
 107:(7,[(709,711)]),108:(6,[(339,339)]),109:(3,[(124,128)]),110:(2,[(174,174)]),
 111:(2,[(541,543)]),112:(6,[(19,21)]),113:(7,[(719,721),(725,725)]),114:(4,[(506,507)]),
}

# Explicit short fragments within selected long lines. Every fragment is checked
# against the source verbatim, including any deletion or uncertainty markup.
fragments={
 3:[r"il suffit que $\forall Y\in\operatorname{Ob}E'$ \deleted{\unsure{on ait}}, $i(Y):\deleted{\unsure{soit}}Y\to vu(Y)$ soit \deleted{\unsure{un isom.}}\inserted{un mono} (resp. un \uline{\unsure{isom|mono}}). C'est aussi nécessaire si on sait que $vu(E')\subset\overline{E'}$"],
 6:[r"Un foncteur $\psi:E_1^{\circ}\to(\mathrm{Ens})$ tel que $\psi\circ\alpha'$ est rep, est-il représentable ?"],
 7:[r"d'une bijection $\tau:I\to J$ et d'isom. $\varphi_i:L_i\xrightarrow{\sim}M_{\tau(i)}$"],
 8:[r"la donnée d'une structure $\unsure{\mathrm{AUC}|\mathrm{ANC}}$ sur celle-ci est \unsure{équivalent|équivalente} à la donnée d'un foncteur $\Pi:\Phi(e)\to C$"],
 10:[r"le passage d'un isom. de $\Pi L_i$ avec $L^{\otimes n}$ à un autre, via une permutation $\sigma$ de $[1,n]$, se fait par $\varepsilon(L)^{\operatorname{sign}(\sigma)}$"],
 13:[r"\uline{Mais c'est tjrs faux}"],
 15:[r"Donc si $\bar\varphi$ est exact à g, $E$ est un topos."],
 19:[r"Donc on trouve que $\beta':\underline{\operatorname{Hom}}'(E,F)\to\underline{\operatorname{Hom}}'(C,F)$ est pleinement fidèle."],
 25:[r"$(*)$ Définition de foncteurs \uline{$\delta$-préexacts} $D.\xrightarrow{u}F$, $D$ muni d'un ens $\delta=(\delta',\delta'')$ de cônes...."],
 26:[r"Si on veut seulement montrer que \deleted{les} topos $R$ est ``algébrique'' c'est encore plus court"],
 29:[r"Or ceci caractérise les morphismes de topos $R'-R$ qui sont des plongements."],
 53:[r"p\,1_A=0,\qquad A\xrightarrow{x\mapsto x^p}A\quad\text{isom}",r"\margin{en car. $0$, on convient que parfait signifie réduit ?}"],
 54:[r"le plus grand ouvert de $\mathcal E$ \deleted{sur lequel} \inserted{tel que} $f$ t. $\mathcal E_{/e'}$ se factorise par \unsure{$V$|$0$}"],
 55:[r"on sait que $V$ est déjà un ouvert de $B=\widehat R$",r"Donc \uuline{OK}"],
 58:[r"Il n'est pas clair cependant que la formation des $e'_n$ commute aux chgt de topos de base $E'\mathbin{-}E$"],
 60:[r"$M$ \uuline{fid} \uline{plat}\\est-ce typique?"],
 63:[r"Une condition nécessaire pour qu' \deleted{\unsure{A soit un}} un Anneau se plonge \unsure{$\to X$|$X'\to X$} dans un corps, c'est que la section nulle (donc tte autre section) soit \unsure{sommande|sommante} direct de $A$, et c'est sans doute suffisant"],
 68:[r"\margin{Peut-on avoir $\operatorname{Fil}^{\pi'}(E)\ne E_{\pi'}$ ?}"],
 70:[r"p.ex. $C$ stable par $\varprojlim$ finies et $\varphi$ exact à g"],
 71:[r"les seuls objets accessibles sont les ensembles ponctuels !"],
 72:[r"Une catégorie satisfaisant les conditions a) est-elle \uline{accessible}, i.e. ses éléments sont ils accessibles ?"],
 76:[r"Si $C\longrightarrow C'$ dans $\Delta$ est pl. fidèle (resp. fid) alors $T(C)\longrightarrow T(C')$ l'est aussi (pour $T$ 2-repr.)."],
 78:[r"Les théories Algébriques sont exactement celles qui sont représentées par des \uline{petites} catégories."],
 80:[r"Mais alors on voit tout de suite que les produits de $C$ sont des produits de $C\Sigma^{-1}$. OK !",r"\margin{Mais il faut \deleted{Si $C$ est} vérifier que la catégorie obtenue est une $\mathcal U$-catégorie.}"],
 81:[r"Les théories algébriques pour $\Delta$ sont celles qui sont 2-représentées par des $R\in\mathrm{Ob}\,\Delta$ admettant des \uline{petites familles \inserted{str.} cogénératrices}."],
 82:[r"\margin{Pb 1 et Pb $1'$ Cela marche pour \uline{tout} ens. $d'$ de petits diagrammes (pas néc. finis)}"],
 85:[r"Comment trouver \inserted{toutes} les $\Sigma$ qui marchent"],
 90:[r"\margin{il faut aussi prévoir les axiomes du type ``flèches rendues égales'' (en réalité, \unsure{un des|cas des|pas des} précédents si on suppose p.ex. $d'=d''=\varnothing$)}"],
 91:[r"Alors pour $\alpha$ assez grand \inserted{(dans l'univers $\mathcal U$)}, on a $R_\alpha\xrightarrow{\simeq}R$."],
 92:[r"cel implique que les foncteurs $R_\alpha$ sont \deleted{pl. fidèl} \uline{fidèles}, donc les $R_\alpha$ sont des sous-catégories."],
 96:[r"$\mathbb Z[t]\longrightarrow\mathbb Z[t,t^{-1}]\times\mathbb Z\simeq\mathbb Z[x,y]/((xy-1)x,(xy-1)y)$",r"La réciproque est vraie, \inserted{et connue}"],
}

root=BASE.parents[2]
assert set(selections)==set(range(1,115))
quote_audit=[]
for c in claims:
    n=int(c['id'].rsplit('-',1)[1]);part,spans=selections[n];fn=source_file(part)
    source=(root/fn).read_text().splitlines()
    selected='\n'.join('\n'.join(source[a-1:b]) for a,b in spans)
    if n in fragments:
        for fragment in fragments[n]:assert fragment in selected,(n,fragment,selected)
        excerpts=fragments[n]
    else:
        excerpts=['\n'.join(source[a-1:b]).strip() for a,b in spans]
    c['source_paraphrase']=c['his_statement']
    c['his_statement']=' […] '.join(excerpts)
    c['source_quotations']=[dict(file=fn,physical_lines=';'.join(f'{a}–{b}' if a!=b else str(a) for a,b in spans),literal_excerpt=t) for t in excerpts]
    c['quotation_note']='Literal excerpt of the supplied transcription, not an ink adjudication. Deletions, insertions and competing readings are retained. source_paraphrase is the earlier English gloss.'
    quote_audit.append(dict(id=c['id'],source_file=fn,selected_lines=spans,literal_fragments=excerpts))

# One selected claim excerpt supplies each consolidated subject’s literal words.
item_quotes={901:1,902:10,903:14,904:16,905:18,906:22,907:29,908:30,909:36,910:38,911:46,912:51,913:56,914:59,915:66,916:72,917:68,918:75,919:82,920:83,921:87,922:96,923:101,924:104,925:105,926:107,927:111}
for i in items:
    n=int(i['id'].split('-')[-1]);c=claims[item_quotes[n]-1]
    i['source_paraphrase']=i['his_words'];i['his_words']=c['his_statement'];i['source_quotations']=c['source_quotations']
(BASE/'quotation_audit.json').write_text(json.dumps(quote_audit,ensure_ascii=False,indent=2)+'\n')
