# 33 - Trabajando con Formularios

## ¿Cómo funcionan los formularios, etiquetas y entradas en HTML?

El elemento `form` en HTML se utiliza para recopilar información del usuario, como nombres y correos electrónicos.
```html
<form action="url-va-aquí">
  <!-- los elementos input van aquí -->
</form>
```

El atributo `action` especifica dónde se enviarán los datos del formulario al enviarlo.

Para recopilar información específica, como nombres y correos electrónicos, se utilizaría el elemento `input`.
```html
<form action="">
  <input type="text" />
</form>
```

Los elementos `input` son elementos vacíos y no tienen etiquetas de cierre. El atributo `type` define el tipo de dato que se espera del usuario.
Para añadir una etiqueta para la entrada, se usaría un elemento `label`.
```html
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
```
Para asociar explícitamente una `label` con un `input`, se puede usar el atributo `for`.
```html
<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="example@email.com" />
</form>
```
Al usar una asociación explícita, los valores para los atributos `for` e `id` deben ser los mismos.
Si deseas mostrar sugerencias adicionales a los usuarios sobre la entrada esperada, puedes usar el atributo `placeholder`.


## ¿Cuáles son los diferentes tipos de botones y cuándo deberías usarlos?

El elemento `button` se utiliza para realizar una acción particular cuando se activa.
Otros ejemplos de uso del elemento `button` incluyen enviar un formulario, mostrar un modal, o alternar un menú lateral abierto y cerrado. El elemento `button` tiene un atributo `type` que controla el comportamiento del botón cuando se activa. El primer valor posible para el atributo `type` sería el tipo `button`.
```html
<button type="button">Show Alert</button>
```
Otro valor posible para el atributo `type` es el valor `submit`.
```html
<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="reset">Reset form</button>
  <button type="submit">Submit form</button>
</form>
```
El tercer valor posible para el atributo `type` es el valor `reset`.

Otra forma de crear botones en HTML es usando el elemento `input`. El elemento `input` también tiene un atributo type con los valores posibles de `submit`, `reset` y `button`. Aquí hay un ejemplo de uso del elemento `input` con el type establecido en `button`:
```html
<input class="start-btn" type="button" value="Start Game" />
```
El atributo `value` se usa para mostrar el texto del botón.

### ¿Qué diferencia hay entre un botón tipo `input` y otro tipo `button`?
Los elementos `input` son elementos vacíos, los que significa que no puede tener hijos, como texto, y solo puede tener una etiqueta de inicio. Por otro lado, el elemento `button` ofrece más flexibilidad porque puedes anidar texto, imágenes e íconos dentro de él.

## ¿Qué es la validación de formularios del lado del cliente en formularios HTML, y cuáles son algunos ejemplos?

Los formularios incorporan el uso del atributo `required` en `inputs`. El atributo `required` especifica que el usuario necesita completar esa parte del formulario antes de que se envíe.
```html
<form action="">
  <label for="email">Email Address (Required field):</label>
  <input
    required
    type="email"
    name="email"
    id="email"
    minlength="4"
    maxlength="64"
  />
  <button type="submit">Submit Form</button>
</form>
```
Otra ventaja de usar el `input` de correo electrónico es que los `inputs` de correo tienen una validación básica para asegurar que las direcciones de email estén correctamente formateadas.

Otras formas de validación para entradas de correo electrónico son usar los atributos `minlength` y `maxlength`. Se utilizan para establecer la longitud mínima y máxima en caracteres para la entrada de correo electrónico.


## ¿Cuáles son los diferentes estados del formulario y por qué son importantes?

Los `inputs` de los formularios pueden estar en diferentes etapas o condiciones como un estado `focus`, estado `readonly` o estado `disabled`.

Cuando el usuario hace clic en un control de formulario o lo selecciona con la tecla Tabulador del teclado, esto significa que está en el estado `focus`. La mayoría de los navegadores mostrarán un borde azul resaltado alrededor de la entrada.
```html
<input disabled type="email" name="email" id="email" />
```

```html
<input
  readonly
  type="email"
  name="email"
  id="email"
  value="example@email.com"
/>
```
Una diferencia clave entre el estado `disabled` y el estado `readonly` es que el estado `readonly` puede enfocarse mientras que el estado `disabled` no.
