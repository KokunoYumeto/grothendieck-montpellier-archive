\\ Compact exact certificate written independently in the tower basis.
\\ Contains every algebraic input; no external witnesses or bnf input.
default(parisizemax,2000000000);default(realprecision,100);
require(ok,label)={if(!ok,error(label));print("PASS ",label)};
el(v)=sum(j=1,18,v[j]*basis[j])/3;
prime_at(p,t)=idealhnf(n,p,t-z^2-z^5-a*z^3);
artin_column(J)={my(fac=idealfactor(n,J),ans=vector(4)~,pp,qq,uu,w);for(k=1,matsize(fac)[1],pp=fac[k,1];qq=idealnorm(n,pp);w=nfmodpr(n,z^3,pp);for(j=1,4,uu=nfmodpr(n,rad[j],pp);if(uu==0,error("nonunit radical at test prime"));uu=uu^((qq-1)/3);ans[j]+=fac[k,2]*if(uu==1,0,if(uu==w,1,if(uu==w^2,2,error("residue symbol"))))));lift(Mod(ans,3))};
local_check(N)={my(ff=factorpadic(p,3,N)[,1],deg=3*log(4+O(3^N)),mat,det);require(vector(#ff,j,poldegree(ff[j]))==[6,6,6],"three local factors of degree six");mat=matrix(3,2,i,j,-log(polresultant(ff[i],lift(un[j])))/deg);require(padicprec(mat,3)>N-15,"absolute logarithm precision");require(vecmin(vector(2,j,valuation(sum(i=1,3,mat[i,j]),3)))>N-15,"local product formula");det=mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1];require(valuation(det,3)==2,"logarithmic index nine");print("LOCAL_PRECISION ",N," MATRIX_MOD81 ",lift(Mod(mat,81))," DET_VAL ",valuation(det,3));};
main()={
p=y^18+1617*y^15+1082193*y^12+385574654*y^9+77580889323*y^6+8385564626034*y^3+383147566015591;
n=nfinit(p);require(nfcertify(n)==[],"certified maximal order");
a=nfroots(n,x^3-269)[1];z=nfroots(n,x^6+x^3+1)[1];
basis=vector(18,j,a^((j-1)\6)*z^((j-1)%6));
require(matdet(matrix(18,18,i,j,nfalgtobasis(n,basis[j])[i]))!=0,"tower basis spans field");
num=[[740549184998, 526461578010, -557710995894, 20396613524, 834066208629, 269271546960, -111559636254, 47651376012, 128108785755, -114719297449, -81554748855, 86395631373, -489466652, -20015464503, -6461831178, 17281827501, -7381727682, -19845474474],
[17889212813, -19864230075, -15763020834, 19142329988, 11999829114, -22253219370, 1549834439, 3173853810, 950364843, -3329148144, 2955723279, 3228000099, -545756019, -306758616, 655799310, -326501774, -510496851, -25475754],
[8594118, -1137294, -6432990, 21889964, -19670253, 15061875, 2058113, -2872287, 3329397, -1332190, 176235, 997560, -525067, 472221, -361389, -318918, 444729, -515994],
[-3061198634644, 212898960429, 2196733098180, -2778672713688, -476947997430, -740558314092, 92343032945, 472122029658, -302204888193, -4700493766, 207271989861, 219766407735, 59336272011, -78504530988, -6477488079, 66964967012, -21302187252, -16807475550],
[-934103308941123, -238943503101082, 180507700466093, -351741143032598, 566554293146475, 1031068311570735, 30779733833058, -48556582298655, -131446987179252, -133645627606489, -147392907765338, -79098648409229, 18279785822499, 26610955045393, 19698995146918, 16527571036303, 12959157774388, 100889473147],
[349881926219204, -123303059157588, -122058690498127, 694489002750061, -648097745079781, 526884043868563, 53877109777038, -18218450949555, -18289991796469, 106586791694733, -100363008485051, 82625182552039, 8241098024896, -2954745153321, -2773900234521, 16559353821251, -15685611709540, 12704262121308],
[-594138651063, -373650200471, 464371298539, -59213991169, -652244114375, -167308011966, 82865774067, -43157292937, -97854144574, 92038679224, 57882568157, -71936274198, 1420985001, 15652197322, 4014966085, -12836829232, 6685544314, 15158694417],
[5854, 4516, -4433, 456, 6382, 2204, 845, 660, -701, -60, 1036, 281, 142, 92, -93, 3, 156, 63],
[144359, 251883, 5356, -71779, 161242, 140406, -33486, -14043, 20922, -22363, -39031, -823, 1723, -3870, -3370, 5187, 2176, -3241],
[196813, -36473, -208687, 160703, 160057, -104336, 30434, -5644, -32405, 24772, 24809, -16282, 4705, -875, -5026, 3845, 3841, -2510]];
rad=vector(4,j,el(num[j]));gen=vector(4,j,el(num[4+j]));un=vector(2,j,el(num[8+j]));
g1=prime_at(1531,492);g2=idealmul(n,prime_at(1531,52),idealpow(n,g1,2));g3=prime_at(10779577093,2237331723);
vq=[-6,-14,0,-3,-7,7,0,-5,-14,0,-4,-14,0,0,-2,0,0,-3];
q=idealhnf(n,7,el(vq));ids=[g1,g2,g3,q];
require(vector(4,j,idealnorm(n,ids[j]))==[1531,1531^3,10779577093,343],"ideal norms");
for(j=1,4,my(fac=nffactor(n,x^3-rad[j]));require(matsize(fac)[1]==1 && poldegree(fac[1,1])==3,Str("radical irreducible ",j));require(rnfdisc(n,x^3-rad[j])[1]==1,Str("relative discriminant one ",j)));
A=matrix(4,4,i,j,artin_column(ids[j])[i]);require(lift(Mod(matdet(A),3))!=0,"independent Artin pairing");print("ARTIN_MATRIX ",A);
orders=[63,21,3,3];for(j=1,4,require(idealhnf(n,gen[j])==idealpow(n,ids[j],orders[j]),Str("principal ideal identity ",j)));
pr3=idealprimedec(n,3);require(#pr3==3,"three primes above three");require(vector(3,j,nfislocalpower(n,pr3[j],rad[1],3))==[0,0,0],"nontrivial three-prime class");
for(j=1,2,my(ff=idealfactor(n,un[j]));for(k=1,matsize(ff)[1],require(ff[k,1][1]==3,"unit support over three")));
local_check(40);local_check(70);
print("COMPACT_CERTIFICATE_COMPLETE_BOUND_729");
};
iferr(main(),err,print("FAIL ",err);quit(1));
quit
