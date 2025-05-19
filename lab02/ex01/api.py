from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
app = Flask(__name__)
#encrypt cho caesar
caesar_cipher = CaesarCipher()
@app.route("/api/caesar/encrypt", method=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text,key)
    return jsonify({'encrypted_message': encrypted_text})
#decrypt cho caesar
@app.route("/api/caesar/decrypt", method=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text,key)
    return jsonify({'decrypted_message': decrypted_text})
#encrypt cho vigenere
vigenere_cipher = VigenereCipher()
@app.route('/api/vigenere/encrypt',methods = ['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text= vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})
#decrypt cho vigenere
@app.route('/api/vigenere/decrypt',methods = ['POST'])
def vigenere_decrypt():
    data = request.json
    plain_text = data['cipher_text']
    key = data['key']
    decrypted_text= vigenere_cipher.vigenere_decrypt(plain_text,key)
    return jsonify({'encrypted_text': decrypted_text})

#encrypt cho railfence
railfence_cipher = RailfenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})
#decrypt cho railfence
#main
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug= True)