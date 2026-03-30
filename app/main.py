from fastapi import FastAPI 
from Crypto.Cipher import AES 
import json, secrets 
app = FastAPI() 
KEY = b"maggikhalo".ljust(32, b'\0') 
@app.get("/") 
def root(): return {"status": "online"} 
@app.get("/api/pw/batches") 
def batches(): 
    data = {"success": True, "data": [{"id": "1", "name": "Test Batch"}]} 
    json_data = json.dumps(data).encode() 
    nonce = secrets.token_bytes(12) 
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce) 
    ct, tag = cipher.encrypt_and_digest(json_data) 
    return {"data": f"{nonce.hex()}:{(ct + tag).hex()}"} 
