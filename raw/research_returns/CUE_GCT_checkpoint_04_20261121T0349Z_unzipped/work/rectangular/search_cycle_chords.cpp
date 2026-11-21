// Structured exploratory rank calculations. These do not extrapolate n.
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
    std::array<Point,6> forms={Point{1,0,0,0},Point{0,1,0,0},
        Point{0,0,1,0},Point{0,0,0,1},Point{1,0,1,0},Point{1,2,3,4}};
    for(int n=4;n<=8;++n) {
        auto pts=points(n);
        auto base=cycle(n);
        int baseline=eliminate(evaluation_jacobian(n,base,pts),pts.size(),4*n*n).pivots.size();
        std::cout<<"{\"n\":"<<n<<",\"base_rank\":"<<baseline<<"}"<<std::endl;
        for(int j=2;j<n;++j) {
            for(size_t f=0;f<forms.size();++f) {
                auto a=base;
                for(int k=0;k<4;++k) a[4*j+k]=forms[f][k];
                int rank=eliminate(evaluation_jacobian(n,a,pts),pts.size(),4*n*n).pivots.size();
                std::cout<<"{\"n\":"<<n<<",\"chord\":[0,"<<j
                    <<"],\"form\":"<<f<<",\"rank\":"<<rank
                    <<",\"excess\":"<<rank-(2*n*n+2)<<"}"<<std::endl;
            }
        }
    }
}
