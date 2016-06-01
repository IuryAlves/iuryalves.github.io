# coding: utf-8

import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(project_path)

import main


if __name__ == '__main__':
	app = main.app
	PORT =  8080
	HOST = '0.0.0.0'
	app.run(host=HOST, port=PORT)