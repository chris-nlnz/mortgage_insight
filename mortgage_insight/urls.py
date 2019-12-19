from django.contrib import admin
from django.urls import path, re_path

from mortgages.views import IndexView, MortgageListView, MortgageDetailView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('mortgages/', MortgageListView.as_view(), name='mortgages-list'),
    re_path('mortgages/(?P<pk>[0-9A-Fa-f-]+)/', MortgageDetailView.as_view(), name='mortgages-detail'),
]
