import random


print("Välkommen till spel 21.")
print("Kasta tärningen och kom nära 21.")
print("Över 21 betyder att du förlorar.")
print("21 betyder att du vinner.")

igen = "ja"

while igen == "ja":
    summa = 0
    kasta_igen = "ja"

    while kasta_igen == "ja":
        tärning = random.randint(1, 6)
        summa += tärning

        print("\nDu fick:", tärning)
        print("Din summa är:", summa)

        if summa > 21:
            print("Du fick över 21 och förlorade.")
            kasta_igen = "nej"

        elif summa == 21:
            print("Du fick 21 och vann.")
            kasta_igen = "nej"

        else:
            kasta_igen = input("Kasta igen? Skriv ja eller nej: ").lower()

            if kasta_igen == "nej":
                avstånd = 21 - summa
                print("\nDu slutar kasta.")
                print("Din summa är:", summa)
                print("Det är", avstånd, "från 21.")
                print("Du fick inte 21 och förlorade.")

            elif kasta_igen != "ja":
                print("Jag förstår inte. Spelet är slut.")
                kasta_igen = "nej"

    igen = input("\nSpela igen? Skriv ja eller nej: ").lower()

print("\nTack för att du spelade.")
