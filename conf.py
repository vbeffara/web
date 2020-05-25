# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Vincent Beffara'
copyright = '2020, Vincent Beffara'
author = 'Vincent Beffara'


# -- General configuration ---------------------------------------------------

extensions = ['sphinx_rtd_theme',
              'sphinxcontrib.bibtex',
              #   'sphinxcontrib.katex',
              'theme']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_show_sourcelink = False
html_static_path = ['_static']
html_theme = 'vb'
html_theme_options = {'prev_next_buttons_location': None}

katex_options = r'''{
    delimiters: [
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true },
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
    ] }'''
