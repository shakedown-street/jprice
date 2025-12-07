from utils.views import pdf_response


def resume_pdf(request):
    disposition = "inline"
    filename = "jordan-price-resume.pdf"

    return pdf_response(
        request,
        "resume/resume.html",
        disposition=disposition,
        filename=filename,
    )
