# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sarah M Brown'
copyright = '2024, Sarah M Brown'
author = 'Sarah M Brown'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
    'sphinx.ext.intersphinx',
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
]

# "sphinxext.rediraffe",

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*",
        "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md", '_bibliography',
        '_data','_pages','_people','_projects']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/brownsarahm/",
  "navbar_end": ["icon-links" ],
  "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_persistent": [],
#   "footer_start": [], # "copyright", "sphinx-version"
#   "footer_end": [], #"theme-version"]
  "secondary_sidebar_items": [],
  "icon_links": [
        {
            # Label for this link
            "name": "Lab GitHub",
            # URL where the link will redirect
            "url": "https://github.com/ml4sts/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa fa-terminal",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "ORCiD",
            # URL where the link will redirect
            "url": "https://orcid.org/0000-0001-5728-0822",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-orcid",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
        
  ]
}




# html_favicon = "_static/favicon.ico"
html_title = project
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": [],
}
blog_baseurl = "https://brownsarahm.com"
blog_title = " Sarah M Brown"
blog_path = "news"
blog_feed_length = 5
fontawesome_included = True
blog_post_pattern = "news/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Bibliography and citations
bibtex_bibfiles = ["_static/papers.bib"]

# OpenGraph config
ogp_site_url = "https://sarahmbrown.org"
# ogp_image = "https://predictablynoisy.com/_static/profile-bw.png"

# Temporarily stored as off until we fix it
# jupyter_execute_notebooks = "off"

# rediraffe_redirects = {
# }

def setup(app):
    app.add_css_file("custom.css")
