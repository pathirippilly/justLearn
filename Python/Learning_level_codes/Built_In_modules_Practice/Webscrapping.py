from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
import requests
import shutil # to save it locally
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="@zkaban92")
        controller.signal(Signal.NEWNYM)

# Make a request through the Tor connection
# IP visible through Tor
renew_connection()
session = get_tor_session()
rq=session.get("https://unsplash.com/s/photos/night")
#soup=BeautifulSoup(rq.text,'html.parser')
with open(r'A:\sample.html', 'w+',encoding="utf-8") as f:
    f.write(rq.text)

#rq.raw.decode_content = True
#with open(r'A:\sample_image.jpg', 'wb') as f:
    #shutil.copyfileobj(rq.raw, f)
# Above should print an IP different than your public IP

# Following prints your normal public IP
#print(requests.get("http://httpbin.org/ip").text)

# signal TOR for a new connection

#renew_connection()
#session = get_tor_session()
#print(session.get("http://httpbin.org/ip").text)

#soup=BeautifulSoup(rq.text,'lxml')
    #with open(r"A:\mygit\projects\Python3\Data\example.html") as f:
        #soup=BeautifulSoup(f,'lxml')
#print(soup.prettify()) # this will print the formatted html read from file

#with open(r"A:\output\sample.txt","w+") as f :
   # f.write(soup.text)

 # gives text of the title
#print(soup.text) # gives all text elements of the file
#print(soup.div) #gives the first division of the file
#soup.find("div",class_="footer")) #gives the  division with specific class=footer
#article=soup.find("div",class_="article")
#print(article.h2.a.text) #accessing header text of the article
