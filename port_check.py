import socket

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} is OPEN on {ip}")
    else:
        print(f"Port {port} is CLOSED on {ip}")
    sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1" # بيفحص جهازي
    ports_to_check = [22, 80, 443, 8080]
    
    for p in ports_to_check:
        check_port(target_ip, p)