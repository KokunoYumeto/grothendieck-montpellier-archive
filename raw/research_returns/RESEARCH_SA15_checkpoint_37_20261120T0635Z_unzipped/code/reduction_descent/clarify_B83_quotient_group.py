from pathlib import Path
import hashlib,json
own=Path(__file__).resolve().parents[1]
p=own/'B_first_wild_swapped_quotients_candidate.tex';raw=p.read_bytes()
pre=own/'notes/B_first_wild_swapped_quotients.initial.tex'
assert not pre.exists();pre.write_bytes(raw)
old=r'''If the common quotient residual action were tame, it would
be trivial over \(L\), since its two diagonal line
characters have order dividing \(p-1\). The preceding
lemma would equate these unequal integers. Thus its
residual wild action is nontrivial.'''
new=r'''The original third-level image over \(L\) is a
\(p\)-group, since its first-level module is rational.
The actual quotient comparison (B-RD83.3) is a subquotient
of that module, so its image over \(L\) is also a
\(p\)-group. If its residual action were tame, it would
therefore be trivial. The preceding lemma would then
equate these unequal integers. Thus its residual wild
action is nontrivial. The actual old first-level image
\(M[p]/J\subset(M/J)[p]\) also supplies an invariant
line, so this is a nontrivial unipotent residual action.'''
s=raw.decode();assert s.count(old)==1;s=s.replace(old,new);p.write_text(s)
print(json.dumps({'preserved':str(pre),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
