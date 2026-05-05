# Capítulo 04 — Recetas para escenarios comunes

## Potenciando

Para apps web multi-página, puedes hacer una mejora de rendimiento al cargar las nuevas páginas añadiendo `hx-boost="true"` a los elementos que quieras cargar. Esto puede ser aplicado como una ancla a los elementos `a` y los elementos `form` y sus botones de envío. Solo funciona para páginas con el mismo dominio que la aplicación web.

Cuando los aplicamos a un elemento ancla, el historial es empujado y la URL en el navegador es actualizada. Esto habilita utilizar el botón de regreso del navegador que regresa la página anterior.

Aquí un ejemplo, que contiene dos elementos ancla, el primero no utiliza `hx-boost`, pero el segundo sí.

```html
<html>
    <head>
        <title>hx-boost Demo</title>
        <link rel="stylesheet" href="styles.css" />
        <script src="https://unpkg.com/htmx.org@2.0.0"></script>
    </head>
    <body>
        <a href="another.html">Without boost</a>
        <a href="another.html" hx-boost="true">With boost</a>
    </body>
</html>
```

Cuando la página es cargada, las etiquetas `link` y `script` son procesadas. El fondo se vuelve azul cielo, y la librería htmx es cargada.

El archivo `sytles.css` es cargado por el contenido de la página principal.

Aquí el archivo `another.html` es referenciado por ambas etiquetas ancla. Nota que el elemento `head` contiene los elementos `link` y `script`.

```html
<html>
    <head>
        <title>Another Page</title>
        <link rel="stylesheet" href="another.css" />
        <script src="another.js"></script>
    </head>
    <body>
        <h1>Another Page</h1>
    </body>
</html>
```

Cuando el enlace "_Without boost_" en la página principal es presionado, la página `another.html` es cargada en forma normal. Las etiquetas `link` y `style` son procesadas, así que el `alert` en `another.js` es desplegado, y el fondo cambia a rojo.

Cuando el link "_With boost_" es la página principal es presionado, la página `another.html` es cargada, pero las etiquetas `link` y `style` no son procesadas. El `alert` no es desplegado y el fondo sigue siendo azul cielo.

## Carga perezosa

Cuando desplegamos el contenido eso es caro de hacer, es útil para atrasar el pedido hasta que el resto de la página ha sido carga o hasta que la parte de la página será desplegada cunado se recorra dentro de la vista.

Para esperar para enviar una petición hasta que la página ha cargado, utiliza `hx-trigger="load"`. Para esperar hasta que los elementos estén dentro del área visible del navegador, utiliza `hx-trigger="revealed"`, por ejemplo:

```html
<table hx-get="/weather/forecast" hx-trigger="revealed"></table>
```

También utiliza el atributo `hx-indicator` para especificar un elemento para desplegar mientras la petición comienza a procesar. La propiedad CSS `opacity` del elemento comienza en 0, cambia a 1 cuando la petición es enviada, y regresa a 0 después de recibir la respuesta. Una buena opción para el elemento es un _spinner_ tipo GIF.

## Validación de _inputs_ con llamadas API

Algunas validaciones de entrada deben ser hechas en el servidor. Como por ejemplo, revisar si una dirección de correo ya existe en otro usuario. Esto puede ser hecho cuando el usuario está escribiendo en lugar de esperar a enviar el formulario.

El siguiente HTML valida un correo mientras se escribe. Una petición GET es enviada al _endpoint_ `/email-validate` cuando el evento `keyup`.

El modificador `changed` le indica la petición solo debería enviar si el valor entrante ha cambiado. Un ejemplo del evento `keyup` no ha cambiado su valor, es cuando se utilizan las flechas para mover el cursos dentro del campo de entrada.

El modificador `delay` le indica que debería esperar a enviar la petición por el tiempo especificado. Si otro evento `keyup` que cambia el valor es recibido antes de la cantidad de tiempo haya terminado, la espera vuelve a comenzar. Esto permite a los usuarios escribir continuamente sin disparar un evento cada vez que presiona una tecla.

El _endpoint_ `/email-validate` regresa un texto vacío si el correo no está en uso, o el mensaje "email en uso". El texto regresado es utilizado como el contenido del elemento `span` que sigue al elemento `input`.

