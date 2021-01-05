import random
import time
from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.contrib.auth import authenticate, login, logout
from coivd.app.user.models import User


class Sessions(View):
    def post(self, request):
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except Exception as e:
            return HttpResponse("参数错误！")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("登录成功！")
        else:
            return HttpResponse("登录失败！")
            # render(request,'login.html')

    def delete(self, request):
        logout(request)
        return HttpResponse("注销成功！")


class Users(View):
    @staticmethod
    def gen_name():
        salt = str(int(float((str(time.time())[7:])) * 1000000))
        return str(random.randrange(100000, 999999)) + salt

    def post(self, request):
        password = request.POST["password"]
        username = self.gen_name()
        user = User.objects.create_user(username, '', password)
        user.save()
        return HttpResponse("注册成功！{}".format(username))
