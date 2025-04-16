# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath(".."))  # so autodoc finds your package

project = 'Intelligence Academy'
author  = 'Intelligence Academy'
release = '0.1'
version = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
]

autosummary_generate = True
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# MyST (Markdown) support
myst_enable_extensions = [
    'deflist',
    'colon_fence',
    'html_admonition',
    'html_image',
]

# HTML output
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "image_light": "logo-light.png",
        "image_dark": "logo-dark.png",
    },
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field.html", "navbar-icon-links"],
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
    "collapse_navigation": False,
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
}
html_css_files = ["css/custom.css"]
html_favicon = "_static/favicon.ico"
