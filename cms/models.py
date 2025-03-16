from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField



# contact page
class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class CustomContactForm(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    message = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GeneralSetting(models.Model):
    brand_name = models.CharField(max_length=255, blank=True)
    brand_logo = CloudinaryField('image', null=True, blank=True)
    # brand_email = models.EmailField(max_length=255, blank=True)
    # brand_phone = models.CharField(max_length=255, blank=True)
    # brand_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.brand_name

class SocialMediaLink(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    icon = CloudinaryField('icon', null=True, blank=True)
    def __str__(self):
        return self.name    

class Footer(models.Model):
    brand = models.ManyToManyField(GeneralSetting, related_name="footer")
    about_text = models.TextField()
    social_media_links = models.ManyToManyField(SocialMediaLink, related_name="footer")
    location = models.CharField(max_length=255, blank=True, null=True)  
    location_icon = CloudinaryField('location_icon', null=True, blank=True)
    copyright_text = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"Footer"

    
    
class ContactUsPage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    background_image = CloudinaryField('background_image', null=True, blank=True)
    contact_title = models.CharField(max_length=255)
    contact_info = models.ManyToManyField(Contact, related_name='contact')
    contact_form = models.ManyToManyField(CustomContactForm, related_name='contact')
    footer = models.ManyToManyField(Footer, related_name='contact')

    def __str__(self):
        return self.title



# Home page

class Card(models.Model):
    title = models.CharField(max_length=255, blank=True)
    card_content = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    discription = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)
    rating = models.PositiveIntegerField(default=5)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} - Rating: {self.rating}"
    
class LandingPage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.CharField(max_length=255, blank=True)
    background_image = CloudinaryField('background_image', null=True, blank=True)
    card = models. ManyToManyField(Card, related_name='card')
    testimonial = models.ManyToManyField(Testimonial, related_name='testimonial')

    def __str__(self):
        return self.hero_title