# pages/views.py
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


def home_page_view(request):
    context = {
        "inventory_list": ["widget1", "widget2", "widget3"],
        "greetings": "Thank You For Visting",
    }
    return render(request, "home.html", context)


class about_page_view(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "1234567890"
        return context
