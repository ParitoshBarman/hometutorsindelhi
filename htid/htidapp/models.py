from django.db import models

# Create your models here.



class ContactMessage(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    msgTime = models.TimeField(auto_now_add=True)
    msgdate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.fullname