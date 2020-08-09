from django.db import models


class PersonModel(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()


class PostModel(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
