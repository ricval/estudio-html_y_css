import os
import asyncio
import httpx

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Carpeta donde guardarás tus archivos .html
templates = Jinja2Templates(directory="02-lazy-loading/templates")

# Declaración de un objeto con pydantic
class Company(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str
    email: str
    company: Company

URL = "https://jsonplaceholder.typicode.com/users"

# Opcional: Esto sirve todo lo que esté en /public (CSS, JS, imágenes) 
# para que el HTML pueda cargarlos.
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/", response_class=FileResponse)
def read_root():
    # Buscamos el archivo dentro de la carpeta 'public'
    return FileResponse("public/02/lazy-loading.html")


@app.get("/users", response_class=HTMLResponse)
async def get_user(request: Request):
    """get user"""
    await asyncio.sleep(1)

    # 2. Hacemos la petición (Equivalente a fetch)
    async with httpx.AsyncClient() as client:
        res = await client.get(URL)
        # 3. Parseamos el JSON (Equivalente a res.json())
        users = res.json()

    return templates.TemplateResponse("lazy-loading.html", {"request": request, "users": users})

# Aquí colocas el bloque principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
