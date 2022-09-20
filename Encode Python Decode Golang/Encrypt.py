import base64
from distutils import errors
from distutils.log import error
import rsa

publicKey =""
with open('public.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
s =b"Datazip has this code to decrypt"
encrypt= rsa.encrypt(s, publicKey)
e = base64.b64encode(encrypt)
print(e.decode())

