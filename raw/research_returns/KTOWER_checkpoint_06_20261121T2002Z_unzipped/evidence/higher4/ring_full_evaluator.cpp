// Complete exact identifying-row evaluation and two determinants over
// (Z/M)[w]/(w*w-w+2). No primality or field assumption is made.
// The companion Python wrapper first checks the complete archived model.
// Build: g++ -O3 -std=c++17 -fopenmp ring_full_evaluator.cpp -lgmpxx -lgmp
#include <gmpxx.h>
#include <omp.h>
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using Z = mpz_class;
struct R { Z a = 0, b = 0; };
static Z M;
struct Inconclusive : std::runtime_error { using std::runtime_error::runtime_error; };
static void require(bool yes, const std::string& message) {
    if (!yes) throw std::runtime_error(message);
}
static void reduce(Z& x) { mpz_mod(x.get_mpz_t(), x.get_mpz_t(), M.get_mpz_t()); }
static Z reduced(Z x) { reduce(x); return x; }
struct Scratch { Z ac, bd, cross, sx, sy, twice; };

// Output may alias an input. The three-product formula is
// (a+bw)(c+dw)=(ac-2bd)+((a+b)(c+d)-ac)w.
static void multiply(R& out, const R& x, const R& y, Scratch& t) {
    if (x.b == 0 && y.b == 0) {
        mpz_mul(t.ac.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_mod(out.a.get_mpz_t(), t.ac.get_mpz_t(), M.get_mpz_t());
        out.b = 0;
        return;
    }
    if (x.b == 0) {
        mpz_mul(t.ac.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_mul(t.cross.get_mpz_t(), x.a.get_mpz_t(), y.b.get_mpz_t());
    } else if (y.b == 0) {
        mpz_mul(t.ac.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_mul(t.cross.get_mpz_t(), x.b.get_mpz_t(), y.a.get_mpz_t());
    } else {
        mpz_mul(t.ac.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_mul(t.bd.get_mpz_t(), x.b.get_mpz_t(), y.b.get_mpz_t());
        mpz_add(t.sx.get_mpz_t(), x.a.get_mpz_t(), x.b.get_mpz_t());
        mpz_add(t.sy.get_mpz_t(), y.a.get_mpz_t(), y.b.get_mpz_t());
        mpz_mul(t.cross.get_mpz_t(), t.sx.get_mpz_t(), t.sy.get_mpz_t());
        mpz_sub(t.cross.get_mpz_t(), t.cross.get_mpz_t(), t.ac.get_mpz_t());
        mpz_mul_2exp(t.twice.get_mpz_t(), t.bd.get_mpz_t(), 1);
        mpz_sub(t.ac.get_mpz_t(), t.ac.get_mpz_t(), t.twice.get_mpz_t());
    }
    mpz_mod(out.a.get_mpz_t(), t.ac.get_mpz_t(), M.get_mpz_t());
    mpz_mod(out.b.get_mpz_t(), t.cross.get_mpz_t(), M.get_mpz_t());
}

// Fused dst -= x*y reduces once per coordinate. dst is distinct from x,y.
static void subtract_product(R& dst, const R& x, const R& y, Scratch& t) {
    if (x.b == 0 && y.b == 0) {
        mpz_submul(dst.a.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        reduce(dst.a);
        return;
    }
    if (x.b == 0) {
        mpz_submul(dst.a.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_submul(dst.b.get_mpz_t(), x.a.get_mpz_t(), y.b.get_mpz_t());
    } else if (y.b == 0) {
        mpz_submul(dst.a.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_submul(dst.b.get_mpz_t(), x.b.get_mpz_t(), y.a.get_mpz_t());
    } else {
        mpz_mul(t.ac.get_mpz_t(), x.a.get_mpz_t(), y.a.get_mpz_t());
        mpz_mul(t.bd.get_mpz_t(), x.b.get_mpz_t(), y.b.get_mpz_t());
        mpz_add(t.sx.get_mpz_t(), x.a.get_mpz_t(), x.b.get_mpz_t());
        mpz_add(t.sy.get_mpz_t(), y.a.get_mpz_t(), y.b.get_mpz_t());
        mpz_mul(t.cross.get_mpz_t(), t.sx.get_mpz_t(), t.sy.get_mpz_t());
        mpz_sub(t.cross.get_mpz_t(), t.cross.get_mpz_t(), t.ac.get_mpz_t());
        mpz_sub(dst.a.get_mpz_t(), dst.a.get_mpz_t(), t.ac.get_mpz_t());
        mpz_mul_2exp(t.twice.get_mpz_t(), t.bd.get_mpz_t(), 1);
        mpz_add(dst.a.get_mpz_t(), dst.a.get_mpz_t(), t.twice.get_mpz_t());
        mpz_sub(dst.b.get_mpz_t(), dst.b.get_mpz_t(), t.cross.get_mpz_t());
    }
    reduce(dst.a); reduce(dst.b);
}
static Z norm(const R& x) { return reduced(x.a*x.a + x.a*x.b + 2*x.b*x.b); }
static Z common(const Z& x) { Z g; mpz_gcd(g.get_mpz_t(), x.get_mpz_t(), M.get_mpz_t()); return g; }
static bool unit(const R& x) { return common(norm(x)) == 1; }
static R inverse(const R& x) {
    Z n = norm(x), t;
    require(mpz_invert(t.get_mpz_t(), n.get_mpz_t(), M.get_mpz_t()) != 0,
            "attempt to invert a nonunit norm");
    return {reduced((x.a+x.b)*t), reduced(-x.b*t)};
}
static R conjugate(const R& x) { return {reduced(x.a+x.b), reduced(-x.b)}; }
static unsigned count(std::istream& in, const std::string& label) {
    long long x;
    require(bool(in >> x) && x >= 0 && x <= std::numeric_limits<int>::max(),
            "bad count: " + label);
    return unsigned(x);
}
static Z integer(std::istream& in, const std::string& label) {
    Z x; require(bool(in >> x), "missing integer: " + label); return x;
}
static void end_input(std::istream& in) {
    std::string extra; require(!(in >> extra), "trailing input");
}
using Exponent = std::array<unsigned,2>;
using Orbit = std::array<Exponent,3>;
using Monomial = std::array<unsigned,3>;
using Frame = std::array<std::array<R,3>,3>; // columns, then coordinates
using Point = std::array<std::array<Z,3>,2>;
struct Model {
    unsigned k, source, d;
    Z E, E2;
    std::vector<std::vector<Monomial>> expanded;
    std::vector<Exponent> pairs;
    std::vector<std::vector<std::pair<unsigned,Z>>> basis;
    std::vector<Point> points;
    std::array<std::vector<Frame>,2> frames;
};
static Model read_model(std::istream& in) {
    M = integer(in, "modulus"); require(M > 1, "modulus must exceed one");
    Model m;
    m.k=count(in,"k"); m.source=count(in,"source dimension"); m.d=count(in,"dimension");
    require(m.k>=1 && m.source>0 && m.d>0 && m.d<=m.source, "invalid dimensions");
    require(size_t(m.d) <= std::numeric_limits<size_t>::max()/m.d,
            "matrix size overflow");
    Z factorial; mpz_fac_ui(factorial.get_mpz_t(), 2UL*m.k+1);
    require(common(336*factorial)==1, "coefficient denominator is not a unit");
    Z power; mpz_ui_pow_ui(power.get_mpz_t(),2,m.k+1);
    m.E=reduced(1+power+power*power); m.E2=reduced(m.E*m.E);
    require(common(m.E)==1, "comparison parameter is not a unit");
    std::vector<Orbit> source(m.source);
    std::set<Exponent> pair_set;
    for(unsigned j=0;j<m.source;j++) {
        unsigned sz=0,sw=0;
        for(auto& ab:source[j]) {
            ab[0]=count(in,"exponent"); ab[1]=count(in,"exponent");
            require(ab[0]<=m.k && ab[1]<=m.k && (ab[0]%2)==(ab[1]%2),
                    "invalid orbit exponent");
            sz+=ab[0]; sw+=ab[1]; pair_set.insert(ab);
        }
        require(sz==m.k && sw==m.k, "wrong orbit bidegree");
        require(std::is_sorted(source[j].begin(),source[j].end()), "unsorted orbit");
        if(j) require(source[j-1]<source[j], "duplicate or unsorted source orbit");
    }
    m.pairs.assign(pair_set.begin(),pair_set.end());
    m.expanded.resize(m.source);
    for(unsigned j=0;j<m.source;j++) {
        Orbit o=source[j];
        do {
            Monomial mon;
            for(unsigned i=0;i<3;i++)
                mon[i]=unsigned(std::lower_bound(m.pairs.begin(),m.pairs.end(),o[i])-m.pairs.begin());
            m.expanded[j].push_back(mon);
        } while(std::next_permutation(o.begin(),o.end()));
    }
    m.basis.resize(m.d);
    for(auto& col:m.basis) {
        unsigned n=count(in,"sparse column length");
        require(n>0 && n<=m.source, "invalid sparse column length");
        std::set<unsigned> seen;
        for(unsigned j=0;j<n;j++) {
            unsigned i=count(in,"sparse row index"); Z c=integer(in,"coefficient");
            require(i<m.source && c>0 && c<M && seen.insert(i).second,
                    "invalid sparse basis entry");
            col.emplace_back(i,std::move(c));
        }
    }
    unsigned np=count(in,"point count"); require(np==m.d+2, "wrong point count");
    m.points.resize(np);
    for(auto& point:m.points) for(auto& row:point) for(auto& x:row) {
        x=integer(in,"point coordinate"); reduce(x);
    }
    for(unsigned c=0;c<2;c++) {
        unsigned n=count(in,"frame count"); require(n==(c==0?6U:7U), "wrong frame count");
        m.frames[c].resize(n);
        for(auto& frame:m.frames[c]) for(auto& col:frame) for(auto& x:col) {
            x.a=integer(in,"frame coefficient"); x.b=integer(in,"frame coefficient");
            reduce(x.a); reduce(x.b);
        }
    }
    end_input(in); return m;
}

struct Workspace {
    std::array<std::vector<R>,3> zp,wp,values;
    std::vector<R> base,current,sum2,sum4,schur;
    Scratch scratch;
    R term,product;
    explicit Workspace(const Model& m) : base(m.source),current(m.source),
        sum2(m.source),sum4(m.source),schur(m.source) {
        for(unsigned i=0;i<3;i++) {
            zp[i].resize(m.k+1); wp[i].resize(m.k+1); values[i].resize(m.pairs.size());
        }
    }
    void evaluate(const Model& m,const std::array<R,3>& z,const std::array<R,3>& w,
                  std::vector<R>& result) {
        for(unsigned i=0;i<3;i++) {
            zp[i][0]={1,0}; wp[i][0]={1,0};
            for(unsigned j=1;j<=m.k;j++) {
                multiply(zp[i][j],zp[i][j-1],z[i],scratch);
                multiply(wp[i][j],wp[i][j-1],w[i],scratch);
            }
            for(unsigned j=0;j<m.pairs.size();j++)
                multiply(values[i][j],zp[i][m.pairs[j][0]],wp[i][m.pairs[j][1]],scratch);
        }
        for(unsigned j=0;j<m.source;j++) {
            result[j]={0,0};
            for(const auto& mon:m.expanded[j]) {
                multiply(term,values[0][mon[0]],values[1][mon[1]],scratch);
                multiply(product,term,values[2][mon[2]],scratch);
                result[j].a+=product.a; result[j].b+=product.b;
            }
            reduce(result[j].a); reduce(result[j].b);
        }
    }
    void frame_sum(const Model& m,const std::array<R,3>& z,const std::array<R,3>& w,
                   const std::vector<Frame>& frames,std::vector<R>& result) {
        for(auto& x:result) x={0,0};
        for(const auto& frame:frames) {
            std::array<R,3> zz,ww;
            for(unsigned j=0;j<3;j++) {
                for(unsigned i=0;i<3;i++) {
                    R bar=conjugate(frame[j][i]);
                    multiply(term,bar,z[i],scratch); zz[j].a+=term.a; zz[j].b+=term.b;
                    multiply(term,frame[j][i],w[i],scratch); ww[j].a+=term.a; ww[j].b+=term.b;
                }
                reduce(zz[j].a); reduce(zz[j].b); reduce(ww[j].a); reduce(ww[j].b);
            }
            evaluate(m,zz,ww,current);
            for(unsigned j=0;j<m.source;j++) {
                result[j].a+=current[j].a; result[j].b+=current[j].b;
            }
        }
        for(auto& x:result) { reduce(x.a); reduce(x.b); }
    }
    static void project(const Model& m,const std::vector<R>& values,std::vector<R>& result) {
        result.resize(m.d);
        for(unsigned j=0;j<m.d;j++) {
            result[j]={0,0};
            for(const auto& entry:m.basis[j]) {
                mpz_addmul(result[j].a.get_mpz_t(),values[entry.first].a.get_mpz_t(),entry.second.get_mpz_t());
                mpz_addmul(result[j].b.get_mpz_t(),values[entry.first].b.get_mpz_t(),entry.second.get_mpz_t());
            }
            reduce(result[j].a); reduce(result[j].b);
        }
    }
    void row(const Model& m,unsigned index,std::vector<R>& a,std::vector<R>& s) {
        std::array<R,3> z,w;
        for(unsigned j=0;j<3;j++) { z[j]={m.points[index][0][j],0}; w[j]={m.points[index][1][j],0}; }
        evaluate(m,z,w,base);
        frame_sum(m,z,w,m.frames[0],sum2); frame_sum(m,z,w,m.frames[1],sum4);
        for(unsigned j=0;j<m.source;j++) {
            schur[j].a=reduced(m.E2*base[j].a-m.E*sum2[j].a-sum4[j].a);
            schur[j].b=reduced(m.E2*base[j].b-m.E*sum2[j].b-sum4[j].b);
        }
        project(m,base,a); project(m,schur,s);
    }
};

static R determinant_ring(std::vector<R>& a,unsigned n,int threads) {
    R det{1,0}; Scratch scratch;
    for(unsigned k=0;k<n;k++) {
        if(k+1==n) { multiply(det,det,a[size_t(k)*n+k],scratch); break; }
        unsigned p=k; while(p<n && !unit(a[size_t(p)*n+k])) p++;
        if(p==n) throw Inconclusive("quadratic determinant: unit pivot unavailable at "+std::to_string(k));
        if(p!=k) {
            for(unsigned j=k;j<n;j++) std::swap(a[size_t(k)*n+j],a[size_t(p)*n+j]);
            det.a=reduced(-det.a); det.b=reduced(-det.b);
        }
        R pivot=a[size_t(k)*n+k], inv=inverse(pivot);
        multiply(det,det,pivot,scratch);
        #pragma omp parallel for schedule(static) num_threads(threads)
        for(int ii=int(k)+1;ii<int(n);ii++) {
            unsigned i=unsigned(ii); Scratch local; R factor;
            multiply(factor,a[size_t(i)*n+k],inv,local);
            if(factor.a!=0 || factor.b!=0)
                for(unsigned j=k+1;j<n;j++)
                    subtract_product(a[size_t(i)*n+j],factor,a[size_t(k)*n+j],local);
            a[size_t(i)*n+k]={0,0};
        }
        if((k+1)%100==0) std::cerr<<"quadratic determinant pivots "<<k+1<<"/"<<n<<"\n";
    }
    return det;
}
static Z determinant_scalar(std::vector<Z>& a,unsigned n,int threads) {
    Z det=1;
    for(unsigned k=0;k<n;k++) {
        if(k+1==n) { det=reduced(det*a[size_t(k)*n+k]); break; }
        unsigned p=k; while(p<n && common(a[size_t(p)*n+k])!=1) p++;
        if(p==n) throw Inconclusive("scalar determinant: unit pivot unavailable at "+std::to_string(k));
        if(p!=k) {
            for(unsigned j=k;j<n;j++) std::swap(a[size_t(k)*n+j],a[size_t(p)*n+j]);
            det=reduced(-det);
        }
        Z pivot=a[size_t(k)*n+k],inv;
        require(mpz_invert(inv.get_mpz_t(),pivot.get_mpz_t(),M.get_mpz_t())!=0,"nonunit scalar pivot");
        det=reduced(det*pivot);
        #pragma omp parallel for schedule(static) num_threads(threads)
        for(int ii=int(k)+1;ii<int(n);ii++) {
            unsigned i=unsigned(ii); Z factor=reduced(a[size_t(i)*n+k]*inv);
            if(factor!=0) for(unsigned j=k+1;j<n;j++) {
                mpz_submul(a[size_t(i)*n+j].get_mpz_t(),factor.get_mpz_t(),a[size_t(k)*n+j].get_mpz_t());
                reduce(a[size_t(i)*n+j]);
            }
            a[size_t(i)*n+k]=0;
        }
        if((k+1)%100==0) std::cerr<<"scalar determinant pivots "<<k+1<<"/"<<n<<"\n";
    }
    return det;
}
static void print_ring(std::ostream& out,const R& x) { out<<'['<<x.a<<','<<x.b<<']'; }
static void print_row(std::ostream& out,const std::vector<R>& row) {
    out<<'['; for(unsigned j=0;j<row.size();j++) { if(j) out<<','; print_ring(out,row[j]); } out<<']';
}
static std::set<unsigned> sample_indices(const std::string& arg) {
    std::set<unsigned> out; std::stringstream input(arg); std::string item;
    while(std::getline(input,item,',')) {
        require(!item.empty(),"empty sample index"); std::stringstream one(item);
        unsigned i=count(one,"sample index"); end_input(one); require(out.insert(i).second,"duplicate sample index");
    }
    return out;
}
static int determinant_mode() {
    M=integer(std::cin,"modulus"); require(M>1,"bad modulus");
    unsigned n=count(std::cin,"matrix dimension");
    require(n==0 || size_t(n)<=std::numeric_limits<size_t>::max()/n,"matrix size overflow");
    std::vector<R> a(size_t(n)*n);
    for(auto& x:a) { x.a=integer(std::cin,"matrix coefficient"); x.b=integer(std::cin,"matrix coefficient"); reduce(x.a); reduce(x.b); }
    end_input(std::cin); R det=determinant_ring(a,n,1); Z g=common(norm(det));
    std::cout<<"{\"status\":\""<<(g==1?"UNIT_DETERMINANT":"NONUNIT_DETERMINANT")<<"\",\"determinant\":";
    print_ring(std::cout,det); std::cout<<",\"gcd_norm\":"<<g<<"}\n";
    return g==1?0:3;
}

int main(int argc,char** argv) {
    try {
        if(argc==2 && std::string(argv[1])=="--determinant") return determinant_mode();
        require(argc>=2,"usage: ring_full_evaluator model.txt [--threads N] [--sample-rows i,j] [--sample-output path]");
        int threads=1; std::set<unsigned> samples; std::string sample_output;
        for(int i=2;i<argc;i++) {
            std::string key=argv[i]; require(i+1<argc,"missing option argument"); std::string val=argv[++i];
            if(key=="--threads") { std::stringstream s(val); threads=int(count(s,"threads")); end_input(s); require(threads>=1&&threads<=4,"threads must be1..4"); }
            else if(key=="--sample-rows") samples=sample_indices(val);
            else if(key=="--sample-output") sample_output=val;
            else throw std::runtime_error("unknown option");
        }
        require(samples.empty()==sample_output.empty(),"sample indices and output must be supplied together");
        std::ifstream input(argv[1]); require(bool(input),"cannot open model");
        Model m=read_model(input);
        for(unsigned i:samples) require(i<m.points.size(),"sample row outside supplied points");
        auto start=std::chrono::steady_clock::now();
        std::vector<Z> a(size_t(m.d)*m.d);
        std::vector<R> s(size_t(m.d)*m.d);
        std::atomic<unsigned> completed{0}; std::atomic<bool> failed{false};
        #pragma omp parallel num_threads(threads)
        {
            Workspace work(m); std::vector<R> ar,sr;
            #pragma omp for schedule(dynamic,1)
            for(int ii=0;ii<int(m.d);ii++) {
                unsigned i=unsigned(ii); work.row(m,i,ar,sr);
                for(unsigned j=0;j<m.d;j++) {
                    if(ar[j].b!=0) failed=true;
                    a[size_t(i)*m.d+j]=ar[j].a; s[size_t(i)*m.d+j]=sr[j];
                }
                unsigned done=++completed;
                if(done%50==0 || done==m.d) {
                    #pragma omp critical
                    std::cerr<<"native complete identifying rows "<<done<<"/"<<m.d<<"\n";
                }
            }
        }
        require(!failed && completed==m.d,"incomplete or nonscalar identifying evaluation");
        unsigned extra=0;
        if(!samples.empty()) {
            std::ofstream out(sample_output); require(bool(out),"cannot create sample output");
            out<<"{\"modulus\":"<<M<<",\"k\":"<<m.k<<",\"dimension\":"<<m.d<<",\"rows\":[";
            bool first=true; Workspace work(m); std::vector<R> ar(m.d),sr(m.d);
            for(unsigned i:samples) {
                if(i<m.d) for(unsigned j=0;j<m.d;j++) { ar[j]={a[size_t(i)*m.d+j],0}; sr[j]=s[size_t(i)*m.d+j]; }
                else { work.row(m,i,ar,sr); extra++; }
                if(!first) out<<','; first=false;
                out<<"{\"index\":"<<i<<",\"evaluation\":"; print_row(out,ar);
                out<<",\"schur\":"; print_row(out,sr); out<<'}';
            }
            out<<"]}\n"; require(bool(out),"sample write failed");
        }
        Z da=determinant_scalar(a,m.d,threads); R det_a{da,0};
        require(unit(det_a),"evaluation determinant is a nonunit");
        R det_s=determinant_ring(s,m.d,threads), det_o; Scratch scratch;
        multiply(det_o,det_s,inverse(det_a),scratch);
        Z g=common(norm(det_o));
        double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::cout<<"{\"status\":\""<<(g==1?"PASS_NATIVE_COMPLETE":"NONUNIT_SCHUR_DETERMINANT")
          <<"\",\"modulus\":"<<M<<",\"k\":"<<m.k<<",\"dimension\":"<<m.d
          <<",\"source_dimension\":"<<m.source<<",\"comparison_point_modulus\":"<<m.E
          <<",\"all_recomputed_evaluation_rows\":"<<completed
          <<",\"frame_counts\":[6,7],\"extra_rows_evaluated\":"<<extra
          <<",\"native_threads\":"<<threads<<",\"unit_pivots_per_determinant\":"<<m.d-1
          <<",\"det_evaluation\":"; print_ring(std::cout,det_a);
        std::cout<<",\"det_schur_evaluations\":"; print_ring(std::cout,det_s);
        std::cout<<",\"det_schur_operator\":"; print_ring(std::cout,det_o);
        std::cout<<",\"gcd_norm_determinant_modulus\":"<<g<<",\"elapsed_seconds\":"<<seconds<<"}\n";
        return g==1?0:3;
    } catch(const Inconclusive& e) {
        std::cout<<"{\"status\":\"INCONCLUSIVE_UNIT_PIVOT\",\"error\":"<<std::quoted(e.what())<<"}\n";
        return 2;
    } catch(const std::exception& e) {
        std::cout<<"{\"status\":\"ERROR\",\"error\":"<<std::quoted(e.what())<<"}\n";
        return 2;
    }
}
