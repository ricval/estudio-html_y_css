# 20 - Trabajando con Enlaces

## ¿Cuáles son los diferentes tipos de atributos `target` y cómo funcionan?

El atributo `target` le indica al navegador dónde abrir la URL del elemento anchor.

```html
<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
```

Hay cuatro valores importantes posibles para este atributo. Ten en cuenta que cada valor está precedido por un guion bajo.
  1. `_self` - Es el valor predeterminado, abre el enlace en la pestaña o ventana actual.
  2. `_blank` - Abre el enlace en una nueva pestaña o ventana.
  3. `_parent` - Abre el enlace en el padre del contexto actual. Por ejemplo, si tu sitio web tiene un `iframe`, un valor de `_parent` en ese `iframe` se abriría en la pestaña/ventana de tu sitio web, no en el marco incrustado.
  4. `_top` - Abre el enlace en el contexto de navegación más alto. Esto es similar a `_parent`, pero el enlace siempre se abrirá en la pestaña/ventana completa del navegador, incluso para marcos incrustados anidados.


## ¿Cuál es la diferencia entre rutas absolutas y relativas?

Un **camino absoluto** es un enlace completo a un recurso. Comienza desde el directorio raíz, incluye todos los demás directorios y finalmente el nombre del archivo y la extensión.

Una **ruta relativa** especifica la ubicación de un archivo en relación con el directorio del archivo actual. No incluye el protocolo ni el nombre de dominio, haciéndolo más corto y más flexible para enlaces internos dentro del mismo sitio web.


## ¿Cuál es la diferencia entre barras, un solo punto y doble punto en la sintaxis de rutas?

Estos se llaman rutas de archivos. Hay tres sintaxis clave que debe conocer. Primero es la barra, que puede ser una barra invertida (\) o una barra diagonal (/) dependiendo de tu sistema operativo. La segunda es el punto único (.). Y finalmente, tenemos el doble punto (..).

Un solo punto señala el directorio actual, y dos puntos señalan el directorio padre.


## ¿Cuáles son los diferentes estados de los enlaces y por qué son importantes?

Hay cinco estados diferentes en los que un enlace puede estar.
  1. `:link` - Este estado representa un enlace que el usuario no ha visitado.
  2. `:visited` - se aplica cuando un usuario ya ha visitado la página a la que se enlaza.
  3. `:hover` - Este estado se aplica cuando un usuario está pasando el cursor sobre un enlace.
  4. `:focus` - Este estado se aplica cuando enfocamos un enlace. Generalmente presionando la tecla `tab`.
  5. `:active` - Este estado se aplica a enlaces que están siendo activados por el usuario. Al momento de dar clic con el ratón.

Cuando uses estos estados para estilizar tus enlaces, hay un orden específico en el que necesitas escribir tu CSS: link, visited, hover, focus, luego active.