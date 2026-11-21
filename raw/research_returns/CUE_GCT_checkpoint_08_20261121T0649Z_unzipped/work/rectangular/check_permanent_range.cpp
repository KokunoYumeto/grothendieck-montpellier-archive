// Exact evaluation-Jacobian certificates over F_101 for four-variable
// permanent pencils. Forward subset DP and its reverse derivative sweep.
// Build: g++ -O3 -std=c++17 check_permanent_range.cpp -o check_permanent_range
// Usage: check_permanent_range min_n max_n output_directory
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

constexpr int P = 101;
using Point = std::array<int,4>;

uint32_t next_random(uint32_t &state) {
    state = 1664525u*state+1013904223u;
    return state;
}

int power(int a, int b) {
    int value = 1;
    while (b) {
        if (b & 1) value = value*a % P;
        a = a*a % P;
        b >>= 1;
    }
    return value;
}

std::vector<Point> points(int n) {
    std::vector<Point> out;
    for (int a=n; a>=0; --a)
        for (int b=n-a; b>=0; --b)
            for (int c=n-a-b; c>=0; --c)
                out.push_back({a,b,c,n-a-b-c});
    return out;
}

std::vector<uint8_t> evaluation_jacobian(
        int n, const std::vector<int>& pencil, const std::vector<Point>& pts) {
    const unsigned size = 1u<<n;
    const int cols = 4*n*n;
    std::vector<uint8_t> result(pts.size()*cols);
    std::vector<unsigned> row(size);
    for(unsigned s=1;s<size;++s) row[s]=__builtin_popcount(s)-1;
    std::vector<int> matrix(n*n);
    std::vector<uint16_t> forward(size), reverse(size);
    std::vector<uint64_t> gradient(n*n);
    for(size_t point=0;point<pts.size();++point) {
        for(int cell=0;cell<n*n;++cell) {
            int v=0;
            for(int k=0;k<4;++k) v+=pencil[4*cell+k]*pts[point][k];
            matrix[cell]=v%P;
        }
        forward[0]=1;
        for(unsigned s=1;s<size;++s) {
            unsigned value=0, bits=s;
            const int base=n*row[s];
            while(bits) {
                unsigned bit=bits&(-bits);
                int j=__builtin_ctz(bits);
                value+=matrix[base+j]*forward[s^bit];
                bits^=bit;
            }
            forward[s]=value%P;
        }
        std::fill(reverse.begin(),reverse.end(),0);
        std::fill(gradient.begin(),gradient.end(),0);
        reverse[size-1]=1;
        for(unsigned s=size-1;s>0;--s) {
            const unsigned factor=reverse[s];
            if(!factor) continue;
            const int base=n*row[s];
            unsigned bits=s;
            while(bits) {
                unsigned bit=bits&(-bits), previous=s^bit;
                int j=__builtin_ctz(bits);
                gradient[base+j]+=factor*forward[previous];
                reverse[previous]=(reverse[previous]+factor*matrix[base+j])%P;
                bits^=bit;
            }
        }
        for(int cell=0;cell<n*n;++cell) {
            const int g=gradient[cell]%P;
            for(int k=0;k<4;++k)
                result[point*cols+4*cell+k]=g*pts[point][k]%P;
        }
    }
    return result;
}

struct Elimination {
    std::vector<int> pivots;
    int determinant=1;
};

Elimination eliminate(std::vector<uint8_t> a, int rows, int cols) {
    Elimination output;
    int i=0;
    for(int j=0;j<cols && i<rows;++j) {
        int k=i;
        while(k<rows && !a[k*cols+j]) ++k;
        if(k==rows) continue;
        if(k!=i) {
            for(int h=0;h<cols;++h) std::swap(a[k*cols+h],a[i*cols+h]);
            output.determinant=P-output.determinant;
        }
        int pivot=a[i*cols+j];
        output.determinant=output.determinant*pivot%P;
        const int inverse=power(pivot,P-2);
        for(int h=j+1;h<cols;++h) a[i*cols+h]=a[i*cols+h]*inverse%P;
        a[i*cols+j]=1;
        for(int k2=i+1;k2<rows;++k2) {
            const int factor=a[k2*cols+j];
            if(!factor) continue;
            for(int h=j+1;h<cols;++h)
                a[k2*cols+h]=(a[k2*cols+h]+P*P-factor*a[i*cols+h])%P;
            a[k2*cols+j]=0;
        }
        output.pivots.push_back(j);
        ++i;
    }
    if(i<rows) output.determinant=0;
    return output;
}

