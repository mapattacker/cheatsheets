## Git Push from VSCode without Password Prompt
1) Go to Github > Settings > Developer Settings > Personal access tokens > create token. Check Repo. Copy the token
2) Click `git add *` > `git commit -m '.'` > `git push`. Either a popup or within the console, will ask for the username & password.
3) Username for 'https://github.com': mapattacker
4) Password for 'https://mapattacker@github.com': paste personal access token

## Add SSH Access to Github/Gitlab

1) In your terminal > `ssh-keygen`
2) Accept all defaults
3) Copy the public key `cat ~/.ssh/id_rsa.pub`
4) Go to Github/Gitlab Settings > SSH Keys, and paste the keys here
5) We should be able to git push/pull/clone now without logging in

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

``bash
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mapattacker/datavis.git
git push -u origin master
``

## Add Repository to a Root Folder
1) __Existing repository__: clone project, eg `git clone https://github.com/mapattacker/cheatsheets.git`

## Commit and Upload to GitHub
1) `git add`: add changes in the repository to the staging area
   * `git add -A`: add all changes including deleted files
   * `git add *`: add all changes, excluding deleted files
2) `git commit -m "add a message here"`: commit files with a message tag to repository
3) `git push`: push committed files to GitHub
4) A git alias can be used to combine all 3 commands into one. This needs to be set at each repository in your local machine
    * `git config alias.pushall '! git commit -a -m "commit" && git push'`: push-all refers to the alias name, it can be thus called using `git pushall`
    * `git config --global --unset alias.YourAlias`: to remove the set alias

## Branches
 * Reference: https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html
 1. **Checkout Branch**
   * `git branch`: check which branch is active, asterisk sign beside
   * `git fetch`: fetch all remote branches
   * `git checkout branch`: switch to another branch
   * `git fetch; git checkout branch`: switch to a branch from remote
 2. **Create Single Branch**
   * `git clone --single-branch --branch <repo-url>`: clone existing branch. e.g. `git clone --single-branch --branch main-branch git@gitlab.com:projectname/repo/scene-understanding.git`
 2. **Create from Existing Branch (1)**
   * `git checkout -b newBranch develop`
   * `git push origin newBranch`
 3. **Create from Existing Branch (2)**
   * `git push origin develop:newBranch`
 4. **Delete Branch**
   * Locally
      * `git branch -d branch-to-delete`: will check if the branch is merged
      * `git branch -D branch-to-delete`: will NOT check if the branch is merged (forced delete)
   * Remotely
      * `git push origin -d branch-to-delete`: delete branch in remote
 5. **Merge Branch**
   * to merge branchB into branchA
      * `git checkout branchA`
      * `git merge branchB`
   * merge conflicts
      * sometimes it might be necessary to merge branches locally
      * after forcing the merge locally, go to the IDE & accept/reject the conflicts

## Go back to previous commit
   * `git checkout hashkey`

## Some Git Commands
   * `git status`: shows which branch you are at, and changes not set for commit
   * `git pull`: pull all contents from github repository into local repository
   * `git add 'foldername/scriptname.py'`: stage specific files for committing
   * `git add -A`: stage all changes
   * `git add *`: stages new files and modifications, without deletions
   * `git add -u`: stages modifications and deletions, without new files
   * `git rm -r dir_name`: add removed directory & contents within
   * `git reset`: unstage all files set for committing
   * `git status`: shows files changed
   * `git remote -v`: shows the source of repository in remote server
   * `git remote rm origin`: remove origin location from remote. Remote location needed for push / pull / fetch commands
   * `git remote add heroku https://git.heroku.com/xxx.git`: add new remote location
   * `git diff`: show changes made in files

## Git Commands Combine
   * `alias lazygit="git add *; git add .gitlab-ci.yml; git commit -m 'test'; git push;";`: call `lazygit` in bash

## Git Tags
   * `git tag -a v1.0.0 -m "1st prod version"`: tag in local
   * `git push origin v1.0.0`: push to github. can check from the commits section
   * `git tag -d v1.0`: delete local tag ONLY
   * `git push -d origin v1.0.0`: delete remote tag ONLY
   * `git tag`: list tags

