from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Giữ lại các query params hiện có và thay đổi 1 số key, ví dụ:
    {% url_replace sort='price_asc' %}
    """
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        if value is None:
            query.pop(key, None)
        else:
            query[key] = value
    query_string = query.urlencode()
    return '?' + query_string if query_string else ''
