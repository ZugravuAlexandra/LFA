import copy
SIMB=set()
STARI=set()
S_I=set()
F=set()

l={'lit:','stari:','#','tranz:','End'}   # pentru a-mi fi mai usor sa stiu ce citesc din fisier 
f=open('input2.txt')
for linie in f:
    linie=linie.split(',')
    linie=" ".join(linie)
    linie=set(linie.rstrip().split()) # eliminam spatiile si impartim setul de carctere in set de cuvinte cheie
    if linie.intersection(l)==set():  # verificam daca linia nu contine niciunl din cuvintele cheie din set
        for x in linie:
            if x.isnumeric()==False and len(linie)==1:  # verificam daca elementul nu este numeric si daca linia contine doar un element
                SIMB.update(x)        #adaugam literele alfabetului
            elif x.isnumeric()==True:
                x=int(x)    # daca este numar, il convertim la nr intreg
                STARI.add(x)          #adaugam starile automatului
                if len(linie)>1 and 'S_I' in linie:
                    S_I.add(x)  # adaugam starea initiala
                elif len(linie)>1 and 'F' in linie:
                    F.add(x)  # adaugam starea finala
print(SIMB)
print(STARI)
print(S_I)
print(F)
f.close()

stari = len(STARI)  # nr de stari

L=[[0 for i in range(len(SIMB))] for j in range(len(STARI))]  # facem o matrice cu dim len(stari) si literele din stari si simb
f=open('input2.txt')
for linie in f:
        linie=linie.split(',')
        linie=" ".join(linie)
        linie=linie.rstrip().split()
        if set(linie).intersection(l)==set():
            if len(linie)==3:  # daca linia contine doar 3 elem atunci x, z vor fi starile converite la int
                x=int(linie[0])
                z=int(linie[2])
                e=list(SIMB) # facem SIMB ca lista pentru a putea sa accesam pozitiile elementelor 
                for i in range(len(e)):  # parcurgem pozitiile din lista e
                    if e[i]==linie[1]:  # daca elementul este egal cu al doilea element din linie atunci y devine valoare lui i
                        y=i
                L[x][y]=z  
f.close()

print("Lista de adiacenta este:")
for linie in L:
    print('  '.join(map(str, linie)))

m = [[0 for i in range(len(STARI))] for j in range(len(STARI))]  # matrice de dim nr de stari din STARI

# completam matricea cu 1 sau 0 in funcie de starea finala
for i in range(len(STARI)):                 #matricea completata cu 1 sau 0
    for j in range(len(STARI)):
        if j <= i-1:
            if (i in F) ^ (j in F) == True:
                 m[i][j] = 1
            else:
                 m[i][j] = 0
        else:
            m[i][j] = []
print("Matrice completata cu 1 sau 0 este:")
for linie in m:
    print('  '.join(map(str, linie)))

ok = 1
while (ok != 0):                        #extindem pe 1 in matrice
    ok = 0
    for i in range(1,len(STARI)):
        for j in range(len(STARI)-1):
            if j <= i - 1:
                k = 0
                if m[i][j] == 0:
                    while (k != len(SIMB)):  # verificam daca exista o litera k in SIMB a.i starea din tranzitia din j cu k si starea din tranzitia i cu k sa fie marcate cu 1
                        if m[L[j][k]][L[i][k]] == 1 or m[L[i][k]][L[j][k]] == 1:
                            m[i][j] = 1
                            ok = 1
                        k = k+1

print("Matricea extinsa cu 1 este:")
for linie in m:
    print('  '.join(map(str, linie)))

U = set()  # set pentru perechile marcate
u = []  #lista de perechi nemarcate 
for i in range(1,len(STARI)):
    for j in range(len(STARI)-1):
        if j <= i - 1:
            if m[i][j] == 0:  # perechea i, j este pusa in perechea nemarcata 
                u.append(list((i,j)))
                U.add(i)
print("Perechile nemarcate sunt:")
print(u)

STARI = STARI.difference(U)  #eliminam starile marcate din setul STARI


#actualizam lista de adiacena pentru a inlocui starile marcate cu starile coresp din parechile nemarcate
for i in range(len(L)):
    for j in range(len(SIMB)):
        if L[i][j] not in STARI: # daca starea respectiva nu se afla in STARI se cauta in u perechea  si se inlocuieste cu perechea nemarcata
            for p in range(len(u)):
                if u[p][0] == L[i][j]:
                    L[i][j] = u[p][1]

Lm = copy.deepcopy(L)  # copiem in Lm pe L
for i in range(len(u)):
    j = 0
    del Lm[u[i][j]]  # eliminam liniile corespunzatoare starilor marcae din lista Lm
print()
print("DFA minimizat este:")
print("lit:")
for x in SIMB:
    print(x)
print("End")

print("stari:")
for x in STARI:
    if x in S_I:
        print(f"{x},S_I")
    elif x in F:
        print(f"{x},F")
    else:
        print(x)
print("End")

STARI = list(STARI)
SIMB = list(SIMB)
print("tranz:")
for i in range(len(STARI)):
    b = 0
    for j in range(len(SIMB)):
        print(f"{STARI[i]}, {SIMB[j]}, {Lm[i][b]}")
        b += 1

print("End")