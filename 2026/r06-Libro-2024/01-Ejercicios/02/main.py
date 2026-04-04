import os
import uuid

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Declaración del tipo de dato Perro
class Perro(BaseModel):
    """ Clase Perro """
    id: str
    nombre: str
    raza: str

# Declaración de la variable con tipado
perros: dict[str, Perro] = {}

def add_perro(nombre: str, raza: str) -> Perro:
    """ Función para añadir un perro al diccionario de perros """
    id = str(uuid.uuid4())  # Creamos un id UUID aleatorio
    perro = Perro(id=id, nombre=nombre, raza=raza)
    perros[id] = perro
    return perro

# Añade dos perros de ejemplo
add_perro('Cometa', 'Puddle')
add_perro('Oscar', 'Pastor Alemán')

# Función para regresar un Renglón de Perro en HTML
def dog_row(perro: Perro):
    """Función que regresa un Perro como reglón HTML"""

    html_content = f"""
    <tr class="on-hover">
        <td>{perro.nombre}</td>
        <td>{perro.raza}</td>
        <td class="buttons">
            <button 
                class="show-on-hover" 
                hx-delete="/dog/{perro.id}" 
                hx-confirm="¿Estás seguro de que quieres eliminar a {perro.nombre}?" 
                hx-target="closest tr" 
                hx-swap="delete">
                X
            </button>
        </td>
    </tr>
    """
    # Entregamos el html
    return html_content

# Opcional: Esto sirve todo lo que esté en /public (CSS, JS, imágenes) 
# para que el HTML pueda cargarlos.
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/", response_class=FileResponse)
def read_root():
    # Buscamos el archivo dentro de la carpeta 'public'
    return FileResponse("public/02/index.html")


@app.get("/table-rows", response_class=HTMLResponse)
def entrega_rows():
    # 1. Generamos el HTML para cada perro en el diccionario
    # Usamos .values() para obtener los objetos Perro
    html_segments = [dog_row(perro) for perro in perros.values()]
    
    # 2. Unimos todos los segmentos en un solo string
    # Nota: Si dog_row devuelve HTMLResponse, usamos .body.decode() 
    # Si dog_row devuelve solo string, usamos el objeto directamente
    full_html = "".join([
        (r.body.decode() if isinstance(r, HTMLResponse) else r) 
        for r in html_segments
    ])
    
    # 3. Retornamos el bloque completo como HTML
    return full_html


@app.post("/dog", response_class=HTMLResponse, status_code=201)
async def recibe_perro_nuevo(name: str = Form(""), breed: str = Form("")):
    # Recibe el perro del formulario y lo crea para insertarlo en el diccionario de perros
    perro = add_perro(name, breed)
    # Entrega el perro creado como renglón de tabla html
    return dog_row(perro)


@app.delete("/dog/{id}")
def borrar_perro(id: str):
    perros.pop(id)


# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
