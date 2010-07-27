import os

from django.conf import settings
from django import template


URL_TEMPLATE = getattr(settings, 'VERSIONED_MEDIA_URL_TEMPLATE',
                       '%(path)s%(name)s%(.ext)s?%(version)d')

register = template.Library()

@register.simple_tag
def versioned_media(path):
    """
    Allows auto versioning of files based on modification date.
    Usage::

        {% versioned_media "js/script.js" %}

    """
    fullpath = os.path.join(settings.MEDIA_ROOT, path)
    try:
        modification_time = os.path.getmtime(fullpath)
    except OSError:
        # file not found
        if settings.DEBUG:
            raise
        else:
            modification_time = 404 # be silent in production

    path, name = os.path.split(path)
    name, ext = os.path.splitext(name)
    if path:
        path += '/'
    url = URL_TEMPLATE % {'path': path, 'name': name, '.ext': ext,
                          'version': modification_time}
    return settings.MEDIA_URL + url
