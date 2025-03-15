from rest_framework import serializers
from .models import Book, Author
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from datetime import date

def validate_publication_date(value):
    """
        Validates that the given publication date is not in the future.
    """
    if value > date.today():
        raise ValidationError('Publication date cannnot be in the future.')

class BookSerializer(serializers.ModelSerializer):
    """
        Serializer for Book Model.
        Converts Book model instances to and from JSON representations.
        Includes validation for the publication_date field
        Handles the relationship with the Author model.
    """    
    publication_date = serializers.DateField(validators=[validate_publication_date])
    class Meta:
        model = Book
        fields = '__all__'
        
        
class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model.
        Converts Author model instances to and from JSON representations.
    """
    class Meta:
        model = Author
        fields = '__name__'
