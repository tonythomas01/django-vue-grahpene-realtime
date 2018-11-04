from graphene_django_subscriptions.consumers import GraphqlAPIDemultiplexer
from channels.routing import route_class
from dashboard.subscriptions import SnippetSubscription


class CustomAppDemultiplexer(GraphqlAPIDemultiplexer):
    consumers = {
      'snippets': SnippetSubscription.get_binding().consumer,
    }


app_routing = [
    route_class(CustomAppDemultiplexer)
]
