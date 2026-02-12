# 15 - Trabajando con imágenes y SVGs

## ¿Cuáles son formas comunes de optimizar los activos de medios?

Los dos formatos más utilizados son PNG y JPG, pero ahora los nuevos formatos incluyen WEBP o AVIF.

## ¿Qué son los SVG y cuándo deberías usarlos?

Los formatos de imagen comunes como PNG y JPG están clasificados como formatos rasterizados.

SVG significa gráfico vectorial escalable. Se puede escalar a cualquier tamaño sin afectar la calidad.

Los SVG tienen específicamente el beneficio adicional de almacenar datos en XML.

**Ejemplo:**
```html
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="45" stroke="black" stroke-width="4" fill="yellow" />
  <circle cx="35" cy="40" r="5" fill="black" />
  <circle cx="65" cy="40" r="5" fill="black" />
  <path d="M35 65 Q50 80 65 65" stroke="black" stroke-width="4" fill="transparent" />
</svg>
```

Una de las bibliotecas de íconos más populares, **Font Awesome**, usa imágenes SVG para sus íconos.