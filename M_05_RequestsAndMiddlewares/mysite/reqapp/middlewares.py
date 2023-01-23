from django.http import HttpRequest
from django.core.cache import cache
from django.shortcuts import render


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        limit_request_count = 20
        timeout_requests = 60
        response = self.get_response(request)
        ip_address = request.META.get("REMOTE_ADDR")
        count = cache.get_or_set('ip:{}'.format(ip_address), 0, timeout_requests)
        count += 1
        if count > limit_request_count:
            raise Exception(f'Превышена квота для запросов: '
                            f'{limit_request_count} запросов в '
                            f'{timeout_requests} сек')
        else:
            cache.set('ip:{}'.format(ip_address), count, timeout_requests)
        return response
