# Generating the key
def keygen (plain_text, key):
    i = 0
    k = 0
    str_key = ""
    while i<len(plain_text):
        str_key += key[k]
        k += 1
        k %= len(key)
        i += 1
    return str_key
