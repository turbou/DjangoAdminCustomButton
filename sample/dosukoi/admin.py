from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Oyoyo

@admin.register(Oyoyo)
class OyoyoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/my_change_form.html'
    search_fields = ('name',)
    list_display = ('name',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.save_on_top = False
        self.save_as = False
        extra_context = extra_context or {}
        extra_context['can_custom1'] = True
        extra_context['can_custom2'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

