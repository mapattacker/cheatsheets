# Windows Command Line

`dir`                     --list files directories in current directory

`mkdir rst, test`         --make two directories at current folder, called rst & test

`cls`                     --clear screen

### System Info

`where python`            --show file path of a program 

`tree`                    --show tree structure of current directory and within

`systeminfo`              --show every details about your computer

`shutdown -f -t 636`      --time shutdown. -f refers to force shutdown; -t refers to time in seconds

### Output as Text

`systeminfo >c:\systeminfo.txt`           --output cmd output to text file. Needs admin access

### Run as Executable

Create a .cmd file, save commands in the file and double click it.



# Bash

__Zip File With Password__

`zip -er archive.zip ./` cd to directory and use the code. enter pw.


__for loops__

`for i in $( ls ); 
do echo $i;
done`

__Show / Hide hidden folders/files__

`defaults write com.apple.finder AppleShowAllFiles YES`

killall Finder

`defaults write com.apple.finder AppleShowAllFiles NO`

killall Finder

__Get Password__

 `security find-generic-password -ga "WiFi_Name"` --show wifi password

### Some Commands

`ifconfig | less`   --show ip address, less make it output line by line. Press "q" to quit.

`sudo su` --change to root user

`echo $PATH` --prints out path variables

`ls -a`   --list all directories & files (including hidden ones)

`ls -1`   --change to vertical view (number 1)

`ls -l`   --list date of modification & read/write, etc. (letter L)

`cd` 			--go back one directory before

`cd ..`   --go up one level

`cd ~`		--go back to login base directory

`cd \`    --go back to system root directory

`cd ~desktop`		--go to desktop directory

`cd /java1.8*`  --* is a wild card

`open .`			--open current directory in Finder

`ls`			--list files and directories

`brew list`		--list of packages installed using homebrew

`clear`   --clear screen

`mkdir -p folder1/folder2/folder3` --make nested directories

`sudo rm -r directoryname` --delete directory and descending files, but WITH a prompt

`sudo rm -rf directoryname` --delete directory and descending files, but WITHOUT a prompt. rf = recursive, force.

`rmdir projectfolder`  --delete folder if empty

`apt list --installed`  --check installed software in Ubuntu

`unzip kafka-manager-1.1.zip` --unzip file

`sudo mv target/kafka-manager-1.1.zip ~/`   --cut and paste file from current directory to ~/

`sudo cp target/kafka-manager-1.1.zip ~/`   --copy and paste file from current directory to ~/

`sudo rm target/kafka-manager-1.1.zip`   --delete file

`history | grep "iodbctest"`  --search history of a particular command

`tail -f filename`  --live updates from a particular file, eg. error logs



### Permissions

`chmod 777 dirOrfile`   -- 777: no restriction for all `(rwxrwxrwx)

`chmod -R 777 dirOrfile`   -- grant 777 permissions to all files/folders in directory



### TMUX (Terminal Multiplexer)

`tmux`  --quick start for a tmux session

`tmux new -s session_name`  --start a commandline session direct in the os, will not be subjected to timeout if any.  

`Ctrl + B (release then select) "`  --split horizontally

`Ctrl + B (release then select) %`  --split vertically

`Ctrl + B (release then select) arrow-key`  --switch to another window

`Ctrl + B (release then select) CTRL + arrow-key` --adjust window size

`Ctrl + B (release then select) [`  --scroll up and down within a window with arrow keys

`Ctrl + D`  --close window / alternatively, type exit

`tmux a-t session_name`   --go back to same session


### iTerm2

