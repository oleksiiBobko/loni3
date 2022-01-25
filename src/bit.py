a = 0b10100111
b = 0b01000000
c = a & b

for i in range(16):
    m = 1 << i
    print(1 if (a & m) > 0 else 0)