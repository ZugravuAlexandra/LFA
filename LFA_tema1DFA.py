with open("date.txt", "r") as file:
    # alfabetul si starile
    alfabet = file.readline().split() 
    stari = file.readline().split()

    # DFA-ul ca un dictionar de dictionare
    dfa = {stare:{litera: [] for litera in alfabet} for stare in stari}
    #print(dfa)

    # Citim tranzitiile si le adaugam in DFA
    for linie in file.readlines():
        linie = linie.split()
        if len(linie) == 1 and linie[0][0] in alfabet:
            # Daca am o singura litera, litera este cuvantul pe care il verific
            cuvant = linie[0]
        elif len(linie) != 1 and linie[1] in alfabet :
            # Daca am o tranzitie, o adaug in dfa
            stare_in, litera, stare_fin = linie
            dfa[stare_in][litera].append(stare_fin)
        else:
            # starile finale
            stari_finale = linie

# Citim cuvantul
cuvant = input("Introduceti un cuvant: ")

drum = [] 
stare_c = stari[0] 

# verificare pentru cuvantul vid
if cuvant == '':
    if stare_c in stari_finale:
        # daca este un cuvant vid si starea curenta este finala, atunci cuvantul vid este acceptat
        print("Cuvantul vid este acceptat")
    else:
        # altfel cuvantul vid nu este acceptat
        print("Cuvantul vid nu este acceptat")
else:
    ok = False
    for pozitie in range(0, len(cuvant)):
        litera = cuvant[pozitie]
        if dfa[stare_c][litera] != []:
            stare_c = dfa[stare_c][litera][0]
            drum.append(stare_c)
            # print(drum)
            if stare_c in stari_finale and pozitie == len(cuvant) - 1:
                # cavantul este acceptat daca suntem la sfarsitul lui si suntem in stare finala
                print(f"Cuvantul {cuvant} este acceptat, iar drumul sau este: {' => '.join(drum)}")
                ok = True
                break
        else:
            break
    if ok == False:
        print(f"Cuvantul {cuvant} nu este acceptat :( \nIncearca alt cuvant")

