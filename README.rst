django-versioned-media-tag
==========================

Django tag to include media files versioned with modification date.

Installation
============

#. Run ``python setup.py install`` or place versioned_media on your
   PYTHONPATH.
#. Add ``'versioned_media'`` to the ``INSTALLED_APPS``.

Usage
=====

Following template::

    {% load versioned_media %}
    {% versioned_media "styles.css" %}
    {% versioned_media "js/main.js" %}

Will render to this::

    http://example.com/static/styles.css?1280260290
    http://example.com/static/js/main.js?1280260305

If you want, you can change the format of generated urls. For example,
put this line to project's settings.py::

    VERSIONED_MEDIA_URL_TEMPLATE = '%(path)s%(name)s.ver%(version)d%(.ext)s'

And the mentioned template will render as::

    http://example.com/static/styles.ver1280260290.css
    http://example.com/static/js/main.ver1280260305.js

Related docs
============

http://developer.yahoo.com/performance/rules.html#expires
