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

selected_id = '' # Mantiene el id del perro seleccionado actual

# Función para regresar un Renglón de Perro en HTML
def dog_row(perro: Perro, actualizar: bool = False):
    """
    Si el perro es actualizado, queremos ejecutar un swap fuera-de-banda
    así el renglón de la tabla podrá ser remplazado por el existente.
    """
    atributos: dict[str, str] = {}

    if actualizar:
        atributos['hx-swap-oob'] = 'true'

    html_content = f"""
    <tr class="on-hover" id="row-{perro.id}" {atributos}>
        <td>{perro.nombre}</td>
        <td>{perro.raza}</td>
        <td class="buttons">
            <button 
                class="show-on-hover" 
                hx-confirm="¿Estás seguro de que quieres eliminar a {perro.nombre}?" 
                hx-delete="/dog/{perro.id}" 
                hx-target="closest tr" 
                hx-swap="outerHTML"
                type="button"
            >
                🗑️
            </button
                class="show-on-hover"
                hx-put="/select/{perro.id}"
                hx-swap="none"
                type="button"
            >
                ✏️
            <button>
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
    return FileResponse("public/03/index3.html")


@app.get("/form", response_class=HTMLResponse)
def get_form():
    """get_form"""
    atributos: dict[str, str] = {
        "hx-on:htmx:after-request": "this.reset()"
    }

    if (selected_id):
        # Actualiza un renglón existente
        atributos['hx-put'] = f"/dog/{selected_id}"
    else:
        # Añade un nuevo renglón
        atributos["hx-post"] = "/dog"
        atributos["hx-target"] = "tbody"
        atributos["hx-swap"] = "afterbegin"
    
    perro_seleccionado = perros.get(selected_id)

    html_content = f"""
    <form hx-disabled-elt="#submit-btn" {atributos}>
        <div>
        <label for="name">Nombre</label>
        <input
            id="name"
            name="name"
            required
            size={30}
            type="text"
            value={perro_seleccionado.nombre}
        />
        </div>
        <div>
            <label for="breed">Raza</label>
            <input
                id="breed"
                name="breed"
                required
                size={30}
                type="text"
                value={perro_seleccionado.raza}
            />
        </div>
        <div class="buttons">
            <button id="submit-btn">{'Actualizar' if selected_id else 'Añadir'}</button>
            {"""
            <button hx-put="/deselect" hx-swap="none" type="button">
                Cancel
            </button>
            """ if selected_id else ""}
        </div>
    </form>
    """

    # Entrega del html
    return html_content


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


@app.put("/select/{id}", response_class=HTMLResponse)
async def reemplazar_perro(response: Response):
    """reemplazar_perro"""
    selected_id = id
    # Añadimos el encabezado de Htmx
    response.headers["HX-Trigger"] = "selection-change"
    
    # Retornamos el texto plano
    return None


@app.put("/dog/{id}", response_class=HTMLResponse)
async def actualizar_perro(response: Response, name: str = Form(""), breed: str = Form("")):
    """actualizar_perro"""
    perro_actualizado = Perro(id=id, nombre=name, raza=breed)
    perros[id] = perro_actualizado

    selected_id = ''
    response.headers["HX-Trigger"] = "selection-change"
    return dog_row(perro_actualizado, true)


@app.put("/deselect", response_class=HTMLResponse)
async def deseleccionar(response: Response):
    """reemplazar_perro"""
    selected_id = ''
    response.headers["HX-Trigger"] = "selection-change"
    return None


@app.delete("/dog/{id}")
def borrar_perro(id: str):
    perros.pop(id)
    return None


# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
