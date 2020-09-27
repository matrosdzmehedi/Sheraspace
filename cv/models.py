from django.db import models
from django.urls import reverse 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .utils import unique_slug_generator,calculate_age


class PersonCv(models.Model):

    Gen = [('Male', 'Male'), ('Female', 'Female')]
    Vibag=[('Barisal','Barisal'),('Chittagong','Chittagong'),('Dhaka','Dhaka'),('Khulna','Khulna'),('Mymensingh','Mymensingh'),('Rajshahi','Rajshahi'),('Rangpur','Rangpur'),('Sylhet','Sylhet')]


    name=models.CharField( max_length=50,blank=False)
    slug=models.SlugField(unique=True)
    dob=models.DateField( auto_now=False, auto_now_add=False)
    age=models.IntegerField(default=None)
    phone=models.CharField( max_length=50,blank=False)
    address=models.CharField( max_length=50,blank=False)
    institute=models.CharField( max_length=50,blank=False)
    ps_year=models.IntegerField(blank=False)
    f_name=models.CharField( max_length=50,blank=False)
    gender=models.CharField(max_length=20, choices=Gen)
    email=models.EmailField( max_length=50,blank=False)
    district=models.CharField(max_length=20, choices=Vibag)
    subject=models.CharField( max_length=50,blank=False)




    def save(self,*args, **kwargs):
        self.age=calculate_age(self.dob)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cv_details', kwargs={'slug': self.slug})



def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
	    instance.slug = unique_slug_generator(instance) 



pre_save.connect(pre_save_receiver, sender = PersonCv) 