```html
<label for="email">Email</label>
<input
    id="email"
    hx-get="/email-validate"
    hx-target="#email-error"
    hx-trigger="keyup changed delay:200ms"
    name="email"
    type="email"
>
<span class="error" id="email-error">
```

## Borrando un elemento

A veces el resulta de enviar una petición debe borrar un elemento. Por ejemplo, en una app tipo tareas, al presionar el botón borrar, envía una petición HTTP para que el servidor borre. Entonces el renglón debería ser borrado del DOM.

Al utilizar `hx-swap="delete"` y `hx-target="closes div"` en un el elemento `button`. El _endpoint_ `DELETE /todo/${id}` no necesita regresar nada HTML y el `div` que contiene el `button` será eliminado.

```html
<div class="todo-item">
    <input
        type="checkbox"
        checked={isCompleted}
        hx-patch={`/todos/${id}/toggle-complete`}
        hx-swap="outerHTML"
        hx-target="closest div"
    >
        <div class={isCompleted ? 'completed' : ''}>{description}</div>
        <button
        class="plain"
        hx-confirm={`Really delete "${description}"?`}
        hx-delete={`/todos/${id}`}
        hx-swap="delete"
        hx-target="closest div"
    >
        Delete
    </button>
</div>
```

## Transiciones CSS

Añadir transiciones CSS pueden dar un toqué pulido a tu aplicación web. Por ejemplo, cuando tu tarea es borra en tu aplicación de recordatorios, el renglón en la lista puede instantáneamente desaparecer. Pero es más visual si el renglón desaparece gradualmente antes de desperecer por completo.

Cuando htmx intercambia el DOM sigue una serie de pasos:

- Añade la clase CSS `htmx-swapping` al elemento objetivo.
- Espera por un corto tiempo (`htmx.config.defaultSwapDelay` por defecto es 0).
- Remueve la clase CSS `htmx-swapping` del elemento objetivo.
- Añade la clase CSS `htmx-settling` al elemento objetivo.
- Crea un elemento DOM representando el nuevo HTML y añade la clase CSS `htmx-added` a él.
- Intercambia el nuevo elemento DOM dentro del DOM, además remplaza el objetivo o coloca relativamente al objetivo.
- Espera por un corto periodo de tiempo (`htmx.config.defaultSettleDelay` por defecto 20ms).
- Remueve la clase CSS `htmx-added` del nuevo elemento DOM.
- Remueve la clase CSS `htmx-settling` del elemento objetivo.

Hay dos cosas que se requieren para implementar las transiciones CSS. Primero, el elemento existente y el nuevo elemento deben tener el mismo `id`. Este es referido como un _stable id_. Segundo, la espera de `swap` debe estar establecido con la misma duración que la transición CSS, por ejemplo, `hx-swap="outerHTML swap:1s"`.

El siguiente CSS cambia la `opacity` de 1 a 0 en una duración de un segundo utilizando al función `ease-out`.

```css
.todo-item.htmx-swapping {
    opacity: 0;
    transition: opacity 1s ease-out;
}
```

El atributo `hx-swap` en el botón de borrar es modificado para incrementar la espera entre añadir la clase CSS `htmx-swapping` al objetivo y removerlo. El objetivo en este caso es el elemento que representa el renglón de la tarea la cual contiene el botón borrar. Esta espera remueve el objetivo hasta que la transición CSS haya terminado.

```html
<button
    class="plain"
    hx-confirm="Are you sure?"
    hx-delete={`/todos/${id}`}
    hx-swap="delete swap:1s"
    hx-target="closest div"
>
    Delete
</button>
```

## Reiniciando un Formulario

Normalmente es deseable reiniciar un `form` después de un envío exitoso. Esto limpia todos los controles contenidos en el `form` para prepararlo parar un nuevo ingreso de información. Un `form` pude ser reiniciado llamando a `this.reset()` donde `this` hace referencia al `form`.

Para especificar un código que se ejecute después de que la petición ha sido enviado y una respuesta ha sido recibida, utiliza el atributo `hx-on:htmx:after-request`. La versión corta de este atributo es: `hx-on::after-request`, el cual remueve el `htmx` de en medio.

