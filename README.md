# Python Project Creation Automation

Creates a local git repo with README.md as intial commit and creates/adds a remote repo

---

1) Edit path of `linux/new-project` to point to `automate_python_project.py`

2) Edit `script.config`, `directory` is where projects will be created and `editor` is the editor in your PATH to open the newly created project (If no editor is in your path, your project will still be created but will not be opened in your editor)

3) Add linux folder to $PATH
`PATH=$PATH:~/path/to/linuxFolder`

   `echo $PATH` to see what's in your PATH

4) Run to create projects
`new-project`