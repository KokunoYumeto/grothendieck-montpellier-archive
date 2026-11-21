import urllib.request,json,pathlib,hashlib,concurrent.futures,datetime
root=pathlib.Path(__file__).resolve().parent
sha=json.loads((root/'provenance.json').read_text())['commit']
extra=['LastSeeSawThetaIdentity','SeeSawLastPeriodFactorizationOfClassData','SeeSawKernelLiftCombinationOfDefiniteClassData','BesselPeriodThetaLiftUnfolding','BesselPeriodThetaLiftEqIntegralKernel','ThetaInnerProductFormulaDefiniteOfRallisConverge','RallisInnerProductConvergentOfWeilSiegelFormula','LastTwoStepsDoubleLiftPeriodEqIntegral','BesselPeriodDoubleStepIteratedQuotientIntegral','BesselModelDoublingData','ConjugateRowPairingPoincareSeriesBesselPeriods','DoubleLiftPeriodRankZeroFubiniCompactQuotient','SeesawCombinationsCompositeNeZeroOfVacuum','SeeSawLastTwoStepsDoubleLiftPeriodValue','UnfoldedPeriodEqIntegralBesselPeriods','BesselDoubleStepUnfoldingOfUnfoldingsAndLink']
paths=[str(p.relative_to(root)) for p in root.rglob('*.lean')]
paths += ['Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/'+n+'.lean' for n in extra]
paths += ['Development/AbelianVarietyTheory/Definitions/LatticeFrames/'+n+'.lean' for n in ['BesselCompatibility','PerIntOnAmb','AdmissiblePeriodOfPeriodInt','TopFormula','ValLastX']]
paths=list(dict.fromkeys(paths))
base=f'https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/{sha}/src/'
def fetch(p):
 url=base+p;dest=root/p
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'THETA3-source-audit'})
  data=urllib.request.urlopen(req,timeout=45).read()
  previous=dest.read_bytes() if dest.exists() else None
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  return {'path':p,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'previous_equal':previous==data if previous is not None else None,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as e:return {'path':p,'url':url,'error':str(e)}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for r in ex.map(fetch,paths):
  results.append(r)
  print(r['path'],r.get('bytes',r.get('error')),'unchanged='+str(r.get('previous_equal')),flush=True)
(root/'pinned_manifest.json').write_text(json.dumps({'commit':sha,'source_role':'secondary mirror; no Lean build','files':results},indent=2))
