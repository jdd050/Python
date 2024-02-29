import regex
import socket
import subprocess

def get_ipv4() -> list:
    # create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # connect to google.com so the host machine IPv4 address can be retrieved
            s.connect(('www.google.com', 443)) # 443 = HTTPS
            # get the local IPv4 addr of host machine
            ipv4_addr = str(s.getsockname()[0])
        except Exception as e:
            print("Error: ", e)
            ipv4_addr = ""
        finally:
            s.close()
    
    octets = regex.findall(r"[^.]+", ipv4_addr)
    # convert each bit to a number rather than string
    for i in range(len(octets)):
        octets[i] = int(octets[i])
        pass
    
    return octets

def get_subnet_mask() -> str:
    try:
        ip_info = subprocess.run(["ipconfig"], capture_output=True, text=True, check=True)
        output = ip_info.stdout
        lines = output.split("\n")
        for line in lines:
            if "Subnet Mask" in line:
                line = line.replace(" ", "")
                result = line[22:] # subnet mask starts on char 22 (windows only)
                break
    except Exception as e:
        print("Error: ", e)
        return ""
    return result    

def lookup_host(ip_addr, subnet_mask) -> list:
    ips = []
    # Split IP address and subnet mask into octets
    ip_octets = ip_addr
    subnet_octets = [int(octet) for octet in subnet_mask.split('.')]
    
    # Calculate network address by performing bitwise AND operation
    network_address = [ip_octets[i] & subnet_octets[i] for i in range(4)]

    # Calculate the number of host bits by counting the number of zeros in the subnet mask
    host_bits = 32 - sum(bin(octet).count('1') for octet in subnet_octets)

    # Calculate the number of possible host addresses
    num_hosts = 2 ** host_bits - 2  # Subtract 2 for network and broadcast addresses

    # Generate all possible host addresses within the subnet
    for i in range(1, num_hosts + 1):
        # Calculate the next host address by incrementing the last octet of the network address
        next_host = [(network_address[j] + (i >> (24 - 8 * j)) % 256) for j in range(4)]
        ips.append(next_host)
    
    return ips


host_ipv4 = get_ipv4()
subnet_mask = get_subnet_mask()
ips = lookup_host(host_ipv4, subnet_mask)
print(f"{host_ipv4}\n{subnet_mask}\n{ips}")