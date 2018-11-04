import graphene
from graphene_django_subscriptions.subscription import Subscription
from dashboard.serializers import SnippetSerializer


class SnippetSubscription(Subscription):
    class Meta:
        serializer_class = SnippetSerializer
        stream = 'snippets'
        description = 'Snippet Subscription'
