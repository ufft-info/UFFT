"""Run all independent checks; propagate any nonzero exit status."""
import subprocess,sys
from pathlib import Path
base=Path(__file__).resolve().parent
for name in ['verify_baseline.py','verify_deeper.py','verify_flux_sweep.py','check_author_certificate.py','check_supplement.py','check_flux_moments.py']:
 print('\nRUN '+name,flush=True)
 result=subprocess.run([sys.executable,str(base/name)],cwd=base)
 if result.returncode:
  print('FAILED: '+name,flush=True);sys.exit(result.returncode)
print('\nALL INDEPENDENT CHECKS PASSED')
