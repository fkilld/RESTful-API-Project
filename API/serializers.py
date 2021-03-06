from django.contrib.auth.models import User, Group
from rest_framework import serializers
from API.models import Item, CharityRegistration, UserRegistration, OrderedItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['ItemName','Charity','Quantity','Category']


class CharityLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'Password']


class CharityGetAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'CharityName', 'City']


class CharityRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'Password', 'CharityName', 'City']


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email', 'CharityName', 'City', 'UserName', 'Password']


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email', 'Password']

class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ['ItemID','OrderDate','ItemName','Quantity','UserName']