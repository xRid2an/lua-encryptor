"""
Contoh penggunaan dasar
"""

from encryptor import encrypt_to_lua, encrypt_to_lua_base64

def main():
    print("🔐 Lua Encryptor - Contoh Penggunaan")
    print("=" * 40)
    
    # Contoh 1: Enkripsi sederhana
    text = "print('Hello World!')"
    key = "mysecret"
    
    print("\n📝 Teks asli:")
    print(text)
    
    print("\n🔒 Enkripsi sederhana:")
    result1 = encrypt_to_lua(text, key)
    print(result1[:200] + "...")
    
    print("\n🔒 Enkripsi Base64:")
    result2 = encrypt_to_lua_base64(text, key)
    print(result2[:200] + "...")
    
    # Simpan ke file
    with open("example_encrypted.lua", "w") as f:
        f.write(result2)
    print("\n✅ Saved to: example_encrypted.lua")

if __name__ == "__main__":
    main()
