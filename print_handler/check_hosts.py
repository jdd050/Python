import socket
import subprocess

def get_ipv4() -> list:
    # create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # connect to google.com so the host machine IPv4 address can be retrieved
            s.connect(("www.google.com", 443)) # 443 = HTTPS
            # get the local IPv4 addr of host machine
            ipv4_addr = str(s.getsockname()[0])
        except Exception as e:
            print("Error: ", e)
            ipv4_addr = ''
        finally:
            s.close()
    
    octets = [int(octet) for octet in ipv4_addr.split('.')]
    return octets

def get_subnet_mask() -> list:
    try:
        # run ipconfig in cmd and capture output
        ip_info = subprocess.run(["ipconfig"], capture_output=True, text=True, check=True)
        output = ip_info.stdout
        # split by newlines
        lines = output.split("\n")
        # grab the line containing the subnet mask
        for line in lines:
            if "Subnet Mask" in line:
                line = line.replace(" ", "")
                result = line[22:] # subnet mask starts on char 22 (windows only)
                break
    except Exception as e:
        print(e)
        return [None]
    else:
        octets = [int(octet) for octet in result.split('.')]
        return octets    

def lookup_host(ip_addr, subnet_mask) -> list:
    ips = []
    # calculate the network address
    network_addr = [ip_addr[i] & subnet_mask[i] for i in range(4)]

    # calculate host bits (CIDR notation)
    CIDR = sum(bin(octet).count('1') for octet in subnet_mask)
    host_bits = 32 - CIDR
    # calculate total amount of hosts
    num_hosts = pow(2, host_bits) - 2
    print(f"CIDR notation: {network_addr[0]}.{network_addr[1]}.{network_addr[2]}.{network_addr[3]}/{CIDR}\nTotal possible hosts: {num_hosts}")
    # calculate all possible ips
    for i in range(1, num_hosts + 1):
        host = [network_addr[j] + (i >> ((32-host_bits)-host_bits*j)) % 256 for j in range(4)]
        ips.append(f"{host[0]}.{host[1]}.{host[2]}.{host[3]}")
    return ips

host_ipv4 = get_ipv4()
subnet_mask = get_subnet_mask()
ips = lookup_host(host_ipv4, subnet_mask)
print(f"{host_ipv4}\n{subnet_mask}\n{ips}")