#define main saved_uniform_main
#include "check_permanent_range.cpp"
#undef main
std::vector<int> cycle(int n) {
    std::vector<int> a(4*n*n);
    for(int i=0;i<n;++i) {
        a[4*(n*i+i)]=1;
        a[4*(n*i+i)+1]=(P-(i+1))%P;
        a[4*(n*i+(i+1)%n)+2]=1;
        a[4*(n*i+(i+1)%n)+3]=(P-(i+1)*(i+1)%P)%P;
    }
    return a;
}
int main() {
    std::vector<std::array<int,4>> successful;
    const int n=4;
    std::vector<std::pair<int,int>> chords;
    for(int i=0;i<n;++i) for(int j=0;j<n;++j)
        if(j!=i && j!=(i+1)%n) chords.push_back({i,j});
    auto pts=points(n);
    for(size_t c=0;c<chords.size();++c) for(size_t d=c+1;d<chords.size();++d) {
        auto a=cycle(n);
        for(int k=0;k<4;++k) {
            a[4*(n*chords[c].first+chords[c].second)+k]=Point{1,2,3,4}[k];
            a[4*(n*chords[d].first+chords[d].second)+k]=Point{2,5,7,11}[k];
        }
        int rank=eliminate(evaluation_jacobian(n,a,pts),pts.size(),4*n*n).pivots.size();
        if(rank>2*n*n+2) {
            successful.push_back({chords[c].first,chords[c].second,chords[d].first,chords[d].second});
            std::cout<<"{\"n\":4,\"chords\":[["<<chords[c].first<<','<<chords[c].second
                <<"],["<<chords[d].first<<','<<chords[d].second<<"]],\"rank\":"<<rank<<"}"<<std::endl;
        }
    }
    for(auto pattern:successful) {
        for(int n=5;n<=12;++n) {
            auto a=cycle(n);auto pts=points(n);
            for(int k=0;k<4;++k) {
                a[4*(n*pattern[0]+pattern[1])+k]=Point{1,2,3,4}[k];
                a[4*(n*pattern[2]+pattern[3])+k]=Point{2,5,7,11}[k];
            }
            int rank=eliminate(evaluation_jacobian(n,a,pts),pts.size(),4*n*n).pivots.size();
            std::cout<<"{\"n\":"<<n<<",\"chords\":[["<<pattern[0]<<','<<pattern[1]
                <<"],["<<pattern[2]<<','<<pattern[3]<<"]],\"rank\":"<<rank
                <<",\"excess\":"<<rank-(2*n*n+2)<<"}"<<std::endl;
        }
        break; // A single successful pattern is enough for conceptual follow-up.
    }
}
