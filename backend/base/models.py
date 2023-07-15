from django.db import models 

class bcc_unit(models.Model):
    unitnumber = models.CharField(max_length=2)
    leaders = models.CharField(max_length=100)
    secretary = models.CharField(max_length=100)
    pastoral_minstry = models.CharField(max_length=100)
    education_minstry = models.CharField(max_length=100)
    socialaction_minstry = models.CharField(max_length=100)
    family_minstry = models.CharField(max_length=100)
    laity_minstry = models.CharField(max_length=100)
    youth_minstry = models.CharField(max_length=100)

    def __str__(self):
        return self.unitnumber



class family(models.Model):
    #number = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL,null=True, related_name='unit_numberfam')
    unitnumber = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL, null = True)
    familynumber = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.familynumber


class person(models.Model):
    #number = models.ForeignKey(bcc_unit,on_delete=models.SET_NULL,null=True, related_name='unit_numberper')
    #family_number = models.ForeignKey(family,on_delete=models.SET_NULL,null=True, related_name='familyphone')
    #address = models.ForeignKey(family,on_delete=models.SET_NULL, null = True, related_name='familyaddress')
    familynumber = models.ForeignKey(family,on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100, blank=True ,null=True)

    
