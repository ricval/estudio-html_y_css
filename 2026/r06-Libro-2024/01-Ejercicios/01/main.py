import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Opcional: Esto sirve todo lo que esté en /public (CSS, JS, imágenes) 
# para que el HTML pueda cargarlos.
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/", response_class=FileResponse)
def read_root():
    # Buscamos el archivo dentro de la carpeta 'public'
    return FileResponse("public/01/index.html")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get('/version', response_class=PlainTextResponse)
def version():
    # Si solo quieres el número (ej: "3.12.1")
    v = sys.version_info
    return f"v{v.major}.{v.minor}.{v.micro}"

# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
