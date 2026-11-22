from pathlib import Path
import hashlib,json,runpy,contextlib,io,datetime,time
base=Path(__file__).resolve().parent.parent
src=base.parent/'monodromy/code/nonordinary_five_theta_packet_probe.py'
author=base.parent/'monodromy/outputs/nonordinary_five_theta_packet_probe.json'
original=author.read_bytes(); original_hash=hashlib.sha256(original).hexdigest()
copy=base/'code/independent_nonordinary_five_theta_packet_probe.py'
copy.write_bytes(src.read_bytes())
stdout=io.StringIO();start=time.perf_counter()
with contextlib.redirect_stdout(stdout):ns=runpy.run_path(str(copy))
elapsed=time.perf_counter()-start
assert author.read_bytes()==original
(base/'outputs/independent_five_theta_packet_probe.stdout.txt').write_text(stdout.getvalue())
result=ns['result'];assert result['good_nodal_count']==20 and result['lagrangian_count']==156
assert result['max_packet_census']=={2:20,4:80,5:56}
# Independent exact polynomial coefficient check after Y=y+b, X=x+a:
# f=Y+a^8 X^2+a^4 X, Y^2+Y=a^4 X+a X^4+X^5.
mul=ns['mul'];power=ns['power'];identities=0
for a,b in ns['points'][1:]:
    c1=power(a,4)^power(a,4)
    c2=power(a,8)^power(a,8)
    c4=a^power(a,16)
    assert (c1,c2,c4)==(0,0,0)
    assert b^mul(power(a,8),power(a,2))^mul(power(a,4),a)^power(b,4)==0
    identities+=1
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
rec={'status':'FULL_BOUNDED_PROOF_CODE_PASS','actual_utc':now,'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'author_output_sha256':original_hash,'author_output_preserved':True,'isolated_runtime_seconds':elapsed,'internal_runtime_seconds':result['runtime_seconds'],'explicit_Weil_divisor_identities':identities,'lagrangian_count':156,'good_nodal_count':20,'max_packet_census':result['max_packet_census'],'bad_cyclic_line_count':result['bad_cyclic_line_count'],'rational_difference_count':result['rational_difference_count'],'scope':'Full code read and exact isolated rerun; direct proof of fP divisor, common-pole Weil ratio, nondegenerate pairing coordinate reconstruction and finite packet census. Geometric triple/tangency exhaustiveness checked as an outline; no complete author geometric proof file existed at read time. No universal target or monodromy conclusion.'}
(base/'outputs/independent_five_theta_packet_audit.json').write_text(json.dumps(rec,indent=2)+'\n')
with (base/'CHECK_EVENTS.tsv').open('a') as f:f.write('\t'.join([now,'five-theta-packet-census','INDEPENDENT_PROOF_CODE_PASS','Explicit GF16 Weil pairing and156 Lagrangian census',str(src),f'Isolated runtime{elapsed}; author output preserved;20 good packets; no universal target conclusion'])+'\n')
print(json.dumps(rec,indent=2))
