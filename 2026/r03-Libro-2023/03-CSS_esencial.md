# Capítulo 03: CSS Esencial #

## 03.01 - Introducción a las Hojas de Estilo en Cascada (CSS) ##

Juegan un rol importante en le mundo del desarrollo web, separando el contenido de la presentación.

### 03.01.01 - El Rol del CSS en el Desarrollo Web ###

El rol principal cae en desacoplar el contenido de la presentación. Separando el estilo del contenido, los desarrolladores pueden administrar, actualizar y modificar la apariencia del sitio web sin afectar la estructura.

#### El concepto de Cascada

El termino "cascada" en CSS se refiere al orden de prioridad y específicamente en la aplicación de estilos a los elementos. Entender el concepto de cascada es crucial para resolver conflictos y asegurarse que los estilos son aplicados consistentemente. Los estilos pueden ser heredados de los elementos padres, sobre-escribiendo por un selector más especifico, o influenciado por el orden en que los estilos son declarados.

### 03.01.02 - Sintaxis CSS

#### Reglas CSS y Declaraciones

Las reglas CSS consisten de selectores y declaraciones. Un selector apunta a un elemento HTML, y las declaraciones definen como esos elementos deberían aparecer.

  - Selectores:
        - Los selectores definen los elementos HTML que usaran las reglas de estilo que se aplicaran.
        - Los tipos de selectores incluyen selectores de etiqueta, clase, id, atributos y pseudo-clases.

    - Declaraciones:
        - Consisten en pares de propiedades-valor.
        - Definen el aspecto de un elemento por su estilo. (ejem. color, font-size).
        - Los valores especifican los detalles del estilo para la propiedad del selector.

    - Especificación:
        - Determina con que regla toma precedencia cuando múltiples reglas apuntan al mismo elemento.

Ejemplo:
```css
/* Selector */
h1 {
    /* Declaración */
    color: #336699;
    font-size: 24px;
}
```

#### Selectores y Propiedades

Los selectores y propiedades son los bloques de construcción del estilado CSS, permiten a los desarrolladores precisar el elemento objetivo y definir su apariencia.

  - Tipos de Selector
    - Etiqueta: Apuntan a una etiqueta especifica HTML.
    - Clase: Apuntan a los elemento con el atributo class especifico.
    - Id: Apunta a un único elemento con el atributo id especifico.
    - Atributo: Apunta a los elementos basados en los valores de un atributo.
    - Pseudo-clases: Apuntan a elementos en estados específicos (ejem. `:hover`)
  - Propiedades Comunes:
    - Color: Define los colores de texto y fondo.
    - Font: Controla la tipografía, incluyendo la familia y el tamaño.
    - Margen y _Padding_: Establece el espaciado alrededor de los elementos.
  - Propiedades Cortas:
    - Permiten declaraciones concisas para múltiples propiedades relacionadas (ejem. `margin` en lugar de `margin-top margin-right`, etc.)

#### Comentarios en CSS

- Se escriben dentro de los caracteres `/* comentario */`.
- Pueden ser estar en una sola línea hasta varias.

### 03.01.03 - Selectores CSS

#### Tipos de Selectores (Class, id, Tag)

- **Tag**: Elementos basados en su nombre de etiquetas.
- **Class**: Especificados por el atributo `class`. ejem. `.subrayado`.
- **ID**: Selecciona un solo elemento especificado por el atributo `id`, ejemplo: `#formulario-nuevo`.

#### Combinando y Agrupando Selectores

Ejemplo de combinación: `.main p {}`. Aplicará cambios en lso párrafos dentro de una etiqueta con clase main.


## 03.02 - Aplicando Estilo a Texto y Fuentes

### 03.02.01 - Propiedades de las Fuentes

Puedes elegir entre: la familia, tamaño, peso, estilo.

#### Familia de la Fuente

Define el tipo de fuente. Por lo general se declara una lista, y el navegador hará un intento por la primera disponible de la lista.
```css
body {
    font-family: 'Arial', sans-serif;
}
```
En este caso, el navegador intentará establecer la familia de la fuente en "Arial", si no está disponible, intentará con la siguiente: "sans-serif".

