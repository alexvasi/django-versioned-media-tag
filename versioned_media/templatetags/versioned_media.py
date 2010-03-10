import os
from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def versioned_media(path):
    """Allows auto versioning of files based on modification times.
    Example: {% versioned_media "script.js" %} returns '/site_media/script.js?1217877755'
    """
    modification_time = os.path.getmtime(os.path.join(settings.MEDIA_ROOT, path))
    return "".join([settings.MEDIA_URL, path, "?%d" % int(modification_time)])
