from django.http import HttpResponse,JsonResponse
from django.views import View

from utils.logger import logger
from .models import Info



class CoivdInfo(View):
    def get(self, request):
        info = Info.show_newest
        return JsonResponse(info)

    def post(self, request):
        ret = request.POST.get("ret")
        data = request.POST.get("data")
        print(ret)
        print(data)
        if  data is None:
            logger.info('缺少参数')
            return JsonResponse({'msg': '缺少参数'}, status=200)
        coivd = Info(ret=ret, data=data)
        coivd.save()
        return JsonResponse({'msg': 'ok'}, status=200)
