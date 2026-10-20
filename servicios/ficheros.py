import json
from pathlib import Path

fichero = Path("datos.json")

def guardar_datos(datos):
    with open(datos, "w"):
        json.dump(datos,fichero)

def cargar_datos():
    if not fichero.exists():
        return []

    with fichero.open(encoding="utf-8") as biblioteca:
        return json.load(biblioteca)
