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
