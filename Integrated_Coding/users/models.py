from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    # educational details
    institute=models.CharField(default='Silicon Institute of Technology', max_length=50)
    yop=models.CharField(default='2023', max_length=4)
    programme=models.CharField(default='B.Tech', max_length=10)
    cgpa=models.FloatField(default=9.00)

    # personal details
    fullname=models.CharField(default='user', max_length=25)
    gender=models.CharField(default='male', max_length=15)
    city=models.CharField(default='Bhubaneswar', max_length=20)
    state=models.CharField(default='Odisha', max_length=20)
    contact=models.CharField(default='789456321', max_length=10)   

    def __str__(self):
        return f'{self.user.username} Profile'
