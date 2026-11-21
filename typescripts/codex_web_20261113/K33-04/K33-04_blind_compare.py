"""Compare each independent reading to its page; run from any directory."""
from pathlib import Path
import csv,json,re,unicodedata
root=Path(__file__).resolve().parent
decisions=json.loads(r'''{
  "098|case b, final object": [
    "imm fermée",
    "imm fermée",
    "Keep the abbreviation. Only three low letter groups occur before the long f."
  ],
  "098|brace below first Hom": [
    "donc }f^!",
    "donc }f^!",
    "Keep the exclamation. The high stroke has a separate dot, followed by the baseline hyphen."
  ],
  "098|above duality identities": [
    "et de restriction|et de bidirection",
    "et de restriction|et d'induction|et de bidirection",
    "Keep the compressed original reading and add the alternative. The slope beyond the tall stroke does not resolve the word."
  ],
  "099|opening display": [
    "\\widetilde F_x",
    "\\overset{\\handwritten{\\sim}}{F}_x",
    "The tilde has one free pen curve. Register it separately from type F."
  ],
  "099|membership after a_i,b_i": [
    "b_i\\in T_x",
    "b_i\\handwritten{\\in}T_x",
    "The free epsilon strokes differ between the two occurrences; mark both as handwriting."
  ],
  "099|scalar and integral in last formula": [
    "+\\int_{T_x}",
    "+\\handwritten{\\int}_{T_x}",
    "The long asymmetric curve is inked in, with typed subscript."
  ],
  "100|above s'ensuit": [
    "formellt|formellmt",
    "formellt|formellmt",
    "The raised ending consists of a short ligature and a final stem. Retain the manuscript abbreviation."
  ],
  "100|inserted qualification on L prime": [
    "tout degré|tous degré",
    "tout degré|tous degré|tous degrés",
    "The short terminal strokes on both words allow the plural. Keep all readings."
  ],
  "100|category supplied above des complexes": [
    "K^-(X)^{\\mathrm{plat}}",
    "K^-(X)^{\\mathrm{plat}}",
    "The upright before both oblique strokes is visible. Keep K, distinct from C later on the sheet."
  ],
  "100|middle, equivalence": [
    "équivalent :|à",
    "équivalent :",
    "The word ends at the cross of t. The next two detached points settle the colon; there is no final e."
  ],
  "100|small words before Donc": [
    "on note que",
    "on \\unsure{note|voit} que",
    "The cross and the preceding short downstroke fit note. The reading voit remains possible."
  ],
  "101|local correspondence": [
    "\\approx",
    "\\approx",
    "Both lines bend in the same direction. Keep approximately equal."
  ],
  "101|membership of sigma": [
    "\\varepsilon",
    "\\varepsilon",
    "The short letter has rounded lobes. Preserve the epsilon used in the type."
  ],
  "101|summation lower limit": [
    "\\varepsilon G_I",
    "\\varepsilon G_I",
    "At high contrast this is the same epsilon, with no preceding sigma."
  ],
  "102|crossed after notation": [
    "Si $L_{\\bullet}$ ou $M$",
    "Si $L_{\\bullet}$ ou $M$|Si $L_{\\bullet},M$",
    "The strike crosses two small marks between L and M. A comma is possible; retain both readings."
  ],
  "102|above base change": [
    "f:X\\mathbin{-}Y",
    "f:X\\longrightarrow Y",
    "The tapered join has two short strokes pointing back from its tip. Read the arrowhead."
  ],
  "102|insert above un calcul": [
    "parfois|tjours",
    "pfois|parfois|tjours",
    "Under enlargement the first two shafts pass directly to ois. Prefer the compressed form pfois."
  ],
  "103|proof, immediately before sum": [
    "e(S^f/S)\\unsure{=}",
    "e(S^f/S)=",
    "Two horizontal rows of type fragments occupy exactly the height of adjacent equals signs. The blind reading settles the sign."
  ],
  "104|upper slanted note": [
    "suppl. pour",
    "suppl. \\unsure{pour|sur}",
    "At the rotated baseline the initial looks more like the downstroke of p, but the initial of Lois overlaps it. Include sur."
  ],
  "104|numbers before laws": [
    "1), 2 uncertain, 3)",
    "1), 2 uncertain, 3)",
    "The middle numeral is only a returning stroke. The series favours 2; keep its doubt mark."
  ],
  "106|lower heading": [
    "Variante ou généralisation|Variante de projection",
    "Variante de projection|Variante ou projection|Variante ou généralisation",
    "A low loop following the p resembles the descending j in projection; the short intervening word remains indistinct."
  ],
  "106|slanting note, object": [
    "A_{\\unsure{Y',Y}!}",
    "A_{\\unsure{Y',Y}}^{\\unsure{!|g}}",
    "The small last sign sits above the adjacent Y's; its upper hook and lower curl admit another letter."
  ],
  "107|multiplicity mark between q) and =": [
    "comma or point",
    "point or comma",
    "The small upright oval has no clear comma tail. Prefer a point and retain the other reading."
  ],
  "108|struck restart": [
    "pouvons|pourr",
    "pouvons|pourr",
    "The long cancellation permits either continuation after pou; keep both and the original preference."
  ],
  "108|last participle": [
    "en faisant avec",
    "en partant|faisant avec",
    "The loop lacks the long cross stroke seen in faisceau one line below. Prefer partant but retain the earlier reading."
  ],
  "108|just before D minus": [
    "déborder|tomber des",
    "tomber|déborder dans|des",
    "The beginning resembles the writer's t; little survives of the middle. The following word is a d with a short undulation."
  ],
  "108|fragment after variantes": [
    "provenant followed by struck de",
    "pr.|pro followed by struck venant|venant de",
    "The enlargement separates the intact pr and its point from the returning stroke through the rest. The extent and ending of the cancellation remain doubtful."
  ],
  "109|right of the line ending Tor bracket": [
    "no separate punctuation",
    "\\qquad\\unsure{:}",
    "Two aligned dots appear well to the right of the equals. Added with doubt as to whether they were intentional."
  ],
  "110|before first table": [
    "qu. cpct",
    "qu. cpct",
    "The second group begins with an open c followed by a descender and ends in a crossed t. Both appearances support cpct; the first group has a short u-shaped continuation."
  ],
  "110|first table braces": [
    "si Y qu. cpct / f compactifiable",
    "si Y qu. cpct / f compactifiable",
    "The two abbreviated groups at the upper right repeat the strokes at the end of the paragraph, including the low stem on the second group."
  ],
  "110|pullback bottom start": [
    "D(\\deleted{\\unsure{X}}Y)",
    "D(\\deleted{\\unsure{X}}Y)",
    "The final Y has a crosswise earlier shaft underneath it. Keep Y live and the doubtful X underneath, in the deletion."
  ]
}''')
alignments=json.loads(r'''{
  "100|dark M in two places": "L_{\\bullet},\\deleted{L}M_{\\bullet}",
  "102|insertion over foncteurs": "exacts",
  "103|theorem sum": "\\handwritten{\\sum}_{\\underline p}L(S^f_{\\underline p})",
  "103|residue-field lengths": "L(K^f_k)=[K:k]_i",
  "106|vertical pair, left of box": "X\\arrow[d,\"f\"']\\&K^\\bullet\\\\\nY\\&L_\\bullet",
  "109|second case, hats on S and R": "\\mathrm{hd}_{\\overset{\\handwritten{\\scriptscriptstyle\\wedge}}{R}}\\overset{\\handwritten{\\scriptscriptstyle\\wedge}}{S}",
  "110|inserted functors": "comme foncteurs $D^-(X)$ --- $D^-(Y)$, $D(X)$ --- $D(Y)$",
  "110|dim statement": "$f_*$ est de dim cohomologique finie",
  "110|extension hypothesis": "soit de type fini sur un corps, soit de type fini sur $\\operatorname{Spec}\\mathbb Z$",
  "110|ordinary direct image qualifier": "\\text{si }Y\\text{ de t.f.}\\\\\\text{sur un corps}\\\\\\text{ou sur }\\operatorname{Spec}\\mathbb Z,\\\\\\text{et }f\\text{ de t.f.}",
  "110|ordinary second row superscripts": "D^{\\unsure{+|e}}(X)\\;\\text{---}\\;D^{\\unsure{+|c}}(Y)"
}
''')
from hashlib import sha256
# The witness came after the blind comparison. Reverse only its local edits
# in memory and verify the resulting bytes against the immutable audit hash.
reversion=json.loads(r'''{"098": ["f625723c51a86c9f2208da1e1539548fd7ff350625c713807197328fbd3340cd", "0948147491639da748dc6c2c0b22c890ae6ec6b8bed3cac28c69bac7756c191e", [[381, 381, "", "\\unsure{"], [382, 382, "", "|\\bullet}"], [902, 902, "", "\\unsure{"], [912, 912, "", "}"], [966, 978, "ction|d'indu", ""]]], "100": ["baebbf977da5cda96b0521f6b6be306a103e9614736994ec5a9a7e109d8d56fe", "6e60049dcda835e63c12b4ce232947e2a6923992a57e59db7982c91c7992e520", [[713, 720, "|homom.", ""], [1284, 1284, "", "\\unsure{"], [1287, 1287, "", "}"], [1712, 1712, "", "unsure{\\"], [1726, 1727, "{", "|-"]]], "102": ["17a2e5fc22aa1e6b245e389d2677797abfd8c8957f0b2d4c7ef2976e73806772", "0e6a9fc54784ad6cdfb356101809bc02002aa8d28eca3bef07eed69cbdf4809f", [[129, 129, "", "\\unsure{"], [137, 137, "", "|hypertors}"], [1112, 1121, "|$f^*$ ou", ""]]], "104": ["0d498a1b0e3d49e925b8aa339f1a4cf7548aecda6ed27639d956c5029616b937", "42a01b7647df06b1b78015f7e932796f746b2a559d8cfe18187e107ccc56190e", [[2035, 2035, "", "\\unsure{"], [2038, 2038, "", "}"]]], "106": ["1aaa328fa0269108a3634dc3092f091ca32b5a1cbfd14b15aa70bb61351aa7c6", "91f5397e666b37ac8349dd0e915851f890820a91dff83b9b25dd8aaad27837de", [[176, 186, "$|$\\otimes", ""], [1200, 1200, "", "unsure{\\"], [1205, 1208, "OK.", "cqfd}"], [1891, 1891, "", "\\unsure{"], [1895, 1895, "", "}"], [2557, 2557, "", "\\unsure{"], [2558, 2558, "", "|i}"]]], "108": ["a4c2b3871cb2abb061ea3faae7f929bbbcdf2552910bf87b4493c4604d5b0c1c", "183f54372063bd20970a566f9de346f0d57c4424ddc6a698e04861bcf4b1f78b", [[732, 773, "|pour les précédentes|pour les précédents", ""]]], "110": ["9826bcf7f979d7eb40fed97d6b98ebe211fc150176def50f34df04592ce603d1", "41b7fc5a2110785762e5fa60b953af63ccb2335a458c1f0ea0ea6ae26cccbcec", [[170, 175, "|dans", ""]]]}''')
def audited_page(n):
 source=(root/'pages'/f'K33-04_33_scan{n}.tex').read_text()
 if n not in reversion:return source
 post,pre,ops=reversion[n]
 dig=lambda s:sha256(s.encode()).hexdigest()
 if dig(source)==pre:return source
 if dig(source)!=post:raise ValueError('Unexpected page revision: '+n)
 for a,b,old,restored in reversed(ops):
  if source[a:b]!=old:raise ValueError('Witness patch does not match '+n)
  source=source[:a]+restored+source[b:]
 if dig(source)!=pre:raise ValueError('Restored audit hash differs: '+n)
 return source


