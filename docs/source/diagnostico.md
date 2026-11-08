# 3. Diagnóstico de accesibilidad

## 3.1 Metodología

El diagnóstico se realizó mediante:

- Inspección visual de la interfaz.
- Pruebas de navegación mediante teclado.
- Identificación de los principios POUR afectados.
- Evaluación mediante WAVE.
- Revisión del código y validación HTML mediante W3C.

## 3.2 Resumen de barreras

| ID | Componente | Barrera identificada | Principio POUR |
|:---|:---|:---|:---|
| B-01 | Selección de perfil | Dificultad para navegar y seleccionar opciones mediante teclado. | Operable |
| B-02 | Botones radio | Interacción imprecisa y limitada a flechas de navegación al hacer uso del teclado. | Operable |


## 3.3 Resultados generales de WAVE

[Describir los errores, alertas y advertencias encontrados.]

![Resultados de WAVE](evidencias/wave-original.png)

*Figura 2. Evaluación de accesibilidad de la interfaz original.*

## 3.4 Validación inicial del código

[Incluir resultados del validador W3C.]

## 3.5 Análisis individual de las barreras

```{toctree}
:maxdepth: 1

B-01
B-02
```