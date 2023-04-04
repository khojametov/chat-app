import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen()

clients = []


def broadcast_message(msg):
    for client_socket in clients:
        try:
            client_socket.sendall(msg)
        except Exception as e:
            print(e)
            clients.remove(client_socket)


def handle_client(client_socket, _):
    clients.append(client_socket)

    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            broadcast_message(msg)
        except Exception as e:
            print(e)
            break

    clients.remove(client_socket)
    client_socket.close()


def accept_clients():
    while True:
        try:
            client_socket, client_addr = server_socket.accept()
            print('Client connected:', client_addr)
            threading.Thread(target=handle_client, args=(client_socket, client_addr)).start()
        except Exception as e:
            print(e)


threading.Thread(target=accept_clients).start()
