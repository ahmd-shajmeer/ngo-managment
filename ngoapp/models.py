from django.db import models

from django.contrib.auth.models import User


    # Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class ngo_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    oname= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    address= models.CharField(max_length=50)  
    licence= models.ImageField(null=True)   

class user_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=50)
    address= models.CharField(max_length=50)  
    idproof= models.ImageField(null=True)   
    photo= models.ImageField(null=True)  

class project(models.Model):
    ngo= models.ForeignKey(ngo_reg,on_delete=models.CASCADE)
    pname=models.CharField(max_length=150)
    pdes= models.CharField(max_length=1000)
    amount= models.CharField(max_length=150) 
    photo= models.ImageField(null=True)    





class udonation(models.Model):
    reg = models.ForeignKey(user_reg,on_delete=models.CASCADE)
    ngo= models.ForeignKey(ngo_reg,on_delete=models.CASCADE)
    project=models.ForeignKey(project,on_delete=models.CASCADE,null=True)
    amt= models.CharField(max_length=150)
    amount= models.IntegerField(max_length=50)  
    status=models.CharField(max_length=150,null=True)


class assigneddonation(models.Model):
    project= models.ForeignKey(project,on_delete=models.CASCADE)
    donation= models.ForeignKey(udonation,on_delete=models.CASCADE)
    ngo= models.ForeignKey(ngo_reg,on_delete=models.CASCADE)
    amount= models.CharField(max_length=150) 
    

class expenditure(models.Model):
    project= models.ForeignKey(project,on_delete=models.CASCADE)
    etype= models.CharField(max_length=150) 
    amount= models.CharField(max_length=150) 
    edes= models.CharField(max_length=1500) 
    bill=models.ImageField(null=True) 


