from rest_framework import serializers
from .models import DeveloperProfileModel, DeveloperProfileModel


class DeveloperProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperProfileModel
        fields = '__all__'

    read_only_fields = ('id', 'date_joined', 'date_updated') 
    extra_kwargs = {
        'password': {'read_only': True},}

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfileModel
        fields = '__all__'

    read_only_fields = ('id', 'date_joined', 'date_updated') 
    extra_kwargs = {
        'password': {'read_only': True},}       