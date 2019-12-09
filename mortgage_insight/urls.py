from django.contrib import admin
from django.urls import path

from mortgages.views import IndexView, MortgageListView, MortgageDetailView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('mortgages/', MortgageListView.as_view(), name='mortgages-list'),
    path('mortgages/<int:pk>/', MortgageDetailView.as_view(), name='mortgages-detail'),
]