literal_decisions={
 '101|local correspondence': r'S_R^f\handwritten{\approx}S\mathbin',
 '101|membership of sigma': r'\sigma} \varepsilon G_I',
 '101|summation lower limit': r'\sum}_{\varepsilon G_I}',
 '104|numbers before laws': r'\unsure{2}) Commutativité',
 '107|multiplicity mark between q) and =': r'e_E(\underline q)\unsure{.|,}=',
 '108|last participle': r'en \unsure{partant|faisant} avec',
 '108|just before D minus': r'\unsure{tomber|déborder} \unsure{dans|des} $D^-$',
 '108|fragment after variantes': r'\unsure{pr.|pro}\deleted{\unsure{venant|venant de}}',
 '110|first table braces': r'\text{si }Y\text{ qu. cpct}\\ f\text{ compactifiable}',
}

def norm(s):
 s=unicodedata.normalize('NFC',s).replace('’',"'").replace('–','-')
 s=s.replace(r'\mathbin{\ooalign{\hfil$\mathrm{x}$\hfil\cr\hfil$\handwritten{\bigcirc}$\hfil\cr}}',r'\otimes')
 s=s.replace(r'\overset{\handwritten{\sim}}{F}',r'\widetilde F').replace(r'\overset{\handwritten{\sim}}{S}',r'\widetilde S')
 for letter in ('R','S'):
  s=s.replace(r'\overset{\handwritten{\scriptscriptstyle\wedge}}{'+letter+'}',r'\hat '+letter)
 for _ in range(5):
  s=re.sub(r'\\(handwritten|deleted|inserted|uline|uuline|text|mathrm|operatorname)\{([^{}]*)\}',r'\2',s)
  s=re.sub(r'\\unsure\{([^{}|]*)(?:\|[^{}]*)?\}',r'\1',s)
 s=s.replace(r'\longrightarrow',r'\to').replace(r'\rightarrow',r'\to')
 s=s.replace(r'\widetilde',r'\tilde').replace(r'\!', '').replace(r'\,','').replace(r'\;', '')
 return re.sub(r'[$\s{}\\_^]','',s).casefold()
