import os
import sys
import subprocess
from configparser import ConfigParser
import project_create
from github import Github
from getpass import getpass

# config parser set up
config = ConfigParser()
configFilePath = str(os.getcwd()) + '/enter/files/here/to/script.config'
config.read(configFilePath)

# global project variables
directory = config.get('DEFAULT', 'directory')
editor = config.get('DEFAULT', 'editor')
project_name = input('Project name: ')
repo_name = input('Repository name: ')

def CreateProject():
  project_create.Init(project_name, repo_name)

# Following is false if project_name does not exist yet
while os.path.isdir(directory + '/' + project_name):
  project_name = input("Project name already exists, please enter a new name: ")

try:
  # changes into correct directory and runs the project creation process
  os.chdir(directory)
  CreateProject()

  # git local intialization - CreateProject() places us in project directory
  subprocess.call("git init", shell=True)
  subprocess.call("git add .", shell=True)
  subprocess.call("git commit -m \"initial commit\"", shell=True)

  # git remote intialization
  user = input("Github Username: ")
  password = getpass() # getpass() used to prevent terminal echo
  g = Github(user, password)
  repo = None
  
  # Loop until repo is created successfully or told to stop
  while repo is None:
    try:
      repo = g.get_user().create_repo(repo_name)
    except Exception as e:
      print("Error in creating repo - ERROR MESSAGE BELOW:\n\n{}".format(str(e)))
      repo_name = input("\nEnter a new repo name or type 'STOP' to stop creation of remote repository: ")
    
    if repo == 'STOP':
      break

  # git remote add origin and push origin master
  # repo.full_name == 'username/githubRepoName'
  try:
    subprocess.call("git remote add origin https://github.com/{}.git".format(repo.full_name), shell=True)
    subprocess.call("git push -u origin master", shell=True)
  except Exception as e:
    print("Error:\n{}\n".format(str(e)))
    print("Error with one of the following commands:\n'git remote add origin https://github.com/{}.git'\n'git push -u origin master'".format(repo.full_name))
    print("NOTE: You can't push to remote until it is added properly")

  # open project in editor
  try:
    subprocess.call("{} .".format(editor), shell=True)
  except Exception as e:
    print("No editor called {} found\n{}".format(editor, str(e)))

  print("Project Creation Finished!")

except Exception as e:
  print("There was an error when creating the project:\n\n{}".format(str(e)))

