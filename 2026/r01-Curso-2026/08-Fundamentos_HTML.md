# 08 - Fundamentos de HTML

## ¿Qué son los elementos `<div>` y cuándo debes usarlos?

El elemento `div` se usa como contenedor para agrupar otros elementos.

Principalmente usarás el elemento `div` cuando quieras agrupar elementos HTML que compartirán un conjunto de estilos CSS.


## ¿Qué son los IDs y las clases, y cuándo debes usarlos?

El atributo `id` añade un identificador único a un elemento HTML.

Puedes hacer referencia al nombre id de title dentro de tu JavaScript o CSS.

Otra cosa a tener en cuenta acerca de los valores de `id` es que no pueden tener espacios en ellos.

En contraste con el atributo `id`, el valor del atributo `class` no necesita ser único y puede contener espacios.

Si quieres agregar múltiples nombres de clase a un elemento, puedes hacerlo separando los nombres con un espacio. Aquí tienes un ejemplo actualizado aplicando múltiples clases a un elemento `div`.

```html
<div class="box red-box"></div>
```

¿cuándo debes usar un `id` en lugar de `class`? Las clases son mejores para usar cuando quieres aplicar un conjunto de estilos a muchos elementos. Si quieres apuntar a un elemento específico, es mejor usar un `id` porque esos valores deben ser únicos.


## ¿Qué son las entidades HTML y cuáles son algunos ejemplos comunes?

Una entidad HTML, o referencia de carácter, es un conjunto de caracteres utilizados para representar un carácter reservado en HTML.
Por ejemplo si quisieras mostrar el código: `<p>This is an <img /> element</p>` no se vería bien, porque el navegador trataría de interpretarlo como HTML. Lo que debes hacer es cambiar los símbolos de `<` y `>` por: `&lt;p&gt;` y `&lt;/p&gt;`. Con esto se imprimirá el texto HTML como texto y el navegador no lo interpretara como código.

```html
<p>This is an &lt;img /&gt; element</p>
```
Resultado:
> This is an &lt;img /&gt; element


## ¿Cuál es el papel del elemento de `<script>` en HTML, y cómo se puede usar para enlazar archivos JavaScript externos?

El elemento `<script>` se usa para incrustar código ejecutable. La mayoría de los desarrolladores utilizarán esto para ejecutar código JavaScript.

Aquí hay un ejemplo de cómo usar el elemento `<script>` para enlazar a un archivo JavaScript externo:

```html
<script src="path-to-javascript-file.js"></script>
```

