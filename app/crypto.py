import json
import secrets
from Crypto.Cipher import AES

RAW_KEY = b"maggikhalo"
KEY = RAW_KEY.ljust(32, b'\0')

def encrypt_payload(data: dict) -> str:
    json_data = json.dumps(data).encode('utf-8')
    nonce = secrets.token_bytes(12)  # GCM standard nonce size
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    
    ciphertext, tag = cipher.encrypt_and_digest(json_data)
    
    # Format: IV:Ciphertext+Tag
    return f"{nonce.hex()}:{(ciphertext + tag).hex()}"