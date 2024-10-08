from django.shortcuts import render
from django.views.generic import View
from Core.models import *

class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        context = {}
        context['contact'] = Contact.objects.get()
        context['carousel'] = Carousel.objects.all()
        context['circle'] = Circle.objects.all()
        return render(request, self.template_name, context)