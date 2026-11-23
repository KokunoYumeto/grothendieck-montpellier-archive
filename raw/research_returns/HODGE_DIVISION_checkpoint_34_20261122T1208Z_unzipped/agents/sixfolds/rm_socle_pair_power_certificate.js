function powerSocleCertificate() {
  const started = new Date().toISOString();
  const startMs = Date.now();
  const assert = (b,s) => { if (!b) throw new Error(s); };
  const safe = x => { assert(Number.isSafeInteger(x),"unsafe integer"); return x; };
  const exps = [];
  for(let i=0;i<81;i++) { let j=i; const a=[]; for(let k=0;k<4;k++){a.push(j%3);j=Math.floor(j/3);} exps.push(a); }
  const idx = a => a[0]+3*a[1]+9*a[2]+27*a[3];
  const mm = (i,j) => { const a=exps[i].map((x,k)=>x+exps[j][k]); return a.some(x=>x>=3)?-1:idx(a); };
  const mono = (i,c=1) => c?new Map([[i,c]]):new Map();
  const add = (a,b,sgn=1) => { const c=new Map(a); for(const [i,x] of b){const y=safe((c.get(i)||0)+sgn*x);if(y)c.set(i,y);else c.delete(i);}return c; };
  const scale = (a,t) => {const c=new Map();for(const [i,x]of a){const y=safe(x*t);if(y)c.set(i,y);}return c;};
  const mul = (a,b) => { const c=new Map();for(const [i,x]of a)for(const[j,y]of b){const k=mm(i,j);if(k<0)continue;const z=safe((c.get(k)||0)+safe(x*y));if(z)c.set(k,z);else c.delete(k);}return c; };
  const eq = (a,b) => a.size===b.size && [...a].every(([i,c])=>b.get(i)===c);
  const degree = i=>exps[i].reduce((a,b)=>a+b,0);
  const pairs = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const vi=[0,1,2,3].map(k=>{const a=[0,0,0,0];a[k]=2;return mono(idx(a));});
  const ui=[0,1,2,3].map(k=>{const a=[0,0,0,0];a[k]=1;return mono(idx(a));});
  const E=pairs.map(([i,j])=>mul(vi[i],vi[j]));
  const J=[[1,0,1,0],[0,1,0,1],[-3,5,-9,10],[-8,5,-16,15]];
  const p=pairs.map(([i,j])=>safe(J[i][0]*J[j][1]-J[i][1]*J[j][0]));
  const q=pairs.map(([i,j])=>safe(J[i][2]*J[j][3]-J[i][3]*J[j][2]));
  assert(JSON.stringify(p)==="[1,5,5,3,8,25]","p tuple");
  assert(JSON.stringify(q)==="[1,10,15,9,16,25]","q tuple");
  const perms=[];
  function perm(a,left){if(!left.length){let inv=0;for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)inv+=a[i]>a[j];perms.push([a,inv%2?-1:1]);return;}for(const x of left)perm([...a,x],left.filter(y=>y!==x));}
  perm([], [0,1,2,3]);
  const det = M => {let out=new Map();for(const [a,s]of perms){let term=mono(0,s);for(let i=0;i<4;i++)term=mul(term,M[i][a[i]]);out=add(out,term);}return out;};
  const pf = P => add(add(mul(P[0],P[5]),mul(P[1],P[4]),-1),mul(P[2],P[3]));
  const mixed = (P,Q) => add(add(add(mul(P[0],Q[5]),mul(Q[0],P[5])),add(mul(P[1],Q[4]),mul(Q[1],P[4])),-1),add(mul(P[2],Q[3]),mul(Q[2],P[3])));
  assert(eq(det(J.map(r=>r.map(x=>mono(0,x)))),mono(0,-20)),"integer Jacobian");
  assert(eq(mixed(p.map(x=>mono(0,x)),q.map(x=>mono(0,x))),mono(0,-20)),"transverse constant planes");
  assert(p.every(x=>x!==0)&&q.every(x=>x!==0),"all six pure brackets nonzero");
  let monomialProducts=0;
  for(let i=0;i<81;i++)for(let j=0;j<81;j++){
    const k=mm(i,j);
    if(k>=0)assert(degree(k)===degree(i)+degree(j),"graded product");
    monomialProducts++;
  }
  for(let i=1;i<81;i++)assert(mm(i,80)<0,"top annihilated");
  const cases=[];
  for(const nonlinear of [false,true]){
    // u1=w1+w3^2, u2=w2+w4^2, u3=w3, u4=w4, w=J X.
    // Thus d u/d X = N(u) J, with N_13=2u3, N_24=2u4.
    const N=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>mono(0,i===j?1:0)));
    if(nonlinear){N[0][2]=scale(ui[2],2);N[1][3]=scale(ui[3],2);}
    const H=Array.from({length:4},()=>Array.from({length:4},()=>new Map()));
    for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)H[i][j]=add(H[i][j],scale(N[i][k],J[k][j]));
    assert(eq(det(H),mono(0,-20)),"nonlinear Jacobian determinant");
    const L=H.map((r,i)=>r.map(h=>scale(mul(vi[i],h),3)));
    const P=pairs.map(([i,j])=>add(mul(L[i][0],L[j][1]),mul(L[i][1],L[j][0]),-1));
    const Q=pairs.map(([i,j])=>add(mul(L[i][2],L[j][3]),mul(L[i][3],L[j][2]),-1));
    const S=P.map((a,i)=>add(a,Q[i]));
    assert(pf(P).size===0 && pf(Q).size===0,"decomposable pure planes");
    assert(eq(mixed(P,Q),mono(80,-1620)),"mixed Jacobian socle");
    assert(eq(det(L),mono(80,-1620)),"full actual generator Jacobian");
    assert(eq(pf(S),mono(80,-1620)),"symplectic pencil");
    let crosses=0;
    for(let i=0;i<6;i++)for(let j=0;j<6;j++){assert(add(mul(P[i],Q[j]),mul(Q[i],P[j]),-1).size===0,"scalar cross minor");crosses++;}
    for(let i=0;i<6;i++){
      const leadP=new Map([...P[i]].filter(([j])=>degree(j)===4));
      const leadQ=new Map([...Q[i]].filter(([j])=>degree(j)===4));
      assert(eq(leadP,scale(E[i],9*p[i]))&&eq(leadQ,scale(E[i],9*q[i])),"exact leading tuple");
    }
    const ideals = [0,5].map(e=>{
      const eindex=[...E[e].keys()][0];
      const basis = new Set();
      for(let j=0;j<81;j++){const k=mm(eindex,j);if(k>=0)basis.add(k);}
      assert(basis.size===9,"socle-factor ideal dimension");
      const reps=exps.map((a,j)=>({a,j})).filter(({a})=>pairs[e].every(k=>a[k]===0));
      const constant=9*(p[e]+q[e]);
      for(const {j}of reps){
        const target=mm(eindex,j), value=mul(S[e],mono(j));
        assert(value.get(target)===constant,"unit triangular diagonal");
        for(const [k]of value)assert(basis.has(k)&&(k===target||degree(k)>degree(target)),"unit triangular ideal span");
      }
      return basis;
    });
    const intersection=[...ideals[0]].filter(i=>ideals[1].has(i));
    assert(JSON.stringify(intersection)==="[80]","ideal intersection exactly socle");
    assert(eq(mul(S[0],S[5]),mono(80,8100)),"nonzero socle pair product");
    assert(9*135!==45*18,"independent constant ratios contradict unit companion");
    cases.push({nonlinear_parameters:nonlinear,scalar_cross_minors:crosses,
      pure_initial_ranks:[6,6],length:81,socle_degree:8,
      full_jacobian_coefficient:-1620,mixed_wedge_coefficient:-1620,
      chosen_pencil_entries:[0,5],chosen_pair_product:8100,ideal_dimensions:[9,9],intersection_dimension:1});
  }
  return {status:"PASS",started_utc:started,seconds:(Date.now()-startMs)/1000,
    arithmetic:"Exact safe integers; every arithmetic addition and product in polynomial operations checked with Number.isSafeInteger.",
    matrix:J,p,q,constant_mixed_wedge:-20,monomial_basis_products:monomialProducts,
    cases,scope:"Two actual length-81 linear/nonlinear parameter-power examples, all scalar cross minors, actual gradient Jacobians and socle-pair intersections. Universal all-multiplicity obstruction remains the written proof."};
}

console.log(JSON.stringify(powerSocleCertificate(), null, 2));

