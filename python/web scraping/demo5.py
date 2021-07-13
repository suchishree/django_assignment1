import requests
from bs4 import BeautifulSoup
html_string = '''<html>
     <head>
          <style>.my_bg_color{
               background-color: yellow;
               color: mediumvioletred;
          }
          .one{
               background-color: aqua;
               color: yellow;
          }
          </style>
     </head>
     <body>
     <h1 class="my_bg_color">welcome to html</h1>
     <h1 class="one">welcome to web scraping</h1>
     <h1 class="my_bg_color">welcome to both</h1>
     </body>
</html>
'''
bs = BeautifulSoup(html_string,"html.parser")
result = bs.find("h1",{"class":"one"}).text
print(result)
