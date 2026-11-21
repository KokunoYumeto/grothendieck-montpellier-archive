// Cross-check EVERY evaluation-Jacobian entry using a different permanent
// algorithm: Ryser's formula, Gray-code row sums, and a reverse derivative
// sweep through the Gray-code recurrence. No subset-permanent DP is used.
#define main saved_certificate_generation_main
#include "check_permanent_range.cpp"
#undef main

std::vector<int> ryser_gradient(int n,const std::vector<int>& matrix) {
    const unsigned states=1u<<n;
    std::vector<int> sums(n),prefix(n+1),suffix(n+1),adjoint(n),gradient(n*n);
    std::vector<uint8_t> local((size_t)states*n);
    for(unsigned t=1;t<states;++t) {
        unsigned gray=t^(t>>1);
        int j=__builtin_ctz(t);
        int direction=(gray&(1u<<j)) ? 1 : -1;
        for(int i=0;i<n;++i) sums[i]=(sums[i]+direction*matrix[i*n+j]+P)%P;
        prefix[0]=suffix[n]=1;
        for(int i=0;i<n;++i) prefix[i+1]=prefix[i]*sums[i]%P;
        for(int i=n-1;i>=0;--i) suffix[i]=suffix[i+1]*sums[i]%P;
        bool negative=(n+__builtin_popcount(gray))&1;
        for(int i=0;i<n;++i) {
            int value=prefix[i]*suffix[i+1]%P;
            local[(size_t)t*n+i]=negative && value ? P-value : value;
        }
    }
    for(unsigned t=states-1;t>0;--t) {
        unsigned gray=t^(t>>1);
        int j=__builtin_ctz(t);
        int direction=(gray&(1u<<j)) ? 1 : -1;
        for(int i=0;i<n;++i) {
            adjoint[i]=(adjoint[i]+local[(size_t)t*n+i])%P;
            gradient[i*n+j]=(gradient[i*n+j]+direction*adjoint[i]+P)%P;
        }
    }
    return gradient;
}

int main(int argc,char** argv) {
    if(argc!=4) return 2;
    int first=std::stoi(argv[1]),last=std::stoi(argv[2]);
    std::string path=argv[3];
    for(int n=first;n<=last;++n) {
        uint32_t state=20261121u+1009u*n; // All recorded certificates use attempt0.
        std::vector<int> pencil(4*n*n);
        for(auto &v:pencil) v=(next_random(state)>>16)%P;
        auto pts=points(n);
        const int columns=4*n*n;
        std::vector<uint8_t> reference(pts.size()*columns);
        std::ifstream raw(path+"/permanent_range_n"+std::to_string(n)+".u8",std::ios::binary);
        raw.read(reinterpret_cast<char*>(reference.data()),reference.size());
        if(raw.gcount()!=(std::streamsize)reference.size()) return 3;
        std::vector<int> matrix(n*n);
        auto begin=std::chrono::steady_clock::now();
        for(size_t row=0;row<pts.size();++row) {
            for(int cell=0;cell<n*n;++cell) {
                int value=0;
                for(int k=0;k<4;++k) value+=pencil[4*cell+k]*pts[row][k];
                matrix[cell]=value%P;
            }
            auto gradient=ryser_gradient(n,matrix);
            for(int cell=0;cell<n*n;++cell)
                for(int k=0;k<4;++k) {
                    int expected=gradient[cell]*pts[row][k]%P;
                    if(expected!=reference[row*columns+4*cell+k]) {
                        std::cerr<<"mismatch n="<<n<<" row="<<row<<" col="<<4*cell+k<<std::endl;
                        return 1;
                    }
                }
        }
        auto end=std::chrono::steady_clock::now();
        std::cout<<"{\"n\":"<<n<<",\"entries_checked\":"<<reference.size()
                 <<",\"ryser_matches_all_entries\":true,\"seconds\":"
                 <<std::chrono::duration<double>(end-begin).count()<<"}"<<std::endl;
    }
    return 0;
}
