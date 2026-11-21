# Resume this sustained research run

Run: GCT_KRON_20261120. Model: GPT-6 Astra Pro; effort not exposed.
Root: /workspace/scratch/e3994f8d0062/GCT_KRON_work.
Read the supplied PROMPT.md and current LEDGER, QUESTIONS, CHECK_EVENTS and TIMED_REVIEWS before continuing. The archive was unpacked exactly once into ../sources.

## Timing and delivery rules

Start2026-11-20T23:00:17Z. Checkpoints every45minutes and no others, complete fresh ZIPs including all work and supplied sources, excluding old ZIPs. Checkpoints01–06 have been durably saved;07 is due2026-11-21T04:15:17Z. Do not overwrite, rename or delete old checkpoints. Only deliver checkpoint ZIPs and final GCT_KRON_final.zip, never individual papers/files.

Actual reviews01 at02:00:17.030081,02 at03:01:32.313313,03 at04:00:22.659890UTC all recorded movement; no-movement streak0. Nextreview04 due05:00:17UTC, then hourly. Two consecutive ACTUAL reviews without movement trigger finalization. Never invent a review or count packaging/constant changes as movement. Review03 explicitly says the general large-padding gate did not move during its interval.

## Current strongest actual results

A034: for every unpadded n=m>=3, R=n²,D=R+1,lambda=(n(n−1)²+1,3,2^(R−2)), every s>=1 satisfies q_(s lambda)>=p_n(s)>K=sk=g=h_n(s), where p counts parts1..n and h counts parts2..n. Both actual sides are positive for EVERYs>=2. Permanent HWray contains polynomial C[Z,U2,...,Un], degrees1..n; the ENTIRE determinant HWray is C[U2,...,Un], degrees2..n. The latter is normal with positive monomial basis but genuine relative-support hole1 in generated latticeZ. Root and three agents full-proof readPASS.

O030 gives the three-parameter extension Lambda(u,a,k), exactK=h_n(k), permanent lower sum_j h_n(k−j). A033 improves q_(2lambda)>=3 whereK1 for alln. F028 gives stronger cubic count C_s, with exact checked14minor and full binary permanent/Hessian-pair dominance. F025 exact K5<q=a6<sk10<g11 at n=m3,d12,lambda(19,7,2^5); K5 is explicitly cited LMR publishedp476 input. A031 finite m3–6 endpoint full q=a, lambda3<=2,length<=2m+2; no arbitrary-size conclusion.

A035 K=a1 on every basic proper partial Hessian bracket2<=r<n². The entire binary F/partial-Hessian coefficient algebra injects on Det forr<=2n; only its own HWcopies are compared. A036 C[Z_r,U2,...,Un] injects on Det at EVERYproper3<=r<n², so the whole constructed positive algebra cannot give padded obstructions at any stretch. A037 proves the pair algebra is proper: ternary cubic degree8,type(14,6,4) has pair3<ambient=Det4, with explicit missing Aronhold product S(F)F0²I2. All complete root readsPASS.

A038 uses known Beauville Cor6.4pp52–53 and a proved zero-entry3x3 det=per reduction: all cubic four-row types have q3=K3=a in every degree. Every internally padded per3 four-row type has q^3<=K_n for alln>=3, all degrees, no later-row bound. It controls all copies outside the Hessian pair algebra too. Root complete proof/source readingPASS; agent independent review pending.

General large-padding actual comparison remains open. BIPcandidates require m>=190,rows>=52, n<P_d(dm),n<P_d(lambda2),lambda_(2j)>=28−j,q>=2,padding constraints and failure of all support/jet gates. M019 requires lambda4>=27 ORlambda2>=239063403 and strictly improves all one-sided M018 choices viaO025. M017,A025 additional gates retained in QUESTIONS. These reductions do not settle PvsNP.

## Active endpoint work QA033

Exact conditional residue reduction QA033-RJ in agents/jet_review/structured_permanent_residue_reduction.tex: base xJ+y diag(a_i), factorial transform, first-jet kernel K dimensionm(m−1), square quadratic map Hom(V,K)->H_m tensorSym²V*, dimV2m−1. Rawtensor onlypairs/triangles. Finite m3..6 full rank, not uniform proof.

O031 proves endpoint-gradient normal form and uniform pure-Q² isomorphism. QA033-CB proves detJ(charge)=charge^M detJ(1),M=C(m,2), without rank hypotheses. Reduced square [[A,0],[C,F]] invertible iff A surjective,F injective, inducedC:kerA->cokerF isomorphism. M-dimensional last gate only after both separate ranks proved.

QA033-SYM NOW PROVES F GENERICALLY INJECTIVE ALLm. Ordered a_i=epsilon^(−i) and edge scaling yields interval gradient g_ab,i=(2a−i)p_a+i p_b+2sum_(j<a)p_j for a<=i<b. Last-outputsyzygies Tskew; p_m² forcesT1=0; p_m equations give W=T L_k withdiag2a−k,lower2. Descending-column recurrence −[j+h(l−1−j)]T_jl+(h−1)sum_(a>j)T_al=0 killsT, induction completes. Root wholeproofreadPASS; independent archive review requested.

Mixed A and final charge remain OPEN. Ordered full charged limit has a universal last-output cokernel, so only separate rank proofs can use that limit. saturation_obstructions has a raw dual induction; do NOT assume the proposed alternating-Omega quotient because v_a modulof_k are dependent for evenk>=4. Rigorously known raw A_a(f_k)=0 and A_b(v_a)=−A_a(v_b), plus old symmetric-edge equations. verify_new_jets independently working on same system.

## Current agents

archive_finish: A038, independent QA033-SYM read, then useful remaining source/family work.
verify_new_jets: QA033-CB and QA033-SYM; mixed A dual elimination and charge.
saturation_obstructions: O031, mixed A induction; coordinate with verifier.

## Build and save

build_package.py expands every input into one self-contained GCT_KRON.tex, consolidates QUESTIONS/CHECK_EVENTS. All newerA035–38,RJ,O031,CB,SYM integrated. Compile twice with:
env TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}' xetex -fmt=/workspace/scratch/e3994f8d0062/GCT_KRON_work/render/xelatex.fmt -progname=xelatex -interaction=nonstopmode -halt-on-error -output-directory=render GCT_KRON.tex
Current paper242pages, compiled twice without overfull/undefined/duplicate-label warnings; selected new-page contact sheets visually checked. Final full production review remains.

create_checkpoint.py NUMBER hasdueguard,exclusiveZIP,CRC/hashmanifest. It rebuildsTeX, so ensurePDFmatchesstable integratedsource. External publications remain outsidework; exactURLs/locators/hashes recorded and manifestsincluded, not copied. Full supplied corpus isincluded.

Library fastpath: discover mcp__codex_apps__library_create_library_file, create absoluteZIPpath library_artifact_type other, then withinSAMEfunctions.exec applyreturnedxattrs with python3 ../.library_helpers/library_file_transfer.py apply-xattrs PATH ID and JSONstdin. Reuse alreadyfetchedhelperthisrequest. RecordreceiptID onlyafterverifiedsuccess. Deliver onlyZIPsandboxlink. Latestc06SHA2870eefbea36271ddc339286eeeb5240bea16181c0a878a110774ef7a761dbb6,10446744bytes,320files; libfile_fde3_f-7cdcd4d08af48191aee8d6460771f25d_3de54532f60c8191850458563edee173.
