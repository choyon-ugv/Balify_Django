from rest_framework import serializers
from . models import Contact, CustomContactForm, GeneralSetting, SocialMediaLink, Footer, ContactUsPage, Card, Testimonial, LandingPage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CustomeContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomContactForm
        fields = '__all__' 

class GeneralSettingSerializer(serializers.ModelSerializer):
    brand_logo = serializers.SerializerMethodField()
    
    class Meta:
        model = GeneralSetting
        fields = '__all__'
        
    def get_brand_logo(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.brand_logo:
            return obj.brand_logo.build_url(width=500, height=500, crop="fill")
        return None

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = SocialMediaLink
        fields = [
            'name',
            'url',
            'icon_url',
        ]
    
    def get_icon_url(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.icon:
            return obj.icon.build_url(width=500, height=500, crop="fill")
        return None

class FooterSerializer(serializers.ModelSerializer):
    brand = GeneralSettingSerializer(many=True)  # Explicit serialization
    social_media_links = SocialMediaLinkSerializer(many=True)
    location_icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Footer
        fields = [
            'brand',
            'about_text',
            'location',
            'location_icon_url',
            'social_media_links',
            'copyright_text'
        ]
        
    def get_location_icon_url(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.location_icon:
            return obj.location_icon.build_url(width=500, height=500, crop="fill")
        return None
    

# ContactUsPage page serial

class ContactUsPageSerializer(serializers.ModelSerializer):
    contact_info = ContactSerializer(many=True)
    contact_form = CustomeContactFormSerializer(many=True)
    footer = FooterSerializer(many=True)
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ContactUsPage
        fields = [
            'title',
            'image_url',
            'contact_title',
            'contact_info',
            'contact_form',
            'footer'
        ]
        
    def get_image_url(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.background_image:
            return obj.background_image.url if obj.background_image else None


# Homepage serialization

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Testimonial
        fields = [
            'discription',
            'image_url',
            'name',
            'rating'
        ]
        
    def get_image_url(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.image:
            return obj.image.url if obj.image else None

class LandingPageSerializer(serializers.ModelSerializer):
    background_image_url = serializers.SerializerMethodField()
    card = CardSerializer(read_only=True,many=True)
    testimonial = TestimonialSerializer(many=True)
    
    class Meta:
        model = LandingPage
        fields = [
            'hero_title',
            'hero_subtitle',
            'background_image_url',
            'card',
            'testimonial'
        ]

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     # add card to data, many to many relationship
    #     data['card'] = CardSerializer(instance.card.all(), many=True).data
    #     # add testimonial to data, many to many relationship
    #     data['testimonial'] = TestimonialSerializer(instance.testimonial.all(), many=True).data
    #     return data
    def get_background_image_url(self, obj):
        # Apply transformations (e.g., resize to 500x500)
        if obj.background_image:
            return obj.background_image.url if obj.background_image else None