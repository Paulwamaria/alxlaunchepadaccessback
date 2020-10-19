from django.shortcuts import render
from djoser import email

# Create your views here.


def index(request):
    """The view will expose the homepage endpoint."""
    title = "Alpdaccessor"
    greet = "Welcome to Alxlpdaccessor API home page."
    context = {
        "title": title,
        "greet": greet,
    }
    return render(request, 'accounts/index.html', context)


class ActivationEmail(email.ActivationEmail):
    template_name = 'email/activation.html'


class AccountReset(email.PasswordResetEmail):
    template_name = 'email/resetPass.html'


class ConfirmActivation(email.ConfirmationEmail):
    template_name = 'email/confirmation.html'
