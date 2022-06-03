# Get IP Address and Host Name of a Website
#import module to get IP Address 
import socket

#Choose any website
website = "www.youtube.com"
print("Website You Entered is: " + website)

#Get IP Address of the website
IP_Address = socket.gethostbyname(website)
print("The IP Address of the given website is: " + IP_Address)

#Get Host Name of the website
Host_Name = socket.gethostname()
print("The Host Name is: " + Host_Name)