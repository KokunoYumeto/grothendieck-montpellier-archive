"""(g) Fixed weights of the chain elements (paper P5, Lemma on fixed tangent dimensions).
a0805369bae2ebddc (Claude Opus 5.5 at effort high), 25 Nov 2026."""
import itertools
out=[]
ok=True
for n in range(2,21):
    M=2**(n-1)
    w=[pow(-2,i,M) for i in range(n-1)]+[0]          # w_1..w_n of the Kronecker element (0-based)
    # U_n = W + S_(2,1)W : weights e_i (mult 1), 2e_i+e_j i!=j (mult 1), e_i+e_j+e_k distinct (mult 2)
    fixed = sum(1 for i in range(n) if w[i]%M==0)
    fixed += sum(1 for i in range(n) for j in range(n) if i!=j and (2*w[i]+w[j])%M==0)
    fixed += 2*sum(1 for i,j,k in itertools.combinations(range(n),3) if (w[i]+w[j]+w[k])%M==0)
    chain = all((2*w[i]+w[i+1])%M==0 for i in range(n-1))
    ok &= fixed==n and chain
    if n>=4:
        # cubic forms: monomials x^a with |a|=3 fixed by diag(zeta^{w_i}) (same weights)
        mons=[c for c in itertools.combinations_with_replacement(range(n),3) if sum(w[i] for i in c)%M==0]
        ok &= len(mons)==n
out.append(f"(g) fixed weight spaces: dim U_n^g = n and dim (Sym^3)^g = n (n>=4), 2<=n<=20: {ok}")
print(out[0])
open('p5_checks_output.txt','a',encoding='utf-8').write(out[0]+'\n')
