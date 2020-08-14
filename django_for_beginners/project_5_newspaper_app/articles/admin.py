from django.contrib import admin

# Register your models here.
from . import models


class CommentInline(admin.StackedInline):
    model = models.Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
