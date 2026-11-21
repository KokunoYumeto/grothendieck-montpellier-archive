// Independent finite check: Gray-code Ryser, linear-factor prefix/suffix
// products, and explicit auxiliary gradients (no subset-DP reverse sweep).
#define main previous_border_main
#include "check_border_ternary.cpp"
#undef main

std::vector<int> ryser_row(const Data&d,const Point&x){
 int n=d.n,p=d.p;unsigned N=1u<<n;std::vector<int>A(n*n),u(n),v(n),s(n),pr0(n+1),pr1(n+1),su0(n+1),su1(n+1);std::vector<int>gu1(n),gv1(n),gu2(n),gv2(n);int per=0,vs=0;unsigned previous=0;
 for(int i=0;i<n;++i){for(int k=0;k<3;++k){u[i]=(u[i]+d.u[3*i+k]*x[k])%p;v[i]=(v[i]+d.v[3*i+k]*x[k])%p;}for(int j=0;j<n;++j)for(int k=0;k<3;++k)A[n*i+j]=(A[n*i+j]+d.A[3*(n*i+j)+k]*x[k])%p;}
 for(unsigned counter=1;counter<N;++counter){unsigned gray=counter^(counter>>1),diff=gray^previous;int j=__builtin_ctz(diff),delta=(gray&diff)?1:-1;previous=gray;for(int i=0;i<n;++i)s[i]=(s[i]+delta*A[n*i+j]+p)%p;vs=(vs+delta*v[j]+p)%p;int sign=((n-__builtin_popcount(gray))&1)?-1:1;
  pr0[0]=1;pr1[0]=0;for(int i=0;i<n;++i){int h=int(1LL*u[i]*vs%p);pr0[i+1]=int(1LL*pr0[i]*s[i]%p);pr1[i+1]=int((1LL*pr1[i]*s[i]+1LL*pr0[i]*h)%p);}
  su0[n]=1;su1[n]=0;for(int i=n-1;i>=0;--i){int h=int(1LL*u[i]*vs%p);su0[i]=int(1LL*su0[i+1]*s[i]%p);su1[i]=int((1LL*su1[i+1]*s[i]+1LL*su0[i+1]*h)%p);}
  per=(per+sign*pr0[n]+p)%p;uint64_t d1=0,d2=0;
  for(int i=0;i<n;++i){int o0=int(1LL*pr0[i]*su0[i+1]%p),o1=int((1LL*pr1[i]*su0[i+1]+1LL*pr0[i]*su1[i+1])%p);gu1[i]=(gu1[i]+sign*int(1LL*vs*o0%p)+p)%p;gu2[i]=(gu2[i]+sign*int(1LL*vs*o1%p)+p)%p;d1+=1ULL*u[i]*o0;d2+=1ULL*u[i]*o1;}
  int a=d1%p,b=d2%p;unsigned bits=gray;while(bits){unsigned bit=bits&(-bits);int k=__builtin_ctz(bits);bits^=bit;gv1[k]=(gv1[k]+sign*a+p)%p;gv2[k]=(gv2[k]+sign*b+p)%p;}
 }
 std::vector<int>out;for(int k=0;k<3;++k)out.push_back(per*x[k]%p);for(int i=0;i<n;++i)for(int k=0;k<3;++k)out.push_back(gu1[i]*x[k]%p);for(int j=0;j<n;++j)for(int k=0;k<3;++k)out.push_back(gv1[j]*x[k]%p);out.insert(out.end(),gu2.begin(),gu2.end());out.insert(out.end(),gv2.begin(),gv2.end());return out;
}

int main(int argc,char**argv){if(argc<4)return 2;int n=std::stoi(argv[1]);std::string mode=argv[2],dir=argv[3];uint32_t seed=argc>4?std::stoul(argv[4]):20261121u+4099u*n;auto d=make_data(n,mode,seed);auto pts=points(n+1);int cols=8*n+3;std::string stem=dir+"/border_"+mode+"_m"+std::to_string(n);std::ifstream raw(stem+".u16",std::ios::binary);if(!raw)return 3;auto start=std::chrono::steady_clock::now();size_t checked=0;for(size_t r=0;r<pts.size();++r){auto row=ryser_row(d,pts[r]);for(int c=0;c<cols;++c){uint16_t expected;raw.read(reinterpret_cast<char*>(&expected),2);if(!raw||expected!=row[c]){std::cerr<<"Mismatch row="<<r<<" col="<<c<<" expected="<<expected<<" got="<<row[c]<<std::endl;return 1;}++checked;}}double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();std::ofstream out(stem+"_ryser.json");out<<"{\n\"m\":"<<n<<",\n\"prime\":"<<d.p<<",\n\"entries_checked\":"<<checked<<",\n\"all_match\":true,\n\"seconds\":"<<seconds<<",\n\"method\":\"Gray-code Ryser with prefix/suffix linear-factor coefficients and explicit auxiliary gradients\"\n}\n";std::cout<<"m="<<n<<" all "<<checked<<" entries agree; seconds="<<seconds<<std::endl;}
