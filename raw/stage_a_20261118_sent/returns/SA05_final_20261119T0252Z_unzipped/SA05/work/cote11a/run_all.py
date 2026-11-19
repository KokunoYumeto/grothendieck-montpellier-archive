"""Rebuild and audit the authored deliverables. Run from workspace root."""
import pathlib,subprocess,sys,datetime
R=pathlib.Path('SA05/work/cote11a');logs=[]
scripts=['build_records.py','build_claims.py','build_problems.py','build_readings_links.py','build_references.py','build_search_events.py','polish_outputs.py','check_calculations.py','validate_scope.py']
for script in scripts:
 p=subprocess.run([sys.executable,str(R/script)],capture_output=True,text=True)
 logs.append('PROGRAM '+script+'\n'+p.stdout+p.stderr+'\nEXIT '+str(p.returncode))
 if script=='check_calculations.py':(R/'calculation_output.txt').write_text(p.stdout+p.stderr)
 (R/'build_output.txt').write_text('\n\n'.join(logs)+'\n')
 if p.returncode:print(p.stdout+p.stderr);sys.exit(p.returncode)
print(logs[-1]);print('All build and mathematical-check output saved in '+str(R/'build_output.txt'))
