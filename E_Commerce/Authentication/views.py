from .forms import *
from .utils import *
from Core.models import *
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import authenticate, login, get_user_model

# User = get_user_model()

class LoginRegisterView(View):
    template_name = 'registration/login.html'
    confirm_email_template = 'registration/confirm_email.html'
    def get_context_data(self):
        context = {}
        context['contact'] = Contact.objects.get()
        context['carousel'] = Carousel.objects.all()
        context['circle'] = Circle.objects.all()
        context['reg_form'] = CreateUserForm
        context['log_form'] = LoginUserForm
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        if 'register' in request.POST:
            context['reg_form'] = CreateUserForm(request.POST)
            if context['reg_form'].is_valid():
                global user
                user = context['reg_form'].save(commit=False)            
                send_email_for_verify(request, user)
                return render(request, self.confirm_email_template)
            return render(request, self.template_name, context)
            
            
        elif 'login' in request.POST:
            context['log_form'] = LoginUserForm(request.POST)
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username = email, password = password)
            remember_me = request.POST.get('remember_me', False)
            if user is not None:
                login(request,user)
                if remember_me:
                    request.session.set_expiry(2592000)
                return redirect('home')
            return render(request, self.template_name, context)

class EmailVerify(View):
    invalid_verify = 'registration/invalid_verify.html'

    # @staticmethod
    # def get_user(uidb64):
    #     try:
    #         uid = urlsafe_base64_decode(uidb64).decode()
    #         user = CustomUser.objects.get(pk=uid)
    #     except (TypeError, ValueError, OverflowError,
    #             CustomUser.DoesNotExist, ValidationError):
    #         user = None
    #     return user
    
    def get(self, request, uidb64, token):
        global user
        # user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, self.invalid_verify)

def Logout(request):
    logout(request)
    return redirect('home')