# 12 - Trabajar con Elementos de Audio y Video

## ¿Cuáles son los roles de los elementos HTML Audio y Video y cómo funcionan?

El elemento `audio` soporta formatos de audio populares como mp3, wav y ogg.

El elemento `video` soporta formatos mp4, ogg y webm.

**Ejemplo:**
```html
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3" loop controls></audio>
```

El atributo `controls` permite a los usuarios gestionar la reproducción de audio, incluyendo ajustar el volumen, pausar, o reanudar la reproducción.
El atributo `loop` es un atributo booleano que hace que el audio se reproduzca continuamente.
Otro atributo que puedes usar es el atributo `muted`.

En cuanto a los tipos de archivos de audio, hay diferencias en qué navegadores soportan qué tipo. Puedes usar elementos `source` dentro del elemento `audio`, y el navegador seleccionará la primera fuente que comprenda.

**Ejemplo:**
```html
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

Todos los atributos que hemos aprendido hasta ahora también son compatibles con el elemento `video`.

Si deseas mostrar una imagen mientras el video se descarga, puedes usar el atributo `poster`.

```html
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
  width="400"
></video>
```

También puedes utilizar varias fuentes para que el navegador opté por la mejor opción para reproducir el formato que pueda.

```html
<video
  controls
  width="400"
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
>
  <source
    src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
    type="video/mp4"
  />
  <source
    src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.webm"
    type="video/webm"
  />
  Your browser does not support the video tag.
</video>
```
