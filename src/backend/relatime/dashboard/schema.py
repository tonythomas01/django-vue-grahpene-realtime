import graphene

from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from dashboard.models import Snippet


class SnippetNode(DjangoObjectType):
    class Meta:
        model = Snippet
        interfaces = (Node, )
        filter_fields = ['title', 'code']


class Query(object):
    snippet = Node.Field(SnippetNode)
    all_snippets = DjangoFilterConnectionField(SnippetNode)


class ParentQuery(Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=ParentQuery)
