from django.contrib import admin
from .models import Contact, CustomContactForm, GeneralSetting, SocialMediaLink, Footer, ContactUsPage, Card, Testimonial,LandingPage
from unfold.admin import ModelAdmin


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    pass

@admin.register(GeneralSetting)
class GeneralSettingAdmin(ModelAdmin):
    pass
   
@admin.register(CustomContactForm)
class CustomContactFormAdmin(ModelAdmin):
    pass

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(ModelAdmin):
    pass

@admin.register(Footer)
class FooterAdmin(ModelAdmin):
    pass

@admin.register(Card)
class CardAdmin(ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    pass

@admin.register(LandingPage)
class LandingPageAdmin(ModelAdmin):
    pass

@admin.register(ContactUsPage)
class ContactUsPageAdmin(ModelAdmin):
    pass

