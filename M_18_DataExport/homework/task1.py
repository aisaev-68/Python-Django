import codecs

def decode_string(input_string: str) -> str:
    decoded_string = codecs.decode(input_string.encode('cp1251'), 'utf-8')

    return decoded_string


def decrypt_string(input_string: str, key) -> str:
    decrypted_string = ''

    key_opti = "".join(list(key) * ((len(input_string) // len(key)) + len(key)))
    print(len(key_opti))
    for i, char in enumerate(input_string):
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('а') + ord(key_opti[i])) % 32 + ord('а'))
            decrypted_string += shifted_char
        else:
            decrypted_string += char
    return decrypted_string

def decode_and_decrypt(input_string: str, key) -> str:
    decoded_string = decode_string(input_string)
    print(decoded_string)
    decrypted_string = decrypt_string(decoded_string, key)
    return decrypted_string

input_string = "РҐРѕС‰СѓСЏ СЋСЉРЅР¶СѓР±, Рѕ С‘РѕС€СЊС‡С‰ СЋСЉРѕС‘СѓР±."
# input_string = "Хакер пляшет, а чайник плачет."
key = 'окна'
result = decode_and_decrypt(input_string, key)
print(result)