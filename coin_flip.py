import random

passa = 0
streak = 0

for test_numerow in range(10000):
    lista = []
    for i in range(100):
        lista.append(random.randint(0,1))

    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            streak = 0
            passa += 1

wynik = passa / 100
print('Szansa na 6 z rzedu wynosi: ' + str(wynik) + ' %') 


        
