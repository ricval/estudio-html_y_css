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

Esta aplicación puede mantener una colección de cualquier data ordenado. Hagamos una lista para perros. La información la mantendremos en memoria.

Ejemplo 02: [index.html](01-Ejercicios/public/02/index.html)

¿Cuál es el propósito de los atributos `hx-` en el elemento `form`?

El atributo `hx-post` especifica que el _request_ será por _POST_ al _endpoint_ `/dog` cuando el formulario sea enviado. El _body_ del _request_ contendrá la información del formulario como el nombre y la raza. Y como veremos, la respuesta contendrá un nuevo renglón para la tabla.

El atributo `hx-disabled-elt` desactiva el botón Añadir mientras cualquier _request_ asociado al formulario está siendo procesado. `elt` es la abreviación para elemento. Esto previene envío duplicados o dobles.

El atributo `hx-target` especifica que el HTML regresado deberá remplazar el elemento `tbody` que está dentro del elemento `table`.

El atributo `hx-swatp` especifica que el renglón de la tabla regresado deberá ser insertado después del comienzo de lo indicado. Debido a que el elemento `tbody` es el objetivo, el nuevo renglón de la tabla será insertado antes de todos los renglones existentes.

El atributo `hx-on` especifica que después de que el _request_ _POST_ es procesado, el `form` deberá ser reiniciado. Esto limpia los valores de nombre y raza de los _inputs_. Como versión simplificada `htmx` puede ser removido del atributo, dejándolo en: `hx-on::after-request`.

¿Cuáles son los propósitos de los elementos `hx-` en el elemento `table`?

El atributo `hx-trigger` especifica el evento que lanzará un _HTTP request_. En este caso, se disparará cuando la tabla aparece en pantalla. Para esta app, eso pasa inmediatamente, ya que no hay mucho contenido sobre la tabla. Pero si hubiera más contenido sobre la tabla el usuario necesitaría desplazarse hacia abajo para verla, htmx esperaría hasta que la tabla fuera "_revealed_" "revelada" para enviar el _request_.

El atributo `hx-get` especifica que el _request_ será un _GET_ que deberá enviar a `/table-rows`. Como veremos, la respuesta será el contenido de un renglón de la tabla por cada perro que haya sido ingresado previamente.

El atributo `hx-target` especifica los renglones que serán regresados y remplazaran el contenido del elemento `tbody`.