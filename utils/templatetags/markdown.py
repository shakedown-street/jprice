from io import StringIO

import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


md.Markdown.output_formats["plain"] = unmark_element
unmark = md.Markdown(output_format="plain")
unmark.stripTopLevelTags = False


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])


@register.filter()
@stringfilter
def unmarkdown(value):
    return unmark.convert(value)
