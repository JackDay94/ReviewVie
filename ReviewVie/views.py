from django.shortcuts import render

"""
Custom error pages for 404 and 500 errors.
From:
https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317
"""


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def internal_server_error_view(request, *args, **argv):
    return render(request, "500.html", status=500)


def permission_denied_view(request, exception):
    return render(request, "403.html", status=403)
