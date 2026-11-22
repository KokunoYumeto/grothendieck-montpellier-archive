#!/usr/bin/env python3
"""Download the original Nagata example and its essential correction."""
from ROOT_fetch_ring_sources import main

main([
    ("ROOT_Nagata1952.pdf", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26B873ADB5B5E081DD6735B161E34A0E/S0027763000022959a.pdf/on_krulls_conjecture_concerning_valuation_rings.pdf"),
    ("ROOT_Nagata1955_correction.pdf", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C3A684A6F79F93EFBE72D607DE61F4AB/S0027763000023436a.pdf/corrections_to_my_paper_on_krulls_conjecture_concerning_valuation_rings.pdf"),
    ("ROOT_Ribenboim1955.pdf", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7A60D6EAE856E6A2F806FF895E50165F/S002776300002331Xa.pdf/sur-une-conjecture-de-krull-en-theorie-des-valuations.pdf"),
], "ROOT_Nagata_sources_fetch.json", "Public primary-source verification of the explicit one-dimensional completely integrally closed local nonvaluation ring; the1955 correction is essential")
