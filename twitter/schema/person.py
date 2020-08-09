from graphene import relay
from graphene_django import DjangoObjectType, filter
from twitter.models import PersonModel
from django_filters import FilterSet, OrderingFilter
from graphene_django_cud import mutations


class PersonFilterSet(FilterSet):
    class Meta:
        model = PersonModel
        fields = ['first_name', 'last_name', 'id']

    order_by = OrderingFilter(
        fields=(
            ('id', 'first_name'),
        )
    )


class Person(DjangoObjectType):
    class Meta:
        model = PersonModel
        interfaces = (relay.Node,)


class PersonQuery(object):
    people = filter.DjangoFilterConnectionField(Person, filterset_class=PersonFilterSet)


class CreatePersonMutation(mutations.DjangoCreateMutation):
    class Meta:
        model = PersonModel


class PatchPersonMutation(mutations.DjangoPatchMutation):
    class Meta:
        model = PersonModel
        return_field_name = "Person"


class PersonMutation(object):
    create_person = CreatePersonMutation.Field()
    update_person = PatchPersonMutation.Field()
