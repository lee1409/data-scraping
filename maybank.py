import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re

# Setup GET request from maybank pointstreat
def get_page(url):
    request = requests.get(url)
    text = request.text
    return BeautifulSoup(text, 'html.parser')

def get_image(bsObj):
    url_list = []
    for child in bsObj.find('div', {'class': 'span10 midlle_content'}).children:
        src = child.find('img')
        if src != -1:
            url_list.append(src)
    return url_list

def get_id(bsObj):
    content =  bsObj.find_all('a', {'class': 'inline'})
    return [ name.attrs['href'] for name in content ]

def get_name(bsObj):
    content = bsObj.find('div', {'class': 'span10 midlle_content'})
    return content.find_all(string=lambda text:isinstance(text, Comment))

def get_content(bsObj, ID):
    '''
        ID is the list
        return list
    '''
    content_list =[]
    for x in ID:
        print(x)
        content = bsObj.find('div', {'id': x[1:], 'class': 'framestyle'})
        #inner_list = [ child.find('ul').getText() for child in content if child.find('ul') != -1 and child.find('ul') != None ]
        #content_list.append(inner_list)
        for child in content:
            desc = child.find('ul')
            if desc != -1 and desc != None:
                content_list.append(desc.getText())
    return [ s.strip() for s in content_list ]

if __name__ == '__main__':
    url = 'http://www.maybank2u.com.my/WebBank/my-dining.html'
    soup = get_page(url)
    print(get_content(soup, get_id(soup)))
