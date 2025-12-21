def encode(message, key):
    lower_map = {}
    upper_map = {}
    for i in range(0, len(key), 2):
        p_ = key[i:i+2]
        if len(p_) == 2:
            a, b = p_[0], p_[1]
            lower_map[a] = b
            lower_map[b] = a
            upper_map[a.upper()] = b.upper()
            upper_map[b.upper()] = a.upper()

    r = ""
    for char in message:
        if char.islower() and char in lower_map:
            r += lower_map[char]
        elif char.isupper() and char in upper_map:
            r += upper_map[char]
        else:
            r += char

    return r

def decode(encrypted_message, key):
    return encode(encrypted_message, key)

print(encode("ABCD", "agedyropulik"))           # => GBCE
print(encode("Ala has a cat", "gaderypoluki"))     # => Gug hgs g cgt
print(decode("Dkucr pu yhr ykbir", "politykarenu")) # => Dance on the table
print(decode("Hmdr nge brres", "regulaminowy"))    # => Hide our beers
