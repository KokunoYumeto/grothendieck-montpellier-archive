// Exact coefficient formulas for the cyclic criterion, using two path arcs.
// Unlike the exploratory subset DP, this works in polynomial time in m.
#define main old_border_main
#include "check_border_ternary.cpp"
#undef main

struct Poly {
 int d,p;std::vector<int>a;
 Poly(int degree,int prime):d(degree),p(prime),a((d+1)*(d+1)){}
 int& at(int x,int z){return a[x*(d+1)+z];}
 int at(int x,int z)const{return a[x*(d+1)+z];}
};
Poly one(int p){Poly a(0,p);a.at(0,0)=1;return a;}
Poly linear(const int* c,int p){Poly a(1,p);a.at(1,0)=c[0];a.at(0,0)=c[1];a.at(0,1)=c[2];return a;}
Poly add(const Poly&a,const Poly&b){if(a.d!=b.d||a.p!=b.p)throw 1;Poly c=a;for(size_t i=0;i<c.a.size();++i)c.a[i]=(c.a[i]+b.a[i])%a.p;return c;}
Poly multiply(const Poly&a,const Poly&b){Poly c(a.d+b.d,a.p);std::vector<uint64_t>s(c.a.size());for(int i=0;i<=a.d;++i)for(int j=0;j+i<=a.d;++j)if(int x=a.at(i,j))for(int k=0;k<=b.d;++k)for(int l=0;l+k<=b.d;++l)if(int y=b.at(k,l))s[(i+k)*(c.d+1)+j+l]+=1ULL*x*y;for(size_t k=0;k<s.size();++k)c.a[k]=s[k]%a.p;return c;}

std::pair<Poly,Poly> cyclic_forms(const std::vector<Poly>&ell,const std::vector<Poly>&h,const std::vector<Poly>&u,const std::vector<Poly>&v){
 int n=ell.size(),p=ell[0].p;std::vector<Poly>lp,hs,left,right;lp.push_back(one(p));for(int k=1;k<n;++k)lp.push_back(multiply(lp.back(),ell[k]));for(int k=0;k<=n;++k)hs.emplace_back(n-k,p);hs[n]=one(p);for(int k=n-1;k>=0;--k)hs[k]=multiply(h[k],hs[k+1]);
 for(int k=0;k<n;++k){left.emplace_back(k,p);right.emplace_back(n-k,p);}left[1]=v[1];for(int k=1;k<n-1;++k)left[k+1]=add(multiply(h[k],left[k]),multiply(v[k+1],lp[k]));right[n-1]=v[0];for(int k=n-1;k>0;--k)right[k-1]=add(multiply(v[k],hs[k]),multiply(ell[k],right[k]));
 Poly t(n+1,p);for(int k=1;k<n;++k){auto term=multiply(u[k],multiply(left[k],right[k]));for(size_t j=0;j<t.a.size();++j)t.a[j]=(t.a[j]+2*term.a[j])%p;}return {right[0],t};
}

void write_poly(const std::string&path,const Poly&a){std::ofstream f(path,std::ios::binary);for(int x:a.a){uint16_t y=x;f.write(reinterpret_cast<char*>(&y),2);}}
int main(int argc,char**argv){if(argc<3)return 2;int n=std::stoi(argv[1]);std::string dir=argv[2];auto d=make_data(n,"balanced2_cycle",20261121u+4099u*n);int p=d.p;std::vector<Poly>ell,h,u,v;for(int i=0;i<n;++i){ell.push_back(linear(&d.A[3*(n*i+i)],p));h.push_back(linear(&d.A[3*(n*i+(i+1)%n)],p));u.push_back(linear(&d.u[3*i],p));v.push_back(linear(&d.v[3*i],p));}auto start=std::chrono::steady_clock::now();auto at=cyclic_forms(ell,h,u,v);std::vector<Poly>et,ht,ut,vt;for(int i=0;i<n;++i){int j=(n-i)%n;et.push_back(ell[j]);ht.push_back(h[(j+n-1)%n]);ut.push_back(v[j]);vt.push_back(u[j]);}auto bt=cyclic_forms(et,ht,ut,vt);std::filesystem::create_directories(dir);std::string stem=dir+"/cyclic_coefficients_m"+std::to_string(n);write_poly(stem+"_a.u16",at.first);write_poly(stem+"_b.u16",bt.first);write_poly(stem+"_t.u16",at.second);write_poly(stem+"_tp.u16",bt.second);std::ofstream out(stem+".json");out<<"{\n\"m\":"<<n<<",\n\"prime\":"<<p<<",\n\"q\":"<<d.q<<",\n\"seed\":"<<d.seed<<",\n\"u0\":["<<d.u[0]<<','<<d.u[1]<<','<<d.u[2]<<"],\n\"v0\":["<<d.v[0]<<','<<d.v[1]<<','<<d.v[2]<<"],\n\"encoding\":\"u16 row-major coefficient[x*(degree+1)+z], y exponent=degree-x-z\",\n\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n}\n";std::cout<<"m="<<n<<" coefficients generated in "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<" seconds\n";return 0;}
