// Independent verification of conjugacy-word sums for central PT tests.
// Heap's permutation traversal, reversed cycle representatives, and the
// words h*g and h^{-1}*g differ from the discovery implementation.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
int main(int argc,char**argv){
  if(argc!=2)return 2; ifstream in(argv[1]); int n,k,cases;in>>n>>k>>cases;
  if(n<1||n>10||k<1||cases<1)return 3;
  vector<uint64_t> powers(n+1,1);for(int i=1;i<=n;i++)powers[i]=powers[i-1]*(n+1);
  auto key=[&](const vector<int>&p){
    bool used[11]={};uint64_t z=0;
    for(int i=1;i<=n;i++)if(!used[i]){
      int j=i,len=0;do{used[j]=true;j=p[j];++len;}while(j!=i);
      z+=powers[len];
    }return z;
  };
  vector<vector<int>> reps(k,vector<int>(n+1));
  unordered_map<uint64_t,int> index;
  for(int c=0;c<k;c++){
    int l;in>>l;vector<int> shape(l);for(auto&x:shape)in>>x;
    // Place the cycles in reverse shape order and orient every cycle backward.
    int pos=1;
    for(auto it=shape.rbegin();it!=shape.rend();++it){
      int len=*it;for(int j=0;j<len;j++)reps[c][pos+j]=pos+(j+len-1)%len;
      pos+=len;
    }
    if(pos!=n+1)return 4;index[key(reps[c])]=c;
  }
  vector<vector<long long>> a(cases,vector<long long>(k)),b=a;
  vector<vector<vector<long long>>> expected(cases,vector<vector<long long>>(k,vector<long long>(k)));
  for(int z=0;z<cases;z++){
    for(auto&x:a[z])in>>x;for(auto&x:b[z])in>>x;
    for(auto&row:expected[z])for(auto&x:row)in>>x;
  }
  if(!in)return 5;
  auto actual=expected;for(auto&C:actual)for(auto&row:C)fill(row.begin(),row.end(),0);
  vector<int> h(n+1),inv(n+1),word1(n+1),word2(n+1),heap(n+1,0);
  for(int i=1;i<=n;i++)h[i]=i;
  long long total=0;
  auto visit=[&](){
    ++total;for(int i=1;i<=n;i++)inv[h[i]]=i;
    int hc=index.at(key(h));
    for(int gc=0;gc<k;gc++){
      for(int i=1;i<=n;i++){word1[i]=h[reps[gc][i]];word2[i]=inv[reps[gc][i]];}
      int c1=index.at(key(word1)),c2=index.at(key(word2));
      for(int z=0;z<cases;z++)actual[z][gc][hc]+=a[z][c1]*b[z][c2];
    }
  };
  visit();int i=1;
  while(i<=n){
    if(heap[i]<i-1){swap(h[(i%2)?1:heap[i]+1],h[i]);visit();++heap[i];i=1;}
    else{heap[i]=0;++i;}
  }
  long long factorial=1;for(int j=2;j<=n;j++)factorial*=j;
  if(total!=factorial)return 6;
  long long checked=0;
  for(int z=0;z<cases;z++)for(int g=0;g<k;g++)for(int htype=0;htype<k;htype++){
    ++checked;if(actual[z][g][htype]!=expected[z][g][htype]){
      cerr<<"mismatch "<<z<<' '<<g<<' '<<htype<<' '<<actual[z][g][htype]<<' '<<expected[z][g][htype]<<'\n';return 7;
    }
  }
  cout<<"{\"status\":\"PASS\",\"n\":"<<n<<",\"permutations\":"<<total
      <<",\"cases\":"<<cases<<",\"word_sums_checked\":"<<checked<<"}\n";
}
