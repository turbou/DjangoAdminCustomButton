from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Oyoyo

@admin.register(Oyoyo)
class OyoyoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/my_change_form.html'
    search_fields = ('name',)
    list_display = ('operation', 'name', 'app_status')
    list_filter = ('app_status',)
    fieldsets = [
        (None, {'fields': [
            ('name', 'app_status'),
        ]}),
    ]

    def operation(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        str_buffer = []
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="修正" name="edit" onclick="location.href=\'%s?mode=update\'">修正</button>' % url)
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="更新承認" name="edit" onclick="location.href=\'%s?mode=upauth\'">更新承認</button>' % url)
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary" title="営業承認" name="edit" onclick="location.href=\'%s?mode=bzauth\'">営業承認</button>' % url)
        return mark_safe('<div class="bootstrap">%s</div>' % ('&nbsp;&nbsp;'.join(str_buffer)))
    operation.short_description = '操作'

    def get_list_display_links(self, request, list_display):
        return None

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.save_on_top = False
        self.save_as = False
        extra_context = extra_context or {}
        if 'mode' in request.GET:
            mode = request.GET.get('mode')
            if mode == 'update':
                extra_context['can_update'] = True
            elif mode == 'upauth':
                extra_context['can_upauth'] = True
            elif mode == 'bzauth':
                extra_context['can_bzauth'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    class Media:
        css = {
            "all": ("bootstrap/css/mybootstrap.css",)
        }
        js = ('bootstrap/js/bootstrap.min.js',)

