This post covers how to generate PDF documents with HTML and CSS in Django using [WeasyPrint](https://weasyprint.org/). You can use this technique to generate invoices, reports, resumes, or any other document that needs to be presented in a printable format. This is the exact method I use to generate my resume, and invoices for freelance work.

With this method, building PDFs is as simple as building a regular Django web page. You can leverage the full power of Django templates, static files, and CSS to create beautiful PDF documents and serve them as a regular Django view.

In this tutorial, I will assume you have a basic understanding of Django, including views, templates, static files, and URL routing.

---

## Implementation

### Setup

The installation method will depend on your operating system. Here I will be showing the installation method for Debian/Ubuntu. If you're using another OS, refer to the [WeasyPrint installation documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation).

On Debian/Ubuntu, you can install the required system packages with:

```bash
apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 libjpeg-dev libopenjp2-7-dev libffi-dev
```

Then install WeasyPrint using pip inside your virtual environment:

```bash
pip install weasyprint
```

### Generic PDF View

Now we can create a generic Django view that will render a Django template to a PDF using WeasyPrint. You can put this view in any of your Django apps, but I typically will put it in a `utils` app.

`utils/views.py`

```python
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML


def pdf_response(request, template, *args, **kwargs):
    context = kwargs.get("context", {})
    disposition = kwargs.get("disposition", "inline")
    filename = kwargs.get("filename", "output.pdf")

    html_template = get_template(template)
    rendered_html = html_template.render(context).encode(encoding="UTF-8")

    pdf_file = HTML(
        string=rendered_html, base_url=request.build_absolute_uri()
    ).write_pdf()
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = '{}; filename="{}"'.format(disposition, filename)

    return response

```

This view function takes a request, a template name, and optional context data. It renders the template to HTML, converts it to a PDF using WeasyPrint, and returns it as an HTTP response with the appropriate content type. You can specify the filename and whether the PDF should be displayed inline in the browser or downloaded as an attachment.

### Example Usage

Now that we have our generic PDF view, we can use it to create a specific PDF view for our application. As an example, lets create a simple invoice PDF view:

`invoices/views.py`

```python
from utils.views import pdf_response


def invoice_pdf(request):
    invoice_data = {
        "invoice_number": "INV-001",
        "date": "2024-01-01",
        "bill_to": "John Doe",
        "items": [
            {"description": "Web Design", "quantity": 1, "price": 500},
            {"description": "Hosting", "quantity": 12, "price": 10},
        ],
    }

    context = {
      "invoice": invoice_data,
    }

    return pdf_response(
        request,
        template="invoices/invoice.html",
        context=context,
        disposition="attachment",
        filename="invoice_INV-001.pdf",
    )
```

And add the URL route for the invoice PDF view:

`invoices/urls.py`

```python
path("invoice/", invoice_pdf, name="invoice_pdf"),
```

In this example, we define an `invoice_pdf` view that prepares some sample invoice data and calls the `pdf_response` function with the appropriate template and context.

Notice that we can pass context data to the PDF view just like a regular Django view. In the `invoices/invoice.html` template we can use standard Django template syntax to render the invoice data. We can also use static files to include CSS styles or images in the PDF.

`invoices/templates/invoices/invoice.html`

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Invoice {{ invoice.invoice_number }}</title>
    <link rel="stylesheet" href="{% static 'invoices/invoice.css' %}" />
  </head>
  <body>
    <h1>Invoice {{ invoice.invoice_number }}</h1>
    <p>Date: {{ invoice.date }}</p>
    <p>Bill To: {{ invoice.bill_to }}</p>
    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th>Quantity</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {% for item in invoice.items %}
        <tr>
          <td>{{ item.description }}</td>
          <td>{{ item.quantity }}</td>
          <td>${{ item.price }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>
```

The template uses Django's template language to dynamically insert invoice data. You can also create a CSS file to style the invoice

You can also control the page sizes, margins, and other print-specific styles using CSS `@page` rules. For example, you can add the following to your CSS file to set the page size to A4 and add margins:

```css
@page {
  size: A4;
  margin: 2rem;
}
```

Now when you navigate to `/invoice/` in your browser, it will generate and download a PDF invoice using the specified template and data.

## Common Issues & Debugging

There are some common issues you may encounter when generating PDFs with WeasyPrint:

- **CSS limitations**: There are some limitations to the CSS features supported by WeasyPrint, so be sure to check the [WeasyPrint documentation](https://doc.courtbouillon.org/weasyprint/stable/features.html#css-support) for details.
- **Fonts not displaying correctly**: Ensure that the fonts you are using in your CSS are accessible to WeasyPrint. You may need to use web-safe fonts or include font files in your static files.

Refer to the [WeasyPrint documentation](https://doc.courtbouillon.org/weasyprint/stable/index.html) for more troubleshooting tips, best practices, and advanced usage. There are also examples of other common use cases like adding headers/footers, page numbers, and more.

## Summary

With these steps, we covered how to generate PDF documents in Django using WeasyPrint. We created a generic PDF view that can render any Django template to a PDF, and demonstrated how to use it to create an invoice PDF. With this approach, you can leverage the full power of Django templates and CSS to create beautiful, printable documents for your application.
