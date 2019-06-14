import re


def slugify(string):
    """
    Simplifies ugly strings into something URL-friendly.
    :param string:
    :return:
    """
    string = string.lower()
    for c in [' ', '-', '.', '/']:
        string = string.replace(c, '_')
    string = re.sub('\W', '', string)
    s = string.replace('_', ' ')
    string = re.sub('\s+', ' ', s)
    string = string.strip()
    string = string.replace(' ', '-')
    return string