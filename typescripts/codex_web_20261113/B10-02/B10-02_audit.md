# Second reading audit

Times are UTC. Each crop-first reading was recorded before reopening that page’s transcription. Formula lists reproduce every delimited formula in the final page file, including repeated one-letter occurrences; state macros remain visible in those lists. No OCR, external text, or compilation was used.


## Scan 42

Start (UTC): 2026-11-13T19:59:10.618256+00:00

End (UTC): 2026-11-13T20:03:23.048655+00:00

Crop-first words/accents (before opening the page file): « pe de présentation finie », « préschéma », « opé-rateurs » (interior overtyped; possible « opératerus »), « homogènes », « fibré principal homogène », « fidèlement », « localement de présentation finie », « indice », « Compte tenu », « l'énoncé », « résulte », « propriété », inserted « couvrants », « fppf rappelée ». Acute accents are visible in présentation, préschéma, homogènes, fibré, énoncé, résulte, propriété and rappelée; grave accent in fidèlement. No accent on Compte, principal or couvrants. The opening « pe » is a continuation, not a word supplied from another page. Deleted word before l'énoncé looks like l'exp/l'ex; overwritten word below couvrants remains uncertain. Top H in H = H_j × S looks doubled. Marginal definitions have j descending and i without descender; the body has i ≥ j. Handwritten manuscript 10, archive 41. Two crossing flourish strokes occupy the otherwise empty lower part.


Comparison: read the six underlined lines and the proof against the crop, including the cropped opening and the two marginal replacement definitions. All formula factors and base indices agree with the visible forms. Each j in H_j, G_j and S_j has a descender; the i in the later H_i, G_i and S_i does not. The index inequality is ≥. The first H after « Pour que » has offset typed impressions; retained as mathbb H. Other capitals inspected separately retain ordinary typed forms. The cancelled formula above sous G remains uncertain; its apparent equality and indices have not been inferred as certain from the left-margin definition. The thick correction at sous G does not establish whether the main G itself is cancelled, so its existing doubt is retained. Every correction, insertion and underlining in the upper paragraph and proof is represented. The two lower strokes have no labels or arrowheads; their crossings and bends are represented by the TikZ figure. No text appears in the bottom third apart from the archive number. The following formula/correction lists were compared to these crops, not to another transcription.


### Changes

No change.

### Every delimited formula, in page-file order

1. inline

```tex
H_j
```

2. inline

```tex
S_j
```

3. inline

```tex
G_j
```

4. inline

```tex
\mathbb{H}=H_j\handwritten{\times}_{S_j}S
```

5. inline

```tex
S
```

6. inline

```tex
\deleted{\unsure{G|H}}\inserted{G=G_j\handwritten{\times}_{S_j}S}
```

7. inline

```tex
\unsure{G}\inserted{\deleted{\unsure{G=G_j\times_{S_j}S}}}
```

8. inline

```tex
i\handwritten{\in}I
```

9. inline

```tex
i\handwritten{\geq}j
```

10. inline

```tex
H_i=H_j\handwritten{\times}_{S_j}S_i
```

11. inline

```tex
S_i
```

12. inline

```tex
\deleted{\unsure{G_i}}\inserted{G_i=G_j\handwritten{\times}_{S_j}S_i}
```

13. inline

```tex
G_i
```

### Every i/j index occurrence (local TeX contexts)

1. `e présentation finie, $H_j$ un $S_j$-préschéma de `
2. `ation finie, $H_j$ un $S_j$-préschéma de présentat`
3. `pérateurs|opératerus} $G_j$. Pour que $\mathbb{H}=`
4. `. Pour que $\mathbb{H}=H_j\handwritten{\times}_{S_`
5. `=H_j\handwritten{\times}_{S_j}S$ soit un $S$-préschéma`
6. `nsure{G|H}}\inserted{G=G_j\handwritten{\times}_{S_`
7. `=G_j\handwritten{\times}_{S_j}S}$ (resp. un fibré prin`
8. `ted{\deleted{\unsure{G=G_j\times_{S_j}S}}}$\unsure`
9. `eted{\unsure{G=G_j\times_{S_j}S}}}$\unsure{)} pour la `
10. `tten{\geq}j$, tel que $H_i=H_j\handwritten{\times}`
11. `{\geq}j$, tel que $H_i=H_j\handwritten{\times}_{S_`
12. `=H_j\handwritten{\times}_{S_j}S_i$ soit un $S_i$-présc`
13. `ndwritten{\times}_{S_j}S_i$ soit un $S_i$-préschém`
14. `es}_{S_j}S_i$ soit un $S_i$-préschéma en espaces h`
15. `sous $\deleted{\unsure{G_i}}\inserted{G_i=G_j\hand`
16. `\unsure{G_i}}\inserted{G_i=G_j\handwritten{\times}`
17. `ure{G_i}}\inserted{G_i=G_j\handwritten{\times}_{S_`
18. `=G_j\handwritten{\times}_{S_j}S_i}$ (resp. un fibré pr`
19. `ndwritten{\times}_{S_j}S_i}$ (resp. un fibré princ`
20. `incipal homogène sous $G_i$).}  Compte tenu de (10`

### Handwritten and correction placements

1. handwritten, following `\cotefile{10} \scanpage{42} \mspage{`:

```tex
\handwritten{10}
```

2. handwritten, following `érateurs|opératerus} $G_j$. Pour que $\mathbb{H}=H_j`:

```tex
\handwritten{\times}
```

3. deleted, following `S$ soit un $S$-préschéma en espaces homogènes sous $`:

```tex
\deleted{\unsure{G|H}}
```

4. inserted, following `ma en espaces homogènes sous $\deleted{\unsure{G|H}}`:

```tex
\inserted{G=G_j\handwritten{\times}_{S_j}S}
```

5. handwritten, following `omogènes sous $\deleted{\unsure{G|H}}\inserted{G=G_j`:

```tex
\handwritten{\times}
```

6. inserted, following ` (resp. un fibré principal homogène sous $\unsure{G}`:

```tex
\inserted{\deleted{\unsure{G=G_j\times_{S_j}S}}}
```

7. deleted, following ` fibré principal homogène sous $\unsure{G}\inserted{`:

```tex
\deleted{\unsure{G=G_j\times_{S_j}S}}
```

8. handwritten, following `ine{, il faut et il suffit qu'il existe un indice $i`:

```tex
\handwritten{\in}
```

9. handwritten, following `fit qu'il existe un indice $i\handwritten{\in}I$, $i`:

```tex
\handwritten{\geq}
```

10. handwritten, following `ten{\in}I$, $i\handwritten{\geq}j$, tel que $H_i=H_j`:

```tex
\handwritten{\times}
```

11. deleted, following ` soit un $S_i$-préschéma en espaces homogènes sous $`:

```tex
\deleted{\unsure{G_i}}
```

12. inserted, following `ma en espaces homogènes sous $\deleted{\unsure{G_i}}`:

```tex
\inserted{G_i=G_j\handwritten{\times}_{S_j}S_i}
```

13. handwritten, following `ogènes sous $\deleted{\unsure{G_i}}\inserted{G_i=G_j`:

```tex
\handwritten{\times}
```

14. deleted, following ` de (10.14) et de (EGA IV 8.8.2, 8.8.3 et 8.10.5) , `:

```tex
\deleted{\unsure{l'exp|l'ex}}
```

15. deleted, following `é résulte de la propriété concernant les morphismes `:

```tex
\deleted{\unsure{concernant|couvrant}}
```

16. inserted, following `es morphismes \deleted{\unsure{concernant|couvrant}}`:

```tex
\inserted{couvrants}
```


## Scan 43

Start (UTC): 2026-11-13T20:03:23.096154+00:00

End (UTC): 2026-11-13T20:04:55.426163+00:00

Crop-first words/accents: « Préschémas », « Notations : soient », « préschéma », « S-préschéma », « structural », « Lemme », « Soient », « quasi-compacts », « quasi-séparés », « structuraux », « homomorphisme canonique », « isomorphisme », « affines », « plat », « fausse|faux Formule » in the circled margin note. Middle: « Posons », « quasi-séparé », « S'est », « d'après », « D'après », « se factorise à travers », « au moyen d'un morphisme p : G », « quasi-séparés », cancelled « sur », « même », handwritten « Ou », « ou bien », « de nouveau », handwritten « ou p' » without a visible grave accent on ou. Bottom: « D'où », « d'après », « Corollaire », « On définit », « sous-catégorie pleine », « des X-préschémas », « quasi-séparés », « S-préschémas », « Ce foncteur commute aux produits finis ». Acute accents in Préschémas/préschéma/séparé/définit/catégorie; grave in après, à and où; circumflex in même. Plain typed X in X-préschémas and G in p:G remain unusual. Handwritten round a-like A, looped O, phi, stars, arrows; two S glyphs look double struck. Two small curved correction marks appear below the first tensor and below f_* in c), plus a small angular mark above « d'un » in the proof.


Full text comparison: all paragraphs, references, comma/semicolon interventions, the two marginal circles, and the handwritten « ou » were reread. The handwritten « ou » has no visible accent. Typed p:G and X-préschémas are retained. Added four graphic pen marks: the little hook at the lemma underline, the curve beneath the tensor base, the curve below f-star in c), and the angular mark above d'un. The circles retain all their visible words and the underlined O. The first g-prime pullback exponent in the long base-change formula is a many-rayed star; the second has two strong crossing strokes and an indistinct extra stroke, now marked star|times. Primes are distinct from the commas. No i or j indices occur. Each A-like glyph was checked against the initial rounded a-shaped letter; the A/a ambiguity remains. Every O has the looped handwritten shape except the plain underlined O in the margin. The tensor index S and the S-prime in the Y-prime definition have offset impressions; the other S letters, including the heading and Sch index, have single strokes. Spec and Sch have ordinary typed capitals. The handwritten phi has the same open-loop form in the display; no bold alphabet was introduced. All displayed factors, bases, pullback and direct-image star positions and the final factor order A(Y) tensor A(X) were compared individually. Formula and correction lists below include repeated small occurrences as well as the principal displays.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{\makebox[0pt][l]{\raisebox{-2ex}{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.1) -- (.09,.1) -- (.09,-.07);\end{tikzpicture}}}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
% Curved pen mark below the tensor-base index.
\figure{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.18) .. controls (.25,-.2) and (.8,-.18) .. (1.25,.22);\end{tikzpicture}}}

```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
}
% Curved pen mark below the star of f in c).
\figure{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.15) .. controls (.15,-.16) and (.45,-.16) .. (.6,.16);\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{\makebox[0pt][l]{\raisebox{2ex}{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0) -- (.17,.09) -- (.43,-.05);\end{tikzpicture}}}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\unsure{
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
|\times}
```


### Every delimited formula, in page-file order

1. inline

```tex
S
```

2. inline

```tex
X
```

3. inline

```tex
S
```

4. inline

```tex
f:X\handwritten{\to}S
```

5. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}(X)=f_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)
```

6. inline

```tex
X
```

7. inline

```tex
Y
```

8. inline

```tex
S
```

9. inline

```tex
S
```

10. inline

```tex
f:X\handwritten{\to}S
```

11. inline

```tex
g:Y\handwritten{\to}S
```

12. display

```tex
\handwritten{\varphi}:\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_{\mathbb{S}}}\handwritten{\mathcal{A}}(Y)\handwritten{\longrightarrow}\handwritten{\mathcal{A}}(X\handwritten{\times}_S Y)
```

13. inline

```tex
f
```

14. inline

```tex
g
```

15. inline

```tex
f
```

16. inline

```tex
g
```

17. inline

```tex
g
```

18. inline

```tex
f_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)
```

19. inline

```tex
\handwritten{\mathcal{O}}_S
```

20. inline

```tex
f_*(\underline{O}_X)
```

21. inline

```tex
g
```

22. inline

```tex
S'=\operatorname{Spec}\handwritten{\mathcal{A}}(X\unsure{)}
```

23. inline

```tex
Y'=Y\handwritten{\times}_S\mathbb{S}'
```

24. inline

```tex
g'=g\handwritten{\times}_S S'
```

25. inline

```tex
v
```

26. inline

```tex
S'\handwritten{\to}S
```

27. inline

```tex
Y
```

28. inline

```tex
S
```

29. inline

```tex
S'
```

30. inline

```tex
S
```

31. inline

```tex
g
```

32. display

```tex
g'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{Y'})=v^{\handwritten{*}}g_{\handwritten{*}}(\handwritten{\mathcal{O}}_Y)=\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_{S'}.
```

33. inline

```tex
f
```

34. inline

```tex
v
```

35. inline

```tex
p:G\handwritten{\to}S'
```

36. inline

```tex
X\handwritten{\times}_S Y=X\handwritten{\times}_{S'}Y'
```

37. inline

```tex
p_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)=\handwritten{\mathcal{O}}_{S'}
```

38. inline

```tex
v
```

39. inline

```tex
f
```

40. inline

```tex
p
```

41. inline

```tex
Y
```

42. inline

```tex
S
```

43. inline

```tex
Y'
```

44. inline

```tex
S'
```

45. inline

```tex
X
```

46. inline

```tex
S
```

47. inline

```tex
p
```

48. display

```tex
\deleted{\unsure{p'_*|q'_*}}\ p'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{X\handwritten{\times}_S Y})=g'^{\handwritten{*}}p_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)=g'^{\handwritten{\unsure{*|\times}}}(\handwritten{\mathcal{O}}_{S'})=\handwritten{\mathcal{O}}_{Y'}\handwritten{,\ \text{ou }p'=p\times_{S'}Y'.}
```

49. display

```tex
\handwritten{\mathcal{A}}(X\handwritten{\times}_S Y)=v_{\handwritten{*}}g'_{\handwritten{*}}p'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{X\handwritten{\times}_S Y})=v_{\handwritten{*}}g'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{\handwritten{Y}'})=v_{\handwritten{*}}(\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_{S'})=\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{A}}(X)
```

50. inline

```tex
X\handwritten{\rightsquigarrow}\operatorname{Spec}\handwritten{\mathcal{A}}(X)
```

51. inline

```tex
\operatorname{Sch}_{/S}
```

52. inline

```tex
X
```

53. inline

```tex
S
```

54. inline

```tex
\handwritten{\mathcal{A}}(X)
```

55. inline

```tex
\handwritten{\mathcal{O}}_S
```

56. inline

```tex
S
```

57. inline

```tex
S
```

58. inline

```tex
S
```

59. inline

```tex
S
```

### Every i/j index occurrence (local TeX contexts)

None.

### Handwritten and correction placements

1. handwritten, following `\scanpage{43} \mspage{`:

```tex
\handwritten{11}
```

2. handwritten, following `\uline{11.- Préschémas en groupes affines.}  \uline{`:

```tex
\handwritten{11}
```

3. handwritten, following ` soient $S$ un préschéma, $X$ un $S$-préschéma, $f:X`:

```tex
\handwritten{\to}
```

4. handwritten, following `andwritten{\to}S$ le morphisme structural; on pose $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

5. handwritten, following `on pose $\handwritten{\unsure{\mathcal{A}|a}}(X)=f_{`:

```tex
\handwritten{*}
```

6. handwritten, following `tten{\unsure{\mathcal{A}|a}}(X)=f_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

7. handwritten, following `f_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)$.  `:

```tex
\handwritten{\makebox[0pt][l]{\raisebox{-2ex}{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.1) -- (.09,.1) -- (.09,-.07);\end{tikzpicture}}}}
```

8. handwritten, following `chémas quasi-compacts et quasi-séparés sur $S$, $f:X`:

```tex
\handwritten{\to}
```

9. handwritten, following `asi-séparés sur $S$, $f:X\handwritten{\to}S$ et $g:Y`:

```tex
\handwritten{\to}
```

10. handwritten, following `es structuraux. Alors l'homomorphisme canonique} \[ `:

```tex
\handwritten{\varphi}
```

11. handwritten, following `l'homomorphisme canonique} \[ \handwritten{\varphi}:`:

```tex
\handwritten{\mathcal{A}}
```

12. handwritten, following `[ \handwritten{\varphi}:\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

13. handwritten, following `:\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

14. handwritten, following `en{\otimes}_{\handwritten{\mathcal{O}}_{\mathbb{S}}}`:

```tex
\handwritten{\mathcal{A}}
```

15. handwritten, following `athcal{O}}_{\mathbb{S}}}\handwritten{\mathcal{A}}(Y)`:

```tex
\handwritten{\longrightarrow}
```

16. handwritten, following `written{\mathcal{A}}(Y)\handwritten{\longrightarrow}`:

```tex
\handwritten{\mathcal{A}}
```

17. handwritten, following `dwritten{\longrightarrow}\handwritten{\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

18. handwritten, following `urved pen mark below the tensor-base index. \figure{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.18) .. controls (.25,-.2) and (.8,-.18) .. (1.25,.22);\end{tikzpicture}}
```

19. margin, following `.2) and (.8,-.18) .. (1.25,.22);\end{tikzpicture}}} `:

```tex
\margin{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) ellipse (1.2 and .7);
\node[align=left] at (0,0) {\unsure{fausse|faux}\\Formule};
\end{tikzpicture}}}
```

20. handwritten, following `(.8,-.18) .. (1.25,.22);\end{tikzpicture}}} \margin{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) ellipse (1.2 and .7);
\node[align=left] at (0,0) {\unsure{fausse|faux}\\Formule};
\end{tikzpicture}}
```

21. handwritten, following ` est plat et affine}  \uline{c) $g$ est plat et $f_{`:

```tex
\handwritten{*}
```

22. handwritten, following `ne}  \uline{c) $g$ est plat et $f_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

23. handwritten, following `ndwritten{*}}(\handwritten{\mathcal{O}}_X)$ est un $`:

```tex
\handwritten{\mathcal{O}}
```

24. handwritten, following ` Curved pen mark below the star of f in c). \figure{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.15) .. controls (.15,-.16) and (.45,-.16) .. (.6,.16);\end{tikzpicture}}
```

25. margin, following `.16) and (.45,-.16) .. (.6,.16);\end{tikzpicture}}} `:

```tex
\margin{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) ellipse (1.1 and .7);
\node at (0,0) {$f_*(\underline{O}_X)$};
\end{tikzpicture}}}
```

26. handwritten, following ` (.45,-.16) .. (.6,.16);\end{tikzpicture}}} \margin{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) ellipse (1.1 and .7);
\node at (0,0) {$f_*(\underline{O}_X)$};
\end{tikzpicture}}
```

27. handwritten, following `i est plat et affine. Posons $S'=\operatorname{Spec}`:

```tex
\handwritten{\mathcal{A}}
```

28. handwritten, following `me{Spec}\handwritten{\mathcal{A}}(X\unsure{)}$ $Y'=Y`:

```tex
\handwritten{\times}
```

29. handwritten, following `e{)}$ $Y'=Y\handwritten{\times}_S\mathbb{S}'$, $g'=g`:

```tex
\handwritten{\times}
```

30. handwritten, following `written{\times}_S S'$ et notons $v$ le morphisme $S'`:

```tex
\handwritten{\to}
```

31. handwritten, following ` III 1.4.15 et IV 1.2.7 ou II 1.5.2), on a : \[ g'_{`:

```tex
\handwritten{*}
```

32. handwritten, following ` 1.2.7 ou II 1.5.2), on a : \[ g'_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

33. handwritten, following `\handwritten{*}}(\handwritten{\mathcal{O}}_{Y'})=v^{`:

```tex
\handwritten{*}
```

34. handwritten, following `andwritten{\mathcal{O}}_{Y'})=v^{\handwritten{*}}g_{`:

```tex
\handwritten{*}
```

35. handwritten, following `al{O}}_{Y'})=v^{\handwritten{*}}g_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

36. handwritten, following `*}}g_{\handwritten{*}}(\handwritten{\mathcal{O}}_Y)=`:

```tex
\handwritten{\mathcal{A}}
```

37. handwritten, following `written{\mathcal{O}}_Y)=\handwritten{\mathcal{A}}(Y)`:

```tex
\handwritten{\otimes}
```

38. handwritten, following `=\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

39. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

40. handwritten, following ` II 1.2.7), $f$ se factorise à travers $v$ au moyen `:

```tex
\handwritten{\makebox[0pt][l]{\raisebox{2ex}{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0) -- (.17,.09) -- (.43,-.05);\end{tikzpicture}}}}
```

41. handwritten, following `- (.43,-.05);\end{tikzpicture}}}}d'un morphisme $p:G`:

```tex
\handwritten{\to}
```

42. handwritten, following `'un morphisme $p:G\handwritten{\to}S'$, et on a : $X`:

```tex
\handwritten{\times}
```

43. handwritten, following `tten{\to}S'$, et on a : $X\handwritten{\times}_S Y=X`:

```tex
\handwritten{\times}
```

44. handwritten, following `en{\times}_S Y=X\handwritten{\times}_{S'}Y'$ et $p_{`:

```tex
\handwritten{*}
```

45. handwritten, following `handwritten{\times}_{S'}Y'$ et $p_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

46. handwritten, following `t $p_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)=`:

```tex
\handwritten{\mathcal{O}}
```

47. deleted, following `que $v$ et $f$ sont quasi-compacts et quasi-séparés,`:

```tex
\deleted{sur}
```

48. handwritten, following `ur} il en est de même de $p$ (EGA IV 1.2.2 et 1.2.4)`:

```tex
\handwritten{;}
```

49. handwritten, following ` même de $p$ (EGA IV 1.2.2 et 1.2.4)\handwritten{;} `:

```tex
\handwritten{O}
```

50. deleted, following ` et IV 1.2.7), et dans les deux cas, on trouve : \[ `:

```tex
\deleted{\unsure{p'_*|q'_*}}
```

51. handwritten, following `s, on trouve : \[ \deleted{\unsure{p'_*|q'_*}}\ p'_{`:

```tex
\handwritten{*}
```

52. handwritten, following ` \deleted{\unsure{p'_*|q'_*}}\ p'_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

53. handwritten, following `}\ p'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{X`:

```tex
\handwritten{\times}
```

54. handwritten, following `itten{\mathcal{O}}_{X\handwritten{\times}_S Y})=g'^{`:

```tex
\handwritten{*}
```

55. handwritten, following `{X\handwritten{\times}_S Y})=g'^{\handwritten{*}}p_{`:

```tex
\handwritten{*}
```

56. handwritten, following `imes}_S Y})=g'^{\handwritten{*}}p_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

57. handwritten, following `_{\handwritten{*}}(\handwritten{\mathcal{O}}_X)=g'^{`:

```tex
\handwritten{\unsure{*|\times}}
```

58. handwritten, following `mathcal{O}}_X)=g'^{\handwritten{\unsure{*|\times}}}(`:

```tex
\handwritten{\mathcal{O}}
```

59. handwritten, following `\unsure{*|\times}}}(\handwritten{\mathcal{O}}_{S'})=`:

```tex
\handwritten{\mathcal{O}}
```

60. handwritten, following `en{\mathcal{O}}_{S'})=\handwritten{\mathcal{O}}_{Y'}`:

```tex
\handwritten{,\ \text{ou }p'=p\times_{S'}Y'.}
```

61. handwritten, following `tten{,\ \text{ou }p'=p\times_{S'}Y'.} \]  D'où : \[ `:

```tex
\handwritten{\mathcal{A}}
```

62. handwritten, following `s_{S'}Y'.} \]  D'où : \[ \handwritten{\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

63. handwritten, following `dwritten{\mathcal{A}}(X\handwritten{\times}_S Y)=v_{`:

```tex
\handwritten{*}
```

64. handwritten, following `}(X\handwritten{\times}_S Y)=v_{\handwritten{*}}g'_{`:

```tex
\handwritten{*}
```

65. handwritten, following `es}_S Y)=v_{\handwritten{*}}g'_{\handwritten{*}}p'_{`:

```tex
\handwritten{*}
```

66. handwritten, following `written{*}}g'_{\handwritten{*}}p'_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

67. handwritten, following `*}}p'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{X`:

