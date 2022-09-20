import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.padding import MGF1, OAEP
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from M2Crypto import BIO, RSA
encrypted_message = "M+bpzevgVRlPGn2sFZ5Ry9pWZNKaG2TZEMTB/Xu1tqhsOllf6BSZ6VpOKE9N0Y3k7qnLKriB5TJK7Z3yknXUsiS8ICfsBahcR5hORVSt4XJPcq+XkTW4OF9zg2HIiwJfcBHy7HIpLo+BaY/k7xuUknEYUZtZYmqmx0acM10RyTQ="
encrypted_message_bytes = base64.b64decode(encrypted_message.encode("utf-8"))
PRIVATE_KEY = open('private.pem', 'r').read()
private_key_bytes = PRIVATE_KEY.encode("utf-8")
private_key: RSAPrivateKey = load_pem_private_key(private_key_bytes, None)
padding = OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
decrypted_message = private_key.decrypt(encrypted_message_bytes, padding)
print(decrypted_message)