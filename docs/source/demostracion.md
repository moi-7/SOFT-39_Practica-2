# Demostración

## Videos

```{note}
La Información personal del usuario en los videos se removió con el fin de proteger sus datos.
```

El código muestra como añadir un color de fondo mientras el usuario navega con la tecla <code>TAB</code> en su teclado.

```css
li.ui-selectlistbox-item.ui-corner-all:focus-visible {
    background-color: #dedede;
}
```

#### Página de inicio

```{raw} html
<video controls controlslist="nodownload noremoteplayback" preload="metadata" width="100%" playsinline muted loading="lazy" poster="_static/images/inicio.png">
  <source src="_static/videos/inicio.mp4" type="video/mp4">
  Tu navegador no admite la reproducción de video.
</video>
```

#### Lista de factura
```{raw} html
<video controls controlslist="nodownload noremoteplayback" preload="metadata" width="100%" playsinline muted loading="lazy" poster="_static/images/tabla.png">
  <source src="_static/videos/tabla.mp4" type="video/mp4">
  Tu navegador no admite la reproducción de video.
</video>
```