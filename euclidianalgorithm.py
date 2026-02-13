dividend = 39
modulo = 100

a = dividend
b = modulo
if a < b:
    a,b = b,a

while a % b != 0:
    a,b = b, a%b

print("gcd: "+str(b))

if b == 1: #inverse
    print("inverse: "+str(pow(dividend, -1, modulo)))

