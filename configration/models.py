from django.db import models

# Create your models here.
class UserR(models.Model):
    first_name = models.CharField(max_length=50)
    list_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=False,blank=False)
    password = models.CharField(max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    def __str__(self):
        return self.first_name+self.list_name
