Prerequisites: You have a Linux server with Python 3 and Flask installed.  

To prepare a Debian distribution of Linux for this (e.g., Ubuntu, Linux Mint, Kali Linux), run these three commands:

sudo apt -y update
sudo apt -y install python3 python3-pip 
sudo pip3 install flask

The firewalls (either software or hardware) have no restriction to access port 5050 from the server where you will run curl commands.  
You only need one server as long as you can have two terminals open.

Usage instructions:

1.  Run the program like this: python3 pyrest.py

2.  From another Linux terminal draft a curl command like this:

curl -X POST http://127.0.0.1:5050/api/v1/resources/fibonacci -d "InputValue='6'"

You should replace 127.0.0.1 if you are not on the server running the pyrest.py program with the IP address of the server that is 
running pyrest.py.  (You could replace 5050 with the port you assigned in the program.)  The "6" should be replaced with the 
number of Fibonacci numbers you want to display.

3.  Run the command you just drafted.
