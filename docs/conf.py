"""Configuration file controlling how sphinx builds VietFin documentation."""

import vietfin

import os
import sys


# source: <https://github.com/lepture/shibuya/blob/master/docs/conf.py>
# <https://github.com/theOGognf/finagg/blob/main/docs/conf.py>
# <https://github.com/pradyunsg/furo/blob/main/docs/conf.py>

# -- Path setup --------------------------------------------------------------

# __location__ = os.path.dirname(__file__)
# sys.path.insert(0, os.path.join(__location__, "../src"))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information ------------------------------------------------------

project = "VietFin"
copyright = "Copyright &copy; 2023, Huy"
author = "Huy"

version = vietfin.__version__
release = version

# -- General configuration ----------------------------------------------------

extensions = [
    # Sphinx's own extensions
    # "sphinx.ext.autodoc",  # integrate function signatures and docstring from code base into docs
    "sphinx.ext.napoleon",  # enables sphinx to parse numpydoc style docstrings
    "sphinx.ext.viewcode",  # adds a helpful link to the source code of each object in the API reference sheet
    # "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",  # shorten external links that point to URLs on one and the same site
    # "sphinx.ext.todo",
    # "sphinx.ext.autosummary",
    # Third-party extensions
    "sphinxcontrib.mermaid",  # embed Mermaid graphs
    "myst_parser",  # parse markdown files
    # "myst_nb",  # parse ipynb files
    "nbsphinx",  # works with Shibuya theme better than myst-nb
    # "sphinx_sitemap",
    "sphinx_design",  # adds more web components, replace features of sphinx_togglebutton, sphinx_inline_tabs
    "sphinx_copybutton",  # adds a copy button to the code blocks
    # "sphinx-hoverxref",  # show a floating window (tooltips or modal dialogues) on the cross references 
    # "autoapi.extension",  # parse source code and docstrings to create an API reference sheet
    # "autodoc2",  # replace sphinx.ext.autodoc
]

exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for myst-parser ----------------------------------------------------

# Enable the use of regular markdown syntax with mermaid instead of {mermaid} in mermaid codeblock.
myst_fence_as_directive = ["mermaid"]

# -- Options for sphinxcontrib.mermaid ----------------------------------------------------

# # Enable the use of mermaid-cli to render mermaid diagram as svg/png format
# mermaid_cmd = "C:\\Users\\huytr\\AppData\\Roaming\\npm\\mmdc.cmd"
# mermaid_cmd_shell = True

# Force the output for Mermaid diagram as raw-html/svg/png when building HTML files
mermaid_output_format = "raw"

# disable nbsphinx from loading RequireJS. Without this option, nbsphinx breaks sphinxcontrib-mermaid to not render mermaid diagram as raw html
nbsphinx_requirejs_path = ''

# -- Options for extlinks ----------------------------------------------------

extlinks = {
    'pull': ('https://github.com/vietfin/vietfin/pull/%s', 'pull request #%s'),
    'issue': ('https://github.com/vietfin/vietfin/issues%s', 'issue #%s'),
}

# -- Options for HTML output -------------------------------------------------

html_title = "VietFin"
html_theme = "shibuya"
html_logo = "_static/logo.jpg"

html_static_path = ["_static"]
# html_extra_path = ["_public"]

html_favicon = "_static/favicon/favicon.ico"

html_theme_options = {
   "accent_color": "blue",
   "dark_code": True,
   "toctree_collapse": False,
   "globaltoc_expand_depth": 1,
}

# Shibuya theme - Add an “Edit This Page” link
html_context = {
    "source_type": "github",
    "source_user": "vietfin",
    "source_repo": "vietfin",
    "source_version": "dev",  # branch name to use with this button # optional
    "source_docs_path": "/docs/",  # docs source directory # optional
}

# -- Options for sphinx_sitemap ----------------------------------------------------

# html_baseurl = "https://shibuya.lepture.com/"
# sitemap_url_scheme = "{link}"

# -- Options for myst-nb ------------------------------

# # explain: https://myst-nb.readthedocs.io/en/v0.9.0/use/execute.html#triggering-notebook-execution
# jupyter_execute_notebooks = "auto"

# # explain: https://myst-nb.readthedocs.io/en/v0.9.0/use/execute.html#dealing-with-code-that-raises-errors 
# execution_allow_errors=True

# myst_enable_extensions = [
#     "amsmath",
#     "colon_fence",
#     "deflist",
#     "dollarmath",
#     "html_image",
# ]
# myst_url_schemes = ("http", "https", "mailto")

# -- Options for autoapi ----------------------------------------------------

# autoapi_dirs = ["../src"]  # location to parse for API reference

# -- Options for autodoc2 -------------------------------------------------

# autodoc2_packages = [
#     {
#         "path": "../src/vietfin/",
#         "auto_mode": True,
#     },
# ]

# autodoc2_render_plugin = "myst"