# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'themachinethatgoesping'
copyright = '2022, Ghent University'
author = 'themachinethatgoesping authors'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

#autodoc
add_module_names = False
autodoc_member_order = 'bysource'
python_use_unqualified_type_names = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}
intersphinx_disabled_domains = ['std']


templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_logo  = 'themachinethatgoesping.svg'
html_theme_options = {
    'logo_only': False,
    #'display_version': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
