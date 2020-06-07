# -- Path setup --------------------------------------------------------------
from pybtex.style.formatting.plain import Style as UpStyle
from pybtex.style.template import sentence, tag, names
from pybtex.plugin import register_plugin
from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title
import arxiv
import pickle

# -- Project information -----------------------------------------------------

project = 'Vincent Beffara'
copyright = '2020, Vincent Beffara'
author = 'Vincent Beffara'


# -- General configuration ---------------------------------------------------

extensions = ['sphinxcontrib.bibtex', 'sphinxcontrib.katex', 'sphinx_sass']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git']


# -- Options for HTML output -------------------------------------------------

html_favicon = '_static/favicon.png'
html_show_sourcelink = False
html_static_path = ['_static']
html_theme = 'basic'
html_title = project
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
    _, title, part = split_explicit_title(text)

    try:
        cache = pickle.load(open("arxiv.pickle", "rb"))
    except (IOError, ValueError, TypeError):
        cache = {}
    if part not in cache:
        cache[part] = arxiv.query(id_list=[part])[0]
        pickle.dump(cache, open("arxiv.pickle", "wb"))

    data = cache[part]
    a = nodes.strong("", ", ".join(data.authors) + ", ")
    t = nodes.emphasis("", data.title + ", ")
    l1 = nodes.reference(title, title, internal=False, refuri=data.arxiv_url)
    l2 = nodes.reference("[PDF]", "[PDF]", internal=False, refuri=data.pdf_url)
    return [a, t, l1, nodes.Text(" "), l2], []


def setup(app):
    app.connect('builder-inited',
                lambda app: app.add_role('arxiv', arxiv_role))
