temp=int(input("Koliko je stupnjeva?"))

if temp<0:
    print("smrzavanje")
elif temp<= 15:
    print("Hladno")
elif temp>=26:
    print("vruće")
else:
    print("Ugodno je")


































# Program pita za temperaturu (u °C).
# Ispod 0 → "Smrzavanje"
# 0–15 → "Hladno"
# 16–25 → "Ugodno"
# 26 i više → "Vruće"