```tex
\handwritten{\times}
```

68. handwritten, following `ritten{\mathcal{O}}_{X\handwritten{\times}_S Y})=v_{`:

```tex
\handwritten{*}
```

69. handwritten, following `{X\handwritten{\times}_S Y})=v_{\handwritten{*}}g'_{`:

```tex
\handwritten{*}
```

70. handwritten, following `imes}_S Y})=v_{\handwritten{*}}g'_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{O}}
```

71. handwritten, following `{*}}g'_{\handwritten{*}}(\handwritten{\mathcal{O}}_{`:

```tex
\handwritten{Y}
```

72. handwritten, following `}}(\handwritten{\mathcal{O}}_{\handwritten{Y}'})=v_{`:

```tex
\handwritten{*}
```

73. handwritten, following `mathcal{O}}_{\handwritten{Y}'})=v_{\handwritten{*}}(`:

```tex
\handwritten{\mathcal{A}}
```

74. handwritten, following `'})=v_{\handwritten{*}}(\handwritten{\mathcal{A}}(Y)`:

```tex
\handwritten{\otimes}
```

75. handwritten, following `(\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

76. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

77. handwritten, following `tten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_{S'})=`:

```tex
\handwritten{\mathcal{A}}
```

78. handwritten, following `tten{\mathcal{O}}_{S'})=\handwritten{\mathcal{A}}(Y)`:

```tex
\handwritten{\otimes}
```

79. handwritten, following `=\handwritten{\mathcal{A}}(Y)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

80. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{A}}
```

81. handwritten, following `(X) \] d'après (EGA II 1.4.7).  \uline{Corollaire 11`:

```tex
\handwritten{.}
```

82. handwritten, following `laire 11\handwritten{.}2.- On définit un foncteur $X`:

```tex
\handwritten{\rightsquigarrow}
```

83. handwritten, following ` $X\handwritten{\rightsquigarrow}\operatorname{Spec}`:

```tex
\handwritten{\mathcal{A}}
```

84. handwritten, following `s quasi-compacts et quasi-séparés sur $S$ tels que $`:

```tex
\handwritten{\mathcal{A}}
```

85. handwritten, following `S$ tels que $\handwritten{\mathcal{A}}(X)$ soit un $`:

```tex
\handwritten{\mathcal{O}}
```


## Scan 44

Start (UTC): 2026-11-13T20:04:55.603938+00:00

End (UTC): 2026-11-13T20:06:46.830084+00:00

Crop-first words/accents: « Définition 11.3.- Etant donné », « quasi-compact et quasi-séparé », « enveloppe affine », « Etant donnés », « quasi-cohérents », « S-foncteur », « S-foncteurs », « sous-S-foncteur », « formé », « homomorphismes », « cf. Exp. I » with Exp. struck, « binivoque » with un inserted over n, « Soit X un S-préschéma », another « binivoque » with un above n, then « correspondance biunivoque », « sous-ensemble », « Proposition 11.5.- Soient X un S-préschéma quasi-compact quasi-séparé », « vérifiées » with final s cancelled, « Alors », « homomorphisme canonique », « où », « désigne l'Algèbre symétrique », « Pour montrer », « d'après », « même », « D'après ». Etant has no initial accent in both occurrences. Acute accents on Définition/donné/donnés/séparé/cohérents/formé/préschéma/vérifiée/désigne/symétrique; grave on où, Algèbre, après; circumflex on même. The typed binivoque forms and Soient X remain conspicuous. Two small pen marks near 11.3/11.4 may be vu or checking flourishes. The handwritten algebra S has an angular outline and doubled/crossed portions; the V forms have two left strokes, and the W in the inserted equivalence has parallel left stems. Circled marginal 5. Several parentheses are thickly cancelled in the first Hom-of-modules formula.


Full reading completed from the three thirds and the enlarged Hom/parenthesis/S crops. The typed headings have ordinary single-stroke capitals; Etant has no accent. The first bi-n-ivoque has n cancelled and un inserted; the second has un above a surviving n, so the original n remains. Final s of vérifiées is cancelled. The inserted i.e. equivalence reverses E/F in the W pair and is retained in that order. The enlarged closing shape after the first Hom formula shows one hatched parenthesis before the comma: removed the invented extra closing parenthesis and marked the single hatched one as a doubtful cancelled parenthesis, matching the local cancellation before F. The final Mod punctuation remains uncertain. Handwritten S was examined at the first heavy occurrence, at the clearer « où S(F) », and under the bottom cancellation: the ordinary S outline has closing reinforcement strokes in both bowls, so changed the provisional fraktur/calligraphic reading to mathbb S. W has parallel left stems on this very crop and is mathbb W; removed the provisional plain-W alternative. Every V has separate parallel strokes; the E/F forms have distinct lobes/crossbars, and A/a remains ambiguous. The O in the last paragraph has a visibly double-struck S index. No i/j index occurs. Hom subscripts, T/S bases, the order E,F, and every product/tensor arrow were checked. The short vu-like marks remain doubtful rather than expanded into words with certainty; the marginal 5 and all underlines remain. The displayed formula list below includes the inline long expressions as written.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
han
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
writ
->
ele
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
d{\u
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
sure
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
)
->
}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
unsure{\
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
W}|
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
unsure{\
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
}|\mathcal{S}
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```


### Every delimited formula, in page-file order

1. inline

```tex
S
```

2. inline

```tex
G
```

3. inline

```tex
S
```

4. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}(G)
```

5. inline

```tex
\handwritten{\mathcal{O}}_S
```

6. inline

```tex
G_{\mathrm{af}}
```

7. inline

```tex
G
```

8. inline

```tex
S
```

9. inline

```tex
G_{\mathrm{af}}=\operatorname{Spec}\handwritten{\mathcal{A}}(G)
```

10. inline

```tex
\handwritten{\mathcal{O}}_S
```

11. inline

```tex
\handwritten{\mathcal{E}}
```

12. inline

```tex
\handwritten{\mathcal{F}}
```

13. inline

```tex
\handwritten{\mathcal{H}om}_S(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

14. inline

```tex
S
```

15. inline

```tex
S
```

16. inline

```tex
\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}})
```

17. inline

```tex
\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})
```

18. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

19. inline

```tex
S
```

20. inline

```tex
\handwritten{\mathcal{H}om}_S(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

21. inline

```tex
\handwritten{\mathcal{O}}_S
```

22. inline

```tex
\handwritten{\mathcal{O}}_S
```

23. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))(T)
```

24. inline

```tex
\deleted{\unsure{\operatorname{Hom}}}\operatorname{Hom}_{\handwritten{\mathcal{O}}_{S\deleted{\unsure{T}}}\text{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T,\deleted{\unsure{(}}\handwritten{\mathcal{F}\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T\deleted{\unsure{)}}
```

25. inline

```tex
\text{i.e.}\quad \mathcal{H}om_{\underline{O}_S}(\mathbb{V}(\mathcal{F}),\mathbb{V}(\mathcal{E}))\simeq\mathcal{H}om_{\underline{O}_S}(\mathbb{W}(\mathcal{E}),\mathbb{W}(\mathcal{F})).
```

26. inline

```tex
X
```

27. inline

```tex
S
```

28. inline

```tex
S
```

29. inline

```tex
X
```

30. inline

```tex
\handwritten{\mathcal{H}om}_S(\deleted{\handwritten{\unsure{\mathbb{V}|W}}}\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

31. inline

```tex
\operatorname{Hom}_S(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

32. inline

```tex
S
```

33. inline

```tex
X
```

34. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

35. inline

```tex
\operatorname{Hom}_S(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))=\operatorname{Hom}_{\handwritten{\mathcal{O}}_S\text{-}\unsure{\mathrm{Mod.}|\mathrm{Mod;}}}(\handwritten{\mathcal{E}},\handwritten{\mathcal{A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}})))
```

36. inline

```tex
X
```

37. inline

```tex
S
```

38. inline

```tex
S
```

39. inline

```tex
f:X\handwritten{\to}S
```

40. inline

```tex
\handwritten{\mathcal{E}}
```

41. inline

```tex
\handwritten{\mathcal{F}}
```

42. inline

```tex
\handwritten{\mathcal{O}}_S
```

43. inline

```tex
f
```

44. inline

```tex
\handwritten{\mathcal{F}}
```

45. inline

```tex
\handwritten{\mathcal{O}}_S
```

46. inline

```tex
\handwritten{\varphi:\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})\handwritten{\longrightarrow\mathcal{A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}))
```

47. inline

```tex
\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})
```

48. inline

```tex
\handwritten{\mathcal{F}}
```

49. inline

```tex
S
```

50. inline

```tex
X
```

51. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

52. inline

```tex
\operatorname{Hom}_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X)\handwritten{\otimes\mathcal{F}})
```

53. inline

```tex
\handwritten{\mathcal{F}}
```

54. inline

```tex
\handwritten{\mathcal{O}}_{\mathbb{S}}
```

55. inline

```tex
\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})
```

56. inline

```tex
\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}})
```

57. inline

```tex
S
```

### Every i/j index occurrence (local TeX contexts)

None.

### Handwritten and correction placements

1. handwritten, following `\scanpage{44} \mspage{`:

```tex
\handwritten{12}
```

2. handwritten, following `at, quasi-compact et quasi-séparé sur $S$, tel que $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

3. handwritten, following `dwritten{\unsure{\mathcal{A}|a}}(G)$ soit plat sur $`:

```tex
\handwritten{\mathcal{O}}
```

4. handwritten, following `$ le $S$-groupe $G_{\mathrm{af}}=\operatorname{Spec}`:

```tex
\handwritten{\mathcal{A}}
```

5. margin, following `}=\operatorname{Spec}\handwritten{\mathcal{A}}(G)$. `:

```tex
\margin{\deleted{\handwritten{\unsure{vu}}}}
```

6. deleted, following `torname{Spec}\handwritten{\mathcal{A}}(G)$. \margin{`:

```tex
\deleted{\handwritten{\unsure{vu}}}
```

7. handwritten, following `pec}\handwritten{\mathcal{A}}(G)$. \margin{\deleted{`:

```tex
\handwritten{\unsure{vu}}
```

8. handwritten, following `n{\unsure{vu}}}}  \uline{11.4.}- Etant donnés deux $`:

```tex
\handwritten{\mathcal{O}}
```

9. handwritten, following ` donnés deux $\handwritten{\mathcal{O}}_S$-Modules $`:

```tex
\handwritten{\mathcal{E}}
```

10. handwritten, following `hcal{O}}_S$-Modules $\handwritten{\mathcal{E}}$ et $`:

```tex
\handwritten{\mathcal{F}}
```

11. handwritten, following `\handwritten{\mathcal{F}}$ quasi-cohérents, notons $`:

```tex
\handwritten{\mathcal{H}om}
```

12. handwritten, following `si-cohérents, notons $\handwritten{\mathcal{H}om}_S(`:

```tex
\handwritten{\mathbb{V}}
```

13. handwritten, following `ndwritten{\mathcal{H}om}_S(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

14. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

15. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

16. handwritten, following `le $S$-foncteur des morphismes de $S$-foncteurs de $`:

```tex
\handwritten{\mathbb{V}}
```

17. handwritten, following `ismes de $S$-foncteurs de $\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

18. handwritten, following `itten{\mathbb{V}}(\handwritten{\mathcal{F}})$ dans $`:

```tex
\handwritten{\mathbb{V}}
```

19. handwritten, following `itten{\mathcal{F}})$ dans $\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

20. handwritten, following `ritten{\mathbb{V}}(\handwritten{\mathcal{E}})$, et $`:

```tex
\handwritten{\mathcal{H}om}
```

21. handwritten, following `en{\mathcal{E}})$, et $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

22. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

23. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

24. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

25. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

26. handwritten, following `andwritten{\mathcal{E}}))$ le sous-$S$-foncteur de $`:

```tex
\handwritten{\mathcal{H}om}
```

27. handwritten, following `sous-$S$-foncteur de $\handwritten{\mathcal{H}om}_S(`:

```tex
\handwritten{\mathbb{V}}
```

28. handwritten, following `ndwritten{\mathcal{H}om}_S(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

29. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

30. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

31. handwritten, following `\mathbb{V}}(\handwritten{\mathcal{E}}))$ formé des $`:

```tex
\handwritten{\mathcal{O}}
```

32. handwritten, following `s $\handwritten{\mathcal{O}}_S$- homomorphismes de $`:

```tex
\handwritten{\mathcal{O}}
```

33. deleted, following `ndwritten{\mathcal{O}}_S$-foncteurs en modules (cf. `:

```tex
\deleted{Exp.}
```

34. handwritten, following `foncteurs en modules (cf. \deleted{Exp.} I). Alors $`:

```tex
\handwritten{\mathcal{H}om}
```

35. handwritten, following `leted{Exp.} I). Alors $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

36. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

37. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

38. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

39. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

40. deleted, following `dwritten{\mathcal{E}}))(T)$ est en correspondance bi`:

```tex
\deleted{n}
```

41. inserted, following `athcal{E}}))(T)$ est en correspondance bi\deleted{n}`:

```tex
\inserted{\handwritten{un}}
```

42. handwritten, following `))(T)$ est en correspondance bi\deleted{n}\inserted{`:

```tex
\handwritten{un}
```

43. deleted, following `n}\inserted{\handwritten{un}}ivoque canonique avec $`:

```tex
\deleted{\unsure{\operatorname{Hom}}}
```

44. handwritten, following `ted{\unsure{\operatorname{Hom}}}\operatorname{Hom}_{`:

```tex
\handwritten{\mathcal{O}}
```

45. deleted, following `m}}}\operatorname{Hom}_{\handwritten{\mathcal{O}}_{S`:

```tex
\deleted{\unsure{T}}
```

46. handwritten, following `l{O}}_{S\deleted{\unsure{T}}}\text{-}\mathrm{Mod.}}(`:

```tex
\handwritten{\mathcal{E}\otimes}
```

47. handwritten, following `{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

48. handwritten, following `en{\mathcal{E}\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

49. deleted, following `dwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T,`:

```tex
\deleted{\unsure{(}}
```

50. handwritten, following `}_S}\handwritten{\mathcal{O}}_T,\deleted{\unsure{(}}`:

```tex
\handwritten{\mathcal{F}\otimes}
```

51. handwritten, following `eleted{\unsure{(}}\handwritten{\mathcal{F}\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

52. handwritten, following `en{\mathcal{F}\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

53. deleted, following `ndwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T`:

```tex
\deleted{\unsure{)}}
```

54. inserted, following `S}\handwritten{\mathcal{O}}_T\deleted{\unsure{)}}$, `:

```tex
\inserted{\handwritten{$\text{i.e.}\quad \mathcal{H}om_{\underline{O}_S}(\mathbb{V}(\mathcal{F}),\mathbb{V}(\mathcal{E}))\simeq\mathcal{H}om_{\underline{O}_S}(\mathbb{W}(\mathcal{E}),\mathbb{W}(\mathcal{F})).$}}
```

55. handwritten, following `tten{\mathcal{O}}_T\deleted{\unsure{)}}$, \inserted{`:

```tex
\handwritten{$\text{i.e.}\quad \mathcal{H}om_{\underline{O}_S}(\mathbb{V}(\mathcal{F}),\mathbb{V}(\mathcal{E}))\simeq\mathcal{H}om_{\underline{O}_S}(\mathbb{W}(\mathcal{E}),\mathbb{W}(\mathcal{F})).$}
```

56. margin, following `mathbb{W}(\mathcal{E}),\mathbb{W}(\mathcal{F})).$}} `:

```tex
\margin{\handwritten{\unsure{vu}}}
```

57. handwritten, following `}(\mathcal{E}),\mathbb{W}(\mathcal{F})).$}} \margin{`:

```tex
\handwritten{\unsure{vu}}
```

58. handwritten, following `semble des morphismes de $S$-foncteurs de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

59. deleted, following `oncteurs de $X$ dans $\handwritten{\mathcal{H}om}_S(`:

```tex
\deleted{\handwritten{\unsure{\mathbb{V}|W}}}
```

60. handwritten, following `de $X$ dans $\handwritten{\mathcal{H}om}_S(\deleted{`:

```tex
\handwritten{\unsure{\mathbb{V}|W}}
```

61. handwritten, following `}om}_S(\deleted{\handwritten{\unsure{\mathbb{V}|W}}}`:

```tex
\handwritten{\mathbb{V}}
```

62. handwritten, following `ten{\unsure{\mathbb{V}|W}}}\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

63. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

64. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

65. inserted, following `handwritten{\mathcal{E}}))$ est en correspondance bi`:

```tex
\inserted{\handwritten{un}}
```

66. handwritten, following `n{\mathcal{E}}))$ est en correspondance bi\inserted{`:

```tex
\handwritten{un}
```

67. handwritten, following `handwritten{un}}nivoque avec $\operatorname{Hom}_S(X`:

```tex
\handwritten{\times}
```

68. handwritten, following `e avec $\operatorname{Hom}_S(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

69. handwritten, following `}_S(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

70. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

71. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

72. handwritten, following `semble des morphismes de $S$-foncteurs de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

73. handwritten, following `foncteurs de $X$ dans $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

74. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

75. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

76. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

77. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

78. handwritten, following `que avec un sous-ensemble de $\operatorname{Hom}_S(X`:

```tex
\handwritten{\times}
```

79. handwritten, following `ble de $\operatorname{Hom}_S(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

80. handwritten, following `}_S(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

81. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

82. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

83. handwritten, following `V}}(\handwritten{\mathcal{E}}))=\operatorname{Hom}_{`:

```tex
\handwritten{\mathcal{O}}
```

84. handwritten, following `{O}}_S\text{-}\unsure{\mathrm{Mod.}|\mathrm{Mod;}}}(`:

```tex
\handwritten{\mathcal{E}}
```

85. handwritten, following `hrm{Mod.}|\mathrm{Mod;}}}(\handwritten{\mathcal{E}},`:

```tex
\handwritten{\mathcal{A}}
```

86. handwritten, following `handwritten{\mathcal{E}},\handwritten{\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

87. handwritten, following `}},\handwritten{\mathcal{A}}(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

88. handwritten, following `A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

89. handwritten, following `$-préschéma quasi-compact quasi-séparé sur $S$, $f:X`:

```tex
\handwritten{\to}
```

90. handwritten, following `, $f:X\handwritten{\to}S$ le morphisme structural, $`:

```tex
\handwritten{\mathcal{E}}
```

91. handwritten, following `rphisme structural, $\handwritten{\mathcal{E}}$ et $`:

```tex
\handwritten{\mathcal{F}}
```

92. handwritten, following `{\mathcal{E}}$ et $\handwritten{\mathcal{F}}$ deux $`:

```tex
\handwritten{\mathcal{O}}
```

93. deleted, following `{O}}_S$-Modules quasi-cohérents. On suppose vérifiée`:

```tex
\deleted{s}
```

94. handwritten, following `suivantes :}  \uline{a) $f$ est affine}  \uline{b) $`:

```tex
\handwritten{\mathcal{F}}
```

95. handwritten, following `\uline{b) $\handwritten{\mathcal{F}}$ est plat sur $`:

```tex
\handwritten{\mathcal{O}}
```

96. margin, following `r $\handwritten{\mathcal{O}}_S$.}  \uline{Alors :}  `:

```tex
\margin{\handwritten{\begin{tikzpicture}\draw (0,0) ellipse (.45 and .65);\node at (0,0) {5};\end{tikzpicture}}}
```

97. handwritten, following `written{\mathcal{O}}_S$.}  \uline{Alors :}  \margin{`:

```tex
\handwritten{\begin{tikzpicture}\draw (0,0) ellipse (.45 and .65);\node at (0,0) {5};\end{tikzpicture}}
```

98. handwritten, following `tikzpicture}}} \uline{i) l'homomorphisme canonique $`:

```tex
\handwritten{\varphi:\mathcal{A}}
```

