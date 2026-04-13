# Capítulo 03 — Desarrollando _Endpoints_

Para implementar una aplicación web utilizando htmx requiere definir varios _endpoint_ HTTP. Cada _endpoint_ utiliza un verbo HTTP especifico, que aplica un patrón URL, y opcionalmente acepta datos en diferentes formas. Te mostraremos buenas practicas para implementar un buen diseño de _endpoints_.

Una respuesta desde un _endpoint_ htmx puede hacer cualquiera de las siguientes cosas:

1. Regresar un HTML para remplazar en una localización especifica por el atributo `hx-target`.
2. Regresar un HTML para remplazar en otra localización utilizando intercambiadores fuera-de-banda.
3. Lanzar un evento en el navegador con o sin datos asociados.
4. No regresar nada.

Lanzar un evento es útil para informar al cliente que algo interesante está ocurriendo en el servidor. El cliente puede escuchar el evento y tomar acción.

No regresar nada puede ser útil para _endpoints_ que solo necesitan hacer una acción como actualizar algo en la base de datos. En algunos casos, la interfaz de usuario no requiere ninguna actualización.

>[!info]
>El atributo `hx-select` especifica un selector CSS que identifica el elemento HTML que va incluir. Por ejemplo, suponga que la respuesta incluye los elementos HTML que describen unos platillos de comida y nosotros solo queremos actualizar los postres. Podríamos modificar el _endpoint_ para habilitar la respuesta solo a estos. Pero una alternativa sería utilizar `hx-select=".desert"`.
>
>El atributo `hx-select-oob` es similar, pero solo aplica a los intercambios fuera-de-banda.

## HTTP Request

Especifica un verbo (como _GET_ o _POST_), un URL objetivo, y opcionalmente incluir un data o información. La URL está compuesta de un protocolo (como lo es https), un dominio (como pjecz.gob.mx) y una ruta (como /perro/raza).

La mayoría de los HTTP _endpoints_ realizan operaciones CRUD, y el verbo utilizado en los _request_ sirven como un indicador de esto. Piensa en la información del servidor como un recurso y cada verbo HTTP como una acción a realizar en un recurso. Por ejemplo, cada descripción de un perro en la base-de-datos como un recurso.

La siguiente tabla describe el uso típico de los verbos HTTP:

  Verbo | Acción
--------+-------
POST    | Crea un recurso.
GET     | Lee/regresa un recurso.
PUT     | Remplaza un recurso (actualiza todas sus propiedades).
PATCH   | Actualiza un recurso (solo un sub-conjunto de sus propiedades).
DELETE  | Borra un recurso.
--------+-------

_Endpoints_ que no realizan operaciones CRUD son típicamente invocadas con el verbo POST.

Muchas operaciones para dar data/información en un _request_ HTTP están disponibles, resumidas en la siguiente tabla:

Localización de la Data | Uso Típico | Ejemplo
------------------------+-----------------------------------+----------------------------------
request headers         | autentificación y autorización    | Authorization: {algún-token}
request headers         | negociación de contenido          | Accept: application/json
path parameters         | especificando un recurso          | /perros/{algún-id}
query parameters        | filtrado, ordenación y paginación | /perros?raza=puddle&acendente=false&page=2
request body            | creando o actualizando un recurso | {"nombre": "Cometa", "raza": "Puddle"}
------------------------+-----------------------------------+----------------------------------

En el primer capítulo, creamos una aplicación CRUD que implementaba los siguientes _endpoints_:

- GET /perro — Ninguna información/data es pasado a este _endpoint_.
- POST /dog — El _request body_ contiene la información para crear un nuevo perro.
- DELETE /dog/:id — La URL contiene el _query parameter_ que especifica el id del perro a borrar.

Se pudieron agregar los siguientes _endpoints_:

- GET /perro/:id — La URL contiene un parámetro-de-ruta que especifica el id de un solo perro a entregar.
- PUT /perro/:id — La URL contiene un parámetro-de-ruta que especifica el id del perro a actualizar. El _request body_ contiene la información/data para actualizar todas sus propiedades de un perro existente.
- PATCH /perro/:id — La URL contiene un parámetro-de-ruta que especifica el id del perro a actualizar. El _request body_ contiene la información/data para actualizar cierta información o propiedades de un perro existente.

## HTTP Responses

Las respuestas desde un _endpoint_ HTTP puede regresar información/data en el encabezado y en e cuerpo.

El encabezado `Content-Type` especifica el formato de la información en el cuerpo. La siguiente tabla describe los valores comunes en el encabezado, pero hay muchos más posibles.

