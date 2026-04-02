# 00 — Introducción

## Prefacio

Los desarrollo web modernos se han vuelto sobre complicados. _Frameworks_ populares tienen con curvas de aprendizaje algo pesadas para poder conseguir el resultado deseado.

He tenido experiencia de primera mano con el desarrollo web con aproximaciones que incluyen JavaScript vanilla, jQuery, AngularJS, Angular, React, Vue y Svelte. Para mí, cada uno de ellas supuso una mejora con respecto a lo anterior. Pero se trataba de mejoras graduales.

He encontrado **htmx** diferente de estos _frameworks_ y librerías. Vayamos a descubrir como **htmx** simplifica el desarrollo web, resultando en aplicaciones que son fácil de entender y requieren menos código.

Los _framesworks_ modernos para ser implementados en una aplicación de una-sola-página _single-page_ (_SPAs_) frecuentemente te llevan a seguir los siguientes pasos:

- El navegador descarga algo con un montón de código en JavaScript.
- Las interacciones del usuario disparan envíos en _HTTP request_ a un _endpoint_ en el servidor.
- Los _endpoints_ hacen _queries_ a la base de datos.
- La información de la base de datos es convertida en _JSON_.
- JavaScript corre en el navegador y analiza el _JSON_ y lo convierte en un objeto JavaScript.
- El _framework_ genera un HTML desde el objeto JavaScript y lo inserta en le DOM.

_HyperText Markup eXtensions (htmx)_ es una librería del lado del cliente que simplifica el proceso.
Con **htmx**, los _endpoints_ convierten la información en HTML (o texto plano) en lugar de JSON, y eso regresa al navegador. El JavaScript en el navegador no necesita analizar más el JSON y generar un HTML a partir de él. Solo es necesario insertar el HTML en el DOM. Refrescar la página entera ya no es necesario.

La librería **htmx** es algo pequeña — menos de 17Kb.

## Conocimiento requerido

Es útil que sepas algo de lo siguiente:

- Saber utilizar un editor de código como VS Code
- HTML para especificar que será renderizado en el navegador
- CSS para dar estilo a lo renderizado
- Un lenguaje de programación para implementar los _endpoints_ HTTP
- Conceptos básicos de HTTP como _request_ y _responses_
- Comandos de línea de comandos básicos para cambiar de directorio e iniciar un servidor local web
