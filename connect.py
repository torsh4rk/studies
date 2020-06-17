#Usage connect.py + IP

import socket,sys

def connect(ip):
    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((ip, ports)) == 0:
            print("Port {} open!". format(ports))
            print("Service: {}". format(s.recv(1024)))
            s.close()

def main():
    if len(sys.argv) < 2:
        print ("[+] Exemple for the use: connect.py 192.168.1.1")
    else:
        connect(sys.argv[1])

if __name__ == '__main__':
    main()