def quote(s):return chr(96)+s.replace('|',r'\|').replace(chr(96),"'")+chr(96)
def run():
 rows=list(csv.DictReader((root/'K33-04_blind.tsv').open(),delimiter='\t'))
 diffs=[];unmatched=[];matches=0
 for r in rows:
  n,loc,read=r.values();key=n+'|'+loc
  page=audited_page(n)
  excerpt=alignments.get(key,read)
  if key in decisions:
   before,after,why=decisions[key]
   # The table sometimes describes the mark in words. Confirm its literal
   # LaTeX at the corresponding place before reporting the editorial decision.
   anchor=literal_decisions.get(key,after)
   if anchor not in page:raise ValueError('Audit reading not in page: '+key)
   diffs.append([n,loc,read,before,after,why]);continue
  if norm(excerpt) in norm(page):matches+=1;continue
  unmatched.append((n,loc,read))
 out=['# Blind comparison', '', f'{len(rows)} independent entries. {matches} agree after alignment of the typography or the cited passage. {len(diffs)} differences required an editorial decision.','',
 'The blind TSV records the image reading. For pages edited at the witness stage the script reconstructs the audited text in memory and verifies its SHA-256 before it compares readings. The two excerpt columns preserve the first-pass and audit decisions even when the later witness check changed a marked passage. The alignment list in this script identifies equivalent notations and excerpts in repeated formulas.', '',
 '| Scan | Place | Blind reading | First pass | Audit reading | How settled on the image |','|---|---|---|---|---|---|']
 for n,loc,read,bef,aft,why in diffs:out.append('| '+' | '.join([n,loc,quote(read),quote(bef),quote(aft),why])+' |')
 if unmatched:out+=['','## Unaligned entries','']+[f'- {n}, {loc}: {quote(read)}' for n,loc,read in unmatched]
 (root/'K33-04_blind_compare.md').write_text('\n'.join(out)+'\n')
 if unmatched:raise ValueError('Unaligned entries: '+str(unmatched))
 print('entries',len(rows),'aligned',matches,'decisions',len(diffs))
if __name__=='__main__':run()
