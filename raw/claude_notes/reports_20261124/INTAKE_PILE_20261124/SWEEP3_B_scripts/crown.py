import importlib.util,sys
sys.argv=['x','0']
spec=importlib.util.spec_from_file_location('c','sa21_check.py'); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
down=[frozenset(),frozenset(),frozenset({0,1}),frozenset({0,1})]  # a=0,b=1 < c=2,d=3
syms,N=c.M(down); m=len(syms); fam=c.closed_sets(N,m)
print('strata',m,'supports',len(fam),'OML',c.is_oml(fam,N,m),'conditional',c.conditional(down,4))
