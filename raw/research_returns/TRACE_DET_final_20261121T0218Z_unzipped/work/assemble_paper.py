from pathlib import Path
root=Path(__file__).resolve().parent.parent
w=root/'work'
core=(w/'paper_core.tex').read_text()
marker=r"\section{TOY-01--02:"
pos=core.index(marker)
parts=[core[:pos]]
parts += [(w/f'paper_{name}.tex').read_text() for name in ['actual_determinants','signed_kernel','positive_kernel','period_frame','bessel_projector','bessel_weights','endpoint','resolvent_bridge','weighted_endpoint','weil_bridge','arithmetic_kernel','bessel_boost']]
parts += [core[pos:]]
parts += [(w/f'paper_{name}.tex').read_text() for name in ['masullo','masullo_green','masullo_bridge','masullo_characters','masullo_character_metric','programmes','archive','end']]
out = root/'deliverables' if (root/'deliverables').is_dir() else root
(out/'TRACE_DET.tex').write_text('\n'.join(parts))
