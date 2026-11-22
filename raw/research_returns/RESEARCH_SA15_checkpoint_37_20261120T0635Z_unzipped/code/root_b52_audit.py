"""Root full CM-subclass proof/source audit and author-preserving exact rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json,hashlib
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_tame_CM_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_tame_CM_gate.json'
summary=w/'outputs/root_b52_audit.json'
assert not dest.exists() and not summary.exists()
before=author.read_bytes();old=Path.write_text;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    assert path.resolve()==author.resolve()
    return old(dest,data,*args,**kwargs)
try:
    Path.write_text=write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=old
    (w/'outputs/root_verify_tame_CM_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('lem:B-RD52-CM','independent re-proof',
  'PASS: all hypotheses and the whole proof rederived. Generic endomorphisms after finite extension extend to the good model by the previously audited Tate full-faithfulness theorem, after clearing denominators for quasi-endomorphisms. Reduction is injective by the [p]-composition/least-valuation argument, also exactly original Hopkins-Gross4.2. Algebraically closed residue therefore forces finite-extension endomorphisms to descend to a faithful tame good field. The rational algebra embeds in the special height-two division algebra and acts on a two-dimensional Qp-space, so under CM it is quadratic. Ramified CM is excluded: for p3mod4 its finite normalizer order divides2(p-1) and all such roots have square reduced norm; for p1mod4 the generic semilinear normalizer has determinants plus/minus unit norms, again squares modulo p. In the unramified case the noncentral division-algebra normalizer coset has odd valuation and no units, hence all generic Galois action centralizes E. A nonsquare determinant gives a unit with non-Fp residue, generating O_E, so the Tate lattice is an actual free rank-one O_E-module.'),
 ('lem:B-RD52-LT','independent re-proof',
  'PASS: entire integral uniqueness and wild-layer proof rederived. The sum x=sum v^i lambda^(-i) satisfies vx=xlambda by noncommutative telescoping and reduces to the nonzero scalar p²-1, hence gives an integral unit conjugator. The height-two deformation parameter has a nontrivial mu_(p²-1) tangent weight. Averaging about the canonical fixed lift gives an exact eigenparameter; its multiplier minus1 is a unit, so an O_E-action forces that parameter to vanish. Tate full faithfulness supplies the action on the model. Thus the Tate character is the standard oriented Lubin-Tate character times a finite tame twist. The primitive p² polynomial (pT+T^(p²))^(p²-1)+p is Eisenstein over W(k), including arbitrary algebraically closed perfect k; all torsion points are O_E/p² multiples of a primitive point, so the full division group is (O_E/p²)^units. Its first wild layer of orderp² survives every tame good base extension. No finite-residue local class-field statement is silently extended.'),
 ('thm:B-RD52','independent re-proof',
  'PASS: full upper and lower assertions rederived in the potentially-CM potentially-supersingular height-two formal subclass, e=p-1, mu_p contained, p>=5. Equal p² torsion gives equal finite determinant; the square case is the previously proved B50 exclusion. In the nonsquare case, align tangent embeddings so both representations are theta times epsilon_i over the same O_E. The full wild first layer forces the mod-p intertwiner to centralize F_(p²), hence to be multiplication by a nonzero scalar. The remaining intertwining equations give equal finite twists modulo p and therefore exactly. The p-level counterexample uses the two effective finite twists omega and omega^(p²-p+1) of the standard Lubin-Tate group over W(Fpbar)[1/p](mu_p). Their mod-p exponents p and1 are Frobenius-conjugate, while finite exponents {1,p} and {2-p,2p-1} differ for every p>=5 and have equal primitive norms. The manuscript index in this subclass is exactly1. At least one non-CM model is therefore necessary in every remaining unrestricted p² ambiguity; no non-CM realization or exclusion is asserted.'),
 ('rem:B-RD52-scope','targeted proof check',
  'PASS: full scope and retained failure statement checked against the complete program. The initial structural matrix-equality failure and the corrected entrywise expansion remain separate, retained records. The finite code supports algebra only; it is not claimed to classify deformations or all potentially good groups.'),
 ('B52-ORIGINAL-SOURCES','used and rechecked in this run',
  'PASS: root freshly opened the indexed original Lubin-Tate1965 and read Lemma1 with full proof, Theorem1 with full proof pp381-383, and Theorem2(b),(d),(e) with full written proof pp383-384. Direct PDF URL first timed out; cached original retrieval then succeeded. Root freshly read original Hopkins-Gross1994 Proposition4.2 and full proof, Proposition5.7 with equations5.3-5.8, and the entire Proposition12.10 proof with its preceding arbitrary-residue local-A-algebra definition. Its finite source residue is not confused with the larger residue of R. The existing Tate1967 full-faithfulness audit and B49 faithful-tame proof were explicitly reused; no new Tate source opening or page-image inspection is claimed.'),
 ('B52-EXACT-CERTIFICATE','computation or formal certificate',
  f"PASS: complete program read then independently rerun, author output unchanged, {out['elapsed_seconds']} seconds. Checked {out['matrix_tests']} matrices, {out['norm_tests']} norms, {out['ramified_root_tests']} ramified-norm cases, {out['eisenstein_coefficients']} Eisenstein coefficients, {out['unit_conjugacy_telescoping_terms']} noncommutative telescoping terms and {len(out['lower_character_pairs'])} explicit lower character pairs. All exact identities passed.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',kind,result])
record={'status':'FULL PROOF/SOURCE/CODE PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],
        'author_output_sha256_unchanged':hashlib.sha256(before).hexdigest(),'events':len(events),
        'remaining_gate':'At least one of the two formal models in a putative unrestricted p² ambiguity must be non-CM. The unrestricted least index remains in{1,2}.',
        'fresh_source_refs':['turn598612481view0','turn598612481view1','turn598612481view2','turn598612481view3','turn598612481view4','turn368981258view0','turn368981258view2'],
        'failed_retrieval':'turn699496932view0 direct original Lubin-Tate PDF timeout, followed by successful cached original read.'}
summary.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
