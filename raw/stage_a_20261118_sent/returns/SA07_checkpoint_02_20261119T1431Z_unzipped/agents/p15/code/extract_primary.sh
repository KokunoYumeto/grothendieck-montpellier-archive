#!/bin/sh
set -eu
pdftotext -layout agents/p15/evidence/EGA_IV3.pdf agents/p15/evidence/EGA_IV3.txt
pdftotext -layout agents/p15/evidence/Li_BasicRep.pdf agents/p15/evidence/Li_BasicRep.txt
pdftotext -layout agents/p15/evidence/Milne_LAG.pdf agents/p15/evidence/Milne_LAG.txt
rg -n '8\.8\.2|8\.10\.5' agents/p15/evidence/EGA_IV3.txt
rg -n '1\.20|1\.21|1\.40' agents/p15/evidence/Li_BasicRep.txt