Formato | Valor `Content-Type`
--------+---------------------
texto   | text/plain
JSON    | application/json
HTML    | text/html
image   | image/jpeg, image/png, etc.
--------+---------------------

## Endpoints Targets

Es común para _endpoints_ htmx regresar un solo elemento HTML. El único elemento puede tener muchos elementos hijo, pero sigue siendo un solo elemento.

Como ya vimos, al regresar un elemento este remplazará en el DOM la localización especificada por el atributo `hx-target`. Exactamente como lo indicamos en el atributo `hx-swap`.

Algunas veces podría ser deseable actualizar múltiples partes de la página actual. Se puede hacer de tres maneras: Ampliando-el-alcance, utilizando intercambios fuera-de-banda o disparando un evento. Examinemos las tres opciones.

### Ampliando-el-alcance

Una opción es actualizar un elemento más grande que incluya todas las partes involucradas. Usualmente no es la mejor opción, porque requiere un regreso de HTML más grande y complejo de lo realmente necesario, que podría incluir elementos que no quieres remplazar. No es muy optimo.

### Intercambios Fuera-de-banda

La mayoría de las veces el HTML regresado por el _endpoint_ remplaza el DOM en una localización especificada por el atributo `hx-swap`. Pero a veces quieres remplazar varias localizaciones.

Los fragmento HTML por ser insertados en la localización indicada por `hx-target` pueden ser considerados intercambios dentro-de-banda. Todos los demás deberían utilizar intercambios fuera-de-banda incluyendo el atributo `hx-swap-oob` (`oob` viene del inglés _out-of-band_).

La siguiente tabla describe los posibles valores del atributo `hx-swap-oob`:

Valor                           | Significado
--------------------------------+---------------
`true`                          | Remplaza el elemento que coincida con el atributo id con ese elemento (igual que `outerHTML`).
un valor válido de `hx-swap`    | Coloca este elemento relativo a el elemento existente con el atributo id que coincide.
un valor válido de `hx-swap` seguido de un selector CSS | Coloca este elemento relativo al elemento que coincide con el selector CSS.
--------------------------------+---------------

```html
<div class="todo-item">
    <input type="checkbox" hx-patch="/todos/82/toggle-complete" />
    <div>buy highlighters</div>
    <input
        name="description"
        type="text"
        value="buy highlighters"
        hx-patch="/todos/82/description" />
    <button hx-delete="/todos/82">Delete</button>
</div>
<p id="status" hx-swap-oob="true">2 of 3 remaining</p>
```

```html
<html>
    <head>
        <title>Out-of-Band Demo</title>
        <script src="https://unpkg.com/htmx.org@2.0.0"></script>
    </head>
    <body>
        <button hx-get="/demo" hx-target="#target1">Send</button>
        <div id="target1">original 1</div>
        <div id="target2">original 2</div>
        <div id="target3">original 3</div>
    </body>
</html>
```

```html
<div>new 1</div>
<div id="target2" hx-swap-oob="true">new 2</div>
<div id="target2" hx-swap-oob="afterend">
    <div>after 2</div>
</div>
<div hx-swap-oob="innerHTML:#target3">new 3</div>
```

Explicando el ejemplo anterior:

La página por defecto muestra un botón "Send" con tres items:

```text
[Send]
original 1
original 2
original 3
````

Al presionar el botón [Send] cambia a:

```text
[Send]
new 1
new 2
after 2
new 3
```

El texto 'new 1' es reemplazado por 'original 1' porque el `div` regresado que lo contiene no incluye el atributo `hx-swap-oob` y el botón que lanza el evento _endpoint_ tiene como objetivo con el atributo `hx-target` el '#target1'.

El texto 'new 2' es reemplazado por 'original 2' porque el `div` regresado que lo contiene el atributo `hx-swap-oob` en `true` y el tributo `id` en 'target2'.

El texto 'after 2' es insertado después del elemento con el `id` "target2" porque el `div` regresado contiene un atributo `hx-swap-oob` con el valor "afterend" y el atributo `id` con "target2".

El texto "new 3" es reemplazado por "original 3" porque el `div` regresado que lo contiene tiene el atributo `hx-swap-oob` con el valor "innerHTML:#target3".

### Eventos disparadores

Un _endpoint_ puede establecer el encabezado de respuesta `HX-Trigger` para que el evento que lo dispare en el navegador cuando la respuesta es recibida. El valor del encabezado puede ser el nombre del evento o un objeto JSON que contenga como llave el nombre del evento y un valor arbitrario. Si un valor es dado, el cliente puede encontrarlo en `event.datail.value`.

## Poniéndolo en práctica

