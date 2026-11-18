"""Assemble audited source and index doubts. No OCR, outside readings or compilation."""
from pathlib import Path
import csv,re,json
OUT=Path(__file__).resolve().parent
ID='K157-4-06'

def macros(s,name):
 for m in re.finditer(r'\\'+name+r'\{',s):
  i=m.end(); start=i; depth=1
  while i<len(s) and depth:
   if s[i]=='\\':
    z=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);i+=len(z.group()) if z else 1;continue
   if s[i]=='{':depth+=1
   elif s[i]=='}':depth-=1
   i+=1
  if depth:raise ValueError((name,m.start(),'unclosed'))
  yield m.start(),i,s[start:i-1]

def cell(s):return s.replace('|','&#124;').replace('\n',' ').replace('`','&#96;')
def grounds(n,a):
 if n==84 and a==r'n|\pi':return 'One arch lacks the clear crossbar of nearby pi. The power calculation favours pi, but n remains first from the ink.'
 if n in (87,88,96) and r'\deleted' in a:return 'Superposed or hatched strokes leave the earlier form and/or its cancellation status unresolved. The alternatives describe the same physical locus.'
 if n==90 and a=='K|X':return 'Short left upright and long lower-right arm favour K; the later family uses clear X_i, which favours X contextually but does not settle this glyph.'
 if n==82 and a==r'f|p':return 'Long looped stem favours f locally. The preceding factorization f=pi would favour p as the class member; the page is not normalized.'
 if 'varinjlim' in a or 'underline{\\lim}' in a:return 'The lower stroke has an uncertain or unresolved terminal head. The inductive-system prose favours a right-arrow limit, but the visible stroke determines candidate order.'
 if a in (r'\sim|\simeq',r'\simeq|\sim'):return 'The raised wave is visible; whether a separate short horizontal belongs to it is unresolved. Isomorphism context does not determine the exact drawn decoration.'
 if 'mathscr' in a or 'mathcal' in a:return 'Curl, loop or hooked capital admits the listed alphabet candidates. Its mathematical role does not decide script versus ordinary/Greek form.'
 if a in (r'\Psi|\Upsilon',r'\Phi|\varphi'):return 'The loop/cup and central stem allow the listed Greek forms. First ambiguous occurrence on the page is marked; repeated matching forms use its first candidate.'
 if a==r'\alpha\delta|\alpha\beta':return 'Two low signs are present; the second curved return can be delta or beta. Closure language suggests an orthogonality iteration but does not decide the ink.'
 if n==95 and a=='88|89':return 'The own-page number is overwritten. Adjacent numbering favours 88; the right-hand loops also admit 89.'
 if n==97 and a=='90':return 'Small number lies among oblique annotation strokes; 90 agrees with the sequence, but the crossing remains a reading obstacle.'
 if n==97:return 'Small oblique, reduced or crossed writing was reread rotated and enlarged. The listed candidates remain low confidence; surrounding argument is not used to restore missing letters.'
 if '|' in a:return 'The local reduced or crossed strokes admit these candidates. No further contextual preference is secure enough to override the ink; see the scan-specific audit and notation table.'
 return 'Tentative reading of compressed or cancelled strokes. No secure additional candidate; contextual plausibility does not establish the letters.'

