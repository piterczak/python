def collatz(num):
    if(num != 1):
        if (num % 2 == 0):  # Parzyste
            num = num // 2
            return num
        elif (num % 2 == 1):    # Nieparzyste
            num = (3 * num) + 1
            return num

try:
    num = int(input(('Wprowadź liczbę \n'))) # sprawdzam czy num jest integerem
    while num != 1:                          # pętla 
        collatz(num)
        print(num)
        num = collatz(num)
    else:
        print('Koniec, wynik wynosi 1 \n')
except ValueError:
    print('Błąd, wprowadź poprawną liczbę')
        
