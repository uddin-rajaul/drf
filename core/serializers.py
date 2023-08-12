from rest_framework import serializers
from .models import CheckList, CheckListItem

class CheckListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'


class CheckListItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'
