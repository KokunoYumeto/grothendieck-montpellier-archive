"""Read exact numbered source ranges and keep the output as evidence."""
from pathlib import Path
import sys
P=Path(__file__).resolve().parents[1];ROOT=P.parents[2]
P.joinpath('outputs').mkdir(exist_ok=True)
file=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3])
lines=(ROOT/file).read_text().splitlines()
out='\n'.join(f'{i+1:5d}\t{lines[i]}' for i in range(a-1,min(b,len(lines))))+'\n'
(P/'outputs'/('read_'+Path(file).stem+f'_{a}_{b}.txt')).write_text(out)
print(out)
