import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from blog.models import Category, Page
import random

def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def change_views_and_likes(cat, vi, li):
    # likes, views in Pagemodel
    # for c in Category.objects.all():
    #     if c.name == cat:
    #         for p in Page.objects.filter(category=c):
    #             p.views = vi
    #             p.likes = li
    #             print vi, li
    #             p.save()
    #             print 'save'
    #     else:
    #         pass
    for c in Category.objects.all():
        if c.name == cat:
            c.views = vi
            c.likes = li
            c.save()
            print 'save ok'

def add_page_views(num=1, title= None):

    if not title:
        page = Page.objects.all()
        num = random.randrange
        for p in page:
            p.views = num(1, 100)
            p.save()
    else:
        page = Page.objects.get(title=title)
        page.views += num
        page.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting BLog population script..."
    # populate()
    # change_views_and_likes('Django', 64, 32)
    # change_views_and_likes('Python', 128, 64)
    # change_views_and_likes('Other Frameworks', 32, 16)
    add_page_views()
