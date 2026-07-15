from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings

class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Join 10,000+ visionary innovators using our cutting-edge, AI-powered platform!"
        return context

    def form_valid(self, form):
        
        response = super().form_valid(form)

        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
            messages.info(
                self.request,
                "We've sent you an email to verify your account. Please check your inbox."
            )
        else:
            messages.success(
                self.request,
                f"Welcome {form.cleaned_data['first_name']}! Your account has been created."
            )
    
        return response

def index(request):
    return render(request, 'core/index.html')

@login_required
def secret(request):
    return render(request, 'core/secret.html')
