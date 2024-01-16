from django.db import models
from django.contrib.auth.models import User
GENDER_TYPE=(
    ('Male','Male'),
    ('Female','Female'),
    
)
# Create your models here.
class UserAccount(models.Model):
    user=models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    birth_date=models.DateTimeField(null=True, blank=True)
    gender_type=models.CharField(max_length=10,choices=GENDER_TYPE,default='Male')
    address=models.TextField(null=True, blank=True)
    phone_no=models.IntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    
    def __str__(self):
        return self.user.username