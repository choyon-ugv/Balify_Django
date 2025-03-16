from django.urls import path
from . views import ContactView, CustomContactFormView, GeneralSettingView, SocialMediaLinkView, FooterView, ContactUsPageView, CardView, TestimonialView, LandingPageView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('custom-contact/', CustomContactFormView.as_view(), name='custom_contact'),
    path('general-setting/', GeneralSettingView.as_view(), name='general_setting'),
    path('social-media-link/', SocialMediaLinkView.as_view(), name='social_media_link'),
    path('footer/', FooterView.as_view(), name='footer'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact_us_page'),
    path('card/', CardView.as_view(), name='card'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('landing-page/', LandingPageView.as_view(), name='landing_page'),
]