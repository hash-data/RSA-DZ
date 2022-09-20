import rsa
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.padding import MGF1, OAEP
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/public.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/private.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def PrivateKey():
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey

# generateKeys() # To generate the keys first

encrypted_message = "CAHVgoZdCvNB7+oRiyINUbZJZ3avA5c/5pU2dbR9Yy0xeu81r9ibuZ6GkvV5R4FGpVR8WO5ukC5gl17h0kOrPnkocXorQ3W2R0uNQZoP1J4vWUO/vO1LkykKm+HbBHCiC70kvyXHKZ2B2kgBCp4M7ykaHwuJwf3peWWktxGMaTQ="
encrypted_message_bytes = base64.b64decode(encrypted_message.encode("utf-8"))
PRIVATE_KEY = open('keys/private.pem', 'r').read()
private_key_bytes = PRIVATE_KEY.encode("utf-8")
private_key: RSAPrivateKey = load_pem_private_key(private_key_bytes, None)
padding = OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
decrypted_message = private_key.decrypt(encrypted_message_bytes, padding)
print("Decrypted Message : ",decrypted_message.decode('utf-8'))