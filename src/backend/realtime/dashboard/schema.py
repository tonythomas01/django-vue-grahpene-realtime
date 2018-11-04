import graphene

from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from dashboard.subscriptions import SnippetSubscription
from dashboard.models import Snippet


class SnippetNode(DjangoObjectType):
    class Meta:
        model = Snippet
        interfaces = (Node, )
        filter_fields = ['title', 'code']


class SnippetSubscriptions(graphene.ObjectType):
    snippet_subscription = SnippetSubscription.Field()


class Query(object):
    snippet = Node.Field(SnippetNode)
    all_snippets = DjangoFilterConnectionField(SnippetNode)


class ParentQuery(Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

class ParentSubscription(SnippetSubscriptions, graphene.ObjectType):
    class Meta:
        description = 'Parent definition of snippet subscriptions'

schema = graphene.Schema(
    query=ParentQuery, subscription=ParentSubscription
)
