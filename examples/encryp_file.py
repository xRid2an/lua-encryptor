"""
Contoh enkripsi file
"""

from encryptor import encrypt_file

def main():
    # Buat file contoh
    with open("example.lua", "w") as f:
        f.write("""
local function greet(name)
    return "Hello, " .. name
end
print(greet("World"))
""")
    
    print("📄 File example.lua dibuat")
    
    # Enkripsi file
    success = encrypt_file("example.lua", "encrypted_example.lua", "mykey123")
    
    if success:
        print("✅ File berhasil dienkripsi menjadi encrypted_example.lua")
        
        # Tampilkan hasil
        with open("encrypted_example.lua", "r") as f:
            content = f.read()
            print("\n📝 Hasil enkripsi:")
            print(content[:300] + "...")

if __name__ == "__main__":
    main()
