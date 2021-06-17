#from googlesearch import search
import ssl
#import requests
from bs4 import BeautifulSoup
import urllib.request
from itertools import permutations

ssl._create_default_https_context = ssl._create_unverified_context

alphabets = ['y', 'p', 'i', 'x', 'h', 'a', 'm', 'm', 'e', 'k', 'r', 'r']

w_list = ['h', 'l', 'l', 'e']

def word_search(word):
    #word = "xtek"
    url = "https://www.vocabulary.com/dictionary/" + word + ""
    print(url)

    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')

    soup1 = soup.find(class_="short")

    try:
        soup1 = soup1.get_text()
        print(soup1)
    except AttributeError:
        print('Cannot find such word! Check spelling.')
        #exit()

"""
for (a,b,c,d,e,f,g) in combinations_with_replacement(alphabets, 7):
    word = a+b+c+d+e+f+g
    word_search(word)
"""


perm = set(permutations(w_list, 4))

# Print the obtained permutations
for i,j,k,l in perm:
    word = i+j+k+l
    word_search(word)
    #print(word)