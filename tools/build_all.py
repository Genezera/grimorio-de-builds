"""Rebuild all six pages and crafting data, offline, from any working directory."""
from pathlib import Path
import subprocess
import sys
import os

HERE = Path(__file__).resolve().parent
for script in ['craft/build_data.py', 'build_site.py', 'oracle/opatch.py', 'oracle/obuild.py', 'build_landing.py']:
    subprocess.run([sys.executable, '-X', 'utf8', str(HERE / script)], cwd=HERE, check=True,
                   env={**os.environ, 'PYTHONUTF8': '1'})
