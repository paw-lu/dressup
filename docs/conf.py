"""Sphinx configuration."""
from datetime import datetime


project = "Dress up"
author = "Paulo S. Costa"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
html_theme = "material"
