from rest_framework import serializers
from .models import CheckList

class CheckListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'

