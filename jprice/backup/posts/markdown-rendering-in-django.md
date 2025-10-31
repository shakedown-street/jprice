When you need to render markdown in Django you might think to reach for [django-markdown](https://pypi.org/project/django-markdown/), which is fine, I'm not knocking it, but we can create our own minimal solution very easily. This solution works great because you don't need to install a Django app. In this guide I'll show you how to use the [Markdown](https://pypi.org/project/Markdown/) package with a simple template tag wrapper, create a field widget using [CodeMirror](https://codemirror.net/5/), and implement syntax highlighting using [Prism.js](https://prismjs.com/).

---

Install `markdown` package:

```bash
pip install markdown
```

Store raw content in a regular `TextField`

```python
from django.db import models


class Post(models.Model):
	content = models.TextField()
```

Next we'll want to create a markdown template tag in any of your installed Django apps. For this I usually create an app called `utils`.

`utils/templatetags/markdown.py`

```python
import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])
```

**Note**: The `markdown.extensions.fenced_code` enables support for fenced code blocks, allowing you to write code blocks in markdown using triple backticks (\`\`\`). Without this extension, only indented code blocks are supported by default.

We can now use this template tag in our Django templates:

```html
{% load markdown %}
<div>{{post.content | markdown | safe}}</div>
```

You could stop here and already have basic markdown rendering, it's that easy. However, we can take this a step further and implement dead simple syntax highlighting and create a field widget to make writing markdown in our forms and admin forms easier than a regular textarea.

---

Implementing syntax highlighting

---

Creating CodeMirror widget
