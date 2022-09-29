from django.db import models
from django.db.models.fields.files import FileField, ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 




class job (models.Model):
    username=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000,null=True)
    company=models.CharField(max_length=1000,null=True)
    location=models.CharField(max_length=1000,null=True)
    email=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    jobs=models.CharField(max_length=1000)
    category=models.CharField(max_length=1000,null=True)
    job_time=models.CharField(max_length=1000,null=True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class wishlist (models.Model):
    username=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000,null=True)
    company=models.CharField(max_length=1000,null=True)
    location=models.CharField(max_length=1000,null=True)
    email=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    jobs=models.CharField(max_length=1000)
    category=models.CharField(max_length=1000,null=True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class all_cv (models.Model):
    username=models.CharField(max_length=1000,null=True)
    name=models.CharField(max_length=1000,null=True)
    cv=FileField(upload_to = 'cv/',null=True)


    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class edit_profile_model (models.Model):
    username=models.CharField(max_length=1000)
    phone=models.CharField(max_length=1000,null=True)
    address=models.CharField(max_length=1000,null=True)
    previous_job=models.CharField(max_length=1000,null=True)
    your_field_of_job=models.CharField(max_length=1000)

    def __str__(self):
        if len(self.username)>50:
            return self.username[:50]+"..."
        return self.username

class edit_profile_picture (models.Model):
    username=models.CharField(max_length=1000)
    profile_picture=ImageField(upload_to = 'profile_picture/')

    def __str__(self):
        if len(self.username)>50:
            return self.username[:50]+"..."
        return self.username

class apply_for_job (models.Model):
    username=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    post_id=models.IntegerField(max_length=1000)
    title=models.CharField(max_length=1000,null=True)
    phone=models.CharField(max_length=1000,null=True)
    email=models.CharField(max_length=1000,null=True)
    education=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)



    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name