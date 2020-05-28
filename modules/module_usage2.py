# subprocess

import subprocess

with open('python_h.txt', 'w') as out:
	subprocess.call(['python3', '-h'], stdout = out)
