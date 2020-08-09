from django.contrib import admin

# Register your models here.
from twitter.models import PersonModel, PostModel

admin.site.register(PersonModel)
admin.site.register(PostModel)