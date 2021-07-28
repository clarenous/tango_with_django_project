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

    # golang_pages = [{'title': 'The Golang Programming Language', 'url': 'https://golang.org'},
    #                 {'title': 'Learn Go Programming', 'url': 'https://golangr.com'},
    #                 {'title': 'Beego Framework', 'url': 'https://beego.me'}]
    #
    # rust_pages = [{'title': 'Rust Programming Language', 'url': 'https://www.rust-lang.org'},
    #               {'title': 'Learning Rust', 'url': 'https://learning-rust.github.io'}]
    #
    # swift_pages = [{'title': 'Swift - Apple Developer', 'url': 'https://developer.apple.com/swift/'},
    #                {'title': 'About Swift', 'url': 'https://docs.swift.org/swift-book/'}]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages},
            # 'Golang': {'pages': golang_pages},
            # 'Rust': {'pages': rust_pages},
            # 'Swift': {'pages': swift_pages},
            }

    # If you want to add more categories or pages, # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], default_views(cat))

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = default_views(name)
    c.likes = default_likes(name)
    c.save()
    return c


def default_views(cat_name):
    views_by_names = {
        "Python": 128,
        "Django": 64,
        "Other Frameworks": 32,
        "Golang": 120,
        "Rust": 60,
        "Swift": 20,
    }
    return views_by_names[cat_name]


def default_likes(cat_name):
    likes_by_names = {
        "Python": 64,
        "Django": 32,
        "Other Frameworks": 16,
        "Golang": 70,
        "Rust": 30,
        "Swift": 10,
    }
    return likes_by_names[cat_name]


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
