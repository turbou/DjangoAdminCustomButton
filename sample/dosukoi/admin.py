from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Oyoyo

@admin.register(Oyoyo)
class OyoyoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/my_change_form.html'
    search_fields = ('name',)
    list_display = ('operation', 'name',)

    def operation(self, obj):
        str_buffer = []
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="修正" name="edit" value="0">修正</button>')
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="更新承認" name="edit" value="0">更新承認</button>')
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="営業承認" name="edit" value="0">営業承認</button>')
        return mark_safe('<div class="bootstrap">%s</div>' % ('&nbsp;&nbsp;'.join(str_buffer)))
    operation.short_description = '操作'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.save_on_top = False
        self.save_as = False
        extra_context = extra_context or {}
        extra_context['can_custom1'] = True
        extra_context['can_custom2'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    class Media:
        css = {
            "all": ("bootstrap/css/mybootstrap.css",)
        }
        js = ('bootstrap/js/bootstrap.min.js',)

