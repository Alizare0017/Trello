from rest_framework import serializers
from .models import Workspace, Membership, Board


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.visiblity = validated_data.get('visiblity', instance.visiblity)
        instance.save()
        return instance