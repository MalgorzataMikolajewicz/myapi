from rest_framework import serializers


from .models import Map, Value

class MapGETSerializer(serializers.ModelSerializer):
    wartosc = serializers.CharField(source="value.wartosc")

    class Meta:
        model = Map
        fields = ["wartosc"]
    

class MapPOSTSerializer(serializers.ModelSerializer):
    value = serializers.SlugRelatedField(slug_field="value", queryset=Value.objects.all())

    class Meta:
        model = Map
        fields = ["value"]


class ValueGETSerializer(serializers.ModelSerializer):
    wartosc = serializers.SlugRelatedField(slug_field="wartosc", queryset=Value.objects.all())
    class Meta:
        model = Value
        fields = ["wartosc"]


class ValuePOSTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Value
        fields = "__all__"



