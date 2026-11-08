# Solución

## Videos

```{note}
La Información personal del usuario en los videos se removió con el fin de proteger sus datos.
```

El código muestra como añadir un color de fondo mientras el usuario navega con la tecla <code>TAB</code> en su teclado.

```css
li.ui-selectlistbox-item:focus-visible {
    background-color: #dedede;
}
```

El código agrega la funcionalidad de usar los botones <code>Enter</code> y <code>Space</code> como selectores.

```js
const lista = document.querySelector(".ui-selectlistbox-list"); 

lista.addEventListener("keydown", (event) => { 
    const li = event.target.closest(".ui-selectlistbox-item"); 
    if (!li) return; 
    
    if (event.key === " " || event.key === "Enter") { 
        event.preventDefault(); 
        
        // 1. Clear styling from all items first
        const allItems = lista.querySelectorAll(".ui-selectlistbox-item");
        allItems.forEach(item => {
            item.style.color = "";
            item.style.backgroundColor = "";
        });

        // 2. Click and style the newly selected item
        li.click(); 
        li.style.color = "white"; 
        li.style.backgroundColor = "#42a5f5";
    } 
});
```

#### Página de inicio

```{raw} html
<video controls controlslist="nodownload noremoteplayback" preload="metadata" width="100%" playsinline muted loading="lazy" poster="_static/images/inicio-fixed.png">
  <source src="_static/videos/inicio-fixed.mp4" type="video/mp4">
  Tu navegador no admite la reproducción de video.
</video>
```

#### Lista de factura

```js
const boxes = document.querySelectorAll(".ui-radiobutton-box");

boxes.forEach((box) => {
  box.addEventListener("keydown", (event) => {
    const radio = box.querySelector(".ui-radiobutton-icon");
    if (!radio) return;

    if (event.key === " " || event.key === "Space" || event.key === "Enter") {
      event.preventDefault();
      radio.click();
    }
  });
});
```

```{raw} html
<video controls controlslist="nodownload noremoteplayback" preload="metadata" width="100%" playsinline muted loading="lazy" poster="_static/images/tabla-fixed.png">
  <source src="_static/videos/tabla-fixed.mp4" type="video/mp4">
  Tu navegador no admite la reproducción de video.
</video>
```