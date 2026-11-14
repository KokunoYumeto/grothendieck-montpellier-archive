# Release audit

Status: **BLOCKED**.

This audit checks source reconstruction, translation tokens, reader coverage, actual PDF reports, and separately recorded visual reviews. It does not infer that a page has been read or viewed.

| Gate | Result |
|---|---|
| checked-page coverage | PASS |
| page-review coverage | PASS |
| page-review record consistency | PASS |
| unique decision IDs | PASS |
| NOTES concern documentary coverage | BLOCKED |
| checked-source reconstruction | PASS |
| English translation coverage and fidelity | BLOCKED |
| twelve standalone PDFs | BLOCKED |
| guide manifest | PASS |
| privacy screen | PASS |

## PDF status

### EGA_V_FR_diplomatique

required visual inspections pending; geometry flags require explicit visual disposition

Pending visual pages: [1, 6, 11, 15, 20, 25, 26, 30, 34, 35, 39, 43, 44, 45, 49, 52, 53, 57, 58, 63, 68, 73, 77, 78, 82, 87, 92, 96, 101, 106, 111, 115, 120, 125, 126, 130, 135, 139, 144, 149, 151, 154, 158, 163, 168, 173, 177, 180, 182, 187].

### EGA_V_FR_corrige_apparat

required visual inspections pending

Pending visual pages: [1, 12, 22, 23, 34, 45, 55, 66, 77, 88, 89, 91, 92, 99, 110, 121, 132, 143, 154, 164, 175, 176, 177, 178, 186, 197, 198, 199, 200, 201, 202, 203, 208, 214, 215, 216, 219, 226, 227, 228, 230, 239, 240, 241, 252, 263, 273, 284, 288, 289, 290, 295, 306, 317, 328, 336, 337, 338, 339, 350, 361, 372, 382, 393, 394, 404, 415, 426].

### EGA_V_FR_texte_de_lecture

required visual inspections pending

Pending visual pages: [89, 90, 91, 92, 95, 96, 98, 101, 103, 106, 111, 115, 120, 124, 125, 130, 135, 139, 144, 147, 149, 154, 158, 163, 168, 173, 177, 182, 187].

### EGA_V_FR_master_annotated

required visual inspections pending

Pending visual pages: [1, 12, 22, 23, 34, 45, 55, 66, 77, 88, 89, 91, 92, 99, 110, 121, 132, 143, 154, 164, 175, 176, 177, 178, 186, 197, 198, 199, 200, 201, 202, 203, 208, 214, 215, 216, 219, 226, 227, 228, 230, 239, 240, 241, 252, 263, 273, 284, 288, 289, 290, 295, 306, 317, 328, 336, 337, 338, 339, 350, 361, 372, 382, 393, 394, 404, 415, 426].

### EGA_V_EN_corrected_translator_notes

reader changed since compilation; compiled PDF hash is absent or differs; source inputs or rendering configuration are stale; individual archive link targets are unverified; marginal notes have no verified same-page anchors; working or obsolete unchecked label remains; printed page coverage or order differs; common annotated page data differs from its master; PDF source-page destinations differ; distinct archive-page URLs differ; required visual inspections pending; geometry flags require explicit visual disposition

Pending visual pages: [1, 8, 14, 21, 28, 35, 41, 45, 48, 55, 61, 68, 75, 78, 79, 80, 82, 88, 95, 100, 101, 102, 103, 104, 105, 108, 115, 117, 118, 119, 122, 129, 130, 131, 135, 142, 143, 149, 156, 162, 169, 176, 182, 188, 189, 190, 196, 203, 209, 216, 223, 229, 236, 237, 238, 243, 250, 256, 263].

### EGA_V_EN_reading

source inputs or rendering configuration are stale; working or obsolete unchecked label remains; printed page coverage or order differs; common annotated page data differs from its master; PDF source-page destinations differ; distinct archive-page URLs differ; required visual inspections pending

Pending visual pages: [1, 5, 10, 13, 14, 19, 23, 28, 32, 37, 41, 46, 50, 55, 59, 63, 68, 69, 72, 77, 78, 79, 81, 83, 86, 90, 91, 95, 99, 104, 108, 112, 113, 117, 121, 126, 130, 135, 139, 144, 148, 153, 157, 160, 162, 166, 171, 175].

### EGA_V_EN_master_annotated

reader changed since compilation; compiled PDF hash is absent or differs; source inputs or rendering configuration are stale; individual archive link targets are unverified; marginal notes have no verified same-page anchors; working or obsolete unchecked label remains; printed page coverage or order differs; common annotated page data differs from its master; PDF source-page destinations differ; distinct archive-page URLs differ; required visual inspections pending; geometry flags require explicit visual disposition

Pending visual pages: [1, 8, 14, 21, 28, 35, 41, 45, 48, 55, 61, 68, 75, 78, 79, 80, 82, 88, 95, 100, 101, 102, 103, 104, 105, 108, 115, 117, 118, 119, 122, 129, 130, 131, 135, 142, 143, 149, 156, 162, 169, 176, 182, 188, 189, 190, 196, 203, 209, 216, 223, 229, 236, 237, 238, 243, 250, 256, 263].

### EGA_V24_EN_diplomatic

required visual inspections pending; geometry flags require explicit visual disposition

Pending visual pages: [1, 3, 5, 7, 9, 11, 12, 13, 15, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 37, 39, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 62, 64, 66, 68, 69, 70, 71, 72, 74, 76, 78, 80].

### EGA_V24_EN_corrected_apparatus

required visual inspections pending

Pending visual pages: [1, 3, 5, 7, 9, 11, 12, 13, 15, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 37, 39, 40, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 62, 64, 66, 68, 69, 70, 71, 72, 74, 76, 78].

### EGA_V24_EN_reading

required visual inspections pending

Pending visual pages: [1, 3, 5, 7, 9, 11, 12, 13, 15, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 37, 39, 40, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 62, 64, 66, 68, 69, 70, 71, 72, 74, 76, 78].

### EGA_V24_EN_master_annotated

required visual inspections pending

Pending visual pages: [1, 3, 5, 7, 9, 11, 12, 13, 15, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 37, 39, 40, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 62, 64, 66, 68, 69, 70, 71, 72, 74, 76, 78].

### EGA_V_GUIDE

required visual inspections pending

Pending visual pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25].
