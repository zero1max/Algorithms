# Task 1

numbers = []

for i in range(5):
    s = int(input("Sonni kiriting: "))
    numbers.append(s)

nol = 0
nol1 = 0
nol2 = 0
for x in numbers:
    if x > 0:
        nol += 1
    elif x < 0:
        nol1 += 1
    else:
        nol2 += 1
print(f"Musbat sonlar soni: {nol}")
print(f"Manfiy sonlar soni: {nol1}")
print(f"0 lar soni: {nol2}")