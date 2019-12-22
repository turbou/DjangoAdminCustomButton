from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Oyoyo

class OyoyoAdminForm(forms.ModelForm):
    updated_at_chk = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['updated_at_chk'].initial = self.instance.updated_at
        self.fields['name'].widget.attrs = {'size':30, 'placeholder':'名前'}

    def clean(self):
        cleaned_data = super().clean()
        if self.instance.id:
            oldobj = self._meta.model.objects.get(pk=self.instance.id)
            if str(oldobj.updated_at) != cleaned_data['updated_at_chk']:
                raise forms.ValidationError('他の誰かが変更を加えています。開き直してから再度、保存してください。')

@admin.register(Oyoyo)
class OyoyoAdmin(admin.ModelAdmin):
    form = OyoyoAdminForm
    change_form_template = 'admin/my_change_form.html'
    search_fields = ('name',)
    list_display = ('operation', 'name', 'app_status', 'updated_at')
    list_filter = ('app_status',)
    fieldsets = [
        (None, {'fields': [
            ('name', 'app_status', 'updated_at_chk',),
        ]}),
    ]

    def operation(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        str_buffer = []
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary list_button" title="修正" name="edit" onclick="location.href=\'%s?mode=update\'">修正</button>' % url)
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary list_button" title="更新承認" name="edit" onclick="location.href=\'%s?mode=upauth\'">更新承認</button>' % url)
        str_buffer.append('<button type="button" class="btn btn-sm btn-outline-secondary list_button" title="営業承認" name="edit" onclick="location.href=\'%s?mode=bzauth\'">営業承認</button>' % url)
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
            "all": ("bootstrap/css/mybootstrap.css", "admin/css/my.css")
        }
        js = ('bootstrap/js/bootstrap.min.js',)

