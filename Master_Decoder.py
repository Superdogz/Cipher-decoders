import math

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def cesar_cipher(code):
    for i in range(1,26): #go through each shift
        shifted = ""

        for l in code: #create the shifted string
            shifted = shifted + alpha[(alpha.index(l)+i)%26]

        with open("words.txt") as file: #check for valid words
                for word in file:
                    if word.strip() in shifted:
                        print("Found Ceasar Shift at P=C+"+str(i)+" ("+word.strip()+")")
                        print(shifted)
                        print()
                        break #only needs one recognized word

# def transposition_cipher(code):
#     tracker = list(code)

#     for l in range(2,math.ceil(len(code)/2)+1):
#         temp = tracker.copy()
#         curr = 0
#         decrypt = ""
#         while len(temp) != 0:
#             decrypt = decrypt + code[curr]
#             temp.remove(curr)
#             curr += l
#             if curr >= len(code):
#                 try:
#                     curr = temp[0]
#                 except:
#                     break
#         with open("words.txt") as file: #check for valid words
#             for word in file:
#                 if word.strip() in decrypt:
#                     print("Found Ceasar Shift at P=C+"+str(i)+" ("+word.strip()+")")
#                     print(decrypt)
#                     print()
#                     break #only needs one recognized word

def multiplication_cipher(code):
    mult_inverses = [1,9,21,15,3,19,7,23,11,5,17,25]
    for m in mult_inverses:
        multiplied = ""
        for i in code:
            multiplied = multiplied + alpha[(alpha.index(i)*m)%26]
        with open("words.txt") as file: #check for valid words
            for word in file:
                if word.strip() in multiplied:
                    print("Found Multiplication Cipher at P=C*"+str(m)+"; original mult inverse was "+str(pow(m, -1, 26))+" ("+word.strip()+")")
                    print(multiplied)
                    print()
                    break #only needs one recognized word but can trigger multiple times for different inverse values.

def affine_cipher(code):
    mult_inverses = [1,9,21,15,3,19,7,23,11,5,17,25]
    for m in mult_inverses:
        for shift in range(0,26):
            affined = ""
            for i in code:
                affined = affined + alpha[(alpha.index(i)*m + shift)%26]
            with open("words.txt") as file: #check for valid words
                for word in file:
                    if word.strip() in affined:
                        print("Found Affine Cipher at P=C*"+str(m)+"+"+str(shift)+"; original mult inverse was "+str(pow(m, -1, 26))+" ("+word.strip()+")")
                        print(affined)
                        print()
                        break




if __name__ == "__main__":
    # cipher_text = "yfcfqqmazhupqzfc" 
    cipher_text = "vaoemegdaoemegdmoejlsimyusekxybjlsotmoe"
    
    cipher_text = cipher_text.lower()
    cesar_cipher(cipher_text)
    multiplication_cipher(cipher_text)
    affine_cipher(cipher_text)
 
