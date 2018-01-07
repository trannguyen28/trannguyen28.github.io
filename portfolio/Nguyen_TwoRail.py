text = 'the quick brown fox jumps over the lazy dog'
even = ''
odd = ''

def encrypt (text, even, odd):
    count = 0 
    for i in (text):
        count = count + 1
        if count % 2 == 0:
            even = even + i
        if count % 2 == 1:
            odd = odd + i
    cipher = even + odd
    return cipher

enc = encrypt(text, even, odd)
print (enc)

def decrypt (enc, even, odd):
    count = 0
    counteven = 0
    countodd = -1
    
    for i in (enc):             # separate the string
        count = count + 1
        if count >= 22:
            odd = odd + i
        else:
            even = even + i
            
    for i in range (43):        # order alternately
        x = sum(zip(list(odd), list(even)+[0]), ())[:-1]
        str1 = ''.join(x)
    return str1
       
dec = decrypt(enc, even, odd)
print (dec)
