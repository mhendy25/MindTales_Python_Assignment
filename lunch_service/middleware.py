from django.urls import resolve
from django.http import JsonResponse

class VersionRoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        build_version = request.headers.get('build-version')
        # print(f"Build version: {build_version}")
        if build_version:
            if build_version.startswith('1.'):
                request.path_info = self.route_v1(request.path_info)
            else:
                request.path_info = self.route_v2(request.path_info)
        # print(f"Modified path: {request.path_info}")
        response = self.get_response(request)
        return response

    def route_v1(self, path):
        return path.replace('/menu/', '/menu1/')

    def route_v2(self, path):
        return path.replace('/menu/', '/menu2/')