import uuid
import random


def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code


def code(seed=None):
    if (not seed) or (type(seed) != str) or (len(seed) < 10):
        seed = str(uuid.uuid4())[:10]

    code = ""
    for character in seed:
        print(character)
        value = str(ord(character))
        code += value

    return code[:20]
    # return seed


print(code('detail views'))
print(get_promo_code(20))
