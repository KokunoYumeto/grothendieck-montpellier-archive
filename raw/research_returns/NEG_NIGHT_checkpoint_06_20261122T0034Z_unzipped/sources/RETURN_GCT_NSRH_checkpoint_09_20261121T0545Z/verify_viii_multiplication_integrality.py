"""Bounded exact audit of VIII's printed multiplication data.

This does not recompute the unprinted multiplication table.  Figure 2
is checked as raw formulas; Figures 24--35 are checked only as their
printed, factored/rescaled coefficient vectors.
"""
from pathlib import Path
import hashlib
import json
import re
import sympy as s

root = Path(__file__).resolve().parents[1]
source = root / 'sources/LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex'
text = source.read_text()
q = s.symbols('q', nonzero=True)

raw = {
    'F2_a': -(1+q)**2*(q*q+q+1)*(q-1)**2/q**3,
    'F2_b': -(q*q+q+1)*(q-1)**2/q**2,
    'F2_c': (1+q)**2/q,
    'F2_d': (1+q)**2*(6*q+5*q*q+5)/q**2,
    'F2_e': (1+q*q)**2*(q*q+q+1)*(q-1)**2/q**4,
    'F2_f': (1+q)**2*(2*q*q+q+1)*(q*q+q+2)/q**3,
}
raw_out = {}
for key, expr in raw.items():
    expanded = s.expand(expr)
    terms = {}
    for term in s.Add.make_args(expanded):
        exponent = term.as_powers_dict().get(q, s.Integer(0))
        assert exponent.is_Integer
        coefficient = s.simplify(term / q**exponent)
        assert coefficient.is_Integer
        terms[int(exponent)] = int(coefficient)
    assert s.expand(sum(c*q**e for e,c in terms.items())-expr) == 0
    numerator, denominator = s.fraction(s.cancel(expr))
    assert len(s.Poly(denominator,q).terms()) == 1
    raw_out[key] = {
        'coefficients': dict(sorted(terms.items())),
        'range': [min(terms),max(terms)],
        'value_at_1': int(expr.subs(q,1)),
        'reduced_denominator': str(denominator),
    }

figures = re.findall(r'\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}', text, re.S)
by_label = {}
for figure in figures:
    label = re.search(r'\\label\{([^}]+)\}',figure)
    if label:
        by_label[label.group(1)] = figure

f2 = by_label['fmultkron2']
assert len(re.findall(r'c\(',f2)) == 13

labels = [
    'fmultcon1','fmult2','fmult3','fmult4','fmult5','fmult6',
    'fmult7_3','fmult8','fmult9','fmult7_4','fmult8_2','fmult9_2',
]
vectors = {}
for number,label in enumerate(labels,24):
    figure = by_label[label]
    body = re.search(r'\\begin\s*\{array\}\{[^}]*\}(.*?)\\end\s*\{array\}',figure,re.S).group(1)
    body = re.sub(r'\\noalign\{\\medskip\}','',body)
    cells = re.split(r'&|\\\\',body)
    values = []
    for cell in cells:
        cell = cell.strip()
        if not cell:
            continue
        assert re.fullmatch(r'-?\d+',cell), (label,cell)
        values.append(int(cell))
    assert values
    vectors[label] = {
        'figure':number,'entries':len(values),
        'minimum':min(values),'maximum':max(values),
        'all_integer':True,
    }

result = {
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'figure_2_labeled_constants':13,
    'figure_2_distinct_formulas':6,
    'raw_formula_audit':raw_out,
    'normalized_vector_audit':vectors,
    'vector_total_entries':sum(v['entries'] for v in vectors.values()),
    'scope':'Only the six printed raw formulas and twelve printed rescaled/factored vector tables. No unprinted table or omitted scaling exponents are reconstructed.',
}
destination = Path(__file__).with_name('viii_multiplication_integrality_certificate.json')
destination.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: all six Figure2 raw formulas have integral Laurent coefficients; all thirteen labeled entries are covered.')
print('PASS: all twelve Figure24--35 vector tables contain signed integers:',result['vector_total_entries'],'entries.')
print(json.dumps(raw_out,indent=2))
print('Saved',destination.name)
