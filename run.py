# coding: utf-8

import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(project_path)

import main


if __name__ == '__main__':
	app = main.app
	port =  os.getenv("PORT", 5000)
	host = os.getenv("HOST", "localhost")
	debug = os.getenv("DEBUG", False)
	app.run(host=host, port=port, debug=debug)