def impartire_gramatica(fisier):
    # facem un dictionar in care cheile vor fi simboluri neterminale (literele mari), iar valorile vor fi cele terminale si neterminale (lit. mici si mari)
    gramatica = {}

    with open(fisier, "r") as f:
        for linie in f:
            # Impartim linia în stanga si dreapta
            stanga, dreapta = linie.strip().split("->")

            # Partea dreaptă a regulii de producție este o listă de simboluri terminale și neterminate separate de "|"
            dreapta = dreapta.strip().split("|")

            # Adăugăm simbolul neterminal și lista de simboluri din partea dreaptă
            gramatica[stanga] = [simbol.strip() for simbol in dreapta]

    # Returnăm dictionarul 
    return gramatica



def acceptare(gramatica, simbol_s, cuvant):
    # Verificăm dacă cuvântul este acceptat de gramatica regulată
    # simbolul de start este S
    
    # daca cuvantul este vid, vedem daca este in gramatica si are o tranzitie care sa genereze lambda
    if cuvant=="":
        if 'lambda' in gramatica[simbol_s]:
            return True
        else:
            return False
        
    for tranzitie in gramatica[simbol_s]:
        # daca lungimea este mai mare ca 1 verificam daca prima litera este la fel cu prima litera a cuvantului 
        # atunci vom apela recursiv functia acceptare cu restul cuvantului si noul simbol
        if len(tranzitie) > 1 and tranzitie[0] == cuvant[0]:
            restul_cuvant = cuvant[1:]
            if acceptare(gramatica, tranzitie[1], restul_cuvant):
                return True
        # daca lungimea este egala cu 1 verificam daca este egala cu prima litera a cuvantului si returnam True
        # deoarece se poate produce cuvantul format dintr-o singura litera
        elif len(tranzitie) == 1 and tranzitie == cuvant:
            return True
    
    # daca nicio conditie nu se respecta atunci inseamna ca acel cuvant nu este generat de gramatica
    return False


simbol_s = 'S'
gramatica = impartire_gramatica(input("Introduceți numele fișierului pentru gramatica regulată: ").strip())
cuvinte = input("Introduceți numele fișierului cu cuvinte: ")

with open(cuvinte, "r") as f:
    for linie in f:
        cuvant = linie.strip()
        if acceptare(gramatica, simbol_s, cuvant)==True:
            print(f"Cuvântul '{cuvant}' este generat de gramatică.")
        else:
            print(f"Cuvântul '{cuvant}' nu este generat de gramatică.")

