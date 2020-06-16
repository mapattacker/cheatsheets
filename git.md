## Git Push from VSCode without Password Prompt
1) Go to Github > Settings > Developer Settings > Personal access tokens > create token. Check Repo. Copy the token
2) Click `git add *` > `git commit -m '.'` > `git push`. Either a popup or within the console, will ask for the username & password.
3) Username for 'https://github.com': mapattacker
4) Password for 'https://mapattacker@github.com': paste personal access token

## Steps for Versioning using Git & GitHub / GitLab

1) Create new Git Directory, eg. `mkdir github`
2) Go into directory: `cd github`
3) Create github key > `ssh-keygen` > enter to accept defaults
4) Open file & copy keys `cat ~/.ssh/id_rsa.pub` OR `open ~/.ssh/id_rsa.pub` OR `open -a textedit ~/.ssh/id_rsa.pub`
5) Go to Github/GitLab > Settings > SSH and GPG Keys > paste the key here

## Link Folder to Repository
1) create new project folder `mkdir testfolder`, then `git init`
2) Go to Github > create new repository (DO NOT create a README.md or other files) > get repository link
3) `git add README.md`
4) `git commit -m "first commit"`
5) `git remote add origin https://github.com/mapattacker/testrepo.git`
6) `git push -u origin master` > enter username & token as password

```bash
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mapattacker/datavis.git
git push -u origin master
```

## Add Repository to a Root Folder
1) __Existing repository__: clone project, eg `git clone https://github.com/mapattacker/cheatsheets.git`

## Commit and Upload to GitHub
1) `git add`: add changes in the repository to the staging area
   * `git add -A`: add all changes including deleted files
   * `git add *`: add all changes, excluding deleted files
2) `git commit -m "add a message here"`: commit files with a message tag to repository
3) `git push`: push committed files to GitHub
4) A git alias can be used to combine all 3 commands into one. This needs to be set at each repository in your local machine
    * ``git config alias.pushall '! git commit -a -m "commit" && git push'``: push-all refers to the alias name, it can be thus called using ``git pushall``
    * ``git config --global --unset alias.YourAlias``: to remove the set alias

## Branches
 * Reference: https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html
 * `git branch`: check which branch is active, asterisk sign beside
 * `git clone -b feature/repository https://bitbucket.ship.gov.sg/scm/vam.git`: clone existing branch

## Some Git Commands
   * `git status`: shows which branch you are at, and changes not set for commit
   * `git pull`: pull all contents from github repository into local repository
   * `git add 'foldername/scriptname.py'`: stage specific files for committing
   * `git reset`: unstage all files set for committing
   * `git config --global user.name "Jake Teo"`: set username. Will show in commit message
   * `git config --global user.email "xxx@gmail.com"`: set email. Will show in commit message
   * `git log`: show commits for the day
   * `git status`: shows files changed
   * `git remote -v`: shows the source of repository in remote server
   * `git remote rm origin`: remove origin location from remote. Remote location needed for push / pull / fetch commands
   * `git remote add heroku https://git.heroku.com/xxx.git`: add new remote location

## Git Release
   * `git tag -a v1.0.0 -m "1st prod version"`: tag in local
   * `git push origin v1.0.0`: push to github. can check from the commits section
   * `git tag` list tags

## Username
   * For single repo:
      * `git config user.name`: display current local username
      * `git config user.name "Your Name"`: change username in current repo
   * For all repos:
      * `git config --global user.name`: display global username
      * `git config --global user.name "Your Name"`: change global username 

## Git Conflicts
   * sometimes there can be conflicts when trying to push your commits to master, because there are already a conflict when someone else have committed new changes. a prompt saying `Please enter a commit message to explain why this merge is necessary, especially if it merges an updated upstream into a topic branch` will be given. To resolve this:
     * press `i` > write your merge message > press `esc` > write `:wq` > then press enter

## .gitignore file
   * for folders `folder/`
   * for single file `file.txt`
   * for all files of an extension `*.txt`
   * for all folders in all directories `**\__pycache__`
   * https://medium.com/@haydar_ai/learning-how-to-git-ignoring-files-and-folders-using-gitignore-177556afdbe3

## Resources
1) http://rogerdudler.github.io/git-guide/
2) https://help.github.com/articles/basic-writing-and-formatting-syntax/
