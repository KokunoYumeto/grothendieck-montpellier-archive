# Coverage audit of the sent transcription packages (17 Nov 2026 00:29 UTC)

Built by `tools_20261113/coverage_audit.py` (script, no model): the scans each package's MANIFEST.json asked for, against the page files of its final return and of its checkpoints in `returns/`.

Packages sent: 77; scans asked for: 3221; scans in a final return: 2923. Packages without a final return: 7. Finals missing scans: 0.

## Packages without a final return

| Package | Scans asked | Checkpoints | Scans in checkpoints | Not in any return (to re-queue if the run is over) |
|---|---:|---:|---:|---|
| P021_230_MPL_57_226-270 | 43 | 0 | 0 | 57: 226-231, 233-246, 248-270 |
| P030_156_MPL_93_221-236+161-5 | 43 | 0 | 0 | 161-5: 3-29; 93: 221-236 |
| P032_220_MPL_122 | 32 | 0 | 0 | 122: 3-18, 20-35 |
| P033_91_MPL_15_139-194 | 45 | 1 | 31 | 15: 179-180, 182-187, 189-194 |
| P037_194_MPL_46_002-048 | 42 | 0 | 0 | 46: 2-23, 27-34, 36, 38-48 |
| P045_185_MPL_84_097-145 | 48 | 1 | 43 | 84: 141-145 |
| P046_88_MPL_12_150-168+15_002-033 | 45 | 1 | 45 | - |

## Finals missing scans

| Package | Scans asked | In the final | Missing | Recoverable from a checkpoint | In no return |
|---|---:|---:|---|---|---|

## Near-empty page files in finals (under 40 characters outside comments)

- 36_MPL_144_122-167: 144: 152
- P014_95_MPL_136_095-141: 136: 110
- P016_97_MPL_136_189-234: 136: 224
- P026_94_MPL_136_047-094: 136: 93
- P036_231_MPL_57_271-315: 57: 282
- P044_60_MPL_22+23_002-016: 22: 19; 23: 8

## Complete

04_MPL_147_138-190, 05_MPL_149_001-090, 06_MPL_149_091-136, 07_MPL_146_001-099, 08_MPL_146_100-134, 09_MPL_142_001-093, 10_MPL_142_094-122, 11_MPL_16+47+54+44, 30_MPL_5+6_001-037, 31_MPL_6_038-067+7_001-060, 32_MPL_7_061-072+8_001-078, 32b_MPL_7_061-072+8_001-078_continue, 33_MPL_8_079-081+9+4+100, 34_MPL_144_001-061, 35_MPL_144_062-121, 36_MPL_144_122-167, 37_MPL_144_168-184+148_001-028, 38_MPL_148_029-072, 39_MPL_143+141, 40_MPL_145, 41_MPL_150_001-043, 42_MPL_150_044-084, 43_MPL_150_085-099+151_001-031, 44_MPL_151_032-075, 45_MPL_152+120, 46_MPL_121_001-048, 47_MPL_121_049-073+153+155, 48_MPL_156-1+156-2, MPL_147_003-047, MPL_147_048-137, MPL_1_002-050, P001_174_MPL_154_127-176, P002_173_MPL_154_077-126, P003_83_MPL_14_087-132, P004_81_MPL_14_002-044, P005_145_MPL_72_035-081, P006_202_MPL_91_099-143, P007_66_MPL_134-8_043-087, P008_50_MPL_93_002-046, P009_211_MPL_33_098-146, P010_210_MPL_33_050-097, P011_186_MPL_84_146-193, P012_92_MPL_15_195-228+18_002-017, P013_209_MPL_33_002-049, P014_95_MPL_136_095-141, P015_90_MPL_15_087-138, P016_97_MPL_136_189-234, P017_138_MPL_11_002-042, P018_73_MPL_105, P019_98_MPL_136_235-281, P020_93_MPL_18_018-062, P022_141_MPL_60_036-070, P023_212_MPL_33_147-181+34_002-017, P024_96_MPL_136_142-188, P025_140_MPL_60_002-035, P026_94_MPL_136_047-094, P027_74_MPL_106+107, P028_193_MPL_45_033-080, P029_139_MPL_11_043-058+56, P031_223_MPL_131, P034_218_MPL_36_053-085+39, P035_232_MPL_62_002-050, P036_231_MPL_57_271-315, P038_246_MPL_2, P039_199_MPL_90+91_002-018, P040_217_MPL_36_002-052, P041_80_MPL_133, P042_206_MPL_31_002-051, P043_190_MPL_43_094-142, P044_60_MPL_22+23_002-016

## Decisions (the user, 17 Nov ~00:4x-01:0x UTC) and the content check

- **No return at all: re-send whole.** P021, P030, P032 and P037 are back in packages/ with refreshed results blocks.
- **Partial returns: re-send only what is not done.** P033 (MPL_15_139-194) stalled after checkpoint 01. Its 14
  missing scans (cote 15: 170-171, 179-194) need a small package, still to build in the current pipeline (PLAN.json
  plus results block). Its 31 done scans are in checkpoint 01 and are not re-sent.
- **Still running:** P045 (5 scans not yet in a checkpoint) and P046 (checkpoint 01 already holds every scan). Audit
  them again when their finals come, or when they stop.
- **Content of the finals:** every row of every final's inventory says transcribed = yes (63,385 rows). No page file
  carries a placeholder ("not transcribed", "timed out", TODO and the like). The 111 page files under 600 bytes are real
  short pages: margin numbers, headings, printers' colophons. So no final is partial inside.
- Not covered: the continuation package 32b_MPL_7_061-072+8_001-078_continue (no MANIFEST of its own) and the Codex-web
  units, whose coverage is in CODEX_COVERED_SCANS.tsv.
