# -- Path setup --------------------------------------------------------------

import os
import sys
from pybtex.style.formatting.plain import Style as UpStyle
from pybtex.style.template import sentence, tag, names
from pybtex.plugin import register_plugin

sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Vincent Beffara'
copyright = '2020, Vincent Beffara'
author = 'Vincent Beffara'


# -- General configuration ---------------------------------------------------

extensions = ['sphinxcontrib.bibtex', 'sphinxcontrib.katex']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_show_sourcelink = False
html_static_path = ['_static']
html_theme = 'basic'

katex_options = r'''{
    delimiters: [
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true },
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
    ] }'''


def sass(x, y, z):
    os.system("sass --no-source-map _static/basic.scss _static/basic.css")


class MyStyle(UpStyle):
    def __init__(self):
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence=True):
        formatted_names = names(role, sep=', ', sep2=' and ', last_sep=' and ')
        if as_sentence:
            return tag('b')[sentence[formatted_names]]
        else:
            return formatted_names


register_plugin('pybtex.style.formatting', 'mystyle', MyStyle)


def setup(app):
    app.connect('source-read', sass)
