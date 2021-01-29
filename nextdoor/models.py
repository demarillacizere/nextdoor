 
from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=40)
    pop_count=

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profiles/',default='default.jpeg')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    bio= models.CharField(max_length=250)
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name


class Business(models.Model):
    name=models.CharField(max_length=40)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    contacts=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=40,null=True)
    


    def __str__(self):
        return self.name

class Authority(models.Model):
    name=models.CharField(max_length=40)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    contacts=models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name=models.CharField(max_length=40)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    contacts=models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    title=models.CharField(max_length=40)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    alert=models.CharField(max_length=300, null=True)
    date_posted = models.DateTimeField(auto_now_add= True,null=True)


    def __str__(self):
        return self.title
