# -*- coding: utf-8 -*-

import os

REPO_NAME = "/"  # Used for FREEZER_BASE_URL
DEBUG = True
AUTHOR = {
	'name': 'Iury Alves',
	'twitter': 'https://twitter.com/IuryAlvesdeSouz',
	'github': 'https://github.com/IuryAlves',
	'email': 'iuryalves20.gmail.com'
}
BLOG_TITLE = "Iury's thoughts"

APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = APP_DIR
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_BASE_URL = REPO_NAME

FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'