```html
<form
  hx-post="/todos"
  hx-target="#todo-list"
  hx-swatp="afterbegin"
  hx-disabled-elt="#add-btn"
  hx-indicator=".htmx-indicator"
  hx-on::after-request="this.reset()"
  x-data="{text: ''}"
>
  <input
    name="description"
    placeholder="enter new todo here"
    size="{30}"
    type="text"
    x-model="text"
  >
  <button id="add-btn" :disabled="text.trim().length === 0">
    Add
  </button>
   <img alt="loading" class="htmx-indicator" src="spinner.gif" />
</form>
```

- `hx-target` - Especifica el HTML regresado por el _endpoint_ POST `/todos` que coincidirá con los elementos con el id "todo-list" (no mostrados aquí).

- `hx-swap` - Especifica el HTML regresado que será insertado al principio del contenido del elemento objetivo.

- `hx-disabled-elt` - Especifica el botón "Add" que debería ser deshabilitado mientras la petición POST `/todos` está siendo procesada.

- `hx-indicator` - El elemento con la clase CSS "htmx-indicator" debería mostrar mientras la petición POST `/todos` está siendo procesada.

- `hx-on::after-request` - Especifica el `form` que debería ser reiniciado después de recibir la respuesta satisfactoria del POST `/todos`.


## Búsqueda Activa

Cuando el usuario detiene su tecleo por 200 milisegundos y el valor del input ha cambiado, la petición POST es enviada al _endpoint_ `/search`. Nota que presionando las teclas de flecha que mueven el cursos a través del `input` no cambian el valor. El _endpoint_ regresa un listado de items (elementos `li`) describiendo los nombres que coinciden. Estos remplazan el contenido actual (`innerHTML`) de los elementos de la lista sin orden (`ul`) con el id "matches".

```html
<html>
    <head>
        <title>htmx Active Search</title>
        <link rel="stylesheet" href="styles.css" />
        <script src="https://unpkg.com/htmx.org@2.0.0"></script>
    </head>
    <body>
        <label for="name">Name</label>
        <input
            autofocus
            hx-trigger="keyup changed delay:200ms"
            hx-post="/search"
            hx-target="#matches"
            name="name"
            size="{10}"
        >
        <ul id="matches"></ul>
    </body>
</html>
```

## Actualizaciones Optimistas

Si un _endpoint_ puede ser lento al responder, utilizando `hx-indicator` para mostrar un _spinner_ es buena idea. La interfaz puede asumir éxito y actualizarse a sí mismo optimisticamente. Por ejemplo, presionando en el botón "like" puedes inmediatamente cambiar el color o quitarlo que será utilizado cuando la respuesta es recibida. Si la respuesta indica éxito, el color cambia a lleno de color. Si la respuesta indica un fallo, el color puede ser reiniciado.

Cuando la columna con el corazón de "like" es presionada, dos cosas pasan. Primero, la función `optimisticLike` es llamada e inmediatamente remplaza el corazón actual con uno rosa. Segundo, la petición PUT es enviada a el _endpoint_ `/dog/:breed` para intercambiar cualquier raza de perro que te guste en el servidor. Este _endpoint_ regresa un nuevo corazón que será rojo o blanco y remplaza el corazón rosa que es temporalmente mostrado.

```html
<script>
    function optimisticLike(event)  {
        const td = event.target;
        // Replace the text "pink-heart" with the corresponding emoji.
        td.textContent = 'pink-heart';
    }
</script>
    ...
    <table hx-get="/table-rows" hx-target="tbody" hx-trigger="revealed">
        <thead>
            <tr>
                <th>Raza</th>
                <th>¿Te Gusta?</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>
    <img alt="loading" class="htmx-indicator" src="/spinner.gif" />
    ...
```
Segmento htmx

```html
    <tr>
        <td>{breed}</td>
        <td
            class="center"
            hx-put="{/dog/${breed}"
            hx-indicator=".htmx-indicator"
            hx-on:click="optimisticLike(event)"
        >
            { getHeart(dogs.get(breed) ?? false) }
        </td>
    </tr>
```

## Paginación

Cuando hay un gran número de items que desplegar. Normalmente se utiliza la paginación para mostrar una página de items a la vez.

