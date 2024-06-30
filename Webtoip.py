
import socket
print("                  ")
print("    ")
print("WEBTOIP2.0 by LOU!X")
print("..                    ")
print("                      ")
print("...                    ")
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

# Prompt the user for a domain name
domain_name = input("Enter the domain name (e.g., example.com): ")

# Resolve the domain name to an IP address
ip_address = resolve_domain_to_ip(domain_name)

# Print the result
print(f"The IP address for {domain_name} is {ip_address}")

with open("ip.txt", "a") as file:
    file.write(f"{domain_name} - {ip_address}")

print(input(" THANKS FOR USING THIS TOOL...press enter to exit_"))
