from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    return {'login_form': AuthenticationForm()}

#con este archivo haremos que se pueda hacer login globalmente desde cualquier pahgina