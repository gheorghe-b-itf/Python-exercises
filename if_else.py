# if
piesa_frumoasa = True

if piesa_frumoasa == True:
    print('dau mai tare')
    print('fredonez')
print("opresc radio")

# if else
# daca nr este par printam par
# alfel printam impar

nr = 4
# ce inseamna par? // se imparte exact la 2; da restul 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# if, else if, else
# cum ne saluta robotelul in functie de ora
ora = int(input('Introdu ora:')) #luam date de la tastatura; ne asiguram ca sunt transformate in int
if ora < 0:
    print('ora negativa')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 19:
    print('buna seara')
elif ora <= 24:
    print('noapte buna')
else:
    print('ora invalida')

#robot telefonic

optiune = int(input('Introdu ora:'))
if optiune == 0:
    print('meniu anterior')
elif optiune == 1:
    print('alege limba romana')
elif optiune == 2:
    print('alege limba engleza')
else:
    print('Optiune invalida')