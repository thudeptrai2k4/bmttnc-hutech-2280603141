from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

server_key = RSA.generate(2048)
clients = []
clients_lock = threading.Lock()

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

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")
    try:
        # Gửi public key server
        send_message(client_socket, server_key.public_key().export_key(format='PEM'))
        # Nhận public key client
        client_public_key_bytes = recv_message(client_socket)
        if client_public_key_bytes is None:
            print(f"Connection closed by {client_address} during key exchange")
            client_socket.close()
            return

        client_public_key = RSA.import_key(client_public_key_bytes)
        # Tạo AES key và mã hóa gửi cho client
        aes_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(client_public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        send_message(client_socket, encrypted_aes_key)

        # Lưu client và key vào danh sách (dùng khóa để tránh race condition)
        with clients_lock:
            clients.append((client_socket, aes_key))

        while True:
            encrypted_message = recv_message(client_socket)
            if encrypted_message is None:
                print(f"Connection closed by {client_address}")
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received from {client_address}: {decrypted_message}")

            if decrypted_message == "exit":
                break

            # Gửi message cho các client khác
            with clients_lock:
                for client, key in clients:
                    if client != client_socket:
                        encrypted = encrypt_message(key, decrypted_message)
                        send_message(client, encrypted)
    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        with clients_lock:
            clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Connection with {client_address} closed")

def main():
    print("Server started and listening on localhost:12345")
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
