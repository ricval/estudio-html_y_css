# 17 - Trabajando con el Elemento `<iframe>`

## ¿Qué son los Elementos Reemplazados y cuáles son algunos ejemplos?

Un elemento reemplazado es un elemento cuyo contenido es determinado por un recurso externo en lugar de por el CSS mismo.

El elemento en sí es reemplazado por el objeto externo: la imagen. Su CSS puede controlar cosas como la posición de la imagen o aplicar un filtro a ella, pero no puede modificar la imagen en sí.

Con la etiqueta `<iframe>` puedes insertar por ejemplo un video de YouTube o una página de mapas.

```html
<iframe
  title="Map of the Royal Observatory, Greenwich, London"
  width="300"
  height="200"
  src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&amp;layer=mapnik">
</iframe>
```

El elemento en sí es reemplazado por el objeto externo: el sitio. Su CSS puede cambiar la posición del sitio incrustado, pero no puede modificar el contenido del sitio.


## ¿Cómo se incrustan vídeos en su página usando el elemento iframe?

```html
<iframe
  width="400"
  height="400"
  src="https://www.youtube.com/embed/PkZNo7MFNFg?si=-UBVIUNM3csdeiWF"
  title="Learn JavaScript - Full Course for Beginners (YouTube video)"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
```

El atributo `src` especifica la URL de la página que desea incrustar. El atributo `width` especifica el ancho del `iframe`. El atributo `height` especifica la altura del `iframe`. El atributo `allowfullscreen` permite al usuario mostrar el `iframe` en modo de pantalla completa. También es una buena práctica especificar un atributo `title` para el `iframe`, ya que es importante para la accesibilidad.

El atributo `allow`, por otro lado, te permite definir lo que un iframe puede o no puede hacer. Esto se llama una lista de permisos. En el ejemplo anterior, agregar `clipboard-write` permite que la página incrustada escriba elementos en tu portapapeles. Los elementos en una lista de permisos pueden separarse por puntos y comas o espacios, y ambos pueden usarse juntos.

Si desea incrustar HTML directo dentro del elemento `iframe`, debe usar el atributo `srcdoc` en lugar de `src`.
