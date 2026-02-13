# 24 - Comprender Elementos Semánticos Matizados

## ¿Cuándo deberías usar el elemento de énfasis en vez del elemento de texto idiomático?

El elemento de texto idiomático, `i`, originalmente se utilizaba para propósitos presentacionales para mostrar el texto en cursiva. Pero ahora, se usa frecuentemente para resaltar voz o estado de ánimo alternativos, términos idiomáticos de otro idioma, términos técnicos y pensamientos.

```html
<p>There is a certain <i lang="fr">je ne sais quoi</i> in the air.</p>
```

El elemento `i` no indica si el texto es importante o no, solo muestra que de alguna manera es diferente del texto circundante.

Si necesitas enfatizar la importancia del texto, puedes usar un elemento semántico similar llamado el elemento de énfasis, `em`.

Es importante saber que estos elementos no deben usarse solo para propósitos presentacionales. Si necesitas mostrar el texto en cursiva, pero el texto no tiene un propósito especial, estilo o significado en el párrafo, deberías usar CSS en su lugar.


## ¿Cuándo se debe usar el elemento Strong en lugar del elemento que llama la atención?

El "elemento que llama la atención", `b`, se utiliza comúnmente para resaltar palabras clave en resúmenes, o nombres de productos en reseñas. Normalmente, los navegadores muestran este texto en negrita.

Si necesitas enfatizar la importancia del texto, debes usar el elemento `strong` en lugar del `b`.

`strong` es un elemento HTML semántico que enfatiza texto que es crucial o urgente.

Visualmente ambos son muy similares, porque ambos se renderizan en negrita por defecto. Pero sus significados son bastante diferentes. Mientras el "elemento que llama la atención" `b` solo atrae atención al texto, sin indicar un alto nivel de importancia, el elemento `strong` hace más que eso. Conlleva un sentido de importancia o urgencia. Esta es su principal diferencia.

Para elegir entre ellos, considera el propósito del texto y su importancia dentro del contenido circundante.


## ¿Qué son las listas de descripción, y cuándo deberías usarlas?

Las listas de descripción son perfectas para presentar términos y definiciones en un formato organizado y fácil de leer, como en un glosario, o un diccionario real, donde puedes encontrar palabras con sus definiciones correspondientes.

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <!-- <dt>JS</dt>
  <dd>JavaScript</dd> -->
</dl>
```

Necesitarás tres elementos HTML para definir una lista de descripción. Primero, el elemento de lista de descripción, `dl`, que es el contenedor para toda la lista. Puedes ver que envuelve todos los otros elementos de la lista de descripción en el ejemplo.
Luego, un elemento de término de descripción, `dt`, para cada término.
Y finalmente, después de cada término encontrarás un elemento de detalles de descripción, `dd`, para la descripción, o detalles asociados con ese término.

Otros casos de uso para listas de descripción incluyen especificaciones de productos, preguntas frecuentes, información de contacto y metadatos. Esencialmente, cuando tienes dos piezas de información relacionadas en un formato de par clave-valor, donde una actúa como una etiqueta, la clave, y la otra actúa como información relacionada adicional, el valor, puedes usar una lista de descripción.
