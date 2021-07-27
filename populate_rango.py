#!/usr/bin/env python
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/'}]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/'}]

    other_pages = [{'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
                   {'title': 'Flask', 'url': 'http://flask.pocoo.org'}]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages}}

    # If you want to add more categories or pages, # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = default_views(cat.name)
    p.likes = default_likes(cat.name)
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def default_views(cat_name):
    if cat_name == "Python":
        return 128
    elif cat_name == "Django":
        return 64
    elif cat_name == "Other Frameworks":
        return 32
    else:
        return 0


def default_likes(cat_name):
    if cat_name == "Python":
        return 64
    elif cat_name == "Django":
        return 32
    elif cat_name == "Other Frameworks":
        return 16
    else:
        return 0


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
