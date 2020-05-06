## Dual Boot Installation from Windows 10

 1. Download Ubuntu ISO file from website
 2. Install Bootable Ubuntu into USB thumbdrive using Rufus
    * at least 4GB
    * Note its file format, so can format to same state later
    * follow official steps in https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-window
 3. Create Windows Partition
    * Control Panel > Administrative Tools > Create & Format Harddisk Partitions
    * Right click C:/ > Shrink > specify a storage limit
    * A space called "free space" will be created
 4. With Ubuntu USB plugged in, restart computer
    * Press F1 or other function keys to go BIOS
    * Go to Boot Menu > boot from USB/Removeable Media
 5. Revert thumbdrive to normal
    * right click bootable USB drive > Format > Format Table Type > Format
 6. Merge partition back to C://
    * install NIUBI partition editor
    * right click C:// > Resize/Move Volume > drag right in GUI
    * click Apply icon


Resources:
   * https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/
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
   * Top toolbar > View > Virtual Machine 1 > Select Resize to (Max Resolution)
   * Top toolbar > View > Full-Screen Mode
 2. Alternate
   * Top toolbar > Device > Insert Guest Addition CD Images

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

## Starting Ubuntu, Basics

* ``sudo apt-get install build-essential``: install all the basic functions in terminal, e.g. make
* ``sudo apt-install git``: install git
* System Monitor: like Windows Task Manager

### Installing 