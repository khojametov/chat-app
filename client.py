import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            print(msg.decode('utf-8'))
        except Exception as e:
            print(e)
            break

threading.Thread(target=receive_messages).start()

while True:
    try:
        msg = input()
        client_socket.sendall(msg.encode('utf-8'))
    except Exception as e:
        print(e)
        break
