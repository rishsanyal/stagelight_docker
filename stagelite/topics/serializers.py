from rest_framework import serializers

from .models import Votes, BaseTopicModel, Topic, UserSubmission, \
    Competitions


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseTopicModel


class VotesSerializer(BaseSerializer):
    class Meta:
        model = Votes
        fields = '__all__'


class TopicSerializer(BaseSerializer):
    votes = VotesSerializer
    title = serializers.CharField(max_length=300, trim_whitespace=True)

    class Meta:
        model = Topic
        fields = '__all__'

    def validate(self, data):
        return data

    def create(self, validated_data):
        topic = Topic.objects.create(**validated_data)
        return topic


class UserSubmissionSerializer(BaseSerializer):
    topic = TopicSerializer
    # user = CurrentUserSerializer
    votes = VotesSerializer
    submission_entry = serializers.CharField()

    class Meta:
        model = UserSubmission
        fields = '__all__'


class CompetitionSerializer(BaseSerializer):
    votes = VotesSerializer

    class Meta:
        model = Competitions
        fields = '__all__'
