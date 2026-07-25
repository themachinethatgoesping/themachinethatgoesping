# SPDX-FileCopyrightText: 2022 - 2026 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder.

# -- Project information

import datetime
import sys
from pathlib import Path

_source_dir = Path(__file__).parent.resolve()
sys.path.insert(0, str(_source_dir))

import themachinethatgoesping

from _generate_api_stubs import generate_api_stubs

project = 'themachinethatgoesping'
copyright = f'2022-{datetime.date.today().year}, Ghent University'
author = 'themachinethatgoesping authors'

release = themachinethatgoesping.__version__
version = themachinethatgoesping.__version__

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'autoapi.extension',
    'sphinx_design',
    'nbsphinx',
    'nbsphinx_link',
    'sphinx.ext.mathjax',
]

exclude_patterns = ['_build', '**.ipynb_checkpoints', '_autoapi_stubs']

# Suppress specific warnings from auto-generated docstrings and autoapi
# - docutils: C++ template parameter docstrings with special indentation
# - autoapi.python_import_resolution: internal module resolution in stubs
# - ref.python: duplicate cross-reference targets from re-exported symbols
suppress_warnings = ['docutils', 'autoapi.python_import_resolution', 'ref.python']

# -- Automatic API documentation (sphinx-autoapi) -----------------------------
# The C++ core is exposed via nanobind, so there are no importable .py sources.
# We regenerate a clean stub tree from the *installed* package at build time
# (see _generate_api_stubs.py). This keeps the API reference in sync with the
# documented release with zero manual maintenance and works out of the box on
# Read the Docs, where the package is installed from PyPI.
autoapi_type = 'python'
_autoapi_stub_root = generate_api_stubs(_source_dir)
if _autoapi_stub_root is not None:
    autoapi_dirs = [str(_autoapi_stub_root)]
    autoapi_generate_api_docs = True
else:
    # Fall back to whatever stubs are checked in so the build still succeeds.
    autoapi_dirs = ['../../python/stubs/']
    autoapi_generate_api_docs = False

autoapi_root = 'api'
autoapi_keep_files = False
autoapi_add_toctree_entry = False
autoapi_member_order = 'bysource'
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
]


#autodoc
add_module_names = False
autodoc_member_order = 'bysource'
autodoc_default_flags = ['members']
python_use_unqualified_type_names = True

# -- napoleon ----------------------------------------------------------------
# Render numpydoc "Attributes" sections as :ivar: fields instead of standalone
# `.. attribute::` directives. This avoids "duplicate object description"
# warnings when autoapi already documents the real attribute/property.
napoleon_use_ivar = True

# -- nbsphinx ----------------------------------------------------------------
# Tutorial notebooks are pulled in (via nbsphinx-link) from the external
# `tutorials` repository and ship with pre-computed outputs. We never execute
# them at build time: rendering the stored outputs keeps the build fast and
# reproducible, while the sphinx-book-theme still offers light interactivity on
# the already-rendered content.
nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}
intersphinx_disabled_domains = ['std']


templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
#html_theme = "pydata_sphinx_theme"
html_theme = 'sphinx_book_theme'
#html_theme = 'sphinx_pdj_theme'

#documentation for theme: https://sphinx-book-theme.readthedocs.io/en/latest/index.html

html_static_path = ['_static']
html_logo  = 'themachinethatgoesping.svg'
html_favicon = 'themachinethatgoesping.svg'
html_theme_options = {
    #'logo_only': False,
    "logo": {
        "text": "themachinethatgoesping\n"+themachinethatgoesping.__version__,
    },

    "repository_url": "https://github.com/themachinethatgoesping/themachinethatgoesping",
    "path_to_docs": "docs/source",
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,

    # "light_css_variables": {
    #     "color-brand-primary": "darkgray",
    #     "color-brand-content": "#008a9a",
    # },

    # "dark_css_variables": {
    #     "color-brand-primary": "lightgray",
    #     "color-brand-content": "#008a9a",
    # },
    #'display_version': False,
}
#html_title = 'themachinethat\ngoesping\n' + themachinethatgoesping.__version__

# -- Options for EPUB output
epub_show_urls = 'footnote'
