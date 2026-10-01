n = 189368
if n > 0 and n % 2 == 0:
    print(f"{n} est un nombre pair et positif")

age = int(input("Entrez votre âge : "))

if age < 12:
    print("tarif enfant")

elif age <= 17:
    print("tarif jeune")

else:
    print("tarif adulte")

    total = 0
    while total < 1000:
        total += 1
        print ( total )