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

project = 'AM3 test documentation'
copyright = '2023, Annika'
author = 'Annika'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [	'myst_parser', 
				'sphinx.ext.mathjax',
			    "sphinx.ext.napoleon",
			    "sphinx.ext.autodoc",
 				"sphinx_rtd_dark_mode",
 				'sphinx.ext.autosectionlabel',
 				"nbsphinx"
 			]

napoleon_google_docstring = True
napoleon_use_param = False


default_dark_mode = True

source_suffix = [
    ".md",
    ".rst",
    ".txt",
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]

sphinx_gallery_conf = {
    "default_thumb_file": "media/logo.png"
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_dark_mode'

html_theme_options = {
    "logo_only": False,
    "display_version": False,
    "collapse_navigation": True,
    "navigation_depth": 4,
    "prev_next_buttons_location": "bottom",  # top and bottom
}

html_logo = "media/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
