from django.conf import settings


def app_version(request):
    try:
        return {'app_version': settings.APP_VERSION}
    except AttributeError:
        return {'app_version': ''}
