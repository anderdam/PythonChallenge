from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()  # rip it out

# Get comments in the source code
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    try:
        with open("mess.txt", 'a') as f:
            f.write(c)
    except:
        pass
    c.extract()
# print("Arquivo criado com sucesso!")

# Buscar o texto de um site e salvá-lo em um arquivo txt
