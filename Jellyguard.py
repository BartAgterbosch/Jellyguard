from genericpath import exists
from time import sleep
import subprocess
import os
import glob

# To install a jellyfin tunnel, preferably install the tunnel with the name 'Jellyfin' or 'jellyfin'.
# If the tunnel is not aptly named, it will grab and activate the first tunnel it finds.
# Which may or may not be the correct tunnel if several tunnels are installed.
# 
# It will check for the systemdrive, which may or may not be C:
# And will then check to see if wireguard is installed under Program Files or Program Files (x86)
# If wireguard is not found, but installed in a different directory, reinstall it on the systemdrive first.
# If wireguard is not found, and is not installed yet, install wireguard on the systemdrive first.
#
# A config file will be placed in the userprofile's documents folder, when the app is first run, it will open the file for you to edit.
# Make sure to place the Jellyfin Media Player's full location in the file as such ex: C:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe
# Save and exit the file, run Jellyguard again.
# If all conditions are met, it will launch successfully


if (exists(os.getenv("SystemDrive") + "\Program Files\WireGuard\wireguard.exe")):
    wireguard = os.getenv("SystemDrive") + "\Program Files\WireGuard\\"
elif (exists(os.getenv("SystemDrive") + "\Program Files (x86)\WireGuard\wireguard.exe")):
    wireguard = os.getenv("SystemDrive") + "\Program Files (x86)\WireGuard\\"
else:
    exit(0)

if (glob.glob(wireguard + "Data\Configurations\*.conf.dpapi")):
    if (glob.glob(wireguard + "Data\Configurations\*ellyfin.conf.dpapi")):
        peer = str(glob.glob(wireguard + "Data\Configurations\*ellyfin.conf.dpapi")).split("\\")[-1].split(".")[0]
    else:
        peer = str(glob.glob(wireguard + "Data\Configurations\*.conf.dpapi")).split("\\")[-1].split(".")[0]
else:
    exit(0)

if (exists(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf")):
    with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "r") as config:
        jellyfin = config.readline().strip()
        config.close()

    if not (exists(jellyfin)):
        exit(0)
else:
    if not (exists(os.getenv("USERPROFILE") + "\Jellyguard")):
        os.makedirs(os.getenv("USERPROFILE") + "\Jellyguard")

    if (exists(os.getenv("SystemDrive") + "\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")):
        with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "w") as config:
            config.write(os.getenv("SystemDrive") + "\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")
            config.close()
        jellyfin = os.getenv("SystemDrive") + "\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe"
    elif (exists(os.getenv("SystemDrive") + "\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")):
        with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "w") as config:
            config.write(os.getenv("SystemDrive") + "\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")
            config.close() 
        jellyfin = os.getenv("SystemDrive") + "\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe"
    elif (exists("D:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")):
        with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "w") as config:
            config.write("D:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")
            config.close() 
        jellyfin = "D:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe"
    elif (exists("D:\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")):
        with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "w") as config:
            config.write("D:\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe")
            config.close()
        jellyfin = "D:\Program Files (x86)\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe"
    else:
        with open(os.getenv("USERPROFILE") + "\Jellyguard\jg.conf", "w") as config:
            config.write("C:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe\n# The above filepath is an example filepath, please edit the filepath to the correct path of JellyfinMediaPlayer.exe\n# Then save this file, close notepad, and run Jellyguard again")
            config.close()
        sleep(2)
        os.system("notepad.exe " + os.getenv("USERPROFILE") + "\Jellyguard\jg.conf")
        exit(0)
    
subprocess.run([wireguard + "wireguard.exe", "/installtunnelservice", wireguard + "Data\Configurations\\" + peer + ".conf.dpapi"])
sleep(5)
subprocess.run([jellyfin])
sleep(2)
subprocess.run([wireguard+"wireguard.exe", "/uninstalltunnelservice", peer])