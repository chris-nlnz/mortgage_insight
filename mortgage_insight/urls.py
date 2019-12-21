from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from mortgages.views import IndexView, MortgageListView, MortgageDetailView


urlpatterns = [
    path('admin/', admin.site.urls),

    # See https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
    # for good examples of how to extend / customise the Django auth flow
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', IndexView.as_view(), name='index'),
    path('mortgages/', MortgageListView.as_view(), name='mortgages-list'),
    re_path('mortgages/(?P<pk>[0-9A-Fa-f-]+)/', MortgageDetailView.as_view(), name='mortgages-detail'),
]
