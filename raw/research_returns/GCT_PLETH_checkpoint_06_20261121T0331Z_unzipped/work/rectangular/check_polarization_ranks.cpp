#include <array>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr long long P=1000003;
using Counts=array<int,15>;
using Mat=array<array<int,4>,4>;
struct Term {int coeff; Counts counts;};
using Candidate=vector<Term>;
struct Point {Mat X; array<int,4> x;};

int md(long long a){a%=P; if(a<0)a+=P;return (int)a;}
int power(int a,long long b){int z=1;while(b){if(b&1)z=md(1LL*z*a);a=md(1LL*a*a);b>>=1;}return z;}
vector<vector<int>> minors;
vector<Point> points;
vector<array<array<int,5>,15>> forms;
vector<long long> directweights;
int directbase;

void direct_character(int b){
    if(b>7)return;
    int N=4*b;directbase=N+1;
    directweights.assign(directbase*directbase*directbase,0);
    vector<array<int,4>> mon;
    for(int i=0;i<=b;i++)for(int j=0;j<=b-i;j++)for(int k=0;k<=b-i-j;k++)
        mon.push_back({i,j,k,b-i-j-k});
    int m=mon.size();
    for(int i=0;i<m;i++)for(int j=i;j<m;j++)for(int k=j;k<m;k++)for(int l=k;l<m;l++){
        int x=mon[i][0]+mon[j][0]+mon[k][0]+mon[l][0];
        int y=mon[i][1]+mon[j][1]+mon[k][1]+mon[l][1];
        int z=mon[i][2]+mon[j][2]+mon[k][2]+mon[l][2];
        directweights[x+directbase*y+directbase*directbase*z]++;
    }
}

long long direct_multiplicity(array<int,4> lam){
    array<int,4>rho{3,2,1,0},perm{0,1,2,3};
    long long ans=0;
    do{
        int sg=1;array<int,4> w{};bool good=true;
        for(int i=0;i<4;i++){
            w[i]=lam[i]+rho[i]-rho[perm[i]];
            if(w[i]<0||w[i]>=directbase)good=false;
            for(int j=i+1;j<4;j++)if(perm[i]>perm[j])sg=-sg;
        }
        if(good)ans+=sg*directweights[w[0]+directbase*w[1]+directbase*directbase*w[2]];
    }while(next_permutation(perm.begin(),perm.end()));
    return ans;
}

int detsmall(const vector<vector<int>>& A){
    int h=A.size(), ans=0;
    vector<int> p(h);iota(p.begin(),p.end(),0);
    do{
        int sg=1,z=1;
        for(int i=0;i<h;i++){
            z=md(1LL*z*A[i][p[i]]);
            for(int j=i+1;j<h;j++)if(p[i]>p[j])sg=-sg;
        }
        ans=md(ans+sg*(long long)z);
    }while(next_permutation(p.begin(),p.end()));
    return ans;
}

void setup(){
    for(int h=1;h<=4;h++)
        for(int mask=1;mask<16;mask++)if(__builtin_popcount((unsigned)mask)==h){
            vector<int>I;for(int j=0;j<4;j++)if(mask&(1<<j))I.push_back(j);
            minors.push_back(I);
        }
    // Match itertools.combinations ordering in the producer.
    stable_sort(minors.begin(),minors.end(),[](auto&a,auto&b){
        return a.size()!=b.size()?a.size()<b.size():a<b;
    });
    mt19937 rng(20261121);
    for(int z=0;z<64;z++){
        Point pt;
        for(auto&row:pt.X)for(auto&x:row)x=1+(rng()%(P-1));
        for(auto&x:pt.x)x=1+(rng()%(P-1));
        points.push_back(pt);
        array<array<int,5>,15> fs{};
        for(int m=0;m<15;m++){
            const auto&I=minors[m];int h=I.size();
            vector<vector<int>> A(h,vector<int>(h));
            for(int i=0;i<h;i++)for(int j=0;j<h;j++)A[i][j]=pt.X[i][I[j]];
            fs[m][0]=detsmall(A);
            for(int j=0;j<h;j++){
                auto B=A;for(int i=0;i<h;i++)B[i][j]=pt.x[i];
                fs[m][I[j]+1]=detsmall(B);
            }
        }
        forms.push_back(fs);
    }
}

int coefficient(const Counts& cnt,int point,int L){
    int base=L+1,N=base*base*base*base;
    array<int,4> place{1,base,base*base,base*base*base};
    vector<array<int,4>> to(N);
    for(int z=0;z<N;z++)
        for(int j=0;j<4;j++)to[z][j]=(z/place[j])%base<L ? z+place[j] : -1;
    vector<int> dp(N),nd(N);dp[0]=1;
    for(int m=0;m<15;m++)for(int repeat=0;repeat<cnt[m];repeat++){
        fill(nd.begin(),nd.end(),0);
        auto&f=forms[point][m];
        for(int z=0;z<N;z++)if(dp[z]){
            nd[z]=md(nd[z]+1LL*dp[z]*f[0]);
            for(int j:minors[m])if(to[z][j]>=0)
                nd[to[z][j]]=md(nd[to[z][j]]+1LL*dp[z]*f[j+1]);
        }
        dp.swap(nd);
    }
    return dp[N-1];
}

