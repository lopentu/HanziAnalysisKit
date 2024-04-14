import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

sys.path.insert(0, str(CURRENT_DIR.parent.parent))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "HanziAnalysisKit"
copyright = "2024, lope"
author = "lope"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "numpydoc",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["build", ".DS_Store"]
exclude_trees = [".build"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # alabaster
import sphinx_rtd_theme

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_copy_source = True

html_static_path = ["_static"]

html_css_files = ["custom.css"]
