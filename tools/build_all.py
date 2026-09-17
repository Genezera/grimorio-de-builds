"""Rebuild every page (Silverfist, Oracle, the kit builds, landing, rites) and crafting data from any working directory."""
from pathlib import Path
import subprocess
import sys
import os

HERE = Path(__file__).resolve().parent
KIT_BUILDS = ['tactician', 'infernalist', 'acolyte', 'pathfinder', 'smith']
steps = [[s] for s in ['craft/build_data.py', 'build_site.py', 'oracle/opatch.py', 'oracle/obuild.py']]
steps += [[f'kit/{s}', bid] for bid in KIT_BUILDS for s in ('kassets.py', 'kpatch.py', 'kbuild.py')]
steps += [['build_landing.py'], ['build_rites.py']]
for script, *args in steps:
    subprocess.run([sys.executable, '-X', 'utf8', str(HERE / script), *args], cwd=HERE, check=True,
                   env={**os.environ, 'PYTHONUTF8': '1'})
