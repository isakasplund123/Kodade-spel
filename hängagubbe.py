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
