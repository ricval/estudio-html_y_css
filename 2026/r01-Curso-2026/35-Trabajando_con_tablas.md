# 35 - Trabajando con Tablas

## ¿Para qué se usan las tablas HTML y para qué no deben usarse?

La tabla tiene un elemento de encabezado, `thead`, un elemento de cuerpo de tabla, `tbody`, y un pie de tabla, `tfoot`.

Los elementos de encabezado, cuerpo y pie de tabla pueden contener cierta cantidad de filas de tabla, `tr`. Y cada fila de tabla puede contener un encabezado de tabla, `th`, que etiqueta los datos en esa fila. También puede contener cierta cantidad de celdas de datos individuales, llamadas datos de tabla, `td`.

```html
<table>
  <thead>
    <tr>
      <th>The title of this table</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First Row</th>
      <td>
        First Data Cell
      </td>
    </tr>
    <tr>
      <th>Second Row</th>
      <td>
        Second Data Cell
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th>The footer of this table, which might contain date of publication, author credits, or other meta information.</th>
    </tr>
  </tfoot>
</table>
```

Hace muchos años, los desarrolladores podrían haber utilizado un `table` para posicionar elementos no relacionados con datos en una página web. Hoy en día, los desarrolladores usan CSS flexbox y grid para estructurar sus diseños.

Por ahora, solo usa tablas HTML para su propósito original: mostrar datos tabulares.

