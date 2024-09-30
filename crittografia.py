# creazione environment, per evitare che ubuntu non vi faccia 
# installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
lucakey= "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0yThh9uoOWQD5Go+3B4p\n6LRR8MOG/0fkMJrCYMbwK3TgLvIa/D/QnEtnLSa6CqwQlbL8QzCcLzqdxcux5QCf\nluwJChG2w87InAo6V/5roFc7BWei2sF68qQr3SGriNrHi7+DyYvkyeZfln/ukVFl\nA+EE2PoGMcP/2BsnW+9Z3mrDFgC+C57YOCLiNd1L1Fax9nq9FUuM7AbR3yCNkM/B\ntPDUrCJFoRkqLEbknVFIUjZyFjjL4NQh4yIJ8C73UcHl8bgTxZbzixU9evYyC1lx\n/RopnFnKpSz+I2LCHINUIcURDQYUi8b+zYpqLCJF8ZccLORofuswz6WZ1CfTzKXq\nBwIDAQAB\n-----END PUBLIC KEY-----"
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEoAIBAAKCAQEArIiC/PGICkA5qJtNk63/wORhEJopqj7MesuPcm1eiPHsg1cy\nnD3kplzYuwEkLyXo1CxIeHpXrLfz9p0JSdYkEK4dyYJ8IZBWLnosmJ0xLCnVLx3h\nnxKBFAlDzjCiyvcthAx6duKVK4E+LAH6IZEVlE+yfk2/ashgFnNitZbGn49kBMbx\nMbPYKiDOMtyjGSmeHi7+A75NCfPqniCFpIfOnKhczrNVVZUs5Oy2RsmZtiNLPvgU\nh6vLNeEgqhSE7xDilfQ8H0txfZ8zjLDb3VFcTCElfXpuro3PVVRYcmhF60H3gwxV\nbbowRm6K+IQkku7RX8MkZg6yGgP5wCHXU0Z1owIDAQABAoH/E/Bjjgy4rltDseRU\n2sibsmBKdQVlDrLEFRyxE3zphyyNN9DVIYw/5IyxALw6FdOvf7IyBj9fz2KqgwSQ\nvoVnamGhymT+5OW/y6PO1ZSKwz5K4TNjBYWTACJyiibp8VmuFRvsAwm8cmD7gIFu\nXw6AMnAuQXkRRfj0b0banAktMyUyV6FlyYftimuoojKgguF3QR3aLM4Eqy5bXu98\n/PXvq5fYWYvZ8xjvJFV+2nKLx+ZxkYVlYoExW3TntLNs71vzJLd5+NB/G4rVbdTc\nRNisi1IQNCye2BrR+pX08CShUN7zPRIFJiqfEF+iCbGjIQ/8VIXzR9hBN7kE8XNs\nNrUVAoGBALvITM803D/xMnjaH08OJFtpTvCFWuemTYoQwygILzFfEdr/FtpjA3CH\nyIlzf6a62p2u8cwCQHi1ZKVZaHdAd20HiVYrXtJRQjhlzt7TTyahhD4riCxyLJAP\nTIbS5VYHVePg9soJq9P7aQacrXDWZtI1GncabtFXtdjvBA41dEO3AoGBAOs2CzfL\nFRch8lHkLoCMLYFnJdTlsjO75zjPiMWZM2C0/yHv6fCk67v8kCXgq1txbRK6eHbZ\nJKxV0nsEczYjiXFkYETTpUEU5sP4zZfIuS85AH95dhyZyD6oZaYLaL4JZ20z8Y6K\ntCLuw0FFqCbhJCQzc0WKbh4dDDJtT8TYFpV1AoGARAE3/9pO4UFCXA3yRLkEZa5v\njh9dWoMZlaSYaIj+Pk0FtF+pMRGmjzw9XbncQs9smKpgmtc97fkTJ+aHNJi+J1gR\nXol6X4RaDP6huoSgJ4da0wEE4cO/a7R+rFz3/P3PFyXDekuiVLS5xlE7Zp/ewMXG\nfdeuxlWTX6q/tz2Yi2UCgYAtsA+5xK7SEXv6QDJwMcpdCmYk1oEo32Toehd9GmcK\nb93m/60XW1GW8FYnpV5josKnEqV3oHIpL3p0/sZKS9jUt8SjWeENpTu18UwuIYUn\nERFxsWwp3g0xbpBgEnNEBpuacK6JG5Ql/O7cbOVet/jHN186sMr2+nl2ChmmiLrK\nSQKBgCIdskfa/d2YdQScCUa1c4jNiYmrkFxLVCEmLF1eZFZy21sZwfEEdNa8gc9Q\nXXUCSGOSJbcIwrj3c7Pv6cLb4lYeasRq4tTpRYqvRNrEWHs31n110lepXIA0GOzs\nfKiN1qqCtEQkI/5t9nJoG3a5fPPN02PuliboLit9+qr4MVpw\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArIiC/PGICkA5qJtNk63/\nwORhEJopqj7MesuPcm1eiPHsg1cynD3kplzYuwEkLyXo1CxIeHpXrLfz9p0JSdYk\nEK4dyYJ8IZBWLnosmJ0xLCnVLx3hnxKBFAlDzjCiyvcthAx6duKVK4E+LAH6IZEV\nlE+yfk2/ashgFnNitZbGn49kBMbxMbPYKiDOMtyjGSmeHi7+A75NCfPqniCFpIfO\nnKhczrNVVZUs5Oy2RsmZtiNLPvgUh6vLNeEgqhSE7xDilfQ8H0txfZ8zjLDb3VFc\nTCElfXpuro3PVVRYcmhF60H3gwxVbbowRm6K+IQkku7RX8MkZg6yGgP5wCHXU0Z1\nowIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key_2 = RSA.import_key(lucakey)

# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "Ciao luca, sei gay??"
encrypted_message = encrypt_message(message, public_key_2)
#decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
#print("Decrypted Message:", decrypted_message)