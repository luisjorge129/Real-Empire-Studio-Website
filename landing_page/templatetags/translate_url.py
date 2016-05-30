from django import template
from django.utils import translation

register = template.Library()

@register.tag(name='translate_url')
def do_translate_url(path):
    language = translation.get_language()

    if language == 'en':
        language = 'es'
    elif language == 'es':
        language = 'en'

    translation.activate(language)

    newpath = '/' + language + path[3:]

    return newpath

@register.tag(name='language_label')
def language_label(path):
    language = translation.get_language()

    if language == 'en':
        language = 'English'
    elif language == 'es':
        language = 'Espanol'

    return language

register.filter('do_translate_url', do_translate_url)
register.filter('language_label', language_label)
