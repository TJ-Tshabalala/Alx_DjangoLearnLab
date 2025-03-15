from rest_framework import serializers
from .models import Book, Author
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from datetime import date

class BookSerializerValidation(serializers.ValidationError):

    def validate_publication_date(value):
        """
        Validates that the given publication date is not in the future.
    """
        if value > date.today():
            raise ValidationError('Publication date cannnot be in the future.')

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True) # type: ignore
    """
        Serializer for Book Model.
        Converts Book model instances to and from JSON representations.
        Includes validation for the publication_date field
        Handles the relationship with the Author model.
    """    
    publication_date = serializers.DateField(validators=[publication_date])
    class Meta:
        model = Book
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model.
        Converts Author model instances to and from JSON representations.
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__name__'
