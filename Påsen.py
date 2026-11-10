itemlist = []


print("välkommen till påsen, här kan du: ")



while True:
    print("sida 1/2")
    print("V: Visa innehållet i påsen")
    print("L: Lägg till ett item i påsen")
    print("F: leta efter ett item i påsen")
    print("Q: Avsluta programmet")
    print("N: kolla nästa sida")
    print("---------------------------------------------------")  
    val3 = input("Vad vill du göra?: ").upper()

    if val3 == "N":
        print("sida 2/2")
        print("Här kan du:")
        print("T: Ta bort ett item från påsen")
        print("R: Rensa påsen")
        print("O: gå tillbaka till sida 1")
        print("Q: Avsluta programmet")
        print("---------------------------------------------------")
        val2 = input("Vad vill du göra?:").upper()
        if val2 == "T":
            print("---------------------------------------------------")
            ta_bort = input("Vilket item vill du ta bort?: ").upper()
            if ta_bort in itemlist:
                itemlist.remove(ta_bort)
                print(f"{ta_bort} har tagits bort från påsen.")
                print("---------------------------------------------------")
            else:
                print("----------------------------------------------------")
                print(f"{ta_bort} finns inte i påsen.")

        elif val2 == "R":
            if itemlist:
                rensade_items = itemlist.copy()
                itemlist.clear()
                print("---------------------------------------------------")
                print(f"{rensade_items} har rensats.")
                print("---------------------------------------------------")
            else:
                print("Din påse är redan tom.")
                print("---------------------------------------------------")
        elif val2 == "O":
            continue

        elif val2 == "Q":
            print("programmet avslutas.")
            break
        
        continue

    val = val3
    if val == "V":
        print(f"dina items är: {itemlist}")
        print("---------------------------------------------------")
        
        
    elif val == "L":
        itemlist.append(input("Vad vill du lägga till i påsen?: ").upper())
        print("---------------------------------------------------")
        print(f"{itemlist[-1]} har lagts till i påsen.")
        print("---------------------------------------------------")

    elif val == "F":
        search_item = input("Vad vill du leta efter i påsen?: ").upper()
        if search_item in itemlist:
            print("Itemet finns i påsen!")
        else:
            print("Itemet finns inte i påsen.")


    elif val == "Q":
        print("Programmet avslutas.")
        break
            
        
        

        

        





