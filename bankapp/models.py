from django.db import models
 
# Create your models here.
class Customers(models.Model):
    
    account_no = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    phno = models.CharField(max_length=10)
    balance = models.IntegerField()
     
    def __str__(self):
        return self.name +'----'+ self.account_no

class Transactions(models.Model):
    
    sender = models.CharField(max_length=10)
    receiver = models.CharField(max_length=10)
    amount = models.IntegerField()
     
    def __str__(self):
        return self.sender +'----'+ self.receiver
