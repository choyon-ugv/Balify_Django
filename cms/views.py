from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, GeneralSetting, SocialMediaLink, Footer, ContactUsPage, Card,Testimonial, LandingPage
from .serializers import ContactSerializer, CustomeContactFormSerializer, GeneralSettingSerializer, SocialMediaLinkSerializer, FooterSerializer, ContactUsPageSerializer, TestimonialSerializer, LandingPageSerializer, CardSerializer

class ContactView(APIView):
    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many= True)
        response = {
            "status": 200,
            "success": True,
            "message": "Contact add successfully",
            "data": serializer.data
        }
        return Response(response)
    
class CustomContactFormView(APIView):
    def post(self, request):
        serializer = CustomeContactFormSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": 201,
                "success": True,
                "message": "Contact created successfully",
                "data": serializer.data
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneralSettingView(APIView):
    def get(self, request): 
        settings = GeneralSetting.objects.all()
        serializer = GeneralSettingSerializer(settings, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "General settings fetched successfully",
            "data": serializer.data
        }
        return Response(response)


class SocialMediaLinkView(APIView):
    def get(self, request):
        social_media_links = SocialMediaLink.objects.all()
        serializer = SocialMediaLinkSerializer(social_media_links, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Social media links fetched successfully",
            "data": serializer.data
        }
        return Response(response)

    
class FooterView(APIView):
    def get(self, request):
        footer_data = Footer.objects.all()
        serializer = FooterSerializer(footer_data, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Footer fetched successfully",
            "data": serializer.data
        }
        return Response(response)
    
class ContactUsPageView(APIView):
    def get(self, request):
        contact_us_page = ContactUsPage.objects.all()
        serializer = ContactUsPageSerializer(contact_us_page, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Contact us page fetched successfully",
            "data": serializer.data
        }
        return Response(response)
    

# HOMEPAGE VIEW

class CardView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Cards fetched successfully",
            "data": serializer.data
        }
        return Response(response)
    
class TestimonialView(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Testimonials fetched successfully",
            "data": serializer.data
        }
        return Response(response)
    
class LandingPageView(APIView):
    def get(self, request):
        landing_page_data = LandingPage.objects.all()
        serializer = LandingPageSerializer(landing_page_data, many=True)
        response = {
            "status": 200,
            "success": True,
            "message": "Landing page fetched successfully",
            "data": serializer.data
        }
        return Response(response)