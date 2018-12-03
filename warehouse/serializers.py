from .models import *
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'store_num', 'location', 'purchase_date',
                  'purchase_price')


class PresentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Present
        fields = ('id', 'name', 'introduction', 'on_date', 'status',
                  'cost', 'hot', 'off', 'off_cost', 'pdepot', 'category')
