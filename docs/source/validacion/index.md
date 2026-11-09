# 6. Validación de accesibilidad

Objetivo: demostrar que las soluciones funcionan y que las modificaciones no introdujeron nuevas barreras.

## 6.1 Metodología

La validación se realizó mediante herramientas automáticas
y pruebas manuales.

Se consideraron los siguientes mecanismos:

- WAVE: evaluación de errores y alertas de accesibilidad.
- W3C Validator: validación de la estructura HTML.
- Pruebas manuales: navegación e interacción mediante teclado.

## 6.2 Evaluación WAVE

### Interfaz original

[Describir los resultados obtenidos.]

![WAVE original](evidencias/wave-original.png)

### Interfaz modificada

[Describir los resultados después de implementar los cambios.]

![WAVE solución](evidencias/wave-solucion.png)

## 6.3 Validación W3C

| Elemento evaluado | Original | Modificado |
|---|---|---|
| Errores HTML | [Cantidad] | [Cantidad] |
| Advertencias | [Cantidad] | [Cantidad] |

[Incluir observaciones relevantes del validador.]

## 6.4 Pruebas manuales de teclado

| Prueba | Resultado esperado | Resultado obtenido |
|---|---|---|
| Presionar Tab | Recorrer los elementos interactivos. | [Resultado] |
| Presionar Espacio | Activar la opción enfocada cuando corresponda. | [Resultado] |
| Presionar Enter | Activar la opción cuando corresponda. | [Resultado] |
| Identificar el foco | Mostrar un indicador visual perceptible. | [Resultado] |
| Navegación secuencial | Mantener un orden lógico de navegación. | [Resultado] |

## 6.5 Resultado por componente

| ID | Componente | Estado | Observaciones |
|---|---|---|---|
| B-01 | Selección de perfil | [Estado] | [Observaciones] |
| B-02 | Botones radio | [Estado] | [Observaciones] |

## 6.6 Limitaciones

[Documentar problemas pendientes o aspectos que no pudieron
validarse completamente.]

```{note} Diferencia entre evaluación automática y manual
WAVE y W3C no sustituyen las pruebas de interacción mediante teclado. Una página puede no presentar errores automáticos y aun así contener barreras de operabilidad.
```