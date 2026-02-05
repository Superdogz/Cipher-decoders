text = "lzwugvwogjvakjgddquzsaj" #change this

count = {}
percent = {}

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]
for letter in alpha:
    count[letter] = text.count(letter)
    percent[letter] = int(text.count(letter)/len(text)*100)

print("Letter count:")
print(dict(sorted(count.items(), key=lambda x: x[1], reverse=True)))
print()
print("Letter percentage:")
print(dict(sorted(percent.items(), key=lambda x: x[1], reverse=True)))
    