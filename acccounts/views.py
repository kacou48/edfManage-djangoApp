from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

#for sending email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader  import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError #force_text,
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, View

from .forms import UserRegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm

from .models import LesAbonnee 



class EmailThread(threading.Thread):
    
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()



def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'ACTIVATION DE COMPTE'
    email_body = render_to_string('accounts/activation.html',{
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
        })
    
    email=EmailMessage(subject=email_subject, body=email_body,
                 from_email=settings.EMAIL_HOST_USER,
                 to=[user.email]
                )
    EmailThread(email).start() # la classe qui envoie le mail.




User = get_user_model()

class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    
    def dispatch(self, request, *args, **kwargs): # rediriger vers blog si utilisateur connecté
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse_lazy('dashbord')
            )
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(self.request.POST)
        #print('id',profile_id)
        #print(registration_form)
        

        if registration_form.is_valid():
            print('it work!')
            user = registration_form.save()

            send_activation_email(user, request)

            
            #login(self.request, user)
            messages.success(
                self.request,
                (
                    f'Nous vous envoyons un e-mail pour verifier votre compte.'
                    
                )
            )


            #login(self.request, user)
            return HttpResponseRedirect(
                reverse_lazy('user_login')
            )

        return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                
            )
        )

    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
        
        return super().get_context_data(**kwargs)

"""
class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    redirect_authenticated_user = False

"""



class LoginPageView(View):
    template_name = 'accounts/user_login.html'
    form = LoginForm

    def get(self, request):
        form = self.form()
        #messages = ''
        return render(request, self.template_name,
                      context={'form':form}

        )

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password']   #verifie l'autentification...
            )

            
            if user is not None:
                if not user.is_email_verified:
                    messages.error(
                        self.request,
                        (
                            f"Cet Email n'est pas verifié, s'il vous plait consultez votre boite email."
                            
                        )
                    )
                    
                    return render(request, self.template_name, context={'form':form})


                login(request, user)
                if LesAbonnee.objects.filter(user=user).exists():
                    return redirect('list_formation')
                else:
                    return redirect('abonnement')
      
        messages.error(
                    self.request,
                    (
                        f"L'addresse mail ou le password est invalide."
                        
                    )
                )
        return render(request, self.template_name, context={'form':form})




def activate_user(request, uidb64, token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user=None

    if user and generate_token.check_token(user, token):
        user.is_email_verified=True
        user.save()
        messages.success(request, "Email verifié, vous pouvez vous connectez")
        return redirect(reverse_lazy('user_login'))

    return render(request, 'accounts/activate-failed.html', {'user': user})




class LogoutView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


@login_required
def dashbord(request):

    return render(request, 'accounts/dashbord.html')


@login_required
def myaccount(request):
    user = request.user
    #user.userprofile.status = 'inactif'
    #user.userprofile.save()
    #print(user) 
    
    return render(request, 'accounts/myaccount.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                             instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'votre compte a bien ete mis à jour')
            return redirect('myaccount')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        print(u_form)
        print('\n')
        print(p_form)
    return render(request, 'accounts/profile_update.html', locals())