[Download](https://iterm2.com/index.html)

`Command+D`	--Split current window vertically

`Command+Shift+D`	--Split current window horizontally

`Ctrl+Alt+Left/Right/Up/Down`	--Move between window (panes)

`Ctrl+D`	Close window (pane). Could also type exit

`Command+Alt+2/3/4`	Switch to iTerm window number 2 (or 3, 4, etc)

`Command+T`	New window in new tab

`Command+Left/Right`	Move between tabs

### Terminator

`Ctrl+alt+t`  --open Terminator

`Ctrl + shift + o` --split horizontal

`Ctrl + shift + e` --split vertical


### Cron Job in Mac

http://www.nncron.ru/help/EN/working/cron-format.htm

Key thing is to store the cronjob statement into a file called crontab at the root. Add `MAILTO=""` to the top so that email will not be sent to the terminal.

```
* * * * *  command to execute
│ │ │ │ │
│ │ │ │ └─── day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
│ │ │ └──────── month (1 - 12)
│ │ └───────────── day of month (1 - 31)
│ └────────────────── hour (0 - 23)
└─────────────────────── min (0 - 59)
```
  `0 10-16 * * 1-5 /path/to/script/script.sh` --every hour from 10am to 4pm, Mon to Fri

  `*/5 * * * * /path/to/script/script.sh` --every 5 minutes

  `crontab -l`  --list of cronjobs

  `env EDITOR=nano crontab -e`  --edit cronjobs in nano


  `*/10 * * * * /Users/xx/anaconda3/bin/python /path/to/script/script.py` --run python script

  Live editor: https://crontab.guru
  

### SSH

`ipconfig getifaddr en0` -- get wifi ip address

`sudo systemsetup -getremotelogin` -- checks if ssh remote login is on/off

`sudo systemsetup -setremotelogin on` -- enable ssh

`ssh login_name@192.168.1.xxx` -- from another computer, enter ssh followed by username@ip_address


__TextEdit editor__			

`open -a TextEdit .bash_profile`



### Manipulating Files

`cat test.txt`  --prints out entire file contents

`less test.txt`  --prints out a small portion of file contents. arrow up-down to scroll. Q to quit.

`head test.txt` --prints first 5 lines of the file

`touch test.txt`  --create new file

`> filename.txt` --create new file

`mv test.txt test1.txt` --rename file from test to test1

`echo "hello there" >> test.txt` --append text to file. create file if not exist.

`echo "hello there" > test.txt` --replace text to file's contents. create file if not exist.



### NANO text editor

`nano .bash_profile`	--open bash profile; in Mac

`nano ~/.profile`	--open bash profile; in Ubuntu

`ctrl + o`			--save / press enter after this command

`ctrl + x`			--exit

`ctrl + D`			--close python, pyspark session

`alt + /`   --scroll to end of file (Win)

`CTRL + e` --go to end of line (Mac)

`F6 or Ctrl+W`  --search

`Shift + Insert`  	--paste from clipboard

`Alt + U`   --undo

`CTRL + Spacebar` --move cursor to next word

 

### UBUNTU installation

`sudo apt-get update`  --update latest package versions

`sudo apt-get install package_name`  --install package

`sudo apt-get remove package_name`  --uninstall package, keep config files

`sudo apt-get purge package_name`  --uninstall package, remove config files

`sudo apt-get purge --auto-remove package_name` --uninstall package, remove config files and it's dependencies

`apt list --installed`  --list installed packages

`apt list --installed tableau"*"` --list install package, using a wild card

`apt list --installed | less`  --list installed packages, line by line. press `q` to exit

`sudo dpkg -i installer_name` --install .deb installers (-i = install)

`dpkg -l` --list installed packages

`dpkg -l | grep installer_name` --list specific package


### Locate

`pwd`			--show full directory path (print working directory)

`locate filename` --locate all file names containing the word, includes full path

`which bash` --shows path where command/exe is installed in

`sudo find / -name "*iodbc*"` --find packages



### .bashrc

`nano ~\.bashrc` --create & open bashrc file

`alias npp='notepad++'` --assign an alias in the file

`source ~\.bashrc` --reload file



### HDFS

`hdfs dfs`  -- show all commands

`hdfs dfs -ls`  --list directory contents in hdfs

`hdfs dfs -put foldername foldername` --copy folder and all contents from edge and paste in hdfs datanode



# PowerShell

`new-item newfile.txt` --create new file. Note to type in *file* when prompted "type" after pressing enter.


# Resources
  * https://medium.com/@kadek/command-line-tricks-for-data-scientists-c98e0abe5da