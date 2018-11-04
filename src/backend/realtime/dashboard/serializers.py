from rest_framework.serializers import ModelSerializer
from dashboard.models import Snippet


class SnippetSerializer(ModelSerializer):
    class Meta:
        fields = ('__all__',)
        model = Snippet
