# Jellyguard
An quick and dirty Python Windows program for the Jellyfin Media Player and Wireguard, that will automatically activate the Wireguard tunnel for Jellyfin in the background, then executes Jellyfin, and when the user is done with Jellyfin and closes the Jellyfin Media Player then Jellyguard will again automatically deactivate the Wireguard tunnel in the background.

This way devices/users can tunnel into your network to access the Jellyfin server using Wireguard, without having to go through the hassle of activating and deactivating Wireguard tunnels first.
Effectively achieving the same result as direct access via https would give, without the need of exposing your server to the public internet.


### Prerequisites:
Wireguard installation on system drive.
Jellyfin Media Player installation.
Imported tunnel in Wireguard which connects to the correct lan where the Jellyfin server is located.

To use this program, Jellyfin Media Player and Wireguard must be installed first as a prerequisite, after which the tunnel should be imported into Wireguard prior to running this program.
Wireguard should be installed on the machine's systemdrive (usually C:), and in case of Wireguard having multiple tunnels, the tunnel should be aptly named "jellyfin" or "Jellyfin", so that it will be recognizable.
If there are multiple tunnels installed and Jellyguard cannot fine a tunnel named "jellyfin" or "Jellyguard", then it will simply grab and activate the very first tunnel it sees, which may or may not be the incorrect one.


### Usage:
If these conditions are met, then on the first run Jellyguard will try to located JellyfinMediaPlayer.exe in either the system drive (usually C:) or the D: drive, if this fails it will place a config file named jg.conf in the Windows user directory, under the Jellyguard folder.
It will then launch the config file in notepad for you to edit, where you should change the example path and point the config file to the correct Jellyfin Media Player install location, save the file, and exit.
From that point on, if the location turns out to be correct, the Jellyguard app should be configured and it should work as intended.


### Note:
I'm aware the code could probably still use a lot of cleaning up, and there are quite a few ambiguous lines, it's quick, it's dirty, but it works.
Jellyguard does require admin rights to launch, so it will pop up uac, unfortunately this is not something I can work around since Wireguard commandline needs administrative privileges.
