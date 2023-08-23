from django.db import models 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13,blank=True, null=True) #while deploying remove null/blank constraint
    avatar = models.ImageField(null=True,default="avatar.png")
    #USERNAME_FIELD = 'email'

    # Add any additional fields or methods as needed

    def __str__(self):
        return self.username
class bcc_unit(models.Model):
    unitname = models.CharField(max_length=100)
    unitnumber = models.IntegerField()
    leaders = models.CharField(max_length=100)
    secretary = models.CharField(max_length=100)
    pastoral_minstry = models.CharField(max_length=100)
    education_minstry = models.CharField(max_length=100)
    social_action_minstry = models.CharField(max_length=100)
    family_minstry = models.CharField(max_length=100)
    laity_minstry = models.CharField(max_length=100)
    youth_minstry = models.CharField(max_length=100)

    def __str__(self):
        return str(self.unitnumber)



class family(models.Model):
    #number = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL,null=True, related_name='unit_numberfam')
    unitnumber = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL, null = True)
    familynumber = models.IntegerField()
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.familynumber)


class person(models.Model):
    #number = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL,null=True, related_name='unit_numberper')
    #family_number = models.ForeignKey(family,on_delete=models.SET_NULL,null=True, related_name='familyphone')
    #address = models.ForeignKey(family,on_delete=models.SET_NULL, null = True, related_name='familyaddress')
    familynumber = models.ForeignKey(family,on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100, blank=True ,null=True)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

class parishpreist(models.Model):
    priestname = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.priestname
    
class phoneno(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class parishcouncil(models.Model):
    name = models.CharField(max_length=100)
    desigination = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.desigination