#### Tamaño de Fuente y Peso

`font-size` determina el tamaño de la fuente. Puede especificar varios tipos de unidades como: pixeles, ems o porcentajes.
`font-weight` define el espesor de los caracteres, puede ser una valor entre los rangos: normal o bold.
```css
h1 {
    font-size: 24px;
    font-weigth: bold;
}
```

#### Estilo de Fuente y Variante

La propiedad `font-style` habilita la manipulación del estilo del texto, permitiendo aplicar estilos como itálico o oblicuo. Mientras que `font-variant` controla el aspecto como todo en mayúsculas pequeñas.

```css
p {
    font-style: italic;
    font-variant: small-caps;
}
```

### 03.02.03 - Fuentes Web

#### Utilizando Fuentes Personalizadas

Las fuentes personalizadas proveen un forma de expresión que da identidad y creatividad.
Para utilizar una fuente personalizada utilice el formato WOFF (_Web Open Font Format_) o WOFF2. Son formatos optimizados para la web.
Utilice una referencia de archivos de fuente en tu css como: `@font-face`. Debe especificar el nombre de la fuente (familia), su dirección fuente (_source_) y otras propiedades.
```css
@font-face {
    font-family: 'FuentePersonalizada';
    src: url('path/to/fuente-personalizada.woff2') format('woff2');
    /* más propiedades */
}
```

Provea un listado seguro de fuente por si no se consigue renderizar las fuentes personalizadas.
Pruebe su sitio web en varios navegadores, para asegurarse de que las fuentes se ven correctamente.

#### Google Fonts y Font Awesome

**Google Fonts**: Es un sitio popular gratis de recursos de varias fuentes, optimizadas para la web.
Visite el sitio y copie la etiqueta `<link>` dentro de su `<head>` en su archivo HTML.

