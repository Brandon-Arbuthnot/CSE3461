Readme Lab 3
Sonny Shi
CSE 3461 Tu/Thur 12:45 - 2:05

To start the program run

python3 ftps.py <local-port-on-gamma>

Then, start troll on beta.cse.ohio-state.edu with the command (on one line)

troll -C 127.0.0.1 -S <IP-address-of-gamma> -a <client-port-on-beta> -b <server-port-on-gamma> -r -t -x 0 <troll-port-on-beta>

Next, start ftpc.py on beta.cse.ohio-state.edu with the command (on one line)

python ftpc.py <IP-address-of-gamma> <remote-port-on-gamma> <troll–port-on-beta>
<local-file-to-transfer>