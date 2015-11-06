Readme Lab 4
Sonny Shi
CSE 3461 Tu/Thur 12:45 - 2:05

To start the program run

python3 ftps.py <local-port-on-gamma> <troll port on gamma>

Then, start troll on beta.cse.ohio-state.edu with the command (on one line)

troll -S <IP-address-of-beta> -C <IP-address-of-gamma> -a 5001 -b <server-port-on-gamma> -r -t -x 0 <troll-port-on-beta>

On gamma.cse.ohio-state.edu, start troll with the command (on one line) 

troll -C <IP-address-of-gamma> -S <IP-address-of-beta> -a <server-port-on-gamma> -b 5001 <troll-port-on-gamma> -t -x <packet-drop-%>

Next, start ftpc.py on beta.cse.ohio-state.edu with the command (on one line)

python ftpc.py <IP-address-of-gamma> <remote-port-on-gamma> <troll–port-on-beta> <local-file-to-transfer>
