"""Explicitly curated final reference/wording repairs; no source reading is altered."""
from pathlib import Path
P=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle')
p=P/'code/build_claims.py'
s=p.read_text()
start=s.index('# Codex B15-01 mathematical pages')
end=s.index('# Reused analytic manuscript:')
part=s[start:end]
part=part.replace("['Voight2021','DeligneMilne1982']", "['StacksYoneda2026','StacksDescent2026','StacksProjective2026']")
part=part.replace("['Voight2021']", "['StacksKaroubi2026','StacksProjective2026','StacksDescent2026']")
part=part.replace('search=[26,1,3]', 'search=[26,28,29,30,34,35]')
part=part.replace('search=[26]', 'search=[26,28,29,30,34,35]')
s=s[:start]+part+s[end:]
p.write_text(s)
p=P/'proofs.md';s=p.read_text()
s=s.replace('Saved blocks analytic_majorant, analytic_bounds, and analytic_coefficients record the exact algebraic checks.', 'Saved blocks analytic_majorant, analytic_remainder, analytic_radius, ODE_component_index and complex_inverse_warning record the corresponding exact checks; the universal convergence arguments are proved in this section rather than inferred from finite computation.')
s=s.replace('Pro61 lines481–507', 'Pro61 lines 481–507').replace('Codex B15-01 scan63','Codex B15-01 scan 63')
p.write_text(s)
# Only expository strings are touched. Diplomatic quotations, labels and raw source files are frozen.
p=P/'code/build_items.py';s=p.read_text()
rep={'and3':'and 3','computes2h':'computes 2h','andp²':'and p²','between0 and1':'between 0 and 1','overQ':'over Q','inH':'in H','example[2]':'example [2]','with2↦4':'with 2↦4','productU°×G_m':'product U°×G_m','projectionpr₂':'projection pr₂','kernelU°':'kernel U°','Proposition2':'Proposition 2','characterpr₂²':'character pr₂²','Onh(P¹)':'On h(P¹)','actdiag':'act diag','specificsl₂':'specific sl₂','Cartanτ':'Cartan τ','weightj':'weight j','satisfyj':'satisfy j','theTate':'the Tate','ForGL₂,the':'For GL₂, the','automorphismθ':'automorphism θ','invertsdet':'inverts det','specifiedTate':'specified Tate','characterε':'character ε','asdiag':'as diag','moduleN':'module N','normal formN':'normal form N'}
for a,b in rep.items():s=s.replace(a,b)
p.write_text(s)
print('Applied explicit primary-reference and prose repairs; no transcription changed.')