**Font Awesone**: Provee una fuente de iconos escalables, para proyectos web, y pueden ser personalizados añadiendo color con CSS.
Para incluirlo añada es link a su head:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fontawesome/5.15.3/css/all.min.css" integrity="sha384-r5ce/VgQ2Fq52lqG2J0ebH/NTStGhv8g32Q6ZWo3PeQ/hv3sDVmO7f5t4APqprL4" crossorigin="anonymous">
```
y para utilizarla
```html
<i class="fas fa-heart"></i>
```

#### Estrategias de Carga de Fuentes

Utilice la propiedad `font-display` en la regla `@font-face` para controlar como se despliegan las fuentes mientras se están cargando. Las opciones incluyen: `auto`, `swap`, `fallback` y `optional`.

**Pre-carga las fuentes**: Utilizando la etiqueta `<link>` con el atributo `rel="preload"` en el `<head>` de tu HTML. Aseguras que tu navegador descargue los recursos de tu fuente al principio del proceso de carga de la página.
```html
<link rel="preload" href="path/to/font.woff2" as="font" type="font/woff2" crossorigin="anonymous">
```

**Carga Asíncrona**: Las fuentes no esenciales pueden ser asíncronas, utilizando JavaScript para prevenir una carga lenta de la página. Añade la creación de elemento `<link>` dinámicamente:
```js
var fontLink = document.createElement('link');
fontLink.rel = 'stylesheet';
fontLink.href = 'path/to/no-esencial-fuente.css';
document.head.appendChild(fontLink);
```

**API de carga de fuentes**: Utiliza la carga de fuentes por API para verificar y reaccionar al estatus de la carga de tu fuente.
```js
var customFont = new FontFace('CustomFont', 'url(path/to/customfont.woff2)');
customFont.load().then(function(font) {
    document.fonts.add(font);
    document.body.style.fontFamily = 'CustomFont, sans-serif';
});
```

**Optimiza los archivos de tus fuentes**: Herramientas como 'Font Squirrel' o convertidores online te pueden asistir en este proceso.


## 03.03 - _Box Model_ y _Layout_

La estructura visual de tu página depende de esto.

### 03.03.01 - Vistazo al _Box Model_

El _Box Model_ conceptualiza cada elemento HTML como un caja rectangular compuesta por cuatro componente clave: Contenido, Separación, Borde y Margen.
- **Contenido**: Representa el contenido actual o la información dentro de la caja. Incluye texto, imágenes u otros tipos de media.
- **Separación**: Es el _padding_, la separación entre el contenido y el borde. Da más espacio, asegurándose de que el contenido no toque el borde.
- **Borde**: Es lo que rodea al _padding_ y el contenido. Definido comúnmente como una línea sutil de una caja.
- **Margen**: Es el espacio fuera del borde. Separa a esta caja de otras.

#### Dando tamaño al Box Model (Content-Box vs Border-Box)

CSS provee dos modelos primarios de tamaño de caja: Content-Box y Border-Box.
- **Content-Box**: Es el utilizado por defecto. El ancho y alto solo se aplican al área del contenido. El padding, borde y margen son añadidos para especificar el ancho y alto.
- **Border-Box**: Las propiedades de ancho y alto incluyen el contenido, padding y borde. El margen de fuera restante se suma al ancho y alto. Este model simplifica los cálculos del _layout_ especialmente cunado se esta tratando con varios tamaños de contenido.

#### Content-Box para Precisión

El modelo **Content-Box** es utilizado por los diseñadores cuando se requiere de precisión en el tamaño del contenido.
```css
/* Ejemplo: Content-Box para posición en el tamaño */
.content-box-element {
    box-sizing: content-box;
    width: 200px; /* El ancho solo se aplica al contenido */
    padding: 20px;
    border: 2px solid #333;
}
```

#### Border-Box para Diseño Responsivo Simplificado

Cuando utilizas Border-Box, el ancho especificado incluye el padding y el borde. Esto simplifica los cálculos del layout, especialmente cuando se manejan varios tamaños de contenido o diseño flexible, componentes responsivos.
```css
/* Ejemplo: Border-Box para diseños responsivos */
.border-box-element {
    box-sizing: border-box;
    width: 200px; /* El ancho incluye el contenido, padding y borde */
    padding: 20px;
    border: 2px solid #333;
}
```

### 03.03.02 - Margen, Separación y Borde

```css
/* Individual margins */
.element {
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 15px;
    margin-left: 25px;
}

