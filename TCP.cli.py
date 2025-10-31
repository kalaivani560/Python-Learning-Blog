import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Enter message: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print("Echo from server:", data.decode())

client_socket.close()
