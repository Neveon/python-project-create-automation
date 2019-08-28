import os
import subprocess
import configparser
import project_types

# config parser set up
config = configparser.ConfigParser()
config.read("script.config")

# global project variables
directory = config.get("DEFAULT", "directory")
editor = config.get("DEFAULT", "editor")
project_name = input('Project name: ')

def CreateProject():
  project_types.Init(project_name)

while os.path.isdir(directory + project_name):
  project_name = input("Project name already exists, please enter a new name: ")

try:
  # changes into correct directory and runs the project creation process
  os.chdir(directory)
  CreateProject()

  # git process
  subprocess.call("git init", shell=True)
  subprocess.call("git add .", shell=True)
  subprocess.call("git commit -m \"initial commit\"", shell=True)

  # open project in editor
  try:
    subprocess.call("{} .".format(editor), shell=True)
  except Exception as e:
    print("No editor called {} found\n{}".format(editor, str(e)))

  print("Project Created Successfully!")

except Exception as e:
  print("There was an error when creating the project: {}".format(str(e)))

