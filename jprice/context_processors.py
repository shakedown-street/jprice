def current_view(request):
    return {"current_view": request.resolver_match.view_name}
