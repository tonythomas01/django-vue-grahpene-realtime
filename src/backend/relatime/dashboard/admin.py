from django.contrib import admin
from dashboard.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Snippet, SnippetAdmin)