notation=r'''# K157-4-06 — Final reading apparatus

## Notation table

Readings were made from the supplied images in one stream. The completed K157-4-05 notation table was consulted before scan 82 and is retained in preceding_notation_K157-4-05.md. Earlier tables are comparison aids, never sources of words. The table below supersedes first-reading hypotheses; the audit records each correction and the actual second-reading times. A recurring unresolved form is marked at its first occurrence on each page; visibly different forms remain distinguished.

| Scan / approximate manuscript locus | LaTeX reading / candidates | Ink and reconciliation |
|---|---|---|
| 82 upper and middle | `C,\mathrm{TC},F,\mathrm{TF},M,I`; `\widetilde C_0` | Ordinary capitals, with upright multiletter class names; separate tilde and lower zero. Retains K157-4-05 alphabet where the ink agrees. |
| 82 orthogonality displays | `\alpha` / `\ast`; `\alpha\delta` / `\alpha\beta` | Raised loop and returning leg, then two distinct low signs. Not replaced by a conventional orthogonality symbol. |
| 82 final paragraph | `\Phi` / `\varphi`; `\Psi` / `\Upsilon` | Loop/cup and central stems; first ambiguous occurrence marked. |
| 82 middle | `\mathrm{Cat}_{\mathcal U}` / `\mathscr U` | Small lowered curl restored in audit; not part of the preceding word. |
| 82 factorization | `pi` / `pj`; class member `f` / `p` | Dotted short terminal stroke in composite; long looped class-member stem. Later same-form f remains f. |
| 83 opening and lower formula | `u_!`; `I'→I`; `\mathbb N^{\circ}` / `o`; `B_G` | Dot separates ! from prime; N has doubled strokes; G's inward bar resolved in the audit. |
| 84 heading and definitions | `E`, `\mathrm{Filt}^{\pi}`, `\mathcal U` / `U`, `L_{\pi_0}` | E has three bars, F two; Filt is a word, not a script capital; pi has cap and two legs. |
| 84 final power chain | `(\pi')^{n}` / pi exponent; pi-prime `\geq` / `>` | One arch lacks a secure cap, so n first. Cardinal arithmetic does not license changing it. |
| 85 whole sheet | one outer `\deleted`, with nested local deletions | Three diagonal strokes cross the entire draft. Local crossed words and inserted X_i remain represented inside it. |
| 85 displays | `I_\pi(X)`, `X_i`, `X_X`, `J\subset I_\pi(X)` | Capital I cap/foot; J lower hook; i short and dotted; final X subscript is a capital X. |
| 86 first definition | `\widetilde I`, `I'`, `X_{I'}` | Raised wave on I and separate prime; no inferred E argument on Filt. |
| 86 cardinal chain | `\pi'^{\pi^{2}}` / top `?` | Two raised levels preserved; small upper hook remains doubtful. |
| 87 construction | `\alpha,\beta,I'_\alpha,I'_{\alpha+1},i_J` | Greek loop/double turn; primes above I. First I'_0 prime resolved. First i_J is an insertion linked below major. |
| 87 I superscript | deleted xi / live xi / deleted star | One heavy locus, represented by alternatives including uncertain cancellation status. Two alternative deleted macros do not mean two physical deletions. |
| 87 margin and 88–90 bounds | `\pi>\pi_0`, `\pi^{\pi_0}=\pi`; initial lemma bound `\leq\pi_0` | Low zero is visible and retained, including where it differs from the application. |
| 88 middle | `\mathscr P` / `\mathcal P` / `P`, subscript `\leq\pi_0` | Hooked stem and broad bowl; not a Greek capital. |
| 88 Card / i_J | ordinary Card / barred C; possible deleted e before i_J | Detached short upper stroke and looped overwritten lower stem remain explicit alternatives. |
| 89 displays / prose | underbraces; `\pi.\pi`; literal `=` shorthand | Explanatory lines kept beneath their actual segments. Baseline full stop is not normalized to a centred dot; equals shorthand not expanded. |
| 89 system / insertion | `X_{\widetilde i}`, `\widetilde I`; inserted de tilde I ... | Separate waves over short dotted i and capital I. Audit removed a duplicate I falsely placed inside the cancellation. |
| 90 opening | `(I')_{\alpha\in A}` / E-prime-like overwritten form | No internal alpha supplied where none is visible; later union explicitly has I'_alpha. |
| 90 proposition | first `K_i` / `X_i`; `J` / `\mathcal J`; final c) / b) | Local first glyph has K-like limbs; later X is a distinct shape. Label is overwritten. |
| 91 representation | first `\sim` / `\simeq`; short i_J and i in J | Wave/extra stroke uncertain; J has a hook below, unlike lowercase i. Inserted système replaces cancelled représentation. |
| 91 NB / final formula | first `\varinjlim` / underlined lim; final plain lim / varinjlim | Short lower stroke in NB has a weak hooked end; last formula lacks a clear direction arrow. Distinct local shapes remain distinguished. |
| 92 middle display | literal `\varprojlim` | Lower arrow points LEFT despite inductive-system prose. Not changed to an expected colimit. |
| 92 proposition | varinjlim / underlined lim; literal `\varinjlim_I X` | First short head uncertain. No missing i is supplied to X. |
| 92 revisions | inserted réunion, cancelled old generated-part construction | Internal on prend I'_0 is retained within the old block; caret paths control insertion positions. |
| 93 representations | X / alpha in one rounded object glyph; coniques / canoniques; parfaitement / bien | Alphabet/word alternatives reflect reduced loops and overlap with the slanted margin. Alambiqué resolved by enlargement. |
| 93 definition | set `M` versus full-category `\underline M`; `\underline{\mathrm{Filt}^{\pi}}` | Separate underlines. Uncertain M after On dit que overlaps the inserted cardinal and remains doubtful. |
| 93 margin | filtration cardinale stricte; Filt^pi; cardinal <=pi | Rotated and reread; final filtrantes overlaps the body and remains qualified. |
| 94 adapted system | `X_{i_J}\xleftarrow{\simeq}\varinjlim_{j\in J}X_j` | Wave plus additional bar resolved; the inner lowercase j has a descender. Other i's are short. |
| 94 cancelled b) | inserted `(en \underline M),` | Closing parenthesis and short underline restored; whole lower definition remains cancelled. |
| 95 labels / numbering | circled a_pi, double-circled b_pi, circled c_pi/d_pi; own number 88 / 89 | Lower pi belongs to each label. Archive 94 is at upper left. |
| 95 formulas | M / underlined M in a); underlined M/Filt in c); I_M / I_M^pi in b) | First M has separate footlike marks; lower underlines clear. Overdrawn possible pi on I stays doubtful. Both dans M clauses stay literal. |
| 95 interline arrow / prose | `\xleftarrow{\simeq}`; l'a followed by deleted cc; enfin | Enlargements resolve wave plus bar, apostrophe and the f-i-n ending; old doubts removed. |
| 96 cancelled upper condition | e-prime / e; underlined M→E; L_pi | Whole condition and bracketed generating-category clause crossed; nested old letters kept. |
| 96 middle | prop. 1'; underlined lim / varinjlim; I_M | Separate elevated tick resolves prime. Blunt lower-lim stroke differs from the clear arrows in nearby displays. |
| 96 final X_i | possible deleted X then X_i / plain X_i / X | Two X-like crossings and small dotted i; underlying state explicitly uncertain. |
| 96 margins | impliquée / compliquée; simplement / sûrement; On peut prendre filtrant | Rotated; heavy cancellations prevent confident reading. |
| 97 margins | pas bien...; NB...; Passer ici...; Ultra-faux!! | All reread in their own directions. NB has two physically unreadable words under dense hatching; no mathematical illegibility placeholder. |
| 97 crossed lemma | restored La condition b) implique; s'implique / s'entend; x, I_i, alpha_A | Whole attempted lemma remains cancelled. Restored first line is part of that block; last word tentative. |
| 97 live foot | pi-admissible; b_pi), (avec a_pi) | Bottom lemma sits outside broad cancellation; low pi and parentheses preserved. |

## Doubts

Every explicit unsure occurrence in the audited page files is indexed below, including cancelled text and uncertain cancellation status. The line number is the stable source-file line followed by context. The listed alternatives are all retained candidates from this reading, not a claim that the ink permits no other possibility. Confidence is in decipherment, not mathematical plausibility. All unresolved entries below are conservatively low confidence.

| Scan | Source line and nearby text | First reading | Other retained candidates | Confidence | Context preference / grounds |
|---|---|---|---|---|---|
'''

