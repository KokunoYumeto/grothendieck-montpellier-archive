"""Keep completed errata in their logical order and record simple source edits."""
from pathlib import Path
from time import perf_counter

start = perf_counter()
root = Path(__file__).resolve().parents[1]
path = root / "sections/algebra_D.tex"
text = path.read_text()
first = text.index(r"\subsubsection{The meromorphic-section corrections")
last = text.find(r"\begin{lemma}[Proved: closed quotients", first)
if last >= 0:
    block = text[first:last]
    text = text[:first] + text[last:]
    path.write_text(text.rstrip() + "\n\n" + block.rstrip() + "\n")
    print("Moved D12--D16 after D11:", len(block), "characters")
else:
    print("D12--D16 already follow D11")
print("Numbered statements:", path.read_text().count(r"\label{SA23-D-"))
print("Seconds:", round(perf_counter()-start, 6))
