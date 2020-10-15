from rest_framework import serializers
from app.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('personid','name','mobile','email','description')