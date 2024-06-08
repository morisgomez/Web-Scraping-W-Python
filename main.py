#STEP 1: Install Python extension on VS.
#STEP 2: Install Python interpretar from Python website.
#STEP 3: All Python projects should have 'pip' installed 
    #because it allows for the managing of any new packages 
    #installed on project. Pip already comes w/ VS Python extension.
#STEP 4: install 'requests' library package on terminal in VS Code.
    #run 'pip install requests' in local terminal on VS Code.
    #'requests' allows us to make GET, POST etc requests online.
#STEP 5: install 'BeautifulSoup4' library package on terminal in VS Code.
    #run 'pip install beautifulsoup4' in local terminal on VS Code.
    #'BeautifulSoup4' allows us parse data for easy-reading.

#------SETTING UP PYTHON ENVIRONMENT FOR WEB SCRAPING------#

import requests #this library gives ability to make requests for data.
from bs4 import BeautifulSoup #this package gives ability to parse requested HTML data.
  
#Making a GET request.
r = requests.get('https://www.skysports.com/football/teams/argentina/squad') 

#check status code for response received.
#200 means a successful response received.
#401 means need extra permissions.
print(r) #<Response [200]>,

#------ACTUAL WEB SCRAPING AND PUSHING DATA COLLECTED INTO ARRAY------#

#Parsing the HTML.
htmlContent = BeautifulSoup(r.content, 'html.parser') #the content is parsed as html and stored in variable.

#print(htmlContent) #html elements printed jumbled together w/o new lines.
#print("BREAK").
#print(htmlContent.prettify) #prints each html element in new line.
#print("BREAK").
#print(htmlContent.get_text()) #prints each html element w/o tags in new line.
#result = htmlContent.find_all("h6") #stores every <h6> in an array/list w/ indexes.
#result = [<h6>sergio romero</h6>, <h6> martinez emilio</h6>].

s = [] #empty array to push the text in every <h6> element.

#loop 1 and 2 for finding all h6 tags and extracting the text from each:
for tag in htmlContent.find_all("h6"): #outer loop.
   #htmlContent.find_all("h6") creates an array w/ all <h6> elements.
   for txt in tag.stripped_strings: #nested loop.
      #stripped_string is a function which extracts the text only from elements.
      #txt holds stripped string.
      s.append(txt) #append string in txt to empty array.

#loop 3 to print strings in array s:
for x in s:
   print('#', x)

# Output via Terminal:
# Walter Benítez
# Nahuel Guzmán
# Sergio Romero
# Franco Armani
# Willy Caballero
# Agustín Marchesín
# Guido Herrera
# Gerónimo Rulli
# Esteban Andrada
# Emiliano Martinez
# Juan Musso
# Paulo Gazzaniga
# Lucas Martínez Quarta
# Nicolás Otamendi
# Cristian Ansaldi
# Fabricio Bustos
# Leonardo Balerdi
# Nahuel Molina
# Gabriel Mercado
# Leandro Paredes
# Germán Pezzella
# Cristian Romero
# Ramiro Funes Mori
# Milton Casco
# Lisandro Martínez
# Jorge Figal
# Marcos Rojo
# Federico Fazio
# Walter Kannemann
# Renzo Saravia
# Facundo Medina
# Gonzalo Montiel
# Nehuén Pérez
# Marcos Senesi
# Nicolás Tagliafico
# Nicolás Valentini
# Valentín Barco
# Alan Franco
# Emanuel Mammana
# Juan Foyth
# Leonel Di Plácido
# Lucas Biglia
# Ángel di María
# Marcos Acuña
# Thiago Almada
# Joaquín Correa
# Iván Marcone
# Nicolás Domínguez
# Javier Mascherano
# Enzo Fernández
# Guido Pizarro
# Manuel Lanzini
# Enzo Pérez
# Santiago Ascacibar
# Rodrigo Battaglia
# Alejandro Gomez
# Matías Zaracho
# Éver Banega
# Giovani Lo Celso
# Erik Lamela
# Valentín Carboni
# Franco Cervi
# Domingo Blanco
# Franco Vázquez
# Matías Vargas
# Facundo Buonanotte
# Maximiliano Meza
# Gastón Giménez
# Gonzalo Martinez
# Alexis Mac Allister
# Alejandro Garnacho Ferreyra
# Guido Rodríguez
# Exequiel Palacios
# Roberto Pereyra
# Lucas Ocampos
# Dario Benedetto
# Mauro Icardi
# Gonzalo Higuaín
# Julián Álvarez
# Lionel Messi
# Ángel Correa
# Lucas Alario
# Giovanni Simeone
# Sergio Agüero
# Paulo Dybala
# Eduardo Salvio
# Cristian Pavón
# Matias Suarez
# Adolfo Gaich
# Lautaro Martínez
# Nicolás González
# Rodrigo De Paul
