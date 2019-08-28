import os
import subprocess

# Initialized from main script
def Init(project):
  os.mkdir(project)
  os.chdir(project)
  subprocess.check_call("echo '{}' >> README.md".format(project), shell=True)
