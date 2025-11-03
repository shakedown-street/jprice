def current_view(request):
    resolver_match = getattr(request, "resolver_match", None)
    view_name = getattr(resolver_match, "view_name", None)

    return {"current_view": view_name}
