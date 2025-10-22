from django import forms


class MarkdownEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(MarkdownEditor, self).__init__(*args, **kwargs)
        self.attrs["class"] = "markdown-editor"

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/codemirror.css",
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/theme/monokai.css",
                "/static/utils/markdown-editor.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/codemirror.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/mode/markdown/markdown.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/mode/python/python.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.14/mode/javascript/javascript.js",
            "/static/utils/markdown-editor.js",
        )
