import socket
from rsa import RSA
from pka import PKA
import library

def Main():
    host = "127.0.0.1"
    port = 5002

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    rsa = RSA()
    pka = PKA()
    pka.register("server", rsa.get_public_key())

    # Send server's public key to the client
    conn.send(f"{rsa.get_public_key()}".encode())

    # Receive the encrypted DES key
    encrypted_des_key = int(conn.recv(1024).decode())
    des_key = rsa.decrypt(encrypted_des_key)
    print(f"Received DES key: {des_key}")

    # Communication using the DES key
    while True:
        encrypted_message = conn.recv(1024).decode()
        if not encrypted_message:
            break

        decrypted_message = library.decrypt(encrypted_message)
        print(f"Client: {decrypted_message}")

        response = input("Enter your response: ")
        encrypted_response = library.encrypt(response)
        print("Encrypted message to be sent:", encrypted_response)
        conn.send(encrypted_response.encode())
        library.sending()
        
    conn.close()

if __name__ == "__main__":
    Main()
