#!python3
# program który kopiuje wszystkie pliki z danego katalogu, do innego podfolderu


import os, shutil, re


#tworzenie regexu dopasowujacego pliki z zakonczeniem .txt
data_pattern = re.compile(r"""^(.*?) #cały tekst przed rozszerzeniem
    (\.py)$     #wybrane rozszerzenie pliku
    """,re.VERBOSE)

p = r'C:\\Python\\'     #okreslenie w jakim folderze beda pliki
os.makedirs('C:\\Python\\kopia_zapasowa')       #tworzenie folderu kopii zapasowej
for filename in os.listdir('.'):        #   os.listdir('.') tworzy liste string wszystkich plików znajdujących się w danym folderze (.) oznacza current working directory
    mo = data_pattern.search(filename)
    # mo = matching object - sprawdzenie czy dany plik zgadza sie z naszymi wymaganiami co do rozszerzenia
    if mo == None:
        continue            #warunek powodujacy, ze gdy MO jest równe NONE czyli plik nie pasuje do rozszerzenia to pomijamy go i przechodzimy do kolejnego pliku z pętli
    shutil.copy(p + filename,  'C:\\Python\\kopia_zapasowa\\')
    print('Skopiowano ' + filename + ' do folderu kopia zapasowa' )


