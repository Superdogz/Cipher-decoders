code = "yfcfqqmazhupqzfc"
mult_inverse = [1,9,21,15,9,19, 7,23,11, 5,17,25]
              # 1,3, 5, 7,9,11,15,17,19,21,23,25

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]

for m in mult_inverse:
    output = ""
    for i in code:
        output = output + alpha[(alpha.index(i)*m)%26]
    print(m)
    print(output)
    print()
