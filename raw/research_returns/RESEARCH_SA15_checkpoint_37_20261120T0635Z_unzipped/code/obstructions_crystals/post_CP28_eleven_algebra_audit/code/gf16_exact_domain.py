"""Small exact GF(16) domain for bounded polynomial elimination."""
from sympy.polys.domains.field import Field
from sympy.polys.polyerrors import CoercionFailed
from sympy import Integer,Symbol

def raw_mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&16:a^=19
    return out

MUL=tuple(tuple(raw_mul(a,b) for b in range(16)) for a in range(16))
INV=tuple(0 if a==0 else next(b for b in range(1,16) if MUL[a][b]==1) for a in range(16))

class F16:
    __slots__=('v',)
    def __init__(self,v=0):self.v=v.v if isinstance(v,F16) else int(v)&15
    @staticmethod
    def coerce(v):
        if isinstance(v,F16):return v.v
        if isinstance(v,int):return v&1
        return None
    def __add__(self,b):
        c=self.coerce(b)
        return NotImplemented if c is None else F16(self.v^c)
    __radd__=__add__
    __sub__=__add__
    __rsub__=__add__
    def __neg__(self):return self
    def __pos__(self):return self
    def __mul__(self,b):
        c=self.coerce(b)
        return NotImplemented if c is None else F16(MUL[self.v][c])
    __rmul__=__mul__
    def __truediv__(self,b):
        c=self.coerce(b)
        if c is None:return NotImplemented
        if not c:raise ZeroDivisionError
        return F16(MUL[self.v][INV[c]])
    def __rtruediv__(self,b):
        c=self.coerce(b)
        return NotImplemented if c is None else F16(c)/self
    __floordiv__=__truediv__
    def __pow__(self,n):
        if n<0:return (F16(1)/self)**(-n)
        out=F16(1);a=self
        while n:
            if n&1:out=out*a
            a=a*a;n>>=1
        return out
    def __bool__(self):return bool(self.v)
    def __eq__(self,b):return self.v==b.v if isinstance(b,F16) else isinstance(b,int) and b in (0,1) and self.v==b
    def __hash__(self):return hash(self.v)
    def __str__(self):return f'u{self.v}'
    __repr__=__str__
    def __int__(self):return self.v

class GF16Exact(Field):
    def __init__(self):pass
    dtype=F16
    zero=F16(0)
    one=F16(1)
    rep='GF16Exact'
    is_Exact=True
    is_Numerical=True
    is_FiniteField=True
    has_assoc_Ring=False
    def __str__(self):return 'GF(16; u^4+u+1)'
    def __hash__(self):return hash('GF16Exact19')
    def __eq__(self,other):return isinstance(other,GF16Exact)
    def characteristic(self):return 2
    def get_field(self):return self
    def convert(self,a,base=None):
        if isinstance(a,F16):return a
        if isinstance(a,(int,Integer)):return F16(int(a)&1)
        raise CoercionFailed(f'Cannot convert {a!r} to GF16Exact')
    def from_sympy(self,a):return self.convert(a)
    def to_sympy(self,a):
        u=Symbol('u')
        return sum((u**i for i in range(4) if a.v>>i&1),Integer(0))
    def is_positive(self,a):return bool(a)
    def is_negative(self,a):return False
    def canonical_unit(self,a):return self.one

K16=GF16Exact()

def verify_field():
    vals=[F16(a) for a in range(16)]
    assert F16(2)**4+F16(2)+1==0
    assert all(a**16==a for a in vals)
    assert all(a/a==1 for a in vals[1:])
    assert all(a*(b+c)==a*b+a*c for a in vals for b in vals for c in vals)
    return {'field_elements':16,'distributivity_triples':4096,'modulus':19}
