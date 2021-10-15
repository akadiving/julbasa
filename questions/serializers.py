from django.db import models
from rest_framework import serializers
from .models import Category, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """
    A serializer class for Answers
    """
    class Meta:
        model = Answer
        fields = ["body", "right_answer", "image"]

class QuestionSerializer(serializers.ModelSerializer):
    """
    A serializer class for Questions
    """
    choices = AnswerSerializer(many=True, source="choice")
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = ["id", "category", "author", "body", "difficulty", "created_at", "choices",]

    def create(self, validated_data):
        choices = validated_data.pop('choice')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Answer.objects.create(question=question, **choice)
        return question

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choice')
        choices = (instance.choice).all()
        choices = list(choices)
        instance.author = validated_data.get('author', instance.author)
        instance.body = validated_data.get('body', instance.body)
        instance.difficulty = validated_data.get('difficulty', instance.difficulty)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()

        for choice_data in choices_data:
            choice = choices.pop(0)
            choice.body = choice_data.get('body', choice.body)
            choice.right_answer = choice_data.get('right_answer', choice.right_answer)
            choice.image = choice_data.get('image', choice.image)
            choice.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    """
    A serializer class for Cateogories
    """
    class Meta:
        model = Category
        fields = "__all__"