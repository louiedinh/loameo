#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Louie Dinh & Raymond Huang'
SITENAME = u'Loameo'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Vancity Buzz', 'http://www.vancitybuzz.com/'),)
          

# Social widget
SOCIAL = {'twitter': 'http://twitter.com/louiedinh',
          'linkedin': 'http://www.linkedin.com/profile/view?id=103017614'}

DEFAULT_PAGINATION = False

THEME = 'themes/built-texts'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

INDEX_SAVE_AS = 'blog.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

GOOGLE_ANALYTICS = 'UA-39716444-2'
TWITTER_USERNAME = "louiedinh"
DISQUS_SITENAME = "pythonpracticeprojects"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_EXCLUDES = ('pages', 'drafts')

EMAIL_SUBSCRIBE_URL = "http://eepurl.com/TWobf"
FORUMS_URL = ""

SITE_META_DESCRIPTION = "Loameo: Vancouver's Data Blog"

