from django.conf.urls import url
from football import views

urlpatterns = [
    url(r'^$',views.base,name="base"),
]
