// Exact maximal-rank certificates, allowing row rank below the full target.
// Uses the already audited subset-DP evaluator; certificate rows are explicit.
#define main prior_permanent_range_main
#include "check_permanent_range.cpp"
#undef main

struct RankCertificate {
    std::vector<int> rows, columns;
    int determinant = 1;
};

RankCertificate select_minor(std::vector<uint8_t> a, int rows, int columns) {
    RankCertificate out;
    std::vector<int> row_names(rows);
    std::iota(row_names.begin(), row_names.end(), 0);
    int i = 0;
    for(int j=0; j<columns && i<rows; ++j) {
        int k=i;
        while(k<rows && !a[k*columns+j]) ++k;
        if(k==rows) continue;
        if(k!=i) {
            std::swap(row_names[k],row_names[i]);
            for(int h=0;h<columns;++h) std::swap(a[k*columns+h],a[i*columns+h]);
        }
        int pivot=a[i*columns+j];
        // Rows are recorded in pivot-selection order, so no swap sign enters.
        out.determinant=out.determinant*pivot%P;
        int inv=power(pivot,P-2);
        for(int h=j+1;h<columns;++h) a[i*columns+h]=a[i*columns+h]*inv%P;
        a[i*columns+j]=1;
        for(int k2=i+1;k2<rows;++k2) {
            int factor=a[k2*columns+j];
            if(!factor) continue;
            for(int h=j+1;h<columns;++h)
                a[k2*columns+h]=(a[k2*columns+h]+P*P-factor*a[i*columns+h])%P;
            a[k2*columns+j]=0;
        }
        out.rows.push_back(row_names[i]);
        out.columns.push_back(j);
        ++i;
    }
    return out;
}

int main(int argc,char** argv) {
    if(argc!=4) {std::cerr<<"usage: min_n max_n output_directory\n";return 2;}
    int first=std::stoi(argv[1]),last=std::stoi(argv[2]);
    std::string path=argv[3];
    std::filesystem::create_directories(path);
    for(int n=first;n<=last;++n) {
        if(n<17 || n>20) {std::cerr<<"bounded supported range17..20\n";return 3;}
        uint32_t seed=20261121u+1009u*n,state=seed;
        std::vector<int> pencil(4*n*n);
        for(auto &v:pencil) v=(next_random(state)>>16)%P;
        auto pts=points(n);
        auto begin=std::chrono::steady_clock::now();
        auto matrix=evaluation_jacobian(n,pencil,pts);
        auto middle=std::chrono::steady_clock::now();
        auto cert=select_minor(matrix,pts.size(),4*n*n);
        auto end=std::chrono::steady_clock::now();
        std::string prefix=path+"/permanent_range_n"+std::to_string(n);
        std::ofstream raw(prefix+".u8",std::ios::binary);
        raw.write(reinterpret_cast<const char*>(matrix.data()),matrix.size());
        std::ofstream out(prefix+".json");
        out<<"{\n\"n\":"<<n<<",\n\"prime\":101,\n\"seed\":"<<seed
           <<",\n\"attempt_zero_based\":0,\n\"rows\":"<<pts.size()
           <<",\n\"columns\":"<<4*n*n<<",\n\"rank\":"<<cert.rows.size()
           <<",\n\"torus_upper_bound\":"<<4*n*n-2*n+2
           <<",\n\"selected_minor_determinant_mod_prime\":"<<cert.determinant
           <<",\n\"parameter_order\":\"column=4*(n*i+j)+k; zero-based\""
           <<",\n\"row_order\":\"degree-n nonnegative quadruples in decreasing lexicographic order\""
           <<",\n\"matrix_encoding\":\"row-major uint8 entries0..100; companion .u8 file\""
           <<",\n\"prng\":\"uint32 state=1664525*state+1013904223; coefficient=(state>>16)%101\""
           <<",\n\"pencil_coefficients_flat_i_j_k\":[";
        for(size_t i=0;i<pencil.size();++i) {if(i) out<<',';out<<pencil[i];}
        out<<"],\n\"evaluation_points\":[";
        for(size_t i=0;i<pts.size();++i) {
            if(i) out<<',';
            out<<'['<<pts[i][0]<<','<<pts[i][1]<<','<<pts[i][2]<<','<<pts[i][3]<<']';
        }
        out<<"],\n\"selected_rows_zero_based_in_minor_order\":[";
        for(size_t i=0;i<cert.rows.size();++i) {if(i) out<<',';out<<cert.rows[i];}
        out<<"],\n\"selected_columns_zero_based\":[";
        for(size_t i=0;i<cert.columns.size();++i) {if(i) out<<',';out<<cert.columns[i];}
        double eval=std::chrono::duration<double>(middle-begin).count();
        double elim=std::chrono::duration<double>(end-middle).count();
        out<<"],\n\"evaluation_seconds\":"<<eval
           <<",\n\"elimination_seconds\":"<<elim<<"\n}\n";
        std::cout<<"{\"n\":"<<n<<",\"rank\":"<<cert.rows.size()
                 <<",\"torus_upper_bound\":"<<4*n*n-2*n+2
                 <<",\"minor_mod101\":"<<cert.determinant
                 <<",\"evaluation_seconds\":"<<eval
                 <<",\"elimination_seconds\":"<<elim<<"}"<<std::endl;
        if(cert.rows.size()!=static_cast<size_t>(4*n*n-2*n+2)) return 1;
    }
    return 0;
}
