from rest_framework.serializers import ModelSerializer

from restapp.models import user


class userserializer(ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'