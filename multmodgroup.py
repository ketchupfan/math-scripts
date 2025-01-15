from math import gcd

multmodgroup = []

target = int(input("Which multiplication integer modulo group? "))
print()

for x in range(target):
    if gcd(x, target) == 1:
        multmodgroup.append(x)

print(multmodgroup)
print()

for x in multmodgroup:
    factor = x
    iter = 0
    while True:
        print(x % target, end =" ")
        iter += 1
        if (x % target == 1 or iter > 100):
            break
        
        x = x * factor
        
    print()
