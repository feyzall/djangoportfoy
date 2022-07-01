from pyexpat import model
from unicodedata import category, name
from django.db import models


class Experience(models.Model):
    name=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    descripson=models.TextField(max_length=500)
    bolum=models.CharField(max_length=200, default='')
    def __str__(self):
        return self.name

class Menu(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(upload_to="course/%Y/%m/%d")
    subname=models.CharField(max_length=200, default='')
    def __str__(self):
        return self.name

class Social(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(upload_to="course/%Y/%m/%d")
    link= models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class About(models.Model):
    jop=models.CharField(max_length=200)
    birtday=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    dagree=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    freelance=models.BooleanField(default=True)

class Skilss(models.Model):
    name=models.CharField(max_length=200)
    desdrip=models.TextField(max_length=2000, default='')
    yuz=models.CharField(max_length=3, default='')
    def __str__(self):
        return self.name


class Education(models.Model):
    name=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    descripson=models.TextField(max_length=500)
    bolum=models.CharField(max_length=200, default='')
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="course/%Y/%m/%d")
    category=models.CharField(max_length=200 , default='')
    client=models.CharField(max_length=200, default='')
    projectdt=models.CharField(max_length=200, default='')
    url=models.CharField(max_length=200, default='')
    def __str__(self):
        return self.name


class Testimonials(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    def __str__(self):
        return self.name

