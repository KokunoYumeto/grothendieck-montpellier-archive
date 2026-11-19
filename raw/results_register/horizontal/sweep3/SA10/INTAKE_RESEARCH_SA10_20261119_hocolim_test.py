import sys
src = open(sys.argv[1], encoding='utf-8').read().split("allp = list(SP)")[0]
g = {}
exec(src, g)
C = (['r+', 'u', 'r-', 'd'], [('r+', 'u'), ('u', 'r-'), ('r-', 'd'), ('d', 'r+')])
g['SP'].clear(); g['VMAP'].clear()
g['SP'].update({'W0': (['o'], []), 'W1': C, 'W2': (['U', 'D'], []), 'W01': C, 'W02': (['U', 'D'], []),
                'W12': (['U', 'D'], []), 'W012': (['U', 'D'], [])})
idC = {v: v for v in C[0]}
ud = {'U': 'u', 'D': 'd'}; UD = {'U': 'U', 'D': 'D'}
g['VMAP'].update({('W01', 'W0'): {v: 'o' for v in C[0]}, ('W01', 'W1'): idC,
                  ('W02', 'W0'): {'U': 'o', 'D': 'o'}, ('W02', 'W2'): UD, ('W12', 'W1'): ud, ('W12', 'W2'): UD,
                  ('W012', 'W01'): ud, ('W012', 'W02'): UD, ('W012', 'W12'): UD, ('W012', 'W0'): {'U': 'o', 'D': 'o'},
                  ('W012', 'W1'): ud, ('W012', 'W2'): UD})
print('actual Cech cover of C (expected 1,0,0):', g['homology'](list(g['SP'])))
g['SP'].clear(); g['VMAP'].clear()
g['SP'].update({'a': (['o'], []), 'b': (['o'], []), 'm': (['x', 'y'], [])})
g['VMAP'].update({('m', 'a'): {'x': 'o', 'y': 'o'}, ('m', 'b'): {'x': 'o', 'y': 'o'}})
print('pt <- two points -> pt (expected 1,1):', g['homology'](['a', 'b', 'm']))
