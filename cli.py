"""
Command Line Interface
"""

import argparse
import sys
from encryptor import encrypt_to_lua, encrypt_to_lua_base64, encrypt_file, encrypt_directory


def main():
    parser = argparse.ArgumentParser(
        description="Enkripsi script Lua menggunakan Python",
        epilog="Contoh: lua-encrypt 'print(\"Hello\")' -k mykey"
    )
    
    parser.add_argument(
        'text',
        nargs='?',
        help='Teks yang akan dienkripsi'
    )
    
    parser.add_argument(
        '-f', '--file',
        help='File input (.lua)'
    )
    
    parser.add_argument(
        '-d', '--directory',
        help='Direktori untuk batch encrypt'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='File output (default: output.lua)'
    )
    
    parser.add_argument(
        '-k', '--key',
        default='default_key',
        help='Kunci enkripsi (default: default_key)'
    )
    
    parser.add_argument(
        '--base64',
        action='store_true',
        help='Gunakan enkripsi Base64 (rekomendasi)'
    )
    
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Enkripsi semua file .lua dalam direktori'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Lua Encryptor v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Pilih metode enkripsi
    encrypt_func = encrypt_to_lua_base64 if args.base64 else encrypt_to_lua
    
    # Batch encrypt directory
    if args.directory and args.batch:
        print(f"📁 Encrypting all .lua files in {args.directory}")
        encrypted = encrypt_directory(args.directory, args.key)
        print(f"\n✅ {len(encrypted)} files encrypted successfully!")
        return
    
    # Encrypt file
    if args.file:
        output = args.output or args.file.replace('.lua', '_encrypted.lua')
        print(f"🔐 Encrypting: {args.file}")
        if encrypt_file(args.file, output, args.key):
            print(f"✅ Saved to: {output}")
        else:
            print("❌ Encryption failed!")
            sys.exit(1)
        return
    
    # Encrypt text
    if args.text:
        result = encrypt_func(args.text, args.key)
        print(result)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"\n✅ Saved to: {args.output}")
        return
    
    # No input
    parser.print_help()


if __name__ == "__main__":
    main()
