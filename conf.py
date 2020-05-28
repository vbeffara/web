# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from pybtex.style.formatting.plain import Style as UpStyle
from pybtex.style.template import sentence, tag, names
from pybtex.plugin import register_plugin
from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title
import arxiv

# -- Project information -----------------------------------------------------

project = 'Vincent Beffara'
copyright = '2020, Vincent Beffara'
author = 'Vincent Beffara'


# -- General configuration ---------------------------------------------------

extensions = ['sphinxcontrib.bibtex', 'sphinxcontrib.katex', 'sphinx_sass']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git']


# -- Options for HTML output -------------------------------------------------

html_show_sourcelink = False
html_static_path = ['_static']
html_theme = 'basic'
pygments_style = 'monokai'

katex_options = r'''{
    delimiters: [
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true },
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
    ] }'''

sass_configs = [{'entry': "_templates/vb.scss", 'output': "basic.css"}]


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


def arxiv_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    has_explicit_title, title, part = split_explicit_title(text)
    print("Fetching arXiv " + part)
    data = arxiv.query(id_list=[part])[0]

    node = nodes.Text(", ".join(data.authors) + ", " + data.title + ", ")
    link1 = nodes.reference(
        title, title, internal=False, refuri=data.arxiv_url)
    link2 = nodes.reference(
        "[PDF]", "[PDF]", internal=False, refuri=data.pdf_url)
    return [node, link1, nodes.Text(" "), link2], []


def setup_link_role(app):
    app.add_role('arxiv', arxiv_role)


def setup(app):
    app.connect('builder-inited', setup_link_role)
