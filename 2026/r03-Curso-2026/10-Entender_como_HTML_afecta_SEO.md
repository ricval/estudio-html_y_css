# 10 - Entender cómo HTML afecta a SEO

## ¿Cuál es el papel de la Meta Descripción y cómo afecta al SEO?

El SEO, o Optimización para Motores de Búsqueda, es una práctica que optimiza las páginas web para que sean más visibles y ocupen una mejor posición en los motores de búsqueda. Una forma de mejorar el SEO de tu sitio es proporcionar una breve descripción con el elemento `meta`.

```html
<meta
    name="description"
    content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
```

Al establecer el atributo `name` en `description`, se asegura que los navegadores, motores de búsqueda y otras herramientas web interpreten correctamente este metadato. El atributo `content` es donde colocarás tu descripción.


## ¿Cuál es el papel de las etiquetas Open Graph y cómo afectan al SEO?

El protocolo Open Graph le permite controlar cómo aparece el contenido de su sitio web en varias plataformas de redes sociales, como Facebook, LinkedIn y muchas más.

```html
<meta content="freeCodeCamp.org" property="og:title" />
```
Para el atributo `property`, necesitará especificar que es `og:title`. El atributo `content` es donde escribirá el título que desea que aparezca en los sitios de redes sociales.

```html
<meta property="og:type" content="website" />
```
La propiedad `type` se utiliza para representar el tipo de contenido que se comparte en redes sociales. Ejemplos de este contenido incluyen artículos, sitios web, videos o música.

```html
<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>
```

```html
<meta property="og:url" content="https://www.freecodecamp.org" />
```
Hay muchas más propiedades de OG que puede establecer, como `description`, `audio`, `video` y `locale`. Sin embargo, el Open Graph `url`, `image`, `type` y `title` son las más importantes para incluir.