import socket

# Set up a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5354))

# Define a dictionary of hostname-IP address mappings
hosts = {'Ojasvi4807.com': '192.168.1.1', 'www.Ojasvi4807.com': '192.168.1.1', 'mail.Ojasvi4807.com': '192.168.1.2',
         'ftp.Ojasvi4807.com': '192.168.1.3'}

print('DNS server listening on port 5354..')

while True:
    # Receive a message from a client
    data, address = sock.recvfrom(1024)

    # Extract the query from the message
    query = data[12:].decode('utf-8').strip('\x00')

    # Check if the query is a valid hostname
    if query in hosts:
        # Construct a response message with the IP address of the hostname
        response = bytearray(data[:2]) + bytearray(b'\x81\x80') + bytearray(data[4:6]) + bytearray(
            b'\x00\x01\x00\x01\x00\x00\x00\x00') + data[12:] + bytearray(
            b'\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04') + socket.inet_aton(hosts[query])
    else:
        # Construct a response message with a CNAME record pointing to a valid hostname
        response = bytearray(data[:2]) + bytearray(b'\x81\x80') + bytearray(data[4:6]) + bytearray(
            b'\x00\x01\x00\x01\x00\x00\x00\x00') + data[12:] + bytearray(
            b'\x00\x05\x00\x01\xc0\x0c\x00\x05\x00\x01\x00\x00\x00\x3c\x00\x0c\x03\x77\x77\x77\xc0\x0c')

    # Send the response message to the client
    sock.sendto(response, address)
