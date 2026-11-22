// Exact A151 checker reconstructed from the full original function in chat.
// The function body is the 26-test BigInt rational certificate supplied by
// maximal_locus2; the Node runner below is new recovery infrastructure.
function auditA151(){
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>Q(-a.n,a.d),sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a.n*b.n,a.d*b.d),div=(a,b)=>Q(a.n*b.d,a.d*b.n),eq=(a,b)=>a.n===b.n&&a.d===b.d,lt=(a,b)=>a.n*b.d<b.n*a.d,le=(a,b)=>!lt(b,a),fmt=a=>a.d===1n?String(a.n):String(a.n)+'/'+String(a.d);
const z=Q(0),one=Q(1),two=Q(2);
const trim=p=>{p=p.slice();while(p.length>1&&eq(p[p.length-1],z))p.pop();return p;};
const pa=(p,q)=>trim(Array.from({length:Math.max(p.length,q.length)},(_,i)=>add(p[i]||z,q[i]||z))),ps=(p,a)=>trim(p.map(x=>mul(x,a)));
const pm=(p,q)=>{const out=Array.from({length:p.length+q.length-1},()=>z);p.forEach((a,i)=>q.forEach((b,j)=>{out[i+j]=add(out[i+j],mul(a,b));}));return trim(out);};
const peq=(p,q)=>{p=trim(p);q=trim(q);return p.length===q.length&&p.every((a,i)=>eq(a,q[i]));},pv=(p,x)=>p.reduceRight((v,a)=>add(mul(v,x),a),z);
const checks=[],check=(name,ok,detail)=>{checks.push({name,pass:!!ok,detail});if(!ok)throw Error('FAIL: '+name);};
const eps=Q(1,4),amax=Q(1,4),cmax=mul(eps,amax);
check('cmax',eq(cmax,Q(1,16)),fmt(cmax));
check('amplitude square identity',peq([Q(1,4),Q(-1),one],pm([Q(-1,2),one],[Q(-1,2),one])),'1/4-r(1-r)=(r-1/2)^2');
const tplus=y=>[y,add(mul(two,y),one)],tminus=y=>[y,sub(one,mul(two,y))];
check('left join at -1/2',peq(tplus(Q(-1,2)),[Q(-1,2)]),'T_left(-1/2)=-1/2 for every c');
check('middle join at 0',peq(tplus(z),tminus(z))&&peq(tplus(z),[z,one]),'both pieces equal c');
check('right join at 1/2',peq(tminus(Q(1,2)),[Q(1,2)]),'T_right(1/2)=1/2 for every c');
const slopes=[[one],[one,two],[one,neg(two)],[one]];
slopes.forEach((s,i)=>[z,cmax].forEach(c=>{const value=pv(s,c);check('slope '+i+' at c='+fmt(c),le(Q(7,8),value)&&le(value,Q(9,8)),fmt(value)+' in [7/8,9/8]');}));
check('inverse denominators positive',lt(z,Q(7,8)),'1-2c>=7/8>0; 1+2c>=1');
check('forward spatial constant squared',lt(Q(25,8),Q(4)),'25/8<4');
check('inverse spatial constant squared',lt(Q(162,49),Q(4)),'162/49<4');
check('inverse vertical coefficient',eq(div(one,Q(7,8)),Q(8,7)),'1/(7/8)=8/7');
check('inverse cross coefficient',eq(div(eps,Q(7,8)),Q(2,7)),'(1/4)/(7/8)=2/7');
check('inverse block coefficient',eq(add(one,Q(2,7)),Q(9,7)),'1+2/7=9/7');
const angular=div(Q(3),eps),loop=mul(angular,Q(8));
check('angular comparison constant',eq(angular,Q(12)),fmt(angular));
check('loop comparison constant',eq(loop,Q(96)),fmt(loop));
check('shrink constant',eq(div(loop,Q(100)),Q(24,25)),'96/100=24/25');
check('strict contradiction constant',lt(Q(24,25),two),'24/25<2');
check('positive gap after clearing 1+L',peq(pa(ps([one,one],Q(24,25)),ps([z,one],Q(-96,100))),[Q(24,25)]),'(24/25)(1+L)-(96/100)L=24/25>0');
check('tent maximum, first signed comparison',peq(pa([z,one],ps([z,neg(one)],Q(-1))),[z,two]),'delta-(-delta)=2delta>=0');
check('tent maximum, second signed comparison',peq(pa([z,one],ps([z,neg(one)],Q(-1))),[z,two]),'b-(-b)=2b>=0; b<=0 follows by replacing b with -b');
return{theorem:'A151',arithmetic:'exact normalized BigInt rationals; no floating-point sampling',domain:'0<=r<=1,0<=c<=1/16; nonnegative L,b,delta where stated',check_count:checks.length,all_pass:checks.every(c=>c.pass),checks,scope:'Finite algebraic certificate only; compactness, cube-boundary invariance, nearest-point existence, fine subdivision and ray last-exit are proved in the written argument.'};
}

if (require.main === module) {
  const fs = require('fs');
  const path = require('path');
  const started = process.hrtime.bigint();
  const result = auditA151();
  result.elapsed_seconds = Number(process.hrtime.bigint() - started) / 1e9;
  result.observed_at = new Date().toISOString();
  result.recovery_provenance = 'Original 26-test function recovered from complete chat text; Node runner newly added after workspace restoration.';
  const output = process.argv[2] || path.resolve(__dirname, '../logs/check_A151_exact.json');
  fs.mkdirSync(path.dirname(output), {recursive:true});
  fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
  process.stdout.write(JSON.stringify({check_count:result.check_count, all_pass:result.all_pass, elapsed_seconds:result.elapsed_seconds, output})+'\n');
}
module.exports = {auditA151};

