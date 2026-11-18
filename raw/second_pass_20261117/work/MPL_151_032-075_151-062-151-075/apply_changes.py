"""Copy the first-pass pages of block MPL_151_032-075_151-062-151-075 to the output folder and apply the
second-pass corrections. Every old string must occur exactly once in its page, or the script stops."""
import os
import sys

ROOT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = os.path.join(ROOT, "returns/MPL_151_032-075_unzipped/pages")
DST = os.path.join(ROOT, "second_pass/out/MPL_151_032-075")
NAME = "MPL_151_032-075_151_scan{}.tex"

CHANGES = {
    "062": [
        (r"\unsure{X_{\Delta_0}^*|V_{\Delta_0}^*}\arrow[r,dashed]", r"\deleted{V}X_{\Delta_0}^*\arrow[r,dashed]"),
        (r"& V_{ij}\arrow[d,dashed] & X_i^*", r"& V_{i,j}\arrow[d,dashed] & X_i^*"),
        (r"X_j^*\arrow[r,dashed] & X &", r"X_j^*\arrow[r,dashed] & X & {.}"),
        (r"\deleted{\unsure{On a}} Finalement", r"\deleted{\unsure{Notons|On a}} Finalement"),
    ],
    "063": [
        (r"$\unsure{V_{j,k}^j|V_{i,k}^j}$", r"$V_{i,k}^j$"),
        (r"\unsure{seuls|seules}", r"\unsure{seules|seuls}"),
        (r"\inserted{(\unsure{alors} $X_i\subset X_j", r"\inserted{(\deleted{\unsure{Cela|alors}} $X_i\subset X_j"),
        (r"\inserted{\unsure{resp.|pour} $\overline{X_{i'}^*}$ et $X_{i'}$}, sont",
         r"\unsure{resp.|pour} $\overline{X_{i'}^*}$ et $X_{i'}$, sont"),
    ],
    "064": [
        (r"\deleted{\unsure{Dans le}} le cas $i=i'$", r"\unsure{Dans \deleted{le}|\deleted{Dans le}} le cas $i=i'$"),
        (r"Mais le cas $i<\unsure{i'|j'}$ est-il", r"Mais le cas $i<\deleted{\unsure{j}}i'$ est-il"),
        (r"morphisme \inserted{d'un} $V_{ij}$", r"morphisme d'un $V_{ij}$"),
    ],
    "065": [
        (r"\inserted{le card.} $\operatorname{card}I+2\nu$", r"\inserted{\unsure{le|en} cardinal} $\operatorname{card}I+2\nu$"),
        (r"``élémentaires'' i.e. tels que $j$ est successeur de $i$ et le nb",
         r"``élémentaires'' \inserted{i.e. tels que $j$ est successeur de $i$} et le nb"),
    ],
    "066": [
        (r"\underset{\unsure{\updownarrow}}{V_{0,1}^*}",
         r"\underset{\deleted{\unsure{\downarrow}}}{V_{0,1}^{\unsure{*|\deleted{*}}}}"),
        (r"& & & & & & & & & X_n^*", r"& & & & & & & & & X_n^*."),
        (r"\unsure{0|\bullet} \arrow[ru] \arrow[rd]", r"\bullet \arrow[ru] \arrow[rd]"),
        (r"""\deleted{X_0^*} & V_{0,b}^* \arrow[r,phantom,"{\unsure{\to|-}}" description] \arrow[d]""",
         r"\deleted{X_b^*} & V_{0,b}^* \arrow[r] \arrow[d]"),
        (r"& X_b^* & & & & X_a^*", r"& X_b^* & & & & X_a^*."),
        (r"\unsure{préciser|vérifier}", r"préciser"),
    ],
    "067": [
        (r"\text{Si }i,j\in I\text{ et }i\leq j,\text{ alors }",
         r"\text{Si }i,j\in I\,\deleted{\unsure{\varnothing}},\ i\leq j,\text{ alors }"),
        (r"\unsure{simplifiant|simplifier}", r"\unsure{simplifier|simplifiant}"),
    ],
    "068": [
        (r"V_{\unsure{n+n-1|n,n-1}}^*", r"V_{n,n-1}^*"),
    ],
    "069": [
        (r"\unsure{canoniques|coconiques}", r"canoniques"),
        (r"\deleted{\unsure{des voisinages}}", r"\deleted{\unsure{des voisinages $V_{ij}$|démonstration}}"),
    ],
    "070": [
        (r"\unsure{2|4}. \uline{Topos", r"\deleted{2}4. \uline{Topos"),
        (r"\unsure{situation}", r"situation"),
        (r"(1)\quad\left\{\begin{aligned}", r"\unsure{(1)|(11)}\quad\left\{\begin{aligned}"),
        (r"satisfait les $\unsure{=^{\mathrm s}|\overline{\mathrm m}^{\mathrm s}}$ conditions",
         r"satisfait les \illegible{1} $\unsure{=^{\mathrm s}|\overline{\mathrm m}^{\mathrm s}}$ conditions"),
        (r"\unsure{simple|simpl.}", r"simpl."),
    ],
    "071": [],
    "072": [
        (r"\unsure{panneau|piège}", r"panneau"),
        (r"(\unsure{10|9})\quad X_{I'\cup I''}", r"(10)\quad X_{I'\cup I''}"),
        (r"(\unsure{9|11})\quad X_{I'\cap I''}", r"(11)\quad X_{I'\cap I''}"),
        (r"grâce à (1 d).", r"grâce à \unsure{(11 d)|(1) d)}."),
    ],
    "073": [
        (r"définie par les $X_i$ où $i\in I'$", r"définie par les $X_i$ \unsure{avec|où} $i\in I'$"),
    ],
    "074": [
        (r"$I'_0\subset\unsure{I'|I_0}$", r"$I'_0\subset\unsure{I_0|I'}$"),
    ],
    "075": [],
}


def main():
    os.makedirs(DST, exist_ok=True)
    total = 0
    for scan, changes in CHANGES.items():
        with open(os.path.join(SRC, NAME.format(scan)), encoding="utf-8", newline="") as f:
            text = f.read()
        for old, new in changes:
            n = text.count(old)
            if n != 1:
                sys.exit(f"scan {scan}: {n} occurrences of {old!r}")
            text = text.replace(old, new)
            total += 1
        with open(os.path.join(DST, NAME.format(scan)), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(scan, len(changes), "replacements")
    print("total replacements:", total)


if __name__ == "__main__":
    main()
