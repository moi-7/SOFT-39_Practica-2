# Práctica 2 — Accesibilidad Web

Práctica académica desarrollada para el curso **Experiencia de Usuario e Interfaz de Usuario (UX/UI).**

## Descripción general

Esta práctica tiene como objetivo identificar barreras de accesibilidad en interfaces digitales y proponer soluciones basadas en las **Pautas de Accesibilidad para el Contenido Web (WCAG 2.1)**.

Se utiliza Sphinx para generar documentación técnica y uv para gestionar las dependencias y el entorno de Python.

## Tecnologías utilizadas

| Tecnología | Propósito |
|---|---|
| Python 3 | Lenguaje utilizado para la documentación |
| Sphinx | Generación de documentación |
| uv (Astral) | Gestión de dependencias y entornos virtuales |
| Markdown | Redacción de documentación |
| HTML CSS y JS | Estructura y presentación de interfaces |
| Git | Control de versiones |
| WAVE | Evaluación de accesibilidad |
| W3C Validator | Validación de estándares web |

## Requisitos previos

Instalar los siguientes programas:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/), mediante uv
- [uv de Astral](https://docs.astral.sh/uv/)
- [Sphinx](https://www.sphinx-doc.org/), mediante uv

Instalar uv en Linux o macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Comprobar la instalación:

```bash
uv --version
python3 --version
git --version
```

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

Instalar las dependencias declaradas en el proyecto:

```bash
uv sync
```

Si el repositorio incluye `uv.lock`, utilizar:

```bash
uv sync --locked
```

## Inicio rápido

Generar la documentación HTML:

```bash
uv run sphinx-build -b html docs/source docs/build/html
```

La documentación puede visualizarse directamente desde un navegador.

## Configuración

La configuración principal se administra mediante:

| Archivo | Función |
|---|---|
| `pyproject.toml` | Dependencias y configuración de Python |
| `uv.lock` | Versiones de dependencias |
| `docs/source/conf.py` | Configuración de Sphinx |
| `docs/source/index.md` | Página principal de la documentación |

Para crear un proyecto nuevo desde cero:

```bash
uv init --bare
uv add --dev sphinx
uv run sphinx-quickstart docs
```

Estos comandos son de inicialización y no deben ejecutarse nuevamente al clonar un repositorio que ya contiene la configuración.

## Comandos principales

### uv

```bash
uv sync                         # Instalar dependencias
uv add paquete                  # Agregar una dependencia
uv add --dev paquete            # Agregar dependencia de desarrollo
uv remove paquete               # Eliminar una dependencia
uv lock                         # Actualizar el archivo de versiones
uv run comando                  # Ejecutar dentro del entorno
uv tree                         # Mostrar el árbol de dependencias
uv python list                  # Mostrar versiones de Python disponibles
```

### Sphinx

```bash
# Crear la estructura inicial
uv run sphinx-quickstart docs

# Generar documentación HTML
uv run sphinx-build -b html docs/source docs/build/html

# Generar documentación PDF mediante LaTeX
uv run sphinx-build -b latex docs/source docs/build/latex

# Comprobar referencias y enlaces internos
uv run sphinx-build -b linkcheck docs/source docs/build/linkcheck

# Eliminar los archivos generados
rm -rf docs/build
```

La generación de PDF requiere una distribución de LaTeX compatible.

## Validación de accesibilidad

La evaluación se realiza mediante:

1. **WAVE:** identificación de errores y advertencias de accesibilidad.
2. **Validador W3C:** comprobación de la estructura y sintaxis HTML.
3. **WCAG 2.1:** evaluación de los principios perceptible, operable, comprensible y robusto.

Herramientas:

- [WAVE](https://wave.webaim.org/)
- [Validador W3C](https://validator.w3.org/)
- [WCAG 2.1](https://www.w3.org/TR/WCAG21/)

## Contribuciones

~~Para proponer modificaciones:~~

~~1. Crear una rama de trabajo.~~
~~2. Implementar y verificar los cambios.~~
~~3. Registrar los cambios mediante Git.~~
~~4. Enviar una solicitud de incorporación de cambios para su revisión.~~

~~Se recomienda mantener una estructura organizada y documentar las modificaciones importantes.~~

## Licencia

Este proyecto se distribuye bajo la **licencia MIT**.

Consulta el archivo `LICENSE` para conocer los términos y condiciones de uso, modificación y distribución.