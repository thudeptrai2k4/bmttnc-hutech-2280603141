from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_key = RSA.generate(2048)

def recv_all(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def recv_message(sock):
    raw_len = recv_all(sock, 4)
    if not raw_len:
        return None
    message_len = int.from_bytes(raw_len, 'big')
    return recv_all(sock, message_len)

def send_message(sock, message_bytes):
    length = len(message_bytes)
    sock.sendall(length.to_bytes(4, 'big') + message_bytes)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def receive_message():
    while True:
        encrypted_message = recv_message(client_socket)
        if encrypted_message is None:
            print("Connection closed by server.")
            break
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print("Received:", decrypted_message)

def main():
    client_socket.connect(('localhost', 12345))

    # Nhận public key server
    server_public_key_bytes = recv_message(client_socket)
    server_public_key = RSA.import_key(server_public_key_bytes)

    # Gửi public key client
    send_message(client_socket, client_key.publickey().export_key(format='PEM'))

    # Nhận encrypted AES key
    encrypted_aes_key = recv_message(client_socket)
    cipher_rsa = PKCS1_OAEP.new(client_key)
    global aes_key
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    receive_thread = threading.Thread(target=receive_message, daemon=True)
    receive_thread.start()

    while True:
        message = input("Enter message ('exit' to quit): ")
        encrypted_message = encrypt_message(aes_key, message)
        send_message(client_socket, encrypted_message)
        if message == "exit":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