void save(int n,uint32_t initial_seed,int attempt,
          const std::vector<int>& pencil,const std::vector<Point>& pts,
          const std::vector<uint8_t>& matrix,const Elimination& elim,
          double eval_seconds,double elimination_seconds,const std::string& path) {
    const std::string prefix=path+"/permanent_range_n"+std::to_string(n);
    std::ofstream raw(prefix+".u8",std::ios::binary);
    raw.write(reinterpret_cast<const char*>(matrix.data()),matrix.size());
    std::ofstream out(prefix+".json");
    out << "{\n\"n\":" << n << ",\n\"prime\":101,\n\"seed\":" << initial_seed
        << ",\n\"attempt_zero_based\":" << attempt
        << ",\n\"rows\":" << pts.size() << ",\n\"columns\":" << 4*n*n
        << ",\n\"rank\":" << elim.pivots.size()
        << ",\n\"selected_minor_determinant_mod_prime\":" << elim.determinant
        << ",\n\"matrix_encoding\":\"row-major uint8 entries in 0..100, companion .u8 file\""
        << ",\n\"parameter_order\":\"column=4*(n*i+j)+k, indices zero-based\""
        << ",\n\"row_order\":\"degree-n nonnegative quadruples, decreasing lexicographic order\""
        << ",\n\"prng\":\"uint32 state=1664525*state+1013904223; coefficient=(state>>16)%101\""
        << ",\n\"pencil_coefficients_flat_i_j_k\":[";
    for(size_t i=0;i<pencil.size();++i) { if(i) out<<','; out<<pencil[i]; }
    out << "],\n\"evaluation_points\":[";
    for(size_t i=0;i<pts.size();++i) {
        if(i) out<<',';
        out << '[' << pts[i][0] << ',' << pts[i][1] << ',' << pts[i][2] << ',' << pts[i][3] << ']';
    }
    out << "],\n\"selected_columns_zero_based\":[";
    for(size_t i=0;i<elim.pivots.size();++i) { if(i) out<<','; out<<elim.pivots[i]; }
    out << "],\n\"evaluation_seconds\":" << eval_seconds
        << ",\n\"elimination_seconds\":" << elimination_seconds << "\n}\n";
}

int main(int argc,char** argv) {
    if(argc!=4) {std::cerr<<"usage: min_n max_n output_directory\n";return 2;}
    int first=std::stoi(argv[1]),last=std::stoi(argv[2]);
    std::string path=argv[3];
    std::filesystem::create_directories(path);
    for(int n=first;n<=last;++n) {
        if(n<1 || n>16) {std::cerr<<"supported n range is1..16\n";return 3;}
        const auto pts=points(n);
        bool success=false;
        for(int attempt=0;attempt<3 && !success;++attempt) {
            const uint32_t initial_seed=20261121u+1009u*n+104729u*attempt;
            uint32_t state=initial_seed;
            std::vector<int> pencil(4*n*n);
            for(auto &v:pencil) v=(next_random(state)>>16)%P;
            auto begin=std::chrono::steady_clock::now();
            auto matrix=evaluation_jacobian(n,pencil,pts);
            auto middle=std::chrono::steady_clock::now();
            auto elim=eliminate(matrix,pts.size(),4*n*n);
            auto end=std::chrono::steady_clock::now();
            double evaluation=std::chrono::duration<double>(middle-begin).count();
            double elimination=std::chrono::duration<double>(end-middle).count();
            std::cout << "{\"n\":"<<n<<",\"attempt\":"<<attempt
                <<",\"rank\":"<<elim.pivots.size()<<",\"rows\":"<<pts.size()
                <<",\"columns\":"<<4*n*n<<",\"determinant_mod101\":"<<elim.determinant
                <<",\"evaluation_seconds\":"<<evaluation
                <<",\"elimination_seconds\":"<<elimination<<"}"<<std::endl;
            success=elim.pivots.size()==pts.size();
            if(success) save(n,initial_seed,attempt,pencil,pts,matrix,elim,evaluation,elimination,path);
        }
        if(!success) {std::cerr<<"No full rank found at n="<<n<<" in3 tries\n";return 1;}
    }
    return 0;
}
