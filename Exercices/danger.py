import os, subprocess

def run_cmd(cmd):
    # Risque: shell=True
    return subprocess.check_output(cmd, shell=True)

# Risque: clé codée en dur
API_KEY = os.getenv('API_KEY', 'hardcoded-dev-key')
