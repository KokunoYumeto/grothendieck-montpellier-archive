from review_root import review
from pathlib import Path
k='ps_134-2_065'
up=r'\tikz{\draw[->] (1,0)--(.15,0)--(.15,1);}'
espace=r'\tikz[baseline=(x.base)]{\node[draw,ellipse,inner sep=2pt] (x) {espace};}'
app=r'\tikz[baseline=(x.base)]{\node (x) {(App.13)};\draw[->] (-.5,-.35) .. controls (.1,-.7) and (.8,-.4) .. (1.05,-.1);}'
down=r'\tikz{\draw[->] (1,.8)--(.25,.8)--(.25,-.8);}'
review(k,changes=[
(r'\mspage{- 50 -}',r'\mspage{- \hand{5}0 -}','The live5 is handwritten or retraced in pen; no independently readable earlier digit is asserted. The0 and hyphens are typed.'),
(r'\arrow[dl]',r'\arrow[dl,color=blue]','The downward-left diagram arrow is drawn by hand; its typed objects remain plain.'),
(r'\arrow[rr]',r'\arrow[rr,color=blue]','The horizontal diagram arrow is handwritten.'),
(r'\arrow[ul]',r'\arrow[ul,color=blue]','The upward-left diagram arrow is handwritten.'),
(r'\margin{bracket with an upward arrow from this line to the next}',r'\margin{\hand{'+up+r'}}','Replace descriptive editorial prose by the actual upward bent pen arrow.'),
(r'\margin{(espace)}\uline{now to say}',r'\margin{\hand{'+espace+r'}}\uline{now} to say','The source has a circled espace, and the horizontal stroke runs only under now, not the following to say.'),
(r'\qquad * \qquad * \qquad *',r'\hand{$*\qquad *\qquad *$}','The three stars are handwritten.'),
(r'\margin{(App. 13)}',r'\margin{\hand{'+app+r'}}','The marginal App.13 and the curved arrow linking it to the heading are handwritten.'),
(r'\uline{\over{(E)}{\unsure{(App 13)}} \deleted{Local}\inserted{((E) Local} class field\deleted{s} \inserted{(theory} as a duality formula}',r'\over{\unsure{(E)}}{\unsure{(App 13)}} \uline{\deleted{Local}\inserted{(E) Local} class field\deleted{s} \inserted{theory} as a duality formula}','The first arcs before(E) Local and theory are insertion curves, not additional opening parentheses. The old label lies outside the long heading underline, and its covered(E) is now marked doubtful.'),
(r'\margin{curved arrow from the margin note (App. 13) to this line; vertical double arrow from the heading line to the next line}',r'\margin{\hand{'+down+r'}}','Replace the descriptive prose by the long downward spacing arrow; the separate curved placement arrow is retained with App.13.'),
(r'\margin{w/}',r'\margin{\hand{w/}}','The reminder w/ is pale pencil handwriting.'),
(r'\margin{65}',r'\margin{\hand{65}}','The lower-left65 is pencil archive foliation.')
],doubts={'unsure':[
(r'\unsure{(App 13)}','doubt retained','The retraced section label overlaps the earlier typed label; the individual middle strokes cannot all be separated.'),
(r'\unsure{ss}','doubt retained','The letters beneath the live pen w are too thickly covered to establish both s letters independently.')
],'illegible':[]},notes=[
'The live5 of50 is retouched in pen; no separate older digit can be securely recovered. The lower-left65 is pencil archive foliation.',
'The old section-label overprint remains doubtful. The inserted heading reads(E) Local and theory; the extra opening arcs in the initial transcription are placing curves, not literal parentheses. The old typed(E) is also concealed enough to merit a doubt.',
'The new w is clear, but the old ss remains uncertain under its dark strokes.',
'The first displayed functor has a doubled R. The R symbols in the following two displayed identities are plain; the distinction is retained.'
],summary='Both halves and enlarged heading and endowed correction inspected. Preserved all three handwritten diagram arrows, replaced editorial descriptions with the actual spacing and placement graphics, narrowed the now underline, and separated insertion curves from literal heading parentheses. Added uncertainty for the covered old section label while retaining the App13 and ss doubts. The first R is double-struck, the subsequent R symbols plain; the outer lower-case k is visible in the comparison formula.',differences={
1057:('circled handwritten espace and upward bent spacing arrow','our transcription corrected','The source instruction is a circled word and a pen graphic, not literal parentheses or descriptive prose.'),
1058:('no added descriptive heading','the typescript reads as our transcription','The witness supplied heading is not on the image; the actual heading is(E) Local class field theory as a duality formula with its revision layers.'),
1059:('handwritten App.13 label and curved placement arrow','our transcription corrected','The marginal label and its linking curve remain part of the source, while the witness turns the label into a section number.'),
1063:(r'\inserted{ of char. $p>0$}','the typescript reads as our transcription','The handwritten word is abbreviated char.; it is not expanded to characteristic.'),
1066:(r'F\longmapsto\mathbb{R}\underline{\Gamma}_K(F)','the typescript reads as our transcription','The first displayed R has doubled vertical strokes.'),
1067:('isomorphism holds','the typescript reads as our transcription','The source uses singular isomorphism.'),
1068:(r'R\Gamma_k(R\underline{\Gamma}_K(F))','the typescript reads as our transcription','The outer functor visibly has subscript k, omitted by the witness.'),
1069:('This corresponds','the typescript reads as our transcription','The typed verb has its final s.'),
1071:(r'\margin{\hand{w/}}','our transcription corrected','The visible pencil reminder w/ is now marked as handwriting.')
})
k='ps_134-2_066'
review(k,changes=[
(r"$F$\over{\illegible{1}}{\unsure{$'$}}",r"$F$\over{\illegible{1}}{$'$}",'The separate live slanting prime next to the blackened exponent is visible and agrees with the same correction at both G-primes on site63; the old exponent stays unreadable.'),
(r'\hand{and (E)} \inserted{lately.}',r'\hand{and (E) lately.}','Lately continues the handwritten remark on its second line; no distinct insertion caret or directed placing line is visible.'),
(r'\margin{66}',r'\margin{\hand{66}}','The lower-left66 is pencil archive foliation.')
],doubts={'unsure':[(r"$'$",'doubt resolved','The live prime is a separate oblique pen stroke alongside the blackened older exponent; its form matches the two visible G-prime corrections on site63.')],'illegible':[
(r'\illegible{1}','illegibility retained','The old raised character after F is fully blackened.'),
(r'\illegible{1}','illegibility retained','The typed character beneath the live pen6 in SGA6 is not recoverable.')
]},notes=[
'The initial5 of51 is handwritten, while1 and the hyphens are typed.',
'The live prime is now resolved from its separate stroke and the same-page-group comparison with site63; the old exponent remains illegible.',
'The live6 ofSGA6 is legible pen; the earlier character beneath it stays unreadable.',
'The entire remark(d), including lately, is handwritten. The apparent long stroke near may belongs to the descending y; there is no secure directed insertion mark moving lately earlier. Its visible final position is retained.',
'The lower-left66 is pencil archive foliation.'
],summary='Both scan halves inspected. Resolved the live F-prime but retained its blackened old exponent and the unreadable character beneath SGA6. Restored lately as continuous handwriting at the end of remark(d), with no invented transposition. The source’s lower-case k on the left of the opening local-duality formula, capital S on both duality operators in(a), and p=Spec(k) are retained as mathematical slips for the guide. Remarks has no terminal period and did’nt remains literal.',differences={
1072:(r'\uline{Remarks}','the typescript reads as our transcription','The heading is underlined and has no period; the witness adds one.'),
1074:('unequal characteristics','the typescript reads as our transcription','The source has a clear plural s.'),
1075:(r'R\underline{\Gamma}','the typescript reads as our transcription','The underline under Gamma is visible and absent from the witness.'),
1076:(r"$F$\over{\illegible{1}}{$'$}",'our transcription corrected','The separate live prime is legible; the witness leaves F unprimed. The blackened older exponent remains marked.')
})
p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 12:' not in s:
 s+=r'''
\subsection*{Appendix 12: Global duality and geometric class field theory (part D)}
Cote 134-2, sites 62--65 (folios47--50), begins with prime-to-characteristic duality for a smooth separated finite-type scheme of dimension$d$, then asks for its flat-cohomological continuation in characteristic$p$. Curves are the motivating case: cohomology groups with finite coefficients acquire proalgebraic structure, and connected unipotent groups are dualized by Serre's Ext-one construction, while finite étale groups use Pontrjagin duality in degree zero. Combining the two in a suitable derived category suggests the continuous Serre-duality operator$\Delta$; Cartier duality$D$ upstairs and Serre duality downstairs should exchange proper and arbitrary supports, with shift[2] for a curve. This continues parts B--C's geometric class-field programme, and the author says explicitly that the coefficient categories and functors must still be constructed. Site62's example literally contains$\mu_m^{\otimes}$ instead of the preceding$\mu_n^{\otimes d}$; neither the changed index nor the absent exponent is repaired in the readers. Likewise, the opening assertion for an arbitrary sheaf requires the appropriate finiteness and dualizability hypotheses before its claimed perfect cohomology pairings follow. On site63, the displayed shift[2] must govern the surrounding schematic identification of$f^!(\mathbb Q/\mathbb Z)$ with$\mu_\infty$: omitting that shift is not a separate degree-zero identification. Site64 applies Lang's relation between constant-kernel isogenies and rational points over a finite field to obtain the additional shift[1], hence arithmetic duality with total shift[3]. Its$\pi_1^{ar}(J)$ must be read in that stated isogeny sense, not silently identified with the full arithmetic étale fundamental group. The printed$H_!$ has no degree star, and the duplicate closing parenthesis remains literal. The final warning about non-étale coefficients such as$\alpha_p$ introduces formal completion at the boundary in the compact-support triangle on site65; the coefficient formalism and its formal direct-image notation remain part of the proposed construction. The witness changes the live plural ``categories'' to singular on site63, drops the distinctions of italic Ext and the underlined RHom, and changes the lower-case base-field k to capital K twice on site64. These differences matter to the interpretation of the functors and are preserved in the source-based edition. Part E then makes the boundary's local duality problem explicit.

\subsection*{Appendix 13: Local duality and the Greenberg construction (part E)}
Cote 134-2, sites65--66 (folios50--51), starts with a complete discrete valuation ring$V$, fraction field$K$, and residue field$k$, assuming either a coefficient-field lifting or a perfect residue field of positive characteristic. The sought object$R\underline\Gamma_K(F)$ should carry the continuous$k$-algebraic structure suggested by elementary examples and satisfy$R\Gamma_K(F)\simeq R\Gamma_k(R\underline\Gamma_K(F))$. Witt vectors and a cohomological Greenberg functor are proposed as the construction, with$Rj_*$ supplying the first step. This develops the formal-boundary term of part D and predicts a geometric duality shift[1], increased to[2] by Lang's construction when the residue field is finite. Three literal slips at site66 require attention without emendation: the opening formula has$R\Gamma_k(F)$ on the left even though$F$ is on$K$; the inverse-image duality identity uses$D_S$ on both sides although$i^*F$ is on$s$; and the closed point is then called$p=\operatorname{Spec}k$ after the morphism$i:s\to S$ has been introduced. The corresponding types are recovered by reading$K$, $D_s$, and the closed point$s$ in the intended roles, but all three printed readings remain in every reader. The prime-to-residue-characteristic case is presented as already understood, with the mixed-characteristic primary case singled out as subtle. Remark(c) explicitly limits the author's confidence to finite coefficients; the proposed extension to abelian varieties and Neron models, including$H^1(K,F)\simeq\operatorname{Ext}^1(G',\mathbb Q/\mathbb Z)$, is marked with a question mark and ``without any guarantee''. The handwritten prime on the dual abelian scheme$F'$ is visible and restored, whereas the witness drops it; its blackened predecessor stays unreadable. The source also distinguishes the doubled R in the first displayed functor from plain R later, retains the lower-case k omitted by the witness in the comparison formula, and abbreviates ``char.''. The fully handwritten final request about Deligne closes this programme; part F broadens it to ramification. No conjectural assertion here is promoted to a theorem by the corrected reader.
'''
 p.write_text(s)
