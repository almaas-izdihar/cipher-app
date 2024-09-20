from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import HTMLResponse
from typing import Optional
from app.cipher_algorithms import Vigenere, Playfair, Hill


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def get_form():
    with open("app/gui/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.post("/encrypt")
async def encrypt_file(
    file: Optional[UploadFile] = None, 
    text_input: Optional[str] = Form(None),
    key: str = Form(...),
    cipher: str = Form(...)
):
    if text_input:
        content = text_input
    elif file:
        content = await file.read()
        content = content.decode('utf-8')
    else:
        return {"error": "Harap masukkan plaintext atau upload file"}

    if cipher == "vigenere":
        vigenere = Vigenere()
        encrypted = vigenere.encrypt(content, key)
    elif cipher == "playfair":
        playfair = Playfair()
        encrypted = playfair.encrypt(content, key)
    elif cipher == "hill":
        hill = Hill()
        encrypted = hill.encrypt(content, key)

    return {"ciphertext": encrypted}

@router.post("/decrypt")
async def decrypt_file(
    file: Optional[UploadFile] = None,  
    text_input: Optional[str] = Form(None),  
    key: str = Form(...), 
    cipher: str = Form(...)
):
    if text_input:
        content = text_input
    elif file:
        content = await file.read()
        content = content.decode('utf-8')
    else:
        return {"error": "Harap masukkan chipertext atau upload encrypted file"}

    print(content)

    if cipher == "vigenere":
        vigenere = Vigenere()
        decrypted = vigenere.decrypt(content, key)
    elif cipher == "playfair":
        playfair = Playfair()
        decrypted = playfair.decrypt(content, key)
    elif cipher == "hill":
        hill = Hill()
        decrypted = hill.decrypt(content, key)

    print(decrypted)
    return {"plaintext": decrypted}