El siguiente HTML renderiza una table que es llenada a través de la petición GET `/image-row` cuando la página es cargada. Utiliza el parámetro `page` para indicar que página de las imagenes debería mostrar -- inicialmente sería la 1. El servidor establece el tamaño de la página en 5, que es el número de imagenes que serán mostradas.

HTML inicial:

```html
...
<body>
    <h1>Pagination</h1>
    <table
        hx-trigger="load"
        hx-get="/image-rows?page=1"
        hx-indicator=".htmx-indicator"
    ></table>
    <div id="pagination-row">
        <span id="pagination-buttons"></span>
        <img alt="loading" class="htmx-indicator" src="/spinner.gif" />
    </div>
</body>
...
```

Segmento de remplazo htmx:

```html
<!-- It doesn't work to put the headings in index.html and replace tbody instead of table. -->
<table id="image-table">
    <tr>
        <th>File Name</th>
        <th>Image</th>
    </tr>
    {pageFilenames.map((filename, index) => {
        const isLast = index === ROWS_PER_PAGE - 1;
        return ImageRow(filename, isLast);
    })}
</table>

<!-- The hx-indicator and hx-target attributes are inherited by the buttons inside this span. -->
<span
    id="pagination-buttons"
    hx-swap-oob="true"
    hx-indicator=".htmx-indicator"
    hx-target="#image-table"
>
    <button
        disabled={page === 1}
        hx-get={`/image-rows?page=${page - 1}`}
    >
        Previous
    </button>
        <button hx-get={`/image-rows?page=${page + 1}`}>Next</button>
</span>
```

## _Scroll_ Infinito

Otra aproximación para manejar los casos donde hay un gran número de items para desplegar es el llamdo _scroll_ infinito.
Inicialmente, un número pequeño de items es traido del servidor. Cuando el usuario comienza ha hacer _scroll_ hacía abajo hasta llegar al último item en la vista, una petición para obtener más items es automaticamente enviada al servidor. Esto se repite cada vez que el usuario siga haciendo _scroll_ hacía abajo, dando la ilusión de que todos los items fueron cargados a la vez.

Utiliza `hx-swap="beforeend"` para establecer que los renglones de la tabla regresados por el servidor deberen ser colocados antes del final de la tabla en lugar de remplazar la tabla entera.

HTML inicial:

```html
...
<body>
    <h1>Scroll infinito</h1>
    <table
        hx-trigger="load"
        hx-get="/image-rows?page=1"
        hx-indicator=".htmx-indicator"
        hx-swap="beforeend"
    >
        <tr>
            <th>Nombre</th>
            <th>Descripción</th>
        </tr>
    </table>
    <img alt="loading" class="htmx-indicator" src="/spinner.gif" />
</body>
...
```

Segmento htmx para el último renglón de la tabla:

```html
    <!-- Solo si es el último renglón, sino va vacío -->
    <tr 
        hx-trigger="revealed"
        hx-get="/image-rows?page=" + (page + 1)
        hx-indicator=".htmx-indicator"
        hx-swap="afterend"
    >
        <td>{filename}</td>
        <td>
            <img alt="{filename}" src="{./images/ + filename}" />
        </td>
    </tr>
```

## Alternando Selección

Una forma de permitir a los usuario selección una sola opción de una colección de opciones es utilizando el elemento `select` HTML. Otra aproximación es desplegar un conjunto de botones y estilizarlos para mostrar el más reciente presionado con un estilo diferente. Esto tiene la ventaja que los usuarios pueden ver todas las opciones disponibles sin tener que presionar sobre ellas, pero no es recomendable para una gran número de opciones.

En casos donde la selección necesita ser enviada al servidor, para guardar datos en base de datos, podemos utilizar intercambios fuera-de-banda de htmx.

El siguiente HTML envía una petición GET al _endpoint_ `/dogs` para regresar un conjunto inicial de botones que muestran nombres de perros.

Carga inicial:

```html
<body hx-get="/dogs" hx-trigger="load"></body>
```

Envío de segmento htmx:

```html
<button class={classes} hx-get={`/toggle/${name}`} id={name} {...attrs}>
    {name}
</button>
```

## Votación (_Polling_)

