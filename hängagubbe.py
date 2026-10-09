ord = input("Skriv in ordet som ska gissas: ").lower()

gissningar = []
fel = 0
max_fel = 6

lifeline = [
    r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
    r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
    r"""
 ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
    r"""
 ♥ ♥ ♥
      O
     /|\
     / \
""",
    r"""
 ♥ ♥
      O
     /|\
     / \
""",
    r"""
 ♥
      O
     /|\
     / \
""",
    r"""
      
      O
     /|\
     / \
"""
]

def visa_ord(ord, gissningar):
    display = ""

    for bokstav in ord:
        if bokstav in gissningar:
            display = display + bokstav + " "
        else:
            display = display + "_ "

    print(display)
    return display


def visa_gubbe(fel):
    print(lifeline[fel])


print("\n" * 30)

while fel < max_fel:
    visa_gubbe(fel)
    visa_ord(ord, gissningar)

    print("Gissade bokstäver:", gissningar)
    gissning = input("Gissa en bokstav: ").lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv bara en bokstav!")
        continue

    gissningar.append(gissning)

    if gissning in ord:
        print("Rätt gissat!")
    else:
        print("Fel gissat!")
        fel = fel + 1
