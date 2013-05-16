#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'فامیل دور'
SITENAME = u'بلاگ من'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fa'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-sobhe'

import os
script_path = os.path.realpath(__file__)
blog_base_path = os.path.dirname(script_path)

PLUGIN_PATH = os.path.join(blog_base_path, 'plugins/')
PLUGINS = ['pelican-jalali']
