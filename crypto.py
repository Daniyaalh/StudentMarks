import base64

#Taken from
#https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def getFile():
    file = open("test2.txt", "w")
    #d = {"csc235":[["a1",56,57,60],["hi",34,36,12]], "csc311":[["aa6",34,38,12]]}
    #to_write = encode("3334", str(d))
    password = "3331"
    to_write = encode("3331\n", "3331\n")
    file.write(to_write)
    """
    password = "3331"
    l = file.read()
    print(l)
    a = encode(password, l)
    print(a)
    b = decode(password, a)
    print(b)
    """
def test_write():
    file = open("test2.txt", "w")
    file.write(str(encode("3331", "3331")) + "\n")
    file.write("jj")
    file.close()

#test_write()
print(decode("3331", "ZmZmYg=="))
