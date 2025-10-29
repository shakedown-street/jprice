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


def old_resume_pdf(request):
    disposition = "inline"
    filename = "jordan-price-resume.pdf"

    return pdf_response(
        request,
        "resume/old_resume.html",
        disposition=disposition,
        filename=filename,
    )
