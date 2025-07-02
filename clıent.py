import socket
import threading

client_socket = socket.socket()
client_socket.connect(("134.102.157.151", 5000))


def receive():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print(f"{response}")
        except:
            print("Connection closed")
            client_socket.close()
            break


def send():
    while True:
        message = input()
        client_socket.send(message.encode())
        if message == "exit":
            client_socket.close()


# dinleme threadi

thread = threading.Thread(target=receive)
thread.start()

# yazma threadi
thread2 = threading.Thread(target=send)
thread2.start()