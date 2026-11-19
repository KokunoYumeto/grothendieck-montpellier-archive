"""Presentation-only spacing; no IDs, locators, quoted words or verdicts change."""
import re

def polish(value):
    value=value.replace('SGA1 XI§4.1','SGA1 XI §4, after Proposition 4.3')
    value=value.replace('SGA1XI§4.1','SGA1 XI §4, after Proposition 4.3')
    value=value.replace('supplement§','supplement §').replace('Supplement§','Supplement §')
    value=re.sub(r'\b(the|in|on|for|by|with|from|of|at|and|or|its|is|as|to|an|a|into|over|between|under|ordinary|standard|current|precise|exact|earlier|modern|classical|primary|opened|published|relative|finite|full|local|all|both|each)(?=[A-ZΑ-Ωα-ω])',r'\1 ',value)
    value=re.sub(r'(?<=[a-z])(?=[0-9])',' ',value)
    value=re.sub(r'(?<=[0-9])(?=[A-Za-z])',' ',value)
    for old,new in {
      'theclassical':'the classical','thecontracted':'the contracted',
      'theproduct':'the product','thefour-element':'the four-element',
      'thecorrectedstabilizer':'the corrected stabilizer','rotationalstabilizer':'rotational stabilizer',
      'thefieldnormalizer':'the field normalizer','thefield':'the field',
      'relative correctedstatement':'relative corrected statement','fullyproved':'fully proved',
      'Structuredstabilizer':'Structured stabilizer','finiteétale':'finite étale',
      'theuniversalbarestabilizer':'the universal bare stabilizer','geometricpoints':'geometric points',
      'regularoppositions':'regular oppositions','inthatfiber':'in that fiber',
      'overgeneralbases':'over general bases','theargument':'the argument',
      'finitepermutation':'finite permutation','andexplicit':'and explicit','onlypointcounts':'only point counts',
      'thefixed-pointquadratic':'the fixed-point quadratic','thepoints':'the points','thetranscription':'the transcription',
      'remainsunresolved':'remains unresolved','correctedsubstitution':'corrected substitution',
      'localdegree':'local degree','forquotients':'for quotients','oftorus':'of torus',
      'thecomplex':'the complex','thealgebraic':'the algebraic','usesétaleness':'uses étaleness',
      'ramificationindex':'ramification index','fordyadic':'for dyadic',
      'Classicalmultiplicationquotient':'Classical multiplication quotient',
      'exactdivisorformulachecked':'exact divisor formula checked',
      'onthe':'on the','theopened':'the opened','localcyclic':'local cyclic',
      'andquadratic':'and quadratic','bythemselves':'by themselves','allmorphisms':'all morphisms',
      'descentobstructions':'descent obstructions','of theauthor':'of the author',
      'generalstatement':'general statement','falseclaim':'false claim',
      'pointedtamecovers':'pointed tame covers','localinertia':'local inertia',
      'inducedpower':'induced power','oninertia':'on inertia','andtangentroots':'and tangent roots',
      'scalarquotient':'scalar quotient','thefinite':'the finite',
      'groupoidof':'groupoid of','withsquare':'with square','Printedclassicaldihedral':'Printed classical dihedral',
      'correctionrecorded':'correction recorded','Classicaldescentpublished':'Classical descent published'
    }.items(): value=value.replace(old,new)
    return value
