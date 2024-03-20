import sys
sys.stdout.reconfigure(encoding ='utf-8')

from get_module import request_get
from string import Template

url = "https://aves.ninjas.cl/api/birds"
response = request_get(url)

lista_img = [(elemento["images"]["main"], elemento["name"]['spanish'], elemento["name"]['english']) for elemento in response]

nuevo_card =  """<div class="card" style="width: 18rem;">
                <img src="$url" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">$name </h5>
                    <h5 class="card-title">$english</h5>
                 </div>
                </div>
    """
img_template = Template(nuevo_card)
texto_img = ''
# imagen = img_template.substitute(url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/kowo9E1e1JcWLXj9cCvAOFZcy5n.jpg')
for img, name, english in lista_img:
    texto_img += img_template.substitute(url = img, name = name, english = english) + '\n'

    html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1 class="text-center">Aves de Chile</h1>
    <div class="container-fluid py-3">
        <div class="row g-3 row-cols-4">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body = texto_img)

archivo = open('index.html', 'w+', encoding='utf-8') 
archivo.write(html)
archivo.close()
