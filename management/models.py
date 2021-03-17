from django.db import models

# Create your models here.
class Customer(models.Model):
    account_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,null=False)
    slug = models.CharField(max_length=20,null=False,unique=True)
    email = models.EmailField()
    current_balance = models.FloatField(max_length=10,default=0)

    def __str__(self):
        return self.name

    def register(self):
        self.save()
    
class TransectionHistory(models.Model):
    from_account = models.IntegerField(null=False)
    to_account = models.IntegerField(null=False)
    amount = models.FloatField(max_length=10,default=0)
    date_time = models.DateTimeField(auto_created=True)
     