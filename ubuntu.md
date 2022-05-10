## Windows Subsystem for Linux (WSL)

 
 1. In Windows > Search "Turn Windows features on and off"
      * Check "Windows Subsystem for Linux"
      * Check "Hyper-V" and its subdir
 2. WSL commands
      * open powershell as admin
      * `wsl.exe update`: update wsl to v2
 3. In Microsoft Store > search Ubuntu (must be >20.4 for WSL2) > Install
 4. Restart Windows
      * Open Ubuntu Terminal
      * Set your username / password
 5. WSL commands
      * `wsl.exe --list --verbose`: check ubuntu is in wsl2 
      * `wsl.exe --status`: double check ubuntu is in wsl2
      * `wsl --set-default-version 2`: if not, set default
 5. Change VSCode Terminal to Linux
      * Install VSCode > Go to Extensions Tab > Search "Remote - WSL" > Install
      * There should be a new tab added called Remote Explorer
      * Right click > "Connect to WSL"
 6. Set your home directory in terminal
      * `sudo nano /etc/passwd`
      * Scroll to bottom of page, should show your default home directory
         * `harry:x:1000:1000:"",,,:/home/harry:/bin/bash`
         * Change to `harry:x:1000:1000:"",,,:/mnt/c/Users/<your-acc-name>:/bin/bash`
      * Restart Terminal
 7. Allow Terminal to change file permissions in Windows directories 
      * need to chmod 400 github's ssh private key `chmod 400 .ssh/id_rsa`
      * `sudo nano /etc/wsl.conf`
      * Add the following & restart your computer
