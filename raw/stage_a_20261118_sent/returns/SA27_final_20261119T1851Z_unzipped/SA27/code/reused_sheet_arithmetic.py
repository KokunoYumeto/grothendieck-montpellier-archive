"""Arithmetic QA only: the reused sheet is not a homotopy-theory claim."""
from decimal import Decimal as D
import json
dea=[D(x) for x in ['748.80','374.40','748.80','1497.60','1497.60','748.80']]
contributions=[D(x) for x in ['977.71','1238.10','1750.00','319.57','144.90','765.85','212.45','353.51']]
alternative=contributions.copy();alternative[5]=D('765.35')
result={
    'source':'MPL_118_transcription.tex, scan004, combined lines43–75',
    'DEA_sum':str(sum(dea)),
    'contributions_with_765_85':str(sum(contributions)),
    'contributions_with_765_35':str(sum(alternative)),
    'displayed_contribution_subtotal':'6262.09',
    'difference_with_first_reading':str(D('6262.09')-sum(contributions)),
    'grand_from_displayed_subtotals':str(D('5616')+D('6262.09')),
    'grand_from_line_items':str(sum(dea)+sum(contributions)),
    'operating_budget':str(D('920.23')+D('1500.00')),
    'interpretation':'Transcription arithmetic alarm; ink and original account not checked; no reading changed.'
}
assert sum(dea)==D('5616.00')
assert sum(contributions)==D('5762.09')
assert D('6262.09')-sum(contributions)==D('500.00')
print(json.dumps(result,indent=2))