## Git Stash
   * `git stash`: store changes in stash before checkout in another branch
   * `git stash list`: list all the stash
   * `git stash apply`: after going back to branch, put back latest stash

## Git Reset
   * `git reset --hard HEAD~1`: delete the top commit, unable to retrieve back changes after this
   * `git reset --hard 2b237987`: delete till commit hash ID

## Git Logs
   * `git log`: lists commits & their msgs/author/date from most recent first. type q to exit
   * `git log --oneline`: lists only commit messages & sha hash code
   * `git show hash`: list changes
   * `git log --stat`: lists commits and summary of changes
   * `git log -p -2`: lists commits in detail with their difference (change), -2 for two entries

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

## Git LFS (Large File Storage)
   * `brew install git-lfs` or `sudo apt install git-lfs`: install git LFS
   * `git lfs install`: update git hooks
   * `git lfs track ".onnx" ".pb" ".pth" ".h5" ".tflite" ".mp4"`: add large file extensions
   * if repo is already created, use the link below to migrate large files to LFS
      * https://docs.gitlab.com/ee/topics/git/lfs/migrate_to_git_lfs.html
   * see this [video](https://www.youtube.com/watch?v=xPFLAAhuGy0&list=PLqUYzs7QMIAzR82pcut3saEI06fFeEgak&index=48&t=0s) for greater clarity
   * [Others](https://blog.axosoft.com/learning-git-git-lfs/)
   * Download from LFS
      * `git lfs fetch --all`: download all files from LFS

## Remove Files from Git History
   1. `git clone --mirror git@gitlab.com:project/repo-name.git`: clone only the .git
   2. `alias bfg="java -jar /home/jake/Desktop/vama/bfg-1.13.0.jar"`: in ubuntu, download bfg from [official site](https://rtyley.github.io/bfg-repo-cleaner/#download) and set an alias to its path within bash_profile; in Mac, use homebrew to install
   2. `bfg --delete-files "*.{png,jpg,jpeg,bmp,mp4}" repo-name.git`: delete certain file extensions
   3. `cd repo-name.git`: go into git directory
   4. `git reflog expire --expire=now --all && git gc --prune=now --aggressive`: delete old files
   5. `git push --force`: push updated git to remote

## Show Clone URL
   * `git config --get remote.origin.url`: just url, without internet
   * `git remote show origin`: full output with internet

## .gitignore file
   * for folders `folder/`
   * for single file `file.txt`
   * for all files of an extension `*.txt`
   * for all folders in all directories `**\__pycache__`
   * https://medium.com/@haydar_ai/learning-how-to-git-ignoring-files-and-folders-using-gitignore-177556afdbe3

## Submodules
   * __Add new submodule__
      * `git submodule add -b master [URL to Git repo]`: Adds `.gitmodules`
      * `git submodule init`: add `.gitmodules` submodule repo link to `.git/config`
      * `git submodule update --remote`: git pull/checkout a detached head (not existing branch)
   * __Update commits__
      * cd into submodule folder < `git pull`
      * update to submodule repo > `git add xx` > `git commit -m "xx"`> `git push`
      * all normal git commands work within submodule folder including git checkout, branching, logs
   * __Pull branch with existing submodule__
      * `git checkout branchname`
      * `git submodule init`: add `.gitmodules`link to `.git/config`
      * `git pull update --remote`: checks out current commit
   * __Delete Submodule from Repo__
      * `git submodule deinit -f — mymodule`
      * `rm -rf .git/modules/mymodule`
      * `git rm -f mymodule`
   * in the Gitlab/Github, clicking on the submodule folder will be directed to the source repo
   * https://www.vogella.com/tutorials/GitSubmodules/article.html

## Resources
1) http://rogerdudler.github.io/git-guide/
2) https://help.github.com/articles/basic-writing-and-formatting-syntax/
3) https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
