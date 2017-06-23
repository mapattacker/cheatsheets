## Steps for Versioning using Git & GitHub / GitLab

1) Create new Git Directory, eg. "mkdir github"
2) Go into directory: "cd github"
3) Create github key > "ssh-keygen" > enter to accept defaults 
4) Open file & copy keys "cat ~/.ssh/id_rsa.pub" OR "open ~/.ssh/id_rsa.pub" OR "open -a textedit ~/.ssh/id_rsa.pub"
5) Go to Github/GitLab > Settings > SSH and GPG Keys > paste the key here

## __New Repository__
1) create new project folder "> testfolder", then "git init"
2) Go to Github > create new repository > get repository link
3) git add README.md
4) git commit -m "first commit"
5) git remote add origin https://github.com/mapattacker/testrepo.git
6) Go to Github > Personal access tokens > create token. This will be used in place of the password in command line
7) git push -u origin master > enter username & token as password

## __Existing Repository__
1) __Existing repository__: clone project, eg "git clone https://github.com/mapattacker/cheatsheets.git

## __Commit and Upload to GitHub__
1) __git add .__: add all changes in working area to staging area
2) __git commit -m "add a message here"__: commit files with a message tag to repository
3) __git push__: push committed files to GitHub

## __Some Git Commands__
   * __git pull__: pull all contents from github repository into local repository
   * __git config --global user.name "Jake Teo"__: set username. Will show in commit message
   * __git config --global user.email "xxx@gmail.com"__: set email. Will show in commit message
   * __git log__: show commits for the day
   * __git status__: shows files changed
   * __git remote -v__: shows the source of repository in remote server
   * __git remote rm origin__: remove origin location from remote. Remote location needed for push / pull / fetch commands
   * __git remote add heroku https://git.heroku.com/xxx.git__: add new remote location

## __Resources__
1) http://rogerdudler.github.io/git-guide/

test
