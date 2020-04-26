"""Sphinx configuration."""
from datetime import datetime
from typing import Dict


project = "Dress up"
author = "Paulo S. Costa"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.linkcode",
    "sphinx.ext.napoleon",
]
html_favicon = "images/dress.svg"


def linkcode_resolve(domain: str, info: Dict[str, str]) -> str:
    """Link documentation code to GitHub.

    Args:
        domain (str): The language of the object ("py").
        info (Dict[str, Any]): Information about the object. Keys are
            "module" and "fullname".

    Returns:
        str: The address of the hosted code.
    """
    filename = info["module"].replace(".", "/")
    return f"https://github.com/pscosta5/dressup/tree/master/src/{filename}.py"


html_theme = "sphinx_material"
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
html_theme_options = {
    "nav_title": "Dress up",
    "touch_icon": "images/dress.svg",
    "repo_url": "https://github.com/pscosta5/dressup",
    "repo_name": "Dress up",
    "repo_type": "github",
    "base_url": "https://dressup.readthedocs.io/en/latest/",
    "globaltoc_depth": 2,
    "theme_color": "#7e57c2",
    "color_primary": "deep-purple",
    "color_accent": "teal",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#x1F457",
    "master_doc": False,
    "nav_links": [
        {"href": "index", "internal": True, "title": "Dress up"},
        {"href": "reference", "internal": True, "title": "Documentation"},
        {
            "href": "https://github.com/pscosta5/dressup/releases",
            "internal": False,
            "title": "Changelog",
        },
    ],
    "heroes": {
        "index": "Dress up your unicode.",
        "customization": "Configuration options to personalize your site.",
    },
    "version_dropdown": True,
    "version_info": {"Release": "https://dressup.readthedocs.io/en/latest/"},
    "table_classes": ["plain"],
}
