from django.http import HttpResponse

def show(response):
    message =''' <html>
                 <head>
                 </head>
                 <body>
                 <h1>This is anchor tag</h1>
                 <a href="https://www.w3schools.com/tags/tag_a.asp">visit w3schools</a>
                 </body>
                 </html>
                 <html>
                 <body>
                 <p>call to a number</p>
                 <a href="tel:760602707">bou</a>
                 </body>
                 </html>
              '''
    return HttpResponse(message) 