tail=r'''
## Slips kept as written / unresolved textual discrepancies

No doubtful ending, cancelled form or uncertain symbol is promoted here to an established authorial error. The following literal discrepancies are retained for the post-freeze notes, with low confidence in any proposed correction.

| Scan / locus | As written | Possible intended form / question | Grounds |
|---|---|---|---|
| 82 factorization | class member f/p, followed by f in TF | p might be intended | The factorization uses f=pi, but the local ink favours f and is doubtful. |
| 87 lemma opening | cardinal I'_0 <= pi_0 | <= pi might have been intended | The immediately preceding application starts with a subset of cardinal <= pi. No correction supplied. |
| 90 proposition b) | cardinal J <= pi_0 | <= pi might have been intended | The preceding closure construction treats cardinal <= pi. Low-confidence internal comparison only. |
| 92 middle display | left-arrow varprojlim | right-arrow varinjlim might be intended | Inductive-system wording and neighbouring right-arrow formulas contrast with the clear left arrow. |
| 92 Proposition 1 bis | varinjlim_I X | subscript i on X might be intended | Nearby system is (X_i); the displayed shorthand itself has no i. |
| 95 introductory and b) systems | dans M | perhaps ambient E was intended | The subsequent membership criterion is phrased using I_M. Both M readings remain literal; no mathematical repair. |
| 83 / 93 prose | Tout ens. ordonnée; E muni; E satisfait | agreement/syntax questions | These are kept verbatim; no authorial spelling or agreement error is asserted from abbreviated or fast handwriting. |

## Abbreviations met

Proposed expansions appear only here, never in the transcription.

| Written | Proposed expansion | Representative scans |
|---|---|---|
| Cat; cat.; sous-cat. | catégorie(s); sous-catégorie | 82–84,93 |
| TC; TF; Fl; Ob | trivial cofibrations/fibrations; flèches; objets (notation, not expanded) | 82,84–86 |
| tt; tte; ens.; sous-ens | tout; toute; ensemble; sous-ensemble | 83–97 |
| p.ex.; P.ex.; i.e.; cf | par exemple; id est; confer | 83–97 |
| esp.; noeth.; str. | espace; noethérien; strictement | 83–84 |
| card.; card; Card | cardinal / cardinalité | 84–97 |
| hyp.; prop.; lemme; NB; OK | hypothèse; proposition; nota bene; okay | 84–97 |
| syst.; ind.; filtr.; filtr. cardinale | système; inductif; filtrant / filtration | 90–97 |
| grd dev.; dev.; ds | grand devant; devant; dans | 87,92,94 |
| major.; d'élémts | majorant; d'éléments (ending uncertain) | 87–88 |
| tjrs; vérif.; démonstr. | toujours; vérification; démonstration | 84,95,97 |
| f. et s. | faut et suffit | 95 |
| literal = in prose | même(s) | 89–90 |
| lim. | limite(s), uncertain marginal abbreviation | 97 |

## Legibility and limits

All sixteen whole pages and all supplied thirds were personally viewed in order during the first reading. All thirds were read again before the page file was opened in the second reading. Each audit records actual UTC start/end times, a pre-comparison list, every inline/display formula, and the changes. The smallest oblique words, hatch-covered corrections, overwritten symbols and short arrowheads are less secure than the larger formulas. Scan 97's upper margin and cancelled NB are the least legible parts; the two unreadable words there remain an estimate. Scan 85 is an entirely cancelled draft, and scans 94, 96 and 97 have long cancelled passages whose old text must not be treated as live assertions.

No OCR, web source, outside transcription or LaTeX compiler was used. The first-reading apparatus is retained as historical working documentation and is superseded by this register and the audited page files. A complete inventory and formal source balance do not guarantee that every reading is correct.
'''

