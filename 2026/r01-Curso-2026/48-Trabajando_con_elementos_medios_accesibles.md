# 48 - Trabajando con Elementos de Medios Accesibles

## ¿Cuándo se necesita el atributo `alt` y cuáles son algunos ejemplos de buen texto `alt`?

Texto alternativo, a menudo abreviado como `alt` texto, es una breve descripción textual de una imagen. Proporciona información esencial sobre la imagen para usuarios que no pueden verla, como personas que utilizan lectores de pantalla y otras tecnologías de asistencia.

```html
<img src="puppy.png" alt="Un cachorro blanco y negro con un collar naranja descansa sobre su vientre en la arena, mirando hacia un lado. Una pelota naranja brillante reposa cerca de sus patas delanteras." />
```

Recomendación para un buen texto `alt`:

- Generalmente, no necesitas comenzar con "imagen de" o "foto de." Puedes empezar la descripción directamente.
- Generalmente se recomienda terminar el texto `alt` con un punto para consistencia.
- Si la imagen es un enlace a otra página, en lugar de describir la imagen en sí, el `alt` texto debería describir qué ocurrirá si los usuarios hacen clic en ella.

Si una imagen solo se usa con fines decorativos, debería tener "" (vacío) `alt` texto, para que pueda ser ignorado por los lectores de pantalla y otras tecnologías de asistencia.. Cada imagen en su sitio web debería tener un atributo `alt`, incluso si está vacío. Si omite el atributo `alt` por completo, algunos lectores de pantalla leerán el nombre del archivo en su lugar, lo cual puede distraer a las personas que usan tecnologías de asistencia, por lo que no se recomienda.

## ¿Cuáles son los beneficios de accesibilidad de un texto de enlace adecuado y cuáles son algunos ejemplos de textos de enlace adecuados?

## ¿Cuáles son las buenas maneras de hacer que el contenido de audio y video sea accesible?

Para agregar leyendas o subtítulos a su contenido de video o audio, puede usar el elemento `track` dentro de su elemento `video` o `audio`:

```html
<video
  width="400"
  height="300"
  controls
  src="https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4"
>
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</video>

<audio controls src="sample.mp3">
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</audio>
```

El atributo `kind` se utiliza para indicar al elemento `track` cómo debe usarse. Los valores válidos para el atributo `kind` incluyen `captions`, `subtitles`, `chapters` y `metadata`.

El atributo `srclang` representa el idioma para el contenido del `track`.

El atributo `label` es un título descriptivo para el texto de la pista que los navegadores utilizan para identificarlo y mostrarlo en la lista de pistas de texto disponibles.

Otra cosa importante a considerar es proporcionar una transcripción para su contenido de audio y video. Una transcripción es una versión en texto de todas las palabras habladas en su audio o video. Si tiene un video o audio en un sitio web, simplemente puede agregar la transcripción debajo del audio o video:

```html
<audio controls>
  <source src="audio.mp3" />
  Your browser does not support the audio element.
</audio>

<!-- Transcripción -->
<h3>Transcript</h3>
<p>
  [Speaker 1]: Welcome to the tutorial on making accessible content
</p>
<p>
  [Speaker 2]: Today, we'll cover captions, transcripts, and more.
</p>

<!-- Resto de la Transcripción -->
 ...
```

## ¿Cuáles son algunas formas de hacer que las aplicaciones web sean accesibles mediante teclado?

Muchos usuarios dependen de la tecla `Tab` para moverse a través de elementos interactivos en una página web. Por defecto, los navegadores permiten que los usuarios naveguen con tabulador por elementos como enlaces, botones y campos de formulario en el orden en que aparecen en el HTML. Esto se llama el orden natural de tabulación.

A veces, puede que quieras ajustar qué elementos son enfocables o cambiar su orden de enfoque. El atributo `tabindex` te permite hacer esto.

```html
<input tabindex="2">
<input tabindex="1">
<input tabindex="3">
```

`tabindex="0"` añade el elemento al orden natural de tabulación.

`tabindex="-1"` hace que un elemento sea enfocables programáticamente. Esto es útil para gestionar el foco en elementos que normalmente no son enfocables, como encabezados, contenedores, diálogos o mensajes de error.

Cuando el `tabindex` es mayor que `0` establece un orden de tabulación personalizado. Así que los elementos con valores positivos más bajos se enfocan primero.

`accesskey` es otro atributo que puedes usar para hacer que tu proyecto web sea accesible mediante el teclado. Te permite definir una tecla que enfoca o activa un elemento en particular.

`accesskey="s"` asigna la tecla `S` al botón `Guardar`. En la mayoría de los navegadores, presionar `ALT + S` (en Windows) y `CTRL + Option + S` (en Mac) activará este botón.

```html
<button accesskey="s">Save</button>
<button accesskey="c">Cancel</button>
<a href="index.html" accesskey="h">Home</a>
```
