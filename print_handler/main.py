import ctypes
import platform
import socket
import subprocess
import tkinter as tk
import threading

# subclass of threading.Thread that allows the return value of a thread's "target" to be accessed
class ReturnableThread(threading.Thread):
    pass

class Networking:
    def __init__(self, ip_addr=[], subnet_mask=[], test_domain='www.google.com', test_port=443):
        self.ip_addr = ip_addr
        self.subnet_mask = subnet_mask
        self.test_domain = test_domain
        self.test_port = test_port
        self.operating_system = platform.system()
        
    def get_ipv4(self) -> list:
        # create a socket for retrieving local IPv4 addr
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            try:
                # connect to test domain to generate a packet that we can grab the local IPv4 from
                s.connect((self.test_domain, self.test_port))
                # retreive the local IPv4
                ipv4_addr = str(s.getsockname()[0])
            except Exception as e:
                print('Error: ', e)
                ipv4_addr = ''
            finally:
                s.close()
            
        octets = [int(octet) for octet in ipv4_addr.split('.')]
        return octets
    
    def get_subnet_mask(self) -> list:
        try:
            # run ipconfig/ifconfig and capture output
            if (self.operating_system == 'Windows'):
                ip_info = subprocess.run('ipconfig', capture_output=True, text=True, check=True).stdout
                # split the output by newlines
                lines = ip_info.split('\n')
                # grab the line containing the subnet mask
                for line in lines:
                    if ('Subnet Mask' in line):
                        line = line.replace(' ', '')
                        result = line[22:] # subnet mask starts on char 22
                        break
                    else:
                        continue
            elif (self.operating_system == 'Linux'):
                print('Linux') # placeholder
        except Exception as e:
            print('Error: ', e)
            return [None]
        else:
            octets = [int(octet) for octet in result.split('.')]
            return octets
    
    # Determine all possible hosts on the network
    def calculate_hosts(self) -> list:
        ips = []
        # calculate the network address
        network_addr = [self.ip_addr[i] & self.subnet_mask[i] for i in range(4)]

        # calculate host bits (CIDR notation)
        CIDR = sum(bin(octet).count('1') for octet in self.subnet_mask)
        host_bits = 32 - CIDR
        # calculate total amount of hosts
        num_hosts = pow(2, host_bits) - 2
        print(f'CIDR notation: {network_addr[0]}.{network_addr[1]}.{network_addr[2]}.{network_addr[3]}/{CIDR}\nTotal possible hosts: {num_hosts}')
        # calculate all possible ips
        for i in range(1, num_hosts + 1):
            host = [network_addr[j] + (i >> ((32-host_bits)-host_bits*j)) % 256 for j in range(4)]
            ips.append(f"{host[0]}.{host[1]}.{host[2]}.{host[3]}")
        return ips
    
    def ping_host(self, host) -> str:
        if (self.operating_system == 'Windows'):
            ping_result = subprocess.run(f"ping {host} /n 1", shell=True, capture_output=True, text=True).stdout
        elif (self.operating_system == 'Linux'):
            print('Linux') # placeholder
        return ping_result
    
class Main:
    def __init__(self) -> None:
        self.root = tk.Tk()
        # scale window size to monitor resolution
        user32 = ctypes.windll.user32
        self.screen_size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        scale_factor = (1920/800, 1080/600) # Set the scale factor (based on 1920x1080)
        # resize the window
        self.root.wm_geometry(f"{int(self.screen_size[0]/scale_factor[0])}x{int(self.screen_size[1]/scale_factor[1])}")
    
    def scan_network(self) -> list:
        self.port = 8080
        return []
    
    def create_ui(self) -> None:
        
        return None
    
if __name__ == "__main__":
    Main().root.mainloop()