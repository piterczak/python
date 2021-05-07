#! python3
# rename_dates.py jest to program do zmiany nazw plików z amerykańskiego formatu MM-DD-YYYY na europejski format DD-MM-YYYY


import shutil, os, re

#tworzenie regexu który dopasowuje sie do amerykanskiego formatu
date_pattern = re.compile(r"""^(.*?) # cały tekst przed datą
    ((0|1)?\d)-     #1-2 cyfry na miesiac
    ((0|1|2|3)?\d)-         # 1 -2 cyfry na dzień
    ((19|20)\d\d)           #4 cyfry na rok
    (.*?)$          #cały tekst po dacie
    """,re.VERBOSE)

#przeskakiwanie po plikach w working directory
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    #pomijanie plikow bez daty
    if mo == None:
        continue

#tworzenie czesci nazwy pliku
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

#tworzenie plikow w europejskim stylu
    euro_filename = before_part + day_part + '-' +month_part + '-' + year_part + after_part

    #pobranie calych sciezek plikow
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    #zmiana nazwy plikow
    print (f'Renaming "{amer_filename}" to "{euro_filename}"...')
    #shutil.move(amer_filename, euro_filename) #wywalic komentarz po testach
