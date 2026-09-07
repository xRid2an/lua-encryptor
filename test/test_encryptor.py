"""
Unit tests untuk encryptor
"""

import pytest
from encryptor import encrypt_to_lua, encrypt_to_lua_base64


def test_encrypt_to_lua():
    result = encrypt_to_lua("test", "key")
    assert "Lua Encrypted Code" in result
    assert "decrypt" in result
    assert "test" not in result  # Tidak ada plaintext


def test_encrypt_to_lua_base64():
    result = encrypt_to_lua_base64("test", "key")
    assert "Base64" in result
    assert "decrypt_base64" in result
    assert "test" not in result


def test_empty_text():
    with pytest.raises(ValueError):
        encrypt_to_lua("", "key")


def test_empty_key():
    with pytest.raises(ValueError):
        encrypt_to_lua("test", "")


def test_different_keys():
    text = "hello"
    result1 = encrypt_to_lua(text, "key1")
    result2 = encrypt_to_lua(text, "key2")
    assert result1 != result2


@pytest.mark.parametrize("text", [
    "print('Hello')",
    "local x = 10",
    "function test() end",
    "Hello World! 123"
])
def test_various_texts(text):
    result = encrypt_to_lua_base64(text, "testkey")
    assert "encrypted_data" in result
    assert text not in result


if __name__ == "__main__":
    pytest.main(["-v"])
