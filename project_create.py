import os
import subprocess

# Initialized from main script
def Init(project_name, repo_name):
  os.mkdir(project_name)
  os.chdir(project_name)
  # Create README.md with title of project_name
  subprocess.check_call("echo '# {}' >> README.md".format(project_name), shell=True)