99. handwritten, following `isme canonique $\handwritten{\varphi:\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

100. handwritten, following `itten{\varphi:\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

101. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}}
```

102. handwritten, following `handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}}(`:

```tex
\handwritten{\mathcal{F}}
```

103. handwritten, following `}\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})`:

```tex
\handwritten{\longrightarrow\mathcal{A}}
```

104. handwritten, following `thcal{F}})\handwritten{\longrightarrow\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

105. handwritten, following `{\longrightarrow\mathcal{A}}(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

106. handwritten, following `A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

107. handwritten, following `andwritten{\mathcal{F}}))$ est un isomorphisme (où $`:

```tex
\handwritten{\mathbb{S}}
```

108. handwritten, following `$ est un isomorphisme (où $\handwritten{\mathbb{S}}(`:

```tex
\handwritten{\mathcal{F}}
```

109. handwritten, following `ten{\mathcal{F}})$ désigne l'Algèbre symétrique de $`:

```tex
\handwritten{\mathcal{F}}
```

110. handwritten, following `semble des morphismes de $S$-foncteurs de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

111. handwritten, following `foncteurs de $X$ dans $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

112. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

113. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

114. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

115. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

116. handwritten, following `correspondance biunivoque avec $\operatorname{Hom}_{`:

```tex
\handwritten{\mathcal{O}}
```

117. handwritten, following `_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod.}}(`:

```tex
\handwritten{\mathcal{E}}
```

118. handwritten, following `text{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}}\ ,\ `:

```tex
\handwritten{\mathcal{A}}
```

119. handwritten, following `ritten{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes\mathcal{F}}
```

120. handwritten, following `près (11.1, a) et b)), il suffit de montrer que si $`:

```tex
\handwritten{\mathcal{F}}
```

121. handwritten, following `er que si $\handwritten{\mathcal{F}}$ est plat sur $`:

```tex
\handwritten{\mathcal{O}}
```

122. deleted, following ` plat sur $\handwritten{\mathcal{O}}_{\mathbb{S}}$, `:

```tex
\deleted{\unsure{il en est de même de} $\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})$}
```

123. handwritten, following `athbb{S}}$, \deleted{\unsure{il en est de même de} $`:

```tex
\handwritten{\mathbb{S}}
```

124. handwritten, following `ure{il en est de même de} $\handwritten{\mathbb{S}}(`:

```tex
\handwritten{\mathcal{F}}
```

125. handwritten, following `ten{\mathbb{S}}(\handwritten{\mathcal{F}})$} alors $`:

```tex
\handwritten{\mathbb{V}}
```

126. handwritten, following `ten{\mathcal{F}})$} alors $\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```


## Scan 45

Start (UTC): 2026-11-13T20:06:47.126075+00:00

End (UTC): 2026-11-13T20:08:00.762754+00:00

Crop-first words/accents: « il suffit de voir », inserted « il en est de même de », cancelled « résulte des définitions (EGA II 1.7.1), compte tenu d' », handwritten « est un corollaire d' », « un resultat dû à Daniel LAZARD », « suivant lequel toute limite inductive de modules plats est un module plat » with the indicated deletion, handwritten « sur un anneau est une limite inductive filtrante de modules libres de type fini ». « resultat » has no accent. Cancelled « Remarquons de plus », « d'après », « homomorphisme canonique », « est injectif ». Main text: « Montrons maintenant ii) », « Soit », « lui correspond », « tel que si rho est une S-section », « corresponde à », « Mais puisque », « se factorise à travers », « pour chaque S-section », « diagramme commutatif », « peut être considéré », « Réciproquement », « Pour tout S-préschéma », « toute T-section », « correspond à », « ce qui prouve ». Acute accents: résulte, définitions, considéré, Réciproquement, préschéma; grave à/après; circumflex même/dû/être. The marginal eta=? is circled. The diagram has a comma at lower right. The last live Hom has E then F, unlike preceding F then E. The cancelled corollary starts « Corollaire 11.6.- Soit G un S-groupe plat quasi-compact quasi-séparé sur S, tel que » and ends « l'ensemble des applications linéaires »; x-overprinting makes portions tentative.


Read the top correction and the two cancelled passages again at enlargement, followed by the complete proof in both lower crops. « resultat » has no acute accent; « corresponde » has a final e; the section letter after « si » is the round-headed descending rho, retained rather than replaced by eta. The handwritten addition reads « sur un anneau est une limite inductive filtrante de modules libres de type fini. » The S in the insertion, the cancelled paragraph, all proof formulas and the diagram has the same doubled bowl construction seen on the clearer scan-44 S; changed the provisional fraktur reading to mathbb throughout this page. A/a remains explicitly ambiguous at its first occurrence, including its occurrence inside deletion. V has parallel strokes, E/F retain distinct loop/crossbar shapes; the Hom subscript S in the converse is doubly struck. The alternative alpha/d in the converse remains, since the ascender there differs from the other alpha shapes. No i/j indices occur. Checked all O_S and O_T bases and the subscript of each identity, including the unbased tensor in the diagram and the O_T at the end of the last identity subscript. Diagram: E→A(X)⊗SF labelled rho; E→SF; A(X)⊗SF→F; A(X)⊗SF→SF diagonally down-left labelled A(eta)⊗id; F→SF points left. No extra arrow label supplied. Its following handwritten comma is present. The final live Hom has V(E),V(F), in that order. The question mark stays inside the eta=? margin note. Bottom cancelled heading, assumptions and final « applications linéaires » were reread beneath x overstrikes; the less legible local deletions retain doubts. All other readings unchanged.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
unsure{\
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
}|\mathcal{S}
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
frak
->
bb
```


### Every delimited formula, in page-file order

1. inline

```tex
\handwritten{\mathcal{F}}
```

2. inline

```tex
\handwritten{\mathcal{O}}_S
```

3. inline

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

4. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}=\handwritten{\mathbb{S}}(\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}})
```

5. inline

```tex
\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}\longrightarrow}\deleted{\handwritten{\unsure{\mathbb{S}|(}}}\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}\deleted{\unsure{)}}
```

6. inline

```tex
\handwritten{\alpha}
```

7. inline

```tex
S
```

8. inline

```tex
X
```

9. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

10. inline

```tex
\handwritten{\rho}
```

11. inline

```tex
\handwritten{\mathcal{O}}_S
```

12. inline

```tex
\handwritten{\mathcal{E}}
```

13. inline

```tex
\handwritten{\mathcal{A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}))=\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}}(\handwritten{\mathcal{F}})
```

14. inline

```tex
\handwritten{\rho}
```

15. inline

```tex
S
```

16. inline

```tex
X
```

17. display

```tex
(\handwritten{\mathcal{A}(\eta)\otimes}\operatorname{id}_{\handwritten{\mathbb{S}\mathcal{F}}})\handwritten{\circ\rho}:\handwritten{\mathcal{E}\longrightarrow\mathcal{O}}_S\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}=\mathbb{S}\mathcal{F}}
```

18. inline

```tex
\handwritten{\alpha(\eta)}
```

19. inline

```tex
\handwritten{\alpha(\eta)\in}\deleted{\handwritten{\unsure{\mathcal{E}|\mathcal{H}om}}}\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))(S)
```

20. inline

```tex
\handwritten{\mathcal{A}(\eta)\otimes}\operatorname{id}_{\handwritten{\mathbb{S}\mathcal{F}}}
```

21. inline

```tex
\handwritten{\mathcal{F}\to\mathbb{S}\mathcal{F}}
```

22. inline

```tex
S
```

23. inline

```tex
\handwritten{\eta}
```

24. inline

```tex
X
```

25. inline

```tex
\eta={?}
```

26. inline

```tex
\handwritten{\rho}
```

27. inline

```tex
\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}\longrightarrow\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}
```

28. inline

```tex
\handwritten{\rho}
```

29. inline

```tex
\handwritten{\mathcal{O}}_S
```

30. inline

```tex
\handwritten{\mathcal{E}}
```

31. inline

```tex
\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}}
```

32. inline

```tex
\handwritten{\rho\in}\operatorname{Hom}_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}})\handwritten{\subset}\operatorname{Hom}_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod}}(\handwritten{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}})))
```

33. inline

```tex
\handwritten{\alpha}
```

34. inline

```tex
X
```

35. inline

```tex
\handwritten{\mathcal{H}om}_{\mathbb{S}}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

36. inline

```tex
S
```

37. inline

```tex
T
```

38. inline

```tex
T
```

39. inline

```tex
\handwritten{\eta}
```

40. inline

```tex
X\handwritten{\times}_S T
```

41. inline

```tex
\handwritten{\alpha(\eta)}
```

42. inline

```tex
\handwritten{\mathcal{A}(\eta)\otimes}\operatorname{id}_{\handwritten{\mathbb{S}\mathcal{F}\otimes\mathcal{O}}_T}
```

43. inline

```tex
\handwritten{\mathcal{E}\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T
```

44. inline

```tex
\handwritten{\mathcal{F}\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T
```

45. inline

```tex
\handwritten{\unsure{\alpha|d}(\eta)\in\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))(T)
```

46. inline

```tex
\handwritten{\alpha}
```

47. inline

```tex
X
```

48. inline

```tex
\handwritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}))
```

49. inline

```tex
G
```

50. inline

```tex
S
```

51. inline

```tex
S
```

52. inline

```tex
\handwritten{\mathcal{A}}(G)
```

53. inline

```tex
\handwritten{\mathcal{O}}_S
```

54. inline

```tex
\handwritten{\mathcal{E}}
```

55. inline

```tex
\handwritten{\mathcal{O}}_S
```

Diagram 1, all nodes/arrows/labels:

```tex
\begin{tikzcd}[ampersand replacement=\&]
\mathcal{E}\arrow[r,"\rho"]\arrow[d] \& \mathcal{A}(X)\otimes\mathbb{S}\mathcal{F}\arrow[d]\arrow[dl,"\mathcal{A}(\eta)\otimes\operatorname{id}"']\\
\mathbb{S}\mathcal{F} \& \mathcal{F}\arrow[l]
\end{tikzcd}
```

### Every i/j index occurrence (local TeX contexts)

None.

### Handwritten and correction placements

1. handwritten, following `\scanpage{45} \mspage{`:

```tex
\handwritten{13}
```

2. handwritten, following `\mspage{\handwritten{13}} il suffit de voir que si $`:

```tex
\handwritten{\mathcal{F}}
```

3. handwritten, following `ir que si $\handwritten{\mathcal{F}}$ est plat sur $`:

```tex
\handwritten{\mathcal{O}}
```

4. inserted, following `al{F}}$ est plat sur $\handwritten{\mathcal{O}}_S$, `:

```tex
\inserted{il en est de même de $\handwritten{\mathbb{S}\mathcal{F}}$}
```

5. handwritten, following `en{\mathcal{O}}_S$, \inserted{il en est de même de $`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

6. deleted, following `me de $\handwritten{\mathbb{S}\mathcal{F}}$} ce qui `:

```tex
\deleted{résulte des définitions (EGA II 1.7.1), compte tenu d'}
```

7. inserted, following `ulte des définitions (EGA II 1.7.1), compte tenu d'}`:

```tex
\inserted{\handwritten{est un corollaire d'}}
```

8. handwritten, following `éfinitions (EGA II 1.7.1), compte tenu d'}\inserted{`:

```tex
\handwritten{est un corollaire d'}
```

9. deleted, following `}un resultat dû à Daniel LAZARD, suivant lequel tout`:

```tex
\deleted{e limite inductive de modules plats est un}
```

10. deleted, following `imite inductive de modules plats est un} module plat`:

```tex
\deleted{.}
```

11. inserted, following `ive de modules plats est un} module plat\deleted{.} `:

```tex
\inserted{\handwritten{sur un anneau est une limite inductive filtrante de modules libres de type fini.}}
```

12. handwritten, following `ules plats est un} module plat\deleted{.} \inserted{`:

```tex
\handwritten{sur un anneau est une limite inductive filtrante de modules libres de type fini.}
```

13. deleted, following `uctive filtrante de modules libres de type fini.}}  `:

```tex
\deleted{Remarquons de plus que $\handwritten{\unsure{\mathcal{A}|a}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}=\handwritten{\mathbb{S}}(\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}})$ d'après (EGA II 1.1.2), ce qui montre que l'homomorphisme canonique $\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}\longrightarrow}\deleted{\handwritten{\unsure{\mathbb{S}|(}}}\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}\deleted{\unsure{)}}$ est injectif.}
```

14. handwritten, following `s de type fini.}}  \deleted{Remarquons de plus que $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

15. handwritten, following `de plus que $\handwritten{\unsure{\mathcal{A}|a}}(X)`:

```tex
\handwritten{\otimes}
```

16. handwritten, following `en{\unsure{\mathcal{A}|a}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

17. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

18. handwritten, following `{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}=`:

```tex
\handwritten{\mathbb{S}}
```

19. handwritten, following `ten{\mathbb{S}\mathcal{F}}=\handwritten{\mathbb{S}}(`:

```tex
\handwritten{\mathcal{A}}
```

20. handwritten, following `handwritten{\mathbb{S}}(\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

21. handwritten, following `(\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

22. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{F}}
```

23. handwritten, following `.1.2), ce qui montre que l'homomorphisme canonique $`:

```tex
\handwritten{\mathcal{A}}
```

24. handwritten, following `omomorphisme canonique $\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

25. handwritten, following `$\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

26. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{F}\longrightarrow}
```

27. deleted, following `thcal{O}}_S}\handwritten{\mathcal{F}\longrightarrow}`:

```tex
\deleted{\handwritten{\unsure{\mathbb{S}|(}}}
```

28. handwritten, following `_S}\handwritten{\mathcal{F}\longrightarrow}\deleted{`:

```tex
\handwritten{\unsure{\mathbb{S}|(}}
```

29. handwritten, following `tarrow}\deleted{\handwritten{\unsure{\mathbb{S}|(}}}`:

```tex
\handwritten{\mathcal{A}}
```

30. handwritten, following `{\unsure{\mathbb{S}|(}}}\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

31. handwritten, following `}\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

32. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

33. deleted, following `n{\mathcal{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}`:

```tex
\deleted{\unsure{)}}
```

34. handwritten, following `)}}$ est injectif.}  Montrons maintenant ii). Soit $`:

```tex
\handwritten{\alpha}
```

35. handwritten, following `\alpha}$ un morphisme de $S$-foncteurs de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

36. handwritten, following `foncteurs de $X$ dans $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

37. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

38. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

39. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

40. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

41. handwritten, following `mathcal{E}}))$; il lui correspond un homomorphisme $`:

```tex
\handwritten{\rho}
```

42. handwritten, following `orrespond un homomorphisme $\handwritten{\rho}$ de $`:

```tex
\handwritten{\mathcal{O}}
```

43. handwritten, following `\rho}$ de $\handwritten{\mathcal{O}}_S$-Modules de $`:

```tex
\handwritten{\mathcal{E}}
```

44. handwritten, following `O}}_S$-Modules de $\handwritten{\mathcal{E}}$ dans $`:

```tex
\handwritten{\mathcal{A}}
```

45. handwritten, following `tten{\mathcal{E}}$ dans $\handwritten{\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

46. handwritten, following `s $\handwritten{\mathcal{A}}(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

47. handwritten, following `A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

48. handwritten, following `handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}))=`:

```tex
\handwritten{\mathcal{A}}
```

49. handwritten, following `dwritten{\mathcal{F}}))=\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

50. handwritten, following `=\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

51. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}}
```

52. handwritten, following `handwritten{\mathcal{O}}_S}\handwritten{\mathbb{S}}(`:

```tex
\handwritten{\mathcal{F}}
```

53. handwritten, following `\mathbb{S}}(\handwritten{\mathcal{F}})$ tel que si $`:

```tex
\handwritten{\rho}
```

54. handwritten, following `o}$ est une $S$-section de $X$, l'homomorphisme \[ (`:

```tex
\handwritten{\mathcal{A}(\eta)\otimes}
```

55. handwritten, following `written{\mathcal{A}(\eta)\otimes}\operatorname{id}_{`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

56. handwritten, following `ratorname{id}_{\handwritten{\mathbb{S}\mathcal{F}}})`:

```tex
\handwritten{\circ\rho}
```

57. handwritten, following `ten{\mathbb{S}\mathcal{F}}})\handwritten{\circ\rho}:`:

```tex
\handwritten{\mathcal{E}\longrightarrow\mathcal{O}}
```

58. handwritten, following `handwritten{\mathcal{E}\longrightarrow\mathcal{O}}_S`:

```tex
\handwritten{\otimes}
```

59. handwritten, following `\longrightarrow\mathcal{O}}_S\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

60. handwritten, following `S\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}\mathcal{F}=\mathbb{S}\mathcal{F}}
```

61. handwritten, following `mathcal{F}=\mathbb{S}\mathcal{F}} \] corresponde à $`:

```tex
\handwritten{\alpha(\eta)}
```

62. handwritten, following `ponde à $\handwritten{\alpha(\eta)}$. Mais puisque $`:

```tex
\handwritten{\alpha(\eta)\in}
```

63. deleted, following `\eta)}$. Mais puisque $\handwritten{\alpha(\eta)\in}`:

```tex
\deleted{\handwritten{\unsure{\mathcal{E}|\mathcal{H}om}}}
```

64. handwritten, following `Mais puisque $\handwritten{\alpha(\eta)\in}\deleted{`:

```tex
\handwritten{\unsure{\mathcal{E}|\mathcal{H}om}}
```

65. handwritten, following `ed{\handwritten{\unsure{\mathcal{E}|\mathcal{H}om}}}`:

```tex
\handwritten{\mathcal{H}om}
```

66. handwritten, following `cal{E}|\mathcal{H}om}}}\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

67. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

68. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

69. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

70. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

71. handwritten, following `itten{\mathbb{V}}(\handwritten{\mathcal{E}}))(S)$, $`:

```tex
\handwritten{\mathcal{A}(\eta)\otimes}
```

72. handwritten, following `written{\mathcal{A}(\eta)\otimes}\operatorname{id}_{`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

73. handwritten, following `orise à travers l'homomorphisme canonique injectif $`:

```tex
\handwritten{\mathcal{F}\to\mathbb{S}\mathcal{F}}
```

74. handwritten, following `}\mathcal{F}}$. On a donc, pour chaque $S$-section $`:

```tex
\handwritten{\eta}
```

75. handwritten, following ` pour chaque $S$-section $\handwritten{\eta}$ de $X$`:

```tex
\handwritten{,}
```

76. margin, following `ta}$ de $X$\handwritten{,}un diagramme commutatif : `:

```tex
\margin{\handwritten{\begin{tikzpicture}
\draw (0,0) ellipse (.7 and 1.15);
\node at (0,0) {$\eta={?}$};
\end{tikzpicture}}}
```

77. handwritten, following `$X$\handwritten{,}un diagramme commutatif : \margin{`:

```tex
\handwritten{\begin{tikzpicture}
\draw (0,0) ellipse (.7 and 1.15);
\node at (0,0) {$\eta={?}$};
\end{tikzpicture}}
```

78. handwritten, following `at (0,0) {$\eta={?}$}; \end{tikzpicture}}} \diagram{`:

```tex
\handwritten{\begin{tikzcd}[ampersand replacement=\&]
\mathcal{E}\arrow[r,"\rho"]\arrow[d] \& \mathcal{A}(X)\otimes\mathbb{S}\mathcal{F}\arrow[d]\arrow[dl,"\mathcal{A}(\eta)\otimes\operatorname{id}"']\\
\mathbb{S}\mathcal{F} \& \mathcal{F}\arrow[l]
\end{tikzcd}}
```

79. handwritten, following `}\mathcal{F} \& \mathcal{F}\arrow[l] \end{tikzcd}}} `:

```tex
\handwritten{,}
```

80. handwritten, following ` \end{tikzcd}}} \handwritten{,}  ce qui montre que $`:

```tex
\handwritten{\rho}
```

81. handwritten, following `orise à travers l'homomorphisme canonique injectif $`:

```tex
\handwritten{\mathcal{A}}
```

82. handwritten, following `sme canonique injectif $\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

83. handwritten, following `$\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

84. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{F}\longrightarrow\mathcal{A}}
```

85. handwritten, following `andwritten{\mathcal{F}\longrightarrow\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

86. handwritten, following `longrightarrow\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

87. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathbb{S}\mathcal{F}}
```

88. handwritten, following `{O}}_S}\handwritten{\mathbb{S}\mathcal{F}}$ , donc $`:

```tex
\handwritten{\rho}
```

89. handwritten, following `ho}$ peut être considéré comme un homomorphisme de $`:

```tex
\handwritten{\mathcal{O}}
```

90. handwritten, following `phisme de $\handwritten{\mathcal{O}}_S$-Modules de $`:

```tex
\handwritten{\mathcal{E}}
```

91. handwritten, following `O}}_S$-Modules de $\handwritten{\mathcal{E}}$ dans $`:

```tex
\handwritten{\mathcal{A}}
```

92. handwritten, following `ten{\mathcal{E}}$ dans $\handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

93. handwritten, following `$\handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

94. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{F}}
```

95. handwritten, following `\handwritten{\mathcal{F}}$ .  Réciproquement, soit $`:

```tex
\handwritten{\rho\in}
```

96. handwritten, following `ent, soit $\handwritten{\rho\in}\operatorname{Hom}_{`:

```tex
\handwritten{\mathcal{O}}
```

97. handwritten, following `_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod.}}(`:

```tex
\handwritten{\mathcal{E}}
```

98. handwritten, following `text{-}\mathrm{Mod.}}(\handwritten{\mathcal{E}}\ ,\ `:

```tex
\handwritten{\mathcal{A}}
```

99. handwritten, following `ritten{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X)`:

```tex
\handwritten{\otimes}
```

100. handwritten, following ` \handwritten{\mathcal{A}}(X)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

101. handwritten, following `)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{F}}
```

102. handwritten, following `andwritten{\mathcal{O}}_S}\handwritten{\mathcal{F}})`:

```tex
\handwritten{\subset}
```

103. handwritten, following `athcal{F}})\handwritten{\subset}\operatorname{Hom}_{`:

```tex
\handwritten{\mathcal{O}}
```

104. handwritten, following `}_{\handwritten{\mathcal{O}}_S\text{-}\mathrm{Mod}}(`:

```tex
\handwritten{\mathcal{E}}
```

105. handwritten, following `\text{-}\mathrm{Mod}}(\handwritten{\mathcal{E}}\ ,\ `:

```tex
\handwritten{\mathcal{A}}
```

106. handwritten, following `written{\mathcal{E}}\ ,\ \handwritten{\mathcal{A}}(X`:

```tex
\handwritten{\times}
```

107. handwritten, following `,\ \handwritten{\mathcal{A}}(X\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

108. handwritten, following `A}}(X\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

109. handwritten, following `{\mathcal{F}})))$ ; il lui correspond un morphisme $`:

```tex
\handwritten{\alpha}
```

110. handwritten, following `nd un morphisme $\handwritten{\alpha}$ de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

111. handwritten, following ` $X$ dans $\handwritten{\mathcal{H}om}_{\mathbb{S}}(`:

```tex
\handwritten{\mathbb{V}}
```

112. handwritten, following `mathcal{H}om}_{\mathbb{S}}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

113. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

114. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

115. handwritten, following `. Pour tout $S$-préschéma $T$ et toute $T$-section $`:

```tex
\handwritten{\eta}
```

116. handwritten, following ` $T$ et toute $T$-section $\handwritten{\eta}$ de $X`:

```tex
\handwritten{\times}
```

117. handwritten, following `andwritten{\eta}$ de $X\handwritten{\times}_S T$ , $`:

```tex
\handwritten{\alpha(\eta)}
```

118. handwritten, following `}_S T$ , $\handwritten{\alpha(\eta)}$ correspond à $`:

```tex
\handwritten{\mathcal{A}(\eta)\otimes}
```

119. handwritten, following `written{\mathcal{A}(\eta)\otimes}\operatorname{id}_{`:

```tex
\handwritten{\mathbb{S}\mathcal{F}\otimes\mathcal{O}}
```

120. handwritten, following `thcal{F}\otimes\mathcal{O}}_T}$ , homomorphisme de $`:

```tex
\handwritten{\mathcal{E}\otimes}
```

121. handwritten, following `homomorphisme de $\handwritten{\mathcal{E}\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

122. handwritten, following `en{\mathcal{E}\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

123. handwritten, following `n{\mathcal{O}}_S}\handwritten{\mathcal{O}}_T$ dans $`:

```tex
\handwritten{\mathcal{F}\otimes}
```

124. handwritten, following `hcal{O}}_T$ dans $\handwritten{\mathcal{F}\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

125. handwritten, following `en{\mathcal{F}\otimes}_{\handwritten{\mathcal{O}}_S}`:

```tex
\handwritten{\mathcal{O}}
```

126. handwritten, following `\mathcal{O}}_S}\handwritten{\mathcal{O}}_T$ , donc $`:

```tex
\handwritten{\unsure{\alpha|d}(\eta)\in\mathcal{H}om}
```

127. handwritten, following `ndwritten{\unsure{\alpha|d}(\eta)\in\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

128. handwritten, following `eta)\in\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

129. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

130. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{F}}),`:

```tex
\handwritten{\mathbb{V}}
```

131. handwritten, following `\handwritten{\mathcal{F}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

132. handwritten, following `\handwritten{\mathcal{E}}))(T)$, ce qui montre que $`:

```tex
\handwritten{\alpha}
```

133. handwritten, following `\handwritten{\alpha}$ est un morphisme de $X$ dans $`:

```tex
\handwritten{\mathcal{H}om}
```

134. handwritten, following `morphisme de $X$ dans $\handwritten{\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

135. handwritten, following `ritten{\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

136. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

137. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}),`:

```tex
\handwritten{\mathbb{V}}
```

138. handwritten, following `\handwritten{\mathcal{E}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{F}}
```

139. deleted, following `}(\handwritten{\mathcal{F}}))$, ce qui prouve ii).  `:

```tex
\deleted{\unsure{Corollaire 11.6.- Soit} $G$ un $S$-groupe plat, quasi-compact et quasi-séparé sur $S$, \unsure{tel que} $\handwritten{\mathcal{A}}(G)$ soit un $\handwritten{\mathcal{O}}_S$-module plat, \deleted{\unsure{et}} $\handwritten{\mathcal{E}}$ un $\handwritten{\mathcal{O}}_S$-Module quasi-cohérent et plat. Alors l'ensemble des applications linéaires}
```

140. handwritten, following `-compact et quasi-séparé sur $S$, \unsure{tel que} $`:

```tex
\handwritten{\mathcal{A}}
```

141. handwritten, following `re{tel que} $\handwritten{\mathcal{A}}(G)$ soit un $`:

```tex
\handwritten{\mathcal{O}}
```

142. deleted, following ` soit un $\handwritten{\mathcal{O}}_S$-module plat, `:

```tex
\deleted{\unsure{et}}
```

143. handwritten, following `\mathcal{O}}_S$-module plat, \deleted{\unsure{et}} $`:

```tex
\handwritten{\mathcal{E}}
```

144. handwritten, following `eleted{\unsure{et}} $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```


## Scan 46

Start (UTC): 2026-11-13T20:08:01.058996+00:00

End (UTC): 2026-11-13T20:10:06.751925+00:00

Crop-first words/accents: « 11.6.- Soient G un S-groupe plat quasi-compact et quasi-séparé », « quasi-cohérent et plat », crossed « Nous dirons qu' », inserted « Notons qu' », « définit une opération », « si » plus inserted « et seulement si », « vérifie les deux conditions suivantes », « désigne le morphisme structural », four instances « est commutatif. » circled with leftward pointers, « section unité », « Il revient au même » plus inserted « alors », « déduit », « deux axiomes », « Si » at CM1 and CM2, « correspondant », « définit une opération », replacement « compar|comparer I 4.2|9.2 », « Par conséquent », « correspondance biunivoque », « opérations », « Lemme 11.7.- Soient G un S-groupe quasi-compact et quasi-séparé » with « plat et » inserted after S. Acute accents in séparé/cohérent/définit/opération/vérifie/désigne/unité/déduit/conséquent; circumflex in même. Script A is round a-shaped; E has two open lobes; double-stroke V and W. CM1 top-left visibly has A⊗A⊗A and bottom-right A; the definition has A(theta), not a visually mu-shaped symbol. No i/j indices. CM2 has eta and O_S. Small manuscript number 14 and archive 45. The final handwritten reference digit needs enlargement before choosing between 4 and 9.


Text and correction audit: read 11.6 word by word, including Soient, the absence of a comma after plat, Notons qu' above the cancellation, End inserted before the cancelled Hom, et seulement si after si, the comma after E, and the later alors and E→ insertions. The four moved « est commutatif. » phrases were already present as insertions, but their ellipses and long leftward pointer curves were absent: those graphic strokes are now reproduced. Added the visibly handwritten overstroke to the initial L of Lemme. The replacement reference retains compar/comparer and now marks its first digit 4|9 after inspecting the enlarged open loop. The roman I has upper and lower serif bars, not a separate numerical exponent. No i/j indices occur.

Alphabet audit: first A(G), the later standalone A, every A in the two algebra diagrams and the A(theta) expression have the same round a-shaped construction; the initial A/a doubt remains. E is visibly different, with two open lobes. In CM1 the last top-left factor and bottom-right object are A-shaped, as the close crop confirms. Theta is an oval crossed horizontally; mu has a downstroke and rising right branch. The CM1 homomorphism really has theta inside A. Epsilon at the unit and in CM2 has the curled epsilon form, retained as varepsilon; eta has a long descending right stroke. V has parallel left strokes. W inside the dark End correction remains doubtful because of retracing. The two O-subscript S glyphs in the opening inserted End and the rho target have doubled impressions; other S letters and heading capitals remain single.

Arrow-by-arrow comparison: diagram 1 top arrow id_G×theta points right, left arrow mu×id_V(E) points down, right and bottom arrows theta point down/right; the cancelled X remains before V in the lower-left object. Diagram 2 has S×_S V(E)→G×_S V(E) with epsilon×id_V(E), the right diagonal theta points down-left, the left diagonal marked sim points from bottom V(E) up-left. CM1 has top id_A⊗rho pointing left, left Delta⊗id_E pointing up, right rho pointing up, bottom rho pointing left. CM2 top eta⊗id_E points left; E→O_S⊗E is up-left with sim; E→A⊗E is up-right with rho. All tensor products in the algebra diagrams are unbased as drawn; product bases in the first two are S. Checked af subscripts and the last inserted plat et before the page continues. Every formula and correction listed below was compared against its visible location.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-.95,-.18) .. controls (-1.45,-.65) and (-5.8,-.55) .. (-6,-.55);}\node at (0,0) {
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
};\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.15,-.08) .. controls (-1.25,-.55) and (-3.6,-.5) .. (-5.6,-.5);}\node at (0,0) {
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
};\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.1,-.22) .. controls (-1.4,-.4) and (-4.5,-.35) .. (-6,-.55);}\node at (0,0) {
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
};\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.25 and .4);\draw[->] (-1.22,-.04) .. controls (-2.2,-.7) and (-4.3,.0) .. (-5.9,-.35);}\node at (0,0) {
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
};\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\unsure{
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
|9}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
}
```


### Every delimited formula, in page-file order

1. inline

```tex
G
```

2. inline

```tex
S
```

3. inline

```tex
S
```

4. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}(G)
```

