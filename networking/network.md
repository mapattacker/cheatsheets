# Terms

 * WPA: Wi-Fi Protected Access
 * SSID: Service Set Identifier, or basically the wifi network name
 * BSSID: Basic Service Set Identifier, or basically the MAC address of network


# Show Saved Wifi Passwords

`netsh wlan show profile` --show all wifi profiles that you have saved

`netsh wlan show profile <wifi name> key=clear`  --show wifi profile details in Windows, including password (change SSID to wifi name)

`security find-generic-password -wa <wifi name>` --show wifi password in MacOS


# Scan for Wifi Networks

**Linux**

`sudo iwlist scan` --shows SSID

`nmcli dev wifi` --shows SSID, transfer rate, the signal strength and the security

**Mac**

`sudo airport -s` -- SSID, BSSID, RSSI, CHANNEL, SECURITY