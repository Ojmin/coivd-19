from django.conf.urls import url
from .views import Sessions,Users
urlpatterns = [
    url(r'^session/', Sessions),
    url(r'^user/', Users),
]
