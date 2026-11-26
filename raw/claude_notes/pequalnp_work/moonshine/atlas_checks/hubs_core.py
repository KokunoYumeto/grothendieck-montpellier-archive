"""Count, for each curated atlas object, the maps (of all 1281) that name at least one of its core entries, and the
number of home entries those maps come from; also the maps joining two core sets (object-object links)."""
import json, os, sys, collections, itertools
D = sys.argv[1]
M = json.load(open(os.path.join(D, 'maps.json'), encoding='utf-8'))
def rng(p, a, b):
    return ['%s-%03d' % (p, i) for i in range(a, b + 1)]
S, A, W = (lambda *x: [i for r in x for i in (rng('S6', *r) if isinstance(r, tuple) else ['S6-%03d' % r])]), \
          (lambda *x: [i for r in x for i in (rng('AG', *r) if isinstance(r, tuple) else ['AG-%03d' % r])]), \
          (lambda *x: [i for r in x for i in (rng('WEEK', *r) if isinstance(r, tuple) else ['WEEK-%03d' % r])])
CORE = {
 'O1': S((1, 7), 13, 19, 27, 28, (35, 37)) + A(1, 4, 10, 27, 39, 116) + W(5, 6, 13, 14, 15, 22, 99),
 'O2': S(1, 16, 18, 25) + A(10, 14) + W(6, 22),
 'O3': S((8, 12), 23, 25, 26, 37, 38) + A(8, 11) + W(2, 18),
 'O4': S(63, 65, 66, 81, 104, 113) + A(9, 56, 58, 114) + W(7, 91, 139),
 'O5': S(15, 76, 102) + A(2, 8, 9, 91) + W(31, 111, 127, 139),
 'O6': S(2, 3, 29, 67, 94, 95, 105) + A(1, 7, 57, 80, 84, 104) + W(6, 72, 103, 109, 122, 128, 130, 132),
 'O7': S(30, 36, 67, 96, 98, 99, 103, 123) + A(1, 3, 17, 28, (80, 87), 97, 120) + W(24, 109, 121, 126, 127, 132, 133),
 'O8': S(24, 96, 99) + A(1, 15, 16, 34, 35, 98) + W(31,),
 'O9': S(5, 7, 9, 13, 14, 91, 100, 101) + A(10, 16, 22, 29, 41, 91, 92) + W(23, 27),
 'O10': S(29, 33, 83, 84, 86, 87) + A(6, 69, 70, 99, 100) + W(1, 3, 4, 9, 10, 12, 19, 20, 21, 25),
 'O11': S(41, 42, 68, 77, 78, 79, 82, 86, 125) + A(69, 70, 71, 123) + W(8, 36, 90, 91, (97, 104), 107),
 'O12': S(4, 84) + A(63, 70) + W(19, 20, 89, 99),
 'O13': A(20, 23, 24, 25, 28, 34, 118) + W(31, 96, 105, 108, 134),
 'O14': S(57, 69, 90) + A(12, 44, 63, 73) + W(25, 37, 51, 56, 65, 70, 71, 83, 84, 100, 106),
 'O15': S((43, 50), 52, 74, 88, 89, 118) + A(43, 63) + W(13, (28, 30), (33, 35), (38, 41), 44, (52, 54), (58, 66), 86),
 'O16': S((42, 51), 61, 69, 72, 85, 86, 110) + A(69, 70) + W(35, 36, 41, (46, 48), 54, 57, 89),
 'O17': S(42, 46, 68, 109, 119) + A(54, 55, 57, 68) + W(50, 78, 80, 81, 86, 87, 118),
 'O18': S(32, 36, 40, 52, (57, 60), 72, 108) + A(31, 32, (44, 51), 61, 62, 65, 66) + W(33, 49, 53, 143),
 'O19': S((52, 56), 62, 70, 71, 73, (117, 125)) + A(43, 44, 62, 64, 65, 67, 124, 125) + W(34, 45, 55, 58, 59, 64, 78, 79, 87, 129, 131, 150, 151),
 'O20': S(42, 54, 61, 62, 85, (110, 112)) + A(53, 90, 94, 107) + W(19, 28, 43, (45, 48), 59, 61, 63, 102, 107, 108, 129, 130, (135, 138), 147, 153),
 'O21': S((114, 116)) + A(8, 54, 56, 72, (78, 82), 99, (120, 122)) + W(12, 31, 82, 85, 92, 93, 111, 122, 123, 127, 128, (139, 149)),
 'O22': S((29, 33), 37) + A(5, 69, 74, 97, 102, 103) + W(10, 17, 26, 71, 132),
 'O23': S(31, 40, 41) + A(5, 59, 60, 104) + W(6, 11, 33, 37, (67, 69), 74, 83, 142),
 'O24': S(23, 87, 88, 92) + A(17, 40, 52, 101, 109, 126) + W(13, 16, 28, 29, 42, 48, 116, 125),
 'O25': S(7, 14) + A((19, 21), 41, 85, 86) + W(22, 23, 29, 30, 49, 66, 79, 110, 121, 124, 144, 148, 151, 152),
 'O26': S(81, 110) + A(38, 52, 53, 82, 83, 85, 90, (94, 96), 107, 108) + W(110, (112, 114), (122, 124), 127),
 'O27': S(40, 106, 113) + A(71, (110, 113), 115, 117) + W(7, 37, 40, 90),
 'O28': S(60, 98, (104, 107), 117, 121, 122) + W(77, 150),
}
out = {}
for o, core in CORE.items():
    cs = set(core)
    ms = [mp for mp in M if (set(mp['all_ids']) | {mp['home']}) & cs]
    homes = set(mp['home'] for mp in ms)
    files = collections.Counter(mp['mid'].split(':')[0] for mp in ms)
    out[o] = (len(ms), len(homes), dict(files), len(core))
for o in sorted(out, key=lambda o: -out[o][0]):
    print(o, out[o])
# object-object links: maps whose named entries meet both core sets (home in one, a target in the other)
link = collections.defaultdict(list)
for mp in M:
    ids = set(mp['all_ids']) | {mp['home']}
    hit = [o for o, core in CORE.items() if ids & set(core)]
    h = mp['home']
    homeo = [o for o, core in CORE.items() if h in core]
    for a in homeo:
        for b in hit:
            if a != b:
                tg = [i for i in ids if i != h and i in set(CORE[b])]
                if tg:
                    link[tuple(sorted((a, b), key=lambda x: int(x[1:])))].append(mp['mid'])
json.dump({'core': CORE, 'counts': out, 'links': {'%s-%s' % k: sorted(set(v)) for k, v in link.items()}},
          open(os.path.join(D, 'hubs_core.json'), 'w', encoding='utf-8'), ensure_ascii=False)
top = sorted(link.items(), key=lambda kv: -len(set(kv[1])))[:45]
for (a, b), v in top:
    print(a, b, len(set(v)))
