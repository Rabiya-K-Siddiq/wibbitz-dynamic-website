from django.db import models


COMPANY_SIZE = (
    ('1', '1-10'),
    ('2', '11-50'),
    ('3', '51-200'),
    ('4', '201-500'),
)


INDUSTRY_TYPE = (
    ('agriculture', 'Agriculture'),
    ('banking & finance', 'Banking & Finance'),
    ('business services & software', 'Business services & Software'),
)


JOB_ROLE = (
    ('c-suite', 'C-Suite'),
    ('vp', 'VP'),
)


COUNTRY_CHOICE = (
    ('united states', 'united states'),
    ('india', 'india'),
    ('afganistan', 'afganistan'),
    ('america', 'america'),
    ('albania', 'albania'),
)


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
    

class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255, choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128, choices=INDUSTRY_TYPE)
    job_role = models.CharField(max_length=128, choices=JOB_ROLE)
    country = models.CharField(max_length=128, choices=COUNTRY_CHOICE)
    privacy_policy = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.first_name

