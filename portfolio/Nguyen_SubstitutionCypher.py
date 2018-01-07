text = 'the quick brown fox jumps over the lazy dog'
empty = ''

def encrypt (text, empty):
    for i in (text):
        if i == 'a':
            i = '&'
        if i == 'e':
            i = '*'
        if i == 'i':
            i = '%'
        if i == 'o':
            i = '#'
        if i == 'u':
            i = '@'
        empty = empty + i
    return empty
            
enc = encrypt(text, empty)
print (enc)

def decrypt(enc, empty):
    for i in (enc):
        if i == '&':
            i = 'a'
        if i == '*':
            i = 'e'
        if i == '%':
            i = 'i'
        if i == '#':
            i = 'o'
        if i == '@':
            i = 'u'
        empty = empty + i
    return empty

dec = decrypt(enc, empty)
print (dec)
