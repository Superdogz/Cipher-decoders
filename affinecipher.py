code = "vaoemegdaoemegdmoejlsimyusekxybjlsotmoe"


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mult_inverses = [1,9,21,15,3,19,7,23,11,5,17,25]
for m in mult_inverses:
    for shift in range(0,26):
        affined = ""
        for i in code:
            affined = affined + alpha[(alpha.index(i)*m + shift)%26]
        print(affined)