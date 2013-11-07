#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rodrigo Silveira'
SITENAME = u'Rodrigo Silveira'
SITESUBTITLE = u'Digressions on  life, web and stuff.'
SITEURL = 'http://rodlnx:8000'
DESCRIPTION = "Rodrigo Silveira's blog."
AVATAR_IMG = 'theme/img/avatar.jpeg'

MD_EXTENSIONS = ['codehilite', 'extra']
THEME = "ghostly"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATH = "pelican-plugins"
PLUGINS = [
    'assets',
    'minify',
]

FEED_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = 'tag/%s/feed.xml'
FEED_ALL_ATOM = TRANSLATION_FEED_ATOM = None

TWITTER_USERNAME = 'rodms10'
GITHUB_URL = 'https://github.com/rodms10'

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/README.md', 'README.md'),
)

TEMPLATE_PAGES = {
    'extra/404.html': '404.html',
}

DEFAULT_PAGINATION = False
OUTPUT_RETENTION = (".git")
DELETE_OUTPUT_DIRECTORY = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

DISQUS_SITENAME = 'rodms'
GOOGLE_ANALYTICS = 'UA-45383543-1'
