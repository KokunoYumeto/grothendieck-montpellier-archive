from pathlib import Path
root=Path(__file__).resolve().parent.parent
w=root/'work'
core=(w/'paper_core.tex').read_text()
marker=r"\section{TOY-01--02:"
pos=core.index(marker)
parts=[core[:pos],(w/'paper_actual_determinants.tex').read_text(),(w/'paper_endpoint.tex').read_text(),(w/'paper_resolvent_bridge.tex').read_text(),(w/'paper_weil_bridge.tex').read_text(),core[pos:]]
parts += [(w/f'paper_{name}.tex').read_text() for name in ['masullo','masullo_green','masullo_bridge','programmes','archive','end']]
(root/'deliverables'/'TRACE_DET.tex').write_text('\n'.join(parts))
