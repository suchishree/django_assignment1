import requests
from bs4 import BeautifulSoup
html_string = '''<html>
     <head></head>
     <body>
     <h1>welcome to html</h1>
     <h1>welcome to web scraping</h1>
     <h1>welcome to both</h1>
     </body>
</html>'''
bs = BeautifulSoup(html_string,"html.parser")
result = bs.find("h1").text
print(result)
