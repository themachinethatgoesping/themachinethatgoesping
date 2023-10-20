# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder.

# -- Project information

import themachinethatgoesping

project = 'themachinethatgoesping'
copyright = '2022-2023, Ghent University'
author = 'themachinethatgoesping authors'

release = themachinethatgoesping.__version__
version = themachinethatgoesping.__version__

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    #'sphinx.ext.autodoc',
    #'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'autoapi.extension',
    'sphinx_design',
    'nbsphinx',
    'hoverxref',
    'sphinx.ext.mathjax',
]

exclude_patterns = ['_build', '**.ipynb_checkpoints']

#nbsphinx

#hoverxref
hoverxref_auto_ref = True

#autoapi
autoapi_type = 'python'
autoapi_dirs = ['../../python/stubs/themachinethatgoesping/']
autoapi_generate_api_docs = False


#autodoc
add_module_names = False
autodoc_member_order = 'bysource'
autodoc_default_flags = ['members']
autosummary_generate = True
python_use_unqualified_type_names = True

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