```
[automount]
enabled  = true
root     = /mnt/
options  = "metadata,umask=22,fmask=11"
```

 1. 

 1. Install Anaconda
      * See most popular comment using wget & bash [link](https://askubuntu.com/questions/505919/how-to-install-anaconda-on-ubuntu)
      * If have error `Conda command not found`, add anaconda to default paths `export PATH="/home/username/anaconda3/bin:$PATH"` [link](https://stackoverflow.com/questions/35246386/conda-command-not-found)
 2. Windows Terminal
      * Seems like the better terminal which supports multitabs, though no split screens
      * Go to Windows Store > Windows Terminal
      * Go to Terminal > Dropdown > Settings > Change default terminal to Ubuntu
 3. Install Docker
      * install Docker for Windows
      * Docker GUI > settings, check "Use WSL2 based engine"


Resources

 * https://docs.microsoft.com/en-us/windows/wsl/install-win10
 * https://superuser.com/questions/1323645/unable-to-change-file-permissions-on-ubuntu-bash-for-windows-10

## Dual Boot Installation from Windows 10

 1. Download Ubuntu ISO file from website
 2. Install Bootable Ubuntu into USB thumbdrive using Rufus
    * at least 4GB
    * https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-windows#1-overview
 3. Create Windows Partition
    * Control Panel > Administrative Tools > Create & Format Harddisk Partitions
    * Right click C:/ > Shrink > specify a storage limit
    * A space called "free space" will be created
 4. If installation fails
      * Disable Secure Boot
         * Windows search > Advanced Startup > Restart Now
            * Troubleshoot > Advanced Options > UEFI Firmware Settings > Restart
            * At BIOS > Look for Secure Boot Configurations
            * disable Secure Boot > save changes and exit
      * Nvidia driver error (``nouveau 0000:01:00.0: tmr: stalled at ffffffff``)
         * Need to turn off driver at the starting stage
         * press E with selection at Install Ubuntu
         * at line start with Linux, add ``nomodeset`` at the end
         * Note: After installation
            * go to CMD > ``sudo nano /etc/default/grub``
            * remove line ``GRUB_CMDLINE_LINUX="nomodeset"``
            * go to Software & Updates > Additional Drivers
            * Select Nvidia driver > Apply changes > restart
 4. With Ubuntu USB plugged in, restart computer
    * Windows search > Advanced Startup > Restart Now
      * Troubleshoot > Advanced Options > UEFI Firmware Settings > Restart
      * At BIOS > Boot Menu > UEFI etc...
    * Go to Boot Menu > boot from USB/Removeable Media
    * Ubuntu Installation screen comes up
      * Install Ubuntu > continue
      * Installation Type > Something else
      * Set partitions
 5. Set start-up order
    * Windows will still startup
    * to change this go to BIOS > Boot Menu > UEFI Ubuntu
 5. Revert thumbdrive to normal
    * right click bootable USB drive > Format > Start Format
 6. Boot Windows
    * Press F2 when restarting
    * Choose to Windows Boot Manager when ubuntu startup screen appears
 7. Merge partition back to C://
    * Before doing anything, change the boot order to windows first!
    * install NIUBI partition editor
    * right click C:// > Resize/Move Volume > drag right in GUI
    * click Apply icon
 8. Increase Ubuntu Disk Space
    * Go to Windows > Disk Management > Shrink Volume > resulting free space will be parked under "unallocated space"
    * Disk partition management in Ubuntu requires GParted, but can only be done when Ubuntu is not active. Therefore, install GParted in [USB](https://gparted.org/liveusb.php) > try "GNU/Linux Method D: Manual - Overwrite"
    * Go to BIOS > Boot USB (GParted)
    * To merge unallocated partition to Ubuntu partition, the two partitions will need to align side by side
    * Open GParted > Click on partition on the right of unallocated space > move resize > drag the partition to the left without changing its size > the unallocated space will be shifted right. [more](https://askubuntu.com/questions/641713/cannot-move-unallocated-space)
    * Do this till it is beside the Ubuntu parition > move resize Ubuntu partition > expand the partition to fill up the unallocated space
    * Click "tick" icon to activate the partitioning steps you indicated earlier
    * Close system > boot ubuntu


Resources:
   * https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/
   * https://itsfoss.com/fix-ubuntu-freezing/
   * https://answers.microsoft.com/en-us/windows/forum/all/how-to-convert-bootable-usb-back-to-normal-with/a1f991fb-7169-4f5c-931f-b07edd2dc31c
   * https://www.hdd-tool.com/tutorials/resize-volume.html

---

## Virtual Machine from Windows 10

 1. Download Ubuntu ISO file from website
 2. Download & Install Oracle's Virtual Box
 3. In VirtualBox
   * Click New > give a name > select Type (Linux) > Version (Ubuntu)
   * Memory Size > 1GB
   * Create a Virtual Harddisk > Choose HDD file type > VDI
   * Storage on physical HDD > dynamically allocated
   * File location & size > at least 20GB
 4. Add Ubuntu ISO to created VM
   * Click on Created VM > Settings > Storage
   * Under Controller: IDE > Click on "Empty" with CD icon
   * On right panel > Attributes > Optical Drive > Click on CD icon > add Ubuntu ISO 
 5. Before starting, turn off Hyper-V (Window's VM)
   * In Administrator CMD > Run > ``dism.exe /Online /Disable-Feature:Microsoft-Hyper-V``
   * Note Windows Docker runs on top of Hyper-V, so it have to be on when using
 6. Installing Ubuntu
   * Start the created VM
   * Screen up to Try or Install Ubuntu > select latter
   * Updates & Other Software > Click continue
   * Installation Type > select Erase.... > click Install Now
   * Parition tables confirmation > click Continue
   * Where are You > click Continue
   * Who are You > enter username & password
   * Wait for awhile for installation to complete > restart computer

### Switch from Virtual Box to Host at Full Screen
 1. CTRL + m
 2. Drag mouse to bottom centre, VirtualBox panel will popup

### Mouse not Enabled
 1. In VM > top Toolbar > Input > Mouse Integration

### View VM to Full Screen
 1. First try 
   * Top toolbar > Device > Insert Guest Addition CD Images
   * Top toolbar > View > Virtual Machine 1 > Select Resize to (Max Resolution)
   * Top toolbar > View > Full-Screen Mode
 2. Alternate
   * In VM Ubuntu > top right > settings icon
   * Devices > Display > Resolution > select correct resolution
 3. Alternate
   * Virtual Box > File > Preferences > Display
   * Maximum Guest Screen Size > Hint
   * Change width & height appropriately
 4. Alternate
   * Virtual Box > Top Left > View > Virtual Screen 1
   * Scale to percentage screen size


### Configure Resources (RAM, CPU, GPU, HDD)
 1. Poweroff Machine
 2. Click on VM > Settings
   * **RAM**: System > Motherboard > Base Memory
   * **CPU**: System > Processor > Processor(s)
   * **GPU**: Display > Video Memory
 3. **HDD Size**
   * Set Size in VirtualBox
      * Virtual Box Toolbar > File > Virtual Media Manager > Properties > Size > allocate more space
   * Resize in Ubuntu vm
      * Download GParted ISO (gparted-live-1.1.0-1-amd64.iso) https://gparted.org/download.php
      * VirtualBox > create new VM > Select linux & ubuntu x64 > no virtual hdd
      * select new VM > Settings > Storage
         * Controller: IDE > add gparted ISO
         * Controller: SATA > add original ubuntu.vdi state
      * Run new VM > continue for all > display GPart GUI
      * Right click on drive > Resize/Move > Drag to increase size
      * Click "Tick" symbol to save
      * Poweroff VM > Start original Ubuntu VM 


### File Transfers
   1. **Clipboard**
      * In VM > Top Toolbar > Devices > Clipboard > Bidirectional
   2. **USB Drive**
      * In VM > Top Toolbar > Devices > USB Settings > +USB icon > add USB drive

Resources:
   * https://itsfoss.com/install-linux-in-virtualbox/
   * https://www.youtube.com/watch?v=ozJmfSPcfxY (increase vm ubuntu size)
   * https://www.isunshare.com/blog/3-ways-to-transfer-files-between-windows-and-virtualbox/



---

## GPU Driver not Set

 * Settings > Details > About > Graphics > should be indicating an Nvidia GPU name
 * Software & Updates > Additional Drivers > it should be pointing at an Nvidia driver
 * If the drivers are grey out, use the command `sudo ubuntu-drivers autoinstall` to install back the drivers > after that reboot your computer
 * more [info](https://askubuntu.com/questions/1237590/not-able-to-change-the-nvidia-driver-in-ubuntu-20-04)

## Auto Rotation
 
 * Ubuntu sometimes will auto rotate the screen upside down
 * it is best to go settings at top right corner > bottom 2nd icon > click it to lock the screen rotation
 * if it is already rotated > turn your laptop upside down > try to nagivate and lock the screen rotation

## Set File Explorer

 * At top left, click the explorer icon > Preferences
 * At Views > Check > Sort folders before files
 * At List Columns > Check > Type

## Screen Brightness

 * Ubuntu hard install sometimes does not by default enable keystroke or GUI screen brightness
   * option 1: install third party software
      * this software just mask with a dark filter, does not save battery
      * ``sudo add-apt-repository ppa:apandada1/brightness-controller``
      * ``sudo apt update``
      * ``sudo apt install brightness-controller-simple``
   * option 2: 
      * ``sudo nano "/etc/default/grub"``
      * change the line to ``GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor"``
      * ``sudo update-grub``
      * https://askubuntu.com/questions/468277/screen-brightness-isnt-taking-effect-on-a-lenovo-z570


## Bluetooth HeadPhone no Sound
 
 * From software centre, install PulseAudio Volume Control. [link](https://askubuntu.com/questions/239209/no-sound-from-bluetooth-headset-but-its-detected)

## Shortcut Show Desktop

 * Go to Settings > Devices > Keyboard
 * Under Nagivation > Hide all normal windows > change to Ctrl+D or ur preferred keystrokes

## Show full file path

 * drag and drop file into terminal

## Starting Ubuntu, Apps

* ``sudo apt-get install build-essential``: install all the basic functions in terminal, e.g. make
* ``sudo apt install git``: install git
* Anaconda: https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart
* System Monitor: like Windows Task Manager
* Tilix: emulator for multi-window terminal
* Shutter: screenshots
* Pulse Audio Volume Control: overcome some bug to use bluetooth headphones
* Bright Control Simple: for additional screen dim-ness
* Postman: for testing your APIs
* Filezilla: file transfers


### Terminal

 * ``nautilus .``: open current directory in GUI view
 * ``whereis anaconda``: search for installed package path
 * ``pip show packagename``: show path to package
 * ``find path/to/directory -name filename``: find file location
 * ``find / -name "site-packages" -type d``: find folder location
 * ``nano ~/.bashrc``: open bashrc. put stuff that applies only to bash itself
 * ``nano ~/.bash_profile``: open bash_profile. put stuff that applies to your whole session, e.g., programs or env variables
 * ``cp -R ~/Desktop/comply/app /var/www/`` copy paste directories
 * `watch -n 1 free -m`: check RAM every 1 sec
 * `df`: check disk space

### Change terminal abs path to relative path

 * change in (~/.bashrc)[https://unix.stackexchange.com/questions/381113/how-do-i-shorten-the-current-directory-path-shown-on-terminal]
