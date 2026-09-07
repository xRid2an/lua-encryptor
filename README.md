# 🔐 Lua Encryptor

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache2.0-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/xRid2an/lua-encryptor)](https://github.com/xRid2an/lua-encryptor)

Enkripsi teks/script Lua menggunakan Python dengan metode XOR dan Base64.

## ✨ Fitur

- 🔒 Enkripsi XOR sederhana
- 📦 Dukungan Base64 untuk teks panjang
- 🚀 Auto-generate kode Lua dengan fungsi decrypt
- 📁 Enkripsi batch file
- 🛡️ Obfuscation script Lua

# 🚀 Cara penggunaan

## CLI (Command Line Interface)
```bash
# Enkripsi teks langsung:
lua-encrypt "print('Hello World!')" -k "mykey123"

# Enkripsi dari file:
lua-encrypt -f script.lua -k "mykey123" -o encrypted.lua

# Batch encrypt semua file .lua:
lua-encrypt -d ./scripts -k "masterkey" --batch
```
## Python API
```bash
from encryptor import encrypt_to_lua, encrypt_to_lua_base64

# Enkripsi sederhana
result = encrypt_to_lua("print('Hello')", "key123")

# Enkripsi dengan Base64 (rekomendasi)
result = encrypt_to_lua_base64("print('Hello')", "key123")

# Simpan ke file
with open("encrypted.lua", "w") as f:
    f.write(result)
```

## 📦 Instalasi

```bash
# Clone repository
git clone https://github.com/xRid2an/lua-encryptor.git
cd lua-encryptor

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
