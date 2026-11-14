# System-level rendering decisions

These decisions affect presentation or the implementation of recorded source variants; they do not amend the checked source readings.

- Reading-form scan and manuscript-page labels use queued margin paragraphs, allowing consecutive labels and short marginal notes to stack rather than collide. The 134-5 proof at sites 64 and 72 was rendered and inspected after this change; observations are in `VISUAL_QA.json`.
- A marginal note whose entire content is cancelled has an empty corrected reading. Its complete diplomatic content appears in the apparatus, without an empty marginal-note label in the corrected running text.
- A doubt or presentation wrapper whose entire content is cancelled is incorporated into the deletion variant. The original uncertainty remains visible in the diplomatic reader and apparatus; an empty uncertainty marker is not printed in the reading text. An uncertainty containing a live alternative is retained. This addresses actual cases including 134-2/2, /6, /25, 134-3/11, /39, /47, 134-5/4, and 134-7/16.

Apparatus entries use a ragged right edge. This allows the short label, source reading, corrected reading, and editorial reason to break naturally without forcing justified compound fragments beyond the measure. No font scaling or overflow suppression is applied.
