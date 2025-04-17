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


def resume_pdf(request):
    disposition = "inline"
    filename = "jordan-price-resume.pdf"

    return pdf_response(
        request,
        "resume/resume.html",
        disposition=disposition,
        filename=filename,
    )


def new_resume_pdf(request):
    disposition = "inline"
    filename = "jordan-price-resume.pdf"

    return pdf_response(
        request,
        "resume/new_resume.html",
        disposition=disposition,
        filename=filename,
    )


def comprehensive_resume_pdf(request):
    disposition = "inline"
    filename = "jordan-price-resume.pdf"

    return pdf_response(
        request,
        "resume/comprehensive_resume.html",
        disposition=disposition,
        filename=filename,
    )
