This post covers how to build a minimal markdown rendering solution in Django using the [Markdown](https://pypi.org/project/Markdown/) package, along with syntax highlighting using Prism.js and a CodeMirror field widget for editing markdown content. We will be building the exact solution used on this site for blog posts and project pages.

In this post, I will assume you have a working Django project and app already set up, and have basic understanding of Django models, forms, templates, static files, and template tags.

---

## Background / Concepts

Markdown is a lightweight markup language that allows you to write formatted text. It is widely used for writing documentation, blog posts, and other content on the web due to its simplicity and readability. While there are several third-party Django apps available for rendering markdown in Django projects, building your own solution can be beneficial to keep your implementation lightweight and customizable.

To implement markdown rendering in Django we will wrap the `markdown` Python package functionality in a template tag filter. This allows us to convert markdown content stored in our database into HTML when rendering templates. When storing content in a database model, we will store it in a plain old `TextField`. Additionally, we will enhance the user experience by adding syntax highlighting for code blocks using [Prism.js](https://prismjs.com/) and a [CodeMirror](https://codemirror.net/5/) widget for editing markdown content in forms.

## Implementation

Install `markdown` package:

```bash
pip install markdown
```

To store raw content in a database model, we can use a simple `TextField` in our Django model:

```python
from django.db import models


class Post(models.Model):
	content = models.TextField()
```

This is nice and simple, because we don't have to do anything special to store markdown content, just store it as plain text.

Now we'll want to create the template tag. You can put this in any of your Django apps, but I like to create a `utils` app for stuff like this. Create a folder called `templatetags` in your app directory, and add an empty `__init__.py` file to it. Then create a new file called `markdown.py`.

`utils/templatetags/markdown.py`

```python
import markdown as md
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return mark_safe(
        md.markdown(
            value,
            extensions=["markdown.extensions.fenced_code"],
        )
    )
```

We're registering a new template filter called `markdown` that takes a string input and converts it to HTML.

**Note**: The `markdown.extensions.fenced_code` enables support for fenced code blocks, allowing you to write code blocks in markdown using triple backticks (\`\`\`). Without this extension, only indented code blocks are supported.

In our template we can use the filter like so:

```html
<!-- Load the markdown filter -->
{% load markdown %}

<!--  Render markdown content -->
<div>{{post.content | markdown }}</div>
```

Just like that we have markdown rendering in our Django templates!

---

### Syntax Highlighting

To add syntax highlighting for code blocks. Download and include the [Prism.js](https://prismjs.com/download) CSS and JS files in your static files. You can chose the languages, themes and plugins you want to include. Additional themes can be found [here](https://github.com/PrismJS/prism-themes).

In your template, include the Prism CSS and JS files:

```html
{% load static %}

<link href="{% static '/path/to/prism.css' %}" rel="stylesheet" />
<script src="{% static '/path/to/prism.js' %}"></script>
```

You could put this in your base template so it's available site-wide, but I like to only put it on the pages that need it.

---

### CodeMirror Form Widget

**Note**: This section assumes you have jQuery available in your admin or form pages. If you don't, you can modify the JS code to use vanilla JS or another library of your choice.

How you want to edit markdown content on your site is up to you. You could use the regular `TextField` widget, or a third-party WYSIWYG editor, but I like to use CodeMirror for a nice code-editor-like experience.

In the same Django app that you put the template tag, create a new file called `widgets.py`.

`utils/widgets.py`

```python
from django import forms


class MarkdownEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(MarkdownEditor, self).__init__(*args, **kwargs)
        self.attrs["class"] = "markdown-editor"

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/codemirror.css",
                # You can choose any theme you like from CodeMirror themes
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/theme/monokai.css",
                "/static/utils/markdown-editor.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/codemirror.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/mode/markdown/markdown.js",
            # Add any modes you want to support in code blocks like so:
            # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/mode/python/python.js",
            "/static/utils/markdown-editor.js",
        )
```

This widget includes the necessary CSS and JS files for CodeMirror, and applies a `markdown-editor` class to the textarea.

Now create the CSS and JS files referenced in the widget and put them in your static files.

`utils/static/utils/markdown-editor.css`

```css
.CodeMirror {
  flex: 1;
  height: 400px;
}
```

`utils/static/utils/markdown-editor.js`

```javascript
(function () {
  var $ = django.jQuery;
  $(document).ready(function () {
    $('textarea.markdown-editor').each(function (idx, el) {
      CodeMirror.fromTextArea(el, {
        lineNumbers: true,
        lineWrapping: true,
        mode: 'markdown',
        theme: 'monokai',
      });
    });
  });
})();
```

This script initializes CodeMirror on any textarea with the `markdown-editor` class, which our widget adds automatically.

Now we can use the `MarkdownEditor` widget in our forms.

```python
from utils.widgets import MarkdownEditor


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': MarkdownEditor(),
        }
```

Or in the Django admin:

```python
from utils.widgets import MarkdownEditor


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': MarkdownEditor(),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
```

---

## Conclusion

With these steps, you now have a minimal markdown rendering solution in Django that includes syntax highlighting for code blocks and a nice editing experience with CodeMirror. This setup is lightweight, customizable, and can be easily extended to fit your specific needs.
