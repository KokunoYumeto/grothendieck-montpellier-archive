"""Integrate checked finite spherical tests. Does not create a checkpoint."""
from pathlib import Path
import csv,datetime
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'work';P=W/'package'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
newfiles={
 'hurwitz_spherical_order5.tex':"work/'agents/pentagon/hurwitz_spherical_order5.tex'",
 'hurwitz_spherical_socle.tex':"work/'agents/five_level_six/hurwitz_spherical_socle.tex'",
 'hurwitz_full_spherical_covariance.tex':"work/'agents/pentagon/hurwitz_full_spherical_covariance.tex'",
}
f=W/'code/sync_package.py';s=f.read_text();anchor=" 'hurwitz_conjugate_closure_normalization.tex':work/'agents/characters/proofs/hurwitz_conjugate_closure_normalization.tex',"
assert anchor in s
s=s.replace(anchor,anchor+'\n'+''.join(' '+repr(k)+':'+v+',\n' for k,v in newfiles.items()).rstrip())
f.write_text(s)
f=P/'DELTA23.tex';s=f.read_text();anchor='\\input{proofs/hurwitz_conjugate_closure_normalization.tex}'
assert anchor in s
s=s.replace(anchor,anchor+'\n'+''.join('\\input{proofs/'+k+'}\n'for k in newfiles).rstrip())
old='''The active next comparison is a five-puncture Hurwitz action
with four local classes $\\mathcal C$ and one inverse class,
including its order-five pure-frame coboundary. Its construction
and tests are retained as working calculations until separately
proved and checked. Other noncentral orbital comparisons remain
available. No geometric coordinate-deletion compatibility is
assumed, and all finite candidate arrays retain their check status.'''
new='''D23.P29 extends the action to a degree-$6720$ spherical orbit.
D23.F39 proves sixty independent simple factors and trivial
finite order-five cohomology; all eighteen pure primitives even
admit commutator lifts. D23.P30 gives full spherical covariance.
This particular extension therefore supplies no further exclusion.

The active next comparison links the actual free-kernel action
on target-group tuples to evaluations of the same associator word
in $E_0$. Its preliminary last-entry partition test passes.
Additional colored Hurwitz covers and the noncentral orbital
comparisons remain available. Those working calculations are not
promoted to a theorem before their proof and checks. No arbitrary
coordinate-deletion compatibility is assumed.'''
assert old in s
s=s.replace(old,new);f.write_text(s)
f=P/'QUESTIONS.tsv'
with f.open(newline='')as h:r=csv.DictReader(h,delimiter='\t');fields=r.fieldnames;rows=list(r)
newrows=[
 ['Q2-spherical-extension','LochakSchneps1997','pp571-573; newNielsenconstruction','Does the coupled1344 orbit extend with exact full five-puncture marking?','proved','D23.P29: literal6720orbit, fivecolors,60blocks, rotationXi→Xi+3, all18forcedfullf-values andexplicitlocalcochains.'],
 ['Q2-spherical-order5-frame','LochakSchneps1997','Theorem2IIIprime,p573','Does requiring an actual finite pure order5 primitive exclude the survivors?','refuted at specified finite scope','D23.F39: S^60⊂Pprime, solvable5prime quotient andcyclicfactorpermutation implyH1(C5,P)=1. All18explicitprimitives lieS^60 andadmitordinarycommutatorlifts.'],
 ['Q2-spherical-covariance','Prompt','item2 route','Does full spherical four-generator covariance exclude the survivors?','refuted at specified finite scope','D23.P30: all18haveunique6720pointintertwiners extendingoldV, withsigma1/sigma4fixedandcorrectfullf-twists. NoactualGTlift.'],
]
rows.extend(dict(zip(fields,row))for row in newrows)
with f.open('w',newline='')as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (W/'records/root_check_events.tsv').open('a',newline='')as h:
 w=csv.writer(h,delimiter='\t');who='GPT-6 Astra Pro; inherited effort not exposed; run DELTA23; /root'
 for ident,detail,loc in [
  ('D23.P29','PASS: wholeproofread and freshsphere/cochainreplays. Productoneclasspattern, allArtin/sphererelations, rotationmarking, sectorforcedvalues andlocalS-memberships checked. Rootandpentagon independentlycaughtpuregeneratorloopoffbyone; correctedbeforeglobalpurecalculation.','agents/pentagon/hurwitz_spherical_order5.tex; records/root_spherical_five_recheck.log; records/root_order5_cochains_recheck.log'),
  ('D23.F39','PASS: wholeproofread and freshcompletecertificate. Exactthreepairtypes andw40unequalorderwitnesses forceS^60 byGoursat; quotient5prime/solvabilitychecked; additiveaveraging andnonabelianfivecyclecochain recursion independentlyverified. All18globalprimitives liePprime.','agents/five_level_six/hurwitz_spherical_socle.tex; records/root_spherical_socle_recheck.log'),
  ('D23.P30','PASS: wholeproofread; y4=sigma4^-2 makeslastconjugatortrivial, rotationidentifiesfullR, andexhaustivegraphpropagation uniquelyextendsoldV. Fresh18pairfullcovariancereplayPASS.','agents/pentagon/hurwitz_full_spherical_covariance.tex; records/root_spherical_covariance_recheck.log'),
 ]:w.writerow([ident,now,who,'targeted proof check',detail,loc])
with (P/'LEDGER.md').open('a')as h:
 h.write('\n### Spherical order-five route completed at finite scope\n\n'+now+': P29,F39,P30 build thefull6720sphereaction, proveS^60 inits purederivedimage andH1(C5,P)=1, andcheck allfour canonicalgeneratorimages. Every18retainedpair passes, including bothfinalC33forms. This closes this finiteorder5test but isnot furthermain-gatemovement. Themain gate remainsactualrealization/exclusion of(1,0),(27,2). Activefollowup: samef inE0target tuples versusknownHurwitzV, pluschangedlocalclasscovers.\n')
with (P/'IMPLICATIONS.md').open('a')as h:
 h.write('\nP29,F39,P30 show why the orderfivepureframe condition in this particular fullsphericalcover still cannot comparethetwo signs: the purefiniteimage has sixtyindependentsimplefactors, its remaining quotient hasorderprimetofive, and its orderfivecohomologyset is trivial. This is a limitation of thisspecifiedfiniteimage; it doesnot trivialize orderfiveframes in the profinitegroup.\n')
print('Integrated P29,F39,P30 and precise negative finite scopes; no checkpoint created.')
