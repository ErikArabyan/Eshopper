from django.shortcuts import render, redirect
from django.views.generic import View
from Core.models import *
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout, authenticate

class LoginRegisterView(View):
    template_name = 'login.html'
    confirm_email = 'confirm_email.html'
    def get(self, request):
        context = {}
        context['contact'] = Contact.objects.get()
        context['carousel'] = Carousel.objects.all()
        context['circle'] = Circle.objects.all()
        context['reg_form'] = CreateUserForm
        context['log_form'] = LoginUserForm
        return render(request, self.template_name, context)
    
    def post(self, request):
        if 'register' in request.POST:
            reg_form = CreateUserForm(request.POST)
            if reg_form.is_valid():
                user = reg_form.save(commit=False)            
                current_site = get_current_site(request)
                context = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token_generator.make_token(user),
                }
                message = render_to_string('verify_email.html',context=context,)
                email = EmailMessage(
                    'Veryfi email',
                    message,
                    to=[user.email],
                )
                email.send()
                return render(request, self.confirm_email)
            
        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username = email, password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
            message = 'Email or Password are wrong'