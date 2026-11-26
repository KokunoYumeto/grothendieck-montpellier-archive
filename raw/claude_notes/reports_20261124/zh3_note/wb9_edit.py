import pathlib, sys
p = pathlib.Path(sys.argv[1])
t = p.read_text(encoding='utf8')
reps = [
 (r"\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/zeta-and-l-functions-workbench/tree/main/finite-arithmetic-simplicity-test}",
  r"\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/zeta-and-l-functions-workbench/tree/main/work/WB-0009/v1}" "\n"
  r"\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0009.md}"),
 (r"\bibitem{wb} Workbench: \url{\workbenchurl}.",
  r"\bibitem{wb} WB-0009, permanent record: \expandafter\url\expandafter{\recordurl}; programs and check records:" "\n"
  r"\expandafter\url\expandafter{\workbenchurl}."),
 (r"the programs and records are on the workbench \cite{wb}.",
  r"the permanent record of this work is WB-0009, \expandafter\url\expandafter{\recordurl}; its programs and check" "\n"
  r"records are at \expandafter\url\expandafter{\workbenchurl} \cite{wb}."),
 (r"""operator numerically; neither treats multiplicities. Numerical verifications""",
  r"""operator numerically; neither treats multiplicities. On Hexagon, C\'aceres \cite{caceres} states, in the abstract
of his Part~IV, an averaged criterion: the mean energy of the prime-counting error is at least $2B$
unconditionally, with equality if and only if the Riemann hypothesis holds with simple zeros; the test here is
exact at each fixed height, with a certificate, and we have read only that abstract. Numerical verifications"""),
 (r"\bibitem{cc-weil}",
  r"""\bibitem{caceres} P.~C\'aceres, The Riemann hypothesis as a margin: a two-sided criterion verified to $2\cdot10^{29}$,
the fourth-moment anatomy of M\"obius cancellation, and one constant seen from every side, hexagon:2610.00688v3
(2026), abstract, \url{https://hexagonmath.org/2610.00688}.
\bibitem{cc-weil}"""),
]
for a, b in reps:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, b)
p.write_text(t, encoding='utf8', newline='\n')
print('ok')