5. inline

```tex
\handwritten{\mathcal{O}}_S
```

6. inline

```tex
\handwritten{\mathcal{A}}
```

7. inline

```tex
\handwritten{\mathcal{E}}
```

8. inline

```tex
\handwritten{\mathcal{O}}_S
```

9. inline

```tex
S
```

10. inline

```tex
G
```

11. inline

```tex
\inserted{\handwritten{\operatorname{End}_{\mathcal{O}_{\mathbb{S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))}}\deleted{\handwritten{\unsure{\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}}}\handwritten{\simeq\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}),\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}))
```

12. inline

```tex
G
```

13. inline

```tex
\handwritten{\mathcal{E}}
```

14. inline

```tex
\handwritten{\theta}:G\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\handwritten{\longrightarrow\mathbb{V}}(\handwritten{\mathcal{E}})
```

15. inline

```tex
1^\circ)
```

16. inline

```tex
\handwritten{\mu}:G\handwritten{\times}_S G\handwritten{\longrightarrow}G
```

17. inline

```tex
2^\circ)
```

18. inline

```tex
\handwritten{\varepsilon}:S\handwritten{\to}G
```

19. inline

```tex
G
```

20. inline

```tex
\handwritten{\rho}:\inserted{\handwritten{\mathcal{E}\longrightarrow}}\handwritten{\mathcal{A}}(G)\handwritten{\otimes}_{\handwritten{\mathcal{O}}_{\mathbb{S}}}\handwritten{\mathcal{E}}
```

21. inline

```tex
\handwritten{\theta}
```

22. inline

```tex
\mathcal{E}\longrightarrow\mathcal{A}(G)\otimes\mathcal{E}
```

23. inline

```tex
\handwritten{\Delta}:\handwritten{\mathcal{A}\longrightarrow\mathcal{A}\otimes\mathcal{A}}=\handwritten{\mathcal{A}}(G\handwritten{\times}_S G)
```

24. inline

```tex
\handwritten{\mathcal{A}(\theta)}
```

25. inline

```tex
\handwritten{\eta}:\handwritten{\mathcal{A}\to\mathcal{O}}_S
```

26. inline

```tex
\handwritten{\mathcal{A}(\varepsilon)}
```

27. inline

```tex
\handwritten{\theta}_{\mathrm{af}}:G_{\mathrm{af}}\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\handwritten{\longrightarrow\mathbb{V}}(\handwritten{\mathcal{E}})
```

28. inline

```tex
\handwritten{\rho}
```

29. inline

```tex
G_{\mathrm{af}}
```

30. inline

```tex
\handwritten{\mathcal{E}}
```

31. inline

```tex
G
```

32. inline

```tex
\handwritten{\mathcal{E}}
```

33. inline

```tex
G_{\mathrm{af}}
```

34. inline

```tex
\handwritten{\mathcal{E}}
```

35. inline

```tex
G
```

36. inline

```tex
S
```

37. inline

```tex
S
```

38. inline

```tex
\handwritten{\mathcal{A}}(G)
```

Diagram 1, all nodes/arrows/labels:

```tex
\begin{tikzcd}[ampersand replacement=\&]
G\handwritten{\times}_S G\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})
 \arrow[r,"\operatorname{id}_G\handwritten{\times\theta}"]\arrow[d,"\handwritten{\mu\times}\operatorname{id}_{\handwritten{\mathbb{V}(\mathcal{E})}}"']
\& G\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[d,"\handwritten{\theta}"]\\
G\handwritten{\times}_S\deleted{\unsure{X}}\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[r,"\handwritten{\theta}"']
\& \handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})
\end{tikzcd}
```

Diagram 2, all nodes/arrows/labels:

```tex
\begin{tikzcd}[ampersand replacement=\&]
S\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})
 \arrow[rr,"\handwritten{\varepsilon\times}\operatorname{id}_{\handwritten{\mathbb{V}(\mathcal{E})}}"]
\& \& G\handwritten{\times}_S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[dl,"\handwritten{\theta}"]\\
\& \handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[ul,"\handwritten{\sim}"] \&
\end{tikzcd}
```

Diagram 3, all nodes/arrows/labels:

```tex
\begin{tikzcd}[ampersand replacement=\&]
\mathcal{A}\otimes\mathcal{A}\otimes\mathcal{A}
\& \mathcal{A}\otimes\mathcal{E}\arrow[l,"\operatorname{id}_{\mathcal{A}}\otimes\rho"']\\
\mathcal{A}\otimes\mathcal{E}\arrow[u,"\Delta\otimes\operatorname{id}_{\mathcal{E}}"]
\& \mathcal{A}\arrow[u,"\rho"']\arrow[l,"\rho"]
\end{tikzcd}
```

Diagram 4, all nodes/arrows/labels:

```tex
\begin{tikzcd}[ampersand replacement=\&]
\mathcal{O}_S\otimes\mathcal{E}
\& \& \mathcal{A}\otimes\mathcal{E}\arrow[ll,"\eta\otimes\operatorname{id}_{\mathcal{E}}"']\\
\& \mathcal{E}\arrow[ul,"\sim"]\arrow[ur,"\rho"']\&
\end{tikzcd}
```

### Every i/j index occurrence (local TeX contexts)

None.

### Handwritten and correction placements

1. handwritten, following `\scanpage{46} \mspage{`:

```tex
\handwritten{14}
```

2. handwritten, following `plat quasi-compact et quasi-séparé sur $S$ tel que $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

3. handwritten, following ` $\handwritten{\unsure{\mathcal{A}|a}}(G)$ soit un $`:

```tex
\handwritten{\mathcal{O}}
```

4. handwritten, following ` soit un $\handwritten{\mathcal{O}}_S$-Module plat $`:

```tex
\handwritten{\mathcal{A}}
```

5. handwritten, following `O}}_S$-Module plat $\handwritten{\mathcal{A}}$, et $`:

```tex
\handwritten{\mathcal{E}}
```

6. handwritten, following `n{\mathcal{A}}$, et $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```

7. deleted, following `tten{\mathcal{O}}_S$-Module quasi-cohérent et plat. `:

```tex
\deleted{Nous dirons qu'}
```

8. inserted, following `le quasi-cohérent et plat. \deleted{Nous dirons qu'}`:

```tex
\inserted{\handwritten{Notons qu'}}
```

9. handwritten, following `ohérent et plat. \deleted{Nous dirons qu'}\inserted{`:

```tex
\handwritten{Notons qu'}
```

10. inserted, following `ons qu'}}un morphisme de $S$-foncteurs de $G$ dans $`:

```tex
\inserted{\handwritten{\operatorname{End}_{\mathcal{O}_{\mathbb{S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))}}
```

11. handwritten, following `n morphisme de $S$-foncteurs de $G$ dans $\inserted{`:

```tex
\handwritten{\operatorname{End}_{\mathcal{O}_{\mathbb{S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))}
```

12. deleted, following `_{\mathbb{S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))}}`:

```tex
\deleted{\handwritten{\unsure{\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}}}
```

13. handwritten, following `{S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))}}\deleted{`:

```tex
\handwritten{\unsure{\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}}
```

14. handwritten, following `cal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}}}`:

```tex
\handwritten{\simeq\mathcal{H}om}
```

15. handwritten, following `},\mathcal{E})}}}\handwritten{\simeq\mathcal{H}om}_{`:

```tex
\handwritten{\mathcal{O}}
```

16. handwritten, following `{\simeq\mathcal{H}om}_{\handwritten{\mathcal{O}}_S}(`:

```tex
\handwritten{\mathbb{V}}
```

17. handwritten, following `andwritten{\mathcal{O}}_S}(\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

18. handwritten, following `\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}}),`:

```tex
\handwritten{\mathbb{V}}
```

19. handwritten, following `\handwritten{\mathcal{E}}),\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

20. handwritten, following `al{E}}))$ définit une \uline{opération} de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

21. handwritten, following `ne{opération} de $G$ sur $\handwritten{\mathcal{E}}$`:

```tex
\handwritten{,}
```

22. inserted, following `$ sur $\handwritten{\mathcal{E}}$\handwritten{,} si `:

```tex
\inserted{\handwritten{et seulement si}}
```

23. handwritten, following `ndwritten{\mathcal{E}}$\handwritten{,} si \inserted{`:

```tex
\handwritten{et seulement si}
```

24. handwritten, following `itten{et seulement si}} le morphisme correspondant $`:

```tex
\handwritten{\theta}
```

25. handwritten, following `} le morphisme correspondant $\handwritten{\theta}:G`:

```tex
\handwritten{\times}
```

26. handwritten, following `ondant $\handwritten{\theta}:G\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

27. handwritten, following `ta}:G\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

28. handwritten, following `S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})`:

```tex
\handwritten{\longrightarrow\mathbb{V}}
```

29. handwritten, following `mathcal{E}})\handwritten{\longrightarrow\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

30. handwritten, following `fie les deux conditions suivantes :  $1^\circ)$ si $`:

```tex
\handwritten{\mu}
```

31. handwritten, following `ions suivantes :  $1^\circ)$ si $\handwritten{\mu}:G`:

```tex
\handwritten{\times}
```

32. handwritten, following `rc)$ si $\handwritten{\mu}:G\handwritten{\times}_S G`:

```tex
\handwritten{\longrightarrow}
```

33. handwritten, following ` \diagram{\begin{tikzcd}[ampersand replacement=\&] G`:

```tex
\handwritten{\times}
```

34. handwritten, following `[ampersand replacement=\&] G\handwritten{\times}_S G`:

```tex
\handwritten{\times}
```

35. handwritten, following `=\&] G\handwritten{\times}_S G\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

36. handwritten, following `}_S G\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

37. handwritten, following `written{\mathcal{E}})  \arrow[r,"\operatorname{id}_G`:

```tex
\handwritten{\times\theta}
```

38. handwritten, following `atorname{id}_G\handwritten{\times\theta}"]\arrow[d,"`:

```tex
\handwritten{\mu\times}
```

39. handwritten, following `\arrow[d,"\handwritten{\mu\times}\operatorname{id}_{`:

```tex
\handwritten{\mathbb{V}(\mathcal{E})}
```

40. handwritten, following `{id}_{\handwritten{\mathbb{V}(\mathcal{E})}}"'] \& G`:

```tex
\handwritten{\times}
```

41. handwritten, following `thbb{V}(\mathcal{E})}}"'] \& G\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

42. handwritten, following ` \& G\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

43. handwritten, following `ten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[d,"`:

```tex
\handwritten{\theta}
```

44. handwritten, following `en{\mathcal{E}})\arrow[d,"\handwritten{\theta}"]\\ G`:

```tex
\handwritten{\times}
```

45. deleted, following `[d,"\handwritten{\theta}"]\\ G\handwritten{\times}_S`:

```tex
\deleted{\unsure{X}}
```

46. handwritten, following `eta}"]\\ G\handwritten{\times}_S\deleted{\unsure{X}}`:

```tex
\handwritten{\mathbb{V}}
```

47. handwritten, following `imes}_S\deleted{\unsure{X}}\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

48. handwritten, following `ten{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[r,"`:

```tex
\handwritten{\theta}
```

49. handwritten, following `n{\mathcal{E}})\arrow[r,"\handwritten{\theta}"'] \& `:

```tex
\handwritten{\mathbb{V}}
```

50. handwritten, following `\handwritten{\theta}"'] \& \handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

51. inserted, following `mathbb{V}}(\handwritten{\mathcal{E}}) \end{tikzcd}} `:

```tex
\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-.95,-.18) .. controls (-1.45,-.65) and (-5.8,-.55) .. (-6,-.55);}\node at (0,0) {est commutatif.};\end{tikzpicture}}}
```

52. handwritten, following `} \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]`:

```tex
\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-.95,-.18) .. controls (-1.45,-.65) and (-5.8,-.55) .. (-6,-.55);}
```

53. handwritten, following `st commutatif.};\end{tikzpicture}}}  $2^\circ)$ si $`:

```tex
\handwritten{\varepsilon}
```

54. handwritten, following `cture}}}  $2^\circ)$ si $\handwritten{\varepsilon}:S`:

```tex
\handwritten{\to}
```

55. handwritten, following ` \diagram{\begin{tikzcd}[ampersand replacement=\&] S`:

```tex
\handwritten{\times}
```

56. handwritten, following `d}[ampersand replacement=\&] S\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

57. handwritten, following `\&] S\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

58. handwritten, following `{\mathbb{V}}(\handwritten{\mathcal{E}})  \arrow[rr,"`:

```tex
\handwritten{\varepsilon\times}
```

59. handwritten, following `,"\handwritten{\varepsilon\times}\operatorname{id}_{`:

```tex
\handwritten{\mathbb{V}(\mathcal{E})}
```

60. handwritten, following `d}_{\handwritten{\mathbb{V}(\mathcal{E})}}"] \& \& G`:

```tex
\handwritten{\times}
```

61. handwritten, following `bb{V}(\mathcal{E})}}"] \& \& G\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

62. handwritten, following ` \& G\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

63. handwritten, following `en{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[dl,"`:

```tex
\handwritten{\theta}
```

64. handwritten, following `\mathcal{E}})\arrow[dl,"\handwritten{\theta}"]\\ \& `:

```tex
\handwritten{\mathbb{V}}
```

65. handwritten, following `handwritten{\theta}"]\\ \& \handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

66. handwritten, following `en{\mathbb{V}}(\handwritten{\mathcal{E}})\arrow[ul,"`:

```tex
\handwritten{\sim}
```

67. inserted, following `}})\arrow[ul,"\handwritten{\sim}"] \& \end{tikzcd}} `:

```tex
\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.15,-.08) .. controls (-1.25,-.55) and (-3.6,-.5) .. (-5.6,-.5);}\node at (0,0) {est commutatif.};\end{tikzpicture}}}
```

68. handwritten, following `} \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]`:

```tex
\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.15,-.08) .. controls (-1.25,-.55) and (-3.6,-.5) .. (-5.6,-.5);}
```

69. inserted, following `0) {est commutatif.};\end{tikzpicture}}}  Il revient`:

```tex
\inserted{\handwritten{alors}}
```

70. handwritten, following `mmutatif.};\end{tikzpicture}}}  Il revient\inserted{`:

```tex
\handwritten{alors}
```

71. handwritten, following `ndwritten{alors}} au même de dire que le morphisme $`:

```tex
\handwritten{\rho}
```

72. inserted, following `u même de dire que le morphisme $\handwritten{\rho}:`:

```tex
\inserted{\handwritten{\mathcal{E}\longrightarrow}}
```

73. handwritten, following `dire que le morphisme $\handwritten{\rho}:\inserted{`:

```tex
\handwritten{\mathcal{E}\longrightarrow}
```

74. handwritten, following `:\inserted{\handwritten{\mathcal{E}\longrightarrow}}`:

```tex
\handwritten{\mathcal{A}}
```

75. handwritten, following `hcal{E}\longrightarrow}}\handwritten{\mathcal{A}}(G)`:

```tex
\handwritten{\otimes}
```

76. handwritten, following `}\handwritten{\mathcal{A}}(G)\handwritten{\otimes}_{`:

```tex
\handwritten{\mathcal{O}}
```

77. handwritten, following `en{\otimes}_{\handwritten{\mathcal{O}}_{\mathbb{S}}}`:

```tex
\handwritten{\mathcal{E}}
```

78. handwritten, following `_{\mathbb{S}}}\handwritten{\mathcal{E}}$ déduit de $`:

```tex
\handwritten{\theta}
```

79. margin, following `ritten{\theta}$ vérifie les deux axiomes suivants : `:

```tex
\margin{\handwritten{\begin{tikzpicture}
\draw (0,0) ellipse (1.4 and .6);
\node at (0,0) {$\mathcal{E}\longrightarrow\mathcal{A}(G)\otimes\mathcal{E}$};
\end{tikzpicture}}}
```

80. handwritten, following `theta}$ vérifie les deux axiomes suivants : \margin{`:

```tex
\handwritten{\begin{tikzpicture}
\draw (0,0) ellipse (1.4 and .6);
\node at (0,0) {$\mathcal{E}\longrightarrow\mathcal{A}(G)\otimes\mathcal{E}$};
\end{tikzpicture}}
```

81. handwritten, following `otimes\mathcal{E}$}; \end{tikzpicture}}}  (CM1) Si $`:

```tex
\handwritten{\Delta}
```

82. handwritten, following `\end{tikzpicture}}}  (CM1) Si $\handwritten{\Delta}:`:

```tex
\handwritten{\mathcal{A}\longrightarrow\mathcal{A}\otimes\mathcal{A}}
```

83. handwritten, following `cal{A}\longrightarrow\mathcal{A}\otimes\mathcal{A}}=`:

```tex
\handwritten{\mathcal{A}}
```

84. handwritten, following `al{A}\otimes\mathcal{A}}=\handwritten{\mathcal{A}}(G`:

```tex
\handwritten{\times}
```

85. handwritten, following `}}(G\handwritten{\times}_S G)$ est l'homomorphisme $`:

```tex
\handwritten{\mathcal{A}(\theta)}
```

86. handwritten, following `ritten{\mathcal{A}(\theta)}$, le diagramme \diagram{`:

```tex
\handwritten{\begin{tikzcd}[ampersand replacement=\&]
\mathcal{A}\otimes\mathcal{A}\otimes\mathcal{A}
\& \mathcal{A}\otimes\mathcal{E}\arrow[l,"\operatorname{id}_{\mathcal{A}}\otimes\rho"']\\
\mathcal{A}\otimes\mathcal{E}\arrow[u,"\Delta\otimes\operatorname{id}_{\mathcal{E}}"]
\& \mathcal{A}\arrow[u,"\rho"']\arrow[l,"\rho"]
\end{tikzcd}}
```

87. inserted, following `{A}\arrow[u,"\rho"']\arrow[l,"\rho"] \end{tikzcd}}} `:

```tex
\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.1,-.22) .. controls (-1.4,-.4) and (-4.5,-.35) .. (-6,-.55);}\node at (0,0) {est commutatif.};\end{tikzpicture}}}
```

88. handwritten, following `} \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]`:

```tex
\handwritten{\draw (0,0) ellipse (1.2 and .4);\draw[->] (-1.1,-.22) .. controls (-1.4,-.4) and (-4.5,-.35) .. (-6,-.55);}
```

89. handwritten, following `0) {est commutatif.};\end{tikzpicture}}}  (CM2) Si $`:

```tex
\handwritten{\eta}
```

90. handwritten, following `};\end{tikzpicture}}}  (CM2) Si $\handwritten{\eta}:`:

```tex
\handwritten{\mathcal{A}\to\mathcal{O}}
```

91. handwritten, following `{\mathcal{A}\to\mathcal{O}}_S$ est l'homomorphisme $`:

```tex
\handwritten{\mathcal{A}(\varepsilon)}
```

92. handwritten, following `n{\mathcal{A}(\varepsilon)}$, le diagramme \diagram{`:

```tex
\handwritten{\begin{tikzcd}[ampersand replacement=\&]
\mathcal{O}_S\otimes\mathcal{E}
\& \& \mathcal{A}\otimes\mathcal{E}\arrow[ll,"\eta\otimes\operatorname{id}_{\mathcal{E}}"']\\
\& \mathcal{E}\arrow[ul,"\sim"]\arrow[ur,"\rho"']\&
\end{tikzcd}}
```

93. inserted, following `arrow[ul,"\sim"]\arrow[ur,"\rho"']\& \end{tikzcd}}} `:

```tex
\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\handwritten{\draw (0,0) ellipse (1.25 and .4);\draw[->] (-1.22,-.04) .. controls (-2.2,-.7) and (-4.3,.0) .. (-5.9,-.35);}\node at (0,0) {est commutatif.};\end{tikzpicture}}}
```

94. handwritten, following `} \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]`:

```tex
\handwritten{\draw (0,0) ellipse (1.25 and .4);\draw[->] (-1.22,-.04) .. controls (-2.2,-.7) and (-4.3,.0) .. (-5.9,-.35);}
```

95. handwritten, following `re}}}  Il revient au même de dire que le morphisme $`:

```tex
\handwritten{\theta}
```

96. handwritten, following ` $\handwritten{\theta}_{\mathrm{af}}:G_{\mathrm{af}}`:

```tex
\handwritten{\times}
```

97. handwritten, following `_{\mathrm{af}}:G_{\mathrm{af}}\handwritten{\times}_S`:

```tex
\handwritten{\mathbb{V}}
```

98. handwritten, following `{af}}\handwritten{\times}_S\handwritten{\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

99. handwritten, following `S\handwritten{\mathbb{V}}(\handwritten{\mathcal{E}})`:

```tex
\handwritten{\longrightarrow\mathbb{V}}
```

100. handwritten, following `mathcal{E}})\handwritten{\longrightarrow\mathbb{V}}(`:

```tex
\handwritten{\mathcal{E}}
```

101. handwritten, following `bb{V}}(\handwritten{\mathcal{E}})$ correspondant à $`:

```tex
\handwritten{\rho}
```

102. handwritten, following `o}$ définit une opération de $G_{\mathrm{af}}$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

