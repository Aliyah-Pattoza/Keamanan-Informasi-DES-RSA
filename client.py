import socket
from rsa import RSA
from pka import PKA
import library

def Main():
    host = "127.0.0.1"
    port = 5002

    client_socket = socket.socket()
    client_socket.connect((host, port))

    rsa = RSA()
    pka = PKA()

    # Receive server's public key
    server_public_key = eval(client_socket.recv(1024).decode())
    print(f"Server's public key: {server_public_key}")

    # Encrypt and send the DES key
    des_key = "1001100111"
    encrypted_des_key = rsa.encrypt(des_key, server_public_key)
    client_socket.send(str(encrypted_des_key).encode())

    # Communication using the DES key
    while True:
        message = input("Enter your message: ")
        encrypted_message = library.encrypt(message)
        client_socket.send(encrypted_message.encode())
        print("Encrypted message = " + encrypted_message)
        library.sending()

        encrypted_response = client_socket.recv(1024).decode()
        decrypted_response = library.decrypt(encrypted_response)
        print(f"Server: {decrypted_response}")

if __name__ == "__main__":
    Main()