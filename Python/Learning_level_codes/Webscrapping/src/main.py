from bs4 import BeautifulSoup
import os
dataPath='A:\JustLearn\git_justLearn\Python\Learning_level_codes\Webscrapping\data\dummyWeb.html'
with open(dataPath,'r') as htmlFile:
    content = htmlFile.read()
    soup=BeautifulSoup(content,'lxml')
print(soup.prettify())