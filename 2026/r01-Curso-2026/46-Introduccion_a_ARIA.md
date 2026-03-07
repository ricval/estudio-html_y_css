# 46 - Introducción a ARIA #

## ¿Cuál es el propósito de WAI-ARIA y cómo funciona? ##

Hacer accesible el contenido estático puede ser relativamente sencillo, pero el contenido dinámico puede ser más desafiante. Para esto entra en juego WAI-ARIA.

Tenga en cuenta que WCAG y WAI-ARIA no son lo mismo. WCAG proporciona pautas generales para la accesibilidad web, mientras que WAI-ARIA ofrece reglas específicas para hacer que el contenido dinámico e interactivo sea accesible para los usuarios de tecnologías de asistencia.

Por lo tanto, el propósito principal de WAI-ARIA es mejorar la accesibilidad para contenido dinámico y componentes de UI que no tienen equivalentes nativos en HTML.

WAI-ARIA funciona introduciendo un conjunto de atributos que puede añadir a elementos HTML para proporcionar información semántica adicional. Estos atributos se categorizan en roles, estados y propiedades.

Las propiedades ARIA proporcionan detalles adicionales sobre los elementos. Por ejemplo, la propiedad `aria-labelledby` le permite conectar un elemento a una etiqueta específica:

```html
<h2 id="header-id">About freeCodeCamp</h2>
<button id="button-id" aria-labelledby="header-id button-id">Learn More</button>
```

Esto hará que los elementos sean comprensibles y navegables para los usuarios de tecnologías de asistencia.

## ¿Qué son los roles ARIA? ##

ARIA significa Aplicaciones de Internet Ricas y Accesibles.

Los roles ARIA especifican el significado semántico de los elementos HTML. Son esenciales para hacer el contenido web accesible a personas que usan tecnologías de asistencia, como lectores de pantalla.

HTML tiene elementos semánticos y no semánticos, basados en si transmiten significado sobre su contenido.

Muchos elementos HTML semánticos ya tienen un rol ARIA asignado por defecto. Por ejemplo, el elemento `button` tiene un rol ARIA predeterminado de `button`. Pero los elementos no semánticos no tienen un rol. Por ejemplo, los lectores de pantalla no sabrán cómo interpretar el propósito de un `div` si no especifica su rol explícitamente.

Para especificar el rol ARIA de un elemento, solo necesita agregar el atributo `role`, como este `role="ARIA role"`, donde el valor es el nombre de un rol en la especificación ARIA.

Aquí tienes un ejemplo de cómo usar el atributo `role` con un valor de `"alert"`:

```html
<div class="alert" id="exp-warning" role="alert">
  <span class="hidden">Your log in session will expire in 3 minutes.</span>
</div>
```

Hay seis categorías principales de roles ARIA:

- Roles de estructura de documento
- Roles de widget
- Roles de punto de referencia
- Roles de región activa
- Roles de ventana
- Y roles abstractos

Los **roles de estructura de documento** definen la estructura general de la página web. Con estos roles, las tecnologías de asistencia pueden entender las relaciones entre las diferentes secciones y ayudar a los usuarios a navegar por el contenido.

Debe especificar los roles que no tienen un elemento semántico equivalente. Por ejemplo: `toolbar`, `tooltip`, `feed`, `math`, `presentation`, `none`, y `note`.

```html
<div role="math" aria-label="x squared + y squared = 3">
  x<sup>2</sup> + y<sup>2</sup> = 3
</div>
```

Los **roles de widget** definen el propósito y funcionalidad de los elementos interactivos, como las barras de desplazamiento.

Ejemplos de roles de widget incluyen `scrollbar`, `searchbox`, `separator` (cuando es enfocable), `slider`, `spinbutton`, `switch`, `tab`, `tabpanel`, y `treeitem`.

Los **roles de punto de referencia** clasifican y etiquetan las secciones principales de una página web. Los lectores de pantalla los utilizan para proporcionar una navegación conveniente a secciones importantes de una página. Debe usarlos con moderación para mantener el diseño general simple y fácil de entender. Ejemplos de roles de punto de referencia son `banner`, `complementary`, `contentinfo`, `form`, `main`, `navigation`, `region`, y `search`. Cada uno de estos roles tiene un equivalente en HTML, como `header`, `footer`, `aside`, `form`, `main`, `nav`, `section`, y `search`. Si utiliza los elementos HTML adecuados para definir las secciones de su página, entonces no es necesario añadir explícitamente el atributo `role` a estos elementos.

