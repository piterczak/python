#!python3
# program który kopiuje wszystkie pliki z danego katalogu, do innego podfolderu


import os, shutil, re


#tworzenie regexu dopasowujacego pliki z zakonczeniem .txt
data_pattern = re.compile(r"""^(.*?) #cały tekst przed rozszerzeniem
    (\.py)$
    """,re.VERBOSE)

p = r'C:\\Python\\'
os.makedirs('C:\\Python\\kopia_zapasowa')
for filename in os.listdir('.'):
    mo = data_pattern.search(filename)

    if mo == None:
        continue
    shutil.copy(p + filename,  'C:\\Python\\kopia_zapasowa\\')
    print('Skopiowano ' + filename + ' do folderu kopia zapasowa' )