int determinant(vector<vector<int>> A){
    int n=A.size(),d=1;
    for(int j=0;j<n;j++){
        int i=j;while(i<n&&!A[i][j])i++;
        if(i==n)return 0;
        if(i!=j){swap(A[i],A[j]);d=md(-d);}
        int piv=A[j][j];d=md(1LL*d*piv);
        int inv=power(piv,P-2);
        for(int k=j;k<n;k++)A[j][k]=md(1LL*A[j][k]*inv);
        for(int i2=j+1;i2<n;i2++){
            int s=A[i2][j];
            for(int k=j;k<n;k++)A[i2][k]=md(A[i2][k]-1LL*s*A[j][k]);
        }
    }
    return d;
}

int main(int argc,char**argv){
    if(argc!=2)return 2;
    setup();
    string path=argv[1];ifstream in(path);
    int L,b,ncases;in>>L>>b>>ncases;
    direct_character(b);
    string stem=path.substr(0,path.rfind('.'));
    ofstream out(stem+"_RANKS.tsv"), cert(stem+"_CERTIFICATES.txt");
    out<<"partition\tsource_multiplicity\timage_rank_mod_1000003\tcandidates_evaluated\tminor_determinant\tstatus\n";
    cert<<"prime "<<P<<"\noperator coefficient of t1^L t2^L t3^L t4^L\n";
    for(int i=0;i<(int)points.size();i++){
        cert<<"point "<<i;
        for(auto&row:points[i].X)for(int z:row)cert<<" "<<z;
        for(int z:points[i].x)cert<<" "<<z;
        cert<<"\n";
    }
    int fails=0,totalrank=0;
    for(int z=0;z<ncases;z++){
        array<int,4>lam;for(int&v:lam)in>>v;
        int mult,ncand;in>>mult>>ncand;
        if(!directweights.empty()&&direct_multiplicity(lam)!=mult)return 5;
        vector<Candidate> candidates(ncand);
        for(auto&c:candidates){
            int nt;in>>nt;c.resize(nt);
            for(auto&t:c){in>>t.coeff;for(int&v:t.counts)in>>v;}
        }
        int npoints=mult+2,rank=0,used=0;
        if(npoints>(int)points.size())return 4;
        vector<vector<int>> echelon(npoints);
        vector<vector<int>> original;
        vector<int> chosen;
        vector<map<Counts,int>> cache(npoints);
        for(int ci=0;ci<ncand&&rank<mult;ci++){
            vector<int> col(npoints);
            for(int j=0;j<npoints;j++){
                int val=0;
                for(auto&t:candidates[ci]){
                    auto it=cache[j].find(t.counts);
                    int v;
                    if(it==cache[j].end()){
                        v=coefficient(t.counts,j,L);cache[j][t.counts]=v;
                    }else v=it->second;
                    val=md(val+1LL*t.coeff*v);
                }
                col[j]=val;
            }
            used++;
            auto red=col;
            for(int i=0;i<npoints;i++)if(red[i]){
                if(echelon[i].empty()){
                    int inv=power(red[i],P-2);
                    for(int j=i;j<npoints;j++)red[j]=md(1LL*red[j]*inv);
                    echelon[i]=red;original.push_back(col);chosen.push_back(ci);rank++;break;
                }
                int scale=red[i];
                for(int j=i;j<npoints;j++)red[j]=md(red[j]-1LL*scale*echelon[i][j]);
            }
        }
        vector<int> rows;for(int j=0;j<npoints;j++)if(!echelon[j].empty())rows.push_back(j);
        vector<vector<int>> square(rank,vector<int>(rank));
        for(int i=0;i<rank;i++)for(int j=0;j<rank;j++)square[i][j]=original[j][rows[i]];
        int d=determinant(square);if(rank&&d==0)return 3;
        stringstream label;for(int i=0;i<4;i++){if(i)label<<",";label<<lam[i];}
        string status=rank==mult?"PASS":"DEFICIENT_EVALUATION_RANK";
        out<<label.str()<<"\t"<<mult<<"\t"<<rank<<"\t"<<used<<"\t"<<d<<"\t"<<status<<"\n";
        cert<<"partition "<<label.str()<<" multiplicity "<<mult<<" rank "<<rank<<"\n";
        cert<<"candidates";for(int j:chosen)cert<<" "<<j;cert<<"\n";
        cert<<"rows";for(int j:rows)cert<<" "<<j;cert<<"\n";
        for(auto&row:square){for(int j=0;j<rank;j++)cert<<(j?" ":"")<<row[j];cert<<"\n";}
        cert<<"determinant "<<d<<"\n";
        if(rank!=mult){fails++;cerr<<"DEFICIENT "<<label.str()<<" "<<rank<<"/"<<mult<<"\n";}
        totalrank+=rank;
    }
    cout<<"L="<<L<<" b="<<b<<" constituents="<<ncases<<" total_rank="<<totalrank<<" deficient_blocks="<<fails<<"\n";
    return 0;
}
