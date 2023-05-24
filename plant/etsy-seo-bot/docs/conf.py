# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Etsy SEO Bot'
copyright = '2023, Your Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
