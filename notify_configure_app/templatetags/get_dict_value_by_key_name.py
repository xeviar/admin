from django import template

register = template.Library()

def key(d, key_name):
    try:
        return d[key_name]
    except:
        return 'KEY_TOBE_IGNORED'
key = register.filter('key', key)

