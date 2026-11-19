#!/usr/bin/env bash
set -euo pipefail
cd /workspace/scratch/9c0c54a66f6c
mkdir -p agents/p15/evidence/pdf_pages
pdftoppm -f 1 -l 2 -scale-to 1800 -png agents/p15/evidence/Grothendieck1969Hodge.pdf agents/p15/evidence/pdf_pages/Hodge
pdftoppm -f 24 -l 25 -scale-to 1800 -png agents/p15/evidence/BorelHarishChandra1962.pdf agents/p15/evidence/pdf_pages/BHC
pdftoppm -f 26 -l 28 -scale-to 1800 -png agents/p15/evidence/BorelHarishChandra1962.pdf agents/p15/evidence/pdf_pages/BHC
pdftoppm -f 3 -l 5 -scale-to 1800 -png agents/p15/evidence/Grothendieck1969Hodge.pdf agents/p15/evidence/pdf_pages/Hodge
