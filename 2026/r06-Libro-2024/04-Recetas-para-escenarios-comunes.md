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
