from django.db import models

class Contactus(models.Model):
    Name = models.CharField(max_length=122,blank=True,null=True)
    Email = models.EmailField(max_length=122,unique=False)
    Comment = models.CharField(max_length=300,null=True)
    Date = models.DateField()

    def __str__(self):
        return f"{self.Name}({self.Date})"
