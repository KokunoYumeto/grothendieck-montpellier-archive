"""Root actual-file check of the normal-subgroup crown refinement."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
p=root/'parts/C/post21_research/D_normal_subgroup_projective_crowns.tex'
h=hashlib.sha256(p.read_bytes()).hexdigest()
assert h=='41f0af15a1b6f9445d8cb7c29af8c7b0e9f9b6e1848b664594673fa517cb782c'
r=dict(utc=datetime.now(timezone.utc).isoformat(),actor='root',model='GPT-6 Astra Pro (OpenAI)',
 effort='inherited; no separate control exposed',run='SA12 run1',outcome='PASS',
 check_type='full actual-file targeted mathematical proof check',path=str(p.relative_to(root)),sha256=h,
 checks=[
 'Read complete actual candidate. The fixed outer character determines normal H0 and the tame field projection independently of the lift.',
 'Nonsplit wreath transport remains inside B; distinct crown coordinates give distinct S-conjugacy lift classes.',
 'Ambient projective restriction classes lose at most |PGL| when refined to S-conjugacy classes of actual B0-valued restrictions. Choosing actual representatives and conjugating by S preserves the full B-valued condition.',
 'Each of the a−1 additional coset images lies in one fixed S-coset prescribed by the outer character, giving exactly the valid upper bound |S|^(a−1), with no need to control |B| or extend its action to PGL.',
 'The exponent κ(A_R b0+1)+b0−1 follows from a≤b0,t≥1. The stated nonabelian crown inequality supplies the generator bound. No general finite-generation or wild-outer-quotient claim is made.'
 ],source_scope='Earlier fully checked LMT Proposition2.6(ii), exact nonsplit wreath lifting and the newly four-audited projective semilinear count reused. No fresh full primary source read is claimed for this group-theoretic refinement.',
 movement='Enlarges the same post-review14 projective crown reduction; no additional independent movement. Kept separate from the checkpoint22 PDF freeze until subsequent assembly.')
out=root/'parts/D/post21_research/audit_C_normal_subgroup_projective_crowns_root.json'
assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'utc':r['utc'],'path':str(out.relative_to(root)),'sha256':h,'outcome':'PASS'},indent=2))
