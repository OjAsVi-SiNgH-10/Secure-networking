import socket

# Set up a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the hostname to query
hostname = 'www.Ojasvi4807.com'

# Construct a query message
message = bytearray(b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00') + bytearray(hostname.encode('utf-8')) + bytearray(b'\x00\x00\x01\x00\x01')

# Send the query message to the DNS server
sock.sendto(message, ('localhost', 5354))

# Receive the response message from the DNS server
data, addr = sock.recvfrom(1024)

# Extract the IP address from the response message
ip_address = socket.inet_ntoa(data[-4:])

# Print the IP address
print(f'{hostname} has IP address {ip_address}')

# Close the socket
sock.close()
