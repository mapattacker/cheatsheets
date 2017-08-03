# Windows Command Line

`dir`                     --list files directories in current directory

`mkdir rst, test`         --make two directories at current folder, called rst & test

`cls`                     --clear screen

### System Info

`where python`            --show file path of a program 

`tree`                    --show tree structure of directories & files

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

`ls -a`   --list all directories & files (including hidden ones)

`ls -1`   --change to vertical view (number 1)

`ls -l`   --list date of modification & read/write, etc. (letter L)

`cd` 			--go back one directory before

`cd ..`   --go up one level

`cd ~`		--go back to login base directory

`cd \`    --go back to system root directory

`cd ~desktop`		--go to desktop directory

`pwd`			--show full directory path (print working directory)

`open .`			--open current directory in Finder

`ls`			--list files and directories

`brew list`		--list of packages installed using homebrew

`clear`   --clear screen

`> filename.txt` --create new file

`apt list --installed`  --check installed software in Ubuntu

TextEdit editor					

`open -a TextEdit .bash_profile`


`NANO text editor`

`nano .bash_profile`	--open bash profile

`ctrl + o`			--save / press enter after this command

`ctrl + x`			--exit

`ctrl+D`			--close python, pyspark session


### Locate Files

`locate filename` --locate all file names containing the word, includes full path


# PowerShell

`new-item newfile.txt` --create new file. Note to type in *file* when prompted "type" after pressing enter.

