from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        choices = 0
        for form in self.forms:
            dict = form.cleaned_data
            if dict.get('is_main'):
                choices += 1
        if choices == 0:
            raise ValidationError('Выберите главную тему')
        elif choices > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass





