# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import os
import sys
# If your code is in ../src, adjust as needed:
# sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------
project = 'Intelligence Academy'
author = 'Intelligence Academy'
copyright = '2025, Intelligence Academy'

# The full version, including alpha/beta/rc tags
release = '0.1'
version = '0.1.0'


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',      # support Google & NumPy docstrings
    'sphinx.ext.viewcode',      # link to highlighted source
    'myst_parser',              # optional: enable Markdown via MyST
]

autosummary_generate = True  # turn on autosummary

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for MyST parser ------------------------------------------------
myst_enable_extensions = [
    'deflist',
    'colon_fence',
    'html_admonition',
    'html_image',
]


# -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    # Logo (will switch based on user’s theme preference)
    "logo": {
        "image_light": "logo-light.png",
        "image_dark": "logo-dark.png",
    },
    # Navbar layout
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field.html", "navbar-icon-links"],
    # Icon links in the top-right nav bar
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourorg/intelligence-academy",
            "icon": "fab fa-github-square",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/intelligence-academy/",
            "icon": "fab fa-python",
        },
    ],
    # Keep left‑nav chapters collapsed until clicked
    "collapse_navigation": False,
    # Show page‑specific table of contents on the right
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
}

# Add any custom CSS overrides here
html_css_files = [
    "css/custom.css",
]

# Favicon
html_favicon = "_static/favicon.ico"


# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