def main():
 old=OUT/f'{ID}_doubts.md';hist=OUT/f'{ID}_first_reading_apparatus.md'
 if not hist.exists():hist.write_text('# HISTORICAL — superseded working readings\n\n'+old.read_text())
 pages=sorted((OUT/'pages').glob('*.tex'))
 body=[]
 for p in pages:
  n=int(re.search(r'scan(\d+)',p.name).group(1));s=p.read_text()
  for a,b,arg in macros(s,'unsure'):
   line=s.count('\n',0,a)+1
   context=s[max(s.rfind('\n',0,a)+1,a-30):min(len(s),b+30)]
   candidates=arg.split('|')
   body.append(f'| {n} | l.{line}: `{cell(context)}` | `{cell(candidates[0])}` | '+('; '.join('`'+cell(x)+'`' for x in candidates[1:]) or 'none secure')+f' | low | {grounds(n,arg)} |')
 old.write_text(notation+'\n'.join(body)+'\n'+tail)
 (OUT/f'{ID}_transcription.tex').write_text('\\cotefile{157-4}\n'+'\n'.join(p.read_text().rstrip()+'\n' for p in pages))
 (OUT/f'{ID}_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{'+ID+'_transcription}\n\\end{document}\n')
 inv=OUT/f'{ID}_inventory.csv'
 with inv.open(newline='') as f:rows=list(csv.DictReader(f));fields=list(rows[0])
 for r in rows:
  if r['element']=='097-18':r['kind']='text';r['position']='inside cancelled lemma, first abandoned line after title'
  if r['element']=='096-04':r['first_words_or_objects']='Cette condition semble plus impliquée/compliquée (uncertain)'
 if not any(r['element']=='096-17b' for r in rows):rows.append(dict(zip(fields,['157-4','96','text','Grothendieck','096-17b','deletion','inside lower-left slanted margin','whole On peut prendre filtrant note','yes'])))
 special={'087-15':14.5,'088-16':7.5,'091-14':3.5,'096-17b':17.5,'097-18':12.5}
 def key(r):
  v=special.get(r['element'])
  if v is None:v=float(re.search(r'-(\d+)',r['element']).group(1))
  return int(r['scan']),v
 rows.sort(key=key)
 with inv.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 print(json.dumps({'pages':len(pages),'unsure_rows':len(body),'inventory_rows':len(rows)}))
if __name__=='__main__':main()
