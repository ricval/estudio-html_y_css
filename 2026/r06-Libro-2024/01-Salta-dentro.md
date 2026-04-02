# Capítulo 01 — Salta Dentro

## Escogiendo un conjunto de tecnologías

Este libro utiliza lo siguiente:

- **Bun** un entorno de ejecución, gestor de paquetes, empaquetador y ejecutor de pruebas de JavaScript
- **TypeScript** un super-conjunto de JavaScript que añade soporte para tipado.
- **Hono** una librería TypeScript para implementar un servidor HTTP

## Utilizando los atributos htmx

**Htmx** provee un nuevo set de atributos HTML que hacen a HTML más expresivo. La librería **htmx** procesa estos atributos. Algunos de ellos provocan un _HTTP request_ para enviar a los _endpoints_ los que regresan HTML que será insertado en el DOM.

Cualquier evento en cualquier elemento HTML puede disparar un _HTTP request_ de cualquier tipo (GET, POST, PUT, PATCH o DELETE) y la respuesta no resultara en un actualización completa de la página. Todo esto sin necesidad de escribir ningún código JavaScript del lado del cliente.

Actualmente, **htmx** define 36 atributos, pero un subconjunto menor de ellos es el más comúnmente utilizado.

_¿Qué eventos disparan un _request_?_
_¿Un clic del ratón, un envío de un formulario, u otros eventos?_
El atributo `hx-trigger` especifica los tipos de eventos que disparan un _request_.

_¿Qué tipo de _request_ debería ser enviado: GET, POST, PUT, PATCH o DELETE?_
_¿Y a dónde debería enviar el _request_?_
Los atributos `hx-get`, `hx-post`, `hx-put`, `hx-patch` y `hx-delete` describen ambos, el tipos de _request_ ha ser enviado y la URL a donde serán enviado.

_¿Cuándo un endpoint regresa un HTML, qué elemento debería recibirlo?_
El atributo `hx-target` indica el destino indicado del HTML regresado.

_¿Cómo debería el nuevo HTML ser colocado en elemento indicado?_
El atributo `htx-swap` detalla exactamente como el HTML regresado será colocado en el destino fijado. Las opciones se describen en el siguiente diagrama.

Asumiendo que `ht-target` referencia a un elemento `ul`.

```html
<p>antes del listado</p>
<ul>
    <li>Rojo</li>
    <li>Verde</li>
    <li>Azul</li>
</ul>
<p>después del listado</p>
```

Opciones para insertar el contenido:

- `beforebegin` - lo inserta antes del elemento `<ul>`
- `afterbegin` - lo inserta después del elemento `<ul>`
- `beforeend` - termina la inserción antes del elemento `</ul>`
- `afterend` - termina la inserción después del elemento `</ul>`

Opciones para remplazar el contenido:

- `outerHTML` - Remplaza todo el elemento `<ul>...</ul>`
- `innerHTML` - (Opción por defecto) Remplaza el interior de los elementos `<ul>...</ul>` es decir mantiene las etiquetas `<ul>...</ul>` y remplaza todos los elementos `<li></li>`

Opciones que no utilizan respuestas HTML

- `delete`
- `none`

## Creando Tu Primer Proyecto

>[!warning]
>El libro recomiendo utilizar **Bon**. Yo voy a utilizar **Python**.

Ejecuta el siguiente comando para inicializar el ejercicio:

Instalar `uv` si no lo tienes:
```bash
url -LsSf https://astral.sh/uv/install.sh | sh
```
Crea un nuevo proyecto:
```bash
# Inicia un nuevo proyecto
uv init
# Añade las dependencias necesarios
uv add fastapi uvicorn
# Para ejecutar el proyecto y poder ejecutar cambios en vivo
uv run main.py
```

Los servidores para aplicaciones **htmx** juegan dos roles. Primero, sirven archivos estáticos como HTML, CSS, JavaScript e imágenes. Segundo, ellos responden a ciertos _HTTP requests_, típicamente regresando un HTML o texto.

Revisa el código de tu primer ejemplo hecho con _Python - FastAPI_, está en el directorio: `01-Ejercicios/main.py`

```bash
# Instala las dependencias del proyecto
uv sync
# Ejecuta el proyecto
uv run main.py
```

## Creando un aplicación CRUD

