from django.db import models
from django.contrib.auth.models import User
RATINGS_TYPE=(
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
)
# Create your models here.
class HotelInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    hotel_image = models.ImageField(upload_to='hotel/media/uploads/',null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    
    
class Comment(models.Model):
    hotel=models.ForeignKey(HotelInfo,on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    ratings=models.CharField(max_length=10,choices=RATINGS_TYPE)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name