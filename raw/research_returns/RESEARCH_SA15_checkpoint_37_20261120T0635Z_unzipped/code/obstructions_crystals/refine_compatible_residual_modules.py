"""Preserve the audited draft; type the continuation open and prove exact rounding."""
from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
p=own/'post_CP34_compatible_residual_modules_candidate.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='4c9a210e0434382b8ff5bcda70fbb1f45b8d1532f9783b0a0dedb4a44cc82b2c'
assert sha(p)==expected
before=p.read_text()
old=r'''The narrow deck-slice theorem for \(\eta_H\) likewise gives
that the source \(\mathcal K_H\) has zero projection to the
central degree-one Lang space on a dense cubic slice open.
The central sharp open containing \(S_D\) is connected, so
the same zero-morphism argument extends this inclusion to
\(S_D\). Under the actual pullback to the target fibre, its
central projector is precisely \(e_D\) restricted to
\(e_HV\). Indeed the quotient deck group is \(D/H\), and
averaging its cosets after the odd \(H\)-average gives
\(e_D\). Thus'''
new=r'''For this further continuation, define \(R_H\) to be the open
in \(\mathbf P(H^0(B,3\Theta_B))\) where the degree-one curve
and its \(\eta_H\)-pullback are smooth and sharp and all
nontrivial \(\eta_H\)-character multiplication blocks are
invertible. The explicit central character construction makes
\(R_H\) nonempty and integral, and \(S_D\subset R_H\).
The pullback of the source \(\mathcal K_H\) and its central
averaging projector are therefore defined throughout \(R_H\).
The narrow deck-slice theorem for \(\eta_H\) says that their
composition is zero on a nonempty open of \(R_H\). Connectedness
and the same zero-morphism argument extend this to all of
\(R_H\), hence to \(S_D\). In particular no continuation is
made across a point where the intermediate pullback is not sharp.
Under the actual pullback to the target fibre, this central
projector is precisely \(e_D\) restricted to \(e_HV\).
Indeed the quotient deck group is \(D/H\), and averaging its
cosets after the odd \(H\)-average gives \(e_D\). Thus'''
assert before.count(old)==1
after=before.replace(old,new)
old2=r'''At \(\ell=17\), the quotient dimension is at least 782 and
the exceptional dimension is at most 1818, in total rank 2600.'''
new2=r'''There is also the sharper exact integer bound. Put
\(f=\operatorname{ord}_\ell(2)\). Then
\[
 \dim K\le (\ell+1)f
                 \left\lfloor\frac{6\ell-1}{f}\right\rfloor,
 \qquad
 \dim(V/K)\ge9\ell^2-1-(\ell+1)f
                 \left\lfloor\frac{6\ell-1}{f}\right\rfloor.
 \tag{DE-CR10}
\]
In the fixed-principal case this sharper exceptional bound can
likewise replace the exponent in the subtracted term of (DE-CR9).
At \(\ell=17\), one has \(f=8\), each source exceptional
dimension is at most 96, and the target quotient dimension is
at least 872 with exceptional dimension at most 1728, in total
rank 2600.'''
assert after.count(old2)==1
after=after.replace(old2,new2)
old3=r'''The numerical \(\ell=17\) values are direct substitutions;
no finite experiment enters the proof.'''
new3=r'''To prove the refinement, work at the same central geometric
point. Every deck translation of \(\eta_H\), whose group is
\(D/H\simeq C_\ell\), acts on the entire source universal
family and its smooth, sharp coefficient open. It fixes the
central section, because that section is pulled back from \(B\).
Functoriality of the fibre representation therefore makes its
linear action on the source Lang fibre normalize the source
geometric monodromy image. Since \(K_H\) is that image's unique
maximal proper submodule, it is invariant under these deck
translations. Thus it is an actual \(\mathbf F_2[C_\ell]\)-module.
Its averaging projector is zero by (DE-CR6).

The algebra \(\mathbf F_2[C_\ell]\) is semisimple because
\(\ell\) is odd. Every nontrivial simple module has dimension
\(f=\operatorname{ord}_\ell(2)\): the nonidentity \(\ell\)-th
roots have Frobenius orbits of exactly that length. Since the
trivial summand has been excluded, \(\dim K_H\) is a multiple
of \(f\). Its wedge bound \(\dim K_H\le6\ell-1\) therefore
improves to \(f\lfloor(6\ell-1)/f\rfloor\). Summing the
actual direct-sum inclusion (DE-CR4) proves (DE-CR10).
For \(\ell=17\), \(2^4\equiv-1\pmod {17}\) and
\(2^8\equiv1\pmod {17}\), while no proper divisor of eight
gives one. Hence \(f=8\), and the displayed numbers follow
by substitution. No finite experiment enters the proof.'''
assert after.count(old3)==1
after=after.replace(old3,new3)
history=own/'notes/CP34_compatible_residual_typing_rounding'
history.mkdir(exist_ok=False)
(history/'before.tex').write_bytes(p.read_bytes())
recordpath=own/'compatible_residual_modules_candidate_record.json'
(history/'candidate_record.before.json').write_bytes(recordpath.read_bytes())
(history/'changes.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='audited-draft',tofile='typed-rounded-draft')))
p.write_text(after)
now=datetime.now(timezone.utc).isoformat()
r=json.loads(recordpath.read_text())
r.update({'actual_utc':now,'candidate_sha256':sha(p),
          'prior_candidate_sha256':expected,
          'repair':'Defined the exact connected continuation open R_H where the source pullback is sharp. Added complete deck-normalizer stability and F2 cyclic-module proof of integer rounding.',
          'history':str(history.relative_to(root)),
          'scope':'Full proof awaiting final independent audits; exact source-residual inclusion, compatible sum and rounded wedge consequence. At ell17: quotient>=872 and exceptional<=1728. No K=0 claim.'})
recordpath.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':'FINAL CANDIDATE READY','actual_utc':now,'candidate':r['candidate'],
                  'candidate_sha256':r['candidate_sha256'],'history':r['history']}))
