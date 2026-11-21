#define main saved_uniform_main
#include "check_permanent_range.cpp"
#undef main

std::vector<int> base_cycle(int n) {
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
    for (int n: {8,10,12,14}) {
        const auto pts=points(n);
        for (int pattern=0;pattern<6;++pattern) {
            auto a=base_cycle(n);
            uint32_t seed=20261121u+97*pattern;
            int core=pattern<4?pattern+3:0;
            if(core) {
                for(int i=0;i<core;++i) for(int j=0;j<core;++j)
                    for(int k=0;k<4;++k)
                        a[4*(n*i+j)+k]=(next_random(seed)>>16)%P;
            } else {
                const int blocks=pattern-2;
                for(int b=0;b<blocks;++b) {
                    const int i=3*b%n;
                    const int j=(i+1)%n, h=(i+2)%n;
                    for(int k=0;k<4;++k) {
                        a[4*(n*i+h)+k]=(next_random(seed)>>16)%P;
                        a[4*(n*j+i)+k]=(next_random(seed)>>16)%P;
                    }
                }
            }
            auto t0=std::chrono::steady_clock::now();
            auto matrix=evaluation_jacobian(n,a,pts);
            int rank=eliminate(matrix,pts.size(),4*n*n).pivots.size();
            double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();
            std::cout<<"{\"n\":"<<n<<",\"pattern\":"<<pattern
                <<",\"core_size\":"<<core<<",\"rank\":"<<rank
                <<",\"base_excess\":"<<rank-(2*n*n+2)
                <<",\"needed_excess_for_padding\":"<<4*n
                <<",\"seconds\":"<<seconds<<"}"<<std::endl;
        }
    }
}
