from rest_framework import serializers
from .models import CheckList, CheckListItem


class CheckListItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'


class CheckListSerializers(serializers.ModelSerializer):
    items = CheckListItemSerializers(source='checklistitem_set', many=True, read_only = True)
    class Meta:
        model = CheckList
        fields = '__all__'
