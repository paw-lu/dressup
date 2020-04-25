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
html_theme = "sphinx_material"
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Project Name",
    # Set you GA account ID to enable tracking
    "google_analytics_account": "UA-XXXXX",
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://project.github.io/project",
    # Set the color and the accent color
    "color_primary": "blue",
    "color_accent": "light-blue",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/project/project/",
    "repo_name": "Project",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 3,
    # If False, expand all TOC entries
    "globaltoc_collapse": False,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
}
