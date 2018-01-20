from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView
from .models import DeliveryType
from .forms import LetterForm


class LetterListView(TemplateView):
    template_name = "delivery_letter/type_list.html"

    def get_context_data(self, **kwargs):
        kwargs['delivery_type_list'] = DeliveryType.objects.all()
        return  super().get_context_data(**kwargs)


class LetterFormView(FormView):
    template_name = 'delivery_letter/delivery.html'
    success_url = '/'
    form_class = LetterForm

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