Los roles de región activa definen elementos con contenido que cambiará dinámicamente. De esta manera, los lectores de pantalla y otras tecnologías de asistencia pueden anunciar cambios a usuarios con discapacidades visuales. Estos roles incluyen: `alert`, `log`, `marquee`, `status`, y `timer`.

Los **roles de ventana** definen sub-ventanas, como cuadros de diálogo modales emergentes. Estos roles incluyen `alertdialog` y `dialog`.

```html
<div id="custom-dialog" role="dialog" aria-modal="true" aria-labelledby="dialog-title" class="dialog">
  <div class="dialog-content">
    <h3 id="dialog-title">Confirm Action</h3>
    <p>Are you sure you want to delete this file?</p>
    <div class="dialog-actions">
      <button id="confirm-btn">Yes</button>
      <button id="close-dialog">Cancel</button>
    </div>
  </div>
</div>
```

Y finalmente, tenemos **roles abstractos**. Estos roles ayudan a organizar el documento. Solo están destinados a ser utilizados internamente por el navegador, no por los desarrolladores, por lo que debe saber que existen, pero no debe usarlos en sus sitios web o aplicaciones web.

## ¿Cuáles son las funciones de los atributos aria-label y aria-labelledby? ##

El atributo `aria-label` es una etiqueta invisible para elementos interactivos. Añade una etiqueta de texto a un elemento que los lectores de pantalla pueden leer.

`aria-label` es especialmente útil para elementos que no tienen texto visible pero que aún necesitan ser descritos por lectores de pantalla. Por ejemplo, los botones con solo iconos a menudo necesitan `aria-label` para transmitir su propósito.

El atributo `aria-labelledby` hace exactamente lo mismo que el atributo `aria-label`, pero en lugar de definir el texto directamente en el atributo, se usa una referencia al texto que ya existe en la página. El texto existente debe tener un atributo `id`, que se usará como el valor de referencia en el atributo `aria-labelledby`.

```html
<input type="text" aria-labelledby="search-btn">
<button type="button" id="search-btn">Search</button>
```

También es posible combinar múltiples valores de `id` en un único valor de atributo `aria-labelledby`.

```html
<span id="volume-label">Volume</span>
<span id="volume-details">Adjust the volume level</span>
<input aria-labelledby="volume-label volume-details">
```

Una última nota, no uses `aria-label` y `aria-labelledby` en un elemento al mismo tiempo. En este caso, la etiqueta invisible para los lectores de pantalla siempre será determinada por `aria-labelledby` y `aria-label` será completamente ignorada.

## ¿Qué es el atributo aria-hidden y cómo funciona? ##

Si alguna vez necesita mostrar contenido mientras lo oculta al mismo tiempo. Solo necesita agregarlo al elemento HTML que desea ocultar y establecer su valor en `true`, como puede ver aquí: `aria-hidden="true"`.

Este atributo oculta el elemento y todos sus hijos del árbol de accesibilidad, manteniéndolos visibles en la página. Los casos de uso comunes incluyen:

- Iconos e imágenes que solo tienen un propósito decorativo.
- Contenido duplicado.

## ¿Qué es el atributo aria-describedby y cómo funciona? ##

Se utiliza para proporcionar información adicional sobre un elemento a usuarios de lectores de pantalla, haciendo referencia a contenido existente en la página.

El uso más común de `aria-describedby` es para asociar instrucciones y mensajes de error con campos de entrada de formularios. Debido a los varios métodos que tienen los usuarios de lectores de pantalla para navegar una página, es posible que se pierdan estos mensajes al moverse entre entradas. Usar `aria-describedby` ayuda a garantizar que los oigan.

```html
<form>
  <label for="password">Password:</label>
  <input type="password" id="password" aria-describedby="password-help" />
  <p id="password-help">Your password must be at least 8 characters long.</p>
</form>
```

Es más comúnmente utilizado para asociar instrucciones y mensajes de error con campos de entrada de formularios para reducir la posibilidad de que los usuarios de lectores de pantalla se pierdan estos mensajes mientras navegan por el formulario.

