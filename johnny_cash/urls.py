from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^cash/$", "johnny_cash.views.cash", name="cash")
]
