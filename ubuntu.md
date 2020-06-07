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
 6. Merge partition back to C://
    * install NIUBI partition editor
    * right click C:// > Resize/Move Volume > drag right in GUI
    * click Apply icon


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
   * Choose HDD file type > VDI
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


### Configure Resources
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

## Auto Rotation
 
 * Ubuntu sometimes will auto rotate the screen upside down
 * it is best to go settings at top right corner > bottom 2nd icon > click it to lock the screen rotation
 * if it is already rotated > turn your laptop upside down > try to nagivate and lock the screen rotation

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


## Shortcut Show Desktop

 * Go to Settings > Devices > Keyboard
 * Under Nagivation > Hide all normal windows > change to Ctrl+D or ur preferred keystrokes

## Show full file path

 * drag and drop file into terminal

## Starting Ubuntu, Basics

* ``sudo apt-get install build-essential``: install all the basic functions in terminal, e.g. make
* ``sudo apt install git``: install git
* Anaconda: https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart
* System Monitor: like Windows Task Manager


### Terminal

 * ``nautilus .``: open current directory in GUI view
 * ``whereis anaconda``: search for installed package path
 * ``find path/to/directory -name filename``: find file location
 * ``find / -name "site-packages" -type d``: find folder location
 * ``nano ~/.bashrc``: open bashrc. put stuff that applies only to bash itself
 * ``nano ~/.bash_profile``: open bash_profile. put stuff that applies to your whole session, e.g., programs or env variables
 * ``cp -R ~/Desktop/comply/app /var/www/`` copy paste directories