/* Shorthand notation */
.element {
    margin: 10px 20px 15px 25px;
}
```

Bordes
```css
/* Estableciendo propiedades para el borde */
.element {
    border-width: 2px; /* Ancho del borde */
    border-style: solid; /* Estilos de borde (solid, dashed, dotted, etc.) */
    border-color: #333; /* Color del borde */
    border-radius: 10px; /* Añade redondez a las esquinas */
}
```

### 03.03.03 - Posicionamiento de los Elementos

#### Posicionamiento Static, Relative, Absolute y Fixed

**Posicionamiento Estático (_Static_)**: Es el posicionamiento por defecto para todos los elementos HTML. En este modo todos los elementos se posicionan de acuerdo al flujo normal del documento, se van apilando en el orden en el que van apareciendo.

```CSS
.ejemplo-static {
    position: static;
}
```

**Posicionamiento Relativo (_Relative_)**: Cambia el elemento de su posición por defecto sin afectar al arreglo de los otros elemento.

**Posicionamiento Absoluto (_Absolute_)**: Quita el elemento de su posición por defecto y lo posiciona en relativo lo más cerca de su antecesor. Si no hay antecesor, toma la posición relativa del bloque inicial contenedor. Normalmente el elemento `<html>`.

**Posicionamiento Fijo (_Fixed_)**: El elemento se está en esa posición por siempre aún y cuando el usuario haga _scroll_ en la página.

#### Z-Index y Apilando Contexto

**Z-Index**: esta propiedad determina el orden en que se apilan los elementos a través del eje-z. Elemento con mayor z-index aparecerán en frente que los de menor valor.

```css
.z-index-ejemplo {
    z-index: 2;
}
.z-index-ejemplo2 {
    z-index: 1;
}
```

**Apilando Contexto**: Es esencial para distribuciones complejas. Esta formado por ciertas propiedades CSS, como la opacidad y transformación. Elementos con el mismo contexto de apilado son apiladas juntas antes de considerarlas elementos en otro contexto de apilado.
```css
.stacking-context-ejemplo   {
    transform: translateZ(0);
    /* Crea un apilado de contexto */
}
```

### 03.03.04 - Flexbox y Grid Layout

#### Introducción al _Flexbox_

Es el nombre corto de Caja Flexible. Aporta una distribución más eficiente y predecible. Es útil con el arreglo y alineamiento de items dentro de un contenedor.

Es una distribución de una dimensión que trabaja solo con una eje, en lugar de dos, horizontal y vertical. Esto permite la creación de diseños flexibles y responsivos para distribuir espacio dentro de un contenedor y alineando items a lo largo del eje principal y a través de él.

**Conceptos Clave**:
  - **Flex Container**: El elemento padre que contendrá los items tipo flex.
  - **Flex Items**: Los elementos hijos que el contenedor flex convertirá en cajas flexibles.

**Propiedades del Contenedor Flex**:
  - **display**: Establece el flex para habilitar sus propiedades tipo flex.
  - **flex-direction**: Define la dirección del eje principal (_row_, _column_, _row-reverse_, _column-reverse_).
  - **justify-content**: Alinea los items a través de eje principal.
  - **align-items**: Alineación de los item a través del eje.
  - **align-self**: Permite a items individuales sobre escribir los valores de _align-items_.

**Propiedades de los items Flex**:
  - **order**: Especifica el orden.
  - **flex-grow**: Determina cuanto un flex item puede crecer relativamente a otros.
  - **flex-shrink**: Define la habilidad de un item flex para contraerse.
  - **flex-basis**: Establece el tamaño inicial de un item flex.

#### Contenedores Flex e Items

**Creando un Contenedor Flex**:
Para establecer un contenedor flex, asigna la propiedad `display` a `flex` en el elemento padre:
```css
.container  {
    display: flex;
}

.item {
    flex: 1; /* Cada item toma un espaciado igual */
}
```

**Definiendo los Items Flex**:
Cada elemento hijo dentro de un contendor flex se vuelve un item flex:
```html
<div class="container">
    <div class="item">item 1</div>
    <div class="item">item 2</div>
    <div class="item">item 3</div>
</div>
```

#### Introducción al _Grid Layout_

Este tipo utiliza una arreglo bidimesional que da un control preciso sobre el arreglo de los elementos tanto en renglones como en columnas. Es muy poderoso para diseños complejos basados en estructuras de malla.

Permite la creación de mallas con columnas y renglones fijos o de tamaño-flexible.

**Conceptos Clave**:
  - **Grid Container**: Es el elemento padre contenedor de los grid items.
  - **Grid Items**: Son los elementos hijos del grid contenedor que se alinean en renglones y columnas.

**Propiedades del Grid Contanier**:
  - **display**: Establece la malla para habilitar las propiedades de malla.
  - **grid-template-rows / grid-template-columns**: Define el tamaño y número de renglones y columna.
  - **grid-gap**: Especifica el tamaño de espacios entre los grid items.

**Propiedades de los Grid Items**:
  - **grid-row / grid-column**: Determina el lugar de un item dentro del grid.
  - **grid-area**: Asigna un nombre a un item, permitiendo posicionarlo a través de una plantilla grid.

#### Contenedores Grid e Items

**Creación de un Contenedor Grid**:
```css
.container  {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Tres columnas iguales */
    grid-gap: 10px; /* Espacio entre los grid items */
}

.item {
    /* Estilo adicional para los grid items */
}
```

**Definiendo los Grid Items**:
Cada elemento hijo dentro de un contendor grid se vuelve un item grid:
```html
<div class="container">
    <div class="item">item 1</div>
    <div class="item">item 2</div>
    <div class="item">item 3</div>
</div>
```
