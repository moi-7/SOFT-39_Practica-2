# 5. Implementación

## 5.1 Entorno de implementación

**Lenguajes:** HTML, CSS y JavaScript.

**Intervención:** Modificación de componentes existentes
en la interfaz seleccionada.

## 5.2 Componentes modificados

| Componente | Tecnología | Modificación |
|---|---|---|
| Selección de perfil | HTML / CSS / JavaScript | Foco y selección mediante teclado. |
| Botones radio | HTML / CSS / JavaScript | Indicador de foco y activación mediante teclado. |

## 5.3 Atributos HTML

Se incorporó el atributo `tabindex` para permitir que
determinados elementos reciban el foco mediante teclado.

```html
<div class="elemento" tabindex="0"></div>
```

## 5.4 Indicadores visuales de foco
Se utilizaron los estados :focus-visible para diferenciar
visualmente los elementos que reciben el foco.

```css
.elemento:focus-visible {
    outline: 3px solid #2563eb;
    outline-offset: 3px;
}
```

### 5.5 Eventos de teclado
Se incorporaron listeners de JavaScript para gestionar
la activación de los componentes mediante las teclas
Espacio y Enter.

```js
const div = document.querySelector(".elemento");
```

### 5.6 Detalle de implementación
:maxdepth: 1

navegacion-teclado
indicadores-foco

## 5.7 Consideraciones técnicas
[Documentar decisiones de implementación, compatibilidad,
limitaciones y posibles mejoras.]

| Elemento | Responsabilidad |
|---|---|
| `tabindex="0"` | Incorpora el elemento al orden de navegación secuencial del teclado. |
| `:focus-visible` | Permite mostrar un indicador visual de foco. |
| `keydown` | Detecta las pulsaciones de teclado. |
| `event.preventDefault()` | Evita el comportamiento predeterminado cuando se necesita gestionar una activación personalizada. |
| `element.click()` | Activa el mecanismo de clic del elemento. |

**Una observación técnica que conviene incorporar al informe:** `tabindex="0"` y un listener `keydown` no garantizan por sí solos que un `div` se comporte como un botón o un grupo de opciones accesible. Si se implementa un control personalizado, también hay que comprobar su semántica, nombre accesible, estado y comportamiento esperado de teclado. Siempre que sea posible, es preferible conservar controles HTML nativos.

Por ejemplo, un botón radio nativo ya proporciona gran parte del comportamiento de teclado y semántica que tendrías que reconstruir manualmente.