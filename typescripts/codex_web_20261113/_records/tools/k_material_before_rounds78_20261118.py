"""Material sentences of batch K (17 Nov 2026, Claude Opus 5.5 at effort high). They say only what the survey of
HANDWRITING_INVENTORY_20261114.tsv saw: about five sample scans per cote, graded on contact sheets on 14 Nov 2026, plus
the specific scans noted there. The archive's own title of the file is in the prompt already ({TITLE}). Every sentence
says that it rests on sample pages and that other kinds of page are transcribed as they are."""

GENERIC = {
    "C": "his handwritten working notes in his dense working hand, with formulas, insertions, margin notes and struck "
         "passages",
    "B-C": "his handwritten notes in his spaced hand, with formulas",
    "C-D": "his handwritten notes in a dense hand, partly faint or in pencil, with formulas and drawings",
}
SPECIAL = {
    "35": ("a typed list with his handwritten additions and his handwritten lists, in French (lists of exposés and "
           "names), short lines", {}),
    "48": ("his handwritten lists and plans, in French, with short lines and insertions", {}),
    "26": ("his handwritten plans, notations and lists, in French, with short lines, some struck through", {
        4: "scan 4 is typed", 6: "scan 6 is typed"}),
    "37": ("letters from correspondents and lists about the re-editions, in English and French: typed pages and "
           "letters in clear hands of others, besides his own handwriting", {}),
    "97": ("typed pages, some with handwritten corrections, insertions and formulas", {}),
    "109": ("typed pages and lists, some with handwritten corrections", {}),
    "111": ("copies of a typed text (the \"Tapis de Quillen\") with his handwritten annotations", {}),
    "63": ("handwritten pages in his hand and in others' hands, dense, with formulas and many crossings-out", {}),
}
NOTES = {  # specific scans the survey saw, said only when the scan is in the folder
    "34": {210: "scan 210 is typed"},
    "84": {145: "scan 145 is typed", 193: "scan 193 is typed"},
    "62": {26: "scan 26 is typed in purple"},
    "21": {9: "scan 9 is typed"},
    "55": {5: "scan 5 is an annotated typed page, upside down", 9: "scan 9 is an annotated typed page, upside down",
           13: "scan 13 is an annotated typed page, upside down"},
    "75": {33: "scan 33 is typed"},
    "53": {18: "a letter in English of 1973 on yellow lined paper is about scan 18"},
}
GRADE = {"34": "C", "46": "C", "43": "C", "45": "C", "70": "C", "158": "C", "123": "C", "119": "C", "80": "C",
         "74": "C", "23": "C", "57": "C", "118": "C", "102": "C", "127": "C", "49": "C", "50": "C", "85": "C",
         "86": "C", "31": "C", "101": "C", "79": "C", "77": "C", "84": "C", "62": "C", "27": "C", "28": "C",
         "93": "C", "83": "C", "51": "C", "52": "C", "10": "C", "73": "C-D", "76": "C", "88": "C", "162-5": "C",
         "135": "C", "125": "C", "126": "C", "32": "C", "29": "C", "94": "C", "21": "C", "78": "C", "19": "C",
         "161-1": "C", "161-2": "C", "160": "C", "82": "C", "40": "C", "41": "C", "42": "C", "87": "C", "128": "C",
         "161-6": "C", "1": "C", "161-3": "C", "161-4": "C", "145": "C", "148": "C", "81": "B-C", "53": "B-C", "55": "C", "75": "B-C"}
TAIL = ("Other kinds of page may occur among them (typed sheets, letters, printed pages, other hands, drawings): "
        "transcribe each page as it is, in its own language, and record its hand in the inventory.")


def sentence(x):
    c, scans = x["cote"], x["scans"]
    if c in SPECIAL:
        what, notes = SPECIAL[c]
    else:
        what, notes = GENERIC[GRADE[c]], NOTES.get(c, {})
    s = f"Sample pages of this file, looked at in a survey, are {what}."
    seen = [v for k, v in sorted(notes.items()) if k in scans]
    if seen:
        s += " In this task, " + "; ".join(seen) + "."
    if len(scans) > 1 and scans[-1] - scans[0] + 1 > len(scans):
        s += " The scans are not all consecutive: scans of this file that are not listed are blank or belong to other tasks."
    return s + " " + TAIL
