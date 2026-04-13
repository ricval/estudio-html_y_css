# Capítulo 04 - HTML y CSS Avanzado

## 04.01 - Formularios e _Inputs_ de Usuario

### 04.01.01 - Creando los Formularios HTML

#### Estructura y sintaxis para un Formulario

En HTML los formularios se declaran con el elemento `<form>...</form>` encapsulado varios elementos _input_.

```html
<form action="/submit" method="post">
    <!-- Los elementos input van aquí -->
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Enviar</button>
</form>
```

- El atributo `action` especifica la URL a donde se enviara la información.
- El atributo `method` especifica el método HTTP que se utilizará para el envío, (ejem. `GET` o `POST`).

#### Campos Input, Textareas y Botones

Hay una diversidad de elementos _input_ para diferentes 