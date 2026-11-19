from pathlib import Path
OUT=Path(__file__).resolve().parent
TASK=OUT.parent.name
pages=sorted((OUT/'pages').glob('*.tex'))
(OUT/f'{TASK}_transcription.tex').write_text('\n'.join(p.read_text() for p in pages))
(OUT/f'{TASK}_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{'+TASK+'_transcription}\n\\end{document}\n')
print('Assembled',len(pages),'current pages')
