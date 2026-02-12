# 05 - Entendiendo el Código Básico de HTML

## ¿Cuál es el papel del elemento de enlace en HTML y cómo se puede usar para enlazar a hojas de estilos externas?

### `<link>`

El elemento `link` se utiliza para enlazar a recursos externos com las hojas de estilo CSS e íconos.
Debe colocarse dentro del elemento `<head>...</head>`.

```html
<link rel="stylesheet" href="./styles.css" />
```

En atributo `rel` se utiliza para especificar la relación entre el recurso enlazado y el documento HTML.

> 🗒️ **NOTA:** Se considera buena práctica separar el HTML del CSS en diferentes archivos.

El atributo `href` especifica la ubicación URL para el recurso externo.

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ejemplos de elementos link</title>
  <link rel="stylesheet" href="./styles.css" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap"
  rel="stylesheet"
/>
</head>
```

En este ejemplo, el valor `preconnect` para el atributo `rel` le dice al navegador que cree una conexión anticipada con el valor especificado en el atributo `href`. Esto se hace para acelerar los tiempos de carga de estos recursos externos.

Otro caso de uso común para el elemento `link` es enlazar a íconos. Aquí hay un ejemplo de enlace a un favicon:

```html
<link rel="icon" href="favicon.ico" />
```

Un **favicon**, que es la abreviatura de _favorite icon_, es un ícono pequeño que normalmente se muestra en la pestaña del navegador junto al título del sitio. Muchos sitios web usan un favicon para mostrar el ícono de su marca.


## ¿Qué es un boilerplate HTML y por qué es importante?

el _boilerplate HTML_ es como una plantilla lista para tus páginas web. Incluye la estructura básica y los elementos esenciales que todo documento HTML necesita.
Aquí hay un ejemplo:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>
```

- `<!DOCTYPE html>`: Le dice a los navegadores qué versión de HTML estás utilizando.
- `<html>`: Esta engloba todo tu contenido y puede especificar el idioma de tu página. Dentro de la etiqueta. Esta etiqueta agrupa a las etiquetas `<head>` y `<body>`.
- `<head>`: contiene información importante tras bambalinas.
- `<meta>`: Especifica los metadatos de tu sitio. Tienen detalles sobre cosas como la codificación de caracteres.
- `<title>`:  Es el título de tu sitio. Es el texto que aparece en la pestaña o ventana del navegador.
- `<link>`: Vínculos a las hojas de estilo externas.
- `<body>`: Es donde va todo tu contenido.

> 🗒️ **NOTA:** La próxima vez que inicies un nuevo archivo HTML, considera usar un boilerplate. Definitivamente te dará una base sólida sobre la cual construir.


## ¿Qué es la codificación de caracteres UTF-8, y por qué es necesaria?

```html
<meta charset="UTF-8" />
```

