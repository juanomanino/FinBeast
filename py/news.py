import  bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#conexion
url_google_news = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREZzY3pJU0JtVnpMVFF4T1NnQVAB?hl=es-419&gl=CO&ceid=CO%3Aes-419'
cliente= urlopen(url_google_news)
contenido_xml= cliente.read()
cliente.close()

#Lectura en formato xml

pagina= soup(contenido_xml, 'html.parser')
items= pagina.findAll('item')

#Iterar noticias

for item in items:
    print(item.title.text)
    print(item.link.text)
    print(item.pubDate.text)
    print('=' *70)


