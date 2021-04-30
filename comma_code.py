import sys
spam = ['apples', 'oranges', 'beer', 'butter']

def przecinki(wyrazy):
    linia = ' '
    if len(wyrazy) > 1:
        for i in range(len(wyrazy)-1):
            linia += str(wyrazy[i]) + ', '
        linia += 'and ' + str(wyrazy[len(wyrazy)-1])
        return linia
    elif len(wyrazy) == 1:
        linia = wyrazy[0]
        return linia
    elif len(wyrazy) >= 0 :
        print('Blad danych w liscie')
        
    


while True:
    nowa_lista=[]
    ilosc = 0
    ilosc = input('podaj ilosc wyrazow w nowej liscie lub wpisz cokolwiek innego aby wyjsc":   ')
    try: 
        int(ilosc) 
    except: 
        print('Podaj wlasciwa liczbe!')
        break
    for i in range(int(ilosc)):
        nowa_lista.insert(i, input('Podaj ' + str(int(i)+1) + ' wyraz:  '))
    print(przecinki(nowa_lista))



