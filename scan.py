import socket
import ipaddress
import sys

def scan_ports(target, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target, port))
            open_ports.append(port)
            print(f"Port {port} is open.")
        except (socket.timeout, ConnectionRefusedError):
            pass
        finally:
            sock.close()

    return open_ports

def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return True
    except ValueError:
        print(f"ERROR: {ip} is not a valid IP address!")
        sys.exit()
        

if __name__ == "__main__":
    target_host = input("Enter the target host IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    if (validate_ip(target_host)) == True and isinstance(start_port, int) == True and isinstance(end_port, int):

        print(f"Scanning ports {start_port} to {end_port} on {target_host}...")

        open_ports = scan_ports(target_host, start_port, end_port)

        if open_ports:
            print("Open ports:", open_ports)
        else:
            print("No open ports found.")