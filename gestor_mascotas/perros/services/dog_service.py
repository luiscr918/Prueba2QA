import requests
from ..models import Raza

API_URL = "https://dogapi.dog/api/v2/breeds"

def load_breeds():
    if Raza.objects.exists():
        return "Ya existen datos."
    
    response = requests.get(API_URL)
    data = response.json()
    
    breeds_list = data.get('data', [])
    
    for item in breeds_list:
        attr = item['attributes']
        Raza.objects.create(
            nombre=attr['name'],
            descripcion=attr['description'],
            vida_min=attr['life']['min'],
            vida_max=attr['life']['max'],
            hipoalergenico=attr['hypoallergenic']
        )
    return f"Se cargaron {len(breeds_list)} razas."