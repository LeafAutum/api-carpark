from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Carpark(models.Model):

    title=models.CharField(max_length=15,unique=True)
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.title

class Slotsall(models.Model):
       #parkorli=models.ForeignKey(Carpark, null=True, blank=True,on_delete=models.CASCADE)
       slot = models.OneToOneField(Carpark , blank =True,on_delete=models.CASCADE)
       totalslots = models.PositiveIntegerField(default=20,validators = [MinValueValidator(1),MaxValueValidator(20)])
       slotno = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(20)],unique=True)
       updated =models.DateTimeField(auto_now_add=True)
       status = models.BooleanField(default=False)
       def __str__(self):
        return str(self.slotno)+" "+ str(self.slot)
