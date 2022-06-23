from email.policy import default
from django.db import models
class User(models.Model):
    username =models.CharField(max_length=100,default=' ')
    emailid =models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100,default=' ')
    location=models.CharField(max_length=100,default=' ')

class Client(models.Model):
    name=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    password=models.CharField(max_length=100,default=' ')
    phonenumber=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postalcode=models.CharField(max_length=100)

class Project(models.Model):
    projectname=models.CharField(max_length=100)
    projectdiscription=models.CharField(max_length=100)
    projecttechnology=models.CharField(max_length=100)

class Userproject(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)



