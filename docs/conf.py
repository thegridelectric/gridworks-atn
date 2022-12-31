"""Sphinx configuration."""
project = "Gridworks AtomicTNode"
author = "gridworks"
copyright = "2022, gridworks"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
