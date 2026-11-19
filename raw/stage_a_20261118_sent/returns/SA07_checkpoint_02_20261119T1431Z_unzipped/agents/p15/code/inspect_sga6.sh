#!/usr/bin/env bash
set -euo pipefail
cd /workspace/scratch/9c0c54a66f6c
pdfinfo agents/p15/evidence/SGA6_original.pdf
pdftotext -f 1 -l 20 agents/p15/evidence/SGA6_original.pdf agents/p15/evidence/SGA6_first20.txt
pdftoppm -f 6 -l 9 -scale-to 1800 -png agents/p15/evidence/SGA6_original.pdf agents/p15/evidence/pdf_pages/SGA6
