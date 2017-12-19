# Windows Command Line

`dir`                     --list files directories in current directory

`mkdir rst, test`         --make two directories at current folder, called rst & test

`cls`                     --clear screen

### System Info

`where python`            --show file path of a program 

`tree`                    --show tree structure of current directory and within

`netsh wlan show profile` --show all wifi profiles that you have saved

`netsh wlan show profile SSID key=clear`  --show wifi profile details, including password (change SSID to wifi name)

`systeminfo`              --show every details about your computer

`shutdown -f -t 636`      --time shutdown. -f refers to force shutdown; -t refers to time in seconds

### Output as Text

`systeminfo >c:\systeminfo.txt`           --output cmd output to text file. Needs admin access

### Run as Executable

Create a .cmd file, save commands in the file and double click it.



# Bash

__for loops__

`for i in $( ls ); 
do echo $i;
done`

__Show / Hide hidden folders/files__

`defaults write com.apple.finder AppleShowAllFiles YES`

killall Finder

`defaults write com.apple.finder AppleShowAllFiles NO`

killall Finder



### Some Commands

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

`Ctrl + B "`  --split horizontally

`Ctrl + B %`  --split vertically

`Ctrl + B arrow-key`  --switch to another window

`Ctrl + B [`  --scroll up and down within a window with arrow keys

`Ctrl + D`  --close window

`tmux a-t session_name`   --go back to same session



### Cron Job

http://www.nncron.ru/help/EN/working/cron-format.htm



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

`ctrl+D`			--close python, pyspark session

`alt + /`   --scroll to end of file

`F6 or Ctrl+W`  --search

`Shift + Insert`  	--paste from clipboard

`Alt + U`   --undo



### UBUNTU installation

`sudo apt-get update`  --update latest package versions

`sudo apt-get install package_name`  --install package

`sudo apt-get remove package_name`  --uninstall package, keep config files

`sudo apt-get purge package_name`  --uninstall package, remove config files

`sudo apt-get purge --auto-remove package_name` --uninstall package, remove config files and it's dependencies

`apt list --installed`  --list installed packages

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

`source ~\bashrc` --reload file



### HDFS

`hdfs dfs`  -- show all commands

`hdfs dfs -ls`  --list directory contents in hdfs

`hdfs dfs -put foldername foldername` --copy folder and all contents from edge and paste in hdfs datanode



### Shell Scripting

`#!/bin/bash` --shebang, use bash to execute



# PowerShell

`new-item newfile.txt` --create new file. Note to type in *file* when prompted "type" after pressing enter.

