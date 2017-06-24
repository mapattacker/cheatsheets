## Steps for Versioning using Git & GitHub / GitLab

1) Create new Git Directory, eg. `mkdir github`
2) Go into directory: `cd github`
3) Create github key > `ssh-keygen` > enter to accept defaults 
4) Open file & copy keys `cat ~/.ssh/id_rsa.pub` OR `open ~/.ssh/id_rsa.pub` OR `open -a textedit ~/.ssh/id_rsa.pub`
5) Go to Github/GitLab > Settings > SSH and GPG Keys > paste the key here

## New Repository
1) create new project folder `> testfolder`, then `git init`
2) Go to Github > create new repository > get repository link
3) `git add README.md`
4) `git commit -m "first commit"`
5) `git remote add origin https://github.com/mapattacker/testrepo.git`
6) Go to Github > Personal access tokens > create token. This will be used in place of the password in command line
7) `git push -u origin master` > enter username & token as password

## Existing Repository
1) __Existing repository__: clone project, eg `git clone https://github.com/mapattacker/cheatsheets.git`

## Commit and Upload to GitHub
1) `git add .`: add all changes from working area to staging area
2) `git commit -m "add a message here"`: commit files with a message tag to repository
3) `git push`: push committed files to GitHub

## Some Git Commands
   * `git pull`: pull all contents from github repository into local repository
   * `git config --global user.name "Jake Teo"`: set username. Will show in commit message
   * `git config --global user.email "xxx@gmail.com"`: set email. Will show in commit message
   * `git log`: show commits for the day
   * `git status`: shows files changed
   * `git remote -v`: shows the source of repository in remote server
   * `git remote rm origin`: remove origin location from remote. Remote location needed for push / pull / fetch commands
   * `git remote add heroku https://git.heroku.com/xxx.git`: add new remote location

## Resources
1) http://rogerdudler.github.io/git-guide/