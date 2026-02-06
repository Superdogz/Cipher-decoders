code = 'lzwugvwogjvakjkddquzsajhkpriblicvfktyfxqrxkermb'

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

code = code.lower()

for i in range(1,26):
    output = ""
    for l in code:
        output = output + alpha[(alpha.index(l)+i)%26]
    print(i)
    print(output)