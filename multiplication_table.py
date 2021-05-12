#! python3
# program do tworzenia tabliczki NxN

import openpyxl, sys

from openpyxl.styles import Font

if len(sys.argv) == 2:
    try: 
        numer = int(sys.argv[1])
    except Exception as error:
        print(error)
    
    wb=openpyxl.Workbook()
    sheet = wb.active
    for y in range(numer+1):
        for x in range(numer+1):
            #sprawdzenie w ktorej kolumnie jest
            naglowki = False

            if x == 0 and y ==0 :
                naglowki = True
                n = ''
            elif x == 0:
                naglowki = True
                n = y
            elif y == 0:
                naglowki = True
                n = x
            else: 
                n = x * y
            c = sheet.cell(row = y + 1, column = x + 1)
            if naglowki:
                czcionka = Font(bold = True)
                c.font = czcionka
            c.value = n
    f = 'multiplication_table_' + str(numer) + '.xlsx'
    wb.save(f)
    print('Program zapisany jako ' + f )

else:
    print('Prosze wpisac liczbe.')


