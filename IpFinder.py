import socket

# Function to get the IP address of a website
def get_ip_address(website_url):
    try:
        # Get the IP address using the gethostbyname function
        ip_address = socket.gethostbyname(website_url)
        return ip_address
    except socket.gaierror:
        return "Invalid URL or unable to resolve IP address."

# Input: Website URL from the user
if __name__ == "__main__":
    website_url = input("Enter website URL (e.g., example.com): ")
    
    # Get and display the IP address
    ip_address = get_ip_address(website_url)
    print(f"The IP address of {website_url} is: {ip_address}")
