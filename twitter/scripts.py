import os
os.environ["DJANGO_SETTINGS_MODULE"] ="posts.settings"

import django
django.setup()

from twitter.models import PersonModel, PostModel

person = [{
    "first_name": "ramzi",
    "last_name": "tannous",
    "age": 23,
}, {
    "first_name": "samuel",
    "last_name": "tannous",
    "age": 18,
}, {
    "first_name": "randa",
    "last_name": "tannous",
    "age": 18,
},
    {
        "first_name": "maher",
        "last_name": "tannous",
        "age": 25,
    },
    {
        "first_name": "julie",
        "last_name": "tannous",
        "age": 25,
    },
]

posts = [
    {"title": "hello1", "content": "test post 1", "author_id": 1},
    {"title": "hello2", "content": "test post 1", "author_id": 1},
    {"title": "hello23", "content": "test post sdf1", "author_id": 2},
    {"title": "hello23", "content": "test post 1sdf", "author_id": 2},
    {"title": "hello3e23", "content": "test post dfgdf1", "author_id": 3},
    {"title": "helloqwer", "content": "test post dfg1", "author_id": 3},
]

def create_people():
    for p in person:
        people = PersonModel.objects.create(**p)
        people.save()

def create_posts():
    for post in posts:
        p = PostModel.objects.create(**post)
        p.save()

create_people()
create_posts()