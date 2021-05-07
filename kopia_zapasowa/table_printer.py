
#Program do wyswietlania listy w kolumnach, z uwzglednieniem rjustify zaleznym od najdluzszego slowa w stringu


tableData = [['apples', 'oranges', 'cherries', 'banana'],           #tablica zmiennych string
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]



print(tableData)
max_len = []
new_string = " "


def search_for_longest_word(tablica):                                 #tworzenie funkcji szukajacej najduzszego slowa w liscie 
    for wordlist in tablica:
        new_string = max(wordlist, key=len)
        max_len.append(len(new_string))                                   #zapisanie liczby najwiekszej ilosci znakow w liscie
        print(max_len[-1])
    return max_len



def print_table(tablica, max_len):                                      #funkcja wyswietlajaca tablice                                      

    for i in range(len(tablica[0])):
        print()
        for j in range(len(tablica)):
            print(tablica[j][i].rjust(max_len[j]), end=' ')


print_table(tableData, search_for_longest_word(tableData))

