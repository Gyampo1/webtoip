import os
import time
import socket
print("**********")
time.sleep(1.5)
print("***************")
time.sleep(2.5)
print("WEBTOIP2.0 by LOU!X")
print("********************")
time.sleep(3.5)
print("*************************")
print("...                    ")

#loading here

time.sleep(5)

#Disclaimer
print("[*]THIS IS A WEBSITE TO IP CONVERTER. THIS TOOL HEPLS YOU TO CONVERT YOUR TARGET WEBSITES TO THEIR IP ADDRESSES[*]")
print(input("Press ENTER to proceed_ "))

# Function to resolve domain name to IP address
def resolve_domain_to_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Invalid domain name or unable to resolve."

os.system('clear')

# Prompt the user for a domain name
domain_name = input("[*]Enter the domain name (e.g., example.com):_ ")

#clears the page
os.system('clear')

print(" PLEASE WAIT FOR YOUR RESULTS_")

# Resolve the domain name to an IP address
ip_address = resolve_domain_to_ip(domain_name)

 


time.sleep(1.5)


# Print the result
print(f"[*]The IP address for {domain_name} is {ip_address}")

with open("ip.txt", "a") as file:
    file.write(f"{domain_name} - {ip_address}")

time.sleep(2)
print("                     ")
print(input(" THANKS FOR USING THIS TOOL...press enter to exit_"))

