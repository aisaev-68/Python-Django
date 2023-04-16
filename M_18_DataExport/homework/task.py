# lst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
#        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
#
# def decrypt(text: str, i) -> str:
#     """Добавьте код в эту функцию."""
#     decoded_string = ""
#
#     for char in text:
#         if char.isalpha():
#             decoded_char = chr((ord(char) - i) % i)
#             decoded_string += decoded_char
#         else:
#             decoded_string += char
#     return decoded_string
#
#
# def encrypt(crypt, shift):
#     alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#                 'х',
#                 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#     txt_encrypt = ''
#     word_encrypt = []
#     for item in crypt:
#         if item in alphabet:
#             index = alphabet.index(item)
#             txt_encrypt += alphabet[(index - shift) % len(alphabet)]
#         else:
#             if item == '/':
#                 txt_encrypt += '.'
#             elif item == '-':
#                 txt_encrypt += ','
#             elif item == '(':
#                 txt_encrypt += '`'
#             elif item == '.':
#                 txt_encrypt += '-'
#             elif item == '"':
#                 txt_encrypt += '!'
#             elif item == '+':
#                 txt_encrypt += ''
#             else:
#                 txt_encrypt += item
#     txt = txt_encrypt.split()
#     print(txt_encrypt)
#     index_elem = -3
#     for elem in txt:
#         ind = (index_elem + len(elem)) % len(elem)
#         word_encrypt.append(elem[ind:] + elem[:ind])
#         for i_symb in elem:
#             if i_symb == '.':
#                 index_elem -= 1
#                 break
#     return ' '.join(word_encrypt)
#
#
# if __name__ == "__main__":
#     lst = ['а', 'б', 'в', 'г',
#            'д', 'е', 'ж', 'з',
#            'и', 'й', 'к', 'л',
#            'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
#            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#     # Х 1061 - РҐ 1056 1168 112 7
#     # а 1072 - Рѕ 1056 1109 53 37
#     # к 1082 - С‰ 1057 8240
#     # е 1077 - Сѓ 1057 1107 50 30
#     # р 1088 - СЏ 1057 1039 18 49
#     # а - 1109: 1072,
#     e = {
#         1168: 1061,
#         1109: 1072,
#         8240: 1082,
#         1107: 1077,
#         1039: 1088
#     }
#     s = {
#         1035: 1087,
#         1033: 1083,
#         1029: 1103,
#         182: 1096,
#         1107: 1077,
#         177: 1090}
#     # 0 -4 3 7
#     input_str = "РҐРѕС‰СѓСЏ СЋСЉРЅР¶СѓР±, Рѕ С‘РѕС€СЊС‡С‰ СЋСЉРѕС‘СѓР±."
#     # input_str = "Хакер пляшет, а чайник плачет."
#     # [14, 10, 13, 0]  14 28 3 19
#     ds = input_str.encode('cp1251')
#     s = ds.decode('utf-8')
#     dd = sorted(set(list(s)))
#     print(dd)
#
#
#     def decode_string(encoded_string, key):
#         # Создаем словарь соответствий
#
#         key_opti = "".join(list(key) * ((len(encoded_string) // len(key)) + len(key)))
#
#         print(len(key_opti), len(key))
#         print(len(encoded_string))
#         decoded_string = ''
#         for k, char in enumerate(encoded_string):
#
#             if char.isalpha():
#                 decoded_char = chr(ord(char) - ord(key_opti[k]))
#                 decoded_string += decoded_char
#             else:
#                 decoded_string += char
#         return decoded_string
#
#
#     # encoded_string = 'Хощуя юънжуб, о ёошьчщ юъоёуб.'
#     encoded_string = "РҐРѕС‰СѓСЏ СЋСЉРЅР¶СѓР±, Рѕ С‘РѕС€СЊС‡С‰ СЋСЉРѕС‘СѓР±."
#     key = 'окна'
#     print(decode_string(encoded_string, key))  # Выведет: Хакер пляшет, а чайник плачет.

import re
import codecs


def decode_string(input_string: str, key) -> str:
    # Шаг 1: Находим все числа в строке и конвертируем их в символы
    input_string = codecs.decode(input_string.encode('cp1251'), 'utf-8').lower()
    print(input_string)
    key_opti = "".join(list(key) * ((len(input_string) // len(key)) + len(key)))

    decoded_string = ''
    for i, char in enumerate(input_string):
        if char.isalpha():
            input_string1 = chr(ord(char) + ord(key_opti[i]))
            decoded_string += input_string1
        else:
            decoded_string += char

    return decoded_string

key = 'окна'
print(decode_string("РҐРѕС‰СѓСЏ СЋСЉРЅР¶СѓР±, Рѕ С‘РѕС€СЊС‡С‰ СЋСЉРѕС‘СѓР±.", key))