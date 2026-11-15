"""Prepare proposed text-mode repairs and isolated proofs; never edit sources."""
from pathlib import Path
import hashlib
import json
from build_readers import explicit_transform, select_variant, texescape

P = Path(__file__).resolve().parents[1]


def patch(key, before, after, problem, action):
    return dict(key=key, before=before, after=after, problem=problem, action=action)


PATCHES = [
    patch('ps_134-3_023', r'\qquad or \qquad', r'\qquad\text{or}\qquad',
          'The connective or between inclusion functors is set as mathematical variables.',
          'Wrap only the connective in text mode; retain both surrounding quad spaces.'),
    patch('ps_134-3_040', r'\xout{(a functor from A_{/a} to B)}',
          r'\xout{\text{(a functor from }A_{/a}\text{ to }B)}',
          'Cancelled explanatory prose prints as joined italic letters in apparatus entry 10.',
          'Wrap the prose fragments in text mode inside the existing cancellation; retain A_{/a}, B, and punctuation.'),
    patch('ps_134-4_088', r'\xout{\uline{Definition 5}}',
          r'\xout{\text{\uline{Definition 5}}}',
          'The cancelled underlined heading in formula (5) loses its word-number space in the apparatus.',
          'Put the existing underlined heading in text mode inside its unchanged cancellation.'),
    patch('ps_134-5_001', r'\hand{(\mathrm{Hot}^{\underline{W}}_A) or}',
          r'\hand{(\mathrm{Hot}^{\underline{W}}_A)\text{ or}}',
          'The handwritten connective or joins the preceding mathematical parenthesis.',
          'Wrap only the connective and its preceding prose space; retain the handwritten span and the category expression.'),
    patch('ps_134-5_028', r'\hand{if A,B ps.test}',
          r'\hand{\text{if }A,B\text{ ps.test}}',
          'The upper diagram condition prints ifA,Bps.test with missing prose spaces.',
          'Put if and ps.test in text mode, retaining A,B in math mode and the existing label placement.'),
    patch('ps_134-5_028', r'\hand{if A,B \underline{W}-asph.}',
          r'\hand{\text{if }A,B\ \underline{W}\text{-asph.}}',
          'The curved-arrow condition loses spaces around its mathematical variables and treats the adjective as math.',
          'Wrap if and -asph. as text and make the existing prose space after A,B explicit; retain W, underline, curve and label side.'),
    patch('ps_134-5_054', r'\inserted[typed]{(contractors)}',
          r'\inserted[typed]{\text{(contractors)}}',
          'The final prose class name in the hierarchy is set as math letters while adjacent class names are text.',
          'Wrap the complete parenthesized class name in text mode inside the existing typed insertion.'),
    patch('ps_134-5_079', r'\hand{(commutative).}',
          r'\hand{\text{(commutative).}}',
          'The explanatory word beside diagram (26) is set as mathematical variables.',
          'Wrap only the parenthesized prose note and its punctuation in text mode inside the handwritten span.'),
    patch('ps_134-5_129', r'\deleted{home\xout{\unsure{m}}omorphic to}',
          r'\deleted{\text{home\xout{\unsure{m}}omorphic to}}',
          'The deleted phrase home[m?]omorphic to loses the space before to in apparatus entry 5.',
          'Wrap the deleted phrase as text while preserving its nested cancellation and uncertainty macros exactly.'),
    patch('ps_134-6_061', r'\hand{(abelianization)}',
          r'\hand{\text{(abelianization)}}',
          'The left vertical-arrow explanation is set as math letters.',
          'Wrap only the explanatory prose in text mode, retaining the handwritten span and diagram geometry.'),
    patch('ps_134-6_061', r"\hand{``absolute''}",
          r"\hand{\text{``absolute''}}",
          'The quoted word absolute in the right arrow label is set in math mode while the following words are text.',
          'Put the quoted prose word in text mode, preserving the exact quote tokens and the handwritten span.'),
    patch('ps_134-6_074', r'\quad hence \ ', r'\quad\text{hence}\ ',
          'The connective hence in the displayed example is set as mathematical variables.',
          'Wrap only hence in text mode and retain existing explicit spacing.'),
    patch('ps_134-7_010', r'\hand{(final object of U(k)),}',
          r'\hand{\text{ (final object of }U(k)),}',
          'Formula (t) prints finalobjectofU(k) with lost prose spaces.',
          'Wrap only the explanatory prose and its spaces; retain U(k), punctuation, and the handwritten span.'),
    patch('ps_134-7_054', r'\inserted[typed]{via}',
          r'\inserted[typed]{\text{via}}',
          'The inserted connective via in formula (8) is interpreted as mathematical variables.',
          'Wrap only via in text mode inside its existing typed insertion.'),
    patch('ps_134-7_060', r'\hand{(for n \in \underline{N}).}',
          r'\hand{\text{(for }n \in \underline{N}).}',
          'The parenthetical condition after P_n(t) prints forn with no prose space.',
          'Wrap the opening prose and its following space; retain n, membership, N, underline, punctuation, and handwriting.'),
    patch('ps_134-7_072', r'L. \inserted[typed]{in}\ ',
          r'L.\ \inserted[typed]{\text{in}}\ ',
          'The word in after L. is treated as mathematical variables and loses its preceding prose space.',
          'Wrap only in inside the typed insertion and make the preceding prose space explicit; retain the following explicit space.'),
    patch('ps_134-7_081', r"\text{``pointed }\deleted{abeliani}\inserted{lineari}\text{zation''}",
          r"\text{``pointed }\deleted{\text{abeliani}}\inserted{\text{lineari}}\text{zation''}",
          'In formula (6a), the revised prefix of linearization is math italic while the surrounding word is text; the deleted prefix is also math.',
          'Wrap both prose prefixes separately inside their existing deletion/insertion macros, with no added spaces within the word.'),
    patch('ps_134-7_082', r'\quad resp.', r'\quad\text{resp.}',
          'The prose abbreviation resp. in the mixed-homotopy display is set as mathematical variables.',
          'Wrap only resp. in text mode, preserving punctuation and the existing explicit spacing.'),
    patch('ps_134-7_082', r'\quad if\ ', r'\quad\text{if}\ ',
          'The connective if in the mixed-homotopy display is set as mathematical variables.',
          'Wrap only if in text mode and retain the following explicit space.'),
    patch('ps_134-7_097', r'\overset{\hand{adjunction}}',
          r'\overset{\hand{\text{adjunction}}}',
          'The explanatory adjunction label above the isomorphism is set as mathematical variables.',
          'Wrap only the English label in text mode inside its existing handwritten overset.'),
]


