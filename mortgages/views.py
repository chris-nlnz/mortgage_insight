from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from mortgages.models import Mortgage


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {}


class MortgageListView(ListView):
    model = Mortgage
    context_object_name = 'mortgages'
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fancy stuff
        return context


class MortgageDetailView(DetailView):
    model = Mortgage
    context_object_name = 'mortgage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fancy stuff
        return context
