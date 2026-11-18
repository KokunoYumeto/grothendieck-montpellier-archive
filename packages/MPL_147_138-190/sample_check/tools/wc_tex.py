# Word estimate for a transcription page: prose words (struck text included),
# plus one word per formula and one more per relation sign or comma in it.
import re, sys, glob, os

BS = chr(92)
RELNAMES = ('simeq|cong|sim|approx|equiv|neq|ne|leq|geq|le|ge|subset|subseteq|supset|supseteq|in|ni|notin|to|'
            'longrightarrow|rightarrow|leftarrow|longleftarrow|longleftrightarrow|leftrightarrow|mapsto|longmapsto|'
            'hookrightarrow|hookleftarrow|twoheadrightarrow|Rightarrow|Leftarrow|Longrightarrow|Leftrightarrow|'
            'Longleftrightarrow|iff|implies|xrightarrow|xleftarrow|rightrightarrows|rightleftarrows|leftrightarrows|'
            'arrow|ar')
REL = re.compile('(' + BS + BS + '(?:' + RELNAMES + ')(?![A-Za-z])|=|<|>|,)')
ENV = re.compile(BS + BS + r'begin\{(tikzcd|tikzpicture|equation\*?|align\*?|aligned|array|gather\*?|center)\}.*?' + BS + BS + r'end\{\1\}', re.S)
DISP = re.compile(BS + BS + r'\[.*?' + BS + BS + r'\]', re.S)
DD = re.compile(r'\$\$.*?\$\$', re.S)
PAR = re.compile(BS + BS + r'\(.*?' + BS + BS + r'\)', re.S)
INL = re.compile(r'(?<!' + BS + BS + r')\$.*?(?<!' + BS + BS + r')\$', re.S)
COMMENT = re.compile(r'(?<!' + BS + BS + r')%.*')
SCANPAGE = re.compile(BS + BS + r'scanpage\{[^}]*\}')
MACRO = re.compile(BS + BS + r'[A-Za-z]+\*?')


def formulas_and_prose(s):
    s = COMMENT.sub('', s)
    forms = []

    def grab(m):
        forms.append(m.group(0))
        return ' '
    for rx in (ENV, DISP, DD, PAR, INL):
        s = rx.sub(grab, s)
    return forms, s


def count(s):
    forms, prose = formulas_and_prose(s)
    n = 0
    for f in forms:
        n += 1 + len(REL.findall(f))
    prose = SCANPAGE.sub(' ', prose)
    prose = MACRO.sub(' ', prose)
    prose = re.sub(r'[{}\[\]|~]', ' ', prose)
    words = re.findall(r"[0-9A-Za-zÀ-ÿ'’\.\-°]+", prose)
    words = [w for w in words if re.search(r'[0-9A-Za-zÀ-ÿ]', w)]
    return n + len(words), len(words), len(forms)


if __name__ == '__main__':
    tot = 0
    for pat in sys.argv[1:]:
        for f in sorted(glob.glob(pat)):
            s = open(f, encoding='utf-8').read()
            t, w, fm = count(s)
            tot += t
            print(os.path.basename(f), t, w, fm)
    print('TOTAL', tot)
