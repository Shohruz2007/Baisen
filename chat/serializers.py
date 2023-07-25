from .models import GroupConversation, PrivateConversation, GroupMessage, PrivateMessage
from rest_framework import serializers

from user.serializers import UserBaseInfoSerializer

class PrivateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateMessage
        fields = '__all__'

class GroupMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupMessage
        exclude = ('conversation_id',)

class GroupConversationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupConversation
        fields = '__all__'


class PrivateConversationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateConversation
        fields = '__all__'


class GroupConversationSerializer(serializers.ModelSerializer):
    initiator = UserBaseInfoSerializer()

    class Meta:
        model = GroupConversation
        fields = '__all__'

class PrivateConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateConversation
        fields = '__all__'