#! python3
# otwieranie kilku wyszukiwan w przegladarce

import requests, sys, webbrowser, bs4

print('Searching .... ')        # wyswietlanie tekstu podczas pobierania danych ze stron
res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()


#TODO Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#TODO open a browser tabfor each result
linkElems = soup.select('.package-snippet')
num_open=min(5,len(linkElems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)
    

