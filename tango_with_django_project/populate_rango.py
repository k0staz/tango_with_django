import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial", "url":"http://docs.python.org/2/tutorial/", "views": 64},
        {"title":"How to Think like a Computer Scientist", "url":"http://www.greenteapress.com/thinkpython/", "views": 32},
        {"title":"Learn Python in 10 Minutes", "url":"http://www.korokithakis.net/tutorials/python/", "views": 16} 
    ]

    django_pages = [
        {"title":"Official Django Tutorial", "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 64},
        {"title":"Django Rocks", "url":"http://www.djangorocks.com/", "views": 32},
        {"title":"How to Tango with Django", "url":"http://www.tangowithdjango.com/", "views": 16} 
    ]

    other_pages = [
        {"title":"Bottle", "url":"http://bottlepy.org/docs/dev/", "views": 64},
        {"title":"Flask", "url":"http://flask.pocoo.org", "views": 32}
    ]

    pascal_pages = [
        {"title":"Free Pascal", "url":"https://www.freepascal.org/", "views": 64},
        {"title":"Pascal Tutorial", "url":"https://www.tutorialspoint.com/pascal/index.htm", "views": 32},
        {"title":"PascalProgramming", "url":"http://www.pascal-programming.info/index.php", "views": 16} 
    ]

    perl_pages = [
        {"title":"The Perl programming language", "url":"https://www.perl.org/", "views": 64},
        {"title":"Beginner's Introduction to Perl", "url":"https://www.perl.com/pub/2000/10/begperl1.html/", "views": 32},
        {"title":"The Perl for MS Windows", "url":"http://strawberryperl.com/", "views": 16} 
    ]

    prolog_pages = [
        {"title":"SWI-Prolog", "url":"https://www.swi-prolog.org/", "views": 64},
        {"title":"Visual Prolog", "url":"https://www.visual-prolog.com/", "views": 32},
        {"title":"Prolog Tutorial", "url":"https://www.cpp.edu/~jrfisher/www/prolog_tutorial/pt_framer.html", "views": 16} 
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
        "Pascal": {"pages": pascal_pages, "views": 34, "likes": 8},
        "Perl": {"pages": perl_pages, "views": 24, "likes": 4,
        "Prolog": {"pages": prolog_pages, "views": 10, "likes": 2}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script")
    populate()