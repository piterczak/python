import random, sys

wygrane = 0 
przegrane = 0
remisy = 0


def pobieranieRuchuGracza(gracz):
    if gracz == 'w':
        sys.exit()
    elif (gracz == 'k'):
        ruchgracza = 'kamien'
        grajek = 1
        return grajek, ruchgracza
    elif (gracz == 'p'):
        ruchgracza = 'papier'
        grajek = 2
        return grajek, ruchgracza
    elif (gracz == 'n'):
        ruchgracza = 'nozyce'
        grajek = 3
        return grajek, ruchgracza
    else: 
        print('Niewłaściwy wybór, spróbuj ponownie')
        grajek = 0
    return grajek, ''

def ruchKomputera():
    komputer = random.randint(1,3)
    if (komputer == 1):
        rk = 'kamien'
        return komputer, rk
    if (komputer == 2):
        rk = 'papier'
        return komputer, rk
    if (komputer == 3):
        rk = 'nozyce'
        return komputer, rk
    
while True:
    comp, compMove = ruchKomputera()
    print( str(wygrane), 'wygrane, ', str(przegrane), 'przegrane, ', str(remisy), 'remisy') #1- kamien, 2- papier, 3- nozyce
    komputer = random.randint(1,3)
    player, playerMove = pobieranieRuchuGracza(input('Wybierz (k)amień, (p)apier lub (n)ożyce i sprawdź czy wygrasz! Jeśli chcesz wyjść naciśnij (w)yjście.\n'))
    if (player > 0):
        if (player == comp):
            print('Remis')
            remisy = remisy + 1
        if ((player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1)):
            print(str(playerMove) + ' vs ' + str(compMove))
            print ('Przegrana')
            przegrane = przegrane + 1
        if ((player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2)):
            print(str(playerMove) + ' vs ' + str(compMove))
            print ('Wygrana')
            wygrane = wygrane + 1


