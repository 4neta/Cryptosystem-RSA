print('-- RSA Algorithm \\ DECRYPTION --')
print('To decrypt, you need a prepared file "crypto.txt".')
print("Enter your private key")
d = int(input(" d = "))
n = int(input(" n = "))

f = open("crypto.txt","r")
g = open("message_from.txt", "w")

while True:
    line = f.readline().strip()
    if not line:
        break                     # end loop when EOF
    numb = pow(int(line),d)%n     # decrypt numbers
    txt = chr(numb)               # conversion into the original text
    g.write(txt)                  # writing to a file, char by char

f.close()
g.close()