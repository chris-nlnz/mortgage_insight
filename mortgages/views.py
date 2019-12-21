from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from mortgages.models import Mortgage


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        return {}


class MortgageListView(LoginRequiredMixin, ListView):
    model = Mortgage
    context_object_name = 'mortgages'
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fancy stuff
        return context


class MortgageDetailView(LoginRequiredMixin, DetailView):
    model = Mortgage
    context_object_name = 'mortgage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fancy stuff
        return context
