from django.db import models
from people.models import UserAccount

TRANSACTION_TYPE=(
    ('DEPOSIT','DEPOSIT'),
)
# Create your models here.
class Transaction(models.Model):
    account=models.ForeignKey(UserAccount,related_name="transactions",on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    transaction_type=models.CharField(max_length=10,choices=TRANSACTION_TYPE)
    balance_after_transactions=models.DecimalField(max_digits=12,decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering=['timestamp']