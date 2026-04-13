import os
import json

import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Opcional: Esto sirve todo lo que esté en /public (CSS, JS, imágenes) 
# para que el HTML pueda cargarlos.
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/", response_class=FileResponse)
def read_root():
    # Buscamos el archivo dentro de la carpeta 'public'
    return FileResponse("public/02/index2.html")


@app.get("/event-with-no-data", response_class=PlainTextResponse)
async def event_with_no_data(response: Response):
    """event_with_no_data"""
    # Añadimos el encabezado de Htmx
    response.headers["HX-Trigger"] = "event1"
    
    # Retornamos el texto plano
    return "dispatched event1"


@app.get("/event-with-string", response_class=PlainTextResponse)
async def event_with_string(response: Response):
    """event_with_string"""
    # Definimos el trigger como un diccionario de Python
    trigger = {"event2": "some string"}
    
    # Convertimos el diccionario a una cadena JSON
    response.headers["HX-Trigger"] = json.dumps(trigger)
    
    return "dispatched event2"


@app.get("/event-with-object", response_class=PlainTextResponse)
async def event_with_object(response: Response):
    """event_with_object"""

    # Definimos el objeto complejo (diccionario anidado)
    trigger = {
        "event3": {
            "foo": 1, 
            "bar": 2
        }
    }
    
    # Inyectamos el JSON en la cabecera
    response.headers["HX-Trigger"] = json.dumps(trigger)
    
    return "dispatched event3"


# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
