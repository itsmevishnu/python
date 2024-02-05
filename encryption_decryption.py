import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# key = os.urandom(32) # create a 32 bit random bytes
key = "9b104180c209bdd677b53abf1e676542"
print(f"length of key: {len(key)}")
code_bytes = key.encode("utf-8")
hash_key = base64.urlsafe_b64encode(code_bytes.ljust(32))[:32]
iv = "059ff284be86b066".encode()
cipher = Cipher(algorithms.AES(key.encode()), mode=modes.CTR(nonce=iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b"1212") + encryptor.finalize()
decoded_strig = ct.decode("latin-1")
    
print(decoded_strig)
# iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key.encode()[:32]), mode=modes.CTR(nonce=iv))

decryptor = cipher.decryptor()
# ct = decoded_strig.encode("latin-1")
dt = decryptor.update(ct) + decryptor.finalize()
print(dt.decode("latin-1"))
