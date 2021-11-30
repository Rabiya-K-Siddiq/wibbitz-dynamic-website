from django.db import models

class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Clients(models.Model):
    logo = models.FileField(upload_to='clients/')

    def __str__(self):
        return self.logo.url

class Feature(models.Model):
    image = models.ImageField(upload_to='features/')
    icon = models.FileField(upload_to='features/')
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to='features/')

    def __str__(self):
        return self.title
    

