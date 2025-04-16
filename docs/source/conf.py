# -- Path setup --------------------------------------------------------------

import os
import sys
# If your extensions (or modules to document) are in ../src, adjust as needed:
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "Shaping the Future with AI & Technology!"
author = "Mejbah Ahammad"
# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",      # core: automatically document docstrings
    "sphinx.ext.napoleon",     # support for NumPy/Google style docstrings
    "sphinx.ext.viewcode",     # add links to highlighted source code
    "myst_parser",             # parse Markdown files via MyST
    "sphinx.ext.intersphinx",  # link to other projects’ docs (e.g. Python)
]

# Paths that contain templates, relative to this directory.
templates_path = ["_templates"]

# Patterns to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for MyST parser ------------------------------------------------

myst_enable_extensions = [
    "deflist",
    "colon_fence",
    "html_admonition",
    "html_image",
]


# -- Options for HTML output -------------------------------------------------

# Choose a modern theme:
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel.
html_theme_options = {
    # Logos
    "logo": {
        "image_light": "logo-light.png",
        "image_dark": "logo-dark.png",
    },
    # Navbar configuration
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field.html", "navbar-icon-links"],
    # Add external links/icon buttons
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourorg/ia-ai",
            "icon": "fab fa-github-square",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/intelligence‑academy‑ai/",
            "icon": "fab fa-python",
        },
    ],
    # Keep the "Chapters" dropdown collapsed by default
    "collapse_navigation": False,
    # Secondary sidebar items
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
}

# Paths that contain custom static files (such as style sheets), relative to this directory.
html_static_path = ["_static"]

# Additional CSS files (e.g. to override or extend the theme)
html_css_files = [
    "css/custom.css",
]

# Favicon and site icon
html_favicon = "_static/favicon.ico"


# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
