def public_ip():
    import socket
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print('My IP Address is: ', ipAddress,'\n')