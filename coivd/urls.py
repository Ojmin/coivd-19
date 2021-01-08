
from django.urls import path

from coivd.app.info.views import CoivdInfo

urlpatterns = [
    path('coivd_info', CoivdInfo.as_view()),
]
