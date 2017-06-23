## WINDOWS COMMAND LINE

dir             --list files directories in current directory
mkdir rst, test --make two directories at current folder, called rst & test



## TERMINAL / BASH COMMANDS

__for loops__

for i in $( ls ); 

do echo $i

done

Show / Hide hidden folders/files
defaults write com.apple.finder AppleShowAllFiles YES
killall Finder

defaults write com.apple.finder AppleShowAllFiles NO
killall Finder


`cd` 			--go back one directory before

`cd ..`   --go up one level

`cd ~`			--go back to base directory

`cd ~desktop`		--go to desktop directory

`pwd`			--show full directory path (print working directory)

`open .`			--open current directory in Finder

`ls`			--list files and directories

`brew list`		--list of packages installed using homebrew


TextEdit editor					

`open -a TextEdit .bash_profile`


`NANO text editor`

`nano .bash_profile`	--open bash profile

`ctrl + o`			--save

`ctrl + x`			--exit

`ctrl+D`			--close python, pyspark session



## Comparision between different shells
| PowerShell (Cmdlet) | PowerShell (Alias)            | CMD.EXE / COMMAND.COM | Unix shell               | Description                                                                                                   |
|---------------------|-------------------------------|-----------------------|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Get-ChildItem       | gci, dir, ls                  | dir                   | ls                       | List all files / directories in the (current) directory                                                       |
| Test-Connection[a]  | N/A                           | ping                  | ping                     | Sends ICMP echo requests to specified machine from the current machine, or instructs another machine to do so |
| Get-Content         | gc, type, cat                 | type                  | cat                      | Get the content of a file                                                                                     |
| Get-Command         | gcm                           | help                  | type, which, compgen     | List available commands                                                                                       |
| Get-Help            | help, man                     | help                  | apropos, man             | Help on commands                                                                                              |
| Clear-Host          | cls, clear                    | cls                   | clear                    | Clear the screen[b]                                                                                           |
| Copy-Item           | cpi, copy, cp                 | copy                  | cp                       | Copy one or several files / a whole directory tree                                                            |
| Move-Item           | mi, move, mv                  | move                  | mv                       | Move a file / a directory to a new location                                                                   |
| Remove-Item         | ri, del, erase, rmdir, rd, rm | del, erase, rmdir, rd | rm, rmdir                | Delete a file / a directory                                                                                   |
| Rename-Item         | rni, ren, mv                  | ren, rename           | mv                       | Rename a file / a directory                                                                                   |
| Get-Location        | gl, cd, pwd                   | cd                    | pwd                      | Display the current directory/present working directory.                                                      |
| Pop-Location        | popd                          | popd                  | popd                     | Change the current directory to the directory most recently pushed onto the stack                             |
| Push-Location       | pushd                         | pushd                 | pushd                    | Push the current directory onto the stack                                                                     |
| Set-Location        | sl, cd, chdir                 | cd, chdir             | cd                       | Change the current directory                                                                                  |
| Tee-Object          | tee                           | N/A                   | tee                      | Pipe input to a file or variable, then pass the input along the pipeline                                      |
| Write-Output        | echo, write                   | echo                  | echo                     | Print strings, variables etc. to standard output                                                              |
| Get-Process         | gps, ps                       | tlist,[c] tasklist[d] | ps                       | List all currently running processes                                                                          |
| Stop-Process        | spps, kill                    | kill,[c] taskkill[d]  | kill[e]                  | Stop a running process                                                                                        |
| Select-String       | sls                           | find, findstr         | grep                     | Print lines matching a pattern                                                                                |
| Set-Variable        | sv, set                       | set                   | env, export, set, setenv | Set the value of a variable / create a variable                                                               |
| Invoke-WebRequest   | iwr, curl, wget               | N/A                   | wget, curl               | Gets content from a web page on the Internet                                                                  |

