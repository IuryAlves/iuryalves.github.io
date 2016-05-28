# -*- coding: utf-8 -*-

import os

REPO_NAME = "iuryalves.github.io"  # Used for FREEZER_BASE_URL
DEBUG = True
AUTHOR = {
	'name': 'Iury Alves',
	'twitter': 'https://twitter.com/IuryAlvesdeSouz',
	'github': 'https://github.com/IuryAlves',
	'email': 'iuryalves20@gmail.com'
}
BLOG_TITLE = "Iury's thoughts"

APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = APP_DIR
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'