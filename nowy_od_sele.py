from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
#region Stary program
try: 
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name.')
#endregion

linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()