from django.shortcuts import render,redirect
from django.views import View
import sweetify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transaction
from .forms import TransactionForm


class DepositMoneyView(LoginRequiredMixin,View):
    form_class = TransactionForm
    template_name = 'transactions/deposit_form.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form=TransactionForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            user=request.user
            user.account.balance+=amount
            print(user.account.balance)
            user.account.save(
                update_fields=['balance',]
            )
            sweetify.success(request, 'Deposit Successful', icon='success')
            
            
            return redirect('home')





   