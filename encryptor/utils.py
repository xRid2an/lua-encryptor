"""
Utility functions for file handling
"""

import os
from .core import encrypt_to_lua_base64


def encrypt_file(input_file, output_file, key="default_key"):
    """
    Enkripsi file Lua
    
    Args:
        input_file (str): Path file input
        output_file (str): Path file output
        key (str): Kunci enkripsi
    
    Returns:
        bool: True jika berhasil
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        encrypted = encrypt_to_lua_base64(content, key)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def encrypt_directory(directory, key="default_key", pattern="*.lua"):
    """
    Enkripsi semua file dalam direktori
    
    Args:
        directory (str): Path direktori
        key (str): Kunci enkripsi
        pattern (str): Pattern file (default: *.lua)
    
    Returns:
        list: Daftar file yang berhasil dienkripsi
    """
    import glob
    
    encrypted_files = []
    pattern_path = os.path.join(directory, pattern)
    
    for file_path in glob.glob(pattern_path):
        output_path = file_path.replace('.lua', '_encrypted.lua')
        if encrypt_file(file_path, output_path, key):
            encrypted_files.append(output_path)
            print(f"✅ Encrypted: {os.path.basename(file_path)}")
    
    return encrypted_files
