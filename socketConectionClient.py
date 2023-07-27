import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's IP address and port
server_ip = '192.168.0.1'
server_port = 49152

# Connect to the server
client_socket.connect((server_ip, server_port))

x = 10.0
y = 5.0
z = 3.0

p1 = f"227.98, -218.03, 60, 156.46, 82.0, 156.91" + '\r'
p2 = f"227.98, 218.03, 60, 156.46, 82.0, 156.91" + '\r'
p3 = f"360.10, 218.03, 60, 156.46, 82.0, 156.91" + '\r'
p4 = f"360.10, -218.03, 60, 156.46, 82.0, 156.91" + '\r'

# position_data = f"290.8406, -1.61299, 399.6503, -2.9783, 89.4395468, 20.0, 5" + '\r'

# Convert the position data to bytes
count =0
while True:
    if count==0:
        position_bytes = p1.encode()
        count=1
    elif count==1:
        position_bytes = p2.encode()
        count = 2
    elif count ==2:
        position_bytes = p3.encode()
        count = 3
    elif count ==3:
        position_bytes = p4.encode()
        count = 0
    # Send the position data
    client_socket.sendall(position_bytes)

    # Receive data from the server (optional)
    response = client_socket.recv(1024)
    print('Received from server:', response)

# Close the socket connection
client_socket.close()
