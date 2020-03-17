from rest_framework import serializers


class BbSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    price = serializers.FloatField()
    published = serializers.DateTimeField()
    image = serializers.ImageField()


class RubricSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
