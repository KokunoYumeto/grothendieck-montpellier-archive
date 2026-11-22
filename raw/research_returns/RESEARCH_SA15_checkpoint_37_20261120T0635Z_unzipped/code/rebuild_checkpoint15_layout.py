"""Preserve overflow evidence, shorten the prose lead-in, and rebuild CP15."""
from pathlib import Path
import shutil,subprocess,sys,json,datetime
w=Path(__file__).resolve().parents[1]
p=w/'agents/reduction_descent/B_p2_character_level3.tex'
dest=w/'outputs/checkpoint15_overflow_B43_input.tex';assert not dest.exists()
shutil.copy2(p,dest)
shutil.copy2(w/'RESEARCH_SA15_paper.log',w/'outputs/checkpoint15_overflow_build.log')
t=p.read_text();old='Independent author-output-preserving reruns of the full certificate passed\nin $0.5299817019986222$ and $0.6142895730008604$ seconds.'
assert old in t
p.write_text(t.replace(old,'Independent reruns took $0.5299817019986222$ and\n$0.6142895730008604$ seconds, preserving the author output.'))
for name in ['consolidate.py','number_statements.py','merge_registers.py','build_paper.py','merge_registers.py','update_current15.py']:
 subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['build_summary.json','build_console.txt']:
 shutil.copy2(w/'outputs'/name,w/'outputs'/('checkpoint15_final_'+name))
print(json.dumps({'status':'REBUILT','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
