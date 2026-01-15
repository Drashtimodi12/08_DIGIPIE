from rest_framework import serializers
from API_Library.models import *

# ------------------------------------------
# Author
# ------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# ------------------------------------------
# Publication
# ------------------------------------------
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


# ------------------------------------------
# Book
# ------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        # depth = 1       # This is allow nested serialization for related fields. optional (automatic nesting)

    def to_representation(self, instance):
    # This method is called when serializer converts a model object into JSON (serializer.data)

        representation = super().to_representation(instance)
        # Calls parent ModelSerializer method Converts normal fields (id, title, price, author_id, publication_id)
        # into a basic dictionary

        representation['author'] = AuthorSerializer(instance.author).data
        # Replace author ID with full author object Uses AuthorSerializer to show nested author details

        representation['publication'] = PublicationSerializer(instance.publication).data
        # Replace publication ID with full publication object Uses PublicationSerializer to show nested publication details

        return representation
        # Return final customized JSON response
