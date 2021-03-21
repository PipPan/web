from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'home/home.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'
