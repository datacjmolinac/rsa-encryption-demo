from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generar claves
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Guardar claves en archivos
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# Mensaje original
mensaje = "Este es un mensaje secreto."
print("Mensaje original:", mensaje)

# Cifrado
pub_key = RSA.import_key(open("public.pem").read())
cipher = PKCS1_OAEP.new(pub_key)
encrypted = cipher.encrypt(mensaje.encode())
encrypted_b64 = base64.b64encode(encrypted).decode()
print("Mensaje cifrado (base64):", encrypted_b64)

# Descifrado
priv_key = RSA.import_key(open("private.pem").read())
cipher = PKCS1_OAEP.new(priv_key)
decrypted = cipher.decrypt(base64.b64decode(encrypted_b64)).decode()
print("Mensaje descifrado:", decrypted)
