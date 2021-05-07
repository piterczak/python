import random, sys

wygrane = 0 
przegrane = 0
remisy = 0
ex = 0
exit

print('Wybierz (k)amień, (p)apier lub (n)ożyce i sprawdź czy wygrasz! Jeśli chcesz wyjść naciśnij (w)yjście.')
while True:
    print( str(wygrane), 'wygrane, ', str(przegrane), 'przegrane, ', str(remisy), 'remisy') #1- kamien, 2- papier, 3- nozyce
    komputer = random.randint(1,3)
    if (komputer == 1):
        rk = 'kamien'
    if (komputer == 2):
        rk = 'papier'
    if (komputer == 3):
        rk = 'nozyce'
    gracz = input()
    if gracz == 'w':
        sys.exit()
    elif (gracz == 'k'):
        ruchgracza = 'kamien'
        rg = 1
    elif (gracz == 'p'):
        ruchgracza = 'papier'
        rg = 2
    elif (gracz == 'n'):
        ruchgracza = 'nozyce'
        rg = 3
    else: 
        print('Niewłaściwy wybór, spróbuj ponownie')
        ex = ex + 1 
        rg = 0
        if (ex == 3):
            sys.exit()
    if (rg > 0):
        if (rg == komputer):
            print('Remis')
            remisy = remisy + 1
        if ((rg == 1 and komputer == 2) or (rg == 2 and komputer == 3) or (rg == 3 and komputer == 1)):
            print(str(ruchgracza) + ' vs ' + str(rk))
            print ('Przegrana')
            przegrane = przegrane + 1
        if ((rg == 1 and komputer == 3) or (rg == 2 and komputer == 1) or (rg == 3 and komputer == 2)):
            print(str(ruchgracza) + ' vs ' + str(rk))
            print ('Wygrana')
            wygrane = wygrane + 1

    