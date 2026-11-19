"""Record manually selected literal excerpts from the already fully read sources.

This is quotation serialization, not automated mathematical assessment. The
separate source_paraphrase retains the earlier English gloss. Uncertainties and
deletions are copied exactly, and no scan is consulted.
"""
import json
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parents[2]
PRO = 'sources/texts/pro/MPL_68_033-056+162-1+162-6_transcription.tex'
K1 = 'sources/texts/codex/K161-6-01_transcription.tex'
K2 = 'sources/texts/codex/K161-6-02_transcription.tex'
texts = {p: (ROOT / p).read_text().splitlines() for p in (PRO, K1, K2)}
selections = {
    1: (PRO, [(28, 28), (31, 34)]),
    2: (PRO, [(56, 58)]),
    3: (PRO, [(68, 68)]),
    4: (PRO, [(553, 558)]),
    5: (PRO, [(83, 85)]),
    6: (PRO, [(87, 94)]),
    7: (PRO, [(97, 99)]),
    8: (PRO, [(101, 102)]),
    9: (PRO, [(104, 104)]),
    10: (PRO, [(112, 112), (120, 121), (128, 130)]),
    11: (PRO, [(170, 170), (189, 189)]),
    12: (PRO, [(185, 185), (189, 189)]),
    13: (PRO, [(274, 274)]),
    14: (PRO, [(266, 266)]),
    15: (PRO, [(280, 280)]),
    16: (PRO, [(368, 368), (370, 372)]),
    17: (PRO, [(376, 376), (380, 380)]),
    18: (PRO, [(384, 386)]),
    19: (PRO, [(410, 411)]),
    20: (PRO, [(429, 429)]),
    21: (PRO, [(448, 450), (453, 453), (456, 458)]),
    22: (PRO, [(446, 446)]),
    23: (PRO, [(460, 465)]),
    24: (PRO, [(469, 473)]),
    25: (PRO, [(485, 485)]),
    26: (PRO, [(489, 491)]),
    27: (PRO, [(493, 493)]),
    28: (PRO, [(495, 495)]),
    29: (PRO, [(499, 503)]),
    30: (PRO, [(562, 562), (567, 568), (574, 578)]),
    31: (PRO, [(586, 588)]),
    32: (PRO, [(619, 621), (627, 631)]),
    33: (PRO, [(731, 734)]),
    34: (PRO, [(813, 813)]),
    35: (PRO, [(839, 840)]),
    36: (PRO, [(806, 806)]),
    37: (PRO, [(933, 939), (946, 946)]),
    38: (PRO, [(966, 966)]),
    39: (PRO, [(418, 418)]),
    40: (K1, [(25, 25)]),
    41: (K1, [(58, 61)]),
    42: (K1, [(101, 103)]),
    43: (K1, [(117, 117)]),
    44: (K1, [(121, 121)]),
    45: (K1, [(196, 198), (207, 207)]),
    46: (K1, [(228, 230)]),
    47: (K1, [(232, 232)]),
    48: (K1, [(222, 222)]),
    49: (K1, [(249, 249)]),
    50: (K1, [(401, 401)]),
    51: (K1, [(480, 480)]),
    52: (K1, [(433, 433)]),
    53: (K1, [(326, 326)]),
    54: (K1, [(636, 636)]),
    55: (K2, [(97, 97)]),
    56: (K2, [(36, 36)]),
    57: (K2, [(270, 270)]),
    58: (K2, [(294, 298)]),
    59: (K2, [(328, 331)]),
    60: (K2, [(378, 378)]),
    61: (K2, [(419, 419)]),
    62: (K2, [(456, 458)]),
    63: (K2, [(469, 469)]),
    64: (K2, [(532, 532)]),
    65: (K2, [(528, 528)]),
    66: (K2, [(579, 585)]),
    67: (K2, [(555, 555)]),
    68: (K2, [(593, 593), (595, 595)]),
    69: (K2, [(612, 612)]),
    70: (K2, [(606, 606), (610, 610)]),
    71: (K2, [(620, 622)]),
    72: (K2, [(653, 653), (657, 659), (664, 664)]),
    73: (K2, [(677, 677)]),
    74: (K2, [(723, 725)]),
}
# Short portions of very long physical lines were selected manually, after
# reading their complete sentences. They retain the exact transcription text.
short = {
    8: [r"Elle est comm. \unsure{ssi|si} $L$ est commutative, i.e. si $x,y\in L\Rightarrow xy=yx$ --- \inserted{et dans ce cas cette structure est l'\uline{additive} de $L$.}",
        texts[PRO][101]],
    43: [r"Le sous-groupe \inserted{$G_C$} de $G=O(E)$ qui laisse une calotte $C$ invariante, \deleted{\illegible{1}} a dix éléments, \deleted{le sous-g} son intersection \inserted{$G'_C$} avec $G'=SO(E)$ est le groupe (can. isom. à $\mathbb Z/5\mathbb Z$) des rotations d'angle multiple de $2\pi/5=\theta$ autour du \deleted{\unsure{sommet}} \inserted{vecteur} $a$."],
    47: [r"Montrons que \uline{tout} automorphisme \inserted{$g$} du graphe est dans $\Gamma'$."],
    55: [r"Supposons \unsure{pour cela|pour voir|si on sait} que $G$ opère fidèlement sur $J$, alors $G\longrightarrow\mathfrak{S}_5$ est injectif, donc $G\simeq$ sous-groupe d'indice $2$ de $\mathfrak{S}_5$, donc $G\simeq A_5$."],
}

claims = json.loads((P/'claims.json').read_text())
audit = []
for c in claims:
    n = int(c['id'].rsplit('-', 1)[1])
    source, ranges = selections[n]
    full = '\n'.join('\n'.join(texts[source][a-1:b]) for a,b in ranges)
    # Transcriber comments and scan commands are not authorial quotation text.
    fragments = short.get(n) or ['\n'.join(line for line in texts[source][a-1:b]
                    if not line.startswith('%') and not line.startswith(r'\scanpage'))
                                for a,b in ranges]
    assert all(q in full for q in fragments), c['id']
    c.setdefault('source_paraphrase', c['his_statement'])
    c['his_statement'] = '\n[…]\n'.join(fragments)
    q = dict(id=c['id'],source_file=source,selected_lines=ranges,literal_fragments=fragments,
             excerpt_rule='Literal transcription excerpt; […] marks omitted material, not a source symbol.')
    if n in (60,61):
        q['drafting_context'] = 'The whole passage is inside the deleted block at physical lines 374–429; quoting an inner sentence does not revive it.'
    if n == 67:
        q['drafting_context'] = 'The excerpt occurs in the deleted discussion beginning at physical line 551; the later parallel live assertion is separately recorded in the claim.'
    c['source_quotations'] = [q]
    audit.append(q)

(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
(P/'quotation_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Literal source excerpts verified for', len(audit), 'core claims; English glosses retained separately.')
