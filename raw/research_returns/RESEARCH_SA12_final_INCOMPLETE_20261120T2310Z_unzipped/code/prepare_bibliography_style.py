"""Keep apalike/natbib output while allowing more than26 equal-author years."""
from pathlib import Path
import hashlib, json
root=Path(__file__).resolve().parents[1]
source=Path('/usr/share/texlive/texmf-dist/bibtex/bst/base/apalike.bst')
text=source.read_text()
text=text.replace('INTEGERS { last.extra.num }','INTEGERS { last.extra.num suffix.num suffix.quot suffix.rem }')
function=r'''
STRINGS { suffix.text }

FUNCTION {set.alpha.extra.label}
{ "" 'suffix.text :=
  last.extra.num 'suffix.num :=
  { suffix.num #0 > }
  { suffix.num #1 - 'suffix.rem :=
    #0 'suffix.quot :=
    { suffix.rem #25 > }
    { suffix.rem #26 - 'suffix.rem :=
      suffix.quot #1 + 'suffix.quot :=
    }
    while$
    suffix.rem #97 + int.to.chr$ suffix.text * 'suffix.text :=
    suffix.quot 'suffix.num :=
  }
  while$
  suffix.text 'extra.label :=
}

'''
text=text.replace('FUNCTION {forward.pass}',function+'FUNCTION {forward.pass}')
text=text.replace("last.extra.num int.to.chr$ 'extra.label :=",'set.alpha.extra.label')
text=text.replace('"a" chr.to.int$ \'last.extra.num :=',"#1 'last.extra.num :=")
destination=root/'code/sa12-apalike.bst'
destination.write_text(text)
paper=root/'RESEARCH_SA12_paper.tex'
s=paper.read_text().replace('\\bibliographystyle{apalike}','\\bibliographystyle{code/sa12-apalike}')
paper.write_text(s)
aux=root/'build/RESEARCH_SA12_paper.aux'
if aux.exists():
    aux.write_text(aux.read_text().replace('\\bibstyle{apalike}','\\bibstyle{code/sa12-apalike}'))
record={'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'destination':str(destination.relative_to(root)),
        'change':'Only equal-author/equal-year suffixes: a,...,z,aa,... instead of invalid ASCII after z.'}
(root/'code/output/bibliography_style.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
