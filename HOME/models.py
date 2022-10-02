from django.db import models

# Create your models here.


class Visa(models.Model):

    country_choices=[
        ('USA', 'USA'),
        ('China', 'China'),
        ('Russia', 'Russia'),
        ('Japan', 'Japan'),
        ('Autralia', 'Australia')
    ]

    job_choices=[
        ('Doctor', 'Doctor'),
        ('Teacher', 'Teacher'),
        ('Mechanic', 'Mechanic'),
        ('Plumber', 'Plumber'),
        ('Freelancer', 'Freelancer'),
        ('Developer', 'Developer'),
        ('Accountant', 'Accountant'),
        ('Carpenter', 'Carpenter'),
        ('Sporter', 'Sporter'),
        ('Unimployment', 'Haven\'t had yet')
    ]

    name=models.CharField(max_length=40)
    country=models.CharField(max_length=50,choices=country_choices)
    age=models.IntegerField()
    job=models.CharField(max_length=50, choices=job_choices, default='Unimployment')
    ip=models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.name}'