103. deleted, following `e $G_{\mathrm{af}}$ sur $\handwritten{\mathcal{E}}$ `:

```tex
\deleted{\handwritten{\unsure{(Exp. I)}}}
```

104. handwritten, following `thrm{af}}$ sur $\handwritten{\mathcal{E}}$ \deleted{`:

```tex
\handwritten{\unsure{(Exp. I)}}
```

105. inserted, following `hcal{E}}$ \deleted{\handwritten{\unsure{(Exp. I)}}} `:

```tex
\inserted{\handwritten{(\unsure{compar|comparer} I \unsure{4|9}.2)}}
```

106. handwritten, following `\deleted{\handwritten{\unsure{(Exp. I)}}} \inserted{`:

```tex
\handwritten{(\unsure{compar|comparer} I \unsure{4|9}.2)}
```

107. handwritten, following `respondance biunivoque entre opérations de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

108. handwritten, following `athcal{E}}$ et opérations de $G_{\mathrm{af}}$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

109. handwritten, following `thrm{af}}$ sur $\handwritten{\mathcal{E}}$.  \uline{`:

```tex
\handwritten{L}
```

110. handwritten, following ` un $S$-groupe quasi-compact et quasi-séparé sur $S$`:

```tex
\handwritten{,}
```

111. inserted, following `quasi-compact et quasi-séparé sur $S$\handwritten{,}`:

```tex
\inserted{\handwritten{plat et}}
```

112. handwritten, following `act et quasi-séparé sur $S$\handwritten{,}\inserted{`:

```tex
\handwritten{plat et}
```

113. handwritten, following `written{,}\inserted{\handwritten{plat et}} tel que $`:

```tex
\handwritten{\mathcal{A}}
```


## Scan 47

Start (UTC): 2026-11-13T20:10:06.978167+00:00

End (UTC): 2026-11-13T20:12:40.029263+00:00

Crop-first words/accents: « quasi-cohérent », « affine » plus « sur S », cancellation around « G et » leaving a possible t, « sont » changed toward « soit », « plats » with s cancelled, « définissant une opération », « déduit », « se factorise à travers », « injectif » with inserted « grâce au fait que A est plat ! », « opération induite », « stable », « Cela résulte immédiatement des définitions », « en général ». Lemma: « Soient G », « quasi-séparé et quasi-compact », deleted « plat A », « libre », « base », « bien déterminés par cette relation) », « sous-module », « engendré », « quasi-cohérent et de type fini », deleted « et contient x. ». Proof: deleted « Soit F le sous-module de E engendré par les x_i. », « Il est clair », « L'axiome », « d'autre part », « d'où » twice, « puisque », « forment une base », « Enfin ». Proposition: « Soit G », « localement libre après extension fidèlement plate quasi-compacte », « réductif », inserted « par exemple », « comme nous » with a cancelled extra stroke/letter, « l'exposé » cancelled, XXV with upper/lower bars, « Module » over cancelled module, « quasi-cohérent », « définissant ». Acute accents in cohérent/définissant/opération/déduit/résulte/immédiatement/définitions/général/séparé/déterminés/engendré/réductif/exposé; grave à/grâce's following au (grâce itself circumflex)/où/après/fidèlement. No accent supplied to the unusual relation). The last x subscript in rho(x_i)=sum a_ji tensor x looks like a handwritten i with a dot and foot, while j descenders in a_ij/a_ji are clear. A small flourish follows the lemma's final underline at right. Round subscript o remains distinguishable only tentatively from zero.


Read all three thirds, then enlarged the opening corrections, the first-paragraph punctuation, all indexed equations, the last underline flourish and the proposition corrections. The dark opening parenthesis before qu'on lies before the comma, not after it; a separate pale opening curve lies after the comma. Corrected the order and retained the pale second curve with a doubt. Marked the closing parenthesis after rho as handwritten. Added the nonverbal looped flourish at the right end of lemma 11.8. The final t after the cancellation of G e remains visibly outside the dark patch; it stays live. The sont→soit and plats→plat layers remain, and the small round subscript o/0 is still unresolved. The insertion grâce au fait que A est plat ! and its closing parenthesis, all three sur S additions, the inserted F, deleted et contient x., added quasi-cohérent, cancelled proof opening, handwritten I of Il, par exemple, extra cancelled letter after nous, l'exposé deletion and Module replacement are all retained in position. The XXV strokes and upper/lower bars were checked separately.

Index audit, in textual order: base phi_i; sum phi_i⊗x_i; following x_i membership; x_i generators; cancelled proof's x_i; sum Delta(phi_i)⊗x_i = sum phi_i⊗rho(x_i); Delta(phi_i) = sum phi_j⊗a_ij; sum phi_j⊗a_ij⊗x_i = sum phi_i⊗rho(x_i); the phi_i forming a base; rho(x_i)=sum a_ji⊗x_i; a_ji membership; finally sum_i eta(phi_i)x_i. The j in each a_ij/a_ji and phi_j has a descending hook. The handwritten corrected index after the last tensor x has a dot and an i-shaped foot, so the existing i is retained. No summation indices were supplied where the pen has none. The final summation has the explicit i underneath. The O_S bases, all E_o and rho_o indices, and the unbased tensor products were checked separately.

Alphabet audit: rounded A/a ambiguity retained; module E and F have their distinct loops; double-stroke W inspected in both W(E_o) and W(E); double-struck S remains in the lemma's first O-module index, while the other S letters have single impressions. Gamma is angular and phi open-looped with a descending stem. The surprise relation) remains exactly as typed. No mathematical statement or formula was repaired.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{(}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\unsure{
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
)
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
)
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
}
\figure{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw[line width=.7pt] (0,0) -- (.4,0);\draw[line width=1.3pt] (.42,-.01) -- (.49,.09) -- (.46,0) -- (.55,.1) -- (.5,.01) -- (.62,.07) -- (.56,0) -- (.73,.02) -- (.83,.08) -- (.77,0) -- (1,.02) -- (1.12,.04) -- (1.22,0) -- (1.37,.02) -- (1.5,0);\end{tikzpicture}}
```


### Every delimited formula, in page-file order

1. inline

```tex
\handwritten{\mathcal{O}}_S
```

2. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

3. inline

```tex
\handwritten{\mathcal{E}}
```

4. inline

```tex
\handwritten{\mathcal{O}}_S
```

5. inline

```tex
G
```

6. inline

```tex
S
```

7. inline

```tex
\handwritten{\mathcal{E}}
```

8. inline

```tex
S
```

9. inline

```tex
\handwritten{\rho:\mathcal{E}\to\mathcal{A}\otimes\mathcal{E}}
```

10. inline

```tex
G
```

11. inline

```tex
\handwritten{\mathcal{E}}
```

12. inline

```tex
\handwritten{\mathcal{E}}_{\unsure{o|0}}
```

13. inline

```tex
\handwritten{\mathcal{O}}_S
```

14. inline

```tex
\handwritten{\mathcal{E}}
```

15. inline

```tex
\handwritten{\mathcal{E}}_o\handwritten{\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

16. inline

```tex
\handwritten{\rho}
```

17. inline

```tex
\mathcal{A}
```

18. inline

```tex
\handwritten{\mathcal{A}\otimes\mathcal{E}_o\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

19. inline

```tex
\handwritten{\rho_o:\mathcal{E}_o\longrightarrow\mathcal{A}\otimes\mathcal{E}_o}
```

20. inline

```tex
\handwritten{\rho_o}
```

21. inline

```tex
G
```

22. inline

```tex
\handwritten{\mathcal{E}_o}
```

23. inline

```tex
\handwritten{\mathcal{E}}_o
```

24. inline

```tex
\handwritten{\rho}
```

25. inline

```tex
\handwritten{\mathcal{E}}_o
```

26. inline

```tex
\handwritten{\rho)}
```

27. inline

```tex
\handwritten{\mathbb{W}}(\handwritten{\mathcal{E}}_o)\handwritten{\longrightarrow\mathbb{W}}(\handwritten{\mathcal{E}})
```

28. inline

```tex
G
```

29. inline

```tex
S
```

30. inline

```tex
S
```

31. inline

```tex
\handwritten{\mathcal{A}}(G)
```

32. inline

```tex
\handwritten{\mathcal{O}}_{\mathbb{S}}
```

33. inline

```tex
\handwritten{\mathcal{A}}
```

34. inline

```tex
\handwritten{\mathcal{A}}
```

35. inline

```tex
(\handwritten{\varphi}_i)
```

36. inline

```tex
\handwritten{\mathcal{E}}
```

37. inline

```tex
\handwritten{\mathcal{O}}_S
```

38. inline

```tex
G
```

39. inline

```tex
S
```

40. inline

```tex
G
```

41. inline

```tex
\handwritten{\mathcal{E}}
```

42. inline

```tex
S
```

43. inline

```tex
\handwritten{\rho:\mathcal{E}\to\mathcal{A}\otimes\mathcal{E}}
```

44. inline

```tex
G
```

45. inline

```tex
\handwritten{\mathcal{E}}
```

46. inline

```tex
x\handwritten{\in\Gamma}(S,\handwritten{\mathcal{E}})
```

47. inline

```tex
\handwritten{\rho}(x)=\handwritten{\sum\varphi}_i\handwritten{\otimes x}_i
```

48. inline

```tex
x_i\handwritten{\in\Gamma}(S,\handwritten{\mathcal{E}})
```

49. inline

```tex
\mathcal{F}
```

50. inline

```tex
\handwritten{\mathcal{E}}
```

51. inline

```tex
x_i
```

52. inline

```tex
\handwritten{\rho}
```

53. inline

```tex
x
```

54. inline

```tex
\handwritten{\mathcal{O}}_S
```

55. inline

```tex
x\handwritten{\in\Gamma}(S,\handwritten{\mathcal{F}})
```

56. inline

```tex
\handwritten{\mathcal{F}}
```

57. inline

```tex
\handwritten{\mathcal{E}}
```

58. inline

```tex
x_i
```

59. inline

```tex
\handwritten{\mathcal{F}}
```

60. inline

```tex
\handwritten{\sum\Delta}(\handwritten{\varphi}_i)\handwritten{\otimes}x_i=\handwritten{\sum\varphi}_i\handwritten{\otimes\rho}(x_i)
```

61. inline

```tex
\handwritten{\Delta(\varphi}_i\handwritten{)=\sum\varphi}_j\handwritten{\otimes}a_{ij}
```

62. inline

```tex
\handwritten{\sum\varphi}_j\handwritten{\otimes}a_{ij}\handwritten{\otimes}x_i=\handwritten{\sum\varphi}_i\handwritten{\otimes\rho}(x_i)
```

63. inline

```tex
\handwritten{\varphi}_i
```

64. inline

```tex
\handwritten{\mathcal{A}}
```

65. inline

```tex
\handwritten{\rho}(x_i)=\handwritten{\sum}a_{ji}\handwritten{\otimes}x_{\handwritten{i}}
```

66. inline

```tex
a_{ji}\handwritten{\in\Gamma}(S,\handwritten{\mathcal{A}})
```

67. inline

```tex
\handwritten{\rho(\mathcal{F})\subset\mathcal{A}\otimes\mathcal{F}}
```

68. inline

```tex
\handwritten{\mathcal{F}}
```

69. inline

```tex
\handwritten{\rho}
```

70. inline

```tex
x=\handwritten{\sum_i\eta}(\handwritten{\varphi}_i)x_i\handwritten{\in\Gamma}(S,\handwritten{\mathcal{F}})
```

71. inline

```tex
G
```

72. inline

```tex
S
```

73. inline

```tex
S
```

74. inline

```tex
\handwritten{\mathcal{A}}=\handwritten{\mathcal{A}}(G)
```

75. inline

```tex
S
```

76. inline

```tex
G
```

77. inline

```tex
\overline{\underline{\mathrm{XXV}}}
```

78. inline

```tex
\handwritten{\mathcal{E}}
```

79. inline

```tex
\handwritten{\mathcal{O}}_S
```

80. inline

```tex
G
```

81. inline

```tex
S
```

82. inline

```tex
G
```

83. inline

```tex
\handwritten{\mathcal{E}}
```

84. inline

```tex
S
```

85. inline

```tex
\handwritten{\rho:\mathcal{E}\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

86. inline

```tex
G
```

87. inline

```tex
\handwritten{\mathcal{E}}
```

### Every i/j index occurrence (local TeX contexts)

1. ` $(\handwritten{\varphi}_i)$, $\handwritten{\mathc`
2. `handwritten{\sum\varphi}_i\handwritten{\otimes x}_`
3. `i\handwritten{\otimes x}_i$, où les $x_i\handwritt`
4. `\otimes x}_i$, où les $x_i\handwritten{\in\Gamma}(`
5. `E}}$ engendré par les $x_i$ est stable sous $\hand`
6. `E}}$ engendré par les $x_i$.} \handwritten{I}l est`
7. `a}(\handwritten{\varphi}_i)\handwritten{\otimes}x_`
8. `i)\handwritten{\otimes}x_i=\handwritten{\sum\varph`
9. `handwritten{\sum\varphi}_i\handwritten{\otimes\rho`
10. `ndwritten{\otimes\rho}(x_i)$ ; d'autre part, $\han`
11. `dwritten{\Delta(\varphi}_i\handwritten{)=\sum\varp`
12. `ndwritten{)=\sum\varphi}_j\handwritten{\otimes}a_{`
13. `_j\handwritten{\otimes}a_{ij}$ , d'où $\handwritten{\`
14. `handwritten{\sum\varphi}_j\handwritten{\otimes}a_{`
15. `_j\handwritten{\otimes}a_{ij}\handwritten{\otimes}x_i`
16. `j}\handwritten{\otimes}x_i=\handwritten{\sum\varph`
17. `handwritten{\sum\varphi}_i\handwritten{\otimes\rho`
18. `ndwritten{\otimes\rho}(x_i)$, d'où, puisque les $\`
19. `s $\handwritten{\varphi}_i$ forment une base de $\`
20. `$, $\handwritten{\rho}(x_i)=\handwritten{\sum}a_{j`
21. `x_i)=\handwritten{\sum}a_{ji}\handwritten{\otimes}x_{`
22. `\handwritten{i}}$, où $a_{ji}\handwritten{\in\Gamma}(`
23. `que $x=\handwritten{\sum_i\eta}(\handwritten{\varp`
24. `a}(\handwritten{\varphi}_i)x_i\handwritten{\in\Gam`
25. `handwritten{\varphi}_i)x_i\handwritten{\in\Gamma}(`

### Handwritten and correction placements

1. handwritten, following `\scanpage{47} \mspage{`:

```tex
\handwritten{15}
```

2. handwritten, following `\scanpage{47} \mspage{\handwritten{15}} un $`:

```tex
\handwritten{\mathcal{O}}
```

3. handwritten, following `{15}} un $\handwritten{\mathcal{O}}_S$-Module plat $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

4. handwritten, following `e plat $\handwritten{\unsure{\mathcal{A}|a}}$ , et $`:

```tex
\handwritten{\mathcal{E}}
```

5. handwritten, following `athcal{A}|a}}$ , et $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```

6. inserted, following `e quasi-cohérent. On suppose soit que $G$ est affine`:

```tex
\inserted{\handwritten{sur $S$}}
```

7. handwritten, following `hérent. On suppose soit que $G$ est affine\inserted{`:

```tex
\handwritten{sur $S$}
```

8. deleted, following `st affine\inserted{\handwritten{sur $S$}}, soit que `:

```tex
\deleted{\unsure{G e}}
```

9. handwritten, following `ritten{sur $S$}}, soit que \deleted{\unsure{G e}}t $`:

```tex
\handwritten{\mathcal{E}}
```

10. deleted, following `\deleted{\unsure{G e}}t $\handwritten{\mathcal{E}}$ `:

```tex
\deleted{son}
```

11. handwritten, following `ure{G e}}t $\handwritten{\mathcal{E}}$ \deleted{son}`:

```tex
\handwritten{soi}
```

12. deleted, following `n{\mathcal{E}}$ \deleted{son}\handwritten{soi}t plat`:

```tex
\deleted{s}
```

13. handwritten, following `n}\handwritten{soi}t plat\deleted{s} sur $S$. Soit $`:

```tex
\handwritten{\rho:\mathcal{E}\to\mathcal{A}\otimes\mathcal{E}}
```

14. handwritten, following `homomorphisme définissant une opération de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

15. handwritten, following `ation de $G$ sur $\handwritten{\mathcal{E}}$. Soit $`:

```tex
\handwritten{\mathcal{E}}
```

16. handwritten, following `$\handwritten{\mathcal{E}}_{\unsure{o|0}}$ un sous-$`:

```tex
\handwritten{\mathcal{O}}
```

17. handwritten, following `ndwritten{\mathcal{O}}_S$-Module quasi-cohérent de $`:

```tex
\handwritten{\mathcal{E}}
```

18. handwritten, following `\handwritten{\mathcal{E}}$ tel que l'homomorphisme $`:

```tex
\handwritten{\mathcal{E}}
```

19. handwritten, following `tel que l'homomorphisme $\handwritten{\mathcal{E}}_o`:

```tex
\handwritten{\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

20. handwritten, following `ightarrow\mathcal{A}\otimes\mathcal{E}}$ déduit de $`:

```tex
\handwritten{\rho}
```

21. handwritten, following `}$ se factorise à travers l'homomorphisme canonique `:

```tex
\handwritten{(}
```

22. inserted, following `rs l'homomorphisme canonique \handwritten{(}injectif`:

```tex
\inserted{\handwritten{, grâce au fait que $\mathcal{A}$ est plat !)}}
```

23. handwritten, following `orphisme canonique \handwritten{(}injectif\inserted{`:

```tex
\handwritten{, grâce au fait que $\mathcal{A}$ est plat !)}
```

24. handwritten, following `en{, grâce au fait que $\mathcal{A}$ est plat !)}} $`:

```tex
\handwritten{\mathcal{A}\otimes\mathcal{E}_o\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

25. handwritten, following `A}\otimes\mathcal{E}}$ au moyen de l'homomorphisme $`:

```tex
\handwritten{\rho_o:\mathcal{E}_o\longrightarrow\mathcal{A}\otimes\mathcal{E}_o}
```

26. handwritten, following `rightarrow\mathcal{A}\otimes\mathcal{E}_o}$. Alors $`:

```tex
\handwritten{\rho_o}
```

27. handwritten, following `dwritten{\rho_o}$ définit une opération de $G$ sur $`:

```tex
\handwritten{\mathcal{E}_o}
```

28. handwritten, following `e opération de $G$ sur $\handwritten{\mathcal{E}_o}$`:

```tex
\handwritten{(}
```

29. handwritten, following `G$ sur $\handwritten{\mathcal{E}_o}$\handwritten{(},`:

```tex
\handwritten{\unsure{(}}
```

30. handwritten, following `{(}} qu'on appellera \uline{opération induite} sur $`:

```tex
\handwritten{\mathcal{E}}
```

31. handwritten, following `ion induite} sur $\handwritten{\mathcal{E}}_o$ par $`:

```tex
\handwritten{\rho}
```

32. handwritten, following `al{E}}_o$ par $\handwritten{\rho}$, et on dira que $`:

```tex
\handwritten{\mathcal{E}}
```

33. handwritten, following `andwritten{\mathcal{E}}_o$ est \uline{stable} sous $`:

```tex
\handwritten{\rho)}
```

34. handwritten, following `ela résulte immédiatement des définitions et de (11.`:

```tex
\handwritten{6}
```

35. handwritten, following `ra cependant qu'en général l'application canonique $`:

```tex
\handwritten{\mathbb{W}}
```

36. handwritten, following `l l'application canonique $\handwritten{\mathbb{W}}(`:

```tex
\handwritten{\mathcal{E}}
```

37. handwritten, following `handwritten{\mathbb{W}}(\handwritten{\mathcal{E}}_o)`:

```tex
\handwritten{\longrightarrow\mathbb{W}}
```

38. handwritten, following `thcal{E}}_o)\handwritten{\longrightarrow\mathbb{W}}(`:

```tex
\handwritten{\mathcal{E}}
```

39. handwritten, following `oupe quasi-séparé et quasi-compact sur $S$ tel que $`:

```tex
\handwritten{\mathcal{A}}
```

40. handwritten, following `$S$ tel que $\handwritten{\mathcal{A}}(G)$ soit un $`:

```tex
\handwritten{\mathcal{O}}
```

41. deleted, following ` un $\handwritten{\mathcal{O}}_{\mathbb{S}}$-Module `:

```tex
\deleted{\unsure{plat} $\handwritten{\mathcal{A}}$}
```

42. handwritten, following `al{O}}_{\mathbb{S}}$-Module \deleted{\unsure{plat} $`:

```tex
\handwritten{\mathcal{A}}
```

43. handwritten, following `d{\unsure{plat} $\handwritten{\mathcal{A}}$} libre $`:

```tex
\handwritten{\mathcal{A}}
```

44. handwritten, following `l{A}}$} libre $\handwritten{\mathcal{A}}$ de base $(`:

```tex
\handwritten{\varphi}
```

45. handwritten, following `\mathcal{A}}$ de base $(\handwritten{\varphi}_i)$, $`:

```tex
\handwritten{\mathcal{E}}
```

46. handwritten, following `itten{\varphi}_i)$, $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```

47. inserted, following `e quasi-cohérent. On suppose soit que $G$ est affine`:

```tex
\inserted{\handwritten{sur $S$}}
```

48. handwritten, following `hérent. On suppose soit que $G$ est affine\inserted{`:

```tex
\handwritten{sur $S$}
```

49. handwritten, following `e\inserted{\handwritten{sur $S$}}, soit que $G$ et $`:

```tex
\handwritten{\mathcal{E}}
```

50. handwritten, following `handwritten{\mathcal{E}}$ sont plats sur $S$. Soit $`:

```tex
\handwritten{\rho:\mathcal{E}\to\mathcal{A}\otimes\mathcal{E}}
```

51. handwritten, following `homomorphisme définissant une opération de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

52. handwritten, following `n de $G$ sur $\handwritten{\mathcal{E}}$, et soit $x`:

```tex
\handwritten{\in\Gamma}
```

53. handwritten, following `{\mathcal{E}}$, et soit $x\handwritten{\in\Gamma}(S,`:

```tex
\handwritten{\mathcal{E}}
```

54. handwritten, following `n{\in\Gamma}(S,\handwritten{\mathcal{E}})$. Posons $`:

```tex
\handwritten{\rho}
```

55. handwritten, following `itten{\mathcal{E}})$. Posons $\handwritten{\rho}(x)=`:

```tex
\handwritten{\sum\varphi}
```

56. handwritten, following `s $\handwritten{\rho}(x)=\handwritten{\sum\varphi}_i`:

```tex
\handwritten{\otimes x}
```

57. handwritten, following `sum\varphi}_i\handwritten{\otimes x}_i$, où les $x_i`:

```tex
\handwritten{\in\Gamma}
```

58. handwritten, following `\otimes x}_i$, où les $x_i\handwritten{\in\Gamma}(S,`:

```tex
\handwritten{\mathcal{E}}
```

59. inserted, following `déterminés par cette relation). Alors le sous-module`:

```tex
\inserted{\handwritten{$\mathcal{F}$}}
```

60. handwritten, following ` par cette relation). Alors le sous-module\inserted{`:

```tex
\handwritten{$\mathcal{F}$}
```

61. handwritten, following `us-module\inserted{\handwritten{$\mathcal{F}$}} de $`:

```tex
\handwritten{\mathcal{E}}
```

62. handwritten, following `athcal{E}}$ engendré par les $x_i$ est stable sous $`:

```tex
\handwritten{\rho}
```

63. deleted, following ` par les $x_i$ est stable sous $\handwritten{\rho}$,`:

```tex
\deleted{et contient $x$.}
```

64. inserted, following `sous $\handwritten{\rho}$,\deleted{et contient $x$.}`:

```tex
\inserted{quasi-cohérent}
```

65. handwritten, following `$x$.}\inserted{quasi-cohérent} et de type fini sur $`:

```tex
\handwritten{\mathcal{O}}
```

66. handwritten, following `e type fini sur $\handwritten{\mathcal{O}}_S$, et $x`:

```tex
\handwritten{\in\Gamma}
```

67. handwritten, following `ten{\mathcal{O}}_S$, et $x\handwritten{\in\Gamma}(S,`:

```tex
\handwritten{\mathcal{F}}
```

68. handwritten, following `{\in\Gamma}(S,\handwritten{\mathcal{F}})$.} \figure{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]\draw[line width=.7pt] (0,0) -- (.4,0);\draw[line width=1.3pt] (.42,-.01) -- (.49,.09) -- (.46,0) -- (.55,.1) -- (.5,.01) -- (.62,.07) -- (.56,0) -- (.73,.02) -- (.83,.08) -- (.77,0) -- (1,.02) -- (1.12,.04) -- (1.22,0) -- (1.37,.02) -- (1.5,0);\end{tikzpicture}}
```

69. deleted, following `22,0) -- (1.37,.02) -- (1.5,0);\end{tikzpicture}}}  `:

```tex
\deleted{Soit $\handwritten{\mathcal{F}}$ le sous-module de $\handwritten{\mathcal{E}}$ engendré par les $x_i$.}
```

70. handwritten, following `.02) -- (1.5,0);\end{tikzpicture}}}  \deleted{Soit $`:

```tex
\handwritten{\mathcal{F}}
```

71. handwritten, following `Soit $\handwritten{\mathcal{F}}$ le sous-module de $`:

```tex
\handwritten{\mathcal{E}}
```

72. handwritten, following `\handwritten{\mathcal{E}}$ engendré par les $x_i$.} `:

```tex
\handwritten{I}
```

73. handwritten, following `dré par les $x_i$.} \handwritten{I}l est clair que $`:

```tex
\handwritten{\mathcal{F}}
```

74. handwritten, following `ohérent et de type fini. L'axiome (CM1) montre que $`:

```tex
\handwritten{\sum\Delta}
```

75. handwritten, following `L'axiome (CM1) montre que $\handwritten{\sum\Delta}(`:

```tex
\handwritten{\varphi}
```

76. handwritten, following `e $\handwritten{\sum\Delta}(\handwritten{\varphi}_i)`:

```tex
\handwritten{\otimes}
```

77. handwritten, following `a}(\handwritten{\varphi}_i)\handwritten{\otimes}x_i=`:

```tex
\handwritten{\sum\varphi}
```

78. handwritten, following `\handwritten{\otimes}x_i=\handwritten{\sum\varphi}_i`:

```tex
\handwritten{\otimes\rho}
```

79. handwritten, following `}_i\handwritten{\otimes\rho}(x_i)$ ; d'autre part, $`:

```tex
\handwritten{\Delta(\varphi}
```

80. handwritten, following `_i)$ ; d'autre part, $\handwritten{\Delta(\varphi}_i`:

```tex
\handwritten{)=\sum\varphi}
```

81. handwritten, following `itten{\Delta(\varphi}_i\handwritten{)=\sum\varphi}_j`:

```tex
\handwritten{\otimes}
```

82. handwritten, following `=\sum\varphi}_j\handwritten{\otimes}a_{ij}$ , d'où $`:

```tex
\handwritten{\sum\varphi}
```

83. handwritten, following `{\otimes}a_{ij}$ , d'où $\handwritten{\sum\varphi}_j`:

```tex
\handwritten{\otimes}
```

84. handwritten, following `andwritten{\sum\varphi}_j\handwritten{\otimes}a_{ij}`:

```tex
\handwritten{\otimes}
```

85. handwritten, following `\handwritten{\otimes}a_{ij}\handwritten{\otimes}x_i=`:

```tex
\handwritten{\sum\varphi}
```

86. handwritten, following `\handwritten{\otimes}x_i=\handwritten{\sum\varphi}_i`:

```tex
\handwritten{\otimes\rho}
```

87. handwritten, following `\handwritten{\otimes\rho}(x_i)$, d'où, puisque les $`:

```tex
\handwritten{\varphi}
```

88. handwritten, following ` les $\handwritten{\varphi}_i$ forment une base de $`:

```tex
\handwritten{\mathcal{A}}
```

89. handwritten, following `$ forment une base de $\handwritten{\mathcal{A}}$, $`:

```tex
\handwritten{\rho}
```

90. handwritten, following `handwritten{\mathcal{A}}$, $\handwritten{\rho}(x_i)=`:

```tex
\handwritten{\sum}
```

91. handwritten, following `$, $\handwritten{\rho}(x_i)=\handwritten{\sum}a_{ji}`:

```tex
\handwritten{\otimes}
```

92. handwritten, following `_i)=\handwritten{\sum}a_{ji}\handwritten{\otimes}x_{`:

```tex
\handwritten{i}
```

93. handwritten, following `handwritten{\otimes}x_{\handwritten{i}}$, où $a_{ji}`:

```tex
\handwritten{\in\Gamma}
```

94. handwritten, following `ndwritten{i}}$, où $a_{ji}\handwritten{\in\Gamma}(S,`:

```tex
\handwritten{\mathcal{A}}
```

95. handwritten, following `}(S,\handwritten{\mathcal{A}})$, ce qui montre que $`:

```tex
\handwritten{\rho(\mathcal{F})\subset\mathcal{A}\otimes\mathcal{F}}
```

96. handwritten, following `al{F})\subset\mathcal{A}\otimes\mathcal{F}}$, donc $`:

```tex
\handwritten{\mathcal{F}}
```

97. handwritten, following `, donc $\handwritten{\mathcal{F}}$ est stable sous $`:

```tex
\handwritten{\rho}
```

98. handwritten, following `dwritten{\rho}$. Enfin l'axiome (CM2) montre que $x=`:

```tex
\handwritten{\sum_i\eta}
```

99. handwritten, following `axiome (CM2) montre que $x=\handwritten{\sum_i\eta}(`:

```tex
\handwritten{\varphi}
```

100. handwritten, following `\handwritten{\sum_i\eta}(\handwritten{\varphi}_i)x_i`:

```tex
\handwritten{\in\Gamma}
```

101. handwritten, following `handwritten{\varphi}_i)x_i\handwritten{\in\Gamma}(S,`:

```tex
\handwritten{\mathcal{F}}
```

102. handwritten, following `-groupe quasi-compact quasi-séparé sur $S$ tel que $`:

```tex
\handwritten{\mathcal{A}}
```

103. handwritten, following `i-séparé sur $S$ tel que $\handwritten{\mathcal{A}}=`:

```tex
\handwritten{\mathcal{A}}
```

104. inserted, following `ate quasi-compacte de la base $S$ (ce qui est le cas`:

```tex
\inserted{\handwritten{par exemple}}
```

105. handwritten, following `compacte de la base $S$ (ce qui est le cas\inserted{`:

```tex
\handwritten{par exemple}
```

106. deleted, following `ple}} lorsque $G$ est un groupe réductif, comme nous`:

```tex
\deleted{\unsure{l}}
```

107. deleted, following `tif, comme nous\deleted{\unsure{l}} le verrons dans `:

```tex
\deleted{l'exposé}
```

108. handwritten, following `eted{\unsure{l}} le verrons dans \deleted{l'exposé} `:

```tex
\handwritten{$\overline{\underline{\mathrm{XXV}}}$}
```

109. handwritten, following `n{$\overline{\underline{\mathrm{XXV}}}$}), et soit $`:

```tex
\handwritten{\mathcal{E}}
```

110. handwritten, following `{XXV}}}$}), et soit $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```

111. deleted, following `tten{\mathcal{E}}$ un $\handwritten{\mathcal{O}}_S$-`:

```tex
\deleted{module}
```

112. handwritten, following `}$ un $\handwritten{\mathcal{O}}_S$-\deleted{module}`:

```tex
\handwritten{Module}
```

113. inserted, following ` quasi-cohérent . On suppose soit que $G$ est affine`:

```tex
\inserted{\handwritten{sur $S$}}
```

114. handwritten, following `érent . On suppose soit que $G$ est affine\inserted{`:

```tex
\handwritten{sur $S$}
```

115. handwritten, following `e\inserted{\handwritten{sur $S$}}, soit que $G$ et $`:

```tex
\handwritten{\mathcal{E}}
```

116. handwritten, following `handwritten{\mathcal{E}}$ sont plats sur $S$. Soit $`:

```tex
\handwritten{\rho:\mathcal{E}\longrightarrow\mathcal{A}\otimes\mathcal{E}}
```

117. handwritten, following `homomorphisme définissant une opération de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```


## Scan 48

Start (UTC): 2026-11-13T20:12:40.291376+00:00

End (UTC): 2026-11-13T20:15:21.859747+00:00

Crop-first words/accents: « sous-Module quasi-cohérent », « plus petit », F with wavy mark then final F without one, « Lorsque F est de type [x-overtyped clipped word] fini », « même », boxed « Sa formation commute à toute extension de la base S'→S », « On se ramène aisément », inserted « par descente fidèlement plate », « au cas où », « conséquence du lemme 11.8 ». Corollary corrections: « Soit »→« Soient », « pré » deleted before schéma, « affine »→« quasi-compact quasi-séparé », inserted « et » before « quasicompact », « libre » deleted before localement libre, « base,S », « sur S » with altered punctuation, « On se donne une opération de G sur E. », « Alors », « famille filtrante croissante », « stables ». Proof: « conséquence immédiate », cancelled « engendré par ses sections », « et car l'ensemble des sous-Modules quasi-cohérents de type fini de E stables sous G est stable par engendrement. », handwritten « limite inductive de ses sous-Modules quasi-cohérents de type fini (EGA I 9.4.9. , IV 1.7.7.) ». Remark: « J.P. Serre a remarqué », « pour toute ouvert affine », « fidèlement plat », « défini », « projectif (pas nécessairement libre) », « noéthérien régulier », « hypothèse », « être remplacée », « voir à ce sujet », deleted « un exposé de Serre dans SGA (1966/67). » with 6 inserted. New citation has « J.P. Serre », faint Le/le, « Groupes|Groupe de Grothendieck des schémas en groupes réductifs déployés, Pub. Math. n° 34|39, p. 37-52. » Cancelled proposition: « Soient k un corps », deleted second « corps », « algébrique », « vectoriel », « fermée », « Réciproquement », « l'algèbre », « opère », « lui-même », « à gauche », « opération », cancelled incomplete diagon-word then « diagonale », « D'après », « réunion ». Bottom deeply cancelled lines admit « Puisque G est de type fini sur k, A ... type fini sur k, donc il existe ... tel que ... engendre A comme algèbre. L'opération de G sur » only tentatively. Accents observed: acute in cohérent/aisément/schéma/opération/immédiate/engendré/remarqué/défini/nécessairement/noéthérien/régulier/remplacée/exposé/réductifs/déployés/algébrique/fermée/Réciproquement/réunion; grave in ramène/fidèlement/où/après/hypothèse/algèbre/opère/à; circumflex même/être. The grammar « toute ouvert » is visibly typed. Doubts in the citation and last cancelled lines need the enlarged crops.


Read the long page's three overlapping thirds completely, including the pasted remark, the cancelled proposition and the deeply cancelled final lines. Enlargements checked the box, its punctuation and pointer, the base-change sign, the replacement proof reference, the handwritten citation and the two blacked-out lines. The inserted sentence was present but its stepped enclosure and upward stem were missing; added them in TikZ, including the small endpoint dot and crossbar (no invented arrowhead). The final F of the opening paragraph has no tilde; the earlier new submodule has a wavy tilde. The clipped x-overtyped word after type still has no recoverable candidate; its one-word illegible mark remains. The tensor sign after E in the remark has a complete outer loop around crossing strokes, so removed the provisional product-cross alternative. The last cancelled finite-type sentence was overconfident in its middle: broadened the doubt to the complete clause through existe. The surviving i_o/0 and V_{i_o} are still represented separately. No words were added past the visible final sur.

Corrections compared individually: the top insertion; par descente fidèlement plate; Soit/Soient; pré deletion; affine/quasi-compact quasi-séparé; et insertion; deleted libre; punctuation after sur S; On se donne une opération de G sur E.; overwritten A of Alors and G at the end; the entire replaced proof and its I 9.4.9., IV 1.7.7. reference; SGA with inserted 6 and cancelled 1966/67; the separate 1-like stroke; the replacement citation; cancelled corps in 11.11; the locally cancelled incomplete diagon-word; the corrected 0 in 11.10. The source forms toute ouvert, base,S and quasicompact remain. The citation keeps Le/le, Groupes/Groupe and 34/39 as unresolved readings, without consulting a bibliography.

Formula audit: checked S'→S inside the box; every O_S-module and E/F/A occurrence; the remark's U'→U, U', A', E⊗_U U' and A(G); each GL_k(V) occurrence and u:G→GL_k(V); Delta:A→A⊗_k A; (V_i)_{i∈I}; i_o/0∈I and V_{i_o} under the heavy deletion. The i indices have short stems; there are no j indices. The typed A in the cancelled proposition has single typewriter stems, unlike the handwritten round A/a in the upper half. GL's two capitals were inspected in the heading and proof separately and remain ordinary underlined typed capitals. The handwriting E/F/O retains its loop/crossbar forms; IV and I in the proof citation have their visible bars. No diagram is on this page. The three long diagonal strokes cancel the bottom proposition and proof, whose contents remain fully represented with deletion macros.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
figure{\
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.25,.1) .. controls (-.12,-.05) and (0,.6) .. (0,1.1) -- (0,2.5);
\fill (0,2.5) circle (.04);\draw[line width=.8pt] (-.12,2.38) -- (.14,2.38);
\draw (.25,.7) .. controls (.3,.9) and (5.4,.9) .. (5.5,.7) -- (5.5,-.55) -- (4.1,-.55) -- (4.1,-.85) -- (.25,-.85) -- cycle;
\node[align=left,anchor=west] at (.35,-.03) 
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
 
->
\\
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
 
