from rest_framework import fields, serializers
from api.models import *
import imghdr
from django.core.files.base import ContentFile
import base64
import six
import uuid


class Base64ImageField(serializers.ImageField):
    """
    Based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    """

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class PlayerSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Player
        fields = ["id", "name", "last_name","birthday","position","shirt_number","is_titular","team", "photo"]


class TeamSerializer(serializers.ModelSerializer):
    flag = Base64ImageField(max_length=None, use_url=True)
    shell = Base64ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Team
        fields = ["id", "name", "flag", "shell"]


class CouchingStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouchingStaff
        fields = ["id", "name", "last_name", "birthday", "birth_country", "rol", "team"]

