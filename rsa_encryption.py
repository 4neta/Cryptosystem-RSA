print('-- RSA Algorithm \\ ENCRYPTION --')
print("Enter your public key:")
e = int(input(" e = "))
n = int(input(" n = "))
print("Enter the name of message file with the extension (recommend *.txt)")
name_of_file = input(" file name = ")

f = open(name_of_file, "r")
g = open("crypto.txt", "w")

while True:
    char = f.read(1)
    if not char:
        break               # end loop when EOF
    code = int(ord(char))   # codes of chars
    cryp = pow(code,e)%n    # conversion into a cryptogram
    g.write(str(cryp)+"\n") # writing to a file, line by line

f.close()
g.close()