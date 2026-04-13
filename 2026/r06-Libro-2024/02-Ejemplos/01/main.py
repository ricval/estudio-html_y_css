import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Opcional: Esto sirve todo lo que esté en /public (CSS, JS, imágenes) 
# para que el HTML pueda cargarlos.
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/", response_class=FileResponse)
def read_root():
    # Buscamos el archivo dentro de la carpeta 'public'
    return FileResponse("public/01/out-of-band.html")

@app.get("/demo", response_class=HTMLResponse)
def demo():
    """Demo"""

    html_content = """
        <div>new 1</div>
        <div id="target2" hx-swap-oob="true">
            new 2
        </div>
        <div id="target2" hx-swap-oob="afterend">
            <div>after 2</div>
        </div>
        <div hx-swap-oob="innerHTML:#target3">new 3</div>
    """
    # Entregamos el html
    return html_content


# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
