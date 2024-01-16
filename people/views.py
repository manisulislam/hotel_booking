from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
from django.views import View
from .forms import UserRegistrationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token
import sweetify
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from hotel.models import Comment
from django.views.generic import UpdateView,DeleteView
from hotel.forms import CommentForm

# Create your views here.
class UserRegistrationView(View):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            birth_date=form.cleaned_data['birth_date']
            address=form.cleaned_data['address']
            phone_no=form.cleaned_data['phone_no']
            gender_type=form.cleaned_data['gender_type']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            
            # error handle korchi password,email, username
            if password1!=password2:
                sweetify.error(request, 'Passwords do not match')
                return redirect('register')
            if User.objects.filter(username=user_name).exists():
                sweetify.error(request, 'Username already exists')
                return redirect('register')
            # if User.objects.filter(email=email).exists():
            #     sweetify.error(request, 'Email already exists')
            #     return redirect('register')
                
            user=User.objects.create_user(
                username=user_name,
                email=email,
                password=password1,
                
            )
            account=UserAccount.objects.create(
                user=user,
                birth_date=birth_date,
                gender_type=gender_type,
                phone_no=phone_no,
                
            )
            user.is_active=False
            user.save()
            account.save()
            sweetify.success(request, 'Congratulations..Please,check your email for confirm email')
            
            # send confirmation email
            mail_subject='Confirmation Email'
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            token=generate_token.make_token(user)
            confirm_link=f"https://hotel-booking-nit2.onrender.com/people/active/{uid}/{token}"
            message=render_to_string('accounts/email_confirmations.html',{
                'first_name': first_name,
                'last_name': last_name,
                
                'confirm_link': confirm_link
            })
            to_email=email
            send_email=EmailMultiAlternatives(mail_subject,'',to=[to_email])
            send_email.attach_alternative(message,'text/html')
            send_email.send()
            
           
           
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
    
def activate(request,uid64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        sweetify.success(request, 'Account activated successfully')
        return redirect('login')
    else:
        sweetify.error(request, 'Invalid activation link')
        return redirect('register')
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)
    
    def get_success_url(self) :
        sweetify.success(self.request, 'You Logged In Successfully', icon='success')
        
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):   
    
    def get_success_url(self) :
        sweetify.success(self.request, 'You Logged Out Successfully', icon='success')
        
        return reverse_lazy('home')
class ProfileView(View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        user=request.user
        data=Comment.objects.filter(user=user)
        
        return render(request, self.template_name,{"data":data})
    
class editView(UpdateView):
    model=Comment
    form_class=CommentForm
    template_name="book_review.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
    
class deleteView(DeleteView):
    model=Comment
    template_name="accounts/delete.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
    