->
\\
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
};
\end{tikzpicture}}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
unsure{\
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
|\times}
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
}
->
∅
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
\unsure{
->
∅
```


### Every delimited formula, in page-file order

1. inline

```tex
\handwritten{\mathcal{O}}_S
```

2. inline

```tex
\handwritten{\mathcal{F}}
```

3. inline

```tex
\handwritten{\mathcal{E}}
```

4. inline

```tex
\handwritten{\mathcal{O}}_S
```

5. inline

```tex
\handwritten{\widetilde{\mathcal{F}}}
```

6. inline

```tex
\handwritten{\mathcal{E}}
```

7. inline

```tex
\handwritten{\mathcal{F}}
```

8. inline

```tex
\handwritten{\rho}
```

9. inline

```tex
S'\to S
```

10. inline

```tex
\handwritten{\mathcal{F}}
```

11. inline

```tex
\handwritten{\mathcal{F}}
```

12. inline

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

13. inline

```tex
\handwritten{\mathcal{O}}_S
```

14. inline

```tex
S
```

15. inline

```tex
G
```

16. inline

```tex
S
```

17. inline

```tex
S
```

18. inline

```tex
\handwritten{\mathcal{A}}(G)
```

19. inline

```tex
S
```

20. inline

```tex
\handwritten{\mathcal{E}}
```

21. inline

```tex
\handwritten{\mathcal{O}}_S
```

22. inline

```tex
G
```

23. inline

```tex
S
```

24. inline

```tex
G
```

25. inline

```tex
\handwritten{\mathcal{E}}
```

26. inline

```tex
S
```

27. inline

```tex
G
```

28. inline

```tex
\handwritten{\mathcal{E}}
```

29. inline

```tex
\handwritten{\mathcal{E}}
```

30. inline

```tex
\handwritten{\mathcal{O}}_S
```

31. inline

```tex
\handwritten{\mathcal{E}}
```

32. inline

```tex
\handwritten{G}
```

33. inline

```tex
\handwritten{\mathcal{E}}
```

34. inline

```tex
\handwritten{\mathcal{O}}_S
```

35. inline

```tex
\handwritten{\mathcal{E}}
```

36. inline

```tex
G
```

37. inline

```tex
\overline{\underline{\mathrm{IV}}}
```

38. inline

```tex
U
```

39. inline

```tex
S
```

40. inline

```tex
U'\handwritten{\to}U
```

41. inline

```tex
U'
```

42. inline

```tex
A'
```

43. inline

```tex
\handwritten{\mathcal{E}\otimes}_U U'
```

44. inline

```tex
A'
```

45. inline

```tex
S
```

46. inline

```tex
G
```

47. inline

```tex
S
```

48. inline

```tex
\handwritten{\mathcal{A}}(G)
```

49. inline

```tex
k
```

50. inline

```tex
G
```

51. inline

```tex
k
```

52. inline

```tex
G
```

53. inline

```tex
V
```

54. inline

```tex
G
```

55. inline

```tex
\underline{\mathrm{GL}}_k(V)
```

56. inline

```tex
k
```

57. inline

```tex
V
```

58. inline

```tex
u:G\handwritten{\to}\underline{\mathrm{GL}}_k(V)
```

59. inline

```tex
\underline{\mathrm{GL}}_k(V)
```

60. inline

```tex
G
```

61. inline

```tex
G
```

62. inline

```tex
A
```

63. inline

```tex
G
```

64. inline

```tex
G
```

65. inline

```tex
A
```

66. inline

```tex
\handwritten{\Delta}:A\handwritten{\longrightarrow}A\handwritten{\otimes}_k A
```

67. inline

```tex
A
```

68. inline

```tex
(V_i)_{i\handwritten{\in}I}
```

69. inline

```tex
G
```

70. inline

```tex
G
```

71. inline

```tex
k
```

72. inline

```tex
A
```

73. inline

```tex
k
```

74. inline

```tex
i_{\unsure{o|0}}\handwritten{\in}I
```

75. inline

```tex
V_{i_o}
```

76. inline

```tex
A
```

77. inline

```tex
G
```

### Every i/j index occurrence (local TeX contexts)

1. `filtrante croissante $(V_i)_{i\handwritten{\in}I}$`
2. `ritten{\in}I$ tel que $V_{i_o}$ \unsure{engendre $A$ c`

### Handwritten and correction placements

1. handwritten, following `\scanpage{48} \mspage{`:

```tex
\handwritten{16}
```

2. handwritten, following `age{\handwritten{16}} \uline{Alors, pour tout sous-$`:

```tex
\handwritten{\mathcal{O}}
```

3. handwritten, following `\handwritten{\mathcal{O}}_S$-Module quasi-cohérent $`:

```tex
\handwritten{\mathcal{F}}
```

4. handwritten, following `dule quasi-cohérent $\handwritten{\mathcal{F}}$ de $`:

```tex
\handwritten{\mathcal{E}}
```

5. handwritten, following `written{\mathcal{E}}$ il existe un plus petit sous-$`:

```tex
\handwritten{\mathcal{O}}
```

6. handwritten, following `\handwritten{\mathcal{O}}_S$-Module quasi-cohérent $`:

```tex
\handwritten{\widetilde{\mathcal{F}}}
```

7. handwritten, following `ohérent $\handwritten{\widetilde{\mathcal{F}}}$ de $`:

```tex
\handwritten{\mathcal{E}}
```

8. handwritten, following `cal{F}}}$ de $\handwritten{\mathcal{E}}$ contenant $`:

```tex
\handwritten{\mathcal{F}}
```

9. handwritten, following `t $\handwritten{\mathcal{F}}$ qui soit stable sous $`:

```tex
\handwritten{\rho}
```

10. inserted, following `cal{F}}$ qui soit stable sous $\handwritten{\rho}$.}`:

```tex
\inserted{\figure{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.25,.1) .. controls (-.12,-.05) and (0,.6) .. (0,1.1) -- (0,2.5);
\fill (0,2.5) circle (.04);\draw[line width=.8pt] (-.12,2.38) -- (.14,2.38);
\draw (.25,.7) .. controls (.3,.9) and (5.4,.9) .. (5.5,.7) -- (5.5,-.55) -- (4.1,-.55) -- (4.1,-.85) -- (.25,-.85) -- cycle;
\node[align=left,anchor=west] at (.35,-.03) {Sa formation commute\\à toute extension de\\la base $S'\to S$};
\end{tikzpicture}}}}
```

11. handwritten, following `stable sous $\handwritten{\rho}$.}\inserted{\figure{`:

```tex
\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.25,.1) .. controls (-.12,-.05) and (0,.6) .. (0,1.1) -- (0,2.5);
\fill (0,2.5) circle (.04);\draw[line width=.8pt] (-.12,2.38) -- (.14,2.38);
\draw (.25,.7) .. controls (.3,.9) and (5.4,.9) .. (5.5,.7) -- (5.5,-.55) -- (4.1,-.55) -- (4.1,-.85) -- (.25,-.85) -- cycle;
\node[align=left,anchor=west] at (.35,-.03) {Sa formation commute\\à toute extension de\\la base $S'\to S$};
\end{tikzpicture}}
```

12. handwritten, following `ase $S'\to S$}; \end{tikzpicture}}}}\uline{Lorsque $`:

```tex
\handwritten{\mathcal{F}}
```

13. deleted, following `ine{Lorsque $\handwritten{\mathcal{F}}$ est de type `:

```tex
\deleted{\illegible{1}}
```

14. handwritten, following `\deleted{\illegible{1}} fini, il en est de même de $`:

```tex
\handwritten{\mathcal{F}}
```

15. inserted, following `$\handwritten{\mathcal{F}}$.}  On se ramène aisément`:

```tex
\inserted{\handwritten{par descente fidèlement plate}}
```

16. handwritten, following `ten{\mathcal{F}}$.}  On se ramène aisément\inserted{`:

```tex
\handwritten{par descente fidèlement plate}
```

17. handwritten, following `dwritten{par descente fidèlement plate}} au cas où $`:

```tex
\handwritten{\unsure{\mathcal{A}|a}}
```

18. handwritten, following `s où $\handwritten{\unsure{\mathcal{A}|a}}$ est un $`:

```tex
\handwritten{\mathcal{O}}
```

19. deleted, following `nséquence du lemme 11.8.  \uline{Corollaire 11.10.- `:

```tex
\deleted{Soit}
```

20. inserted, following `emme 11.8.  \uline{Corollaire 11.10.- \deleted{Soit}`:

```tex
\inserted{Soient}
```

21. deleted, following `aire 11.10.- \deleted{Soit}\inserted{Soient} $S$ un `:

```tex
\deleted{pré}
```

22. deleted, following `{Soit}\inserted{Soient} $S$ un \deleted{pré} schéma `:

```tex
\deleted{affine}
```

23. inserted, following `Soient} $S$ un \deleted{pré} schéma \deleted{affine}`:

```tex
\inserted{\handwritten{quasi-compact quasi-séparé}}
```

24. handwritten, following `$ un \deleted{pré} schéma \deleted{affine}\inserted{`:

```tex
\handwritten{quasi-compact quasi-séparé}
```

25. inserted, following `mpact quasi-séparé}}, $G$ un $S$-groupe quasi-séparé`:

```tex
\inserted{\handwritten{et}}
```

26. handwritten, following `i-séparé}}, $G$ un $S$-groupe quasi-séparé\inserted{`:

```tex
\handwritten{et}
```

27. handwritten, following `ed{\handwritten{et}}quasicompact sur $S$ , tel que $`:

```tex
\handwritten{\mathcal{A}}
```

28. deleted, following `$ , tel que $\handwritten{\mathcal{A}}(G)$ devienne `:

```tex
\deleted{\unsure{libre}}
```

29. handwritten, following `ement plate quasi-compacte de la base,$S$, et soit $`:

```tex
\handwritten{\mathcal{E}}
```

30. handwritten, following `a base,$S$, et soit $\handwritten{\mathcal{E}}$ un $`:

```tex
\handwritten{\mathcal{O}}
```

31. deleted, following `cohérent. On suppose soit que $G$ est affine sur $S$`:

```tex
\deleted{\unsure{.}}
```

32. handwritten, following ` soit que $G$ est affine sur $S$\deleted{\unsure{.}}`:

```tex
\handwritten{,}
```

33. handwritten, following `\deleted{\unsure{.}}\handwritten{,}soit que $G$ et $`:

```tex
\handwritten{\mathcal{E}}
```

34. handwritten, following `G$ et $\handwritten{\mathcal{E}}$ sont plats sur $S$`:

```tex
\handwritten{.}
```

35. inserted, following `tten{\mathcal{E}}$ sont plats sur $S$\handwritten{.}`:

```tex
\inserted{On se donne une opération de $G$ sur $\handwritten{\mathcal{E}}$\handwritten{.}}
```

36. handwritten, following `n{.}\inserted{On se donne une opération de $G$ sur $`:

```tex
\handwritten{\mathcal{E}}
```

37. handwritten, following `une opération de $G$ sur $\handwritten{\mathcal{E}}$`:

```tex
\handwritten{.}
```

38. handwritten, following `$G$ sur $\handwritten{\mathcal{E}}$\handwritten{.}} `:

```tex
\handwritten{A}
```

39. handwritten, following `{\mathcal{E}}$\handwritten{.}} \handwritten{A}lors $`:

```tex
\handwritten{\mathcal{E}}
```

40. handwritten, following `uctive d'une famille filtrante croissante de sous- $`:

```tex
\handwritten{\mathcal{O}}
```

41. handwritten, following `cal{O}}_S$-Modules quasi-cohérents de type fini de $`:

```tex
\handwritten{\mathcal{E}}
```

42. handwritten, following `e fini de $\handwritten{\mathcal{E}}$ stables sous $`:

```tex
\handwritten{G}
```

43. handwritten, following `$.}  C'est une conséquence immédiate de (11.9) car $`:

```tex
\handwritten{\mathcal{E}}
```

44. deleted, following `diate de (11.9) car $\handwritten{\mathcal{E}}$ est `:

```tex
\deleted{engendré par ses sections (EGA I 1.4.\unsure{1}) et car l'ensemble des sous-$\handwritten{\mathcal{O}}_S$-Modules quasi-cohérents de type fini de $\handwritten{\mathcal{E}}$ stables sous $G$ est stable par engendrement.}
```

45. handwritten, following ` (EGA I 1.4.\unsure{1}) et car l'ensemble des sous-$`:

```tex
\handwritten{\mathcal{O}}
```

46. handwritten, following `cal{O}}_S$-Modules quasi-cohérents de type fini de $`:

```tex
\handwritten{\mathcal{E}}
```

47. inserted, following `{E}}$ stables sous $G$ est stable par engendrement.}`:

```tex
\inserted{\handwritten{limite inductive de ses sous-Modules quasi-cohérents de type fini (EGA I 9.4.9. , $\overline{\underline{\mathrm{IV}}}$ 1.7.7.)}}
```

48. handwritten, following `les sous $G$ est stable par engendrement.}\inserted{`:

```tex
\handwritten{limite inductive de ses sous-Modules quasi-cohérents de type fini (EGA I 9.4.9. , $\overline{\underline{\mathrm{IV}}}$ 1.7.7.)}
```

49. handwritten, following `$ de $S$, il existe un morphisme fidèlement plat $U'`:

```tex
\handwritten{\to}
```

50. handwritten, following `en{\to}U$, avec $U'$ affine d'anneau $A'$, tel que $`:

```tex
\handwritten{\mathcal{E}\otimes}
```

51. handwritten, following `èse que $G$ soit plat sur $S$ (ce qui implique que $`:

```tex
\handwritten{\mathcal{A}}
```

52. deleted, following `written{\mathcal{A}}(G)$ est plat); voir à ce sujet `:

```tex
\deleted{un exposé de Serre dans SGA\inserted{\handwritten{6}}(1966/67).}
```

53. inserted, following `voir à ce sujet \deleted{un exposé de Serre dans SGA`:

```tex
\inserted{\handwritten{6}}
```

54. handwritten, following `sujet \deleted{un exposé de Serre dans SGA\inserted{`:

```tex
\handwritten{6}
```

55. handwritten, following ` Serre dans SGA\inserted{\handwritten{6}}(1966/67).}`:

```tex
\handwritten{\unsure{1}}
```

56. inserted, following `\handwritten{6}}(1966/67).}\handwritten{\unsure{1}} `:

```tex
\inserted{\handwritten{J.P. Serre, \unsure{Le|le} \unsure{Groupes|Groupe} de Grothendieck des schémas en groupes réductifs déployés, Pub. Math. n° \unsure{34|39}, p. 37-52.}}
```

57. handwritten, following `en{6}}(1966/67).}\handwritten{\unsure{1}} \inserted{`:

```tex
\handwritten{J.P. Serre, \unsure{Le|le} \unsure{Groupes|Groupe} de Grothendieck des schémas en groupes réductifs déployés, Pub. Math. n° \unsure{34|39}, p. 37-52.}
```

58. deleted, following `éployés, Pub. Math. n° \unsure{34|39}, p. 37-52.}}  `:

```tex
\deleted{\uline{Proposition 11.11.- Soient $k$ un corps, $G$ un \deleted{corps} $k$-groupe algébrique. Pour que $G$ soit affine, il faut et il suffit qu'il existe un espace vectoriel de dimension finie $V$, et une immersion fermée de $G$ dans $\underline{\mathrm{GL}}_k(V)$ qui soit un morphisme de $k$-groupes.}}
```

59. deleted, following `ine{Proposition 11.11.- Soient $k$ un corps, $G$ un `:

```tex
\deleted{corps}
```

60. deleted, following `GL}}_k(V)$ qui soit un morphisme de $k$-groupes.}}  `:

```tex
\deleted{S'il existe un espace vectoriel $V$ de dimension finie et une immersion fermée $u:G\handwritten{\to}\underline{\mathrm{GL}}_k(V)$, puisque $\underline{\mathrm{GL}}_k(V)$ est affine (Exp. I, 4.5), il en est de même de $G$ (EGA I 4.2.3).}
```

61. handwritten, following ` $V$ de dimension finie et une immersion fermée $u:G`:

```tex
\handwritten{\to}
```

62. deleted, following ` I, 4.5), il en est de même de $G$ (EGA I 4.2.3).}  `:

```tex
\deleted{Réciproquement, supposons $G$ affine. Notons $A$ l'algèbre de $G$. Puisque $G$ opère sur lui-même par translations à gauche, il opère aussi sur $A$, cette opération se traduisant par l'application \deleted{\unsure{diagon|diagona}} diagonale $\handwritten{\Delta}:A\handwritten{\longrightarrow}A\handwritten{\otimes}_k A$. D'après (11.1\handwritten{0}), $A$ (en tant qu'espace vectoriel) est réunion d'une famille filtrante croissante $(V_i)_{i\handwritten{\in}I}$ de sous-espaces vectoriels de dimension finie stables sous $G$.}
```

63. deleted, following `A$, cette opération se traduisant par l'application `:

```tex
\deleted{\unsure{diagon|diagona}}
```

64. handwritten, following `cation \deleted{\unsure{diagon|diagona}} diagonale $`:

```tex
\handwritten{\Delta}
```

65. handwritten, following `e{diagon|diagona}} diagonale $\handwritten{\Delta}:A`:

```tex
\handwritten{\longrightarrow}
```

66. handwritten, following `\handwritten{\Delta}:A\handwritten{\longrightarrow}A`:

```tex
\handwritten{\otimes}
```

67. handwritten, following `ightarrow}A\handwritten{\otimes}_k A$. D'après (11.1`:

```tex
\handwritten{0}
```

68. handwritten, following `réunion d'une famille filtrante croissante $(V_i)_{i`:

```tex
\handwritten{\in}
```

69. deleted, following `es vectoriels de dimension finie stables sous $G$.} `:

```tex
\deleted{\unsure{Puisque $G$ est de type fini sur $k$, $A$ est de type fini sur $k$, donc il existe} $i_{\unsure{o|0}}\handwritten{\in}I$ tel que $V_{i_o}$ \unsure{engendre $A$ comme algèbre. L'opération de $G$ sur}}
```

70. handwritten, following `type fini sur $k$, donc il existe} $i_{\unsure{o|0}}`:

```tex
\handwritten{\in}
```


## Scan 49

Start (UTC): 2026-11-13T20:15:22.020186+00:00

End (UTC): 2026-11-13T20:18:03.079318+00:00

Crop-first words/accents: heading « Proposition 11.11. », Soient→Soit with cancelled k un corps, « schéma en » cancelled, « groupes quasi-compact » altered to groupe plus « algébrique sur le » and « corps », deleted sur. « Les conditions suivantes sont équivalentes », « quasi-affine », « faire opérer », repeated « fidèlement », k- added before schéma, « un vectoriel », « pas nécessairement de dimension finie », deleted « (si G est de type fini sur k) », « isomorphe à », « fermé ». « Démonstration », « trivialement », « opère », « lui-même », « translations à gauche », replacement « sur X quasi-compact et quasi-séparé sur k, il opère aussi », cancelled earlier fidèlement/quasi-affine/enveloppe wording, « grâce au fait », « morphisme structural », « changement de base », « enveloppe affine », « évidemment compatible », « ceci dit », « immersion ouverte », « ce qui revient au même », « implication ». « Supposons maintenant », deleted « que G est de type fini, et », inserted « (iv), i.e. », « en vertu de », « sous-espaces », « dimension », « noyau », « action induite », « sous-schéma fermé », « hypothèse », « s'exprime aussitôt », « l'intersection », « sous-groupe unité », « noethé- » at page end. Acute accents in schéma/algébrique/équivalentes/opérer/nécessairement/fermé/Démonstration/séparé/évidemment/unité/noethé; grave in fidèlement/opère/à/hypothèse; circumflex in même/grâce/aussitôt. The page-end noethé has its acute over the final e, while the earlier e is unaccented. The last cancelled fragment ends « K_i=e (grou »; no completion is visible. All direct-image O glyphs are typed O with an underline; Gamma, stars and arrows are handwritten. The initial S of Supposons and p/m in sous-espaces/dimension appear retouched by hand. A single long vertical pen stroke groups the conditions at left.


Read the five conditions and both proof paragraphs line by line, then rechecked the heading corrections, cancelled (v) qualification, the two x-overtyped lines and the last paragraph at enlargement. Added the handwritten overstroke to the initial S of Supposons. The subscript in the last cancelled K=e fragment differs from the ordinary dotted i elsewhere: its visible shape has a broad top serif and no separate dot. Changed K_i to K_{unsure 1|i|l}; the primary candidate follows that shape rather than the family notation in the surrounding sentence. The cancellation may hide a dot, so i remains a candidate. All other indexed K and V have visible i dots and are unchanged. There are no j indices. The x-overtyped formula actually stops after Spec(Gamma(; no missing arguments or closing parentheses were supplied. Its Gamma-like stroke was compared directly with the handwritten Gamma in the live formula, and the unclear final e of enveloppe remains doubtful.

Correction placements: Soient/Soit, k un corps deletion, schéma en deletion, plural s/quasi-compact deletion, algébrique sur le and corps insertions, sur deletion; k- above schéma; the entire (si G est de type fini sur k), deletion; typed replacement sur X quasi-compact et quasi-séparé sur k, il opère aussi; all implication arrows; the handwritten Gamma/stars/arrows; (iv), i.e. replacing que G est de type fini, et; commas after Alors and 11.10; p in sous-espaces and m in dimension; Aut's cancelled parenthesized argument and inserted V_i subscript; the final cancelled K equation and truncated grou. All are represented. The long left grouping stroke is present.

Formula audit: GL(n)_k has n inside parentheses and k outside underneath; implication arrows all point right and have doubled shafts. Gamma(X,underlined O_X) occurs three times as a complete formula (the first, inside Spec, and after V=), plus the incomplete cancelled occurrence. The direct image is f_* with star below; f:X→Spec k and S→Spec k have rightward arrows; both X→X' arrows and the standalone X' are primed. V_i, K_i and the Aut correction indices were inspected individually; the doubtful last K index is explicitly distinguished. Every O is a typed oval with its own underline, not a handwritten looped O. GL, Aut, V, K, X, G and heading capitals have single typewriter strokes; no double-struck or bold alphabet was substituted. Accents are retained including the final noethé- (first e unaccented), aussitôt and the repeated fidèlement/opère. The word vectoriel has no supplied espace.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
}
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
{\unsure{1|
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
|l}}
```


### Every delimited formula, in page-file order

1. inline

```tex
k
```

2. inline

```tex
G
```

3. inline

```tex
k
```

4. inline

```tex
G
```

5. inline

```tex
G
```

6. inline

```tex
G
```

7. inline

```tex
k
```

8. inline

```tex
G
```

9. inline

```tex
k
```

10. inline

```tex
G
```

11. inline

```tex
k
```

12. inline

```tex
G
```

13. inline

```tex
\mathrm{GL}(n)_k
```

14. inline

```tex
\handwritten{\Rightarrow}
```

15. inline

```tex
\handwritten{\Rightarrow}
```

16. inline

```tex
G
```

17. inline

```tex
\handwritten{\Rightarrow}
```

18. inline

```tex
G
```

19. inline

```tex
X
```

20. inline

```tex
k
```

21. inline

```tex
X'=\operatorname{Spec}(\handwritten{\Gamma}(
```

22. inline

```tex
X
```

23. inline

```tex
k
```

24. inline

```tex
\handwritten{\Gamma}(X,\underline{O}_X)
```

25. inline

```tex
f_{\handwritten{*}}(\underline{O}_X)
```

26. inline

```tex
f:X\handwritten{\to}\operatorname{Spec}k
```

27. inline

```tex
S\handwritten{\to}\operatorname{Spec}k
```

28. inline

```tex
X'=\operatorname{Spec}(\handwritten{\Gamma}(X,\underline{O}_X))
```

29. inline

```tex
X\handwritten{\to}X'
```

30. inline

```tex
G
```

31. inline

```tex
X
```

32. inline

```tex
X\handwritten{\to}X'
```

33. inline

```tex
G
```

34. inline

```tex
X
```

35. inline

```tex
X'
```

36. inline

```tex
V=\handwritten{\Gamma}(X,\underline{O}_X)
```

37. inline

```tex
\handwritten{\Rightarrow}
```

38. inline

```tex
G
```

39. inline

```tex
G
```

40. inline

```tex
V
```

41. inline

```tex
V
```

42. inline

```tex
V_i
```

43. inline

```tex
G
```

44. inline

```tex
K_i
```

45. inline

```tex
G
```

46. inline

```tex
V_i
```

47. inline

```tex
G\handwritten{\to}\underline{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i)}}
```

48. inline

```tex
K_i
```

49. inline

```tex
G
```

50. inline

```tex
G
```

51. inline

```tex
K_{\unsure{1|i|l}}=e
```

52. inline

```tex
K_i
```

53. inline

```tex
G
```

54. inline

```tex
G
```

### Every i/j index occurrence (local TeX contexts)

1. `ten{p}aces vectoriels $V_i$ de di\handwritten{m}en`
2. `s l'action de $G$. Si $K_i$ est le noyau de l'acti`
3. `on induite de $G$ sur $V_i$ , i.e. de $G\handwritt`
4. `\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i`
5. `_i}}}\deleted{\unsure{(V_i)}}$, alors $K_i$ est un`
6. `nsure{(V_i)}}$, alors $K_i$ est un sous-schéma fer`
7. `}} l'intersection des $K_i$ est le sous-groupe uni`

### Handwritten and correction placements

1. handwritten, following `\scanpage{49} \mspage{`:

```tex
\handwritten{17}
```

2. margin, following `\scanpage{49} \mspage{\handwritten{17}} `:

```tex
\margin{\handwritten{\figure{\begin{tikzpicture}\draw (0,0)--(.03,-5);\end{tikzpicture}}}}
```

3. handwritten, following `\scanpage{49} \mspage{\handwritten{17}} \margin{`:

```tex
\handwritten{\figure{\begin{tikzpicture}\draw (0,0)--(.03,-5);\end{tikzpicture}}}
```

4. deleted, following `;\end{tikzpicture}}}} \uline{Proposition} 11.11. Soi`:

```tex
\deleted{\unsure{ent}}
```

5. handwritten, following `\uline{Proposition} 11.11. Soi\deleted{\unsure{ent}}`:

```tex
\handwritten{t}
```

6. deleted, following `on} 11.11. Soi\deleted{\unsure{ent}}\handwritten{t} `:

```tex
\deleted{$k$ un corps}
```

7. deleted, following `ent}}\handwritten{t} \deleted{$k$ un corps}, $G$ un `:

```tex
\deleted{schéma en }
```

8. deleted, following `ted{$k$ un corps}, $G$ un \deleted{schéma en }groupe`:

```tex
\deleted{s quasi-compact}
```

9. inserted, following ` \deleted{schéma en }groupe\deleted{s quasi-compact}`:

```tex
\inserted{\handwritten{algébrique sur le}}
```

10. handwritten, following `schéma en }groupe\deleted{s quasi-compact}\inserted{`:

```tex
\handwritten{algébrique sur le}
```

11. deleted, following `-compact}\inserted{\handwritten{algébrique sur le}} `:

```tex
\deleted{sur}
```

12. inserted, following `erted{\handwritten{algébrique sur le}} \deleted{sur}`:

```tex
\inserted{\handwritten{corps}}
```

13. handwritten, following `dwritten{algébrique sur le}} \deleted{sur}\inserted{`:

```tex
\handwritten{corps}
```

14. inserted, following `e.  (iii) On peut faire opérer $G$ fidèlement sur un`:

```tex
\inserted{$k$-}
```

15. deleted, following `nsure{pas} nécessairement de dimension finie).  (v) `:

```tex
\deleted{(si $G$ est de type fini sur $k$),}
```

16. handwritten, following `mathrm{GL}(n)_k$ .  \uline{Démonstration}. On a (i)$`:

```tex
\handwritten{\Rightarrow}
```

17. handwritten, following `handwritten{\Rightarrow}$(ii) trivialement, et (ii)$`:

```tex
\handwritten{\Rightarrow}
```

18. handwritten, following ` sur lui-même par translations à gauche. On a (iii)$`:

```tex
\handwritten{\Rightarrow}
```

19. deleted, following `ii)$\handwritten{\Rightarrow}$(iv) car si $G$ opère `:

```tex
\deleted{fidèlement sur $X$ quasi-affine sur $k$, alors il opère fidèlement sur l'envelopp\unsure{e} affine $X'=\operatorname{Spec}(\handwritten{\Gamma}($}
```

20. handwritten, following `l'envelopp\unsure{e} affine $X'=\operatorname{Spec}(`:

```tex
\handwritten{\Gamma}
```

21. inserted, following `fine $X'=\operatorname{Spec}(\handwritten{\Gamma}($}`:

```tex
\inserted{sur $X$ quasi-compact et quasi-séparé sur $k$, il opère aussi}
```

22. handwritten, following `i-séparé sur $k$, il opère aussi} sur le vectoriel $`:

```tex
\handwritten{\Gamma}
```

23. handwritten, following `rline{O}_X)$, grâce au fait que la formation de $f_{`:

```tex
\handwritten{*}
```

24. handwritten, following `tion de $f_{\handwritten{*}}(\underline{O}_X)$ ($f:X`:

```tex
\handwritten{\to}
```

25. handwritten, following `sme structural) commute à tout changement de base $S`:

```tex
\handwritten{\to}
```

