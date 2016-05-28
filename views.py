# coding: utf-8

from datetime import datetime
from flask import render_template
from app import app, pages

@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True, key=lambda page: page.meta['date'])
    author = app.config.get("AUTHOR")
    title = app.config.get("BLOG_TITLE")
    year = datetime.now().year

    return render_template('index.html', pages=sorted_posts, author=author, 
    	title=title, year=year)

@app.route('/<path:path>/')
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)