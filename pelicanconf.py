#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-clean-blog'

AUTHOR = 'Justin Lillico'
SITENAME = 'justinlillico.com'
SITEURL = ''
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/Apoc182'),
          ('github', 'https://github.com/Apoc182'),
          ('facebook','https://www.facebook.com/Apocolyptic'))

DEFAULT_PAGINATION = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
