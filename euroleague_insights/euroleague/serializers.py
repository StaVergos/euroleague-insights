from rest_framework import serializers


class ClubSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=255)
    alias = serializers.CharField(max_length=100)
    country_code = serializers.CharField(max_length=3)
    country_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)


class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField(max_length=10)
    fullname = serializers.CharField(max_length=50)
    passport_name = serializers.CharField(max_length=50)
    passport_surname = serializers.CharField(max_length=50)
    jersey_name = serializers.CharField(max_length=50)
    country_code = serializers.CharField(max_length=3)
    country_name = serializers.CharField(max_length=100)
    height = serializers.IntegerField()
    weight = serializers.IntegerField()
    birth_date = serializers.DateTimeField()