def main():
    meta = {m['key']: m for m in json.loads((P.parent/'inputs/text/records/PAGES_PS.json').read_text())}
    overrides = []
    for f in (P/'records').glob('MASTER_VARIANTS_*.json'):
        overrides.extend(json.loads(f.read_text()))
    preamble = (P/'scripts/reader_preamble.tex').read_text()
    keys = list(dict.fromkeys(r['key'] for r in PATCHES))
    manifest = []
    for key in keys:
        source = (P/'checked_pages'/f'{key}.tex').read_text()
        original = source
        source_sha = hashlib.sha256(source.encode()).hexdigest()
        for index, row in enumerate(PATCHES):
            if row['key'] != key:
                continue
            assert source.count(row['before']) == 1, (key, row['before'], source.count(row['before']))
            row['source_line'] = source.count('\n', 0, source.index(row['before'])) + 1
            row['source_sha256_before_batch'] = source_sha
            row['id'] = f'MATH-PROSE:{key}:{index+1:02d}'
            source = source.replace(row['before'], row['after'], 1)
        vv = []
        annotated = explicit_transform(source, key, vv, [o for o in overrides if o['key'] == key])
        assert select_variant(annotated, 0) == source
        m = meta[key]
        url = f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{m['cote']}.pdf\\#page={m['pdf_page']}"
        body = '\\pssource{'+key+'}{'+m['cote']+'/'+str(m['site'])+'}{'+url+'}\n'
        body += ''.join('\\psnumber{'+v.id+'}{'+str(v.number)+'}\n' for v in vv)
        body += annotated+'\n'
        if vv:
            body += '\\psapparatusstart\n'
            for v in vv:
                before = '$'+v.before+'$' if v.in_math else v.before
                after = '$'+v.after+'$' if v.in_math and v.after else v.after
                body += '\\psentry{'+v.id+'}{'+str(v.number)+'}{'+texescape(v.kind)+'}{'+before+'}{'+after+'}{'+texescape(v.reason)+'}\n'
            body += '\\psapparatusend\n'
        tex = ('\\def\\EditionMode{1}\n\\def\\EditionLabel{Local math-prose proof}\n'
               '\\def\\EditionStatus{Proposed wrappers; canonical source unchanged}\n'+preamble+
               '\n\\begin{document}\n'+body+'\n\\end{document}\n')
        out = P/'qa/proofs'/f'{key}_math_prose_apparatus.tex'
        out.write_text(tex)
        proposed = P/'qa/proofs'/f'{key}_math_prose_proposed_source.tex'
        proposed.write_text(source)
        assert (P/'checked_pages'/f'{key}.tex').read_text() == original
        manifest.append({'key':key, 'source_sha256':source_sha,
                         'proposed_source':str(proposed.relative_to(P)),
                         'proposed_source_sha256':hashlib.sha256(source.encode()).hexdigest(),
                         'tex':str(out.relative_to(P)), 'variants':len(vv)})
    (P/'records/MATH_PROSE_PROPOSED_PATCHES.json').write_text(json.dumps(PATCHES, indent=2)+'\n')
    (P/'records/MATH_PROSE_PROOF_BUILD_MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'patches':len(PATCHES), 'source_pages':len(keys), 'proofs':[r['tex'] for r in manifest]}))


if __name__ == '__main__':
    main()
