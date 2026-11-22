#!/usr/bin/env python3
"""Fetch primary sources actually opened in the public literature search."""
from ROOT_fetch_ring_sources import main

main([
    ('ROOT_Olivier1968.pdf', 'https://www.numdam.org/item/SAC_1967-1968__2__A6_0.pdf'),
    ('ROOT_Olivier1978.pdf', 'https://www.boletin.math.org.mx/pdf/2/23/BSMM(2).23.68-74.pdf'),
    ('ROOT_Ferrand2003.pdf', 'https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf'),
], 'ROOT_constructible_sources_fetch.json',
   'Primary-source construction and explicit published identification of EGA I (1971), 7.2.14, with the universal absolutely flat scheme. No claim that the historical word morcelé has thereby been identified.')
