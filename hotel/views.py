from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import HotelInfo
from django.shortcuts import get_object_or_404
from .models import HotelInfo
import sweetify
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import CommentForm
from hotel.models import Comment
# Create your views here.
class HotelDetailView(DetailView):
    model = HotelInfo
    template_name = 'hotel_detail.html'
   
    def get(self, request, *args, **kwargs):
        hotel=get_object_or_404(HotelInfo, pk=kwargs['pk'])
        hotel_comment=Comment.objects.filter(hotel=hotel)
        context={
            'hotel':hotel,
            'hotel_comment':hotel_comment,
            
        }
        return render(request, self.template_name, context)
    
    
        
        
        
def Book_Hotel(request, id):
    hotel = get_object_or_404(HotelInfo, pk=id)
    hotel_price = hotel.price

    user_balance = request.user.account.balance

    if user_balance >= hotel_price:
        request.user.account.balance -= hotel_price
        request.user.account.save(update_fields=['balance'])
        sweetify.success(request, 'Hotel Booked Successfully.Please,Check your email.', icon='success')
        
        mail_subject = 'Hotel Booked Confirmation Email'
        message = render_to_string('book_hotel_mail.html', {
                    'user': request.user,
                    'price': hotel_price,
                    'hotel': hotel
                })
        to_email = request.user.email
        send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()
        return redirect('profile')
    else:
        sweetify.error(request, 'Insufficient Balance.Please,deposit some amount to your account to book the hotel.', icon='error')
        return redirect('home')
    
    
def Book_Review(request, id):
    hotel = get_object_or_404(HotelInfo, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.hotel = hotel
            comment.user = request.user
            comment.save()
            sweetify.success(request, 'Review Submitted Successfully.', icon='success')
            return redirect('profile')
    else:
        form = CommentForm()
    return render(request, 'book_review.html', {'form': form})