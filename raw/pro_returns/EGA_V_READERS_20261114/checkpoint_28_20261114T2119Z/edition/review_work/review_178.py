import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\scanpage{25/178}',r'\scanpage{25/178}'+'\n'+r'\mspage{\hand{\unsure{5}}}'+'\n% NOTE: The upper-right pencil mark is faint; its reading as a folio5 remains uncertain.','The upper-right margin contains a faint pencil mark omitted by the draft. A5 is possible from its angled top and lower curved remnant, but neither the digit nor its folio role is fully secure.'),
(r'\overset{\hand{$\sim$}}{d}',r'\overset{\hand{\sim}}{d}','Both tildes are handwritten above the typed d; the encoding now places them in the existing math context.'),
(r'Q \in',r'Q \hand{\in}','The membership sign in the corollary is handwritten.'),
(r'\neq',r'\hand{\neq}','The not-equal sign in condition (ii) is drawn in pen.'),
(r'Q\otimes',r'Q\hand{\otimes}','The tensor sign before k-prime is handwritten.'),
(r'\longrightarrow (\mathrm{Ens})',r'\hand{\longrightarrow} (\mathrm{Ens})','The arrow in the displayed functor has a hand-drawn shaft and head.'),
(r"\to \underline{E}_{S'}",r"\hand{\to} \underline{E}_{S'}",'The arrow between the two base-changed Modules is pen.'),
(r'\inserted{$\underline{E}$ \unsure{ni}}',r'\inserted{$\underline{E}$ ni}','The inserted underlined E and ni are legible in pen; the dot of i is separate and clear.'),
(r'\inserted[typed]{sous-}\deleted{pré}',r'\inserted[typed]{sous-}\unsure{pré}','Sous- is typed. The only pen stroke is continuous with its curved insertion leader and crosses pré; an independent cancellation is not established. The status of pré remains uncertain instead of being silently deleted.'),
(r'de W \unsure{/}',r'de W \hand{/}.','A pen slash crosses beside a separate typed period after W; both marks are visible.'),
(r'\xout{\unsure{$\underline{G}(\underline{E}_o$}x}',r'\xout{\unsure{$\underline{G}(\underline{E}$}x}\hand{$_{\unsure{Q|o}}$}','The baseline G(E-like group is obscured by typed x marks and remains uncertain. A large lower pen loop with a rightward tail is separately visible below its end; Q/o and its exact attachment remain uncertain, and it is not swallowed into a confidently cancelled typed subscript.')
]
D={
10:'The tilde and not-equal sign are pen; the final0 and period are typed.',
12:'Finie is fully legible under type x cancellation. The tensor sign in Q tensor k-prime is pen.',
21:'The cancelled phrase a évidemment is fully readable; the following peut évidemment is live.',
23:'Both implication arrows in the displayed chain are handwritten, with separate shafts and arrowheads.',
25:'The implication and equivalence arrows are handwritten; their directions are as transcribed.',
32:'The interlinear underlined E and ni are legible handwriting. Their curved leader inserts them after sur and before Q.',
33:'Sous- is typewritten. The single curving leader runs across the top of pré, leaving the proposed deletion of pré uncertain; the letters themselves are clear.',
34:'The cancelled Isom(E group is legible with a pen strike across it and the original underline beneath Isom. The final E is darkened but still recognizable.',
35:'The separate typed period and pen slash after W are both retained. The implication arrow is handwritten. The second Module visibly has subscript1 and is not changed to an unindexed E.',
36:'The tilde above d is handwritten; fidélement retains its typed accent.',
39:'The final cancelled baseline is G(E-like but remains uncertain through the x marks. Its lower pen loop is recorded separately as Q/o with unresolved attachment and cancellation status.',
41:'The lower-left archive178 is handwritten.'
}
N=[
'Both tildes are clearly pen above their typed d characters.',
'All implication and equivalence arrows are pen; the functor arrow and the Module-isomorphism arrow are also pen and have been marked.',
'The inserted underlined E and ni are fully legible handwriting.',
'Sous- is typed. The sole curved pen line is its insertion leader; whether it also cancels pré is unresolved, and the checked text preserves that uncertainty.',
'The visible pen slash and the separate typed period are both represented.',
'The baseline G(E-like group remains uncertain under typed x cancellation. The large lower loop is pen, possibly Q or o, and its attachment/status remains uncertain.',
'The Isom(E text is legible beneath the pen cancellation; its original underline is retained.',
'No long marginal handwriting occurs. The faint omitted upper-right mark and the lower archive number, all insertion leaders and every short handwritten symbol were inspected.'
]
extra=[
dict(line=35,before=r'\underline{E}_1',image=r'\underline{E}_1',decision='retained',reason='The lower-right character is visibly1; no replacement by the earlier unindexed E is made.',category='literal-formula'),
dict(line=5,before='dimensionfinie',image='dimensionfinie',decision='retained',reason='The two printed words run together in the scan.',category='literal-spacing'),
dict(line=30,before='est formé',image='est formé',decision='retained',reason='The scan has the masculine form without a final e.',category='literal-spelling')
]
print(len(complete('ega25_25_178',R,D,N,extra)['decisions']))
