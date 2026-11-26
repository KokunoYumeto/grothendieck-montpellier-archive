// Exact conjugacy-reduced character-word counts for the partial-transpose test.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
uint64_t cycle_key(const vector<int>& p) {
    unsigned seen=0; uint64_t key=0;
    for (int i=0;i<(int)p.size();++i) if (!(seen&(1u<<i))) {
        int j=i,len=0;
        do {seen|=1u<<j; ++len; j=p[j];} while(j!=i);
        key += uint64_t(1) << (4*(len-1));
    }
    return key;
}
int main() {
    int n,k; cin>>n>>k;
    if(n>12 || n<1) return 2;
    vector<vector<int>> reps(k,vector<int>(n));
    vector<long long> ca(k),cb(k);
    unordered_map<uint64_t,int> index;
    for(int c=0;c<k;++c) {
        int l;cin>>l;vector<int> shape(l);
        for(int& x:shape)cin>>x;
        cin>>ca[c]>>cb[c];
        int pos=0;
        for(int len:shape) {
            for(int j=0;j<len;++j)reps[c][pos+j]=pos+(j+1)%len;
            pos+=len;
        }
        if(pos!=n)return 3;
        index[cycle_key(reps[c])]=c;
    }
    vector<vector<long long>> counts(k,vector<long long>(k));
    vector<int> h(n),hi(n),gh(n),ghi(n);
    for(int i=0;i<n;++i)h[i]=i;
    long long enumerated=0;
    do {
        ++enumerated;
        for(int i=0;i<n;++i)hi[h[i]]=i;
        int hc=index.at(cycle_key(h));
        for(int c=0;c<k;++c) {
            for(int i=0;i<n;++i) {
                gh[i]=reps[c][h[i]];
                ghi[i]=reps[c][hi[i]];
            }
            counts[c][hc] += ca[index.at(cycle_key(gh))]*cb[index.at(cycle_key(ghi))];
        }
    } while(next_permutation(h.begin(),h.end()));
    cout<<enumerated<<'\n';
    for(auto& row:counts) {
        for(int c=0;c<k;++c)cout<<row[c]<<(c+1==k?'\n':' ');
    }
}
