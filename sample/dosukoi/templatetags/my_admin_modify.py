from django import template
from django.template.context import Context

register = template.Library()

@register.inclusion_tag('admin/my_submit_line.html', takes_context=True)
def my_submit_row(context):
    """ 
    Display the row of buttons for delete and save.
    """
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    show_save = context.get('show_save', True)
    show_save_and_continue = context.get('show_save_and_continue', True)
    ctx = Context(context)
    ctx.update({
        'show_delete_link': (
            not is_popup and context['has_delete_permission'] and 
            change and context.get('show_delete', True)
        ),  
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': (
            context['has_add_permission'] and not is_popup and 
            (not save_as or context['add'])
        ),
        'show_save_and_continue': not is_popup and context['has_change_permission'] and show_save_and_continue,
        'show_save': show_save,
        'show_custom_button_1': context.get('can_custom1', False),
        'show_custom_button_2': context.get('can_custom2', False),
    })
    return ctx

