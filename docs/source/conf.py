# Project information

project = "CCSS - Accesibilidad Web"
author = "Moisés Reyes"
release = "1.0"

# General configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]

exclude_patterns = []

# Source files

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Language

language = "es"

# HTML configuration

html_theme = "furo"

html_title = "Práctica 2"

html_static_path = ["_static"]

html_theme_options = {
    "navigation_with_keys": True,
}