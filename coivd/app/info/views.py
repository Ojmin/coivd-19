from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Info
import json


class CoivdInfo(View):
    def get(self, request):
        info = Info.show_newest
        return JsonResponse(info)

    def post(self, request):
        info = json.loads(request.body)
        print(info)
        coivd = Info(ret=info['ret'], data=info['data'])
        coivd.save()
        return JsonResponse({'msg': 'ok'}, status=200)