26. handwritten, following `père sur l'enveloppe affine $X'=\operatorname{Spec}(`:

```tex
\handwritten{\Gamma}
```

27. handwritten, following `}(X,\underline{O}_X))$, et le morphisme canonique $X`:

```tex
\handwritten{\to}
```

28. handwritten, following `on de $G$; ceci dit, si $X$ est quasi-affine i.e. $X`:

```tex
\handwritten{\to}
```

29. handwritten, following `X'$, ou ce qui revient au même, sur le vectoriel $V=`:

```tex
\handwritten{\Gamma}
```

30. handwritten, following `underline{O}_X)$, ce qui prouve l'implication (iii)$`:

```tex
\handwritten{\Rightarrow}
```

31. handwritten, following `'implication (iii)$\handwritten{\Rightarrow}$(iv).  `:

```tex
\handwritten{S}
```

32. deleted, following `ghtarrow}$(iv).  \handwritten{S}upposons maintenant `:

```tex
\deleted{que $G$ est de type fini, et}
```

33. inserted, following `ns maintenant \deleted{que $G$ est de type fini, et}`:

```tex
\inserted{\handwritten{(iv), i.e.}}
```

34. handwritten, following `ant \deleted{que $G$ est de type fini, et}\inserted{`:

```tex
\handwritten{(iv), i.e.}
```

35. handwritten, following `que $G$ opère fidèlement sur le vectoriel $V$. Alors`:

```tex
\handwritten{,}
```

36. handwritten, following `vectoriel $V$. Alors\handwritten{,}en vertu de 11.10`:

```tex
\handwritten{,}
```

37. handwritten, following `10\handwritten{,}$V$ est limite inductive de sous-es`:

```tex
\handwritten{p}
```

38. handwritten, following `de sous-es\handwritten{p}aces vectoriels $V_i$ de di`:

```tex
\handwritten{m}
```

39. handwritten, following `au de l'action induite de $G$ sur $V_i$ , i.e. de $G`:

```tex
\handwritten{\to}
```

40. inserted, following ` $G\handwritten{\to}\underline{\operatorname{Aut}}_{`:

```tex
\inserted{\handwritten{V_i}}
```

41. handwritten, following `itten{\to}\underline{\operatorname{Aut}}_{\inserted{`:

```tex
\handwritten{V_i}
```

42. deleted, following `e{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}`:

```tex
\deleted{\unsure{(V_i)}}
```

43. deleted, following `opère fidèlement s'exprime aussitôt par le fait que `:

```tex
\deleted{$K_{\unsure{1|i|l}}=e$ (\unsure{grou}}
```


## Scan 50

Start (UTC): 2026-11-13T20:18:03.146329+00:00

End (UTC): 2026-11-13T20:21:33.495369+00:00

Crop-first words/accents: opening « rien, il s'ensuit », « déjà réduit au groupe unité », « monomorphisme », « immersion fermée », « en vertu de (1.4.2) », « trivialement », « cela prouve 11.11 [cancelled punctuation] pour G de type fini ». Cancelled draft: « Prenons maintenant le cas général, où il reste à prouver », « démonstration précédente », « plus petit » added and looped, « sous-groupe fermé », inserted « peut », « par lequel se factoriser », deleted « (existe », « un tel groupe existe », deleted « puisque », « comme intersection », « invarie », « morphisme correspondant », « De cette façon », « système projectif », « morphisme naturel », « lui-même », « L'hypothèse », underlined « fidèlement », « s'exprime », extra deleted letter after par, « On a donc trouvéun » with a little separating slash, « schéma quasi-compact » plus « et séparé », « quasi-affine », « faisceau structural », « est ample », « En d'autres termes », « canonique », « immersion ouverte », « de façon naturelle », « grâce à », « évidemment dominant », « il reste à prouver que c'est un isomorphisme », « résulte » followed by cancelled « ra de ». Lemma « Soient H un schéma en groupes sur un corps » with k inserted, deleted « G un sous- », « Alors tout sous-schéma en groupes ouvert » plus G, « aussi fermé ». Proof: « Il revient au même », « l'ensemble H-G », « voisinage », « points » with deleted comma before x, « Or », « définissant », « universellement ». Acute accents: déjà's first syllable, réduit, unité, fermée, général, démonstration, précédente, fermé, trouvé, schéma, séparé, évidemment, résulte, définissant; grave déjà's final à, où, à, système, hypothèse, fidèlement; circumflex même/grâce. Cedilla in façon. First handwritten Aut replacement index is i; j descenders in V_j and G_j differ from i in V_i/G_i. The superset-like sign has a clear right-facing outer curve and is repeated in a circled left-margin note; limit arrow points left. The last text stops at universellement.


Read the continuation and the whole cancelled draft, including the lemma and its incomplete proof. Enlarged the Aut substitutions, the containment sign, the lemma corrections, the right page edge after (iv)⇒(i), and the contact between trouvé and un. The page edge actually preserves the closing parenthesis and a low period; retained both. Added the small slanting separator stroke between trouvé and un, rather than silently representing only a normal space. No additional text was supplied after universellement. The cancelled draft remains cancelled, including its lemma and proof, while the first paragraph remains live.

Correction audit: all three locally cancelled Aut arguments and their replacements, deleted punctuation after 11.11, plus petit insertion, peut insertion, (existe deletion, puisque deletion, the heavy containment sign and its circled repetition, extra cancelled r after par, et séparé addition, handwritten d of d'autres, ra de deletion after résulte, corrected G/H in the lemma, inserted k and punctuation, G un sous- deletion, inserted G after ouvert, and cancelled punctuation before x were checked in place. The long lemma grouping stroke is present. The whole-draft diagonal cancellation is represented by the deletion state; smaller readable cancellations remain nested within it.

Indices and formula audit: opening K_i; the first corrected Aut_{V_i}; G_i and Aut(V_i); the second corrected Aut_{V_i}; the third cancelled Aut(V_i) and typed replacement Aut_{V_i}; V_j superset V_i; G_j, V_i, G_j→Aut_{V_i}, G_i, the family G_i and limit G_i. Every j has a descending hook, unlike the dotted i. The natural map points G→G', while the arrow below lim points left. Both following G→G' and G→H maps point right. H=Spec Gamma(G,underlined O_G) has no outer parentheses around the Spec argument; H-G is a plain minus, and k'/k uses a slash. Spec k'→Spec k has a prime on the first k only. All implication arrows point right and have two shafts. Ordinary typed capitals in GL/Aut/Spec and the lemma were checked separately. The H in the lemma is a handwritten replacement over a cancelled G-like glyph; the other H letters are ordinary typed H. Gamma is handwritten, O_G is typed and underlined. Accents, including déjà, réduit, unité, général, précédente, façon, système, hypothèse, fidèlement, séparé, grâce and définissant, match the crops. No other reading change.


### Changes

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
\handwritten{\makebox[0pt][l]{\raisebox{-.5ex}{\begin{tikzpicture}[x=.25cm,y=.25cm]\draw
```

Before -> after (literal TeX spans; ∅ means no characters):

```text
∅
->
(0,-.5)--(.55,1);\end{tikzpicture}}}}
```


### Every delimited formula, in page-file order

1. inline

```tex
K_i
```

2. inline

```tex
G\handwritten{\to}\underline{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i)}}
```

3. inline

```tex
\handwritten{\Rightarrow}
```

4. inline

```tex
\handwritten{\Rightarrow}
```

5. inline

```tex
G
```

6. inline

```tex
\handwritten{\Rightarrow}
```

7. inline

```tex
G_i
```

8. inline

```tex
\operatorname{Aut}(V_i)
```

9. inline

```tex
G\handwritten{\to}\underline{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i)}}
```

10. inline

```tex
G\handwritten{\to}\deleted{\unsure{\operatorname{Aut}(V_i)}}\inserted{\underline{\operatorname{Aut}}_{V_i}}
```

11. inline

```tex
V_j\handwritten{\supset}V_i
```

12. inline

```tex
G_j
```

13. inline

```tex
V_i
```

14. inline

```tex
G_j\handwritten{\to}\underline{\operatorname{Aut}}_{V_i}
```

15. inline

```tex
G_i
```

16. inline

```tex
G_i
```

17. inline

```tex
k
```

18. inline

```tex
G\handwritten{\longrightarrow}G'=\underset{\handwritten{\longleftarrow}}{\lim}G_i
```

19. inline

```tex
G'
```

20. inline

```tex
G
```

21. inline

```tex
V
```

22. inline

```tex
G\handwritten{\to}G'
```

23. inline

```tex
G
```

24. inline

```tex
G
```

25. inline

```tex
H=\operatorname{Spec}\handwritten{\Gamma}(G,\underline{O}_G)
```

26. inline

```tex
G\handwritten{\to}H
```

27. inline

```tex
H
```

28. inline

```tex
G\handwritten{\to}H
```

29. inline

```tex
\supset
```

30. inline

```tex
\deleted{\unsure{G}}\handwritten{H}
```

31. inline

```tex
k
```

32. inline

```tex
G
```

33. inline

```tex
G
```

34. inline

```tex
H
```

35. inline

```tex
H-G
```

36. inline

```tex
x
```

37. inline

```tex
k'/k
```

38. inline

```tex
\operatorname{Spec}k'\handwritten{\to}\operatorname{Spec}k
```

### Every i/j index occurrence (local TeX contexts)

1. `s'ensuit que l'un des $K_i$ est déjà réduit au gro`
2. `\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i`
3. `_i}}}\deleted{\unsure{(V_i)}}$ est un monomorphism`
4. `tion précédente, soit $G_i$ le\inserted{plus petit`
5. `de $\operatorname{Aut}(V_i)$ par lequel\inserted{p`
6. `\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i`
7. `_i}}}\deleted{\unsure{(V_i)}}$ \deleted{(existe} (`
8. `ure{\operatorname{Aut}(V_i)}}\inserted{\underline{`
9. `line{\operatorname{Aut}}_{V_i}}$). Si $V_j\handwritten`
10. `me{Aut}}_{V_i}}$). Si $V_j\handwritten{\supset}V_i`
11. `_j\handwritten{\supset}V_i$, on voit alors tout de`
12. `ors tout de suite que $G_j$ invarie $V_i$ , et que`
13. `ite que $G_j$ invarie $V_i$ , et que le morphisme `
14. `rphisme correspondant $G_j\handwritten{\to}\underl`
15. `line{\operatorname{Aut}}_{V_i}$ se factorise par $G_i$`
16. `_i}$ se factorise par $G_i$ . De cette façon, les `
17. `. De cette façon, les $G_i$ forment un système pro`
18. `{\longleftarrow}}{\lim}G_i$ , où $G'$ est lui-même`

### Handwritten and correction placements

1. handwritten, following `\scanpage{50} \mspage{`:

```tex
\handwritten{18}
```

2. handwritten, following `s $K_i$ est déjà réduit au groupe unité, donc que $G`:

```tex
\handwritten{\to}
```

3. inserted, following ` $G\handwritten{\to}\underline{\operatorname{Aut}}_{`:

```tex
\inserted{\handwritten{V_i}}
```

4. handwritten, following `itten{\to}\underline{\operatorname{Aut}}_{\inserted{`:

```tex
\handwritten{V_i}
```

5. deleted, following `e{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}`:

```tex
\deleted{\unsure{(V_i)}}
```

6. handwritten, following ` fermée en vertu de (1.4.2), ce qui prouve que (iv)$`:

```tex
\handwritten{\Rightarrow}
```

7. handwritten, following `e que (iv)$\handwritten{\Rightarrow}$(v). Comme (v)$`:

```tex
\handwritten{\Rightarrow}
```

8. deleted, following `ten{\Rightarrow}$(i) trivialement, cela prouve 11.11`:

```tex
\deleted{\unsure{.}}
```

9. deleted, following `e 11.11\deleted{\unsure{.}} pour $G$ de type fini.  `:

```tex
\deleted{Prenons maintenant le cas général, où il reste à prouver que (iv)$\handwritten{\Rightarrow}$(i). Avec les notations de la démonstration précédente, soit $G_i$ le\inserted{plus petit} sous-groupe fermé de $\operatorname{Aut}(V_i)$ par lequel\inserted{peut} se factoriser $G\handwritten{\to}\underline{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}\deleted{\unsure{(V_i)}}$ \deleted{(existe} (un tel groupe existe, \deleted{puisque} comme intersection de tous ceux par lesquels se factorise $G\handwritten{\to}\deleted{\unsure{\operatorname{Aut}(V_i)}}\inserted{\underline{\operatorname{Aut}}_{V_i}}$). Si $V_j\handwritten{\supset}V_i$, on voit alors tout de suite que $G_j$ invarie $V_i$ , et que le morphisme correspondant $G_j\handwritten{\to}\underline{\operatorname{Aut}}_{V_i}$ se factorise par $G_i$ . De cette façon, les $G_i$ forment un système projectif de groupes affines sur $k$, et on a un morphisme naturel $G\handwritten{\longrightarrow}G'=\underset{\handwritten{\longleftarrow}}{\lim}G_i$ , où $G'$ est lui-même un groupe affine (EGA IV 8.2.3). L'hypothèse que $G$ opère \uline{fidèlement} sur $V$ s'exprime alors par\deleted{\unsure{r}} le fait que $G\handwritten{\to}G'$ est un monomorphisme. On a donc trouvé\handwritten{\makebox[0pt][l]{\raisebox{-.5ex}{\begin{tikzpicture}[x=.25cm,y=.25cm]\draw (0,-.5)--(.55,1);\end{tikzpicture}}}}un monomorphisme de $G$ dans un schéma affine, ce qui implique que le schéma quasi-compact\inserted{et séparé} $G$ est quasi-affine, i.e. que son faisceau structural est ample, en vertu de EGA IV 18.12.17 . En \handwritten{d}'autres termes, posant $H=\operatorname{Spec}\handwritten{\Gamma}(G,\underline{O}_G)$ , le morphisme canonique $G\handwritten{\to}H$ est une immersion ouverte. Notons maintenant que $H$ est de façon naturelle un schéma en groupes, et $G\handwritten{\to}H$ un homomorphisme de groupes, grâce à 11.2 . Cet homomorphisme est évidemment dominant, il reste à prouver que c'est un isomorphisme, ce qui résulte\deleted{\unsure{ra de}} du lemme suivant:}
```

10. handwritten, following `nant le cas général, où il reste à prouver que (iv)$`:

```tex
\handwritten{\Rightarrow}
```

11. inserted, following `ations de la démonstration précédente, soit $G_i$ le`:

```tex
\inserted{plus petit}
```

12. inserted, following `groupe fermé de $\operatorname{Aut}(V_i)$ par lequel`:

```tex
\inserted{peut}
```

13. handwritten, following `ut}(V_i)$ par lequel\inserted{peut} se factoriser $G`:

```tex
\handwritten{\to}
```

14. inserted, following ` $G\handwritten{\to}\underline{\operatorname{Aut}}_{`:

```tex
\inserted{\handwritten{V_i}}
```

15. handwritten, following `itten{\to}\underline{\operatorname{Aut}}_{\inserted{`:

```tex
\handwritten{V_i}
```

16. deleted, following `e{\operatorname{Aut}}_{\inserted{\handwritten{V_i}}}`:

```tex
\deleted{\unsure{(V_i)}}
```

17. deleted, following `serted{\handwritten{V_i}}}\deleted{\unsure{(V_i)}}$ `:

```tex
\deleted{(existe}
```

18. deleted, following `e{(V_i)}}$ \deleted{(existe} (un tel groupe existe, `:

```tex
\deleted{puisque}
```

19. handwritten, following `tersection de tous ceux par lesquels se factorise $G`:

```tex
\handwritten{\to}
```

20. deleted, following `s ceux par lesquels se factorise $G\handwritten{\to}`:

```tex
\deleted{\unsure{\operatorname{Aut}(V_i)}}
```

21. inserted, following `itten{\to}\deleted{\unsure{\operatorname{Aut}(V_i)}}`:

```tex
\inserted{\underline{\operatorname{Aut}}_{V_i}}
```

22. handwritten, following `ted{\underline{\operatorname{Aut}}_{V_i}}$). Si $V_j`:

```tex
\handwritten{\supset}
```

23. handwritten, following `varie $V_i$ , et que le morphisme correspondant $G_j`:

```tex
\handwritten{\to}
```

24. handwritten, following `pes affines sur $k$, et on a un morphisme naturel $G`:

```tex
\handwritten{\longrightarrow}
```

25. handwritten, following `naturel $G\handwritten{\longrightarrow}G'=\underset{`:

```tex
\handwritten{\longleftarrow}
```

26. deleted, following `opère \uline{fidèlement} sur $V$ s'exprime alors par`:

```tex
\deleted{\unsure{r}}
```

27. handwritten, following `exprime alors par\deleted{\unsure{r}} le fait que $G`:

```tex
\handwritten{\to}
```

28. handwritten, following `itten{\to}G'$ est un monomorphisme. On a donc trouvé`:

```tex
\handwritten{\makebox[0pt][l]{\raisebox{-.5ex}{\begin{tikzpicture}[x=.25cm,y=.25cm]\draw (0,-.5)--(.55,1);\end{tikzpicture}}}}
```

29. inserted, following ` affine, ce qui implique que le schéma quasi-compact`:

```tex
\inserted{et séparé}
```

30. handwritten, following `uctural est ample, en vertu de EGA IV 18.12.17 . En `:

```tex
\handwritten{d}
```

31. handwritten, following `tten{d}'autres termes, posant $H=\operatorname{Spec}`:

```tex
\handwritten{\Gamma}
```

32. handwritten, following `mma}(G,\underline{O}_G)$ , le morphisme canonique $G`:

```tex
\handwritten{\to}
```

33. handwritten, following `$ est de façon naturelle un schéma en groupes, et $G`:

```tex
\handwritten{\to}
```

34. deleted, following ` à prouver que c'est un isomorphisme, ce qui résulte`:

```tex
\deleted{\unsure{ra de}}
```

35. margin, following ` résulte\deleted{\unsure{ra de}} du lemme suivant:} `:

```tex
\margin{\handwritten{\figure{\begin{tikzpicture}
\draw (0,0) ellipse (.6 and .38);\node at (0,0) {$\supset$};
\end{tikzpicture}}}}
```

36. handwritten, following `\deleted{\unsure{ra de}} du lemme suivant:} \margin{`:

```tex
\handwritten{\figure{\begin{tikzpicture}
\draw (0,0) ellipse (.6 and .38);\node at (0,0) {$\supset$};
\end{tikzpicture}}}
```

37. deleted, following `);\node at (0,0) {$\supset$}; \end{tikzpicture}}}}  `:

```tex
\deleted{\uline{Lemme} 11.11.1. Soient $\deleted{\unsure{G}}\handwritten{H}$ un schéma en groupes sur un corps\inserted{$k$}\handwritten{.} \deleted{$G$ un sous-} Alors tout sous-schéma en groupes ouvert\inserted{$G$} de $H$ est aussi fermé.}
```

38. deleted, following `icture}}}}  \deleted{\uline{Lemme} 11.11.1. Soient $`:

```tex
\deleted{\unsure{G}}
```

39. handwritten, following `{\uline{Lemme} 11.11.1. Soient $\deleted{\unsure{G}}`:

```tex
\handwritten{H}
```

40. inserted, following `}}\handwritten{H}$ un schéma en groupes sur un corps`:

```tex
\inserted{$k$}
```

41. handwritten, following `{H}$ un schéma en groupes sur un corps\inserted{$k$}`:

```tex
\handwritten{.}
```

42. deleted, following `n groupes sur un corps\inserted{$k$}\handwritten{.} `:

```tex
\deleted{$G$ un sous-}
```

43. inserted, following `$ un sous-} Alors tout sous-schéma en groupes ouvert`:

```tex
\inserted{$G$}
```

44. margin, following `oupes ouvert\inserted{$G$} de $H$ est aussi fermé.} `:

```tex
\margin{\handwritten{\figure{\begin{tikzpicture}\draw (0,0)--(.03,-.8);\end{tikzpicture}}}}
```

45. handwritten, following `vert\inserted{$G$} de $H$ est aussi fermé.} \margin{`:

```tex
\handwritten{\figure{\begin{tikzpicture}\draw (0,0)--(.03,-.8);\end{tikzpicture}}}
```

46. deleted, following `icture}\draw (0,0)--(.03,-.8);\end{tikzpicture}}}}  `:

```tex
\deleted{Il revient au même de dire que l'ensemble $H-G$ est ouvert, i.e. est un voisinage de chacun de ses points\deleted{\unsure{,}} $x$ . Or , toute extension de corps $k'/k$ définissant un morphisme $\operatorname{Spec}k'\handwritten{\to}\operatorname{Spec}k$ qui est universellement}
```

47. deleted, following `uvert, i.e. est un voisinage de chacun de ses points`:

```tex
\deleted{\unsure{,}}
```

48. handwritten, following `'/k$ définissant un morphisme $\operatorname{Spec}k'`:

```tex
\handwritten{\to}
```


## Final cross-page reconciliation

Start (UTC): 2026-11-13T20:27:41.227724+00:00

End (UTC): 2026-11-13T20:28:47.791023+00:00

Compared the recurring readings recorded in the nine audits and the notation table, and reopened the enlarged first-page letters and scan-43 notation crop. The same rounded handwritten A/a ambiguity is marked at the first occurrence on every affected page (43–48). Clear E, F, O, Hom, V and W forms have consistent encodings; the darker W on 46 keeps its local alternative. The symmetric-algebra S on 44 and 45 has matching reinforced bowl strokes and is consistently mathbb S. Each double-struck typed S remains local to its observed occurrence; surrounding ordinary S letters were not changed. The offset H on 42 remains mathbb H. The typed, underlined O in 49–50 retains that graphic treatment. Every i/j difference is recorded in the page audits; the corrected handwritten i on 47 and the ambiguous cancelled K subscript on 49 remain distinct readings. Greek phi/rho/eta/theta/epsilon forms, stars, primes, and containment/arrow directions were compared with the respective crops. No additional mathematical reading was changed.

Clerical corrections to the audit prose: in the scan-42 accent list, the accent in homogènes/homogène is grave, as the spelling already recorded there and the TeX both show; the sentence calling it acute was an error in that prose. In the scan-47 list, grâce has a circumflex, au has no accent, and à/où/après/fidèlement have grave accents. The transcription spellings require no changes for either correction.

The rule joining words hyphenated at line ends also applies at the scan-49/50 boundary. The source's noethé- / rien is therefore joined without supplying letters: a TeX comment at the end of noethé and comments after the intervening scan/page macros suppress intervening whitespace. The scan-49 and scan-50 letters remain in their own files.

Scan 49, before -> after:

```tex
noethé-
% archive sheet number: 48
->
noethé%
% archive sheet number: 48
```

Scan 50, before -> after:

```tex
\scanpage{50}
\mspage{\handwritten{18}}
rien,
->
\scanpage{50}%
\mspage{\handwritten{18}}%
rien,
```

No formula content changed in this final join; the formula lists above remain current. Inventory rows added during the audit were moved beside their page elements, two overlapping handwritten rows were consolidated, and element identifiers were renumbered in page order. All 299 rows are marked yes. The notation and doubt tables were made contiguous Markdown tables, resolved provisional alternatives were identified, and the legibility note was completed for all nine pages. The preamble is byte-for-byte identical to the attachment. No OCR, web lookup, external transcription or compilation was used.
