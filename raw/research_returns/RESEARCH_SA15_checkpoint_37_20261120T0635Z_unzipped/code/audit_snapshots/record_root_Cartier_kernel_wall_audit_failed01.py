"""Retain full root audit of the conditional Cartier-wall inertia criterion."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/monodromy/post_CP30_Cartier_kernel_wall_inertia_candidate.tex'
expected='b6eb395dbbeafb4587486b34c22af5070af538b45cd8784cf48e3acdcf2be163'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
out=w/'outputs/root_Cartier_kernel_wall_audit.json'
snapshot=w/'notes/root_Cartier_kernel_wall_audited_candidate.tex'
assert not out.exists() and not snapshot.exists();shutil.copy2(p,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:maximal-kernel-variation-stable-loss','prop:birational-Cartier-kernel-wall-inertia','rem:Cartier-kernel-wall-inertia-scope']
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire three-label stable candidate read and independently rederived; full earlier moving-kernel Artin-Schreier proof reread through its conclusion. No new numerical computation or primary-source retrieval claimed.',
 'proof_checks':[
  'The first imageI of a rankr-1 linearized Frobenius is a subbundle after shrinking. Failure of the restrictionF^*I->I to be bijective is exactly containment of the unique kernel line inF^*I. A rational frame ofI in the constant ambient bundle has squared coordinates with zero ground-field differential; expressing the kernel in that frame bounds its projective differential rank byr-2. This contradicts the assumedr-1 and proves stable loss exactlyone.',
  'On the common maximum-rank open the differentiated actual left-kernel equation identifiesdκ withB_lambda onW/ks. The second rank hypothesis makesdκ an isomorphism. Thusκ is etale there, with no identification ofM_s itself as alternating.',
  'Atq=lambda_s(s^[2])=0 its differential is dλ_s evaluated ons^[2]. That evaluation is a nonzero functional on the projective target tangent quotient. Consequentlyq cuts a smooth reduced divisor wherever nonempty; generator changes multiply its differential by a unit.',
  'The full transpose gives(W')^*/kλ_s isomorphic tos-perp. Restricting to(s^[2])-perp has kernelkλ_s precisely onq=0 and determinant a unit timesq by the hyperplane-projection determinant. Hence first relative corankone and simple determinant order hold exactly.',
  'The actual linearized relative kernel isκ restricted to the wall, with differential rankN-2. The Euler bundle on a coefficient chart lies in the constantW*-bundle, and its Frobenius pullback lies in(W')*. Applying the first lemma withr=N-1 gives stable rankN-2, so every hypothesis of the full moving-kernel inertia lemma is verified.',
  'The re-read strict-henselian proof usesr-1 regular fixed unit sections and a last coefficienta=tc. The independent kernel differentials force every nonzero F2-combination of the Artin-Schreier classesb_i/a² to have a nonsquare leading coefficient at ordert^-2; no such class is an AS coboundary. It therefore gives the entire hyperplane radical, including inseparable residue phenomena.'
 ],
 'dependency_reread':'agents/monodromy/mixed_degree_one_uniform_full_groups.tex, complete lemma:moving-kernel-full-root-inertia-candidate and proof; current root differential criterion also freshly read in the common-incidence audit.',
 'scope_guard':'The wall must be nonempty inside the common maximum-rank open. That condition and the global radical generation/connected nonzero Lang-cover condition remain open. This conditional theorem asserts no new unconditional exact-group degree.',
 'numerical_program_executed':False}
out.write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/root_check_events.tsv').open('a',newline='')as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','independent re-proof',
  'PASS: complete stable-loss, simple-wall and full-inertia proof rederived; complete earlier AS dependency reread. Requires nonempty wall inside common open and does not prove global generation. Details: outputs/root_Cartier_kernel_wall_audit.json.'])
with(w/'notes/checkpoint31_changes.md').open('a')as f:
 f.write('\n## Conditional wall inertia and the unresolved intersection\n\nThe full root audit of the three-label moving-kernel wall criterion passed at '+now+'. Maximal kernel variation excludes a further nilpotent step. On any nonempty common Cartier wall the determinant has orderone, stable loss is exactlyone and the actual local inertia is the full hyperplane radical. Nonemptiness inside the common open and global generation remain required. The exact universal Fermat-remainder probe completed at01:46:50.036880 UTC in3.5751673499908065 seconds:399 supports have explicit monomial exclusions; the original111 symmetric-missing supports plus the full nine-coordinate support remain. The eight-support phase checks retain only the nine characters. This is an exploratory algebraic calculation, not a proof of the remaining full-coordinate exclusion or a new monodromy case. Its full program, outputs and streams are retained.\n')
print(json.dumps({'status':'PASS','actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))
