import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'My Site'
author = 'Your Name'
release = '0.1'

extensions = ['myst_parser']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
