import logging
import traceback
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import logout
import datetime
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)


def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

    except:
        ip = ''
    return ip


def get_user_name(request):
    try:
        return request.user.username
    except:
        return 'no-username'



class error500Middleware(object):
    def process_exception(self, request, exception):
        logger.exception(
            ' sheljar.middleware.error500Middleware' +
            ' userlogin:' + get_user_name(request) +
            ' ip:' + get_client_ip(request) +
            ' uri:' + request.build_absolute_uri() +
            ' exception: ' + str(exception) +
            ' traceback' + str(traceback.format_exc())
        )
        return None


class log_requests_Middleware(object):
    def process_request(self, request):
        try:
            logger.debug(
                ' session_key:' + request.session.session_key +
                ' uri:' + request.build_absolute_uri() +
                ' ip:' + get_client_ip(request) +
                ' userlogin:' + get_user_name(request)
            )
        except:
            pass
        return None


class RemoveWWWMiddleware(MiddlewareMixin):
    """
    Based on the REMOVE_WWW setting, this middleware removes "www." from the
    start of any URLs.
    """
    def process_request(self, request):
        host = request.get_host()
        if settings.REMOVE_WWW and host and host.startswith('www.'):
            redirect_url = '%s://%s%s' % (
                request.scheme, host[4:], request.get_full_path()
            )
            return HttpResponsePermanentRedirect(redirect_url)