import graphene
from graphene_django import DjangoObjectType, filter

from twitter.models import PostModel


class Post(DjangoObjectType):
    class Meta:
        model = PostModel
        interfaces = (graphene.relay.Node,)
        filter_fields = ['title', 'id']


class PostQuery(object):
    posts = filter.DjangoFilterConnectionField(Post)

