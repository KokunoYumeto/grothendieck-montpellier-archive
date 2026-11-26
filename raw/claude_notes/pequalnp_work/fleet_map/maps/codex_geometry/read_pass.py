"""Display named primary passages with line locators; retain hashes and measured sizes only."""
import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).parent
DOC = Path("<local>/Documents")
RET = DOC / "grothendieck_archive_transcription_20261110/research_returns"
EDGE = DOC / "Papors/Chatnotes/CHat translates and clean/Noether Multilingual"
def ret(name):
    return next(RET.glob(name))

LOCATORS = {
    "tubes": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/01_tubes/main.tex",
    "periods": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/03_periods/main.tex",
    "positions": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/05_relative_positions/main.tex",
    "powers": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/06_divided_powers/main.tex",
    "laws": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/06_divided_powers/positive_polynomial_laws.tex",
    "posets": ret("POLISH_TOPOLOGY_PERIODS_checkpoint_13*")/"papers/07_posets/main.tex",
    "hodgeA": ret("HODGE_FINISH_final*")/"workbench/work/UNFILED-A/v1/paper/main.tex",
    "hodgeB": ret("HODGE_FINISH_final*")/"workbench/work/UNFILED-B/v1/paper/main.tex",
    "hodgeDetector": ret("HODGE_FINISH_final*")/"workbench/checks/small_detectors_blind/independent_detector_proof.tex",
    "hodgeTarget": ret("HODGE_FINISH_final*")/"continuation/data/gaussian_target_section.tex",
    "thetaPair": ret("NIGHT_AFTER_ALPOGE_checkpoint_11*")/"workbench/zeta-and-l-functions-workbench/papers/theta-chain/finite-pair-example.tex",
    "thetaShift": ret("NIGHT_AFTER_ALPOGE_checkpoint_11*")/"workbench/zeta-and-l-functions-workbench/papers/theta-chain/finite-translations.tex",
    "s6Seed": DOC/"s6_workbench_repo_20261112/pro_returns/S6_01_INVARIANTS/return/fragments/part_A.tex",
    "s6Gauge": (EDGE/"S6_SERIES_PUBLISH_checkpoint_52.zip","agents/continuation4_conductor/S6_SERIES_PUBLISH_c4_conductor_stage20_finite_gauge.tex"),
    "s6Paper": (EDGE/"S6_SERIES_PUBLISH_checkpoint_52.zip","S6_SERIES_PUBLISH_II.tex"),
    "fieldCut": Path.cwd()/"outputs/P_VS_NP/clause_scopes_and_degree_digits.tex",
    "claudeIntake": DOC/"agent_notes/20261123T1106Z_Intake_POLISH_TOPOLOGY_PERIODS_cp12_NOTES.md",
    "claudeMaps": DOC/"agent_notes/maps_ag_hodge_ant_NOTES.md",
}

def source(key):
    p = LOCATORS[key]
    if isinstance(p,tuple):
        with ZipFile(p[0]) as z:
            data = z.read(p[1])
    else:
        data = p.read_bytes()
    return data.decode("utf-8-sig").splitlines()


if __name__ == "__main__":
    key, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    rows = source(key)
    end = min(end, len(rows))
    content = "\n".join(rows[start-1:end])
    print(f"== {key} {start}-{end} [{len(content)} Unicode characters] ==")
    print(content)
