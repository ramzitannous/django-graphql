import graphene
import graphql_jwt
from graphene import ObjectType, Schema
from graphene_django.debug import DjangoDebug
from .person import PersonQuery, Person, PersonMutation
from .post import PostQuery, Post


class RootQuery(PersonQuery, PostQuery, ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


class AuthMutation:
    token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()


class RootMutation(PersonMutation, AuthMutation, ObjectType):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
