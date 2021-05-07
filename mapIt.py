#! python3
#mapit.py program który odpala mape w przegladarce uzywajac
# adresu z command line albo schowka (Ctrl+c)

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # pobieranie adresu z command line
    address = ''.join(sys.argv[1:])
else:
    # pobieranie adresu ze schowka
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
