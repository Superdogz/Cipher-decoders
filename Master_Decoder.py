import math

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def cesar_cipher(code, m_w):
    for i in range(1,26): #go through each shift
        shifted = ""

        for l in code: #create the shifted string
            shifted = shifted + alpha[(alpha.index(l)+i)%26]

        word_count = 0
        with open("words.txt") as file: #check for valid words
                for word in file:
                    if word.strip() in shifted:
                        word_count += 1
        if word_count >= m_w:
            print("Found Ceasar Shift at P=C+"+str(i)+" ("+word.strip()+")")
            print(shifted)
            print()

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

def multiplication_cipher(code, m_w):
    mult_inverses = [1,9,21,15,3,19,7,23,11,5,17,25]
    for m in mult_inverses:
        multiplied = ""
        for i in code:
            multiplied = multiplied + alpha[(alpha.index(i)*m)%26]
        
        word_count = 0
        with open("words.txt") as file: #check for valid words
            for word in file:
                if word.strip() in multiplied:
                    word_count += 1
        if word_count >= m_w:
            print("Found Multiplication Cipher at P=C*"+str(m)+"; original mult inverse was "+str(pow(m, -1, 26))+" ("+word.strip()+")")
            print(multiplied)
            print()

def affine_cipher(code, m_w):
    mult_inverses = [1,9,21,15,3,19,7,23,11,5,17,25]
    for m in mult_inverses:
        for shift in range(0,26):
            affined = ""
            for i in code:
                affined = affined + alpha[(alpha.index(i)*m + shift)%26]
            
            word_count = 0
            with open("words.txt") as file: #check for valid words
                for word in file:
                    if word.strip() in affined:
                        word_count += 1
            if word_count >= m_w:
                print("Found Affine Cipher at P=C*"+str(m)+"+"+str(shift)+"; original mult inverse was "+str(pow(m, -1, 26))+" ("+word.strip()+")")
                print(affined)
                print()
                        




if __name__ == "__main__":
    # cipher_text = "yfcfqqmazhupqzfc" 
    cipher_text = "HBGXXLDSWVQLLAISYMQPMUIOYXCXYIWXNYFDSUVRPQQEWXURZLVVJVGMPFGLCUVSYAJSDYNOGYPDJZKBDNDSCNJNLSYSEBCZLLVIZZUZPWKKWGCQYCHSNYPMPNJOCYYKDGWMSNCVVUPNPRESEYOOYNKXSIDLTNQXMCNLZQCCGYTICCERLHFFPLAZPWWVTUTKYXJKOVGOYNJOHIPNPLQPEBGCSCTOQITCTRVIJYCBDYXOCMKXNYJSDLGWLLMKMFGNTMCZAYCBLHEOLHFEYYZZPWVOOLGDFLPDSYTSNBGCSYJKOVTYFAJDMUEUQLQWSCUDCUXOWMJKOHQGMYEYXYCVZWCVWYIOYXCXOCVGLMRYAONKCFALPFKOGYFGSUVOGYTDSYQVOZQVVGKQSNUKJNJKENJOSCNVLNDKRYPNHUUPFFNYQNWXYYNCDNWPQYFGTNJDCYCCFLG"
    min_words = 2 #minimum english words needed to ouput the decrypted ciper
    
    cipher_text = cipher_text.lower()
    cesar_cipher(cipher_text, min_words)
    multiplication_cipher(cipher_text, min_words)
    affine_cipher(cipher_text, min_words)
 
