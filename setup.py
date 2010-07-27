from distutils.core import setup

setup(name='django-versioned-media-tag',
      version='0.2',
      url='http://github.com/alexvasi/django-versioned-media-tag',
      description='Django tag to include media files versioned with modification date.',
      packages=['versioned_media', 'versioned_media.templatetags'])
