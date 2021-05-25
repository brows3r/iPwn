# iPwn
A Framework meant for the exploitation of iOS devices.
![image](https://user-images.githubusercontent.com/78043996/119547132-ba00ee80-bd62-11eb-989a-1b9522ca6bd4.png)

# Status - ❌
This project is still being worked on. I'm adding more extensions and options for post-exploitation for harvesting Device information and other things.

# Description/How to use [FOR NOOBIES!!!]
iPwn is a framework meant for exploiting and and gaining access to iOS devices. It also has an extension that is a mini-framework called 'iSteal' that is meant for post-exploitation (after you get access to the device). This description will walk you through the different ways and steps to get access to an iOS device and harvest information from it.

The first way of getting access to an iOS device. - SSH-Bruteforcing
Most jailbroken iOS devices with Cydia come prepackaged with OpenSSH. And usually, the credentials are very weak or common, one of the most common passwords will be included in a wordlist that should be in your folder if you downloaded iPwn from my Github.

So lets begin! So first off, we'll start by running the script.
```
python main.py
```
Then, we are going to type in the 'brute' command. (If you want to type help and get familiar with the commands, you may do so.)
![image](https://user-images.githubusercontent.com/78043996/119564117-67313200-bd76-11eb-9acd-e80b952f138d.png)

Once we type in the 'brute' command. Type in 'help' to display all the available commands.
![image](https://user-images.githubusercontent.com/78043996/119564260-95167680-bd76-11eb-8adb-122e9455d47d.png)
Now, we are going to use the 'default' command to start SSH-Bruteforcing with a wordlist containing the most common passwords.
You will be asked to enter the targets IP address, please ensure you are entering the correct and vaild one, press enter, then move on with the next step.
![image](https://user-images.githubusercontent.com/78043996/119564509-deff5c80-bd76-11eb-9df7-a58df14cb08e.png)

<!> IF YOU ARE GETTING ERRORS, PLEASE MAKE SURE THAT HYDRA IS INSTALLED, YOU CAN INSTALL HYDRA WITH THE COMMANDS BELOW <!>
```
commands to install hydra:

sudo apt install hydra
sudo pacman -S hydra
```
# Tested OS's
```
Windows 10 - Stable
Garuda Linux - Stable
Arch based distros - Stable
```

# Supported and tested iOS devices
```
Supported Devices [The post-exploitation extension should work for all of these]
-----------------
iPods newer than the 4th Gen iPod
iPhone 4
iPhone 4S
iPhone 5
iPhone 6
iPhone SE
iPhone 7
iPhone 7+
iPhone 8
iPhone 8+
iPhone X
iPhone XR
iPhone XS
iPhone 11
iPhone 12

My own tested devices [Ones I myself have personally tested]
---------------------
iPhone 4S
iPhone 5S
iPhone SE
iPhone 7+
iPad Air
iPod 4th Gen
```

# Screenshots
![image](https://user-images.githubusercontent.com/78043996/119547477-2845b100-bd63-11eb-96bb-f01106e833b6.png)
![image](https://user-images.githubusercontent.com/78043996/119548701-7909d980-bd64-11eb-9adf-774cc787586e.png)
![image](https://user-images.githubusercontent.com/78043996/119549700-7f4c8580-bd65-11eb-8131-0f261883df45.png)
![image](https://user-images.githubusercontent.com/78043996/119549828-a3a86200-bd65-11eb-831e-5de71ea65323.png)

# Update logs
[5/25/21] - Added 2 extra modules for the 'iSteal' post-exploitation tool.

# Credits
[https://github.com/0x1CA3]
