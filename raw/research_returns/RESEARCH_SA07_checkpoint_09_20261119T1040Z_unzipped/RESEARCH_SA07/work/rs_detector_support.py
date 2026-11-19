"""MSS2026v1 Proposition4.1, with the exterior quotient made explicit.

Indices in the primary source are one-based; these tuples use zero-based
indices.  S is evaluated modulo omega wedge H via the integral projector
(g-1)id - omega wedge contraction.  No arithmetic image is computed here.
"""
from functools import lru_cache

class RSDetector:
    rterms=(
        (-2,((0,1),(2,4),(3,6),(5,7))),
        (2,((0,1),(2,5),(3,6),(4,7))),
        (2,((0,1),(2,5),(3,7),(4,6))),
        (2,((0,1),(2,6),(3,5),(4,7))),
        (1,((0,2),(1,5),(3,6),(4,7))),
    )
    sterms=(
        (1,((1,2),(5,7),(6,8)),(0,3,4)),
        (-1,((1,2),(3,4),(5,7)),(0,6,8)),
        (1,((3,4),(5,8),(6,7)),(0,1,2)),
        (-1,((1,2),(3,4),(5,8)),(0,6,7)),
        (3,((1,2),(4,6),(7,8)),(0,3,5)),
        (-4,((1,2),(3,5),(4,7)),(0,6,8)),
        (-1,((1,2),(3,6),(4,7)),(0,5,8)),
        (1,((1,3),(2,6),(4,7)),(0,5,8)),
    )
    def __init__(self,alphabet):
        self.alphabet=alphabet
        self.genus=len(alphabet)//2
        self.index={x:i for i,x in enumerate(alphabet)}
    def pair(self,x,y):
        i,j=self.index[x],self.index[y]
        return (1 if i%2==0 else -1) if i//2==j//2 and i!=j else 0
    def wedge(self,letters):
        if len(set(letters))<3:return None,0
        sign=(-1)**sum(letters[i]>letters[j] for i in range(3) for j in range(i+1,3))
        return ''.join(sorted(letters)),sign
    @lru_cache(maxsize=200000)
    def word_values(self,word):
        assert len(word)==9
        rv=0;sv={}
        for coefficient,pairs in self.rterms:
            value=coefficient
            for i,j in pairs:value*=self.pair(word[i],word[j])
            rv+=value
        for coefficient,pairs,output in self.sterms:
            value=coefficient
            for i,j in pairs:value*=self.pair(word[i],word[j])
            if not value:continue
            key,sign=self.wedge(tuple(word[i] for i in output))
            if sign:sv[key]=sv.get(key,0)+sign*value
        return rv,tuple((w,c) for w,c in sv.items() if c)
    def derivation(self,D):
        rr={};ss={}
        for i in range(self.genus):
            for first,poly,sign in ((self.alphabet[2*i],D[self.alphabet[2*i+1]],1),
                                    (self.alphabet[2*i+1],D[self.alphabet[2*i]],-1)):
                for tail,c in poly.items():
                    word=first+tail;r,s=self.word_values(word)
                    if r:rr[word[8]]=rr.get(word[8],0)+sign*c*r
                    for key,value in s:ss[key]=ss.get(key,0)+sign*c*value
        contraction={}
        for word,c in ss.items():
            a,b,d=word
            for x,coefficient in ((d,self.pair(a,b)),(a,self.pair(b,d)),(b,self.pair(d,a))):
                if coefficient:contraction[x]=contraction.get(x,0)+c*coefficient
        primitive={w:(self.genus-1)*c for w,c in ss.items()}
        for x,c in contraction.items():
            for i in range(self.genus):
                word,sign=self.wedge((self.alphabet[2*i],self.alphabet[2*i+1],x))
                if sign:primitive[word]=primitive.get(word,0)-c*sign
        return {w:c for w,c in rr.items() if c},{w:c for w,c in primitive.items() if c}
