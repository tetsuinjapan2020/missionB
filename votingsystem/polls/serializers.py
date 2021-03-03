from rest_framework import serializers
from polls.models import Question, Choice

#class QuestionSerializer(serializers.ModelSerializer):
class QuestionListPageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    #pub_date = serializers.DateTimeField()
    #was_published_recently = serializers.BooleanField(read_only=True)
    
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    choice_text = serializers.CharField(max_length=200)
    def create(self, validated_data):
        return Choice.objects.create(**validated_data)
    class Meta:
        model = Choice
        #fields = '__all__'
        fields = ('id', 'choice_text')

class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()

class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')

class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('question_text', 'choices')

